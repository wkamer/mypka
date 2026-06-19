# GL-001 and GL-004 Amendment Proposal v01

**Scope:** Task 75 — Deliverable folder and versioning rule
**Targets:** GL-001 (File Naming Conventions) and GL-004 (Canonical Paths)
**Status:** Awaiting Owner authorization and Iris review before implementation
**Produced by:** Larry, Team Orchestrator
**Date:** 2026-06-08
**Basis:** Owner decision 2026-06-08 — Model A confirmed as canonical unit of work.
Workstream code convention adopted.

**Out of scope for this proposal:**
- Task 77 (English-language rule for governance content) — separate GL-014 proposal
- Task 78 (correction versioning rule, broad scope) — separate SOP-015 proposal
- Task 87 (artifact_type migration) — separate DB migration proposal

---

## 1. Pre-Check Results

Pre-checks performed before writing this proposal. No writes have occurred.

| Check | Result |
|---|---|
| GL-001 contains a "Deliverables" section | No — confirmed absent. Current sections: General Rule, Folder Names, File Names by Type, ALL CAPS, Numbering, Wikilinks, Changelog. |
| GL-001 contains a versioning syntax section | No — confirmed absent. |
| GL-001 current line count | 79 lines |
| GL-004 Deliverables section exists | Yes — lines 126–141. Current text documented in Section 3.2 below. |
| GL-004 contains workstream code mention | No — confirmed absent. |

No collision detected. Proposal may proceed to Iris review and Owner authorization.

---

## 2. Write Structure

**Two writes. One sequence. No batching dependency between them.**

| Write | Target | Type | Batch-stop condition |
|---|---|---|---|
| W-1 | GL-001 — insert three new sections | File edit | If pre-check finds existing Deliverables section, halt and surface to Owner |
| W-2 | GL-004 — update Deliverables section | File edit | If GL-004 Deliverables section content has changed from pre-check baseline, halt and surface to Owner |

Batch-stop across both writes: if W-1 fails or is stopped, do not proceed to W-2.

---

## 3. Exact Amendment Text

### 3.1 W-1 — GL-001 Amendment

**Target file:** `Team Knowledge/Core/Guidelines/GL-001_File naming conventions.md`

**Insertion point:** After the `---` divider that closes the `## File Names by Type` section,
before the `## ALL CAPS` section. In the current file this is between line 47 (`---`) and
line 49 (`## ALL CAPS`).

**What changes:** Three new sections are inserted. The `## ALL CAPS` section and everything
after it is unchanged.

**Text to insert (exact):**

```
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

**Silent overwrite is not permitted.** Corrections to governance deliverables must produce a new versioned file. See [[SOP-015_Proposal Iteration Protocol for System File Changes]].

**Correction Note:** A versioned file at `vNN` where `NN > 01` must include a `## Correction Note` section immediately after the document header, stating what changed from the prior version and why.

---
```

**Changelog entry to append to GL-001:**

```
- 2026-06-08 (Larry, DLH-Task-75): Added Deliverables Folder Naming, Deliverables File Naming, and Versioning sections. Establishes Model A (one folder per artifact) as canonical, optional workstream code convention, file naming and versioning rules. Approved by Owner Walter Kamer.
```

---

### 3.2 W-2 — GL-004 Amendment

**Target file:** `Team Knowledge/Core/Guidelines/GL-004_Canonical paths.md`

**Change type:** Replace the entire `## Deliverables` section content (lines 126–141 in the
pre-check baseline).

**Current text (exact baseline — pre-check confirmed):**

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

**Replacement text (exact):**

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

After both writes are executed:

| Check | Method | Pass condition |
|---|---|---|
| GL-001 contains "Deliverables Folder Naming" section | grep | Match found |
| GL-001 contains "Deliverables File Naming" section | grep | Match found |
| GL-001 contains "Versioning" section | grep | Match found |
| GL-001 contains workstream code mention (DLH) | grep | Match found |
| GL-001 line count increased | wc -l | Greater than 79 |
| GL-004 Deliverables section contains "WorkstreamCode" | grep | Match found |
| GL-004 Deliverables section contains "Eén folder = één deliverable artifact" | grep | Match found |
| GL-004 no longer contains "ouderschapsplan" | grep -v | No match |

If any post-check fails: halt, report to Owner, do not proceed to Task 75 close or Task 87.

---

## 5. Risks

**R-1 — GL-001 section insertion at wrong point:** The three new sections are inserted between
the `---` closing File Names by Type and `## ALL CAPS`. If the file has been modified since
the pre-check, the insertion point may shift. Mitigation: use the exact surrounding text as
the match anchor, not a line number.

**R-2 — GL-004 Dutch examples replaced before Task 77 (English-language rule) is implemented:**
The updated GL-004 examples are in English. Task 77 (GL-014 English-language rule) is not yet
implemented. Risk: the GL-004 update anticipates a rule that does not yet exist in writing.
Assessment: acceptable. GL-004 content is new, not retroactive. English is the target direction.

**R-3 — Workstream code collision:** Two different workstreams independently choose the same
2–5 character code (e.g., both use `LC` for different purposes). Mitigation: the code is
contextual and date-stamped — the folder name still uniquely identifies the artifact. No
registry of codes is required.

---

## 6. Authorization Required

This proposal requires:

1. **Iris review** — route this proposal to Iris for pre-implementation governance check.
2. **Owner authorization** — after Iris review, Owner confirms exact text is approved as written.
3. **Implementation** — Larry executes W-1 and W-2 in sequence using the exact text above.

The Owner does not need to re-read the text after authorization unless Iris surfaces a correction.
If Iris surfaces a correction, this proposal advances to v02 (per SOP-015).

---

## 7. Exact Authorization Prompt (to use after Iris review)

If Iris review passes with no corrections, the Owner may authorize implementation with:

> "GL-001 and GL-004 proposal v01 is approved. Execute W-1 and W-2 as written."

If Iris review surfaces corrections, Larry will produce v02 before re-presenting.

---

*Delivered on: 2026-06-08*
*Delivered at: Deliverables/20260608_Core_DLH GL-001 and GL-004 Amendment Proposal v01/gl-amendment-proposal-v01.md*
