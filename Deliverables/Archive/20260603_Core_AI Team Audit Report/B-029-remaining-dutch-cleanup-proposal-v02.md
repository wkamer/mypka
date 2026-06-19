# B-029 Remaining Dutch System Content Cleanup Proposal v0.2

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**
**Changes vs v0.1:** Penn Identity section verified and added (P-000). Penn UMC warning string inconsistency resolved. Pax pronoun corrected to neutral. UMC sections replaced with full block-level context. Final Recommendation adjusted.

---

## 1. Purpose

This proposal identifies and provides exact English replacements for remaining Dutch system-file content in Penn (The Journal Writer) and Pax (The Research Specialist). These files were partially cleaned in B-026 within the approved scope at the time. Additional Dutch sections were noted outside that scope and deferred. This proposal covers those remaining items in full.

---

## 2. Governance Basis

| Rule | Source |
|---|---|
| All system files must be written in English | GL-014 v1.2 §10 System File Language Rule |
| System files include AGENT.md files | GL-014 v1.2 §10 |
| Only user-facing content may be written in Dutch | GL-014 v1.2 §10 |
| Historical changelog entries not rewritten without explicit Owner approval | GL-014 v1.2 §10 |
| No implementation without Owner's explicit approval | GL-014 v1.2 §1 |
| Owner = Walter Kamer | GL-014 v1.2 Owner definition |
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

Investigation performed using:
- `cat` — full file content
- `grep -n` with `-A` context lines to locate and read specific sections
- `sed -n` for specific line ranges
- ctx_batch_execute for parallel reads

No files were modified, created, moved, renamed or deleted. No write operations executed.

---

## 5. Findings Summary

### Penn — The Journal Writer

Seven Dutch items found in the active body:

| Item | Section | Lines | Type |
|---|---|---|---|
| P-000 | What You Do on Every Input → Text input | ~26 | Active system instruction (inline Dutch) |
| P-001 | `## Verwerking van ruwe input` | ~141–150 | Active system instruction — full section |
| P-002 | `## Proactief Meedenken` | ~153–160 | Active system instruction — full section |
| P-003 | `## Wendy-regel — altijd actief` | ~162–170 | Active system instruction — full section |
| P-004 | `## Automatisch Borgen — zonder te vragen` | ~174–190 | Active system instruction — full section |
| P-005 | `## Walter's Groeicontext` (line ~313) | ~313–315 | Active system instruction — heading + body |
| P-006 | `## UMC — Unified Memory Core` | ~256–294 | Active system instruction — inline Dutch |

Plus two changelog entries containing "Fase 2" — see §7.

### Pax — The Research Specialist

Two Dutch items found:

| Item | Section | Lines | Type |
|---|---|---|---|
| X-001 | `## Proactief Meedenken` | ~30–50 | Active system instruction — full section |
| X-002 | `## UMC — Unified Memory Core` | ~124–153 | Active system instruction — inline Dutch |

Plus one changelog entry containing "Fase 2" — see §7.

---

## 6. Proposed Changes

---

### PENN — ITEM P-000

**File:** `Team/Penn - The Journal Writer/AGENT.md`
**Section:** `## What You Do on Every Input → ### Text input`
**Type:** Active system instruction — inline Dutch comment and filename template

**Current Dutch text (line ~26):**
```markdown
1. Write a journal entry at `PKM/Journal/YYYY/MM/YYYYMMDD_onderwerp 1, onderwerp 2.md` — dit is de enige canonical locatie
```

**Exact English replacement:**
```markdown
1. Write a journal entry at `PKM/Journal/YYYY/MM/YYYYMMDD_subject 1, subject 2.md` — this is the only canonical location
```

**Reason:** `— dit is de enige canonical locatie` is an active Dutch system instruction comment. `onderwerp` is Dutch for "subject" and is used as a filename placeholder in a system instruction context. Both must be in English per GL-014 v1.2 §10.

**Note on filename template:** The template `YYYYMMDD_onderwerp 1, onderwerp 2.md` is a naming convention placeholder. Translating "onderwerp" to "subject" does not change the convention — it translates the placeholder label. The actual journal files created by Penn are not affected since their titles come from real content, not from this template word.

**Risk:** Low. Inline comment translation and placeholder label change only.
**Owner approval required:** Yes.

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

**Reason:** Active system instruction. Must comply with GL-014 v1.2 §10.
**Risk:** Low.
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

**Reason:** Active system instruction. "Wendy" is a proper noun and is unchanged. `"Geborgen als journal entry — [[bestandsnaam]]"` is a reporting template — translated to `"Archived as journal entry — [[filename]]"`.
**Risk:** Low.
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

**Reason:** Active system instruction. "Walter's Groeicontext" was cleaned in Sienna (B-026) but Penn's version at line ~313 was outside that scope. Per Owner terminology, "Walter" in active system headings becomes "Owner". `(sectie Miracle Roadmap)` → `(Miracle Roadmap section)`.
**Risk:** Low.
**Owner approval required:** Yes.

---

### PENN — ITEM P-006

**File:** `Team/Penn - The Journal Writer/AGENT.md`
**Section:** `## UMC — Unified Memory Core`
**Type:** Active system instruction — code comments, labels, inline strings and one closing sentence

**Current full UMC block (lines ~256–295):**
```markdown
## UMC — Unified Memory Core

**Interpreter:** `/opt/mypka-memory/venv/bin/python`

**ICOR Input — zoek eerdere journaalcontext:**
```python
import sys, os
sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
from memory_config import get_dsn
os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
from memory_manager import get_manager
mm = get_manager()

# Eerdere journaalcontext (Laag 6 — Conversation)
pointers = mm.get_summary_pointers(limit=3)
journal_ctx = mm.search_knowledge("thema of persoon", domain="personal", source_type="journal", top_k=3)

# Persoon checken vóór CRM-stub aanmaken (Laag 2 — Entity)
entities = mm.search_entities("naam van persoon")
```

**Na elke journal entry — verplicht (Laag 2 + Laag 6):**
```python
# Entity extraction
entities = mm.extract_and_store_entities(journal_entry_text)

# Sla inzicht terug op als conversation memory
mm.icor_refine(
    layer='conversation',
    content='Inzicht: [patroon of observatie uit de entry].',
    agent='penn',
    topic='journal-inzicht',
    date_ref='2026-05-30'
)
```

Bij grote tool outputs (>2000 chars): PostToolUse hook offloadt automatisch.

Als UMC niet bereikbaar: overslaan en meld "⚠️ UMC niet bereikbaar".
```

**Exact English replacement for full UMC block:**
```markdown
## UMC — Unified Memory Core

**Interpreter:** `/opt/mypka-memory/venv/bin/python`

**ICOR Input — search earlier journal context:**
```python
import sys, os
sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
from memory_config import get_dsn
os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
from memory_manager import get_manager
mm = get_manager()

# Earlier journal context (Layer 6 — Conversation)
pointers = mm.get_summary_pointers(limit=3)
journal_ctx = mm.search_knowledge("theme or person", domain="personal", source_type="journal", top_k=3)

# Check person before creating CRM stub (Layer 2 — Entity)
entities = mm.search_entities("name of person")
```

**After every journal entry — mandatory (Layer 2 + Layer 6):**
```python
# Entity extraction
entities = mm.extract_and_store_entities(journal_entry_text)

# Store insight back as conversation memory
mm.icor_refine(
    layer='conversation',
    content='Insight: [pattern or observation from the entry].',
    agent='penn',
    topic='journal-insight',
    date_ref='2026-05-30'
)
```

For large tool outputs (>2000 chars): PostToolUse hook offloads automatically.

If UMC is not reachable: skip and report "⚠️ UMC niet bereikbaar".
```

**Note on the warning string:** `"⚠️ UMC niet bereikbaar"` appears in both the closing instruction sentence and in an earlier English-language sentence at line ~117. The surrounding system instruction sentences are translated to English. The warning string itself — `"⚠️ UMC niet bereikbaar"` — is the actual display message shown to the Owner and qualifies as user-facing Dutch output. It is intentionally preserved in Dutch in both occurrences. This is consistent with GL-014 v1.2 §10: "Only user-facing content may be written in Dutch."

**Reason:** Active system instructions. Code comments, section labels and placeholder strings are system-file content per GL-014 v1.2 §10. The warning string is user-facing and intentionally preserved.
**Risk:** Low.
**Owner approval required:** Yes.

---

### PAX — ITEM X-001

**File:** `Team/Pax - The Research Specialist/AGENT.md`
**Section:** `## Proactief Meedenken`
**Type:** Active system instruction — heading and full body

**Note on pronouns:** Pax's Identity and Role sections use "His/He" (masculine). The Never Does section (added in Fase 2/B-017) inconsistently uses "she". Since this proposal is translation-only, the Dutch original (`zijn onderzoek` — "his research", `hij begint` — "he starts") is translated using neutral phrasing ("the research", "Pax") to avoid amplifying the existing inconsistency. Pronoun alignment is a separate issue not in scope here.

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

Pax thinks along at the edge of the research.

- When a sub-question raises a relevant follow-up question the Owner probably has not seen yet: name it at the end of the report
- When a source is questionable or a finding is speculative: mark it explicitly — never buried in the text
- When a research question should be broader or narrower than requested: say so before starting, not after
- When a tool or capability needed for the research task has known limitations (e.g. sandbox isolation, no live web access, API rate limits): flag this at the start of the task, before attempting the operation. Never discover limitations mid-execution when they could have been anticipated.
- **Always read the primary source.** If the research question references a notebook, code file, paper or technical spec: retrieve the raw content (raw URL, not the wrapper page) and read the actual code or text. Never write a report based on metadata, summaries or page descriptions. A finding is only "source-backed" when Pax has read the source directly. For GitHub notebooks: always use the `raw.githubusercontent.com` URL, not the `github.com` page.
```

**Reason:** Active system instruction. Must comply with GL-014 v1.2 §10.
**Risk:** Low.
**Owner approval required:** Yes.

---

### PAX — ITEM X-002

**File:** `Team/Pax - The Research Specialist/AGENT.md`
**Section:** `## UMC — Unified Memory Core`
**Type:** Active system instruction — code comments, labels, inline strings

**Current full UMC block (lines ~124–155):**
```markdown
## UMC — Unified Memory Core

**Interpreter:** `/opt/mypka-memory/venv/bin/python`

**ICOR Input — laad context vóór actie:**
```python
import sys, os
sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
from memory_config import get_dsn
os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
from memory_manager import get_manager
mm = get_manager()

# Recente sessiestatus (Laag 8 — Summary)
pointers = mm.get_summary_pointers(limit=3)

# Domeinkennis ophalen (Laag 5 — Knowledge)
ctx = mm.search_knowledge("onderzoeksonderwerp", domain="core", top_k=3)
```

**ICOR Refine — sla nieuwe inzichten terug op:**
```python
mm.icor_refine(
    layer='knowledge',
    content='Inzicht of besluit: ...',
    agent='pax',
    topic='onderzoeksonderwerp',
    date_ref='2026-05-30'
)
```
```

**Exact English replacement for full UMC block:**
```markdown
## UMC — Unified Memory Core

**Interpreter:** `/opt/mypka-memory/venv/bin/python`

**ICOR Input — load context before action:**
```python
import sys, os
sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
from memory_config import get_dsn
os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
from memory_manager import get_manager
mm = get_manager()

# Recent session status (Layer 8 — Summary)
pointers = mm.get_summary_pointers(limit=3)

# Retrieve domain knowledge (Layer 5 — Knowledge)
ctx = mm.search_knowledge("research subject", domain="core", top_k=3)
```

**ICOR Refine — store new insights:**
```python
mm.icor_refine(
    layer='knowledge',
    content='Insight or decision: ...',
    agent='pax',
    topic='research subject',
    date_ref='2026-05-30'
)
```
```

**Reason:** Active system instructions. Code comments and placeholder strings are system-file content per GL-014 v1.2 §10.
**Risk:** Low.
**Owner approval required:** Yes.

---

## 7. Excluded Items

| Item | Reason for exclusion |
|---|---|
| Penn B-024 changelog entry: `Fase 2 system-file language cleanup` | Historical changelog entry. Per GL-014 v1.2 §10: not rewritten without explicit Owner approval. Decision point: Owner may approve translating "Fase 2" → "Phase 2". |
| Pax B-024 changelog entry: `Fase 2 system-file language cleanup` | Same as above. |
| All older session logs and team_log entries | Out of scope per GL-014 v1.2 and B-029 constraints. |

---

## 8. False Positives

| Item | Classification |
|---|---|
| `"⚠️ UMC niet bereikbaar"` display string | **User-facing Dutch output** — intentionally preserved. The surrounding instruction sentences are translated to English (see P-006). The string itself is the message shown to the Owner, who reads Dutch. |
| `[[what-about-me]]` wikilink in P-005 | Proper document reference — unchanged in replacement. |
| Proper nouns: Wendy Opdam, Kyara, Ylana | Proper nouns — not Dutch system instructions. |
| Pax pronoun inconsistency (He/His vs she) | Out of scope — translation task only, not a pronoun alignment task. |

---

## 9. Risk Assessment

| Risk | Level | Mitigation |
|---|---|---|
| Translation error alters Penn behavioral rules | Low | Full block-level replacement text provided — review before executing |
| `## Wendy Rule` heading change breaks references | None | No other file references this section heading |
| UMC placeholder string changes affect Python execution | None | Comment and example strings only — not executed |
| `## Owner's Growth Context` in Penn, already applied in Sienna | None | Consistent result — same heading in both files |
| P-000 filename template change (`onderwerp` → `subject`) | Low | Template label only — Penn's real journal filenames come from content, not this placeholder |

Overall risk: **Low**. All changes are translation-only with no functional impact.

---

## 10. Recommended Execution Plan

After Owner's explicit approval:

1. **Executor:** Nolan (AGENT.md quality specialist)
2. **Approach:** Edit each AGENT.md using the Edit tool — read before edit, change only approved items using exact replacement text from §6
3. **Sequence:** Penn first (more items), then Pax
4. **Changelog entry per file:**
   ```markdown
   - 2026-06-03 (Nolan, B-029): Remaining Dutch system-file content translated to English. No functional changes. Approved by Owner.
   ```
5. **Post-checks:**
   - Penn: `## Processing Raw Input`, `## Proactive Thinking`, `## Wendy Rule`, `## Auto-Archive`, `## Owner's Growth Context` all present in English; UMC comments in English; line ~26 Dutch comment translated
   - Pax: `## Proactive Thinking` in English; UMC comments in English
   - No other files changed
6. **Audit trail:** team_log entry + session log per GL-014 v1.2 §6

---

## 11. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This proposal is read-only. No files have been modified. The execution plan in §10 is not active until Owner's explicit approval is received.

---

## 12. Final Recommendation

This proposal is ready for Owner review. All identified Dutch system-file content has been catalogued with exact English replacement text. Five issues from v0.1 have been resolved:

1. Penn Identity section verified — one Dutch item found and added as P-000.
2. Penn UMC warning string inconsistency resolved — string is user-facing Dutch output and intentionally preserved; surrounding sentences translated.
3. Pax pronoun corrected — neutral phrasing used to avoid introducing non-translation changes.
4. UMC sections replaced with full block-level text to remove execution ambiguity.
5. Final recommendation adjusted to reflect that all issues are now resolved pending Owner approval.

One remaining Owner decision point: whether to also translate "Fase 2" to "Phase 2" in the B-024 changelog entries in Penn and Pax. Default recommendation is to leave these unchanged as historical records.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-029-remaining-dutch-cleanup-proposal-v02.md`*
