# Archive Write Plan — Deliverable Lifecycle IDs 2 and 3

**Date:** 2026-06-13
**Author:** Larry
**Session:** 2026-06-13 DL Control Recovery
**Type:** Write plan
**Scope:** Archive deliverable lifecycle IDs 2 and 3 only
**Status:** Awaiting execution authorization

---

## Scope

Two folders only:

| ID | Artifact Name | Current DB State | Archive Rationale |
|----|--------------|-----------------|------------------|
| 2 | 20260513_Geldstroom Regie_One-pager methodiek | pending_lifecycle_decision | Old GR domain knowledge deliverable. No governance reference. No open actions. |
| 3 | 20260519_Kamer E-commerce_Remy Research Week 21 | pending_lifecycle_decision | Old KE research brief. No governance reference. No open actions. |

Expected active D-folder count: 29 → 27 after execution.

---

## Pre-Execution Stop Checks

Before executing any write action, confirm all of the following. If any check fails: stop, report to Owner, do not proceed.

**SC-1:** Confirm both folders exist on disk at their expected paths:
- `/opt/myPKA/Deliverables/20260513_Geldstroom Regie_One-pager methodiek/`
- `/opt/myPKA/Deliverables/20260519_Kamer E-commerce_Remy Research Week 21/`

**SC-2:** Confirm Archive target directory exists:
- `/opt/myPKA/Deliverables/Archive/`

**SC-3:** Confirm neither folder already exists in Archive (no name collision):
- `/opt/myPKA/Deliverables/Archive/20260513_Geldstroom Regie_One-pager methodiek/` must not exist
- `/opt/myPKA/Deliverables/Archive/20260519_Kamer E-commerce_Remy Research Week 21/` must not exist

**SC-4:** Confirm DB records exist for both IDs with state `pending_lifecycle_decision`:
```sql
SELECT id, artifact_name, state_gl017 FROM deliverable_lifecycle WHERE id IN (2, 3);
```
Expected: 2 rows, both with `state_gl017 = 'pending_lifecycle_decision'`.

**SC-5:** Confirm no other write actions are pending or in-flight for this session that could interfere with the DB or folder structure.

No write-list batch-stop rules apply to this plan. There is no associated write-list.

---

## Write Actions

Execute in order. Stop and report if any action fails before proceeding to the next.

### W-1: Move folder — ID 2

```bash
mv "/opt/myPKA/Deliverables/20260513_Geldstroom Regie_One-pager methodiek" \
   "/opt/myPKA/Deliverables/Archive/20260513_Geldstroom Regie_One-pager methodiek"
```

### W-2: Move folder — ID 3

```bash
mv "/opt/myPKA/Deliverables/20260519_Kamer E-commerce_Remy Research Week 21" \
   "/opt/myPKA/Deliverables/Archive/20260519_Kamer E-commerce_Remy Research Week 21"
```

### W-3: DB update — ID 2

```python
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute(
    "UPDATE deliverable_lifecycle SET state_gl017 = 'archived', state_changed_at = datetime('now') WHERE id = 2"
)
conn.commit()
print(f"Rows updated: {cur.rowcount}")
conn.close()
```

Expected output: `Rows updated: 1`

### W-4: DB update — ID 3

```python
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute(
    "UPDATE deliverable_lifecycle SET state_gl017 = 'archived', state_changed_at = datetime('now') WHERE id = 3"
)
conn.commit()
print(f"Rows updated: {cur.rowcount}")
conn.close()
```

Expected output: `Rows updated: 1`

---

## Post-Execution Verification

After all four write actions complete, verify the following. Report each result.

**V-1:** Confirm folders are no longer present in active Deliverables:
```bash
ls "/opt/myPKA/Deliverables/" | grep -E "20260513|20260519"
```
Expected: no output (both folders moved out).

**V-2:** Confirm folders are present in Archive:
```bash
ls "/opt/myPKA/Deliverables/Archive/" | grep -E "20260513|20260519"
```
Expected: both folder names appear.

**V-3:** Confirm DB state for both IDs:
```sql
SELECT id, artifact_name, state_gl017, state_changed_at FROM deliverable_lifecycle WHERE id IN (2, 3);
```
Expected: both rows show `state_gl017 = 'archived'` and a non-null `state_changed_at`.

**V-4:** Confirm active D-folder count is now 27:
```sql
SELECT COUNT(*) FROM deliverable_lifecycle WHERE state_gl017 != 'archived';
```
Expected: 27.

**V-5:** Confirm disk folder count matches (excluding Archive, INDEX.md, README.md):
```bash
ls "/opt/myPKA/Deliverables/" | grep -v Archive | grep -v INDEX | grep -v README | wc -l
```
Expected: 27.

---

## Explicit Non-Actions

This write plan does not authorize and must not trigger:

- Any action on IDs other than 2 and 3
- Any action on the 11 Category D items
- Any action on IDs 18, 45, 19, 67, 13, or 46
- Any change to team_tasks 92 or 94
- Any GL, SOP, or CLAUDE.md edits
- Any Learning Candidate triage writes
- Any Deliverable Lifecycle sweep beyond IDs 2 and 3
- Any routing of folder contents to GR or KE knowledge bases
- Any new D-folder creation
- Any dashboard work
- Archiving the source deliverable (20260530_Core_UMC diagnose en aanbevelingen)
- Any other write action not listed in the Write Actions section above

---

## Execution Report

After execution: write a G2 execution report to:
`Deliverables/20260612_Core_DL Control Inventory/20260613_archive-execution-report-ids-2-3-v01.md`

The execution report must include: V-1 through V-5 results verbatim, final active count, and any deviations from this plan.

---

Delivered on: 2026-06-13
Delivered at: Deliverables/20260612_Core_DL Control Inventory/20260613_archive-write-plan-ids-2-3-v01.md
