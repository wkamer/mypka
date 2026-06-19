---
status: raw
datum: 2026-05-11
---

# I-Functionele rekeninglaag in de methodiek

## Idee

Het geldsysteem expliciet modelleren als twee lagen: een functionele laag (de 4 hoofdgeldstromen) en een fysieke laag (de rekeningen). Elke rekening krijgt één functioneel label. Dit wordt een vast onderdeel van de methodiek.

## Model

```
Geldsysteem
├── Functionele laag  → 4 hoofdgeldstromen (wat geld doet)
└── Fysieke laag      → rekeningen (waar geld staat)
```

## Functionele rekeningen (standaard)

| Rekening | Functioneel label | Hoofdgeldstroom |
|---|---|---|
| Inkomstrekening | Inkomen komt hier binnen | Inkomen |
| Vaste lastenrekening | Vaste lasten worden hiervan afgeschreven | Bestedingen |
| Leefgeldrekening | Variabele dagelijkse uitgaven | Bestedingen |
| Bufferrekening | Noodbuffer — niet voor dagelijks gebruik | Bescherming |
| Spaardoelrekening | Per spaardoel één rekening | Groei |

## Implicaties voor de methodiek

- Toevoegen aan SOP-001 als vast begrip ("functionele rekening")
- Verwerken in SOP-002 (Scan): rekeningen in kaart brengen als fysieke laag
- Verwerken in SOP-003 (Reset): rekeningontwerp is altijd gebaseerd op functionele labels
- Basis voor visualisatie (zie I-Visualisatie geldsysteem scan.md)

## Open vragen

- Hoe ga je om met rekeningen die meerdere functies hebben (nog niet ideaal ingericht)?
- Aparte sectie in de Scan voor de fysieke laag?
