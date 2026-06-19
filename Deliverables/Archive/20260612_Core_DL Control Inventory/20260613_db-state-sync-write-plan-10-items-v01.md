# DB State Sync Write Plan — 10 Items v01

**Date:** 2026-06-13
**Status:** Awaiting Owner authorization
**Scope:** DB update only — `deliverable_lifecycle` table in `team-knowledge.db`
**Source:** `20260613_post-sync-health-check.md` — residual sync gap, session-scoped exclusions removed

---

## What this plan does

Sets `state='archived'` and `state_changed_at=datetime('now')` for 10 rows in
`deliverable_lifecycle` whose physical folders are confirmed IN_ARCHIVE (per post-sync
health check 2026-06-13) but whose DB `state` column was never updated after prior
physical archive actions.

Same pattern and same SQL guard as `20260613_db-state-sync-write-plan-28-items-v02.md`.

No folder moves. No archive execution. No routing. No new D-folder. No team_tasks
changes.

---

## Exclusions

- **ID 5** — standing source deliverable exclusion. Do not touch.
- **ID 72** — physical location unverified (NO_FOLDER). Excluded until confirmed.
- **ID 53** — `state_gl017=active`, separate open exception. Awaiting explicit Owner decision.
- **team_tasks 92 and 94** — unchanged per standing instruction.

---

## No associated write-list

No write-list exists for this sync plan. No write-list batch-stop rules apply.

---

## Batch-stop rules

1. Run the pre-flight SELECT. It must return exactly 10 rows. If fewer than 10 rows
   match, stop and report which IDs are missing before executing any UPDATE.
2. Execute the UPDATE as a single transaction. If the transaction fails for any reason,
   roll back and report before retrying.
3. Run the post-flight SELECT. It must return exactly 10 rows. If fewer than 10 rows
   are confirmed, stop and report which IDs were not updated.

---

## Target rows

Physical location for all 10 confirmed IN_ARCHIVE per `20260613_post-sync-health-check.md`.

| ID | artifact_name | state | state_gl017 | physical_location |
|----|--------------|-------|-------------|-------------------|
| 2  | 20260513_Geldstroom Regie_One-pager methodiek | ready | archived | IN_ARCHIVE |
| 3  | 20260519_Kamer E-commerce_Remy Research Week 21 | ready | archived | IN_ARCHIVE |
| 6  | 20260530_Personal_Blueprint weekschema en oefeningen | ready | archived | IN_ARCHIVE |
| 7  | 20260531_Personal_Health Monitoring Schema | ready | archived | IN_ARCHIVE |
| 8  | 20260531_Personal_Morning Mobility Routine | ready | archived | IN_ARCHIVE |
| 60 | 20260608_Core_UMC Archive Eligibility Analysis 20260530 | ready | archived | IN_ARCHIVE |
| 61 | 20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen | ready | archived | IN_ARCHIVE |
| 62 | 20260608_Core_Retention Assessment P2 P5 UMC | ready | archived | IN_ARCHIVE |
| 63 | 20260608_Core_Write Proposal GL-013 Additions P2 P5 | ready | archived | IN_ARCHIVE |
| 68 | 20260608_Core_Phase 1 Proposal R1 R5 v02 | ready | archived | IN_ARCHIVE |

---

## Exact SQL

```sql
-- Pre-flight: must return exactly 10 rows before proceeding
SELECT id, artifact_name, state, state_gl017
FROM deliverable_lifecycle
WHERE id IN (2,3,6,7,8,60,61,62,63,68)
  AND state != 'archived'
  AND state_gl017 = 'archived';

-- Update (execute only if pre-flight returns exactly 10 rows)
BEGIN;
UPDATE deliverable_lifecycle
SET state = 'archived',
    state_changed_at = datetime('now')
WHERE id IN (2,3,6,7,8,60,61,62,63,68)
  AND state != 'archived'
  AND state_gl017 = 'archived';
COMMIT;

-- Post-flight: must return exactly 10 rows
SELECT id, artifact_name, state, state_gl017, state_changed_at
FROM deliverable_lifecycle
WHERE id IN (2,3,6,7,8,60,61,62,63,68)
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
