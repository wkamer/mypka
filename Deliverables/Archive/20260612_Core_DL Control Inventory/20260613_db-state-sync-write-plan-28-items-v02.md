# DB State Sync Write Plan — 28 Items v02

**Date:** 2026-06-13
**Status:** Awaiting Owner authorization
**Supersedes:** `20260613_db-state-sync-write-plan-28-items.md` (v01)
**Scope:** DB update only — `deliverable_lifecycle` table in `team-knowledge.db`
**Source analysis:** `20260613_count-reconciliation-and-db-sync-analysis.md`

---

## What this plan does

Sets `state='archived'` and `state_changed_at=datetime('now')` for 28 rows in
`deliverable_lifecycle` whose physical folders are confirmed in `Deliverables/Archive/`
but whose DB `state` column was never updated after the physical archive action.

The WHERE clause and both verification queries include `AND state_gl017 = 'archived'`
as a hard guard. This ensures the sync only touches rows that the analysis established
as reliably classified for archive. Any row where `state_gl017` is not `'archived'`
is excluded from execution even if its ID appears in the list.

No folder moves. No archive execution. No routing. No new D-folder. No team_tasks
changes. No changes to IDs 53, 72, 92, or 94.

---

## Exclusions

- **ID 72** — physical location unverified. Excluded until confirmed.
- **ID 53** — Owner decision pending. Excluded until explicit instruction.
- **team_tasks 92 and 94** — unchanged per standing instruction.

---

## No associated write-list

No write-list exists for this sync plan. No write-list batch-stop rules apply.

---

## Batch-stop rules

1. Run the pre-flight SELECT. It must return exactly 28 rows. If fewer than 28 rows
   match, stop and report which IDs are missing before executing any UPDATE.
2. Execute the UPDATE as a single transaction. If the transaction fails for any reason,
   roll back and report before retrying.
3. Run the post-flight SELECT. It must return exactly 28 rows. If fewer than 28 rows
   are confirmed, stop and report which IDs were not updated.

---

## Target rows

| ID | artifact_name | Current state |
|----|--------------|---------------|
| 4  | 20260520_Core_Unified Memory Core architectuurschets | ready |
| 9  | 20260603_Core_B-021C Closure Record | ready |
| 17 | 20260606_Core_LC Lifecycle Phase 1 Write-List v05 | ready |
| 26 | 20260607_Core_LC Batch 1 Write-List | ready |
| 27 | 20260607_Core_LC Batch 1 Execution Report | ready |
| 28 | 20260607_Core_LC Batch 2 Write-List | ready |
| 29 | 20260607_Core_LC Batch 2 Execution Report | ready |
| 30 | 20260607_Core_LC Triage Write-Plan | ready |
| 31 | 20260607_Core_LC Naming Alignment Impact Assessment | ready |
| 32 | 20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion | ready |
| 33 | 20260607_Core_LC-5-6-7 Processed to Closed Assessment | ready |
| 34 | 20260607_Core_LC-9 Closure Report | ready |
| 35 | 20260607_Core_LCL Session Start Verification | ready |
| 37 | 20260607_Core_Post-SOP-019 Session Start Verification | ready |
| 38 | 20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4 | ready |
| 39 | 20260607_Core_SOP-019 LC-6 Execution Briefing Rule | ready |
| 43 | 20260607_Core_DL Smoke Test Recovery Report | ready |
| 44 | 20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal | ready |
| 47 | 20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal | ready |
| 48 | 20260608_Core_DL Hardening Task 85 Architecture Assessment | active |
| 49 | 20260608_Core_DLH Task 86 Naming Standard Reassessment | active |
| 51 | 20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal | superseded |
| 54 | 20260607_Core_Deliverable Lifecycle Hardening Phase B Triage | ready |
| 64 | 20260608_Core_UMC Archive Eligibility Chain Process Review | ready |
| 65 | 20260608_Core_R1-R5 Prioritization Assessment | ready |
| 66 | 20260608_Core_Phase 1 Proposal R1 R5 v01 | ready |
| 70 | 20260612_Core_DL Batch 1 Archive Execution Plan | ready |
| 71 | 20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal | ready |

---

## Exact SQL

```sql
-- Pre-flight: must return exactly 28 rows before proceeding
SELECT id, artifact_name, state, state_gl017
FROM deliverable_lifecycle
WHERE id IN (4,9,17,26,27,28,29,30,31,32,33,34,35,37,38,39,43,44,47,48,49,51,54,64,65,66,70,71)
  AND state != 'archived'
  AND state_gl017 = 'archived';

-- Update (execute only if pre-flight returns exactly 28 rows)
BEGIN;
UPDATE deliverable_lifecycle
SET state = 'archived',
    state_changed_at = datetime('now')
WHERE id IN (4,9,17,26,27,28,29,30,31,32,33,34,35,37,38,39,43,44,47,48,49,51,54,64,65,66,70,71)
  AND state != 'archived'
  AND state_gl017 = 'archived';
COMMIT;

-- Post-flight: must return exactly 28 rows
SELECT id, artifact_name, state, state_gl017, state_changed_at
FROM deliverable_lifecycle
WHERE id IN (4,9,17,26,27,28,29,30,31,32,33,34,35,37,38,39,43,44,47,48,49,51,54,64,65,66,70,71)
  AND state = 'archived'
  AND state_gl017 = 'archived';
```

---

## After execution

Produce an execution report as a file inside `20260612_Core_DL Control Inventory/`
with pre-flight count, post-flight count, full post-flight SELECT output, and any
deviations.

---

Delivered on: 2026-06-13
Delivered at: Deliverables/20260612_Core_DL Control Inventory/
