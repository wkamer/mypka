# PROPOSAL — SOP-017 Amendment: Source Folder Closure After Archive

**Proposal status:** Draft v02
**Prepared by:** Larry (Team Orchestrator)
**Date:** 2026-06-05
**For:** Owner Walter Kamer
**Amends:** `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md`
**Governance baseline:** GL-014, GL-017, SOP-015, SOP-016, SOP-017, GL-018, SOP-018 (SOP-016 RCP amendment)

---

> **PROPOSAL ONLY.**
> Nothing in this document is implemented, active, or authoritative until the Owner explicitly approves it. SOP-017 is not modified by this proposal document. No system files are created, modified, or moved. No indexes are updated. No execution follows from this document without explicit Owner approval.

> **Exact-text amendment.** If approved, this proposal authorizes additions to four sections of SOP-017: Section 10, Section 13, Section 14, and Section 16. The exact text of all additions is specified below. No other changes are made to SOP-017.

---

## Idea Classification

| Field | Value |
|---|---|
| Scenario | S8 — Governance-Relevant Idea |
| Impact | Low |
| Route | Route D — SOP-015 Proposal Iteration Protocol |
| DP-1 | Owner confirmed classification and Route D via task instruction (2026-06-05) |
| DP-3 | Pending Owner review of this proposal after Review Gate |
| DP-4 | Pending separate Owner implementation confirmation |

**Classification rationale:** The amendment modifies SOP-017, a governance file. S8 applies. Impact is Low: the change is purely additive (new steps, new rule, new report fields); no existing rules are changed or removed; no new system components are introduced; the risk profile is minimal.

---

## Purpose

During the lifecycle processing of the Idea-to-Implementation Governance Pack v05, all authorized deliverables were successfully archived. However, the now-empty active source folder (`Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/`) was not removed as part of the lifecycle execution. This required a separate manual correction by Owner Walter Kamer.

SOP-017 currently governs archive actions for individual files. It does not define what happens to the source folder after all files in it have been archived. The absence of this rule means that empty source folders can accumulate in the active Deliverables tree, creating structural noise and potential confusion between active and completed work.

This amendment closes the gap by:

1. Making source folder closure a mandatory final step of every lifecycle execution that includes an archive action (Section 10 and EX-8)
2. Providing clear behavior for empty folders (delete and record) and non-empty folders (list, surface, hold)
3. Specifying that the source folder check must use a hidden-file-aware method so that folders containing only hidden files are not incorrectly treated as empty
4. Adding required execution report fields to make source folder status auditable (Section 16)
5. Adding a post-execution safeguard checklist item (Section 13)

---

## Current State of SOP-017

SOP-017 currently covers:

- Section 10: Archiving procedure — governs the archive action for individual files; ends with "Write execution report documenting all actions." No step exists for source folder cleanup.
- Section 13: Safeguards Checklist — post-execution items address source file retention and no unintended side effects; no mention of source folder status.
- Section 14: Explicit Rules EX-1 through EX-7 — covers prerequisites, Owner approval requirements, database writes, system file changes, lessons learned, archive proposals, and anti-recursion. No rule addresses source folder closure.
- Section 16: Execution Report Requirements — fields 1 through 13; no field for source folder status.

**Gap:** Lifecycle cleanup has no Definition of Done that includes source folder state. An empty source folder left in active Deliverables is invisible to the governance process until it is noticed manually.

---

## Proposed Amendments

### Amendment A — Section 10: Archiving — add Source Folder Closure subsection

**Location in current file:** End of the Archiving subsection, after the paragraph beginning "After the archive move is executed..."

**Current last block of Archiving subsection:**

> After the archive move is executed:
> - Record the Archived primary state transition in the execution report. Do not write to the source file; the execution report is the governance record.
> - Reference updates in other files follow the same rules as Superseded handling: explicit Owner approval per file; system file updates require SOP-015 proposal.
> - Write execution report documenting all actions.

**Proposed addition (new subsection, appended immediately after the Archiving block):**

---

#### Source Folder Closure (mandatory after every archive action)

After all authorized archive moves in the current lifecycle execution are complete, the Maintainer checks the source folder using a method that surfaces hidden files (e.g., `ls -A` on Linux/macOS, or the platform-equivalent command). The folder is considered empty only when no files are returned, including hidden files.

**If the source folder is empty:**

1. Delete the empty source folder.
2. Record the deletion in the lifecycle execution report: source folder path, confirmation that the folder was empty, confirmation that it was deleted (see Section 16 fields 14 through 18).

**If the source folder is not empty:**

1. Do not delete the folder.
2. List all remaining files in the execution report (see Section 16 field 17).
3. Surface the remaining files to the Owner with a brief description of each.
4. Do not claim lifecycle cleanup complete until the Owner has made a decision about each remaining file.

**Scope:** This check applies to the source folder from which files were archived in this lifecycle execution. It does not apply to parent folders, sibling folders, or folders that were not part of the archive scope.

---

### Amendment B — Section 13: Safeguards Checklist — add post-execution item

**Location in current file:** Post-execution checklist, after the final item "Execution report is written and complete per Section 16."

**Proposed addition (new checklist item appended to post-execution list):**

> - [ ] If archiving was executed: source folder checked per Section 10 Source Folder Closure; source folder status recorded in execution report fields 14 through 18 (see Section 16)

---

### Amendment C — Section 14: Explicit Rules — add EX-8

**Location in current file:** After EX-7 (Anti-recursion rule).

**Proposed addition:**

> **EX-8: Source folder closure is part of lifecycle cleanup Definition of Done.**
> After all authorized archive moves are executed in a lifecycle execution, the source folder must be checked using a method that surfaces hidden files (e.g., `ls -A` on Linux/macOS, or the platform-equivalent command); a folder that contains only hidden files must not be treated as empty. If the source folder is empty, it must be deleted and the deletion recorded in the execution report. If the source folder is not empty, the remaining files must be listed in the execution report and surfaced to the Owner. Lifecycle cleanup is not complete and may not be reported as Done until: the source folder check has been performed, the result has been recorded in the execution report, and (if files remain) the Owner has made a decision about each remaining file. This rule applies to every lifecycle execution that includes at least one archive action. It does not apply to lifecycle executions that contain no archive action.

---

### Amendment D — Section 16: Execution Report Requirements — add fields 14 through 18

**Location in current file:** After field 13 ("Next steps").

**Proposed addition (five new fields):**

> 14. **Source folder checked** — yes / no / not applicable. State "not applicable" only when no archive action was executed in this lifecycle action. When an archive action was executed, this field must be "yes"; "no" is not a valid answer when an archive action occurred.
>
> 15. **Source folder empty after archiving** — yes / no / not applicable (not applicable when field 14 is not applicable).
>
> 16. **Source folder deleted** — yes / no / not applicable. "not applicable" only when no archive action was executed (field 14 is not applicable). "no" when an archive action was executed but the source folder was not deleted because files remained. "yes" when the source folder was empty and was successfully deleted.
>
> 17. **Remaining files in source folder** — not applicable / none / [exact list of filenames remaining]. State "not applicable" only when no archive action was executed (field 14 is not applicable). State "none" only when an archive action was executed and the folder was empty after hidden-file-aware checking. When files remain, list each filename explicitly; do not summarize.
>
> 18. **Reason if folder retained** — state the reason the source folder was not deleted: files remain (list them in field 17); Owner decision pending; archive action was not part of this lifecycle execution; other (specify). Omit if folder was successfully deleted.

---

## Affected Sections

| Section | Change type | Change summary |
|---|---|---|
| Section 10 — Archiving | Addition — new subsection | Source Folder Closure steps: hidden-file-aware check, empty → delete and record, not empty → list, surface, hold |
| Section 13 — Safeguards Checklist | Addition — one post-execution checklist item | Links to EX-8 and Section 16 fields 14–18 |
| Section 14 — Explicit Rules | Addition — new EX-8 | Definition of Done: hidden-file-aware check mandatory; lifecycle cleanup not complete until check performed and recorded |
| Section 16 — Execution Report Requirements | Addition — fields 14 through 18 | Source folder status fields: checked, empty, deleted, remaining files, reason if retained |

**Sections not modified:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 17. Existing EX-1 through EX-7 unchanged. Existing decision rules R1 through R10 unchanged. Existing report fields 1 through 13 unchanged.

---

## Risks

| Risk | Description | Mitigation |
|---|---|---|
| Shared source folder | Source folder contains both archived files and unrelated active files. Deleting it would destroy active work. | The "if not empty, do not delete" path prevents this. All remaining files are listed and surfaced to Owner; no deletion without Owner decision. |
| Over-broad scope | Maintainer applies the check to parent or sibling folders. | Amendment A explicitly scopes the check to the source folder from which files were archived. Parent and sibling folders are out of scope. |
| False empty | Source folder appears empty but contains hidden files. | Amendment A specifies that the check must use a method that surfaces hidden files (e.g., `ls -A` on Linux/macOS, or the platform-equivalent command). A folder is considered empty only when no files are returned, including hidden files. EX-8 reiterates this requirement at the hard-rule level. |
| Retroactive application | Existing archived packs still have empty source folders. | EX-8 applies to future executions only. Retroactive cleanup of existing empty folders is a separate decision for Owner to make; it is not authorized by this amendment. |
| Scope creep into GL-017 | This amendment could be argued to require a GL-017 update. | The Definition of Done is procedural (how to close out a lifecycle execution), not a principle change. GL-017 defines lifecycle states and markers; it does not need to enumerate cleanup steps. This amendment correctly lives in SOP-017. |

---

## Acceptance Criteria

This proposal is acceptable when all of the following are true:

1. The source folder closure steps in Amendment A are clear and actionable: empty folder → delete and record; non-empty folder → list files, surface to Owner, hold lifecycle Done claim.
2. The source folder closure is governed as mandatory: EX-8 uses unambiguous language ("must be checked," "must be deleted," "may not be reported as Done until").
3. EX-8 correctly scopes the rule: applies to every lifecycle execution that includes at least one archive action; does not apply when no archive action was executed.
4. The five new Section 16 fields (14 through 18) cover all cases: archive executed / not executed, folder empty / not empty, folder deleted / retained, remaining files listed.
5. Field 14 correctly makes "not applicable" the only acceptable answer when no archive action occurred, and makes "yes" mandatory when an archive action did occur.
6. Amendment B (Safeguards Checklist) is minimal: one checklist item that links to EX-8 and Section 16 fields 14–18 without duplicating the rule text.
7. No existing section, rule (EX-1 through EX-7), decision rule (R1 through R10), or report field (1 through 13) of SOP-017 is modified.
8. The amendment does not change the archive proposal requirement in EX-6: a formal archive proposal is still required before any file is moved; this amendment adds the source folder check as a post-archive step, not a replacement of EX-6.
9. The amendment does not authorize deleting non-empty folders under any circumstance.
10. The amendment does not authorize retroactive cleanup of existing empty folders; it applies to future executions only.
11. No other governance files (GL-017, GL-016, SOP-016, SOP-015, SOP-018, GL-018) are modified.
12. No execution has occurred as a result of this proposal document.
13. The source folder check in Amendment A uses explicit hidden-file-aware language: the Maintainer must use a method that surfaces hidden files (e.g., `ls -A` on Linux/macOS, or the platform-equivalent command), and the folder is considered empty only when no files are returned, including hidden files.
14. EX-8 contains explicit hidden-file-aware language: the source folder must be checked using a method that surfaces hidden files; a folder containing only hidden files must not be treated as empty.
15. The Owner Decision Options in this proposal clearly separate DP-3 (proposal acceptance) from DP-4 (implementation confirmation): "Accept proposal at DP-3" explicitly states that it does not authorize implementation and that a separate DP-4 confirmation is required before SOP-017 may be modified.
16. Section 16 field 16 uses "no" (not "not applicable") when an archive action was executed but the folder was not deleted because files remained. "Not applicable" is reserved only for when no archive action was executed.
17. Section 16 field 17 explicitly states "not applicable" when no archive action was executed, and "none" only when the archive action occurred and the folder was empty after hidden-file-aware checking.

---

## Owner Decision Options

| Option | Meaning |
|---|---|
| Accept proposal at DP-3 | Amendment proposal accepted as stated after Review Gate findings. This does not authorize implementation. Separate DP-4 implementation confirmation is required before SOP-017 may be modified. |
| Request amendments | Specific changes required before re-review; a v03 amendment proposal is prepared. SOP-017 is not modified until a version is approved. |
| Defer | Proposal noted; no action until Owner names a condition for revisit. |
| Reject | Amendment not accepted; reason stated; SOP-017 remains unchanged. |

---

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-06-05 | v01 | Initial proposal |
| 2026-06-05 | v02 | Review Gate findings applied (review-gate-findings-sop-017-source-folder-closure-amendment-v01.md). Six corrections: (1) Amendment A procedure text updated to include hidden-file-aware check specification (`ls -A` or platform-equivalent) — previously present in risk table only, not in the executable amendment text; (2) EX-8 updated to include hidden-file-aware language at the hard-rule level, aligning procedure and rule; (3) Section 16 field 16 corrected — "not applicable" now reserved for no-archive-action case only; "no" used when archive executed but folder not deleted due to remaining files; (4) Section 16 field 17 corrected — "not applicable" explicitly stated when no archive action was executed; (5) Owner Decision Options corrected to separate DP-3 (proposal acceptance, does not authorize implementation) from DP-4 (separate implementation confirmation required before SOP-017 may be modified), per live SOP-018 Section 12; (6) Acceptance Criteria items 13 through 17 added to cover the four corrections and DP-3/DP-4 separation. |

---

Delivered on: 2026-06-05
Delivered at: Deliverables/20260605_Core_SOP-017 Source Folder Closure Amendment/
