# KE - STORE

**Area:** Stores
**Doel:** Vastleggen hoe de Shopify store staat, wat er werkt, en wat nog open staat.

---

## Store-overzicht

| | |
|---|---|
| **Naam** | Tricolarae |
| **URL** | https://tricolarae.com |
| **Platform** | Shopify |
| **Status** | ~90% ingericht (mei 2026) |
| **Valuta** | USD |
| **Doelmarkt** | Verenigde Staten |
| **Leverancier** | 1 US-gebaseerde leverancier (korte levertijden als prioriteit) |
| **Verkopen** | Geen echte verkopen — alleen 2 testorders van eigenaar |

---

## Merkvisie (leidend voor storeinrichting)

> "Ik bouw geen webshop om zoveel mogelijk producten te verkopen, maar om een plek te creëren waar mensen met een goed gevoel kunnen kopen. Producten die logisch zijn, goed gepresenteerd en gekozen met aandacht."

Elke storewijziging wordt hieraan getoetst: draagt dit bij aan het gevoel?

---

## Wat er live staat

- **Producten:** ~28 actief (9 placeholder + 19 echte dropshipping producten)
- **Focus assortiment:** Dames knitwear — knit tops en cardigans
- **Looks-presentatie:** nog niet ingericht — producten staan los, niet als outfits

---

## Technische aandachtspunten

- **Placeholders nog actief:** Winter Top/Pants/Shoes A/B/C moeten verwijderd worden
- **Valuta:** USD — klopt, doelmarkt is de VS
- **Facebook Pixel:** Controleren of tracking correct is geïnstalleerd (vóór eerste campagne)
- **Producttitels:** Leveranciersnamen staan nog in titels (BOMBOM, Zenana, etc.) — herschrijven

---

## Conversiepunten (te optimaliseren na eerste traffic)

- Productpagina's: beschrijvingen zijn nog supplier-tekst, geen Tricolarae-tone
- Looks: geen outfit-suggesties of "style it with" secties
- Homepage: sluit die aan bij de merkvisie?
- Checkout: eventuele drempels in kaart brengen

---

## Pre-launch checklist — US markt (audit 2026-05-02)

Volledig rapport: `Kamer E-commerce/Deliverables/2026-05-02_us-store-audit/store-audit.md`

### Juridisch verplicht — blokkeert lancering

- [ ] Privacy Policy met CCPA/CPRA sectie (Shopify: Settings → Policies)
- [ ] Terms of Service (Shopify: Settings → Policies)
- [ ] Refund Policy — aansluitend op Trendsi 7-dagenbeleid
- [ ] Shipping Policy — verwerkingstijd, 2–5 werkdagen, US only
- [ ] Contact pagina — bedrijfsnaam, support e-mail, fysiek postadres, reactietijd
- [ ] Cookie banner met CCPA opt-out (Shopify Customer Privacy of app: Pandectes/Consentmo)
- [ ] "Do Not Sell or Share My Personal Information" link in footer
- [ ] Geen "Made in USA" claims — Trendsi sourcet globaal
- [ ] Prijstransparantie bij checkout — geen verborgen kosten
- [ ] Bedrijfsregistratie + sales tax nexus instellen in Shopify (seller of record = Tricolarae)

### Klantvertrouwen — sterk aanbevolen voor lancering

- [ ] About Us pagina — persoonlijk verhaal, merkvisie, wie zit er achter Tricolarae
- [ ] Size Guide pagina — US sizing (inches), modelreferentie
- [ ] FAQ pagina — levertijd, retouren, maatvoering, tracking, betaling
- [ ] Klantvriendelijke Shipping Info pagina (los van de legale policy)
- [ ] Klantvriendelijke Returns pagina (los van de legale policy)
- [ ] Review app installeren (Judge.me of Loox) — vanaf eerste order reviews verzamelen
- [ ] Newsletter signup met 10% welkomstkorting + privacy disclosure
- [ ] Fabric content + verzorgingsinstructies per product (Trendsi levert dit — verifiëren)

### Dropshipping-specifiek

- [ ] Privacy Policy vermeldt dat orderdata gedeeld wordt met Trendsi (fulfillment)
- [ ] Nergens "our warehouse" — gebruik "US fulfillment partner"
- [ ] Productomschrijvingen zijn uniek — niet kopiëren van andere Trendsi-resellers

### Post-launch (eerste 30-60 dagen)

- [ ] Accessibility statement
- [ ] Blog/redactionele content voor SEO
- [ ] Lookbook pagina

---

## Productpagina opbouw (Phase 2.2)

Gebruik de PRSO/FEBE/LIDE copystructuur uit [[KE-Advertising]]:

**Step 1 — Hero Section (PRSO)**
- Sterke headline en duidelijke visuele hero (foto/video)
- Direct CTA zichtbaar ("Shop nu")

**Step 2 — Feature/Benefit Blok (FEBE)**
- Lijstjes met duidelijke voordelen (✓ in plaats van specs)
- Ondersteund met visuals/icons

**Step 3 — Lifestyle/Desire Blok (LIDE)**
- Emotionele beelden of lifestyle-foto's
- Schets de gewenste situatie (before/after)

**Step 4 — Testimonials & CTA (TEST)**
- 2–3 social proof elementen (reviews, sterren, quotes)
- Sterke CTA afsluiting ("Bestel vandaag nog")

**Page structure (volgorde):**
Hero → Proof (badges/reviews) → Benefits → Hoe werkt het → Vergelijking/FAQ → Bundel/Prijs → Garantie → CTA

---

## Shopify code snippets

### Extended Product Description (metafield-gebaseerd)

Voeg toe aan product template voor een uitgebreide omschrijving via metafield:

```liquid
{% if product.metafields.custom.product_description_extended.value != blank %}
  <div class="extended-description" style="padding: 0 5rem;">
    {{ product.metafields.custom.product_description_extended.value }}
  </div>
{% endif %}
```

### Custom Benefits (metafield-gebaseerd)

Voeg toe aan product template om benefits uit metafield te renderen:

```liquid
{% if product.metafields.custom.benefits.value != blank %}
  <div style="background-color: #ffffff; font-size:0.65em; padding: 0px px; border-radius: 8px;">
    {{ product.metafields.custom.benefits | metafield_tag }}
  </div>
{% endif %}
```

---

## Merkkleur referentie (EKAAZA — historisch)

EKAAZA was een eerder store-concept. Kleurlogica is herbruikbaar als referentie bij toekomstige Shopify-setups.

| Kleur | Hex | Gebruik |
|---|---|---|
| Primary Dark | #2A2A34 | Headers, footers, dark sections, badges |
| CTA Orange | #FF6B35 | Primaire knoppen, Add to Cart, urgentie banners |
| Secondary Accent | #E6E8F5 | Feature sections, testimonials, subtiele blokken |
| White | #FFFFFF | Light background, tekst op dark |

**CTA hover:** #E65A2E (contrasting color -15% brightness)
**Selected bundle bg:** #FFE1D6 (contrasting color @ 15% opacity boven white)

Leidend principe: alle niet-primaire kleuren afleiden via formule t.o.v. de brand kit kleuren — nooit willekeurig kiezen.

---

## Open punten

- Placeholderproducten verwijderen (Winter Top/Pants/Shoes A/B/C)
- Facebook Pixel installatie verifiëren vóór eerste campagne
- Producttitels herschrijven — leveranciersnamen eruit (BOMBOM, Zenana, etc.)
- Productbeschrijvingen herschrijven naar Tricolarae-tone
- Look-presentatie toevoegen aan productpagina's

---

*Bijgewerkt: 2026-05-02 — pre-launch checklist toegevoegd op basis van US store audit (Pax)*
