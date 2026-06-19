# Pax Domeinbrief — Sasha: Shopify Specialist

**Opgesteld door:** Pax
**Voor:** Nolan — verwerken in Sasha AGENT.md
**Datum:** 2026-05-19
**Context:** Tricolarae — vrouwenmode, doelmarkt VS, supplier Trendsi (dropshipping fase 1)

---

## 1. Shopify Store Architectuur

### Online Store 2.0 (OS2)

Shopify OS2 is het huidige thema-framework. Elke store die na 2021 is aangemaakt of een modern thema gebruikt, werkt met OS2. Sasha moet dit framework kennen om store-wijzigingen correct uit te voeren.

**Kernconcepten:**

**Sections** — bouwblokken van een pagina. Elk section is een Liquid-bestand (`sections/*.liquid`) of een JSON-configuratiebestand. Sections kunnen worden toegevoegd, verwijderd en herschikt via de theme editor zonder code te wijzigen.

**Blocks** — subcomponenten binnen een section. Een "Product Information" section kan blocks bevatten voor prijs, titel, variant-selector, knoppen. Blocks zijn configureerbaar per pagina.

**JSON templates** (`templates/page.json`, `templates/product.json`) — bepalen welke sections op een pagina worden geladen en in welke volgorde. Moderne OS2 stores gebruiken JSON templates in plaats van Liquid templates voor pagina-opbouw. Bij het lezen van pagina-inhoud altijd het JSON template ophalen naast de page body.

**Metafields** — aangepaste data-velden op producten, pagina's, klanten, orders. Worden gebruikt om content op te slaan die niet in de standaard Shopify-velden past. Voorbeeld: maattabel, stofsamenstelling, herkomst. Altijd checken op metafields vóór een pagina als "leeg" te beschouwen — content kan in metafields leven, niet in `body_html`.

**Metaobjects** — herbruikbare gestructureerde data-entiteiten. Worden gebruikt voor FAQ-items, teamleden, garantieblokken die op meerdere pagina's verschijnen. Bij FAQ of herhalende content-blokken: check of metaobjects in gebruik zijn.

**Liquid** — Shopify's templating language. Sasha hoeft geen Liquid te schrijven, maar moet het kunnen lezen om te begrijpen waar content vandaan komt en waarom een wijziging via de API soms niet het verwachte resultaat geeft.

### Wat Sasha operationeel moet weten

- Pagina-inhoud lezen = altijd drie bronnen: `body_html`, template asset, metafields
- Een wijziging via de API raakt alleen `body_html` — section-content in JSON templates vereist theme asset updates
- Bij twijfel over waar content leeft: fetch de live storefront URL en vergelijk met wat de API retourneert

---

## 2. Product Listing Standaarden

### Titelformule

Een Shopify producttitel voor fashion dropshipping in de VS volgt dit patroon:

```
[Beschrijvend adjectief] [Producttype] [Onderscheidend kenmerk]
```

Voorbeelden:
- "Floral Wrap Midi Dress — Summer Collection" ✓
- "Trendsi Women's Casual Floral Print Long Sleeve Dress" ✗ (leveranciersnaam, te lang, SEO-spam)

**Regels:**
- Geen leveranciersnamen (Trendsi, merknaam supplier) in de titel
- Geen modelnummers of SKU-codes zichtbaar
- Maximaal 70 tekens — alles daarna wordt afgekapt in Google Shopping
- Seizoen, gelegenheid of stijl benoemen als dat de zoekintentie matcht
- Tone of voice: Tricolarae is aspirationeel maar toegankelijk — niet high-fashion, niet fast-fashion

### Beschrijvingsstructuur

```
1. Opening (1-2 zinnen): sfeer en gevoel — wat is het en waarom wil je het?
2. Productdetails (bullets): materiaal, pasvorm, gelegenheid, care instructions
3. Maat & pasvorm: verwijs naar maattabel, geef pasvormadvies (bijv. "valt normaal op maat")
4. Levertijd: altijd vermelden — "Ships within 3–7 business days via Trendsi"
```

**Verbod:** nooit Chinese maattabellen kopiëren vanuit Trendsi. Altijd omzetten naar US sizing of een eigen maattabel aanmaken.

### Afbeeldingseisen

- Minimaal 3 afbeeldingen per product: frontaal, detail, lifestyle/context
- Minimaal 1:1 of 4:5 ratio — vierkant of staand, nooit liggend
- Witte of neutrale achtergrond voor primaire afbeelding (consistentie in collectie-overzicht)
- Lifestyle-foto's tonen het product gedragen in context — voorkeur voor US-vrouwenmodel
- Geen watermarks, geen Trendsi-branding, geen Chinese tekst in afbeeldingen
- Alt-tekst altijd invullen: beschrijf het product, niet "afbeelding 1"

### Collectie-architectuur

- Collecties zijn navigatiemiddelen én SEO-pagina's
- Structuur: per type (Dresses, Tops, Bottoms) + per gelegenheid (Casual, Date Night, Work) + per seizoen
- Elk product in minimaal één type-collectie + één gelegenheid-collectie
- Collectie-beschrijving invullen — dit is indexeerbare SEO-content

### Variant-setup

- Kleurvarianten: gebruik Engelse kleurnamen, geen leverancierskleurcodes
- Maatopties: XS/S/M/L/XL/XXL — nooit numeriek tenzij het product dat vereist
- Bij uitverkochte varianten: verberg of toon "notify me" — nooit lege knoppen tonen

---

## 3. Conversion Rate Optimization (CRO)

### Productpagina-hiërarchie (above the fold)

Op mobiel (70%+ van fashion traffic) moet de eerste viewport bevatten:
1. Productafbeelding (groot, swipeable gallery)
2. Producttitel
3. Prijs (inclusief doorgestreepte prijs als er korting is)
4. Variant-selector (maat/kleur)
5. "Add to Cart" knop — prominent, contrasterende kleur

Alles wat hieronder staat (beschrijving, reviews, levertijd) is belangrijk maar secundair.

### Trust signals

Voor een nieuwe store zonder reviews zijn trust signals extra kritiek:

- **Levertijden transparant** — "Ships in 3–7 business days" boven de fold of direct onder de prijs
- **Retourbeleid zichtbaar** — een retour-badge of korte vermelding op de productpagina ("Free returns within 30 days")
- **Beveiligingslogo's bij checkout** — Shopify Payments badge, SSL-icoon
- **"As seen in" of social proof** wanneer beschikbaar

### Urgentie (ethisch toepassen)

- Lage voorraad signaleren: "Only 3 left in your size" — alleen tonen als het echt klopt (Trendsi voorraad is dynamisch)
- Tijdelijke acties: alleen met echte einddatum
- Geen neppe countdown timers — dit beschadigt merkvertrouwen

### Checkout flow

- Guest checkout altijd ingeschakeld — verplicht account is de grootste checkout-killer
- Zo min mogelijk verplichte velden
- Shopify's native checkout niet aanpassen tenzij absoluut noodzakelijk — het is geoptimaliseerd door Shopify zelf

---

## 4. Shopify SEO

### URL-structuur

Shopify genereert automatisch URLs op basis van handle:
- Producten: `/products/[handle]`
- Collecties: `/collections/[handle]`
- Pagina's: `/pages/[handle]`

**Handle-regels:**
- Altijd lowercase, woorden gescheiden door koppeltekens
- Beschrijvend en keyword-rijk: `/products/floral-wrap-midi-dress` ✓
- Nooit met SKU of leverancierscode: `/products/t12345-dress` ✗
- Handle nooit wijzigen na indexering — breekt backlinks en zorgt voor 404's

### Meta titles & descriptions

**Title tag formule:**
```
[Productnaam] | Tricolarae
```
Maximaal 60 tekens. Keyword vooraan.

**Meta description:**
- 150–160 tekens
- Beschrijf het product en voeg een call-to-action toe
- Geen keyword-stuffing — schrijf voor mensen, niet voor bots

### Structured data

Shopify injecteert automatisch basis-structured data (Product schema) voor producten. Controleer bij thema-updates of dit nog correct werkt. Uitbreiden met: `aggregateRating` zodra reviews beschikbaar zijn.

### Page speed

Page speed is een directe ranking-factor en beïnvloedt conversie direct (-1% conversie per 100ms laadtijd).

Grootste boosdoeners op Shopify:
1. Te veel apps die JavaScript laden
2. Niet-geoptimaliseerde afbeeldingen (gebruik WebP, max 1MB per afbeelding)
3. Font-loading blokkades
4. Ongebruikte app-scripts die blijven laden na app-verwijdering

Sasha controleert page speed bij elke significante store-wijziging via Google PageSpeed Insights. Target: Lighthouse score ≥70 op mobiel.

---

## 5. Trendsi-integratie Workflow

### Wat Trendsi is

Trendsi is een US-gebaseerde fashion dropshipping supplier die direct integreert met Shopify via een officiële app. Producten worden vanuit Trendsi geïmporteerd naar de Shopify store — Trendsi verzorgt fulfillment direct naar de klant.

### Installatie & koppeling

1. Installeer de Trendsi app vanuit de Shopify App Store
2. Maak een Trendsi-account aan op `trendsi.com`
3. Koppel via OAuth in de app — Trendsi krijgt schrijftoegang tot producten en orders
4. Bevestig dat de koppeling actief is: een testimport van één product

### Product importeren

Via de Trendsi app (niet via API):
1. Browse of zoek producten in de Trendsi app
2. Selecteer product → "Add to Store"
3. Trendsi importeert: afbeeldingen, varianten, Trendsi-prijs, beschrijving
4. **Altijd daarna handmatig aanpassen:**
   - Titel herschrijven (geen Trendsi-branding)
   - Beschrijving herschrijven (Tricolarae tone of voice)
   - Verkoopprijs instellen op basis van Nova's margin check
   - Maattabel controleren en omzetten naar US sizing
   - Afbeeldingen screenen (geen Chinese tekst, geen watermarks)

### Prijssync

Trendsi-groothandelsprijzen kunnen wijzigen. De app biedt een optie voor automatische prijsupdate — **uitschakelen**. Nova bepaalt de verkoopprijs op basis van de pricing formula; automatische sync overschrijft dat.

**Instelling:** Trendsi app → Settings → Pricing → zet automatic price sync uit.

### Voorraadsync

Trendsi synchroniseert voorraad automatisch — dit is wenselijk. Als een product uitverkocht raakt bij Trendsi, wordt het in Shopify als "Out of Stock" gemarkeerd. Controleer of de store "Out of stock" producten verbergt of toont met een notificatie-optie.

### Fulfillment-automatisering

Bij een inkomende Shopify-order wordt de order automatisch doorgestuurd naar Trendsi (via de app-integratie) als auto-fulfillment is ingeschakeld. Trendsi verzendt direct naar de klant.

**Controle-instelling:** Trendsi app → Settings → Orders → Auto-fulfill: aan. Bevestig dat tracking-updates automatisch naar Shopify gaan.

### Wat Sasha operationeel bewaakt

- Dagelijks: orders zonder Trendsi-bevestiging na 48u → escaleren naar Nova
- Bij nieuwe producten: altijd handmatig titels/beschrijvingen aanpassen vóór publiceren
- Bij Trendsi app-updates: testen of de koppeling nog werkt na update

---

## 6. App-ecosysteem

### Evaluatiecriteria voor een nieuwe app

Voordat een app wordt geïnstalleerd, beantwoord:
1. Laadt de app JavaScript op de storefront? (impact op page speed)
2. Hoeveel actieve installs en wat is de gemiddelde rating? (>4.5 ster, >500 reviews = veilig)
3. Is er een gratis tier of trial? (altijd eerst testen)
4. Verwijdert de app zijn scripts netjes bij uninstall? (controleer na verwijdering in theme code)
5. Is de functionaliteit niet al ingebouwd in Shopify of een bestaande app?

### Essentiële apps voor Tricolarae (fase 1)

| App | Functie | Prioriteit |
|---|---|---|
| Trendsi | Dropshipping supplier integratie | Kritiek |
| Shopify Email | Transactionele en marketing e-mails | Hoog |
| Meta & Google Channel | Product feed voor Meta Ads en Google Shopping | Hoog |
| Cookie consent (bijv. Pandectes GDPR) | CCPA cookie banner | Verplicht |
| Review app (bijv. Judge.me) | Productreviews — zodra eerste orders binnen | Middel |

### Wat Sasha vermijdt

- Apps die belofte doen op "meer sales" zonder concrete mechanisme (urgency/countdown apps van lage kwaliteit)
- Meerdere apps voor dezelfde functie
- Apps zonder actief onderhoud (laatste update >1 jaar geleden)
- Popup-apps die de checkout-flow onderbreken

---

## 7. Legal & Compliance voor US Dropshipping

### CCPA (California Consumer Privacy Act)

Van toepassing zodra je verkoopt aan Californische consumenten. Vereisten:
- Privacy Policy vermeldt welke data wordt verzameld en met wie gedeeld (inclusief Trendsi als data processor)
- "Do Not Sell or Share My Personal Information" link in de footer — verplicht
- Cookie consent banner — verplicht

### Privacy Policy minimumvereisten

- Welke data wordt verzameld (naam, adres, e-mail, betaaldata)
- Hoe data wordt gebruikt (fulfillment, marketing)
- Welke derde partijen data ontvangen: Trendsi, Shopify Payments, Meta Pixel, Google Analytics
- Retentieperiode
- Rechten van de consument (inzage, verwijdering)
- Contactgegevens voor privacy-vragen

### Refund Policy voor Trendsi-model

Trendsi accepteert retours onder specifieke voorwaarden (defect, verkeerde item). Dit bepaalt wat Tricolarae aan klanten kan beloven.

**Tricolarae retourbeleid-standaard:**
- 30 dagen retourvenster voor defecte of verkeerde items
- Geen retours voor "van gedachten veranderd" (Trendsi dekt dit niet)
- Klant betaalt retourverzending tenzij de fout bij Trendsi/Tricolarae ligt
- Duidelijk communiceren vóór aankoop — niet verstopt in de footer

### Terms of Service

- Governing law: staat waar de business geregistreerd is (VS), niet Nederland
- Geen verwijzingen naar Europese wetgeving (GDPR, Nederlands recht)
- Shopify's policy generator als startpunt — aanpassen op Tricolarae-context

---

## 8. Store Health & Analytics

### Core Web Vitals (Google ranking signals)

| Metric | Wat het meet | Target |
|---|---|---|
| LCP (Largest Contentful Paint) | Hoe snel laadt het grootste element | <2.5s |
| FID/INP (Interaction to Next Paint) | Hoe responsief is de pagina | <200ms |
| CLS (Cumulative Layout Shift) | Verschuift de lay-out tijdens laden? | <0.1 |

Shopify's hosted infrastructure scoort goed op LCP — de grootste risicofactor is onnodige app-scripts.

### Afbeeldingsoptimalisatie

- Formaat: WebP (Shopify converteert automatisch bij upload via admin — check of thema WebP serveert)
- Maximale bestandsgrootte: 1MB per afbeelding vóór upload
- Afmetingen: 2048×2048px voor productafbeeldingen (Shopify schaalt naar beneden)
- Alt-tekst: altijd invullen — zoekmachines en accessibility

### Meta Pixel setup

1. Installeer de Meta & Google Channel app
2. Koppel via OAuth met het Meta Business account
3. Pixel wordt automatisch op alle pagina's geïnjecteerd
4. Controleer met Meta Pixel Helper (browser extension) of events correct vuren: PageView, ViewContent, AddToCart, Purchase

### GA4 setup

1. Maak een GA4 property aan in Google Analytics
2. Koppel via Shopify Admin → Online Store → Preferences → Google Analytics
3. Controleer datastromen: web property + ecommerce tracking ingeschakeld
4. GA4 en Meta Pixel beide actief — GA4 voor eigen analytics, Meta Pixel voor ads-attributie

### Shopify Analytics

Shopify heeft ingebouwde analytics. Sasha bewaakt wekelijks:
- Sessions, conversion rate, average order value
- Top traffic sources
- Top selling products
- Cart abandonment rate

---

## 9. Mobiel-First Standaarden

### Fashion traffic is mobiel

70–80% van fashion e-commerce traffic komt van mobiele apparaten. Elke store-beslissing wordt eerst getest op mobiel.

### Product page op mobiel

- Afbeelding neemt de volledige viewport-breedte in
- Swipebare galerij — minimaal 3 afbeeldingen swipeable
- Prijs en "Add to Cart" knop zichtbaar zonder scrollen (sticky ATC-knop indien thema dit ondersteunt)
- Beschrijving achter een "Read more" toggle — niet als lange scrollende tekst

### Checkout op mobiel

- Shop Pay inschakelen — reduceert checkout-stappen significant voor terugkerende Shopify-klanten
- Apple Pay / Google Pay inschakelen — one-tap checkout op mobiel
- Zo min mogelijk verplichte velden: naam, adres, e-mail, betaling — meer is conversie-verlies

### Navigatie op mobiel

- Hamburger menu met maximaal 6 hoofdcategorieën
- Zoekfunctie prominent — fashion shoppers zoeken actief
- Filteropties in collectie-overzicht: maat, kleur, prijs — mobiel-vriendelijk (slide-out panel)

---

## 10. Fashion/Mode Niche — Tricolarae Specifiek

### Wat werkt in vrouwenmode

**Sizing guides zijn conversie-kritiek** — maatproblemen zijn de #1 reden voor retours in fashion. Elke productpagina heeft een link naar de maattabel. De maattabel is in US sizing, niet Aziatisch.

**Outfit-context afbeeldingen** — toon het product gedragen, niet alleen op een witte achtergrond. "How to style" afbeeldingen verhogen AOV (gemiddelde orderwaarde) omdat ze inspireren tot bijpassende aankopen.

**Seizoenslogica** — fashion is seizoensgebonden. Collecties roteren. Zomer-items promoten in april–juni, niet in september. Sasha bewaakt of gepubliceerde producten seizoensrelevant zijn.

**Retourbeleid als verkoopargument** — in fashion is een soepel retourbeleid een conversie-driver. Positioneer het als vertrouwenssignaal, niet als disclaimer.

**Kleurweergave is kritiek** — afbeeldingen moeten de werkelijke kleur tonen. Bij grote kleurafwijking stijgt het retourpercentage. Trendsi-afbeeldingen screenen op kleurnauwkeurigheid.

### Wat Tricolarae vermijdt

- Overdaad aan producten zonder curation — een store met 500 slecht gepresenteerde producten converteert slechter dan een store met 30 goed gepresenteerde producten
- Leveranciersbranding zichtbaar in de store (Trendsi, Chinese merken)
- Inconsistente toon — elke beschrijving moet klinken als Tricolarae, niet als een gegenereerde productfeed
- Maattabellen in centimeters zonder US-conversie

---

## Samenvatting voor Nolan

Sasha's huidige AGENT.md heeft een sterk operationeel fundament (toolset, approval-protocol, pagina-leesregel). Wat ontbreekt is embedded domain knowledge die haar van een bekwame operator naar een world-class specialist tilt.

Voeg toe aan haar AGENT.md:
1. Shopify OS2 architectuurkennis (metafields, JSON templates, blocks)
2. Concrete product listing standaarden (titelformule, beschrijvingsstructuur, afbeeldingseisen)
3. CRO-principes voor fashion (mobile-first hiërarchie, trust signals, checkout)
4. SEO-standaarden (URL-handles, meta tags, page speed)
5. Trendsi-workflow van import tot fulfillment-check
6. App-evaluatiecriteria en essentiële app-lijst
7. Legal compliance checklist voor US dropshipping
8. Analytics-monitoring (Pixel, GA4, Shopify Analytics)
9. Fashion-niche specifieke kennis (sizing, seizoen, retour als verkoopargument)

Behoud: de bestaande toolset-sectie (Shopify CLI commando's, store URL, scopes), de page content retrieval rule, de approval rule, de proactief meedenken sectie, en de samenwerking met Kai/Vera.

**Delivered on:** 2026-05-19
**Delivered at:** Sasha upgrade traject — Pax domeinbrief
