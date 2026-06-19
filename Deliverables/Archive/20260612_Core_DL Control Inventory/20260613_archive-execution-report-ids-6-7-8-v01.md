# Archive Execution Report — Deliverable Lifecycle IDs 6, 7 and 8

**Date:** 2026-06-13
**Author:** Larry
**Session:** 2026-06-13 DL Control Recovery
**Type:** Execution report
**Write plan:** `20260613_archive-write-plan-ids-6-7-8-v02.md`
**Status:** Complete — no deviations

---

## Execution Summary

All three IDs archived successfully. Active D-folder count decreased from 27 to 24 as planned.

---

## Pre-Execution Stop Check Results

| Check | Result |
|-------|--------|
| SC-1: Source folders exist on disk | Pass |
| SC-2: Archive directory exists | Pass |
| SC-3: No name collisions in Archive | Pass |
| SC-4: DB records in `pending_lifecycle_decision` state | Pass |
| SC-5: No conflicting write actions in-flight | Pass |

---

## Write Action Results

| Action | Result |
|--------|--------|
| W-1: Move folder ID 6 to Archive | OK |
| W-2: Move folder ID 7 to Archive | OK |
| W-3: Move folder ID 8 to Archive | OK |
| W-4: DB update ID 6 — rows updated | 1 |
| W-5: DB update ID 7 — rows updated | 1 |
| W-6: DB update ID 8 — rows updated | 1 |

---

## Post-Execution Verification Results

**V-1:** Folders no longer present in active Deliverables
```
Not present — OK
Not present — OK
Not present — OK
```

**V-2:** Folders present in Archive
```
/opt/myPKA/Deliverables/Archive/20260530_Personal_Blueprint weekschema en oefeningen  Present — OK
/opt/myPKA/Deliverables/Archive/20260531_Personal_Health Monitoring Schema            Present — OK
/opt/myPKA/Deliverables/Archive/20260531_Personal_Morning Mobility Routine            Present — OK
```

**V-3:** DB state for IDs 6, 7 and 8
```
(6, '20260530_Personal_Blueprint weekschema en oefeningen', 'archived', '2026-06-13 14:54:06', 'archive')
(7, '20260531_Personal_Health Monitoring Schema', 'archived', '2026-06-13 14:54:06', 'archive')
(8, '20260531_Personal_Morning Mobility Routine', 'archived', '2026-06-13 14:54:06', 'archive')
```
All three rows: `state_gl017 = 'archived'`, `state_changed_at` set, `owner_decision = 'archive'`. ✓

**V-4:** Active D-folder count in DB
```
Active count: 24
```
Expected: 24 ✓

**V-5:** Active D-folder count on disk
```
24
```
Expected: 24 ✓

---

## Deviations

None.

---

## Final State

| Item | Before | After |
|------|--------|-------|
| Active D-folders (DB) | 27 | 24 |
| Active D-folders (disk) | 27 | 24 |
| ID 6 state_gl017 | pending_lifecycle_decision | archived |
| ID 7 state_gl017 | pending_lifecycle_decision | archived |
| ID 8 state_gl017 | pending_lifecycle_decision | archived |
| ID 6 owner_decision | NULL | archive |
| ID 7 owner_decision | NULL | archive |
| ID 8 owner_decision | NULL | archive |

---

Delivered on: 2026-06-13
Delivered at: Deliverables/20260612_Core_DL Control Inventory/20260613_archive-execution-report-ids-6-7-8-v01.md
