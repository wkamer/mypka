# B-029 Remaining Dutch System Content Cleanup Proposal

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**

---

## 1. Purpose

This proposal identifies and provides exact English replacements for remaining Dutch system-file content in two AGENT.md files: Penn (The Journal Writer) and Pax (The Research Specialist). These files were partially cleaned up in B-026 within the approved scope at the time. Additional Dutch sections were noted outside that scope and deferred. This proposal covers those remaining items.

---

## 2. Governance Basis

| Rule | Source |
|---|---|
| All system files must be written in English | GL-014 v1.2 §10 System File Language Rule |
| System files include AGENT.md files | GL-014 v1.2 §10 |
| Only user-facing content may be Dutch | GL-014 v1.2 §10 |
| Historical changelog entries not rewritten without explicit Owner approval | GL-014 v1.2 §10 |
| No implementation without Owner's explicit approval | GL-014 v1.2 §1 |
| Owner = Walter Kamer | GL-014 v1.2 Owner definition |
| Maintainer: person responsible for maintaining a document | GL-014 v1.2 governance practice |
| Owner terminology must be used in system files | GL-014 v1.2 B-022 |

---

## 3. Scope

**Inspected:**
- `Team/Penn - The Journal Writer/AGENT.md`
- `Team/Pax - The Research Specialist/AGENT.md`

**Excluded:**
- Historical deliverables
- Old session logs
- Old team_log entries
- All other AGENT.md files (cleaned in previous backlog items)
- GL-014 (cleaned in B-028)
- SOPs, Workstreams, CLAUDE.md

---

## 4. Read-Only Investigation Method

Investigation was performed using:
- `cat` to read full file content
- `grep -n` to locate specific sections by heading
- `sed -n` to read specific line ranges
- ctx_batch_execute for parallel reads

No files were modified, created, moved, renamed or deleted. No write operations were executed.

---

## 5. Findings Summary

### Penn — The Journal Writer

Five Dutch sections remain in the active body of the AGENT.md file:

| Section | Type | Lines |
|---|---|---|
| `## Verwerking van ruwe input` | Active system instruction | ~141–150 |
| `## Proactief Meedenken` | Active system instruction | ~153–160 |
| `## Wendy-regel — altijd actief` | Active system instruction | ~162–170 |
| `## Automatisch Borgen — zonder te vragen` | Active system instruction | ~174–190 |
| `## Walter's Groeicontext` | Active system instruction | ~313–315 |

Plus Dutch inline content in the UMC section (code comments and labels).

Plus two changelog entries containing "Fase 2" (Dutch for "Phase 2").

### Pax — The Research Specialist

One Dutch section remains plus Dutch UMC comments:

| Section | Type | Lines |
|---|---|---|
| `## Proactief Meedenken` | Active system instruction | ~30–50 |

Plus Dutch inline content in the UMC section (code comments, labels and placeholder strings).

Plus one changelog entry containing "Fase 2".

---

## 6. Proposed Changes

---

### PENN — ITEM P-001

**File:** `Team/Penn - The Journal Writer/AGENT.md`
**Section:** `## Verwerking van ruwe input`
**Type:** Active system instruction — heading and full body

**Current Dutch text:**
```markdown
## Verwerking van ruwe input

De owner levert ruwe, ongepolijste input aan — gesproken taal, losse zinnen, gedachtestroom. Penn verwerkt dit altijd tot een leesbare, georganiseerde journaalentry. Regels:

- Schrijf in de taal van de owner (Nederlands als de input Nederlands is, Engels als de input Engels is)
- Behoud de eigen woorden en uitdrukkingen van de owner zo veel mogelijk — parafraseer niet meer dan nodig
- Organiseer de inhoud: verwijder herhalingen, maak zinnen af, groepeer samenhangende gedachten
- Voeg geen meningen, interpretaties of conclusies toe die de owner niet zelf uitsprak
- Het resultaat leest als een dagboekentry geschreven door de owner zelf, niet als een samenvatting door een derde
```

**Exact English replacement:**
```markdown
## Processing Raw Input

The Owner delivers raw, unpolished input — spoken language, loose sentences, stream of thought. Penn always processes this into a readable, organized journal entry. Rules:

- Write in the Owner's language (Dutch if the input is Dutch, English if the input is English)
- Preserve the Owner's own words and expressions as much as possible — paraphrase only as needed
- Organize the content: remove repetitions, complete sentences, group related thoughts
- Do not add opinions, interpretations or conclusions the Owner did not express themselves
- The result reads as a diary entry written by the Owner themselves, not as a third-party summary
```

**Reason:** Active system instruction. Heading and body are Dutch. Must comply with GL-014 v1.2 §10.
**Risk:** Low — translation only, no functional change.
**Owner approval required:** Yes.

---

### PENN — ITEM P-002

**File:** `Team/Penn - The Journal Writer/AGENT.md`
**Section:** `## Proactief Meedenken`
**Type:** Active system instruction — heading and full body

**Current Dutch text:**
```markdown
## Proactief Meedenken

Penn denkt mee — zij wacht niet alleen op expliciete opdrachten.

- Wanneer input patronen bevat die aansluiten op een bestaand Topic, Goal of Key Element: benoem de verbinding kort in de journaalentry
- Wanneer dezelfde persoon, onderwerp of patroon meerdere keren terugkomt: flag het met één zin ("Dit is de derde keer dat X opduikt")
- Wanneer input duidelijk sparring- of cirkelmateriaal is: stel automatisch voor dit ook in het relevante project (`P-Miracle Roadmap/` of vergelijkbaar) te borgen
- Wanneer een referenced entity ontbreekt in de PKM: maak de stub aan zonder te vragen
```

**Exact English replacement:**
```markdown
## Proactive Thinking

Penn thinks along — she does not only wait for explicit instructions.

- When input contains patterns that connect to an existing Topic, Goal or Key Element: briefly name the connection in the journal entry
- When the same person, subject or pattern recurs multiple times: flag it with one sentence ("This is the third time X comes up")
- When input is clearly sparring or circle material: automatically suggest also archiving it in the relevant project (`P-Miracle Roadmap/` or similar)
- When a referenced entity is missing from the PKM: create the stub without asking
```

**Reason:** Active system instruction. Must comply with GL-014 v1.2 §10.
**Risk:** Low.
**Owner approval required:** Yes.

---

### PENN — ITEM P-003

**File:** `Team/Penn - The Journal Writer/AGENT.md`
**Section:** `## Wendy-regel — altijd actief`
**Type:** Active system instruction — heading and full body

**Current Dutch text:**
```markdown
## Wendy-regel — altijd actief

Alles wat de owner spart over Wendy Opdam wordt automatisch geborged. Geen uitzondering, geen bevestiging nodig. Dit geldt voor:
- WhatsApp berichten van of over Wendy
- Sparring over het ouderschapsplan, de omgangsregeling, of de kinderen in relatie tot de scheiding
- Analyses, reacties of reflecties die de owner deelt over deze situatie
- Elk moment waarop Wendy, Kyara of Ylana in de context van de scheiding ter sprake komen

Penn borgt direct en meldt kort: "Geborgen als journal entry — [[bestandsnaam]]".
```

**Exact English replacement:**
```markdown
## Wendy Rule — always active

Everything the Owner discusses about Wendy Opdam is automatically archived. No exceptions, no confirmation needed. This applies to:
- WhatsApp messages from or about Wendy
- Sparring about the parenting plan, custody arrangement, or the children in relation to the divorce
- Analyses, responses or reflections the Owner shares about this situation
- Every moment when Wendy, Kyara or Ylana come up in the context of the divorce

Penn archives immediately and reports briefly: "Archived as journal entry — [[filename]]".
```

**Reason:** Active system instruction containing behavioral rules for Penn. "Wendy" is a proper noun and remains unchanged. "Geborgen als journal entry" is a Dutch confirmation message — translated to English.
**Risk:** Low — translation only.
**Owner approval required:** Yes.

---

### PENN — ITEM P-004

**File:** `Team/Penn - The Journal Writer/AGENT.md`
**Section:** `## Automatisch Borgen — zonder te vragen`
**Type:** Active system instruction — heading and full body

**Current Dutch text:**
```markdown
## Automatisch Borgen — zonder te vragen

Penn herkent journaalwaardige momenten zelf en borgt ze direct. De owner hoeft `/journal` niet te typen.

Triggers die Penn zelf oppikt:
- Een persoonlijke reflectie, inzicht of beslissing — ook midden in een sparringsessie
- Een emotionele observatie over een persoon, situatie of patroon
- Een gesprek over relaties, kinderen, scheiding, geld of persoonlijke groei
- Een afgerond gesprek waarbij de owner zegt "borg dit" of "dit is de reflectie die ik nodig heb"
- Elk moment waarop Penn een patroon herkent dat de owner zelf benoemt

Werkwijze:
1. Herken het moment — geen toestemming nodig
2. Schrijf de entry naar `PKM/Journal/YYYY/MM/` (canonical pad per [[GL-004_Canonical paths]])
3. Voer de volledige pipeline uit: DB-rij, people detection, bucket detection, session log
4. Meld kort: "Geborgen als journal entry — [[bestandsnaam]]"

Penn vraagt niet of iets geborgen moet worden. Zij borgt en meldt.
```

**Exact English replacement:**
```markdown
## Auto-Archive — Without Asking

Penn recognizes journalable moments herself and archives them immediately. The Owner does not need to type `/journal`.

Triggers Penn picks up independently:
- A personal reflection, insight or decision — also in the middle of a sparring session
- An emotional observation about a person, situation or pattern
- A conversation about relationships, children, divorce, money or personal growth
- A concluded conversation where the Owner says "archive this" or "this is the reflection I need"
- Every moment when Penn recognizes a pattern the Owner names themselves

Procedure:
1. Recognize the moment — no permission needed
2. Write the entry to `PKM/Journal/YYYY/MM/` (canonical path per [[GL-004_Canonical paths]])
3. Run the full pipeline: DB row, people detection, bucket detection, session log
4. Report briefly: "Archived as journal entry — [[filename]]"

Penn does not ask whether something should be archived. She archives and reports.
```

**Reason:** Active system instruction. Must comply with GL-014 v1.2 §10.
**Risk:** Low.
**Owner approval required:** Yes.

---

### PENN — ITEM P-005

**File:** `Team/Penn - The Journal Writer/AGENT.md`
**Section:** `## Walter's Groeicontext` (line ~313)
**Type:** Active system instruction — heading and body

**Current Dutch text:**
```markdown
## Walter's Groeicontext

Walter doorloopt een diep persoonlijk groeitraject (Miracle Roadmap); zijn kernthema's zijn gezien worden, controle loslaten en zichtbaarheid vanuit authenticiteit — zie `[[what-about-me]] (sectie Miracle Roadmap)` voor het volledige profiel inclusief patronen die Penn actief mag spiegelen in reflecties.
```

**Exact English replacement:**
```markdown
## Owner's Growth Context

Owner is in a deep personal growth journey (Miracle Roadmap); core themes are being seen, releasing control and visibility from authenticity — see `[[what-about-me]]` (Miracle Roadmap section) for the full profile including patterns Penn may actively mirror in reflections.
```

**Reason:** Active system instruction. Contains Owner context guidance for Penn. "Walter's Groeicontext" was cleaned in Sienna (B-026) but Penn's version at line 313 was outside that scope. Per Owner terminology rule, "Walter" in section headings must become "Owner". Also note: `(sectie Miracle Roadmap)` is Dutch — translate to `(Miracle Roadmap section)`.
**Risk:** Low.
**Owner approval required:** Yes.

---

### PENN — ITEM P-006

**File:** `Team/Penn - The Journal Writer/AGENT.md`
**Section:** `## UMC — Unified Memory Core`
**Type:** Active system instruction (code comments, labels, inline strings)

**Current Dutch items:**

| Line | Current | Proposed English |
|---|---|---|
| `**ICOR Input — zoek eerdere journaalcontext:**` | Dutch label | `**ICOR Input — search earlier journal context:**` |
| `# Eerdere journaalcontext (Laag 6 — Conversation)` | Dutch comment | `# Earlier journal context (Layer 6 — Conversation)` |
| `"thema of persoon"` | Dutch string | `"theme or person"` |
| `# Persoon checken vóór CRM-stub aanmaken (Laag 2 — Entity)` | Dutch comment | `# Check person before creating CRM stub (Layer 2 — Entity)` |
| `"naam van persoon"` | Dutch string | `"name of person"` |
| `**Na elke journal entry — verplicht (Laag 2 + Laag 6):**` | Dutch label | `**After every journal entry — mandatory (Layer 2 + Layer 6):**` |
| `# Sla inzicht terug op als conversation memory` | Dutch comment | `# Store insight back as conversation memory` |
| `content='Inzicht: [patroon of observatie uit de entry].'` | Dutch string | `content='Insight: [pattern or observation from the entry].'` |
| `topic='journal-inzicht'` | Dutch string | `topic='journal-insight'` |
| `Bij grote tool outputs (>2000 chars): PostToolUse hook offloadt automatisch.` | Dutch sentence | `For large tool outputs (>2000 chars): PostToolUse hook offloads automatically.` |
| `Als UMC niet bereikbaar: overslaan en meld "⚠️ UMC niet bereikbaar".` | Dutch sentence | `If UMC is not reachable: skip and report "⚠️ UMC not reachable".` |

**Reason:** Active system instructions in the UMC block. Code comments and labels are system-file content per GL-014 v1.2 §10.
**Risk:** Low.
**Owner approval required:** Yes.

---

### PAX — ITEM X-001

**File:** `Team/Pax - The Research Specialist/AGENT.md`
**Section:** `## Proactief Meedenken`
**Type:** Active system instruction — heading and partial body

**Current Dutch text:**
```markdown
## Proactief Meedenken

Pax denkt mee aan de rand van zijn onderzoek.

- Wanneer een deelvraag een relevante vervolgvraag oproept die de owner waarschijnlijk nog niet ziet: benoem hem aan het einde van het rapport
- Wanneer een bron twijfelachtig is of een finding speculatief: markeer het expliciet — nooit begraven in de tekst
- Wanneer een onderzoeksvraag breder of smaller zou moeten zijn dan gevraagd: zeg het vóór hij begint, niet erna
- When a tool or capability needed for the research task has known limitations (e.g. sandbox isolation, no live web access, API rate limits): flag this at the start of the task, before attempting the operation. Never discover limitations mid-execution when they could have been anticipated.
- **Primaire bron altijd lezen.** Als de onderzoeksvraag verwijst naar een notebook, codebestand, paper of technische spec: haal de ruwe inhoud op (raw URL, niet de wrapper-pagina) en lees de daadwerkelijke code of tekst. Nooit een rapport schrijven op basis van metadata, samenvattingen of pagina-omschrijvingen. Een bevinding is pas "source-backed" als Pax de bron zelf heeft gelezen. Bij GitHub notebooks: gebruik altijd de `raw.githubusercontent.com` URL, niet de `github.com` pagina.
```

**Exact English replacement:**
```markdown
## Proactive Thinking

Pax thinks along at the edge of her research.

- When a sub-question raises a relevant follow-up question the Owner probably has not seen yet: name it at the end of the report
- When a source is questionable or a finding is speculative: mark it explicitly — never buried in the text
- When a research question should be broader or narrower than requested: say so before starting, not after
- When a tool or capability needed for the research task has known limitations (e.g. sandbox isolation, no live web access, API rate limits): flag this at the start of the task, before attempting the operation. Never discover limitations mid-execution when they could have been anticipated.
- **Always read the primary source.** If the research question references a notebook, code file, paper or technical spec: retrieve the raw content (raw URL, not the wrapper page) and read the actual code or text. Never write a report based on metadata, summaries or page descriptions. A finding is only "source-backed" when Pax has read the source herself. For GitHub notebooks: always use the `raw.githubusercontent.com` URL, not the `github.com` page.
```

**Note:** The last two bullets were already partially in English. The full section heading and first three bullets are Dutch. All translated for consistency.
**Reason:** Active system instruction. Must comply with GL-014 v1.2 §10.
**Risk:** Low.
**Owner approval required:** Yes.

---

### PAX — ITEM X-002

**File:** `Team/Pax - The Research Specialist/AGENT.md`
**Section:** `## UMC — Unified Memory Core`
**Type:** Active system instruction (code comments, labels, inline strings)

**Current Dutch items:**

| Current | Proposed English |
|---|---|
| `**ICOR Input — laad context vóór actie:**` | `**ICOR Input — load context before action:**` |
| `# Recente sessiestatus (Laag 8 — Summary)` | `# Recent session status (Layer 8 — Summary)` |
| `# Domeinkennis ophalen (Laag 5 — Knowledge)` | `# Retrieve domain knowledge (Layer 5 — Knowledge)` |
| `"onderzoeksonderwerp"` (2 occurrences) | `"research subject"` |
| `**ICOR Refine — sla nieuwe inzichten terug op:**` | `**ICOR Refine — store new insights:**` |
| `content='Inzicht of besluit: ...'` | `content='Insight or decision: ...'` |
| `topic='onderzoeksonderwerp'` | `topic='research subject'` |

**Note:** Penn and Pax UMC sections share the same Dutch UMC boilerplate. Pax's UMC block does not include the two final Dutch sentences found in Penn ("Bij grote tool outputs…" and "Als UMC niet bereikbaar…") — those are Penn-specific. Pax's UMC ends after the code block without those lines.
**Reason:** Active system instructions.
**Risk:** Low.
**Owner approval required:** Yes.

---

## 7. Excluded Items

| Item | Reason for exclusion |
|---|---|
| Penn changelog entry B-024: `Fase 2 system-file language cleanup` | Historical changelog entry. Per GL-014 v1.2 §10: not rewritten without explicit Owner approval. |
| Pax changelog entry B-024: `Fase 2 system-file language cleanup` | Same as above. |
| All older session logs and team_log entries | Out of scope per GL-014 v1.2 and B-029 constraints. |
| Penn Identity section (existing pre-B-026 Dutch body text if any) | Requires separate investigation if applicable; not flagged in this pass. |

**Decision point for Owner:** The B-024 changelog entries in Penn and Pax contain "Fase 2" (Dutch). Owner may explicitly approve translating these to "Phase 2" as part of B-029 execution. Default recommendation: leave unchanged as historical records.

---

## 8. False Positives

| Item | Why no action needed |
|---|---|
| `"⚠️ UMC niet bereikbaar"` in Penn UMC (warning string) | This is the display message to the Owner — user-facing content may remain Dutch. However, the surrounding sentence is system instruction and is translated (see P-006). The warning string itself is borderline. |
| Dutch words inside wikilinks e.g. `[[what-about-me]] (sectie Miracle Roadmap)` | `(sectie Miracle Roadmap)` is Dutch but embedded in a document reference. Translated to `(Miracle Roadmap section)` in the P-005 replacement. |
| `sectie` in P-005 reference | Translated within the replacement text. |
| Proper nouns (Wendy Opdam, Kyara, Ylana) | Proper nouns, not Dutch system instructions. |
| `bestandsnaam` placeholder in Penn P-003 and P-004 | Translated to `filename` in the replacement text. |

---

## 9. Risk Assessment

| Risk | Level | Mitigation |
|---|---|---|
| Translation error alters Penn behavioral rules | Low | Exact replacement text provided — review before executing |
| `## Wendy Rule` heading change breaks routing references | None | No other file references this section by heading |
| UMC string placeholder changes affect Python execution | None | These are comment and example strings only — not executed code |
| `## Owner's Growth Context` naming inconsistency (Penn vs Sienna) | None | Sienna was cleaned in B-026, Penn in B-029 — same result |

Overall risk: **Low**. All changes are translation-only with no functional impact.

---

## 10. Recommended Execution Plan

After Owner's explicit approval:

1. **Executor:** Nolan (AGENT.md quality specialist)
2. **Approach:** Edit each AGENT.md file using the Edit tool (not Write) — read before edit, change only approved items
3. **Sequence:** Penn first (more items), then Pax
4. **Changelog entry per file:**
   ```markdown
   - 2026-06-03 (Nolan, B-029): Remaining Dutch system-file content translated to English. No functional changes. Approved by Owner.
   ```
5. **Post-checks:**
   - Penn: `## Processing Raw Input`, `## Proactive Thinking`, `## Wendy Rule`, `## Auto-Archive`, `## Owner's Growth Context` all exist in English
   - Penn UMC: all Dutch comments and labels translated
   - Pax: `## Proactive Thinking` exists in English
   - Pax UMC: all Dutch comments and labels translated
   - No other files changed
6. **Audit trail:** team_log entry + session log per GL-014 v1.2 §6

---

## 11. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This proposal is read-only. No files have been modified. The execution plan in §10 is not active until Owner's explicit approval is received and communicated.

---

## 12. Final Recommendation

Execute B-029. The changes are translation-only, low risk and complete. After B-029, Penn and Pax will be fully English in their active system-file content, consistent with GL-014 v1.2 §10 and the Owner terminology standard.

The only remaining open decision is whether to also translate "Fase 2" to "Phase 2" in the B-024 changelog entries of Penn and Pax. Default recommendation: leave unchanged as historical records unless Owner explicitly approves.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-029-remaining-dutch-cleanup-proposal.md`*
