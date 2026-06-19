# GL-011 — Project Documentation Conventions

**Geldig voor:** alle agents die `project.md` aanmaken of bijwerken
**Laatste update:** 2026-05-26

---

## Doel

Elke `project.md` is de SSOT voor een project. Deze GL beschrijft de verplichte conventies voor documentatie binnen die bestanden — zodat elk project consistent, doorzoekbaar en direct bruikbaar is.

---

## Mail links in de tijdlijn

Wanneer een tijdlijn-entry refereert aan een e-mail, wordt de mail-ID altijd als klikbare link opgenomen.

**Format:**
```
[19eXXXXXXXXXXXXXX](https://mail.google.com/mail/u/0/#all/19eXXXXXXXXXXXXXX)
```

**Regels:**
- Altijd via `wkamer@gmail.com` (u/0) als basis voor de link
- Meerdere mails op één datum: kommagescheiden achter het datumkopje
- Bij twijfel of een mail bij het project hoort: eerst bevestiging vragen aan de owner
- Geldt voor alle domeinen: Personal, Kamer E-commerce, Geldstroom Regie

**Voorbeeld:**
```markdown
**26 mei 2026** (mails [19e63cacf7ae85f0](https://mail.google.com/mail/u/0/#all/19e63cacf7ae85f0), [19e6405054e693c6](https://mail.google.com/mail/u/0/#all/19e6405054e693c6))
Jesse Voerman stelt MDO-data voor.
```

---

## Tijdlijn-structuur

Elke tijdlijn-entry volgt dit format:

```markdown
**DD mmm YYYY** (mail/mails [id](url))
Beschrijving in 1–3 zinnen. Wie deed wat, wat was het resultaat, wat stond open.
```

- Datumkopje in **bold**
- Mail-IDs direct achter de datum tussen haakjes, als links
- Beschrijving feitelijk en beknopt — geen interpretaties
- Nieuwe entries altijd chronologisch onderaan de sectie

---

## Verplichte secties in project.md

| Sectie | Verplicht | Toelichting |
|---|---|---|
| `## Doel` | Ja | Wat wil dit project bereiken |
| `## Context` | Aanbevolen | Achtergrond die niet uit de tijdlijn volgt |
| `## Betrokkenen` | Ja (als extern) | Tabel per partij met naam, rol, contactinfo |
| `## Tijdlijn` | Ja | Chronologisch, met mail-links |
| `## Huidige stand` | Ja | Actuele status — datum vermelden |
| `## Lopende trajecten` | Indien van toepassing | Per traject: tabel betrokkenen + stand + wachten op + risico |
| `## Open vragen` | Ja | Bulleted lijst van onbeantwoorde vragen |
| `## Aanbeveling` | Indien van toepassing | Concrete volgende actie voor de owner |
| `## Status` | Ja | Actief / Wachten / Afgerond + korte toelichting |

---

## Eigenaarschap

- **Marcus** — primaire eigenaar van deze conventies; past toe bij aanmaken en bijhouden van project.md
- **Sienna** — past toe bij persoonlijke projecten en mail-updates
- Overige specialists — raadplegen deze GL bij elke project.md-write
