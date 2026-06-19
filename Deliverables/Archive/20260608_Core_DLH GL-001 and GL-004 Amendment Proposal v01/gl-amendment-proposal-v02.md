# GL-001 and GL-004 Amendment Proposal v02

**Scope:** Task 75 — Deliverable folder and versioning rule
**Targets:** GL-001 (File Naming Conventions) and GL-004 (Canonical Paths)
**Status:** Awaiting Owner review — do not implement yet
**Produced by:** Larry, Team Orchestrator
**Date:** 2026-06-08
**Basis:** Owner decision 2026-06-08 — Model A confirmed. Workstream code convention adopted.
Review verdict on v01: Accept with corrections. Owner authorized v02 with C-1, C-2, F-3 Option B.

**Out of scope for this proposal:**
- Task 77 (English-language rule for governance content) — separate GL-014 proposal
- Task 78 (correction versioning rule, broad scope) — separate SOP-015 proposal
- Task 87 (artifact_type migration) — separate DB migration proposal

---

## Correction Note

**Corrects:** gl-amendment-proposal-v01.md
**Authorized by:** Owner on 2026-06-08 following review verdict (Accept with corrections).

**C-1 — SSOT fix (mandatory):**
W-1 gains a new Change 1: update the existing File Names by Type table row for "Deliverable"
(GL-001 line 33) from the old format `YYYYMMDD_Domain_description/` to the new format
`YYYYMMDD_Domain_[WorkstreamCode ]ArtifactDescription/`. Without this update, GL-001 would
carry two conflicting definitions of deliverable folder format after implementation.
Post-check plan gains a corresponding check.

**C-2 — Nested fence reformat (mandatory):**
Section 3.1 in v01 wrapped the GL-001 insertion content in a triple-backtick code fence.
That outer fence closed prematurely at the first inner fence (the format string code block),
producing corrupted rendering. In v02, the insertion content is presented as direct markdown
prose with explicit boundary markers — no outer code fence. The content renders as it will
appear in GL-001.

**F-3 Option B — Remove procedural prohibition from GL-001:**
"Silent overwrite is not permitted. Corrections to governance deliverables must produce a
new versioned file. See SOP-015." removed from the Versioning section. GL-001 is a naming
convention guideline; this prohibition belongs in SOP-015 (Task 78). The Correction Note
format requirement is retained — it is a naming and structure rule, not a behavioral
prohibition.

---

## 1. Pre-Check Results

Pre-checks performed on current live files. No writes have occurred.

| Check | Result |
|---|---|
| GL-001 contains a "Deliverables Folder Naming" section | No — confirmed absent |
| GL-001 contains a "Deliverables File Naming" section | No — confirmed absent |
| GL-001 contains a "Versioning" section | No — confirmed absent |
| GL-001 current line count | 79 lines |
| GL-001 File Names by Type table row for "Deliverable" | Present at line 33: `\| Deliverable \| \`YYYYMMDD_Domain_description/\` \| \`20260509_Kamer E-commerce_US store audit/\` \|` |
| GL-004 Deliverables section exists | Yes — lines 126–141 |
| GL-004 contains workstream code mention | No — confirmed absent |
| No collision detected | Confirmed |

---

## 2. Write Structure

**Two target files. W-1 has three sequential changes within GL-001. W-2 is one replacement in GL-004.**

| Write | Change | Target | Batch-stop condition |
|---|---|---|---|
| W-1 | Change 1 | GL-001 line 33 — File Names by Type table row update | If table row not found at expected location, halt W-1 and surface to Owner |
| W-1 | Change 2 | GL-001 line 47 — insert three new sections | If insertion point text not found exactly, halt and surface to Owner |
| W-1 | Change 3 | GL-001 Changelog — append new entry | Execute after Changes 1 and 2 succeed |
| W-2 | — | GL-004 Deliverables section — replace full section | If GL-004 Deliverables section content has changed from pre-check baseline, halt and surface to Owner |

Batch-stop across W-1 and W-2: if W-1 fails at any change, do not proceed to W-2.

---

## 3. Exact Amendment Text

### 3.1 W-1 — GL-001 Amendment

**Target file:** `Team Knowledge/Core/Guidelines/GL-001_File naming conventions.md`

---

#### W-1 Change 1: Update File Names by Type table row

**Location:** GL-001 line 33, within the `## File Names by Type` table.

**Exact current text to replace:**
```
| Deliverable | `YYYYMMDD_Domain_description/` | `20260509_Kamer E-commerce_US store audit/` |
```

**Exact replacement text:**
```
| Deliverable | `YYYYMMDD_Domain_[WorkstreamCode ]ArtifactDescription/` | `20260607_Core_DLH Discovery and Proposal/` |
```

This replaces the old deliverable format (no workstream code, Dutch-origin example) with the
new format (workstream code as optional segment, English Title Case example). The detailed
naming rules for this format are in the new Deliverables Folder Naming section (Change 2).

---

#### W-1 Change 2: Insert three new sections

**Location:** GL-001 — insert after the `---` divider that closes `## File Names by Type`
(currently at line 47), before `## ALL CAPS` (currently at line 49).

**Insertion marker:** The `old_string` for the Edit tool is the `---` divider plus the blank
line plus the `## ALL CAPS` heading that immediately follows it. The insertion content goes
between the existing `---` and `## ALL CAPS`.

**Content to insert — rendered exactly as it will appear in GL-001:**

**[INSERT START]**

---

## Deliverables Folder Naming

The canonical unit of a deliverable is one folder per artifact. One folder = one deliverable = one lifecycle registration.

Folder format:

```
YYYYMMDD_Domain_[WorkstreamCode ]ArtifactDescription/
```

| Segment | Rules |
|---|---|
| `YYYYMMDD` | Date the folder was created |
| `Domain` | One of: `Personal`, `Kamer E-commerce`, `Geldstroom Regie`, `Core` |
| `WorkstreamCode` | Optional. 2–5 uppercase characters identifying the workstream (e.g., `DLH`, `LC4`). Use when a workstream produces more than one deliverable folder. Include one trailing space before `ArtifactDescription`. |
| `ArtifactDescription` | English, Title Case. No underscores within this segment. |

Rules:
- Flat structure only — no subfolders within `Deliverables/` by domain or workstream.
- Domain is always encoded in the folder name, never as a subfolder.
- The workstream code is optional for single-artifact deliverables; recommended when a workstream produces two or more deliverable folders.

Examples:
- `20260607_Core_Discovery and Proposal/` (single artifact, no workstream code)
- `20260607_Core_DLH Discovery and Proposal/` (workstream code DLH)
- `20260607_Core_DLH Phase B Triage/`
- `20260516_Personal_Morning Mobility Routine/`
- `20260516_Kamer E-commerce_Remy Research Week 21/`

Canonical path and archive location: [[GL-004_Canonical paths]].

---

## Deliverables File Naming

Primary document within a deliverable folder: English, lowercase, hyphenated.

File format for revisable deliverables:

```
<description-slug>-v<NN>.md
```

File format for single terminal artifacts not expected to be revised:

```
<description-slug>.md
```

| Segment | Rules |
|---|---|
| `description-slug` | kebab-case, concise, English. May include artifact type prefix when not implied by folder name (e.g., `naming-proposal`, `write-list`, `execution-report`). |
| `v<NN>` | Two-digit zero-padded version number. Starts at `v01`. Increment on each substantive revision. Omit only when the artifact is terminal. |

Examples:
- `architecture-assessment.md` (terminal)
- `naming-proposal-v01.md`
- `write-list-v01.md`
- `execution-report-v01.md`

---

## Versioning

Version numbers use two-digit zero-padded integers starting at `v01`: `v01`, `v02`, `v03`.

**Minor revision (same folder):** A correction or addition that does not change the substance of the deliverable creates a new versioned file in the same folder. The prior version file is preserved. Example: `naming-proposal-v01.md` is superseded by `naming-proposal-v02.md` in the same folder.

**Major revision (new folder):** A revision that changes the fundamental scope, purpose, or audience of a deliverable warrants a new deliverable folder. The original folder is not modified.

**Correction Note:** A versioned file at `vNN` where `NN > 01` must include a `## Correction Note` section immediately after the document header, stating what changed from the prior version and why.

**[INSERT END]**

---

#### W-1 Change 3: Append changelog entry

**Location:** GL-001 `## Changelog` section — append as a new line.

**Text to append:**
```
- 2026-06-08 (Larry, DLH-Task-75): Updated File Names by Type table Deliverable row to extended format. Added Deliverables Folder Naming, Deliverables File Naming, and Versioning sections. Establishes Model A (one folder per artifact) as canonical unit, optional workstream code convention, file naming and versioning rules. Approved by Owner Walter Kamer.
```

---

### 3.2 W-2 — GL-004 Amendment

**Target file:** `Team Knowledge/Core/Guidelines/GL-004_Canonical paths.md`

**Change type:** Replace the entire `## Deliverables` section content (lines 126–141 in the
pre-check baseline).

**Exact current text to replace (baseline confirmed in pre-check):**

```
## Deliverables

Flat structuur — geen domeinsubmappen.

```
Deliverables/YYYYMMDD_Domain_beschrijving/
Deliverables/Archive/
```

Voorbeelden:
- `Deliverables/20260516_Personal_ouderschapsplan/`
- `Deliverables/20260516_Kamer E-commerce_product launch/`
- `Deliverables/20260516_Geldstroom Regie_one-pager/`

**Regel:** domein staat in de mapnaam, nooit als submap.
```

**Exact replacement text:**

```
## Deliverables

Flat structuur — geen domeinsubmappen. Eén folder = één deliverable artifact.

```
Deliverables/YYYYMMDD_Domain_[WorkstreamCode ]ArtifactDescription/
Deliverables/Archive/
```

Voorbeelden:
- `Deliverables/20260516_Personal_Morning Mobility Routine/`
- `Deliverables/20260516_Kamer E-commerce_Remy Research Week 21/`
- `Deliverables/20260516_Geldstroom Regie_One-pager Methodiek/`
- `Deliverables/20260607_Core_DLH Discovery and Proposal/` (workstream code: DLH)
- `Deliverables/20260607_Core_DLH Phase B Triage/`

**Regel:** domein staat in de mapnaam, nooit als submap. Geen workstream-submap.
**WorkstreamCode:** optioneel 2–5 hoofdletters; gebruik wanneer een workstream meer dan één deliverable-folder produceert. Full naming rule: [[GL-001_File naming conventions]].
```

**Changelog entry to append to GL-004:**

```
- 2026-06-08 (Larry, DLH-Task-75): Deliverables section updated — format string extended with optional WorkstreamCode segment, examples updated to English Title Case, one-folder-per-artifact rule made explicit. Approved by Owner Walter Kamer.
```

---

## 4. Post-Check Plan

After all writes are executed:

| Check | Method | Pass condition |
|---|---|---|
| GL-001 File Names by Type row for "Deliverable" shows new format | grep | Row contains `WorkstreamCode` |
| GL-001 File Names by Type row example updated | grep | Row contains `DLH Discovery and Proposal` |
| GL-001 contains "Deliverables Folder Naming" section | grep | Match found |
| GL-001 contains "Deliverables File Naming" section | grep | Match found |
| GL-001 contains "Versioning" section | grep | Match found |
| GL-001 contains workstream code mention (DLH) | grep | Match found |
| GL-001 does NOT contain "Silent overwrite" | grep -c | Zero matches |
| GL-001 line count increased from 79 | wc -l | Greater than 79 |
| GL-004 Deliverables section contains "WorkstreamCode" | grep | Match found |
| GL-004 Deliverables section contains "Eén folder = één deliverable artifact" | grep | Match found |
| GL-004 no longer contains "ouderschapsplan" | grep | No match |

If any post-check fails: halt, report to Owner, do not close Task 75.

---

## 5. Risks

**R-1 — GL-001 table row location shift:** If GL-001 has been modified since the pre-check,
line 33 may have shifted. Mitigation: use the exact row text as the match anchor for the
Edit tool, not a line number. The text `| Deliverable | \`YYYYMMDD_Domain_description/\`` is
unique in the file.

**R-2 — GL-004 Deliverables section content changed:** W-2 replaces the Deliverables section
using the exact baseline text confirmed in the pre-check. If the file has been modified,
the batch-stop fires.

**R-3 — Workstream code collision:** Acknowledged and accepted per Task 85 architecture
assessment. Date-stamped folder names remain unique regardless of code collision.

**R-4 (formerly F-3) — Resolved:** The "Silent overwrite" prohibition has been removed from
GL-001 per Owner decision (F-3 Option B). Task 78 will add this prohibition to SOP-015
as a separate track. No duplication risk.

---

## 6. Authorization Required

This proposal requires:

1. **Owner review** — confirm v02 addresses all review findings before authorizing implementation.
2. **Owner authorization** — explicit confirmation that the exact text in Section 3 is approved as written.
3. **Implementation** — Larry executes W-1 (Changes 1, 2, 3) then W-2 using exact text above.

---

## 7. Exact Authorization Prompt

If Owner confirms v02 is correct, use:

> "GL-001 and GL-004 Amendment Proposal v02 is approved. Execute W-1 Changes 1, 2, and 3, then W-2, as written."

---

*Delivered on: 2026-06-08*
*Delivered at: Deliverables/20260608_Core_DLH GL-001 and GL-004 Amendment Proposal v01/gl-amendment-proposal-v02.md*
