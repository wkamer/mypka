# B-005C — Kamer E-commerce Workstream Language Compliance Proposal v0.2

**Status:** Proposal only — no implementation
**Version:** v0.2 (supersedes v0.1)
**Date:** 2026-06-04
**Author:** Larry (orchestrator)
**Backlog item:** B-005C (team_tasks id: 62)
**Requires approval by:** Owner Walter Kamer — see Approval Gate

---

## Revision Notes

- **Markdown fence integrity fixed (Items 3 and 6):** v0.1 used triple-backtick outer fences around blocks that themselves contained triple-backtick code fences. v0.2 replaces those outer fences with four-backtick fences to eliminate the ambiguity.
- **Filename rename removed from B-005C scope:** v0.1 listed filename rename as in-scope in §4 while Item 17 treated it as a separate decision item — inconsistent. v0.2 removes filename rename from B-005C execution scope entirely. Items 1–16 are the only B-005C core execution scope. Item 17 is moved to §6 as a deferred future candidate.
- **Decision options updated:** Option A now covers Items 1–16 only. Filename rename requires a separate future proposal.
- **Post-check plan added (§8):** Includes Markdown fence integrity verification and WS-001 filename unchanged confirmation.

---

## 1. Purpose

The CLAUDE.md language rule states that internal system-file content should be in English. WS-001 and its index file were created in Dutch. This proposal identifies all Dutch text in those files and provides exact English replacements. No functional changes are proposed — only language compliance.

---

## 2. Governance Basis

| Item | Reference |
|---|---|
| Language rule for system files | CLAUDE.md — "Store in EN, display in NL" |
| Proposal-only discipline | SOP-015 |
| No implementation without Owner approval | GL-014 §1, SOP-015 Step 5 |

---

## 3. Files Inspected

| File | Path |
|---|---|
| WS-001 | `Team Knowledge/Kamer E-commerce/Workstreams/WS-001_Kamer E-commerce operationeel procesframework.md` |
| Workstream index | `Team Knowledge/Kamer E-commerce/Workstreams/workstream-index.md` |

No other files were read. No execution-related files were accessed.

---

## 4. Scope Boundaries

**In scope:**
- Translating Dutch prose, labels, headers, and metadata in WS-001 to English (Items 1–16)
- Translating Dutch column headers and the Dutch title entry in workstream-index.md (Item 16)

**Out of scope:**
- Filename rename — deferred as a separate future candidate (see §6)
- Functional changes to the process (phases, steps, criteria, routing, agents)
- Adding or removing any process step, rule, or agent
- Any SOP, GL, AGENT.md, or other system file
- Database records, scripts, credentials, or `.env` files
- Any other Kamer E-commerce domain file
- Vault-wide grep or wikilink search

**Confirmed: language compliance only.** No process redesign, no new rules, no structural changes. The WS-001 filename remains unchanged.

---

## 5. Proposed Changes

Each item includes: location, exact current text, exact proposed replacement, and rationale.

Note on `**Eigenaar:**`: "Eigenaar" means "owner" in the sense of "responsible phase lead." To avoid ambiguity with "Owner Walter Kamer" (the governance role), this proposal uses `**Lead:**` as the English translation throughout. If Owner Walter Kamer prefers `**Owner:**`, that can be applied instead — the rationale is identical for all occurrences.

---

### Item 1 — File Header Block

**File:** WS-001
**Location:** Lines 1–9

**Current text:**
```
# WS-001 — Kamer E-commerce Operationeel Procesframework

**Domein:** Kamer E-commerce
**Brand:** Tricolarae
**Markt:** Verenigde Staten
**Supplier:** Trendsi (US-gebaseerd)
**Fase:** 1 — Generic Dropshipping
**Aangemaakt:** 2026-05-19
**Eigenaar:** Nova (operationeel) + Vera (strategisch)
```

**Proposed replacement:**
```
# WS-001 — Kamer E-commerce Operational Process Framework

**Domain:** Kamer E-commerce
**Brand:** Tricolarae
**Market:** United States
**Supplier:** Trendsi (US-based)
**Phase:** 1 — Generic Dropshipping
**Created:** 2026-05-19
**Lead:** Nova (operational) + Vera (strategic)
```

**Rationale:** All metadata labels translated. "Kamer E-commerce" remains (proper name). "Tricolarae" remains (brand name). "Trendsi" remains (supplier name). "Generic Dropshipping" remains (English business term already in use).

---

### Item 2 — Purpose Section

**File:** WS-001
**Location:** `## Doel` section

**Current text:**
```
## Doel

Dit document beschrijft het volledige operationele proces van Kamer E-commerce — van product discovery tot post-sale. Het is het fundament voor alle SOPs, workstreams en automatisering die hierop gebouwd worden.

Elke specialist weet wat zijn of haar stap is, wat de input is, wat de output is, en aan wie die output gaat.
```

**Proposed replacement:**
```
## Purpose

This document describes the full operational process of Kamer E-commerce — from product discovery to post-sale. It is the foundation for all SOPs, workstreams, and automation built on top of it.

Each specialist knows what their step is, what the input is, what the output is, and to whom that output goes.
```

**Rationale:** Direct translation. No functional change.

---

### Item 3 — Process Overview Section Header and Diagram

**File:** WS-001
**Location:** `## Procesoverzicht` section with code block

**Note:** This block contains an internal triple-backtick code fence. The outer fence below uses four backticks to avoid ambiguity.

**Current text:**

````
## Procesoverzicht

```
Fase 1   Product Discovery          Bo + owner
   ↓
Fase 2   Product Validatie          Bo
   ↓ Go-signaal
Fase 2b  Margin Check               Nova
   ↓ Break-even CPA + goedkeuring
Fase 3   Supplier Setup & Listing   Nova + Sasha
   ↓ Listing klaar
Fase 4   Store Listing              Sasha
   ↓ Live
Fase 5   Ads Intelligence           Zara
   ↓ Creative briefs goedgekeurd door owner
Fase 6   Campagne Launch            n8n / Kai
   ↓ Campagne actief
Fase 7   Operationele Monitoring    Nova
Fase 8   Performance Analyse        Zara
   ↓ Scale / Kill / Rotate
Fase 9   Strategische Beslissing    Vera + owner
   ↓
Fase 10  Post-Sale & Retentie       Nova + Sasha
```
````

**Proposed replacement:**

````
## Process Overview

```
Phase 1   Product Discovery          Bo + owner
   ↓
Phase 2   Product Validation         Bo
   ↓ Go signal
Phase 2b  Margin Check               Nova
   ↓ Break-even CPA + approval
Phase 3   Supplier Setup & Listing   Nova + Sasha
   ↓ Listing ready
Phase 4   Store Listing              Sasha
   ↓ Live
Phase 5   Ads Intelligence           Zara
   ↓ Creative briefs approved by owner
Phase 6   Campaign Launch            n8n / Kai
   ↓ Campaign active
Phase 7   Operational Monitoring     Nova
Phase 8   Performance Analysis       Zara
   ↓ Scale / Kill / Rotate
Phase 9   Strategic Decision         Vera + owner
   ↓
Phase 10  Post-Sale & Retention      Nova + Sasha
```
````

**Rationale:** "Fase" → "Phase" throughout. Dutch labels in diagram translated. "Scale / Kill / Rotate" already English — unchanged. Agent names unchanged (proper names).

---

### Item 4 — Phase 1: Product Discovery

**File:** WS-001
**Location:** `## Fase 1 — Product Discovery` section

**Current text:**
```
## Fase 1 — Product Discovery

**Eigenaar:** Bo (gesteund door de owner)
**Trigger:** behoefte aan nieuwe producten in het assortiment

**Bronnen:**
- Trendsi app — browse op categorie en trending items
- Meta Ad Library — welke kledingproducten worden actief geadverteerd?
- TikTok Creative Center — trending fashion producten
- Competitor stores — welke producten zetten concurrenten in?

**Output:** longlist van kandidaat-producten met bron en eerste indruk

**Trigger naar fase 2:** minimaal 3–5 kandidaten die passen bij Tricolarae (gevoel, stijl, doelgroep)
```

**Proposed replacement:**
```
## Phase 1 — Product Discovery

**Lead:** Bo (supported by the owner)
**Trigger:** need for new products in the assortment

**Sources:**
- Trendsi app — browse by category and trending items
- Meta Ad Library — which apparel products are being actively advertised?
- TikTok Creative Center — trending fashion products
- Competitor stores — which products are competitors listing?

**Output:** longlist of candidate products with source and first impression

**Trigger to phase 2:** minimum 3–5 candidates that fit Tricolarae (feel, style, target audience)
```

**Rationale:** Direct translation. No functional change.

---

### Item 5 — Phase 2: Product Validation

**File:** WS-001
**Location:** `## Fase 2 — Product Validatie` section

**Current text:**
```
## Fase 2 — Product Validatie

**Eigenaar:** Bo
**Trigger:** longlist ontvangen van fase 1

**Stappen:**
1. Must-Have criteria doorlopen per product — zie [[KE-Products]]
2. Nice-to-Have score toekennen (0–5)
3. Tricolarae-specifieke filters toepassen (merkfit, outfit-context, seizoen)
4. Go / No-Go beslissing documenteren met onderbouwing

**Output:** shortlist met alleen Go-producten + onderbouwing per product

**Trigger naar fase 2b:** Go-signaal van Bo
```

**Proposed replacement:**
```
## Phase 2 — Product Validation

**Lead:** Bo
**Trigger:** longlist received from phase 1

**Steps:**
1. Run Must-Have criteria for each product — see [[KE-Products]]
2. Assign Nice-to-Have score (0–5)
3. Apply Tricolarae-specific filters (brand fit, outfit context, season)
4. Document Go / No-Go decision with rationale

**Output:** shortlist of Go products only + rationale per product

**Trigger to phase 2b:** Go signal from Bo
```

**Rationale:** Direct translation. No functional change.

---

### Item 6 — Phase 2b: Margin Check

**File:** WS-001
**Location:** `## Fase 2b — Margin Check` section

**Note:** This block contains an internal triple-backtick code fence (the pricing formula). The outer fence below uses four backticks to avoid ambiguity.

**Current text:**

````
## Fase 2b — Margin Check

**Eigenaar:** Nova
**Trigger:** Go-signaal van Bo + productdata (Trendsi groothandelsprijs)

**Pricing formula:**
```
Verkoopprijs = Trendsi prijs + shipping + Shopify/Stripe fees + verwachte retourkosten + doelmarge
```

- Target contribution margin: ≥20% per order
- Break-even CPA berekenen → dit getal gaat direct naar Zara
- Producten onder 20% margin: terug naar Bo met bevinding (te duur om te sourcen bij deze verkoopprijs)

**Output:** goedgekeurde verkoopprijs per product + break-even CPA voor Zara

**Trigger naar fase 3:** margin goedgekeurd
````

**Proposed replacement:**

````
## Phase 2b — Margin Check

**Lead:** Nova
**Trigger:** Go signal from Bo + product data (Trendsi wholesale price)

**Pricing formula:**
```
Selling price = Trendsi price + shipping + Shopify/Stripe fees + expected return costs + target margin
```

- Target contribution margin: ≥20% per order
- Calculate break-even CPA → this figure goes directly to Zara
- Products below 20% margin: return to Bo with finding (too expensive to source at this selling price)

**Output:** approved selling price per product + break-even CPA for Zara

**Trigger to phase 3:** margin approved
````

**Rationale:** Direct translation. The formula label inside the code fence is translated for clarity. Numeric criteria unchanged.

---

### Item 7 — Phase 3: Supplier Setup & Listing Preparation

**File:** WS-001
**Location:** `## Fase 3 — Supplier Setup & Listing Voorbereiding` section

**Current text:**
```
## Fase 3 — Supplier Setup & Listing Voorbereiding

**Eigenaar:** Nova (setup) + Sasha (Shopify uitvoering)
**Trigger:** margin goedgekeurd

**Stappen:**
1. Product importeren vanuit Trendsi app naar Shopify (Sasha)
2. Verkoopprijs instellen op basis van fase 2b (Sasha)
3. Supplier scorecard entry aanmaken voor dit product (Nova)
4. Dispatch time en stock beschikbaarheid bevestigen bij Trendsi (Nova)

**Output:** product klaar in Shopify (nog niet gepubliceerd), scorecard actief

**Trigger naar fase 4:** product live-klaar in Shopify
```

**Proposed replacement:**
```
## Phase 3 — Supplier Setup & Listing Preparation

**Lead:** Nova (setup) + Sasha (Shopify execution)
**Trigger:** margin approved

**Steps:**
1. Import product from Trendsi app to Shopify (Sasha)
2. Set selling price based on phase 2b (Sasha)
3. Create supplier scorecard entry for this product (Nova)
4. Confirm dispatch time and stock availability with Trendsi (Nova)

**Output:** product ready in Shopify (not yet published), scorecard active

**Trigger to phase 4:** product ready to go live in Shopify
```

**Rationale:** Direct translation. No functional change.

---

### Item 8 — Phase 4: Store Listing

**File:** WS-001
**Location:** `## Fase 4 — Store Listing` section

**Current text:**
```
## Fase 4 — Store Listing

**Eigenaar:** Sasha
**Trigger:** product klaar in Shopify

**Stappen:**
1. Producttitel schrijven — geen leveranciersnamen, Tricolarae-toon
2. Productbeschrijving en copy
3. Afbeeldingen controleren op kwaliteit en merkfit
4. Levertijdverwachting transparant vermeld (Trendsi levert 3–7 dagen in VS)
5. Product publiceren

**Output:** live listing op Tricolarae

**Trigger naar fase 5:** listing live
```

**Proposed replacement:**
```
## Phase 4 — Store Listing

**Lead:** Sasha
**Trigger:** product ready in Shopify

**Steps:**
1. Write product title — no supplier names, Tricolarae tone
2. Product description and copy
3. Check images for quality and brand fit
4. Delivery time expectation clearly stated (Trendsi delivers 3–7 days in US)
5. Publish product

**Output:** live listing on Tricolarae

**Trigger to phase 5:** listing live
```

**Rationale:** Direct translation. No functional change.

---

### Item 9 — Phase 5: Ads Intelligence

**File:** WS-001
**Location:** `## Fase 5 — Ads Intelligence` section

**Current text:**
```
## Fase 5 — Ads Intelligence

**Eigenaar:** Zara
**Trigger:** listing live + break-even CPA ontvangen van Nova

**Stappen:**
1. Awareness level bepalen voor dit product in de US-markt
2. Market sophistication stage bepalen via Meta Ad Library analyse
3. Angle strategie: welke hoeken testen, in welke volgorde
4. Creative brief per angle: hook, copy-structuur, visuele richting
5. Campagnestructuur: ABO testfase, budget, doelgroep, exclusies

**Output:** creative briefs + campagnestructuur — ter goedkeuring aan owner

**Trigger naar fase 6:** owner keurt creative briefs goed
```

**Proposed replacement:**
```
## Phase 5 — Ads Intelligence

**Lead:** Zara
**Trigger:** listing live + break-even CPA received from Nova

**Steps:**
1. Determine awareness level for this product in the US market
2. Determine market sophistication stage via Meta Ad Library analysis
3. Angle strategy: which angles to test, in which order
4. Creative brief per angle: hook, copy structure, visual direction
5. Campaign structure: ABO test phase, budget, target audience, exclusions

**Output:** creative briefs + campaign structure — for approval by owner

**Trigger to phase 6:** owner approves creative briefs
```

**Rationale:** Direct translation. No functional change.

---

### Item 10 — Phase 6: Campaign Launch

**File:** WS-001
**Location:** `## Fase 6 — Campagne Launch` section

**Current text:**
```
## Fase 6 — Campagne Launch

**Eigenaar:** n8n / Kai
**Trigger:** goedgekeurde creative briefs van Zara

**Parameters (testfase):**
- ABO, klein testbudget
- 6–8 creatives
- Minimaal 3–5 dagen draaien vóór eerste beoordeling

**Output:** actieve testcampagne in Meta

**Trigger naar fase 7 + 8:** campagne actief
```

**Proposed replacement:**
```
## Phase 6 — Campaign Launch

**Lead:** n8n / Kai
**Trigger:** approved creative briefs from Zara

**Parameters (test phase):**
- ABO, small test budget
- 6–8 creatives
- Minimum 3–5 days running before first review

**Output:** active test campaign in Meta

**Trigger to phases 7 + 8:** campaign active
```

**Rationale:** Direct translation. No functional change.

---

### Item 11 — Phase 7: Operational Monitoring

**File:** WS-001
**Location:** `## Fase 7 — Operationele Monitoring` section

**Current text:**
```
## Fase 7 — Operationele Monitoring

**Eigenaar:** Nova
**Trigger:** campagne actief + eerste orders binnengekomen

**Dagelijks:**
1. Orders zonder dispatch bevestiging na 48u → escaleren naar Trendsi
2. Leveringen buiten window (>7 dagen) → proactief klantcontact
3. Nieuwe retourverzoeken → oorzaak registreren

**Maandelijks:** Trendsi scorecard updaten (dispatch time, defect rate, communicatie)

**Output:** operationele gezondheidsrapportage, return-analyse
```

**Proposed replacement:**
```
## Phase 7 — Operational Monitoring

**Lead:** Nova
**Trigger:** campaign active + first orders received

**Daily:**
1. Orders without dispatch confirmation after 48h → escalate to Trendsi
2. Deliveries outside window (>7 days) → proactive customer contact
3. New return requests → register cause

**Monthly:** Update Trendsi scorecard (dispatch time, defect rate, communication)

**Output:** operational health report, return analysis
```

**Rationale:** Direct translation. No functional change.

---

### Item 12 — Phase 8: Performance Analysis

**File:** WS-001
**Location:** `## Fase 8 — Performance Analyse` section

**Current text:**
```
## Fase 8 — Performance Analyse

**Eigenaar:** Zara
**Trigger:** minimaal 3–5 campagnedagen + voldoende data

**Kill-criteria:**
- Hook rate <15% na 1.000+ impressies
- CTR <1% zonder ATC na 1.500 impressies

**Keep-criteria:**
- ROAS >break-even voor 3+ opeenvolgende dagen

**Scale-criteria:**
- Duplicate winner naar CBO
- Budget +20–30% per stap, niet meer

**Output:** scale / kill / rotate beslissing per creative + winner-analyse voor hook database

**Trigger naar fase 9:** winnend product bevestigd of beslissing tot stop
```

**Proposed replacement:**
```
## Phase 8 — Performance Analysis

**Lead:** Zara
**Trigger:** minimum 3–5 campaign days + sufficient data

**Kill criteria:**
- Hook rate <15% after 1,000+ impressions
- CTR <1% without ATC after 1,500 impressions

**Keep criteria:**
- ROAS >break-even for 3+ consecutive days

**Scale criteria:**
- Duplicate winner to CBO
- Budget +20–30% per step, no more

**Output:** scale / kill / rotate decision per creative + winner analysis for hook database

**Trigger to phase 9:** winning product confirmed or decision to stop
```

**Rationale:** Direct translation. Numeric thresholds and business logic unchanged.

---

### Item 13 — Phase 9: Strategic Decision

**File:** WS-001
**Location:** `## Fase 9 — Strategische Beslissing` section

**Current text:**
```
## Fase 9 — Strategische Beslissing

**Eigenaar:** Vera + owner
**Trigger:** performance analyse afgerond

**Vragen die altijd op tafel komen:**
1. Klopt de contribution margin met de doelstelling?
2. Beweegt de LTV:CAC richting 3:1?
3. Is dit product een kandidaat voor branded dropshipping (fase 2 groeipad)?
4. Rechtvaardigt de performance meer budget of een productuitbreiding?

**Output:** go for scale / stop / branded dropshipping transitie

**Fase-transitiecheck (Vera):** bij elk winnend product expliciet toetsen aan [[KE-Strategy]] — wanneer zijn we klaar voor de volgende fase?
```

**Proposed replacement:**
```
## Phase 9 — Strategic Decision

**Lead:** Vera + owner
**Trigger:** performance analysis completed

**Standing review questions:**
1. Is the contribution margin in line with the target?
2. Is LTV:CAC moving toward 3:1?
3. Is this product a candidate for branded dropshipping (phase 2 growth path)?
4. Does performance justify more budget or a product expansion?

**Output:** go for scale / stop / branded dropshipping transition

**Phase transition check (Vera):** for every winning product, explicitly assess against [[KE-Strategy]] — when are we ready for the next phase?
```

**Rationale:** Direct translation. No functional change.

---

### Item 14 — Phase 10: Post-Sale & Retention

**File:** WS-001
**Location:** `## Fase 10 — Post-Sale & Retentie` section

**Current text:**
```
## Fase 10 — Post-Sale & Retentie

**Eigenaar:** Nova (operationeel) + Sasha (technisch)
**Trigger:** order geleverd

**Stappen:**
1. Klant ontvangt tracking automatisch via Shopify
2. Bij vertraging: proactief bericht vóór klacht
3. Retour afhandelen via Trendsi-retourbeleid
4. Return-oorzaak documenteren
5. Bij structureel patroon: productfeedback naar Bo + Nova voor listingaanpassing

**Output:** klanttevredenheid, schone return-data, structurele verbeteringen
```

**Proposed replacement:**
```
## Phase 10 — Post-Sale & Retention

**Lead:** Nova (operational) + Sasha (technical)
**Trigger:** order delivered

**Steps:**
1. Customer receives tracking automatically via Shopify
2. On delay: proactive message before complaint
3. Handle return via Trendsi return policy
4. Document return cause
5. On structural pattern: product feedback to Bo + Nova for listing adjustment

**Output:** customer satisfaction, clean return data, structural improvements
```

**Rationale:** Direct translation. No functional change.

---

### Item 15 — Open Items Section

**File:** WS-001
**Location:** `## Open punten` section

**Current text:**
```
## Open punten

- Bo's AGENT.md updaten met Must-Have criteria en discovery-bronnen (Pax → Nolan)
- Trendsi Shopify app installeren en koppeling testen (Sasha + Kai)
- Eerste margin check uitvoeren op huidig assortiment (Nova)
- Campagne launch via n8n bouwen (Kai) — pas na eerste goedgekeurde creative brief
- Producttitels in Shopify herschrijven — leveranciersnamen eruit (Sasha)
- Placeholder producten verwijderen uit store (Sasha)
```

**Proposed replacement:**
```
## Open Items

- Update Bo's AGENT.md with Must-Have criteria and discovery sources (Pax → Nolan)
- Install Trendsi Shopify app and test connection (Sasha + Kai)
- Run first margin check on current assortment (Nova)
- Build campaign launch via n8n (Kai) — only after first approved creative brief
- Rewrite product titles in Shopify — remove supplier names (Sasha)
- Remove placeholder products from store (Sasha)
```

**Rationale:** Direct translation. No functional change to the action items.

---

### Item 16 — workstream-index.md Column Headers and Title Entry

**File:** workstream-index.md
**Location:** Full file

**Current text:**
```
# Workstream Index — Kamer E-commerce

| Nr | Titel | Bestand | Status |
|---|---|---|---|
| WS-001 | Kamer E-commerce operationeel procesframework | WS-001_Kamer E-commerce operationeel procesframework.md | Active |
```

**Proposed replacement:**
```
# Workstream Index — Kamer E-commerce

| Nr | Title | File | Status |
|---|---|---|---|
| WS-001 | Kamer E-commerce operational process framework | WS-001_Kamer E-commerce operationeel procesframework.md | Active |
```

**Note:** The filename cell retains the current Dutch filename. The WS-001 filename is not renamed as part of B-005C. See §6.

**Rationale:** Column headers translated. Title entry translated. Filename cell unchanged.

---

## 6. Deferred Items — Not Part of B-005C

### Item 17 — Filename Rename (Deferred Future Candidate)

**Status:** Deferred. Not part of B-005C v0.2 execution.

**Current filename:** `WS-001_Kamer E-commerce operationeel procesframework.md`
**Candidate future filename:** `WS-001_Kamer E-commerce operational process framework.md`

**Why deferred:** Renaming a file requires a vault-wide wikilink search and update, which is a broader operation than language compliance within the file. This is a separate scope with its own risks and requires a separate proposal and Owner approval.

**Action:** No filename rename, no grep, no wikilink update may be executed as part of B-005C. If Owner Walter Kamer wishes to proceed with the filename rename, it requires a new dedicated proposal.

---

## 7. Risks and Mitigations

| Risk | Level | Mitigation |
|---|---|---|
| Translation introduces unintended meaning change | Low | All replacements are direct translations; no paraphrasing |
| "Lead" vs "Owner" for phase metadata causes confusion | Low | Proposal uses "Lead" consistently; noted in §5 preamble |
| Numeric thresholds or business logic changed accidentally | Very low | All numeric values verified unchanged in this proposal |
| Markdown fence in WS-001 breaks on edit (pricing formula, diagram) | Low | Post-check item 3 in §8 explicitly verifies fence integrity after execution |
| Out-of-scope files accidentally modified | Very low | Scope boundary defined in §4; executor must verify |

---

## 8. Post-Check Plan

After execution (if approved), the executor must verify:

1. WS-001 exists at the canonical path and the filename is unchanged: `WS-001_Kamer E-commerce operationeel procesframework.md`
2. WS-001 file content spot-check: Phase 1 header reads `## Phase 1 — Product Discovery`, Phase 9 header reads `## Phase 9 — Strategic Decision`, `## Purpose` section present, `## Open Items` section present
3. Markdown fence integrity in WS-001: the triple-backtick code fence inside the Process Overview diagram (§ Process Overview) opens and closes correctly — confirm the diagram is rendered as a code block, not broken text; same check for the pricing formula in Phase 2b
4. workstream-index.md column headers read `Nr | Title | File | Status`
5. workstream-index.md filename cell still reads `WS-001_Kamer E-commerce operationeel procesframework.md` (unchanged)
6. No other files modified — confirm GL-014, SOP-015, CLAUDE.md, and all AGENT.md files are untouched
7. No secret values appear in the edited files

---

## 9. Owner Decision Options

| Option | Description |
|---|---|
| **A — Approve execution of Items 1–16** | Execute Items 1–16 only. WS-001 is translated in-place. workstream-index.md column headers and title entry are updated. WS-001 filename remains unchanged. |
| **B — Request amendments** | Owner returns corrections. Larry produces v0.3. No implementation until a version is approved. |
| **C — Defer** | No action taken now. B-005C remains open. |

**Future candidate — filename rename:** If Owner Walter Kamer wishes to rename WS-001 to an English filename, that requires a separate dedicated proposal covering the file rename, wikilink search, and any dependent updates. It is not part of B-005C.

**Recommended option: A.**

---

## 10. Approval Gate

No implementation may happen until Owner Walter Kamer explicitly approves this proposal.

Approving v0.1 corrections does not constitute implementation approval for v0.2. Implementation requires a separate explicit decision on the options in §9.

This document is a proposal only. No files have been created, modified, or renamed.

---

*Delivered on: 2026-06-04*
*Delivered at: Deliverables/20260603_Core_AI Team Audit Report/b-005c-workstream-language-compliance-proposal-v02.md*
