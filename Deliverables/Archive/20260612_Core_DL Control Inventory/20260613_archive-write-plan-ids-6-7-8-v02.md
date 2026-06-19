# Archive Write Plan — Deliverable Lifecycle IDs 6, 7 and 8

**Date:** 2026-06-13
**Author:** Larry
**Session:** 2026-06-13 DL Control Recovery
**Type:** Write plan
**Scope:** Archive deliverable lifecycle IDs 6, 7 and 8 only
**Status:** Awaiting execution authorization
**Supersedes:** `20260613_archive-write-plan-ids-6-7-8-v01.md`
**Correction v02:** V-1 and V-2 updated to use exact folder name checks. Broad date grep removed to avoid false match on `20260530_Core_UMC diagnose en aanbevelingen`.

---

## Scope

Three folders only:

| ID | Artifact Name | Current DB State | Archive Rationale |
|----|--------------|-----------------|------------------|
| 6 | 20260530_Personal_Blueprint weekschema en oefeningen | pending_lifecycle_decision | Content already routed/copied to PKM Personal. No additional routing needed. Owner decision: archive. |
| 7 | 20260531_Personal_Health Monitoring Schema | pending_lifecycle_decision | Content already routed/copied to PKM Personal. No additional routing needed. Owner decision: archive. |
| 8 | 20260531_Personal_Morning Mobility Routine | pending_lifecycle_decision | Content already routed/copied to PKM Personal. No additional routing needed. Owner decision: archive. |

Expected active D-folder count: 27 → 24 after execution.

---

## Pre-Execution Stop Checks

Before executing any write action, confirm all of the following. If any check fails: stop, report to Owner, do not proceed.

**SC-1:** Confirm all three folders exist on disk at their expected paths:
- `/opt/myPKA/Deliverables/20260530_Personal_Blueprint weekschema en oefeningen/`
- `/opt/myPKA/Deliverables/20260531_Personal_Health Monitoring Schema/`
- `/opt/myPKA/Deliverables/20260531_Personal_Morning Mobility Routine/`

**SC-2:** Confirm Archive target directory exists:
- `/opt/myPKA/Deliverables/Archive/`

**SC-3:** Confirm none of the three folders already exist in Archive (no name collision):
- `/opt/myPKA/Deliverables/Archive/20260530_Personal_Blueprint weekschema en oefeningen/` must not exist
- `/opt/myPKA/Deliverables/Archive/20260531_Personal_Health Monitoring Schema/` must not exist
- `/opt/myPKA/Deliverables/Archive/20260531_Personal_Morning Mobility Routine/` must not exist

**SC-4:** Confirm DB records exist for all three IDs with state `pending_lifecycle_decision`:
```sql
SELECT id, artifact_name, state_gl017 FROM deliverable_lifecycle WHERE id IN (6, 7, 8);
```
Expected: 3 rows, all with `state_gl017 = 'pending_lifecycle_decision'`.

**SC-5:** Confirm no other write actions are pending or in-flight for this session that could interfere with the DB or folder structure.

No write-list batch-stop rules apply to this plan. There is no associated write-list.

---

## Write Actions

Execute in order. Stop and report if any action fails before proceeding to the next.

### W-1: Move folder — ID 6

```bash
mv "/opt/myPKA/Deliverables/20260530_Personal_Blueprint weekschema en oefeningen" \
   "/opt/myPKA/Deliverables/Archive/20260530_Personal_Blueprint weekschema en oefeningen"
```

### W-2: Move folder — ID 7

```bash
mv "/opt/myPKA/Deliverables/20260531_Personal_Health Monitoring Schema" \
   "/opt/myPKA/Deliverables/Archive/20260531_Personal_Health Monitoring Schema"
```

### W-3: Move folder — ID 8

```bash
mv "/opt/myPKA/Deliverables/20260531_Personal_Morning Mobility Routine" \
   "/opt/myPKA/Deliverables/Archive/20260531_Personal_Morning Mobility Routine"
```

### W-4: DB update — ID 6

```python
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute(
    "UPDATE deliverable_lifecycle SET state_gl017 = 'archived', state_changed_at = datetime('now'), owner_decision = 'archive' WHERE id = 6"
)
conn.commit()
print(f"Rows updated: {cur.rowcount}")
conn.close()
```

Expected output: `Rows updated: 1`

### W-5: DB update — ID 7

```python
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute(
    "UPDATE deliverable_lifecycle SET state_gl017 = 'archived', state_changed_at = datetime('now'), owner_decision = 'archive' WHERE id = 7"
)
conn.commit()
print(f"Rows updated: {cur.rowcount}")
conn.close()
```

Expected output: `Rows updated: 1`

### W-6: DB update — ID 8

```python
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute(
    "UPDATE deliverable_lifecycle SET state_gl017 = 'archived', state_changed_at = datetime('now'), owner_decision = 'archive' WHERE id = 8"
)
conn.commit()
print(f"Rows updated: {cur.rowcount}")
conn.close()
```

Expected output: `Rows updated: 1`

---

## Post-Execution Verification

After all six write actions complete, verify the following. Report each result.

**V-1:** Confirm each of the three folders is no longer present in active Deliverables:
```bash
ls -d "/opt/myPKA/Deliverables/20260530_Personal_Blueprint weekschema en oefeningen" 2>/dev/null && echo "FAIL: still present" || echo "Not present — OK"
ls -d "/opt/myPKA/Deliverables/20260531_Personal_Health Monitoring Schema" 2>/dev/null && echo "FAIL: still present" || echo "Not present — OK"
ls -d "/opt/myPKA/Deliverables/20260531_Personal_Morning Mobility Routine" 2>/dev/null && echo "FAIL: still present" || echo "Not present — OK"
```
Expected: all three return `Not present — OK`.

**V-2:** Confirm each of the three folders is present in Archive:
```bash
ls -d "/opt/myPKA/Deliverables/Archive/20260530_Personal_Blueprint weekschema en oefeningen" 2>/dev/null && echo "Present — OK" || echo "FAIL: not found"
ls -d "/opt/myPKA/Deliverables/Archive/20260531_Personal_Health Monitoring Schema" 2>/dev/null && echo "Present — OK" || echo "FAIL: not found"
ls -d "/opt/myPKA/Deliverables/Archive/20260531_Personal_Morning Mobility Routine" 2>/dev/null && echo "Present — OK" || echo "FAIL: not found"
```
Expected: all three return `Present — OK`.

**V-3:** Confirm DB state for IDs 6, 7 and 8:
```sql
SELECT id, artifact_name, state_gl017, state_changed_at, owner_decision FROM deliverable_lifecycle WHERE id IN (6, 7, 8);
```
Expected: all three rows show `state_gl017 = 'archived'`, non-null `state_changed_at`, and `owner_decision = 'archive'`.

**V-4:** Confirm active D-folder count is now 24:
```sql
SELECT COUNT(*) FROM deliverable_lifecycle WHERE state_gl017 != 'archived';
```
Expected: 24.

**V-5:** Confirm disk folder count matches (excluding Archive, INDEX.md, README.md):
```bash
ls "/opt/myPKA/Deliverables/" | grep -v Archive | grep -v INDEX | grep -v README | wc -l
```
Expected: 24.

---

## Explicit Non-Actions

This write plan does not authorize and must not trigger:

- Any action on IDs other than 6, 7 and 8
- Any action on the 11 Category D items
- Any action on IDs 13, 18, 19, 45, 46, 67
- Any change to team_tasks 92 or 94
- Any routing of folder contents to PKM Personal, Lena, or Sienna
- Any GL, SOP, or CLAUDE.md edits
- Any Learning Candidate triage writes
- Any Deliverable Lifecycle sweep beyond IDs 6, 7 and 8
- Any new D-folder creation
- Any dashboard work
- Archiving the source deliverable (20260530_Core_UMC diagnose en aanbevelingen)
- Any other write action not listed in the Write Actions section above

---

## Execution Report

After execution: write a G2 execution report to:
`Deliverables/20260612_Core_DL Control Inventory/20260613_archive-execution-report-ids-6-7-8-v01.md`

The execution report must include: V-1 through V-5 results verbatim, final active count, and any deviations from this plan.

---

Delivered on: 2026-06-13
Delivered at: Deliverables/20260612_Core_DL Control Inventory/20260613_archive-write-plan-ids-6-7-8-v02.md
