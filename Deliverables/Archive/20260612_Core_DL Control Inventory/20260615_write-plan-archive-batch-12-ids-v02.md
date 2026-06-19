# Write Plan v02 — Archive Batch 12 IDs (DL Control Cleanup)

**Date:** 2026-06-15
**Prepared by:** Larry, Team Orchestrator
**Supersedes:** `20260615_write-plan-archive-batch-12-ids-v01.md`
**Status:** Awaiting Owner authorization for execution
**Revision note v01 → v02:** Execution order changed to DB-first with explicit preflight and mismatch recovery instructions.

---

## 1. Items in Scope

| ID | Folder name | Expected state_gl017 | Expected owner_decision |
|----|---|---|---|
| 10 | 20260604_Core_Architecture Triage Memory Domain Routing | pending_lifecycle_decision | deferred |
| 11 | 20260604_Core_Deliverable Lifecycle Knowledge Processing Triage | pending_lifecycle_decision | deferred |
| 13 | 20260604_Core_Review Gate Protocol Triage | pending_lifecycle_decision | deferred |
| 16 | 20260605_Core_SOP-017 Amendment Lifecycle Execution | pending_lifecycle_decision | deferred |
| 36 | 20260607_Core_Learning Candidate Flag Triage Proposal | pending_lifecycle_decision | deferred |
| 40 | 20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards | pending_lifecycle_decision | deferred |
| 41 | 20260607_Core_Final Governance State Verification | pending_lifecycle_decision | deferred |
| 42 | 20260607_Core_DL Phase 1 Retroactive Iris Review | pending_lifecycle_decision | deferred |
| 55 | 20260608_Core_DL Hardening Phase C Proposal v01 | pending_lifecycle_decision | deferred |
| 56 | 20260608_Core_DL Post-Granularity Usability Assessment | pending_lifecycle_decision | deferred |
| 57 | 20260608_Core_DL Usability Assessment Owner Perspective | pending_lifecycle_decision | deferred |
| 59 | 20260608_Core_DL Pending Decision Inventory | active | deferred |

---

## 2. Explicitly Excluded

IDs 12, 18, 19, 45, 46, 50, 52, 58, 67, 69 — not touched.
ID 5 — not touched.
Category D / Registered but Unclear items — not touched.
team_tasks 92 and 94 — not touched.
Source deliverable `20260530_Core_UMC diagnose en aanbevelingen` — not touched.

---

## 3. Target Location

All folders move to: `Deliverables/Archive/`

Archive is not deletion. Folders remain available at the Archive path.

---

## 4. Execution Order

**DB first. Folder moves only after successful DB commit.**

```
Preflight → DB transaction → Commit → Folder moves
                ↓ fail                    ↓ partial fail
            Stop, report             Stop, report partial state + recovery
```

---

## 5. Step 0 — Preflight (stop on any failure before proceeding)

Run all three checks. If any check fails: stop immediately, do not proceed to Step 1.

**Check 0A — All 12 source folders exist:**

```bash
for f in \
  "20260604_Core_Architecture Triage Memory Domain Routing" \
  "20260604_Core_Deliverable Lifecycle Knowledge Processing Triage" \
  "20260604_Core_Review Gate Protocol Triage" \
  "20260605_Core_SOP-017 Amendment Lifecycle Execution" \
  "20260607_Core_Learning Candidate Flag Triage Proposal" \
  "20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards" \
  "20260607_Core_Final Governance State Verification" \
  "20260607_Core_DL Phase 1 Retroactive Iris Review" \
  "20260608_Core_DL Hardening Phase C Proposal v01" \
  "20260608_Core_DL Post-Granularity Usability Assessment" \
  "20260608_Core_DL Usability Assessment Owner Perspective" \
  "20260608_Core_DL Pending Decision Inventory"; do
  [ -d "Deliverables/$f" ] && echo "OK: $f" || echo "MISSING: $f"
done
```

Expected: all 12 lines print `OK`.

**Check 0B — No destination collision (none of the 12 already exist in Archive):**

```bash
for f in \
  "20260604_Core_Architecture Triage Memory Domain Routing" \
  "20260604_Core_Deliverable Lifecycle Knowledge Processing Triage" \
  "20260604_Core_Review Gate Protocol Triage" \
  "20260605_Core_SOP-017 Amendment Lifecycle Execution" \
  "20260607_Core_Learning Candidate Flag Triage Proposal" \
  "20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards" \
  "20260607_Core_Final Governance State Verification" \
  "20260607_Core_DL Phase 1 Retroactive Iris Review" \
  "20260608_Core_DL Hardening Phase C Proposal v01" \
  "20260608_Core_DL Post-Granularity Usability Assessment" \
  "20260608_Core_DL Usability Assessment Owner Perspective" \
  "20260608_Core_DL Pending Decision Inventory"; do
  [ -d "Deliverables/Archive/$f" ] && echo "COLLISION: $f" || echo "CLEAR: $f"
done
```

Expected: all 12 lines print `CLEAR`.

**Check 0C — All 12 DB rows are in expected state:**

```sql
SELECT id, state_gl017, owner_decision
FROM deliverable_lifecycle
WHERE id IN (10, 11, 13, 16, 36, 40, 41, 42, 55, 56, 57, 59)
ORDER BY id;
```

Expected: 12 rows returned. IDs 10–42, 55–57: `state_gl017 = 'pending_lifecycle_decision'`. ID 59: `state_gl017 = 'active'`. All 12: `owner_decision = 'deferred'`. If rowcount != 12 or any value differs: stop, report to Owner.

---

## 6. Step 1 — DB Transaction (only after Preflight passes)

```python
import sqlite3
conn = sqlite3.connect('Team Knowledge/team-knowledge.db')
conn.isolation_level = None  # manual transaction control
cur = conn.cursor()

cur.execute('BEGIN')
cur.execute("""
    UPDATE deliverable_lifecycle
    SET state_gl017 = 'archived',
        owner_decision = 'archived_cleanup_no_active_need'
    WHERE id IN (10, 11, 13, 16, 36, 40, 41, 42, 55, 56, 57, 59)
""")
rowcount = cur.rowcount
print(f'Rows affected: {rowcount}')

if rowcount != 12:
    cur.execute('ROLLBACK')
    print('ROLLBACK: rowcount != 12. No changes written. Stop.')
else:
    # Post-check before commit
    cur.execute("""
        SELECT id, state_gl017, owner_decision
        FROM deliverable_lifecycle
        WHERE id IN (10, 11, 13, 16, 36, 40, 41, 42, 55, 56, 57, 59)
        ORDER BY id
    """)
    rows = cur.fetchall()
    errors = [r for r in rows if r[1] != 'archived' or r[2] != 'archived_cleanup_no_active_need']
    if errors:
        cur.execute('ROLLBACK')
        print(f'ROLLBACK: post-check failed for rows: {errors}. Stop.')
    else:
        cur.execute('COMMIT')
        print('COMMIT OK. All 12 rows verified before commit.')
        for r in rows:
            print(r)

conn.close()
```

**Batch-stop rule:** If ROLLBACK occurs for any reason: stop. Do not proceed to folder moves. Report to Owner.

---

## 7. Step 2 — Folder Moves (only after Step 1 COMMIT OK)

Execute each mv sequentially. After each move, verify source is gone and destination exists before continuing to the next.

```bash
mv "Deliverables/20260604_Core_Architecture Triage Memory Domain Routing" "Deliverables/Archive/"
mv "Deliverables/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage" "Deliverables/Archive/"
mv "Deliverables/20260604_Core_Review Gate Protocol Triage" "Deliverables/Archive/"
mv "Deliverables/20260605_Core_SOP-017 Amendment Lifecycle Execution" "Deliverables/Archive/"
mv "Deliverables/20260607_Core_Learning Candidate Flag Triage Proposal" "Deliverables/Archive/"
mv "Deliverables/20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards" "Deliverables/Archive/"
mv "Deliverables/20260607_Core_Final Governance State Verification" "Deliverables/Archive/"
mv "Deliverables/20260607_Core_DL Phase 1 Retroactive Iris Review" "Deliverables/Archive/"
mv "Deliverables/20260608_Core_DL Hardening Phase C Proposal v01" "Deliverables/Archive/"
mv "Deliverables/20260608_Core_DL Post-Granularity Usability Assessment" "Deliverables/Archive/"
mv "Deliverables/20260608_Core_DL Usability Assessment Owner Perspective" "Deliverables/Archive/"
mv "Deliverables/20260608_Core_DL Pending Decision Inventory" "Deliverables/Archive/"
```

If any move fails: stop immediately. Do not attempt remaining moves. Proceed to Section 8 (Mismatch Recovery).

---

## 8. Mismatch Recovery (folder move failure after DB commit)

If Step 1 committed successfully but one or more moves in Step 2 failed:

**State at failure point:**
- DB: all 12 rows show `state_gl017 = 'archived'`
- Filesystem: N folders moved, (12 - N) folders still at source

**Report to Owner:**
- Which folders were successfully moved (present in Archive)
- Which folders failed to move (still present at source)
- Exact error message from the failed mv

**Recovery options (Owner chooses):**
- Option A (complete forward): manually move the remaining folders or re-run only the failed mv commands. DB state is already correct.
- Option B (revert DB for failed items): issue a targeted UPDATE to restore `state_gl017` and `owner_decision` for the specific IDs whose folders were not moved, so DB and filesystem match again. New write plan required for Option B.

Do not auto-select a recovery path. Report and wait for Owner instruction.

---

## 9. Post-Execution Verification (after all 12 moves succeed)

**9A — Folder check:**

```bash
for f in \
  "20260604_Core_Architecture Triage Memory Domain Routing" \
  "20260604_Core_Deliverable Lifecycle Knowledge Processing Triage" \
  "20260604_Core_Review Gate Protocol Triage" \
  "20260605_Core_SOP-017 Amendment Lifecycle Execution" \
  "20260607_Core_Learning Candidate Flag Triage Proposal" \
  "20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards" \
  "20260607_Core_Final Governance State Verification" \
  "20260607_Core_DL Phase 1 Retroactive Iris Review" \
  "20260608_Core_DL Hardening Phase C Proposal v01" \
  "20260608_Core_DL Post-Granularity Usability Assessment" \
  "20260608_Core_DL Usability Assessment Owner Perspective" \
  "20260608_Core_DL Pending Decision Inventory"; do
  [ -d "Deliverables/Archive/$f" ] && echo "IN ARCHIVE: $f" || echo "MISSING FROM ARCHIVE: $f"
  [ -d "Deliverables/$f" ] && echo "STILL AT SOURCE (ERROR): $f"
done
```

Expected: all 12 print `IN ARCHIVE`, none print `STILL AT SOURCE`.

**9B — DB check:**

```sql
SELECT id, state_gl017, owner_decision
FROM deliverable_lifecycle
WHERE id IN (10, 11, 13, 16, 36, 40, 41, 42, 55, 56, 57, 59)
ORDER BY id;
```

Expected: all 12 rows show `state_gl017 = 'archived'`, `owner_decision = 'archived_cleanup_no_active_need'`.

---

## 10. Out of Scope

- No content edits to any file inside any folder
- No borging writes
- No routing
- No Learning Candidate writes
- No Deliverable Lifecycle sweep
- No GL/SOP/CLAUDE.md edits
- No dashboard work
- No new D-folder

---

## 11. Execution Authorization

Owner must explicitly authorize execution before preflight begins.
This write plan does not constitute authorization.

---

*Delivered on: 2026-06-15*
*Delivered at: Deliverables/20260612_Core_DL Control Inventory/20260615_write-plan-archive-batch-12-ids-v02.md*
