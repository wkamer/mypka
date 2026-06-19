# B-022 Owner Terminology Refactor Proposal

**Datum:** 2026-06-03
**Opgesteld door:** Larry
**Status:** Concept — wacht op Owner's explicit approval
**Geen wijzigingen uitgevoerd**

---

## 1. Korte conclusie

GL-014 AI Team Governance bevat 25+ persoonsnaam-specifieke governance-termen ("Walter", "Walter's akkoord", "Goedgekeurd door Walter"). Dit zijn forwardlooking governance-termen in het authoritative document, geen historische vermeldingen. Ze moeten worden vervangen door rolgebaseerde Owner-terminologie.

De drie PKM-templates die "Walter" bevatten (habit.md, person.md, key-element.md) bevatten persoonlijke content-beschrijvingen — geen governance-termen. Die vallen buiten scope van dit voorstel.

Historische documenten (deliverables, session logs, team_log, changelog-entries) blijven ongewijzigd.

---

## 2. Waarom Owner beter is dan persoonsnaam

| Risico bij persoonsnaam | Oplossing met Owner |
|---|---|
| Governance wordt persoonsgebonden | Governance is rolgebonden — overdraagbaar |
| Toekomstige templates verwijzen naar een persoon | Templates verwijzen naar een rol |
| Bij eigenaarswisseling moet elk document herschreven worden | Eén definitiepunt aanpassen volstaat |
| AI-agents nemen persoonsnaam over als instructief signaal | Rolterm is neutraal en contextonafhankelijk |
| Auditbaarheid is afhankelijk van naamherkenning | Owner is een formele rol in elk document |

---

## 3. Geraakte authoritative documenten

| Bestand | Walter-vermeldingen | Type |
|---|---|---|
| `GL-014_AI Team Governance.md` | 25+ | Authoritative governance |
| `gl-index.md` | 0 | Geen wijziging nodig |
| `SOP-008_Read own journal before task.md` | 0 | Geen wijziging nodig |
| `SOP-009_Write journal entry after task.md` | 0 | Geen wijziging nodig |

---

## 4. Geraakte templates

| Bestand | Walter-vermelding | Type | In scope? |
|---|---|---|---|
| `Templates/habit.md` | "Walter does this" | Persoonlijke content-beschrijving | Nee — content, niet governance |
| `Templates/person.md` | "relate to Walter" | Persoonlijke content-beschrijving | Nee — content, niet governance |
| `Templates/key-element.md` | "Where does Walter stand" | Persoonlijke content-beschrijving | Nee — content, niet governance |
| Changelog-template in GL-014 | "Goedgekeurd door Walter" | Governance-template | **Ja** |

---

## 5. Voorgestelde vervangingen

| Huidige term | Nieuwe term |
|---|---|
| Walter | Owner |
| Walter's akkoord | Owner approval |
| Walter's expliciete akkoord | Owner's explicit approval |
| Walter's directe instructie | Owner's direct instruction |
| Goedgekeurd door Walter | Approved by Owner |
| Keuze Walter | Owner decision |
| Walter direct | Owner directly |
| akkoord van Walter | Owner approval |
| escaleren naar Walter | escalate to Owner directly |
| Bij conflict met Walter's directe instructie | Upon conflict with Owner's direct instruction |

**Definitiepunt (eenmalig toevoegen aan GL-014):**
> Owner = Walter Kamer. In alle procedures, governance-documenten en templates wordt de rolterm Owner gebruikt.

---

## 6. Exacte wijzigingsvoorstellen per bestand

### GL-014_AI Team Governance.md

**Pad:** `Team Knowledge/Core/Guidelines/GL-014_AI Team Governance.md`

| Regel | Huidige tekst | Voorgestelde tekst | Risico |
|---|---|---|---|
| 4 | `**Goedgekeurd door:** Walter` | `**Goedgekeurd door:** Owner (Walter Kamer)` | Geen |
| Header-blok (nieuw) | — | `**Owner definitie:** Owner = Walter Kamer. In alle procedures en templates wordt de rolterm Owner gebruikt.` | Geen |
| 12 | `...wat alleen na Walter's akkoord mag...` | `...wat alleen na Owner approval mag...` | Geen |
| 20 | `Het team mag zonder Walter's voorafgaand akkoord:` | `Het team mag zonder Owner's prior approval:` | Geen |
| 32 | `### Alleen na expliciet akkoord van Walter` | `### Alleen na explicit Owner approval` | Geen |
| 34 | `...na Walter's expliciete "akkoord" of "go":` | `...na Owner's explicit approval ("akkoord" or "go"):` | Geen |
| 60 | `- Walter's approval overslaan omdat iets "urgent" of "klein" lijkt` | `- Bypassing Owner approval because something seems "urgent" or "small"` | Geen |
| 68 | `Walter's akkoord moet expliciet zijn.` | `Owner approval must be explicit.` | Geen |
| 88 | `...vereisen expliciet akkoord van Walter en technische review door Kai.` | `...require Owner's explicit approval and technical review by Kai.` | Geen |
| 89 | `Bij twijfel: stoppen en escaleren naar Walter.` | `When in doubt: stop and escalate to Owner directly.` | Geen |
| 98 | `Larry → Walter` | `Larry → Owner` | Geen |
| 100 | `Walter direct` | `Owner directly` | Geen |
| 101 | `Walter direct` | `Owner directly` | Geen |
| 102 | `...Larry → Walter` | `...Larry → Owner` | Geen |
| 103 | `Walter direct` | `Owner directly` | Geen |
| 114 | `Goedgekeurd door Walter.` | `Approved by Owner.` | Geen |
| 121 | `"Goedgekeurd door Walter" verplicht bij alle changes...` | `"Approved by Owner" required for all changes...` | Geen |
| 141 | `1. **Walter's directe instructie** — altijd leidend` | `1. **Owner's direct instruction** — always leading` | Geen |
| 150 | `Bij conflict met Walter's directe instructie: Walter wint altijd.` | `Upon conflict with Owner's direct instruction: Owner wins always.` | Geen |
| 158 | `...mogen nooit zonder Walter's akkoord worden gewijzigd:` | `...may never be changed without Owner approval:` | Geen |
| 177-185 | `Walter` (kolom Final approval, 9 rijen) | `Owner` | Geen |

**Regel 191 (Changelog-entry) — NIET wijzigen:**
> `2026-06-03 (Larry, B-004): ... Goedgekeurd door Walter.`

Dit is een historische changelog-entry. Die blijft ongewijzigd conform de instructie.

**Approval nodig:** Ja — GL-014 is een authoritative Guideline.
**Risico:** Laag. Alleen terminologie, geen inhoudelijke wijziging.

---

## 7. Wat blijft historisch ongemoeid

De volgende documenten en records worden **niet** aangepast:

- Alle deliverables in `Deliverables/20260603_Core_AI Team Audit Report/`
- Alle session logs in `Team Knowledge/Core/session-logs/`
- Alle team_log entries in databases
- Bestaande changelog-entries in GL-014 en andere bestanden
- Oude auditrapporten
- PKM templates (habit.md, person.md, key-element.md) — persoonlijke content, geen governance
- AGENT.md bestanden — vallen buiten scope van dit voorstel
- SOP's — geen persoonsnaam-governance-termen aangetroffen

---

## 8. Advies van Larry

**Uitvoeren.** Dit is een lage-risico, hoge-waarde verbetering. GL-014 is het authoritative governance-document van het team — het moet rolgebaseerd zijn, niet persoonsgebonden.

**Volgorde aanbevolen:**
1. Definitiepunt toevoegen bovenaan GL-014 (Owner = Walter Kamer)
2. Alle governance-termen in GL-014 vervangen
3. Changelog toevoegen aan GL-014 voor deze wijziging
4. team_log en session log bijwerken per GL-014 §6

**Aandachtspunt:** Toekomstige documenten — nieuwe SOPs, Guidelines, Workstreams, change proposals — moeten direct Owner-terminologie gebruiken. Dit hoeft niet apart te worden opgedragen; het volgt automatisch uit GL-014 zodra het bijgewerkt is.

**CLAUDE.md:** De governance-approval-termen in CLAUDE.md zijn niet aangetroffen in de grep (de phrasing wijkt af). Als Walter wil dat ook CLAUDE.md wordt bijgewerkt, verdient dat een apart voorstel.

---

## 9. Besluitpunt voor Owner

| Besluit | Advies | Opties |
|---|---|---|
| B-022 GL-014 Owner refactor uitvoeren | Ja — laag risico, hoog nut | a) Volledig akkoord b) Alleen changelog-template c) Afwijzen |
| CLAUDE.md ook bijwerken | Apart voorstel aanbevolen | a) Meenemen in B-022 b) Apart als B-023 c) Niet doen |
| PKM templates (habit, person, key-element) | Buiten scope — persoonlijke content | a) Laten zoals het is b) Aparte review |

---

## 10. Bevestiging dat niets is aangepast

- GL-014_AI Team Governance.md: **niet aangepast**
- gl-index.md: **niet aangepast**
- Geen SOP's aangepast
- Geen AGENT.md's aangepast
- Geen Workstreams aangemaakt
- Geen databases gewijzigd
- Geen bestanden verwijderd
- Dit voorstel staat uitsluitend als concept in de Deliverables-map

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-022-owner-terminology-refactor-proposal.md`*
