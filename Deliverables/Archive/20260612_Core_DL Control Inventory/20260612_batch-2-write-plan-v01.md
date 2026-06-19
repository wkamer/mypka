# Batch 2 Write Plan v01

**Date:** 2026-06-12
**Author:** Governance Assistant
**Status:** Awaiting Owner authorization before any execution
**Task reference:** team_task 94
**Placement:** G2 — file inside `20260612_Core_DL Control Inventory/`
**Scope basis:** `20260612_batch-2-scope-proposal-v01.md` (Owner approved 2026-06-12)
**Operating model reference:** `20260612_d-folder-operating-model-proposal-v02.md` (Owner approved 2026-06-12)

---

No execution is authorized by this document.
Execution begins only after Owner explicitly authorizes this write plan.
This document may be reviewed, corrected, or rejected before any action is taken.

---

## 1. Approved Batch 2 Scope

| # | Lifecycle id | Folder |
|---|---|---|
| 1 | 60 | `20260608_Core_UMC Archive Eligibility Analysis 20260530` |
| 2 | 61 | `20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen` |
| 3 | 68 | `20260608_Core_Phase 1 Proposal R1 R5 v02` |

**Batch size: 3** — within the 5-folder maximum per the approved operating model.

---

## 2. Explicit Exclusions

The following are explicitly excluded from this write plan and must not be touched:

| Lifecycle id | Folder | Reason |
|---|---|---|
| 62 | `20260608_Core_Retention Assessment P2 P5 UMC` | Frozen — GL-013 open signal |
| 63 | `20260608_Core_Write Proposal GL-013 Additions P2 P5` | Conditional — pending GL-013 confirmation |

All Category A, C, and D folders are also excluded and must not be touched.

---

## 3. Exact Move Actions

Archive destination: `Deliverables/Archive/`

Execute in order. Halt immediately on any error (see Section 5 — Stop Rules).

| Step | Action | Command |
|---|---|---|
| M-1 | Move id 60 | `mv "/opt/myPKA/Deliverables/20260608_Core_UMC Archive Eligibility Analysis 20260530" "/opt/myPKA/Deliverables/Archive/"` |
| M-2 | Move id 61 | `mv "/opt/myPKA/Deliverables/20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen" "/opt/myPKA/Deliverables/Archive/"` |
| M-3 | Move id 68 | `mv "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v02" "/opt/myPKA/Deliverables/Archive/"` |

**Pre-condition check before M-1:** confirm all 3 source folders exist on filesystem.
If any source folder is missing: halt before executing any move. Report to Owner.

---

## 4. Exact DB Update Actions

Database: `/opt/myPKA/Team Knowledge/team-knowledge.db`
Table: `deliverable_lifecycle`

Execute each UPDATE only after its corresponding move step has succeeded.
Halt immediately on any DB error (see Section 5 — Stop Rules).

| Step | After move | SQL |
|---|---|---|
| DB-1 | After M-1 | `UPDATE deliverable_lifecycle SET state_gl017 = 'archived', owner_decision = 'Archived in Batch 2 — 2026-06-12. Scope approved by Owner.' WHERE id = 60;` |
| DB-2 | After M-2 | `UPDATE deliverable_lifecycle SET state_gl017 = 'archived', owner_decision = 'Archived in Batch 2 — 2026-06-12. Scope approved by Owner.' WHERE id = 61;` |
| DB-3 | After M-3 | `UPDATE deliverable_lifecycle SET state_gl017 = 'archived', owner_decision = 'Archived in Batch 2 — 2026-06-12. Scope approved by Owner.' WHERE id = 68;` |

**Verification after each DB update:** confirm `SELECT state_gl017 FROM deliverable_lifecycle WHERE id = <n>` returns `'archived'` before proceeding to the next step.

---

## 5. Stop Rules

Per the approved operating model (Section 3.7 of `20260612_d-folder-operating-model-proposal-v02.md`).

Halt the batch immediately — before any further move or DB update — if any of the following occur:

| Stop rule | Condition | Action |
|---|---|---|
| SC-1 | A source folder is missing from the filesystem before M-1 | Halt entire batch. Report to Owner. Do not proceed. |
| SC-2 | Any `mv` command returns a non-zero exit code | Halt. Do not execute the corresponding DB update. Report to Owner. |
| SC-3 | Any DB UPDATE fails or returns rowcount != 1 | Halt. Report anomaly to Owner. Do not proceed to next move step. |
| SC-4 | Any verification SELECT returns a value other than `'archived'` | Halt. Report to Owner. Do not proceed. |
| SC-5 | Any folder in the batch is found to be referenced by a live SOP, GL, or CLAUDE.md at execution time | Halt entire batch. Report to Owner. |
| SC-6 | id 62 or id 63 folder is encountered during any step | Halt. Do not touch. Report to Owner. |

A halted batch is not a failed batch. Owner decides whether to retry, skip, or close.
Partial completion (some moves done, some not) must be reported exactly as-is in the execution report.

---

## 6. Execution Report Requirement

Immediately after execution completes (or halts), Larry writes an execution report.

**File location:** G2 — file inside `Deliverables/20260612_Core_DL Control Inventory/`
**Suggested filename:** `20260612_batch-2-archive-execution-report-v01.md`

The execution report must include:
- Date and time of execution
- Result per step (M-1, M-2, M-3, DB-1, DB-2, DB-3): completed / halted / skipped
- Any stop rule triggered and the exact condition
- Final active D-folder count after execution
- Confirmation that ids 62 and 63 were not touched
- Explicit non-actions confirmation

The execution report is required before any further session work. It is not optional.

---

## 7. Explicit Non-Actions Confirmation

The following actions were NOT performed during the preparation of this write plan:

- No archive of any D-folder
- No routing of any file
- No update to any `deliverable_lifecycle` record
- No `team_tasks` update
- No move commands executed
- No dashboard work
- No new D-folder created
- No new folders created
- No DB writes of any kind
- No modification to any existing D-folder
- No edit to any SOP, GL, or CLAUDE.md
- No GL-013 resolution
- No Learning Candidate triage
- No Deliverable Lifecycle sweep
- id 62 and id 63 not touched

---

Delivered on: 2026-06-12
Delivered at: `Deliverables/20260612_Core_DL Control Inventory/20260612_batch-2-write-plan-v01.md`
