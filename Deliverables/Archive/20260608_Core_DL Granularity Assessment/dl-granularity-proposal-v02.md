# Deliverable Granularity Rules — Implementation Proposal v02

**Date:** 2026-06-08
**Prepared by:** Larry
**Type:** Implementation proposal — not an assessment
**Status:** Awaiting Owner approval before execution
**Basis:** Deliverable Lifecycle Granularity Assessment (2026-06-08), accepted by Owner
**Parent folder:** `20260608_Core_DL Granularity Assessment/` — supporting artifact within
the Granularity Assessment initiative

---

## Revision Note — v01 → v02

**Single change:** Section 5.3 target file path corrected.

| Field | v01 | v02 |
|---|---|---|
| SOP-019 target path | `Team Knowledge/Core/SOPs/SOP-019_[filename].md` | `Team Knowledge/Core/SOPs/SOP-019_Governance Gatekeeper Procedure.md` |

No other changes. All rules, amendment texts, examples, implementation steps, post-checks,
batch-stop rules, and rollback plan are identical to v01.

**Iris review basis:** Review report `review-dl-granularity-proposal-v01.md` applies to
this v02. Check 5 (exact file path) passes with this correction. All other checks carry
forward unchanged.

---

## 1. No-Action Scope

This proposal defines going-forward behavior only.

| Out of scope | Reason |
|---|---|
| Retroactive folder migration | Existing folders remain as-is under their current lifecycle state |
| Database changes | No registry modifications |
| Retroactive reclassification | Existing `deliverable_lifecycle` rows are not affected |
| Deletion of any file or folder | No destructive actions |

---

## 2. Proposed Granularity Rules

### 2.1 Rule G1 — Primary Deliverable (New Folder Required)

An output becomes its own deliverable folder when it satisfies at least one of the
following criteria:

| Criterion | Test |
|---|---|
| G1-A: Standalone reference value | The Owner or a team member would navigate directly to this output by name, independently of any parent process. Example: "where is the Remy research brief?" or "what was the GL-017 proposal?" |
| G1-B: Independent approval event | The Owner made or will make an isolated accept/reject decision on this output as a named artifact, not as an intermediate step in a larger flow |
| G1-C: Persistent citation function | At least one other deliverable, SOP, GL, or AGENT.md references this output by folder name. A cross-reference that would break if this folder did not exist |
| G1-D: Substantive knowledge product | The output contains knowledge that will be extracted and written to a domain database or knowledge base file under its own identity |
| G1-E: Multi-version Iris-reviewed artifact | The output underwent at least one full Iris review round (proposal submitted, Iris verdict received, revision made) and produced version iterations as a result. The iterative review process itself makes the artifact independently trackable |

If none of G1-A through G1-E are satisfied: the output does not get its own folder.

---

### 2.2 Rule G2 — Supporting Artifact (File Inside Existing Folder)

An output is a supporting file inside an existing deliverable folder when it satisfies
any of the following:

| Criterion | Output type | Placement |
|---|---|---|
| G2-A: Version iteration | Same output in a later version (v01 → v02 → v03) | File inside the folder of the primary output |
| G2-B: Review report | Iris review report, pre-review checklist, or governance review output for a specific primary artifact | File inside the folder of the artifact being reviewed |
| G2-C: Execution confirmation | Confirms that a defined set of write actions was authorized and completed | File inside the folder of the deliverable the writes served |
| G2-D: Pre-execution planning tool | Write-list, scoping document, or authorization packet for a defined set of writes | File inside the primary deliverable folder for the initiative that owns those writes — unless the write-list itself triggers G1-E (iterative Iris review), in which case it becomes a primary deliverable |
| G2-E: Process state check | Verification table, state report, or condition check produced to confirm workflow readiness at a specific step | File inside the parent process deliverable, or section in the session log if no relevant deliverable folder exists |
| G2-F: Phase output within an initiative | Discovery document, design document, or scoping output serving one phase of a larger workstream | File inside the primary deliverable folder for that workstream — unless the phase output received independent Owner approval as a standalone artifact (G1-B) |
| G2-G: Decision package | Owner decision packet, authorization summary, or approval record for a specific action within a larger flow | File inside the deliverable folder the decision governs |
| G2-H: Initiation proposal for a governance track | Initiation proposal produced to open a SOP-019 track or analogous governance procedure step | File inside the primary deliverable folder for that track |
| G2-I: Correction note or addendum | Correction record, amendment note, or addendum clarifying an earlier output in the same initiative | File inside the folder of the output being corrected |
| G2-J: Incident report for a process error | Recovery report, incident note, or root-cause record for an error that occurred during a governance procedure | File inside the folder of the initiative where the incident occurred |

---

### 2.3 Rule G3 — Tie-Break

When an output satisfies both a G1 criterion and a G2 criterion, G1 takes precedence
if the output will be independently cited or independently approved. G2 takes precedence
if the output serves only one step in a parent flow and will not be independently
referenced once that step is complete.

When genuinely uncertain: default to G2 (file inside existing folder). Creating a
folder is easier than merging a folder later. A supporting file is never lost; an
over-created folder adds permanent noise.

---

## 3. Output-Type Placement Reference Table

This table defines canonical placement for each output type produced by the governance
procedures currently in use.

| Output type | Rule | Canonical placement | File naming |
|---|---|---|---|
| Primary proposal (GL, SOP, AGENT.md) | G1-B | New folder | `[description]-v01.md` |
| Proposal version iteration | G2-A | Inside proposal's folder | `[description]-v02.md` |
| Iris review report | G2-B | Inside the folder of the artifact reviewed | `review-[description]-v01.md` |
| Owner decision package / review package | G2-G | Inside the folder of the artifact it governs | `owner-decision-[description]-v01.md` |
| Execution report (SOP-017 output) | G2-C | Inside the folder of the deliverable the writes served | `er-[description]-v01.md` |
| Write-list (non-Iris-reviewed) | G2-D | Inside the primary deliverable folder for the initiative | `write-list-[description]-v01.md` |
| Write-list (Iris-reviewed, multi-version) | G1-E | New folder | `[description]-write-list-v01.md` |
| Triage report | G1-A, G1-B | New folder — triage outputs are primary deliverables | `triage-[description]-v01.md` |
| Architecture assessment | G1-A, G1-B | New folder | `assessment-[description]-v01.md` |
| Closure report | G1-A, G1-D | New folder | `closure-[description]-v01.md` |
| Session start verification | G2-E | File inside parent process deliverable, or session log section | `session-verification-[description]-v01.md` |
| Governance state check | G2-E | File inside parent process deliverable | `state-check-[description]-v01.md` |
| Initiation proposal (SOP-019 track) | G2-H | File inside the track's primary deliverable folder | `initiation-proposal-v01.md` |
| Phase discovery document | G2-F | File inside the initiative's primary deliverable folder | `discovery-[description]-v01.md` |
| Phase design document | G2-F | File inside the initiative's primary deliverable folder | `design-[description]-v01.md` |
| Smoke test proposal | G2-F | File inside the initiative's primary deliverable folder | `smoke-test-proposal-v01.md` |
| Recovery / incident report | G2-J | File inside the initiative folder where the incident occurred | `incident-[description]-v01.md` |
| Correction note / addendum | G2-I | File inside the folder of the output being corrected | `correction-note-v01.md` |
| Retroactive assessment (e.g., LC retrospective) | G2-E or G2-F | File inside the initiative deliverable folder | `retrospective-[description]-v01.md` |
| Task-specific assessment (internal process check) | G2-E | File inside the most relevant initiative deliverable folder | `task-assessment-[description]-v01.md` |
| Personal deliverable (plan, routine, schema) | G1-A | New folder | `[description].md` |
| Research brief / domain knowledge product | G1-D | New folder | `[description].md` |

---

## 4. Examples Using Recent DLH and SOP-019 Folders

These examples show how current folders would be placed under the proposed rules.
They are retrospective illustrations only — no migration is proposed.

### Example 1 — LC Batch 1 Write-List and Execution Report

**Current (two separate folders):**
- `20260607_Core_LC Batch 1 Write-List/` (1 file)
- `20260607_Core_LC Batch 1 Execution Report/` (1 file)

**Under proposed rules:**
Both are files inside `20260607_Core_LC Naming Alignment Impact Assessment/` (the
primary initiative deliverable for the LC naming alignment work):
- `write-list-lc-batch1-v01.md` — Rule G2-D
- `er-lc-batch1-v01.md` — Rule G2-C

The impact assessment folder already contains the scope and findings. The write-list
and execution report are process instruments serving that scope. They have no
standalone reference value beyond confirming that the writes were authorized and done.

---

### Example 2 — Session Start Verification Reports (three folders)

**Current (three separate folders):**
- `20260607_Core_LCL Session Start Verification/` (3 files)
- `20260607_Core_Post-SOP-019 Session Start Verification/` (1 file)
- `20260607_Core_Final Governance State Verification/` (1 file)

**Under proposed rules:**
All three are files inside the session log for 2026-06-07, or inside the most relevant
active process deliverable at the time:
- `session-verification-lcl-v01.md` → session log or LC triage deliverable folder — Rule G2-E
- `session-verification-post-sop019-v01.md` → session log or SOP-019 deliverable folder — Rule G2-E
- `state-check-final-governance-v01.md` → session log — Rule G2-E

State verification tables confirm process readiness at a workflow step. They belong in
the session record, not in standalone lifecycle artifacts.

---

### Example 3 — SOP-019 Track 1 and Track 2 (LC-5/LC-6/LC-7)

**Current (per-track folders):**
- `20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards/` (5 files)
- `20260607_Core_SOP-019 LC-6 Execution Briefing Rule/` (5 files)
- `20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4/` (1 file)

**Under proposed rules:**
Track 1 and Track 2 each have multi-version Iris-reviewed proposals — they satisfy G1-E.
They correctly warrant their own folders. This pattern is already correct.

The `SOP-019 Initiation Proposal Learning Candidate 4` (1 file, no Iris review, no
execution report inside) would instead be placed as `initiation-proposal-v01.md` inside
the `SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards/` folder it initiated.

---

### Example 4 — DLH Phase A: Discovery and Design (two separate folders)

**Current (two separate folders):**
- `20260607_Core_Auto-Processing Deliverable Lifecycle Discovery/` (1 file)
- `20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design/` (1 file)

**Under proposed rules:**
Both are files inside the primary initiative deliverable for the Deliverable Lifecycle
auto-processing workstream:
- `discovery-scope-proposal-v01.md` — Rule G2-F
- `phase1-design-v01.md` — Rule G2-F

The initiative would have one folder, e.g.:
`20260607_Core_Deliverable Lifecycle Auto-Processing Initiative/`
containing both files plus any subsequent execution reports and Iris reviews.

---

### Example 5 — This Proposal (self-referential)

**Under proposed rules:**
This proposal is placed as `dl-granularity-proposal-v02.md` inside
`20260608_Core_DL Granularity Assessment/` — Rule G2-A (version iteration of v01)
and Rule G2-F (phase-2 output of the Granularity Assessment initiative).

The v01 Iris review report and Owner decision package are also inside this folder
(Rules G2-B and G2-G respectively). The folder holds the complete initiative record:
assessment, proposal v01, proposal v02, review report, and Owner decision package.

---

## 5. Proposed Exact Amendments

### 5.1 GL-017 Amendment

**Target file:** `Team Knowledge/Core/Guidelines/GL-017_Deliverable Lifecycle Knowledge
Processing and Archiving.md`

**Change type:** New section inserted after existing Section 2 (Scope). Existing sections
3 through 7 are renumbered (3 → 4, etc.) or the new section is added as Section 2.1 and
2.2 without renumbering.

**Proposed addition — insert as Section 2.1 and 2.2 after the current Section 2 body:**

---

> **2.1 Primary Deliverable — New Folder Required**
>
> A team output constitutes a primary deliverable and receives its own lifecycle folder
> when it satisfies at least one of the following criteria:
>
> | Criterion | Description |
> |---|---|
> | G1-A: Standalone reference value | The Owner or a team member would navigate to this output by name, independently of any parent process |
> | G1-B: Independent approval event | The Owner made or will make an isolated accept/reject decision on this output as a named artifact |
> | G1-C: Persistent citation function | At least one other deliverable, SOP, GL, or AGENT.md references this output by folder name |
> | G1-D: Substantive knowledge product | The output contains knowledge that will be extracted to a domain database or knowledge base under its own identity |
> | G1-E: Multi-version Iris-reviewed artifact | The output underwent at least one full Iris review round and produced version iterations as a result |
>
> If none of G1-A through G1-E are satisfied, the output does not receive its own folder.
>
> **2.2 Supporting Artifact — File Inside Existing Folder**
>
> A team output is a supporting artifact and is placed as a file inside an existing
> deliverable folder when it falls into any of the following categories:
>
> - Version iterations of a primary deliverable (v01 → v02)
> - Review reports (Iris review reports, governance review outputs) for a specific artifact
> - Execution confirmation records (confirms write actions were authorized and completed)
> - Pre-execution planning tools (write-lists, scoping documents) that did not undergo iterative Iris review
> - Process state checks and session verification reports
> - Phase outputs within an initiative (discovery, design, smoke test) that were not independently approved
> - Decision packages and authorization records for a specific action within a larger flow
> - Initiation proposals for governance track steps (SOP-019 and equivalent)
> - Correction notes, addenda, and incident reports for process errors
>
> When placement is uncertain: default to supporting artifact (file inside existing folder).
> Creating a folder is reversible; folder proliferation compounds.
>
> The canonical placement reference and file naming conventions for each output type are
> defined in SOP-017, Section 4a (Output Placement Reference).

---

### 5.2 SOP-017 Amendment

**Target file:** `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge
Processing and Archiving Procedure.md`

**Change type:** New section 4a inserted after existing Section 4 (Lifecycle Decision
Workflow). Existing sections 5 through 17 are not renumbered.

**Amendment to Section 16 (Execution Report Requirements):**
Add the following as the first paragraph of Section 16:

---

> **Execution report placement:** An execution report produced under this SOP is written
> as a file inside the deliverable folder it describes, unless the execution report itself
> satisfies G1-A, G1-B, G1-C, or G1-D of GL-017 Section 2.1. The execution report file
> is named `er-[description]-v01.md`. It does not receive its own deliverable folder. The
> execution report is a supporting artifact (GL-017 Section 2.2, G2-C) of the deliverable
> it reports on.
>
> Exception: if the execution report documents a governance-significant incident, failure,
> or systemic finding that warrants independent reference, it may qualify as G1-A or G1-D
> and receive its own folder. This exception requires explicit Larry judgment and Owner
> confirmation.

---

**New section 4a — Output Placement Reference:**

Insert after Section 4 (Lifecycle Decision Workflow):

---

> **4a. Output Placement Reference**
>
> Before producing any output during lifecycle processing, apply the granularity test
> from GL-017 Sections 2.1 and 2.2. Use this table as the operational reference:
>
> | Output type | Placement |
> |---|---|
> | Execution report | File inside the deliverable it describes — `er-[description]-v01.md` |
> | Write-list (non-Iris-reviewed) | File inside the initiative's primary deliverable folder — `write-list-[description]-v01.md` |
> | Write-list (Iris-reviewed, multi-version) | New folder (satisfies G1-E) |
> | Owner decision package | File inside the deliverable it governs — `owner-decision-[description]-v01.md` |
> | Review report (Iris or governance) | File inside the folder of the artifact reviewed — `review-[description]-v01.md` |
> | Session / state verification | File inside the parent process deliverable, or section in session log — `state-check-[description]-v01.md` |
> | Correction note or addendum | File inside the folder being corrected — `correction-note-v01.md` |
> | Incident / recovery report | File inside the initiative folder where the incident occurred — `incident-[description]-v01.md` |
> | Phase document (discovery, design) | File inside the initiative's primary folder — `discovery-[description]-v01.md` |
> | Primary proposal (GL, SOP, AGENT.md) | New folder (satisfies G1-B and G1-E) |
> | Triage report | New folder (satisfies G1-A and G1-B) |
> | Assessment | New folder (satisfies G1-A and G1-B) |
> | Closure report | New folder (satisfies G1-A and G1-D) |

---

### 5.3 SOP-019 Amendment

**Target file:** `Team Knowledge/Core/SOPs/SOP-019_Governance Gatekeeper Procedure.md`

**Note:** The exact section number for placement requires reading the current SOP-019
structure before writing. The amendment text is specified here; section placement is
confirmed at write time.

**Amendment text — add to the track execution section:**

---

> **Track artifact placement:**
> Artifacts produced during a SOP-019 track (initiation proposals, Iris review reports,
> execution reports, correction notes) are files inside the track's primary deliverable
> folder, not standalone deliverable folders.
>
> The track's primary deliverable folder is the folder that represents the output the
> track was opened to produce or amend. If no primary deliverable folder exists for the
> track at initiation, create one at that point.
>
> File placement within the track folder:
> - Initiation proposal: `initiation-proposal-v01.md` (and v02, v03 as iterations)
> - Iris review report: `review-[track-description]-v01.md`
> - Execution report: `er-[track-description]-v01.md`
> - Correction note: `correction-note-v01.md`
>
> Exception: if the track produces a new primary deliverable (a new GL, SOP, or
> AGENT.md) that will be independently cited, that output is a new folder in its own
> right per GL-017 Section 2.1. The initiation proposal and execution report for the
> track remain as files inside the track's deliverable folder, not inside the new GL/SOP
> folder.

---

### 5.4 Larry CLAUDE.md Amendment

**Target file:** `CLAUDE.md` (project root)

**Change type:** Additive rule in the Hard Rules section, inserted after the existing
"Domain Check Before Execution" rule.

**Amendment text:**

---

> ### Granularity Gate — Deliverable Folder Creation (mandatory)
>
> Before creating any deliverable folder: apply the GL-017 granularity test (Sections
> 2.1 and 2.2).
>
> Ask: does this output satisfy at least one of G1-A through G1-E?
>
> - If yes: create a new folder.
> - If no: place the output as a file inside the most relevant existing deliverable folder.
>   If no relevant folder exists, use the active initiative folder for the workstream.
>
> Default is G2 (file inside existing folder). Creating a new folder requires an affirmative
> answer to at least one G1 criterion. Uncertainty resolves to G2.
>
> **What this catches:** execution reports, write-lists, session verification reports,
> initiation proposals for governance track steps, phase discovery/design documents,
> incident reports, correction notes, and decision packages for specific actions within
> a larger flow. These do not become standalone folders.
>
> **What this does not affect:** primary proposals, triage reports, architecture assessments,
> research briefs, closure reports, personal deliverables, and any output independently
> approved or cited by the Owner. These continue to receive their own folders.
>
> **Violation trigger:** If Larry creates a deliverable folder without applying this check —
> stop, note the potential misclassification, apply the test retroactively, and report
> to Owner if the folder should have been a file.

---

## 6. Implementation Steps

These steps are executed only after Owner approval of this proposal. Steps are sequential.
Each step is gated by the batch-stop rules in Section 8.

| Step | Action | Actor | Target file |
|---|---|---|---|
| 1 | Owner approval of this proposal (v02) | Owner | This file |
| 2 | Iris review gate — v01 review report carries forward; v02 corrects Check 5 FAIL; all 13 checks now pass | Iris (complete) | `review-dl-granularity-proposal-v01.md` |
| 3 | Write GL-017 amendment (Sections 2.1 and 2.2) | Larry or Kai | `Team Knowledge/Core/Guidelines/GL-017_Deliverable Lifecycle Knowledge Processing and Archiving.md` |
| 4 | Write SOP-017 amendment (Section 16 addition + new Section 4a) | Larry or Kai | `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md` |
| 5 | Read SOP-019 structure; confirm section placement; write SOP-019 amendment | Larry or Kai | `Team Knowledge/Core/SOPs/SOP-019_Governance Gatekeeper Procedure.md` |
| 6 | Write CLAUDE.md amendment (Granularity Gate rule) | Larry | `CLAUDE.md` |
| 7 | Post-check execution (Section 7) | Larry | All amended files |
| 8 | Update `deliverable_lifecycle` registry rows for this proposal (state transition) | Larry | `team-knowledge.db` |
| 9 | Write execution report | Larry | Inside this folder: `er-dl-granularity-proposal-v01.md` |

---

## 7. Post-Checks

After all write steps complete:

| Check | Method | Pass condition |
|---|---|---|
| P1 — GL-017 contains granularity test | Read GL-017 Sections 2.1 and 2.2 | Both sections present; G1-A through G1-E and G2-A through G2-J criteria listed |
| P2 — SOP-017 Section 16 updated | Read SOP-017 Section 16 | First paragraph contains execution report placement rule |
| P3 — SOP-017 Section 4a present | Read SOP-017 | Section 4a exists with output placement reference table |
| P4 — SOP-019 track placement rule present | Read SOP-019 track execution section | Track artifact placement paragraph present |
| P5 — CLAUDE.md Granularity Gate present | Read CLAUDE.md Hard Rules section | Granularity Gate block present with G1/G2 decision logic |
| P6 — No conflicts with existing GL-017 principles | Read GL-017 Sections 3 and 4 | No G1/G2 language contradicts P1 through P13 |
| P7 — No conflicts with GL-016 review gate | Read GL-016 | Granularity rules do not alter what constitutes a governance-relevant deliverable |
| P8 — Example validation | Apply granularity test to three recent DLH outputs | Results match expected placement per Section 4 |

---

## 8. Batch-Stop Rules

The following conditions halt execution of all remaining write steps. The executor stops,
records the halt reason, and escalates to the Owner before any further action.

| Batch-stop condition | Trigger |
|---|---|
| BS-1: GL-017 write fails or produces unexpected content | Any error during Step 3, or GL-017 read-back shows missing sections |
| BS-2: GL-017 amendment conflicts with existing GL-017 principles P1–P13 | Post-check P6 fails |
| BS-3: SOP-017 write fails or produces unexpected content | Any error during Step 4, or SOP-017 read-back shows missing content |
| BS-4: SOP-017 amendment conflicts with GL-017 or GL-015 routing rules | Any conflict identified during P3 or P4 post-check |
| BS-5: SOP-019 structure does not match expected section layout | Read of SOP-019 in Step 5 reveals structure incompatible with amendment |
| BS-6: CLAUDE.md write fails | Any error during Step 6 |
| BS-7: Post-check P8 (example validation) produces unexpected placements | The granularity test as written classifies more than three existing recent deliverables incorrectly as G2 when they should be G1 |
| BS-8: Owner withdraws approval during execution | Any Owner instruction to pause or stop mid-execution |

**No batch-stop rule may be overridden without explicit Owner instruction recorded in
the execution report.**

---

## 9. Rollback Plan

This proposal makes additive changes only. No files are deleted. No folders are moved.
No database rows are altered (except the registry state update in Step 8, which records
the proposal's own lifecycle transition).

**Rollback scope:** Revert content of the four amended files to their pre-amendment state.

| Rollback action | Method |
|---|---|
| GL-017 rollback | Restore pre-amendment GL-017 from session log or git history |
| SOP-017 rollback | Restore pre-amendment SOP-017 from session log or git history |
| SOP-019 rollback | Restore pre-amendment SOP-019 from session log or git history |
| CLAUDE.md rollback | Remove the Granularity Gate block from the Hard Rules section |
| Registry rollback | Not required — Step 8 is a state transition for this proposal's own row, not a schema change |

**Rollback trigger:** Any Owner instruction, or any BS condition that cannot be resolved
within the same session.

**Rollback side effects:** None. The granularity rules would not yet have been applied to
any new output (going-forward only). No folders or files would need to be un-created.

---

## 10. No Associated Write-List Note

This proposal does not have a separate write-list. The implementation steps in Section 6
serve the function of a write-list. A separate write-list document is not warranted — it
would be a G2-D artifact that belongs here, not in a new folder, consistent with the rules
this proposal defines.

There is therefore no write-list batch-stop inheritance concern. The batch-stop rules in
Section 8 are the complete and authoritative batch-stop set for this proposal's
implementation.

---

Delivered on: 2026-06-08
Delivered at: Deliverables/20260608_Core_DL Granularity Assessment/dl-granularity-proposal-v02.md
