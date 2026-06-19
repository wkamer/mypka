"""
Geldstroom Regie — WordPress page builder
Builds and publishes 4 pages via REST API, then sets the homepage.
"""

import urllib.request
import urllib.parse
import json
import base64
import ssl

ctx = ssl._create_unverified_context()
BASE = "https://geldstroomregie.nl/wp-json/wp/v2"
token = base64.b64encode(b"admin:eHlg w17j KpIL HBij rjzu PdQd").decode()
HEADERS = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}


def api(method, path, data=None):
    url = f"{BASE}/{path}"
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
        return json.loads(r.read())


def wp_options(method, path, data=None):
    """Hit wp-json root or custom endpoints."""
    url = f"https://geldstroomregie.nl/wp-json/{path}"
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
        return json.loads(r.read())


# ── Page content definitions ──────────────────────────────────────────────────

HOMEPAGE_CONTENT = """<!-- wp:group {"tagName":"section","className":"hero-section","style":{"spacing":{"padding":{"top":"80px","bottom":"80px"}},"color":{"background":"#f0f7f4"}}} -->
<section class="wp-block-group hero-section" style="background-color:#f0f7f4;padding-top:80px;padding-bottom:80px">

<!-- wp:heading {"level":1,"textAlign":"center","style":{"typography":{"fontSize":"48px"},"color":{"text":"#1a3a2a"}}} -->
<h1 class="wp-block-heading has-text-align-center" style="color:#1a3a2a;font-size:48px">Van geldzorg naar geldrust</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"20px"},"color":{"text":"#3a5a4a"}}} -->
<p class="has-text-align-center" style="color:#3a5a4a;font-size:20px">Geldstroom Regie helpt jou de regie terugnemen over jouw geldstromen.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"},"style":{"spacing":{"blockGap":"16px","margin":{"top":"32px"}}}} -->
<div class="wp-block-buttons">
<!-- wp:button {"backgroundColor":"#2d7a4f","textColor":"#ffffff","style":{"border":{"radius":"6px"}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-text-color has-background" href="/gratis-brochure" style="border-radius:6px;background-color:#2d7a4f;color:#ffffff">Gratis brochure aanvragen</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline","style":{"border":{"radius":"6px","color":"#2d7a4f","width":"2px"},"color":{"text":"#2d7a4f"}}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link has-text-color" href="/geldstroom-scan" style="border-radius:6px;border-color:#2d7a4f;border-width:2px;color:#2d7a4f">Bekijk de Geldstroom Scan</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->

</section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","className":"pain-section","style":{"spacing":{"padding":{"top":"60px","bottom":"60px"}}}} -->
<section class="wp-block-group pain-section" style="padding-top:60px;padding-bottom:60px">

<!-- wp:heading {"level":2,"textAlign":"center","style":{"color":{"text":"#1a3a2a"}}} -->
<h2 class="wp-block-heading has-text-align-center" style="color:#1a3a2a">Herken jij dit?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"18px"}}} -->
<p class="has-text-align-center" style="color:#4a6a5a;font-size:18px">Elke maand verdwijnt er geld. Je weet alleen niet precies waar naartoe.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"18px"}}} -->
<p class="has-text-align-center" style="color:#4a6a5a;font-size:18px">Je spaart af en toe, maar niet structureel.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"18px"}}} -->
<p class="has-text-align-center" style="color:#4a6a5a;font-size:18px">Geld voelt als iets dat je overkomt, niet iets dat je stuurt.</p>
<!-- /wp:paragraph -->

</section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","className":"what-section","style":{"spacing":{"padding":{"top":"60px","bottom":"60px"}},"color":{"background":"#e8f4ee"}}} -->
<section class="wp-block-group what-section" style="background-color:#e8f4ee;padding-top:60px;padding-bottom:60px">

<!-- wp:heading {"level":2,"textAlign":"center","style":{"color":{"text":"#1a3a2a"}}} -->
<h2 class="wp-block-heading has-text-align-center" style="color:#1a3a2a">Wat is Geldstroom Regie?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"18px"},"spacing":{"padding":{"left":"10%","right":"10%"}}}} -->
<p class="has-text-align-center" style="color:#4a6a5a;font-size:18px;padding-left:10%;padding-right:10%">Geldstroom Regie structureert jouw geldstromen van inkomen tot groei. Geen productadvies, geen oordeel — maar een werkend geldsysteem op maat.</p>
<!-- /wp:paragraph -->

</section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","className":"cta-section","style":{"spacing":{"padding":{"top":"60px","bottom":"60px"}}}} -->
<section class="wp-block-group cta-section" style="padding-top:60px;padding-bottom:60px">

<!-- wp:columns {"style":{"spacing":{"blockGap":"32px","padding":{"left":"5%","right":"5%"}}}} -->
<div class="wp-block-columns" style="padding-left:5%;padding-right:5%">

<!-- wp:column {"style":{"color":{"background":"#f0f7f4"},"spacing":{"padding":{"top":"40px","bottom":"40px","left":"32px","right":"32px"}},"border":{"radius":"8px"}}} -->
<div class="wp-block-column" style="background-color:#f0f7f4;border-radius:8px;padding:40px 32px">
<!-- wp:heading {"level":3,"style":{"color":{"text":"#1a3a2a"}}} -->
<h3 class="wp-block-heading" style="color:#1a3a2a">Gratis brochure</h3>
<!-- /wp:heading -->
<!-- wp:paragraph {"style":{"color":{"text":"#4a6a5a"}}} -->
<p style="color:#4a6a5a">Ontdek de 5 meest voorkomende geldlekken en eerste stappen om ze te dichten.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons -->
<div class="wp-block-buttons">
<!-- wp:button {"backgroundColor":"#2d7a4f","textColor":"#ffffff","style":{"border":{"radius":"6px"}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-text-color has-background" href="/gratis-brochure" style="border-radius:6px;background-color:#2d7a4f;color:#ffffff">Download gratis</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</div>
<!-- /wp:column -->

<!-- wp:column {"style":{"color":{"background":"#1a3a2a"},"spacing":{"padding":{"top":"40px","bottom":"40px","left":"32px","right":"32px"}},"border":{"radius":"8px"}}} -->
<div class="wp-block-column" style="background-color:#1a3a2a;border-radius:8px;padding:40px 32px">
<!-- wp:heading {"level":3,"style":{"color":{"text":"#ffffff"}}} -->
<h3 class="wp-block-heading" style="color:#ffffff">Geldstroom Scan</h3>
<!-- /wp:heading -->
<!-- wp:paragraph {"style":{"color":{"text":"#c0d8c8"}}} -->
<p style="color:#c0d8c8">In één sessie weet je precies waar jouw geld naartoe stroomt — en waar de ruimte zit.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"style":{"color":{"text":"#ffffff"},"typography":{"fontSize":"28px","fontWeight":"700"}}} -->
<p style="color:#ffffff;font-size:28px;font-weight:700">€197</p>
<!-- /wp:paragraph -->
<!-- wp:buttons -->
<div class="wp-block-buttons">
<!-- wp:button {"backgroundColor":"#2d7a4f","textColor":"#ffffff","style":{"border":{"radius":"6px"}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-text-color has-background" href="/geldstroom-scan" style="border-radius:6px;background-color:#2d7a4f;color:#ffffff">Bekijk de Scan</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</div>
<!-- /wp:column -->

</div>
<!-- /wp:columns -->

</section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"footer","className":"site-footer-note","style":{"spacing":{"padding":{"top":"32px","bottom":"32px"}},"color":{"background":"#f5f5f5"}}} -->
<footer class="wp-block-group site-footer-note" style="background-color:#f5f5f5;padding-top:32px;padding-bottom:32px">
<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#888888"},"typography":{"fontSize":"13px"}}} -->
<p class="has-text-align-center" style="color:#888888;font-size:13px">info@geldstroomregie.nl | Geldstroom Regie geeft geen advies over specifieke financiële producten, banken, hypotheken of verzekeringen.</p>
<!-- /wp:paragraph -->
</footer>
<!-- /wp:group -->"""


SCAN_CONTENT = """<!-- wp:group {"tagName":"section","style":{"spacing":{"padding":{"top":"60px","bottom":"20px"}}}} -->
<section class="wp-block-group" style="padding-top:60px;padding-bottom:20px">
<!-- wp:heading {"level":1,"textAlign":"center","style":{"color":{"text":"#1a3a2a"}}} -->
<h1 class="wp-block-heading has-text-align-center" style="color:#1a3a2a">Geldstroom Scan</h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"20px"}}} -->
<p class="has-text-align-center" style="color:#4a6a5a;font-size:20px">In één sessie weet je precies waar jouw geld naartoe stroomt — en waar de ruimte zit.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","style":{"spacing":{"padding":{"top":"40px","bottom":"40px","left":"10%","right":"10%"}}}} -->
<section class="wp-block-group" style="padding:40px 10%">
<!-- wp:heading {"level":2,"style":{"color":{"text":"#1a3a2a"}}} -->
<h2 class="wp-block-heading" style="color:#1a3a2a">Voor wie?</h2>
<!-- /wp:heading -->
<!-- wp:list {"style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"17px"}}} -->
<ul style="color:#4a6a5a;font-size:17px">
<li>Je weet dat er iets niet klopt met jouw geldstromen, maar je weet niet waar te beginnen.</li>
<li>Je spaart niet structureel en hebt geen grip op jouw vaste lasten.</li>
<li>Je wil meer rust rondom geld, zonder ingewikkeld advies.</li>
</ul>
<!-- /wp:list -->
</section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","style":{"spacing":{"padding":{"top":"40px","bottom":"40px","left":"10%","right":"10%"}},"color":{"background":"#f0f7f4"}}} -->
<section class="wp-block-group" style="background-color:#f0f7f4;padding:40px 10%">
<!-- wp:heading {"level":2,"style":{"color":{"text":"#1a3a2a"}}} -->
<h2 class="wp-block-heading" style="color:#1a3a2a">Wat krijg je?</h2>
<!-- /wp:heading -->
<!-- wp:list {"style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"17px"}}} -->
<ul style="color:#4a6a5a;font-size:17px">
<li>Helder overzicht van jouw huidige geldstromen</li>
<li>Inzicht in waar geld ongemerkt verdwijnt</li>
<li>Een 50/30/20 gezondheidscheck als thermometer</li>
<li>Concrete eerste kansen om jouw geldsysteem te verbeteren</li>
<li>Een persoonlijk rapport na de sessie</li>
</ul>
<!-- /wp:list -->
</section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","style":{"spacing":{"padding":{"top":"40px","bottom":"40px","left":"10%","right":"10%"}}}} -->
<section class="wp-block-group" style="padding:40px 10%">
<!-- wp:heading {"level":2,"style":{"color":{"text":"#1a3a2a"}}} -->
<h2 class="wp-block-heading" style="color:#1a3a2a">Hoe werkt het?</h2>
<!-- /wp:heading -->
<!-- wp:list {"ordered":true,"style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"17px"}}} -->
<ol style="color:#4a6a5a;font-size:17px">
<li>Bestel de Geldstroom Scan</li>
<li>Vul het intakeformulier in</li>
<li>We plannen een sessie in en je ontvangt jouw rapport</li>
</ol>
<!-- /wp:list -->
</section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","style":{"spacing":{"padding":{"top":"60px","bottom":"60px"}},"color":{"background":"#1a3a2a"}}} -->
<section class="wp-block-group" style="background-color:#1a3a2a;padding-top:60px;padding-bottom:60px">
<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#ffffff"},"typography":{"fontSize":"48px","fontWeight":"700"}}} -->
<p class="has-text-align-center" style="color:#ffffff;font-size:48px;font-weight:700">Pilotprijs: €197</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#aacab8"},"typography":{"fontSize":"15px"}}} -->
<p class="has-text-align-center" style="color:#aacab8;font-size:15px">Tijdelijke pilotprijs — daarna €247</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"},"style":{"spacing":{"margin":{"top":"24px"}}}} -->
<div class="wp-block-buttons">
<!-- wp:button {"backgroundColor":"#2d7a4f","textColor":"#ffffff","style":{"border":{"radius":"6px"},"typography":{"fontSize":"18px"}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-text-color has-background" href="#betalen" style="border-radius:6px;background-color:#2d7a4f;color:#ffffff;font-size:18px">Bestel de Geldstroom Scan</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","style":{"spacing":{"padding":{"top":"32px","bottom":"48px","left":"10%","right":"10%"}}}} -->
<section class="wp-block-group" style="padding:32px 10% 48px">
<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#888888"},"typography":{"fontSize":"13px"}}} -->
<p class="has-text-align-center" style="color:#888888;font-size:13px">Geldstroom Regie geeft geen advies over specifieke financiële producten, banken, hypotheken of verzekeringen. Onze begeleiding richt zich op structuur, overzicht en geldstromen.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->"""


BEDANKT_CONTENT = """<!-- wp:group {"tagName":"section","style":{"spacing":{"padding":{"top":"80px","bottom":"80px"}},"color":{"background":"#f0f7f4"}}} -->
<section class="wp-block-group" style="background-color:#f0f7f4;padding-top:80px;padding-bottom:80px">

<!-- wp:heading {"level":1,"textAlign":"center","style":{"color":{"text":"#1a3a2a"}}} -->
<h1 class="wp-block-heading has-text-align-center" style="color:#1a3a2a">Bedankt voor je bestelling!</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"18px"},"spacing":{"margin":{"top":"24px"}}}} -->
<p class="has-text-align-center" style="color:#4a6a5a;font-size:18px;margin-top:24px">Je ontvangt een bevestiging per e-mail op het adres dat je hebt opgegeven.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"18px"}}} -->
<p class="has-text-align-center" style="color:#4a6a5a;font-size:18px">Vul nu het intakeformulier in zodat we ons goed kunnen voorbereiden op jouw sessie.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"},"style":{"spacing":{"margin":{"top":"32px","bottom":"32px"}}}} -->
<div class="wp-block-buttons">
<!-- wp:button {"backgroundColor":"#2d7a4f","textColor":"#ffffff","style":{"border":{"radius":"6px"},"typography":{"fontSize":"17px"}}} -->
<div class="wp-block-button"><a class="wp-block-button__link has-text-color has-background" href="#intakeformulier" style="border-radius:6px;background-color:#2d7a4f;color:#ffffff;font-size:17px">Vul het intakeformulier in</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->

<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#7a9a8a"},"typography":{"fontSize":"16px"}}} -->
<p class="has-text-align-center" style="color:#7a9a8a;font-size:16px">Wij nemen binnen 2 werkdagen contact met je op om een afspraak in te plannen.</p>
<!-- /wp:paragraph -->

</section>
<!-- /wp:group -->"""


BROCHURE_CONTENT = """<!-- wp:group {"tagName":"section","style":{"spacing":{"padding":{"top":"60px","bottom":"20px"}}}} -->
<section class="wp-block-group" style="padding-top:60px;padding-bottom:20px">
<!-- wp:heading {"level":1,"textAlign":"center","style":{"color":{"text":"#1a3a2a"}}} -->
<h1 class="wp-block-heading has-text-align-center" style="color:#1a3a2a">Ontdek waar jouw geld naartoe stroomt</h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"20px"},"spacing":{"padding":{"left":"10%","right":"10%"}}}} -->
<p class="has-text-align-center" style="color:#4a6a5a;font-size:20px;padding-left:10%;padding-right:10%">Ontvang gratis: 5 signalen dat jouw geldstromen niet op orde zijn — en eerste stappen om dat te veranderen.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","style":{"spacing":{"padding":{"top":"40px","bottom":"40px","left":"10%","right":"10%"}},"color":{"background":"#f0f7f4"}}} -->
<section class="wp-block-group" style="background-color:#f0f7f4;padding:40px 10%">
<!-- wp:heading {"level":2,"style":{"color":{"text":"#1a3a2a"}}} -->
<h2 class="wp-block-heading" style="color:#1a3a2a">Wat krijg je?</h2>
<!-- /wp:heading -->
<!-- wp:list {"style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"17px"}}} -->
<ul style="color:#4a6a5a;font-size:17px">
<li>De 5 meest voorkomende geldlekken in Nederlandse huishoudens</li>
<li>Een eerste check van jouw geldstroom-gezondheid</li>
<li>Praktische eerste stappen zonder ingewikkeld advies</li>
</ul>
<!-- /wp:list -->
</section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","style":{"spacing":{"padding":{"top":"48px","bottom":"48px","left":"10%","right":"10%"}}}} -->
<section class="wp-block-group" style="padding:48px 10%">
<!-- wp:paragraph {"style":{"color":{"text":"#4a6a5a"},"typography":{"fontSize":"16px"},"border":{"color":"#c0d8c8","width":"1px","radius":"8px"},"spacing":{"padding":{"top":"32px","bottom":"32px","left":"32px","right":"32px"}}}} -->
<p style="color:#4a6a5a;font-size:16px;border:1px solid #c0d8c8;border-radius:8px;padding:32px">[Mailerlite formulier komt hier — naam + e-mailadres + knop 'Stuur mij de gratis brochure']</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"align":"center","style":{"color":{"text":"#888888"},"typography":{"fontSize":"13px"},"spacing":{"margin":{"top":"16px"}}}} -->
<p class="has-text-align-center" style="color:#888888;font-size:13px;margin-top:16px">Geen spam. Je kunt je altijd uitschrijven.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->"""


# ── Build pages ───────────────────────────────────────────────────────────────

pages = [
    {
        "title": "Home",
        "slug": "home",
        "content": HOMEPAGE_CONTENT,
        "status": "publish",
    },
    {
        "title": "Geldstroom Scan",
        "slug": "geldstroom-scan",
        "content": SCAN_CONTENT,
        "status": "publish",
    },
    {
        "title": "Bedankt voor je bestelling",
        "slug": "bedankt-scan",
        "content": BEDANKT_CONTENT,
        "status": "publish",
    },
    {
        "title": "Gratis brochure aanvragen",
        "slug": "gratis-brochure",
        "content": BROCHURE_CONTENT,
        "status": "publish",
    },
]

created = {}

for page in pages:
    # Check if slug already exists
    existing = api("GET", f"pages?slug={page['slug']}&per_page=1")
    if existing:
        pid = existing[0]["id"]
        result = api("POST", f"pages/{pid}", page)
        action = "updated"
    else:
        result = api("POST", "pages", page)
        action = "created"
    created[page["slug"]] = result["id"]
    link = result.get("link", "")
    print(f"[{action.upper()}] {page['title']} -> ID={result['id']} | {link}")

# ── Set homepage as front page ────────────────────────────────────────────────
homepage_id = created["home"]

# Use wp/v2/settings endpoint
try:
    settings = api("POST", "settings", {
        "show_on_front": "page",
        "page_on_front": homepage_id,
    })
    print(f"\n[SETTINGS] show_on_front=page, page_on_front={homepage_id}")
    print(f"  show_on_front = {settings.get('show_on_front')}")
    print(f"  page_on_front = {settings.get('page_on_front')}")
except Exception as e:
    print(f"[SETTINGS ERROR] {e}")

print("\n── All done ──")
print(f"  Homepage:        https://geldstroomregie.nl/")
print(f"  Geldstroom Scan: https://geldstroomregie.nl/geldstroom-scan/")
print(f"  Bedankt:         https://geldstroomregie.nl/bedankt-scan/")
print(f"  Brochure:        https://geldstroomregie.nl/gratis-brochure/")
