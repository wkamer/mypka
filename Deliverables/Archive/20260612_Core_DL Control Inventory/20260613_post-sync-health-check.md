# Post-Sync Health Check

**Date:** 2026-06-13
**Follows:** `20260613_db-state-sync-execution-report-28-items.md`
**Scope:** Read-only. No DB mutations, no folder moves, no routing, no new D-folder, no team_tasks changes.

---

## Physical active D-folder count

**24** — unchanged from pre-sync. Expected.

---

## DB count where `state != 'archived'`

**36** — down from 64 before the sync. Reduction of exactly 28. Matches the executed write plan.

---

## DB count by `state_gl017` (all rows)

| state_gl017 | All rows | Of which state != 'archived' |
|---|---|---|
| active | 8 | 8 |
| archived | 44 | 12 |
| pending_lifecycle_decision | 16 | 16 |
| **Total** | **68** | **36** |

---

## Reconciliation verdict

**Clean match.**

DB rows with `state_gl017` in (`active`, `pending_lifecycle_decision`) = 24.
Physical active D-folders = 24.
Zero discrepancy. Every active or pending-decision row has a corresponding folder on disk, and every physical folder has a corresponding DB row in those two states.

---

## Residual DB sync gap — 12 items

These 12 rows have `state != 'archived'` AND `state_gl017 = 'archived'`. All were deliberately excluded from the 28-item write plan. They are a bounded carry-forward, not a new gap introduced by this session.

| ID | artifact_name | state | state_gl017 | physical_location | excluded because |
|----|--------------|-------|-------------|-------------------|-----------------|
| 2 | 20260513_Geldstroom Regie_One-pager methodiek | ready | archived | IN_ARCHIVE | In session-scoped exclusion list — physically archived in session 210 |
| 3 | 20260519_Kamer E-commerce_Remy Research Week 21 | ready | archived | IN_ARCHIVE | In session-scoped exclusion list — physically archived in session 210 |
| 5 | 20260530_Core_UMC diagnose en aanbevelingen | ready | archived | IN_ARCHIVE | Standing exclusion: source deliverable — do not touch |
| 6 | 20260530_Personal_Blueprint weekschema en oefeningen | ready | archived | IN_ARCHIVE | In session-scoped exclusion list — physically archived in session 210 |
| 7 | 20260531_Personal_Health Monitoring Schema | ready | archived | IN_ARCHIVE | In session-scoped exclusion list — physically archived in session 210 |
| 8 | 20260531_Personal_Morning Mobility Routine | ready | archived | IN_ARCHIVE | In session-scoped exclusion list — physically archived in session 210 |
| 60 | 20260608_Core_UMC Archive Eligibility Analysis 20260530 | ready | archived | IN_ARCHIVE | In session-scoped exclusion list — physically archived in an earlier session |
| 61 | 20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen | ready | archived | IN_ARCHIVE | In session-scoped exclusion list — physically archived in an earlier session |
| 62 | 20260608_Core_Retention Assessment P2 P5 UMC | ready | archived | IN_ARCHIVE | In session-scoped exclusion list — physically archived in an earlier session |
| 63 | 20260608_Core_Write Proposal GL-013 Additions P2 P5 | ready | archived | IN_ARCHIVE | In session-scoped exclusion list — physically archived in an earlier session |
| 68 | 20260608_Core_Phase 1 Proposal R1 R5 v02 | ready | archived | IN_ARCHIVE | In session-scoped exclusion list — physically archived in an earlier session |
| 72 | 20260612_Core_DL Batch 2 Process Artifacts Archive Proposal | ready | archived | NO_FOLDER | Explicitly excluded: physical location unverified — not found in active Deliverables or Archive |

IDs 2, 3, 5, 6, 7, 8, 60, 61, 62, 63, 68 are all physically IN_ARCHIVE. Their DB sync gap is the same pattern as the 28 items just resolved — physical action was done in a prior session but DB `state` was never updated. ID 72 is the exception: NO_FOLDER, location unknown.

---

## Open exceptions

**ID 53 — 20260608_Core_DL Granularity Assessment**
- `state=active`, `state_gl017=active`, physical location: ACTIVE_FOLDER
- `owner_decision`: Owner approved v02 for implementation 2026-06-08
- Notes confirm implementation complete, but DB state and state_gl017 remain `active`
- No action taken. Awaiting explicit Owner decision before any change.

**ID 72 — 20260612_Core_DL Batch 2 Process Artifacts Archive Proposal**
- `state=ready`, `state_gl017=archived`, physical location: NO_FOLDER
- `owner_decision` records misclassification: G2 artifact, file moved to DL Control Inventory folder
- Not found in active Deliverables or in Archive
- No action taken. Physical file location inside `20260612_Core_DL Control Inventory/` must be verified before any DB update.

---

## Scope confirmation

- DB mutations: none
- Folder moves: none
- Routing: none
- New D-folder: none
- team_tasks changes: none

---

Delivered on: 2026-06-13
Delivered at: Deliverables/20260612_Core_DL Control Inventory/
