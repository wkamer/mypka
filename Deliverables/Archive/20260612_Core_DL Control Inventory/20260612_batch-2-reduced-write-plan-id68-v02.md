# Batch 2 Reduced Write Plan — id 68 Only — v02

**Date:** 2026-06-12
**Author:** Governance Assistant
**Status:** Awaiting Owner authorization before any execution
**Supersedes:** `20260612_batch-2-reduced-write-plan-id68-v01.md` for Owner review and execution.
v01 is preserved unchanged as a historical artifact. v01 contained an overly broad SC-2
that would have halted on closed historical GL-013 references in id 68. v02 corrects SC-2.
**Task reference:** team_task 94
**Placement:** G2 — file inside `20260612_Core_DL Control Inventory/`
**Scope basis:** `20260612_batch-2-scope-proposal-v01.md` (Owner approved 2026-06-12),
reduced to id 68 only by Owner decision 2026-06-12 following halt report
`20260612_batch-2-archive-execution-report-v01.md`.
**Operating model reference:** `20260612_d-folder-operating-model-proposal-v02.md`

---

No execution is authorized by this document.
Execution begins only after Owner explicitly authorizes this reduced write plan.

---

## 1. Reduced Batch 2 Scope

| Lifecycle id | Folder |
|---|---|
| 68 | `20260608_Core_Phase 1 Proposal R1 R5 v02` |

**Batch size: 1**

**Pre-execution inspection status:** id 68 passed inspection in the halted execution
report (`20260612_batch-2-archive-execution-report-v01.md`, Section 1, id 68 result:
PASS). No open items, no pending routing actions, and no active governance signals were
found.

**Known closed GL-013 references in id 68:** `proposal.md` contains references to GL-013
in the context of W-3, a write action that was rejected by the Owner. The document states:
"Owner rejected W-3 and confirmed no further GL-013 action is required." These references
are closed historical records. They do not constitute an open governance signal and do
not trigger SC-2.

A confirmatory check is still required at execution time (see Section 5, SC-1 and SC-2).

---

## 2. Explicit Exclusions

The following folders are explicitly excluded and must not be touched:

| Lifecycle id | Folder | Reason |
|---|---|---|
| 60 | `20260608_Core_UMC Archive Eligibility Analysis 20260530` | Halted — pending routing actions and GL-013 update; Owner decision required |
| 61 | `20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen` | Halted — unresolved architectural gap, open deliverable registration, GL-013 pending; Owner decision required |
| 62 | `20260608_Core_Retention Assessment P2 P5 UMC` | Frozen — GL-013 open signal |
| 63 | `20260608_Core_Write Proposal GL-013 Additions P2 P5` | Conditional — pending GL-013 confirmation |

All Category A, C, and D folders are also excluded and must not be touched.

---

## 3. Exact Move Action

Archive destination: `Deliverables/Archive/`

| Step | Action | Command |
|---|---|---|
| M-1 | Move id 68 | `mv "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v02" "/opt/myPKA/Deliverables/Archive/"` |

**Pre-condition check before M-1:** confirm the source folder exists on the filesystem.
If missing: halt before executing any move. Report to Owner.

---

## 4. Exact DB Update Action

Database: `/opt/myPKA/Team Knowledge/team-knowledge.db`
Table: `deliverable_lifecycle`

Execute only after M-1 succeeds.

| Step | After move | SQL |
|---|---|---|
| DB-1 | After M-1 | `UPDATE deliverable_lifecycle SET state_gl017 = 'archived', owner_decision = 'Archived in Batch 2 (reduced, id 68 only) — 2026-06-12. Scope approved by Owner.' WHERE id = 68;` |

**Verification after DB-1:** confirm `SELECT state_gl017 FROM deliverable_lifecycle WHERE id = 68` returns `'archived'` before closing execution.

---

## 5. Stop Rules

Halt immediately — before any further action — if any of the following conditions are met:

| Rule | Condition | Action |
|---|---|---|
| SC-1 | Any open item, unresolved decision, or indication that the chain is not closed is found in id 68 folder content at execution time | Halt. Report exact finding to Owner. Do not proceed. |
| SC-2 | Any **open, unresolved, pending, or active** GL-013 signal or other open governance signal is found in id 68 folder content at execution time. **Note:** closed historical GL-013 references where Owner rejected W-3 and confirmed no further GL-013 action is required do not trigger this rule. | Halt. Report exact finding to Owner. Do not proceed. |
| SC-3 | Source folder for id 68 is missing from the filesystem | Halt. Report to Owner. Do not proceed. |
| SC-4 | `mv` command returns a non-zero exit code | Halt. Do not execute DB update. Report to Owner. |
| SC-5 | DB UPDATE fails or returns rowcount != 1 | Halt. Report anomaly to Owner. |
| SC-6 | Verification SELECT returns a value other than `'archived'` | Halt. Report to Owner. |
| SC-7 | id 68 folder is found to be referenced by a live SOP, GL, or CLAUDE.md at execution time | Halt. Report to Owner. |
| SC-8 | ids 60, 61, 62, or 63 are encountered during any step | Halt. Do not touch. Report to Owner. |

---

## 6. Execution Report Requirement

Immediately after execution completes (or halts), Larry writes an execution report.

**File location:** G2 — file inside `Deliverables/20260612_Core_DL Control Inventory/`
**Filename:** `20260612_batch-2-reduced-execution-report-id68-v01.md`

The execution report must include:
- Date and time of execution
- Pre-execution check result for id 68 (folder present / missing)
- Result of M-1: completed / halted
- Result of DB-1: completed / halted / skipped
- Verification SELECT result
- Any stop rule triggered and the exact condition
- Final active D-folder count after execution
- Confirmation that ids 60, 61, 62, and 63 were not touched
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
- No modification to write plan v01
- No GL-013 resolution
- No Learning Candidate triage
- No Deliverable Lifecycle sweep
- ids 60, 61, 62, and 63 not touched

---

Delivered on: 2026-06-12
Delivered at: `Deliverables/20260612_Core_DL Control Inventory/20260612_batch-2-reduced-write-plan-id68-v02.md`
