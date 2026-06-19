# B-063 — GL-001 / Penn AGENT.md Naming Convention Language Review
# Proposal v01

**Status:** Proposal only — no implementation
**Version:** v01
**Date:** 2026-06-04
**Author:** larry
**Backlog item:** B-063 — team_tasks id 63
**Requires approval by:** Owner Walter Kamer — see Approval Gate

---

## 1. Files Inspected

| File | Path | Read for |
|---|---|---|
| GL-001 | `Team Knowledge/Core/Guidelines/GL-001_File naming conventions.md` | Full content — language compliance |
| Penn AGENT.md | `Team/Penn - The Journal Writer/AGENT.md` | Naming convention placeholder language |

No other files were read, modified, or accessed.

---

## 2. Finding

### 2.1 GL-001 — Entirely in Dutch

GL-001 is the authoritative naming convention reference document for the entire vault. The System
File Language Rule, established in B-024/B-025 and codified in GL-014 §7, requires all system
files (Guidelines, SOPs, Workstreams, AGENT.md files) to be written in English.

GL-001 is entirely in Dutch. Every section heading, rule description, and table entry is Dutch.
This is a complete System File Language Rule violation.

**Where the issue is:** GL-001 only for the system file language violation, and secondarily Penn
AGENT.md for inherited Dutch naming convention placeholders that trace directly to GL-001.

### 2.2 Penn AGENT.md — Dutch Naming Convention Placeholders

Penn AGENT.md underwent three language cleanup passes (B-024, B-026, B-029) and is largely in
English. However, eight naming convention placeholders remain in Dutch. These were not caught in
prior cleanup passes because they are format descriptor strings that originate from GL-001's Dutch
conventions. They are exclusively in the naming convention sections of Penn AGENT.md, not in
operational logic.

### 2.3 Scope Classification

| Issue | File | Type |
|---|---|---|
| Entire document in Dutch | GL-001 | System file language violation |
| Dutch naming convention placeholders (8 occurrences) | Penn AGENT.md | Residual Dutch from GL-001 convention language |

---

## 3. Exact Current Text and Proposed Replacement

### 3.1 GL-001 — Full Replacement

The entire file is in Dutch. The proposed replacement is a full English translation. The naming
convention rules themselves are preserved exactly. Format placeholder words are translated to
English equivalents. Proper nouns used as examples (e.g., `De Vries, Ylana.md`,
`P-Geldstroom Regie`, `G-Financiële vrijheid`) are unchanged — they are real names, not system
language.

**Current full file content:**

```
# GL-001 — File Naming Conventions

**Geldig voor:** gehele myPKA vault
**Uitzondering:** scripts (Python, PowerShell) gebruiken kebab-case zonder spaties

---

## Algemene regel

Gebruik spaties in bestandsnamen en mapnamen. Geen underscores als woordscheider, geen camelCase.

---

## Mapnamen

Title Case overal.

```
Team Knowledge/
PKM/My Life/
Kamer E-commerce/
```

---

## Bestandsnamen per type

| Type | Formaat | Voorbeeld |
|---|---|---|
| Algemeen | Beschrijvende naam met spaties | `project overzicht.md` |
| Journal | `YYYYMMDD_onderwerp 1, onderwerp 2.md` | `20260509_voetbal, dochter, parijs.md` |
| Session log | `YYYYMMDD_beschrijving.md` in `YYYY/MM/` | `2026/05/20260509_scaffold restructure.md` |
| Deliverable | `YYYYMMDD_Domain_beschrijving/` | `20260509_Kamer E-commerce_US store audit/` |
| Afbeelding | `YYYYMMDD_beschrijving.ext` | `20260509_visitekaartje anna.jpg` |
| CRM People | `Achternaam, Voornaam.md` | `De Vries, Ylana.md` |
| CRM Organizations | `Volledige Naam.md` | `Kamer E-commerce.md` |
| Topic | `T-Onderwerp.md` | `T-AI.md`, `T-Trading.md` |
| Key Element | `KE-Domein.md` | `KE-Finance.md`, `KE-Self.md` |
| Project (map) | `P-Projectnaam` | `P-Geldstroom Regie` |
| Goal (map) | `G-Titel` | `G-Financiële vrijheid` |
| SOP | `SOP-001_Titel.md` | `SOP-001_How to hire a new team member.md` |
| Guideline | `GL-001_Titel.md` | `GL-001_File naming conventions.md` |
| Workstream | `WS-001_Titel.md` | `WS-001_Daily journaling.md` |
| Script (Python) | `snake_case.py` | `add_task.py`, `session_open.py` |
| Script (PowerShell) | `kebab-case.ps1` | `session-open.ps1` |

---

## ALL CAPS

Alleen voor Project-, Topic- en Key Element-namen in de bestandsnaam zelf (na het prefix):
- `T-AI.md`, `T-TRADING.md` → alleen als het een afkorting of eigennaam is
- Gewone woorden: lowercase na prefix: `T-voeding.md`, `KE-gezondheid.md`

---

## Nummering (SOP/GL/WS)

- Nummers zijn per domein uniek, niet globaal
- Formaat: driecijferig (`001`, `002`, ...)
- Volgorde: chronologisch aangemaakt

---

## Wikilinks

Gebruik altijd de exacte bestandsnaam zonder extensie:
```
[[De Vries, Ylana]]
[[T-AI]]
[[SOP-001_How to hire a new team member]]
```
```

**Proposed replacement — full English translation:**

```
# GL-001 — File Naming Conventions

**Applies to:** entire myPKA vault
**Exception:** scripts (Python, PowerShell) use kebab-case without spaces

---

## General Rule

Use spaces in file names and folder names. No underscores as word separators, no camelCase.

---

## Folder Names

Title Case everywhere.

```
Team Knowledge/
PKM/My Life/
Kamer E-commerce/
```

---

## File Names by Type

| Type | Format | Example |
|---|---|---|
| General | Descriptive name with spaces | `project overview.md` |
| Journal | `YYYYMMDD_subject 1, subject 2.md` | `20260509_football, daughter, paris.md` |
| Session log | `YYYYMMDD_description.md` in `YYYY/MM/` | `2026/05/20260509_scaffold restructure.md` |
| Deliverable | `YYYYMMDD_Domain_description/` | `20260509_Kamer E-commerce_US store audit/` |
| Image | `YYYYMMDD_description.ext` | `20260509_business card anna.jpg` |
| CRM People | `LastName, FirstName.md` | `De Vries, Ylana.md` |
| CRM Organizations | `Full Name.md` | `Kamer E-commerce.md` |
| Topic | `T-Name.md` | `T-AI.md`, `T-Trading.md` |
| Key Element | `KE-Domain.md` | `KE-Finance.md`, `KE-Self.md` |
| Project (folder) | `P-ProjectName` | `P-Geldstroom Regie` |
| Goal (folder) | `G-Title` | `G-Financiële vrijheid` |
| SOP | `SOP-001_Title.md` | `SOP-001_How to hire a new team member.md` |
| Guideline | `GL-001_Title.md` | `GL-001_File naming conventions.md` |
| Workstream | `WS-001_Title.md` | `WS-001_Daily journaling.md` |
| Script (Python) | `snake_case.py` | `add_task.py`, `session_open.py` |
| Script (PowerShell) | `kebab-case.ps1` | `session-open.ps1` |

---

## ALL CAPS

Only for Project, Topic, and Key Element names in the file name itself (after the prefix):
- `T-AI.md`, `T-TRADING.md` → only when it is an abbreviation or proper noun
- Regular words: lowercase after prefix: `T-nutrition.md`, `KE-health.md`

---

## Numbering (SOP/GL/WS)

- Numbers are unique per domain, not globally
- Format: three digits (`001`, `002`, ...)
- Order: chronologically created

---

## Wikilinks

Always use the exact file name without the extension:
```
[[De Vries, Ylana]]
[[T-AI]]
[[SOP-001_How to hire a new team member]]
```

---

## Changelog

- 2026-06-04 (Larry, B-063): Full English translation. No convention rules changed. Approved by Owner Walter Kamer.
```

**Translation notes:**
- `Geldig voor` → `Applies to`
- `Uitzondering` → `Exception`
- `Algemene regel` → `General Rule`
- `Mapnamen` → `Folder Names`
- `Bestandsnamen per type` → `File Names by Type`
- `Formaat` → `Format`
- `Voorbeeld` → `Example`
- `Algemeen` → `General`
- `Beschrijvende naam met spaties` → `Descriptive name with spaces`
- `onderwerp` → `subject`
- `beschrijving` → `description`
- `Afbeelding` → `Image`
- `Achternaam, Voornaam.md` → `LastName, FirstName.md` (format descriptor only; actual CRM file names like `De Vries, Ylana.md` are unchanged)
- `Volledige Naam.md` → `Full Name.md`
- `T-Onderwerp.md` → `T-Name.md`
- `KE-Domein.md` → `KE-Domain.md`
- `Project (map)` → `Project (folder)`
- `P-Projectnaam` → `P-ProjectName`
- `Goal (map)` → `Goal (folder)`
- `G-Titel` → `G-Title`
- `SOP-001_Titel.md` → `SOP-001_Title.md`
- `GL-001_Titel.md` → `GL-001_Title.md`
- `WS-001_Titel.md` → `WS-001_Title.md`
- ALL CAPS section: Dutch text → English; examples `T-voeding.md` → `T-nutrition.md`, `KE-gezondheid.md` → `KE-health.md`
- `Nummering` → `Numbering`
- `Nummers zijn per domein uniek, niet globaal` → `Numbers are unique per domain, not globally`
- `Formaat: driecijferig` → `Format: three digits`
- `Volgorde: chronologisch aangemaakt` → `Order: chronologically created`
- `Wikilinks` heading: unchanged (proper term)
- `Gebruik altijd de exacte bestandsnaam zonder extensie:` → `Always use the exact file name without the extension:`
- Added Changelog section (not present in current file; standard for all GL documents)

**Proper nouns preserved unchanged:**
- `De Vries, Ylana.md` — real person name (example)
- `Kamer E-commerce.md` — organization name (example)
- `P-Geldstroom Regie` — project name (example)
- `G-Financiële vrijheid` — goal name (example; contains Dutch content but is a proper name)
- `T-AI.md`, `T-Trading.md` — abbreviation and proper name (examples)
- `KE-Finance.md`, `KE-Self.md` — already English (examples)
- All SOP/GL/WS title examples — already English

---

### 3.2 Penn AGENT.md — Eight Naming Convention Placeholder Changes

These eight changes translate Dutch format descriptor words to English. They are in the naming
convention sections of Penn AGENT.md only. No operational logic, routing, database calls, or
behavioral instructions are modified.

**Execution method for each change:** Edit tool, exact string match. Read the file immediately
before editing to confirm byte-exact match.

---

**Change P-1** — Image input path format descriptor (line 33)

Current:
```
Save the file to `PKM/Images/YYYY/MM/YYYYMMDD_beschrijving.ext`
```
Proposed:
```
Save the file to `PKM/Images/YYYY/MM/YYYYMMDD_description.ext`
```

---

**Change P-2** — Image embed format descriptor (line 34)

Current:
```
Embed in the journal entry: `![[Images/YYYY/MM/YYYYMMDD_beschrijving.ext]]`
```
Proposed:
```
Embed in the journal entry: `![[Images/YYYY/MM/YYYYMMDD_description.ext]]`
```

---

**Change P-3** — CRM People path format descriptor, image input section (line 35)

Current:
```
create or update `PKM/CRM/People/Achternaam, Voornaam.md`
```
Proposed:
```
create or update `PKM/CRM/People/LastName, FirstName.md`
```

---

**Change P-4** — CRM Organizations path format descriptor (line 36)

Current:
```
create or update `PKM/CRM/Organizations/Naam.md`
```
Proposed:
```
create or update `PKM/CRM/Organizations/Name.md`
```

---

**Change P-5** — Document naming convention format descriptor (line 45)

Current:
```
File to `PKM/Documents/` using naming convention: `YYYYMMDD_Type_Persoon_Detail.ext`
```
Proposed:
```
File to `PKM/Documents/` using naming convention: `YYYYMMDD_Type_Person_Detail.ext`
```

---

**Change P-6** — CRM People path format descriptor, People Detection section (line 59)

Current:
```
create stub at `PKM/CRM/People/Achternaam, Voornaam.md`. Insert row in `personal.db`
```
Proposed:
```
create stub at `PKM/CRM/People/LastName, FirstName.md`. Insert row in `personal.db`
```

---

**Change P-7** — Bucket Detection table: four format descriptor placeholders (lines 75–78)

Current:
```
| Interest / recurring subject | `PKM/My Life/Topics/T-Naam.md` |
| Time-bound effort | `PKM/My Life/Projects/P-Naam/` |
| Recurring rhythm or routine | `PKM/My Life/Habits/H-Naam.md` |
| Outcome or aspiration | `PKM/My Life/Goals/` |
| Stable life dimension | `PKM/My Life/Key Elements/KE-Naam.md` |
```
Proposed:
```
| Interest / recurring subject | `PKM/My Life/Topics/T-Name.md` |
| Time-bound effort | `PKM/My Life/Projects/P-Name/` |
| Recurring rhythm or routine | `PKM/My Life/Habits/H-Name.md` |
| Outcome or aspiration | `PKM/My Life/Goals/` |
| Stable life dimension | `PKM/My Life/Key Elements/KE-Name.md` |
```

---

**Change P-8** — Topic stub format descriptor in Bucket Detection prose (line 84)

Current:
```
create `T-Naam.md` using the standard topic template
```
Proposed:
```
create `T-Name.md` using the standard topic template
```

---

**Change P-9** — CRM wikilink format example in Wiki Convention section (line 96)

Current:
```
the journal entry just writes `[[Voornaam]]` and moves on.
```
Proposed:
```
the journal entry just writes `[[FirstName]]` and moves on.
```

---

**Summary of Penn AGENT.md changes:**

| # | Dutch placeholder | English replacement | Location |
|---|---|---|---|
| P-1 | `beschrijving` | `description` | Image input path |
| P-2 | `beschrijving` | `description` | Image embed format |
| P-3 | `Achternaam, Voornaam` | `LastName, FirstName` | CRM People path (image section) |
| P-4 | `Naam` | `Name` | CRM Organizations path |
| P-5 | `Persoon` | `Person` | Document naming convention |
| P-6 | `Achternaam, Voornaam` | `LastName, FirstName` | CRM People path (People Detection) |
| P-7 | `T-Naam`, `P-Naam`, `H-Naam`, `KE-Naam` | `T-Name`, `P-Name`, `H-Name`, `KE-Name` | Bucket Detection table |
| P-8 | `T-Naam` | `T-Name` | Bucket Detection prose |
| P-9 | `Voornaam` | `FirstName` | Wiki Convention wikilink example |

---

## 4. What Is NOT Changed

**In Penn AGENT.md — explicitly out of scope:**
- `niet standaard python3` (Entity Memory section, line 104) — interpreter note, not naming convention
- `UMC niet bereikbaar` (lines 117, 294) — standard UMC report string, not naming convention
- `geen andere locatie gebruiken` (Links section, line 302) — operational note, not naming convention
- All behavioral logic, routing rules, database calls, cross-link rules, and processing pipelines
- All other AGENT.md files — not referenced in B-063

**In GL-001 — not changed:**
- The naming convention rules themselves — preserved exactly
- Proper noun examples — `De Vries, Ylana.md`, `Kamer E-commerce.md`, `P-Geldstroom Regie`, `G-Financiële vrijheid` — unchanged
- The file name of GL-001 itself (`GL-001_File naming conventions.md`) — unchanged; no wikilinks break

**Across the vault — not changed:**
- Actual CRM People files (e.g., `De Vries, Ylana.md`) — not renamed
- Actual Topic files (e.g., `T-AI.md`) — not renamed
- Any existing file or folder anywhere in the vault
- Any database, UMC, team_log, team_tasks, or backlog record
- Any SOP, other Guideline, or Workstream file
- CLAUDE.md
- Any script or credential file

---

## 5. Confirmation

This is language and naming convention description cleanup only. No agent behavior changes.
No actual file renames. No database changes. No routing changes. No governance model changes.
No project structure changes. No workstream behavior changes.

---

## 6. Rationale

GL-001 is the authoritative naming convention reference. It is entirely in Dutch and has been since
creation. The System File Language Rule (GL-014 §7, established B-024/B-025) requires system files
to be in English. GL-001 pre-dates the rule and was not caught in subsequent cleanup passes because
B-024, B-026, B-029, and B-030B had specific scopes that did not include a full GL-001 translation.

Penn AGENT.md's Dutch naming convention placeholders are a direct inheritance from GL-001's Dutch
convention descriptions. They were not caught in B-024, B-026, or B-029 because they are
indistinguishable from correct Dutch naming convention format strings — they describe the format
of files, not the behavior of Penn.

Translating GL-001 to English and updating Penn AGENT.md's format placeholders to match completes
the language compliance work for the naming convention layer of the system.

---

## 7. Scope Boundaries

**In scope:**
- GL-001: full English translation (Write tool — full file replacement)
- Penn AGENT.md: nine naming convention placeholder changes (Edit tool — exact string replacements)

**Out of scope:**
- Any file not listed above
- Any content in Penn AGENT.md not in the naming convention sections
- Any other agent AGENT.md file
- Any actual file or folder renames
- Any database, UMC, backlog, or system configuration changes

---

## 8. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| GL-001 translation introduces a meaning change | Low | Medium | Proposed replacement is a word-for-word translation; convention rules are structurally identical. Post-check compares rule count and format strings. |
| Penn AGENT.md change breaks a path used in production | Very low | Low | Changes are format descriptor strings only (`T-Naam.md` → `T-Name.md`). Penn does not parse these strings programmatically — they are human-readable instructions. Actual files created by Penn use real names, not these placeholder words. |
| Wikilinks to GL-001 break | None | None | The file NAME of GL-001 is unchanged (`GL-001_File naming conventions.md`). Only internal content changes. |
| Actual CRM file names change | None | None | `De Vries, Ylana.md` and similar files are explicitly preserved as proper-noun examples. No file rename is performed. |
| Out-of-scope Dutch content remains | Certain | Low | `niet standaard python3`, `UMC niet bereikbaar`, and `geen andere locatie gebruiken` in Penn AGENT.md are intentionally out of scope for B-063 (not naming convention language). They can be addressed in a separate cleanup item if Owner chooses. |

---

## 9. Explicit Exclusions

- No implementation of any kind until Owner explicitly approves this proposal
- No execution of any other backlog item
- No modification of GL-001, Penn AGENT.md, or any other file
- No database writes, UMC writes, team_tasks updates, or team_log entries
- No secret values accessed, read, written, or exposed
- No changes to any SOP, Workstream, other Guideline, or CLAUDE.md
- No changes to any actual file names or folder structure in the vault

---

## 10. Post-Check Plan

If approved and executed, the following checks confirm correctness:

| Check | Method | Pass condition |
|---|---|---|
| GL-001 exists at canonical path | `ls` | `Team Knowledge/Core/Guidelines/GL-001_File naming conventions.md` present |
| GL-001 content is fully in English | Read file | No Dutch words in section headings, rule text, or table column headers |
| GL-001 naming convention rules structurally match pre-change | Manual compare | Same number of file type rows, same format patterns, same proper noun examples |
| GL-001 Changelog entry present | Read file | Entry for B-063 with date 2026-06-04 |
| Penn P-1 through P-9: each change applied | Read Penn AGENT.md | None of the nine Dutch strings present; English equivalents present |
| Penn AGENT.md functional content unchanged | Read Penn AGENT.md | All behavioral sections, routing rules, DB calls, and code blocks identical to pre-change state |
| No other files modified | `ls -la` on GL-001 and Penn AGENT.md | Timestamps updated only for these two files |

---

## 11. Execution Order (if approved)

1. Read GL-001 immediately before writing (to confirm byte-exact current state)
2. Write GL-001 with full English replacement content from §3.1
3. Verify GL-001 post-check (read back, confirm English, confirm Changelog entry)
4. Read Penn AGENT.md immediately before editing (to confirm byte-exact current state)
5. Apply changes P-1 through P-9 as sequential Edit operations (exact string match)
6. Verify Penn AGENT.md post-checks (read back, confirm nine changes applied, confirm functional content unchanged)

---

## 12. Owner Decision Options

**Option A — Approve B-063 for execution**
Execute GL-001 full English translation and all nine Penn AGENT.md naming convention placeholder
changes per §3. Both files updated in one session. No further action required for B-063.

**Option B — Request amendments**
Owner identifies gaps, incorrect translations, or items to add or remove. Larry revises as
v02 per SOP-015.

**Option C — Defer**
Accept the proposal but take no action now. B-063 remains open. GL-001 remains in Dutch.
Penn AGENT.md retains Dutch naming convention placeholders.

**Option D — Reject**
The current Dutch naming convention descriptions are acceptable. No translation performed.
B-063 closed without execution.

---

## 13. Recommended Option

**Option A — Approve B-063 for execution.**

GL-001 is the only remaining system file with Dutch-language content. It is the naming convention
authority for the entire vault. Leaving it in Dutch creates an inconsistency with every other
system file (all now in English after B-024, B-026, B-029, B-030B). The Penn AGENT.md changes are
a direct consequence and are low-risk format description updates with no behavioral impact. B-063
completes the language compliance work across the naming convention layer. Risk is very low and
scope is tightly bounded.

---

## Approval Gate

No implementation may happen until Owner Walter Kamer explicitly approves this proposal.

Approval phrase: "approve B-063 proposal v01"

- Approval of this proposal authorizes execution of GL-001 replacement and Penn AGENT.md changes P-1 through P-9 only
- No other files, databases, or system records are touched
- Any deviation from the approved scope requires stopping and reporting to Owner

Governance:
- Owner: Walter Kamer
- Maintainer responsible for execution: Larry, Team Orchestrator

---

*Delivered on: 2026-06-04*
*Delivered at: Deliverables/20260603_Core_AI Team Audit Report/B-063-naming-convention-language-review-proposal-v01.md*
