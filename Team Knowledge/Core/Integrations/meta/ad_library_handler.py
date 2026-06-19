#!/opt/n8n/venv/bin/python3
"""
ad_library_handler.py — Meta Ad Library API handler voor Remy (Product Intelligence)

Ondersteunt Remy's wekelijkse product discovery voor Tricolarae (US fashion dropshipping).

Gebruik als module:
  from ad_library_handler import MetaAdLibrary
  lib = MetaAdLibrary()

  # Zoek actieve ads op keyword
  ads = lib.search_ads(["oversized blazer", "linen set"])

  # EU data (rijker door DSA wetgeving)
  ads_eu = lib.search_ads_eu(["summer dress"])

  # Alle ads van een specifieke adverteerder
  ads = lib.get_page_ads("FashionNova")

  # Filter op minimaal 14 dagen actief (scaling bewijs)
  scaling = lib.ads_active_since(ads, days=14)

  # Extraheer product-signalen
  signals = lib.extract_products(scaling)

  # Volledige weekly research sessie
  lib.weekly_research_report(
      keywords_list=["oversized blazer", "linen co-ord", "summer maxi dress"],
      output_path="/tmp/weekly_research.md"
  )

Vereisten:
  - META_ACCESS_TOKEN met ads_read scope in meta/.env
  - Python: /opt/n8n/venv/bin/python3
  - Rate limit: 200 calls/uur (automatische backoff bij 429/613)
"""

import os
import sys
import re
from datetime import datetime, timedelta, timezone
from typing import Optional

from connection import _read_env, _api_get, _paginate, _API_BASE, _EU_COUNTRIES

# ---------------------------------------------------------------------------
# Configuratie
# ---------------------------------------------------------------------------

_ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')

# Prijspatroon voor extract_products
_PRICE_PATTERN = re.compile(
    r'\$\s?\d+(?:[.,]\d{1,2})?'           # $29.99
    r'|\d+(?:[.,]\d{1,2})?\s?(?:USD|EUR)'  # 29.99 USD
    r'|\d+%\s?off'                          # 30% off
    r'|\bfree shipping\b',                  # free shipping
    re.IGNORECASE
)

# Product-categorie signaalwoorden voor US fashion dropshipping
_CATEGORY_SIGNALS = {
    "tops": ["top", "blouse", "shirt", "crop", "tee", "bodysuit", "tank"],
    "bottoms": ["jeans", "pants", "trousers", "skirt", "shorts", "legging"],
    "dresses": ["dress", "midi", "maxi", "mini", "gown", "romper", "jumpsuit"],
    "outerwear": ["jacket", "coat", "blazer", "cardigan", "hoodie", "sweatshirt"],
    "sets": ["set", "co-ord", "coord", "matching set", "two piece", "two-piece"],
    "accessories": ["bag", "purse", "belt", "hat", "scarf", "jewelry", "earring"],
    "shoes": ["shoe", "heel", "boot", "sandal", "sneaker", "mule", "pump"],
    "swimwear": ["bikini", "swimsuit", "swimwear", "bathing suit", "one-piece"],
}


# ---------------------------------------------------------------------------
# MetaAdLibrary klasse
# ---------------------------------------------------------------------------

class MetaAdLibrary:
    """
    Meta Ad Library API client voor Remy's product discovery.

    Authenticatie: META_ACCESS_TOKEN uit meta/.env (vereist ads_read scope).
    """

    def __init__(self):
        env = _read_env(_ENV_FILE)

        self._token = env.get("META_ACCESS_TOKEN", "").strip()
        self._api_version = env.get("META_API_VERSION", "v21.0").strip()

        if not self._token:
            print(f"ERROR: META_ACCESS_TOKEN niet gevonden in {_ENV_FILE}")
            print("Zet META_ACCESS_TOKEN in Team Knowledge/Core/Integrations/meta/.env")
            sys.exit(1)

        self._base_url = f"{_API_BASE}/{self._api_version}/ads_archive"
        self._base_params = {
            "access_token": self._token,
            "fields": "id,page_name,ad_creative_bodies,ad_creative_link_titles,ad_snapshot_url,publisher_platforms,impressions,ad_delivery_start_time",
        }

    # -----------------------------------------------------------------------
    # 1. search_ads — US markt
    # -----------------------------------------------------------------------

    def search_ads(self, keywords: list[str], country: str = "US", limit: int = 50) -> list[dict]:
        """
        Zoek actieve ads op keyword(s) in een specifiek land.

        Args:
            keywords: Lijst van zoektermen (bijv. ["oversized blazer", "linen set"])
            country:  ISO-landcode (default "US")
            limit:    Max aantal resultaten (default 50)

        Returns:
            Lijst van ad-dicts met id, page_name, ad_creative_bodies,
            ad_snapshot_url, impressions, ad_delivery_start_time.
        """
        results = []
        seen_ids = set()

        for keyword in keywords:
            print(f"  [search_ads] keyword='{keyword}' country={country}")
            params = {
                **self._base_params,
                "search_terms": keyword,
                "ad_reached_countries": country,
                "ad_active_status": "ACTIVE",
                "ad_type": "ALL",
            }
            ads = _paginate(self._base_url, params, limit)
            for ad in ads:
                if ad.get("id") not in seen_ids:
                    ad["_search_keyword"] = keyword
                    ad["_search_country"] = country
                    results.append(ad)
                    seen_ids.add(ad["id"])

        return results

    # -----------------------------------------------------------------------
    # 2. search_ads_eu — EU markt (rijkere data via DSA-wetgeving)
    # -----------------------------------------------------------------------

    def search_ads_eu(self, keywords: list[str], limit: int = 50) -> list[dict]:
        """
        Zoek actieve ads op keyword(s) in EU landen (NL, GB, DE).

        EU DSA-wetgeving verplicht adverteerders meer data te delen,
        waardoor impressie-data en targeting-info rijker zijn dan in de US.

        Args:
            keywords: Lijst van zoektermen
            limit:    Max resultaten per land

        Returns:
            Gecombineerde lijst van ads uit NL, GB en DE (deduplicatie op id).
        """
        results = []
        seen_ids = set()

        for country in _EU_COUNTRIES:
            country_ads = self.search_ads(keywords, country=country, limit=limit)
            for ad in country_ads:
                if ad.get("id") not in seen_ids:
                    seen_ids.add(ad["id"])
                    results.append(ad)

        return results

    # -----------------------------------------------------------------------
    # 3. get_page_ads — alle actieve ads van een specifieke adverteerder
    # -----------------------------------------------------------------------

    def get_page_ads(self, page_name: str, country: str = "US", limit: int = 50) -> list[dict]:
        """
        Haal alle actieve ads op van een specifieke Facebook Page/adverteerder.

        Args:
            page_name: Naam van de Facebook Page (bijv. "FashionNova")
            country:   ISO-landcode (default "US")
            limit:     Max aantal resultaten

        Returns:
            Lijst van ad-dicts voor deze adverteerder.
        """
        print(f"  [get_page_ads] page='{page_name}' country={country}")
        params = {
            **self._base_params,
            "search_page_ids": page_name,  # werkt ook als zoekterm op page name
            "search_terms": page_name,
            "ad_reached_countries": country,
            "ad_active_status": "ACTIVE",
            "ad_type": "ALL",
        }
        # Meta Ad Library zoekt op page_name via search_terms wanneer geen numeriek id
        # Verfijn: filter op page_name match achteraf voor nauwkeurigheid
        ads = _paginate(self._base_url, params, limit * 2)
        filtered = [
            ad for ad in ads
            if page_name.lower() in (ad.get("page_name") or "").lower()
        ]
        return filtered[:limit]

    # -----------------------------------------------------------------------
    # 4. ads_active_since — filter op minimumduur
    # -----------------------------------------------------------------------

    def ads_active_since(self, ads: list[dict], days: int = 14) -> list[dict]:
        """
        Filter ads die minimaal `days` dagen actief zijn.

        Een ad die al 14+ dagen loopt, toont scaling-intentie van de adverteerder —
        niet alleen testing. Dit is een sterk winning-product signaal.

        Args:
            ads:  Lijst van ad-dicts (output van search_ads of get_page_ads)
            days: Minimumdagen actief (default 14)

        Returns:
            Gefilterde lijst van ads ouder dan `days` dagen.
        """
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)
        result = []

        for ad in ads:
            start_raw = ad.get("ad_delivery_start_time")
            if not start_raw:
                continue
            try:
                # Meta levert ISO 8601 format: "2024-03-15T00:00:00+0000"
                start_dt = datetime.fromisoformat(start_raw.replace("+0000", "+00:00"))
                if start_dt <= cutoff:
                    ad["_days_active"] = (datetime.now(timezone.utc) - start_dt).days
                    result.append(ad)
            except (ValueError, TypeError):
                continue

        return result

    # -----------------------------------------------------------------------
    # 5. extract_products — product-signalen uit ad copy
    # -----------------------------------------------------------------------

    def extract_products(self, ads: list[dict]) -> list[dict]:
        """
        Extraheer product-signalen uit ad copy (ad_creative_bodies).

        Detecteert:
        - Prijsaanduidingen ($29.99, 30% off, free shipping)
        - Product-categorieën (dresses, tops, sets, etc.)
        - Dominante keywords per ad

        Args:
            ads: Lijst van ad-dicts

        Returns:
            Lijst van dicts met originele ad data + product-signalen:
            _prices, _categories, _keywords.
        """
        enriched = []

        for ad in ads:
            bodies = ad.get("ad_creative_bodies") or []
            if isinstance(bodies, str):
                bodies = [bodies]
            full_text = " ".join(bodies).lower()

            # Prijssignalen
            prices = _PRICE_PATTERN.findall(full_text)

            # Categorieën
            detected_cats = []
            for category, signals in _CATEGORY_SIGNALS.items():
                if any(sig in full_text for sig in signals):
                    detected_cats.append(category)

            # Keywords (woorden 4+ tekens, geen stopwoorden)
            stopwords = {"this", "that", "with", "your", "from", "have", "will",
                         "shop", "free", "now", "get", "our", "sale", "new"}
            words = re.findall(r'\b[a-z]{4,}\b', full_text)
            freq: dict[str, int] = {}
            for w in words:
                if w not in stopwords:
                    freq[w] = freq.get(w, 0) + 1
            top_keywords = sorted(freq, key=lambda k: freq[k], reverse=True)[:10]

            enriched_ad = dict(ad)
            enriched_ad["_prices"] = prices
            enriched_ad["_categories"] = detected_cats
            enriched_ad["_keywords"] = top_keywords
            enriched.append(enriched_ad)

        return enriched

    # -----------------------------------------------------------------------
    # 6. weekly_research_report — volledige research sessie
    # -----------------------------------------------------------------------

    def weekly_research_report(
        self,
        keywords_list: list[str],
        output_path: str,
        min_days_active: int = 14,
    ) -> str:
        """
        Draait een volledige wekelijkse product research sessie voor Tricolarae.

        Stappen:
        1. Zoek op alle keywords (US + EU)
        2. Filter op minimaal `min_days_active` dagen actief
        3. Extraheer product-signalen
        4. Groepeer per categorie
        5. Schrijf Markdown rapport naar output_path

        Args:
            keywords_list:    Lijst van zoektermen voor deze sessie
            output_path:      Pad voor het Markdown-rapport
            min_days_active:  Minimumdagen actief om als scaling te tellen (default 14)

        Returns:
            Pad naar het geschreven rapport.
        """
        run_date = datetime.now().strftime("%Y-%m-%d")
        print(f"\n[weekly_research_report] Start — {run_date}")
        print(f"  Keywords: {keywords_list}")
        print(f"  Min. actief: {min_days_active} dagen")

        # Stap 1: Zoeken
        print("\n[1/4] Zoeken op keywords (US)...")
        us_ads = self.search_ads(keywords_list, country="US", limit=50)
        print(f"  → {len(us_ads)} US ads gevonden")

        print("\n[2/4] Zoeken op keywords (EU: NL, GB, DE)...")
        eu_ads = self.search_ads_eu(keywords_list, limit=30)
        print(f"  → {len(eu_ads)} EU ads gevonden")

        # Dedupliceer US + EU op id
        all_ads_by_id: dict[str, dict] = {}
        for ad in us_ads + eu_ads:
            all_ads_by_id[ad["id"]] = ad
        all_ads = list(all_ads_by_id.values())
        print(f"  → {len(all_ads)} unieke ads totaal")

        # Stap 2: Filter op actief-duur
        print(f"\n[3/4] Filteren op {min_days_active}+ dagen actief...")
        scaling_ads = self.ads_active_since(all_ads, days=min_days_active)
        print(f"  → {len(scaling_ads)} scaling ads (bewijs van winstgevendheid)")

        # Stap 3: Extraheer signalen
        print("\n[4/4] Extraheren product-signalen...")
        enriched = self.extract_products(scaling_ads)

        # Stap 4: Groepeer per categorie
        by_category: dict[str, list[dict]] = {}
        uncategorized = []
        for ad in enriched:
            cats = ad.get("_categories", [])
            if cats:
                for cat in cats:
                    by_category.setdefault(cat, []).append(ad)
            else:
                uncategorized.append(ad)

        # Stap 5: Schrijf Markdown rapport
        lines = [
            f"# Weekly Product Research — {run_date}",
            f"",
            f"**Store:** Tricolarae (US fashion dropshipping)",
            f"**Keywords onderzocht:** {', '.join(keywords_list)}",
            f"**Totaal ads gevonden:** {len(all_ads)}",
            f"**Scaling ads ({min_days_active}+ dagen actief):** {len(scaling_ads)}",
            f"",
            f"---",
            f"",
        ]

        # Samenvatting per categorie
        lines.append("## Categorie-overzicht\n")
        lines.append("| Categorie | Ads | Top keywords |")
        lines.append("|-----------|-----|-------------|")
        for cat, cat_ads in sorted(by_category.items(), key=lambda x: -len(x[1])):
            # Top keywords over alle ads in categorie
            kw_freq: dict[str, int] = {}
            for a in cat_ads:
                for kw in a.get("_keywords", []):
                    kw_freq[kw] = kw_freq.get(kw, 0) + 1
            top_kws = sorted(kw_freq, key=lambda k: kw_freq[k], reverse=True)[:5]
            lines.append(f"| {cat} | {len(cat_ads)} | {', '.join(top_kws)} |")
        if uncategorized:
            lines.append(f"| (overig) | {len(uncategorized)} | -- |")
        lines.append("")

        # Detail per categorie
        for cat, cat_ads in sorted(by_category.items(), key=lambda x: -len(x[1])):
            lines.append(f"## {cat.title()}\n")

            # Sorteer op langst actief
            sorted_ads = sorted(cat_ads, key=lambda a: a.get("_days_active", 0), reverse=True)

            for ad in sorted_ads[:10]:  # max 10 per categorie
                page = ad.get("page_name", "Onbekend")
                days = ad.get("_days_active", "?")
                snapshot = ad.get("ad_snapshot_url", "")
                prices = ad.get("_prices", [])
                keywords = ad.get("_keywords", [])[:5]
                bodies = ad.get("ad_creative_bodies") or []
                headlines = ad.get("ad_creative_link_titles") or []
                platforms = ad.get("publisher_platforms") or []
                copy_preview = (bodies[0] if bodies else "")[:120]

                lines.append(f"### {page}")
                lines.append(f"- **Actief:** {days} dagen")
                if snapshot:
                    lines.append(f"- **Ad:** [Bekijk ad]({snapshot})")
                if platforms:
                    lines.append(f"- **Platform:** {', '.join(platforms)}")
                if headlines:
                    lines.append(f"- **Headline:** _{headlines[0]}_")
                if prices:
                    lines.append(f"- **Prijs-signalen:** {', '.join(prices[:5])}")
                if keywords:
                    lines.append(f"- **Keywords:** {', '.join(keywords)}")
                if copy_preview:
                    lines.append(f"- **Ad copy:** _{copy_preview}..._")
                lines.append("")

        if uncategorized:
            lines.append("## Overig (niet gecategoriseerd)\n")
            for ad in uncategorized[:5]:
                page = ad.get("page_name", "Onbekend")
                days = ad.get("_days_active", "?")
                lines.append(f"- **{page}** ({days} dagen actief)")
            lines.append("")

        # Footer
        lines.extend([
            "---",
            f"",
            f"*Gegenereerd op {datetime.now().strftime('%Y-%m-%d %H:%M')} door ad_library_handler.py*",
            f"*Data bronnen: Meta Ad Library API (US + EU DSA)*",
        ])

        report_content = "\n".join(lines)

        # Zorg dat output directory bestaat
        output_dir = os.path.dirname(os.path.abspath(output_path))
        os.makedirs(output_dir, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report_content)

        print(f"\nRapport geschreven naar: {output_path}")
        print(f"  {len(scaling_ads)} scaling ads | {len(by_category)} categorieen")
        return output_path


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Meta Ad Library — smoke test")
    print(f"Env bestand: {_ENV_FILE}")
    print("-" * 60)

    lib = MetaAdLibrary()
    print(f"Token geladen: {lib._token[:20]}...")
    print(f"API versie: {lib._api_version}")
    print(f"Basis URL: {lib._base_url}")
    print("")

    # Test 1: API bereikbaarheid — zoek op een breed fashion keyword
    print("[1] API bereikbaarheid — search 'summer dress' (US, limit=5):")
    try:
        ads = lib.search_ads(["summer dress"], country="US", limit=5)
        print(f"  OK — {len(ads)} ads ontvangen")
        if ads:
            first = ads[0]
            print(f"  Eerste ad: page='{first.get('page_name')}' | id={first.get('id')}")
            print(f"  Start: {first.get('ad_delivery_start_time')}")
    except RuntimeError as e:
        print(f"  FOUT: {e}")
        sys.exit(1)

    # Test 2: ads_active_since filter
    print("\n[2] Filter op 14+ dagen actief:")
    if ads:
        scaling = lib.ads_active_since(ads, days=14)
        print(f"  {len(ads)} ads → {len(scaling)} scaling ads (14+ dagen)")
    else:
        print("  Geen ads om te filteren.")

    # Test 3: EU search
    print("\n[3] EU search — 'linen set' (NL/GB/DE, limit=3 per land):")
    try:
        eu_ads = lib.search_ads_eu(["linen set"], limit=3)
        print(f"  OK — {len(eu_ads)} unieke EU ads ontvangen")
    except RuntimeError as e:
        print(f"  FOUT: {e}")

    # Test 4: extract_products op de gevonden ads
    print("\n[4] extract_products:")
    if ads:
        enriched = lib.extract_products(ads[:3])
        for i, a in enumerate(enriched, 1):
            print(f"  Ad {i}: categories={a.get('_categories')} | prices={a.get('_prices')[:3]}")
    else:
        print("  Geen ads voor enrichment.")

    # Test 5: weekly_research_report (kleine test run)
    print("\n[5] weekly_research_report (mini — 2 keywords, /tmp output):")
    try:
        report_path = lib.weekly_research_report(
            keywords_list=["oversized blazer", "summer maxi dress"],
            output_path="/tmp/meta_ad_library_test_report.md",
            min_days_active=7,
        )
        # Toon eerste 20 regels van het rapport
        with open(report_path) as f:
            preview = f.readlines()[:20]
        print("  Rapport preview (eerste 20 regels):")
        for line in preview:
            print(f"    {line}", end="")
    except RuntimeError as e:
        print(f"  FOUT bij rapport genereren: {e}")

    print("\n" + "-" * 60)
    print("Smoke test voltooid.")
    print("")
    print("Scope-check:")
    print("  Als alle tests slaagden → token heeft voldoende ads_read scope.")
    print("  Bij HTTP 400 met 'ads_read' melding → token vernieuwen via")
    print("  developers.facebook.com/tools/explorer (vink 'ads_read' aan).")
