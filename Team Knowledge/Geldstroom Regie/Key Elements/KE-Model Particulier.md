# KE-Model Particulier

Domein: huishoudens (alleenstaanden, stellen, gezinnen)

---

## Modelstructuur

```
Geldstromen
├── Inkomen
│   ├── Vast
│   ├── Vast met afhankelijkheid
│   └── Variabel
└── Bestedingen
    └── Bestemmingen
        ├── Needs
        │   ├── Vast
        │   └── Variabel
        ├── Wants (alleen particulier)
        │   └── Vast
        ├── Reserves
        │   ├── Niet gepland
        │   └── Gepland
        └── Groei
            ├── Financieel (beleggen, ETF, spaarrekening)
            └── Reëel (vastgoed, fysiek bezit)

= Vrij besteedbaar (Inkomen - alle bestemmingen)
```

---

## Inkomen (Income)

| Variant | Omschrijving | Voorbeelden |
|---|---|---|
| Vast | Structureel, geen einddatum, geen externe afhankelijkheid | Salaris, vaste huurinkomsten |
| Vast met afhankelijkheid | Zeker voor de looptijd, daarna onzeker door externe afhankelijkheid | Huurtoeslag, zorgtoeslag, alimentatie |
| Variabel | Geen toezegging vooraf, elke keer opnieuw verdiend | Overuren, freelance opdrachten, bonussen |

> Planningsprincipe: Vast = basis. Vast met afhankelijkheid = bewust meewegen, geen structurele verplichtingen op bouwen. Variabel = niet meetellen totdat het er is.

---

## Bestedingen (Expenses)

### Needs

Noodzakelijke kosten — geen keuze.

| Bucket | Voorbeelden |
|---|---|
| Vast | Huur, energie, verzekeringen |
| Variabel | Boodschappen |

### Wants

Vaste keuzeposten — bewust gekozen, terugkerend. Alleen vast.

| Bucket | Voorbeelden |
|---|---|
| Vast | Sportschool, streaming, abonnementen |

> Variabel discretionair = vrij besteedbaar, geen Wants-bucket.

---

## Reserves

Liquide, vrij opneembaar. Tijdelijk geparkeerd geld voor toekomstig gebruik.

| Bucket | Omschrijving | Voorbeelden |
|---|---|---|
| Niet gepland | Noodbuffer — voor als er iets misgaat. Kan blijven groeien; surplus schuift naar Gepland | Auto kapot, onverwachte medische kosten |
| Gepland | Doelreserve — voor voorziene uitgaven met bestemming | Vakantie, nieuwe auto, verbouwing |

---

## Groei (Growth)

Geld dat rendeert buiten de dagelijkse stroom.

| Bucket | Omschrijving | Voorbeelden |
|---|---|---|
| Financieel | Geld werkt via financiële markten | Beleggen, ETF, spaarrekening |
| Reëel | Geld zit vast in fysiek bezit | Vastgoed, fysieke bezittingen |

> Rendement van Groei stroomt terug als Inkomen Variabel — rente en opbrengst zijn nooit gegarandeerd.

---

## Activaties

Activering = passief geld (Reserves of Groei) dat in beweging komt en een nieuwe stroom opent.

**Vanuit Reserves (geparkeerd → actief)**

| Activatie | Nieuwe stroom |
|---|---|
| Reserves Niet gepland → Needs Vast | Vaste lasten gedekt bij inkomstendip |
| Reserves Niet gepland → Needs Variabel | Onverwachte kosten gedekt |
| Reserves Gepland → Needs Variabel | Geplande aankoop of investering |
| Reserves Gepland → Groei Reëel | Fysiek bezit dat inkomen gaat genereren |
| Reserves Gepland → Groei Financieel | Belegging die rendement gaat genereren |

**Vanuit Groei (renderend → nieuwe stroom)**

| Activatie | Inkomen stroom | Vermogensopbouw |
|---|---|---|
| Groei Reëel | Huurinkomsten → Inkomen Variabel | Waardestijging → Vermogensbalans |
| Groei Financieel | Dividend, rente → Inkomen Variabel | Portfoliogroei → Vermogensbalans |

---

## Vrij besteedbaar

Uitkomst van het systeem — geen bestemming, maar resultaat.

`Vrij besteedbaar = Inkomen - Needs - Wants - Reserves - Groei`

Wat overblijft is écht vrij. Niet "waarschijnlijk vrij" — de rest is al gedekt.
