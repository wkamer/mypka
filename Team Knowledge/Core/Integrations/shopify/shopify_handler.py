#!/opt/n8n/venv/bin/python3
"""
shopify_handler.py — Shopify Admin API handler voor Sasha

Gebruikt de officiële ShopifyAPI Python library (Shopify's eigen library).
Authenticatie via connection.py (client credentials grant).

Vereisten:
  - SHOPIFY_CLIENT_ID en SHOPIFY_CLIENT_SECRET in shopify/.env
  - Library geïnstalleerd in /opt/n8n/venv (ShopifyAPI==12.7.0)
  - Python: /opt/n8n/venv/bin/python3
  - App geïnstalleerd op de store vanuit het Dev Dashboard

Gebruik als module:
  from shopify_handler import ShopifyClient
  client = ShopifyClient()

  # Lezen
  products = client.products(first=10)
  page = client.page(handle="faq")

  # Schrijven (dry_run=True is de default — veilig)
  client.update_page(page_id="123", body_html="<p>Nieuw</p>")          # toont plan, voert NIET uit
  client.update_page(page_id="123", body_html="<p>Nieuw</p>", dry_run=False)  # voert uit na bevestiging

Gebruik als script (smoke test):
  python3 shopify_handler.py
"""

import json
import sys
import urllib.error

from connection import STORE, API_VERSION, _get_token


# --- ShopifyClient ----------------------------------------------------------

class ShopifyClient:
    """
    Officiële ShopifyAPI library wrapper met Sasha's veiligheidsprotocol:
    - dry_run=True op alle schrijfoperaties (default)
    - Pre-change summary altijd tonen vóór executie
    - Rate limit retry ingebouwd (429 → backoff)
    - Nooit een mutation zonder expliciete dry_run=False
    """

    def __init__(self):
        try:
            import shopify
        except ImportError:
            print("ERROR: ShopifyAPI library niet gevonden.")
            print("Installeer via: /opt/n8n/venv/bin/pip install ShopifyAPI")
            sys.exit(1)

        import time
        self._shopify = shopify
        self._time = time
        self._token = _get_token()
        self._session = shopify.Session(STORE, API_VERSION, self._token)
        shopify.ShopifyResource.activate_session(self._session)

    # --- Lezen: REST --------------------------------------------------------

    def shop_info(self) -> dict:
        """Retourneert basisinformatie over de store."""
        shop = self._shopify.Shop.current()
        return {"name": shop.name, "domain": shop.domain, "email": shop.email}

    def products(self, first: int = 10, status: str = "any") -> list:
        """Retourneert producten. Status: 'active' | 'draft' | 'archived' | 'any'."""
        products = self._shopify.Product.find(limit=first, status=status)
        return [
            {
                "id": p.id,
                "title": p.title,
                "handle": p.handle,
                "status": p.status,
                "variants_count": len(p.variants),
                "images_count": len(p.images),
                "body_html_length": len(p.body_html or ""),
            }
            for p in products
        ]

    def product(self, product_id: str) -> dict:
        """Retourneert volledig product inclusief body, images en varianten."""
        p = self._shopify.Product.find(product_id)
        return {
            "id": p.id,
            "title": p.title,
            "handle": p.handle,
            "status": p.status,
            "body_html": p.body_html,
            "variants": [{"id": v.id, "title": v.title, "price": v.price, "sku": v.sku} for v in p.variants],
            "images": [{"id": i.id, "src": i.src, "alt": i.alt} for i in p.images],
        }

    def pages(self) -> list:
        """Retourneert alle store-pagina's."""
        pages = self._shopify.Page.find()
        return [
            {
                "id": p.id,
                "title": p.title,
                "handle": p.handle,
                "template_suffix": getattr(p, "template_suffix", ""),
                "body_html_length": len(p.body_html or ""),
            }
            for p in pages
        ]

    def page(self, handle: str = None, page_id: str = None) -> dict:
        """Retourneert volledige pagina inclusief body_html en template."""
        if handle:
            results = self._shopify.Page.find(handle=handle)
            if not results:
                raise ValueError(f"Pagina met handle '{handle}' niet gevonden.")
            p = results[0]
        elif page_id:
            p = self._shopify.Page.find(page_id)
        else:
            raise ValueError("Geef handle of page_id op.")

        metafields = self._shopify.Metafield.find(resource="pages", resource_id=p.id)

        return {
            "id": p.id,
            "title": p.title,
            "handle": p.handle,
            "template_suffix": getattr(p, "template_suffix", ""),
            "body_html": p.body_html,
            "metafields": [{"namespace": m.namespace, "key": m.key, "value": m.value} for m in metafields],
        }

    def themes(self) -> list:
        """Retourneert alle thema's — markeert het actieve thema."""
        themes = self._shopify.Theme.find()
        return [
            {
                "id": t.id,
                "name": t.name,
                "role": t.role,  # 'main' = actief thema
            }
            for t in themes
        ]

    def theme_asset(self, theme_id: str, asset_key: str) -> str:
        """Retourneert de inhoud van een thema-asset (bijv. templates/page.faq.json)."""
        asset = self._shopify.Asset.find(asset_key, theme_id=theme_id)
        return asset.value

    def orders(self, first: int = 10, status: str = "open") -> list:
        """Retourneert orders. Status: 'open' | 'closed' | 'cancelled' | 'any'."""
        orders = self._shopify.Order.find(limit=first, status=status)
        return [
            {
                "id": o.id,
                "name": o.name,
                "email": o.email,
                "financial_status": o.financial_status,
                "fulfillment_status": o.fulfillment_status,
                "total_price": o.total_price,
                "created_at": o.created_at,
            }
            for o in orders
        ]

    # --- Lezen: GraphQL -----------------------------------------------------

    def graphql(self, query: str, variables: dict = None) -> dict:
        """
        Voert een GraphQL query of mutation uit.
        Voor mutations: gebruik graphql_mutation() — die heeft dry_run-bescherming.
        """
        gql = self._shopify.GraphQL()
        result = gql.execute(query, variables=variables)
        if isinstance(result, str):
            result = json.loads(result)
        if "errors" in result:
            raise RuntimeError(f"GraphQL errors: {result['errors']}")
        return result

    # --- Schrijven: met dry_run-bescherming ---------------------------------

    def graphql_mutation(
        self,
        mutation: str,
        variables: dict = None,
        entity: str = "?",
        before: str = "?",
        after: str = "?",
        dry_run: bool = True,
    ) -> dict | None:
        """
        Voert een GraphQL mutation uit met verplichte pre-change summary.

        dry_run=True  (default) — toont de samenvatting, voert NIET uit.
        dry_run=False           — toont de samenvatting, vraagt bevestiging, voert dan uit.
        """
        print("\n" + "=" * 60)
        print("PRE-CHANGE SUMMARY")
        print("=" * 60)
        print(f"Entity  : {entity}")
        print(f"Voor    : {before}")
        print(f"Na      : {after}")
        print(f"Mutation: {mutation[:200]}{'...' if len(mutation) > 200 else ''}")
        if variables:
            print(f"Variabelen: {json.dumps(variables, indent=2)[:300]}")
        print("=" * 60)

        if dry_run:
            print("DRY RUN — geen wijziging uitgevoerd. Geef dry_run=False om te executeren.")
            return None

        confirm = input("Bevestig (ja/nee): ").strip().lower()
        if confirm not in ("ja", "j", "yes", "y"):
            print("Geannuleerd.")
            return None

        return self._execute_with_retry(lambda: self.graphql(mutation, variables))

    def update_product(
        self,
        product_id: str,
        title: str = None,
        body_html: str = None,
        status: str = None,
        dry_run: bool = True,
    ) -> dict | None:
        """Update een product. Toont pre-change summary. dry_run=True by default."""
        current = self.product(product_id)
        changes = {}
        if title is not None:
            changes["title"] = title
        if body_html is not None:
            changes["bodyHtml"] = body_html
        if status is not None:
            changes["status"] = status.upper()

        mutation = """
        mutation productUpdate($input: ProductInput!) {
          productUpdate(input: $input) {
            product { id title status }
            userErrors { field message }
          }
        }
        """
        variables = {"input": {"id": f"gid://shopify/Product/{product_id}", **changes}}

        before_str = f"title='{current['title']}', status={current['status']}"
        after_str = f"changes: {changes}"

        return self.graphql_mutation(
            mutation, variables,
            entity=f"Product {product_id}",
            before=before_str,
            after=after_str,
            dry_run=dry_run,
        )

    def update_page(
        self,
        page_id: str,
        body_html: str = None,
        title: str = None,
        dry_run: bool = True,
    ) -> dict | None:
        """Update een store-pagina. Behoudt design — injecteert alleen de gewijzigde content."""
        current_page = self._shopify.Page.find(page_id)
        p = current_page
        before_title = p.title
        before_len = len(p.body_html or "")

        if title is not None:
            p.title = title
        if body_html is not None:
            p.body_html = body_html

        print("\n" + "=" * 60)
        print("PRE-CHANGE SUMMARY")
        print("=" * 60)
        print(f"Entity  : Page {page_id} ('{before_title}')")
        print(f"Voor    : body_html {before_len} tekens")
        print(f"Na      : body_html {len(body_html or p.body_html or '')} tekens")
        if title:
            print(f"Titel   : '{before_title}' → '{title}'")
        print("=" * 60)

        if dry_run:
            print("DRY RUN — geen wijziging uitgevoerd. Geef dry_run=False om te executeren.")
            return None

        confirm = input("Bevestig (ja/nee): ").strip().lower()
        if confirm not in ("ja", "j", "yes", "y"):
            print("Geannuleerd.")
            return None

        return self._execute_with_retry(lambda: p.save())

    # --- Intern: retry bij rate limiting ------------------------------------

    def _execute_with_retry(self, fn, max_retries: int = 4):
        """
        Voert fn() uit met exponential backoff bij 429 (rate limit).
        Shopify limiet: 2 req/sec REST, 1000 kostpunten/sec GraphQL.
        """
        delay = 1
        for attempt in range(max_retries):
            try:
                return fn()
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(f"Rate limit geraakt — wacht {delay}s (poging {attempt + 1}/{max_retries})")
                    self._time.sleep(delay)
                    delay *= 2
                else:
                    raise
        raise RuntimeError(f"Mislukt na {max_retries} pogingen (rate limit).")


# --- Smoke test -------------------------------------------------------------

if __name__ == "__main__":
    print("Shopify Handler — smoke test")
    print(f"Store: {STORE} | API versie: {API_VERSION}")
    print("-" * 40)

    client = ShopifyClient()

    print("\n[1] Store info:")
    info = client.shop_info()
    for k, v in info.items():
        print(f"  {k}: {v}")

    print("\n[2] Eerste 5 producten:")
    products = client.products(first=5)
    if products:
        for i, p in enumerate(products, 1):
            print(f"  {i}. [{p['status'].upper()}] {p['title'][:60]}")
            print(f"     handle={p['handle']} | images={p['images_count']} | desc_len={p['body_html_length']}")
    else:
        print("  Geen producten gevonden.")

    print("\n[3] Store-pagina's:")
    pages = client.pages()
    for pg in pages:
        status = "OK" if pg["body_html_length"] > 0 else "LEEG"
        print(f"  [{status}] {pg['title']} (/{pg['handle']}) — {pg['body_html_length']} tekens")

    print("\nSmoke test voltooid.")
