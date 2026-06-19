# Pilot A Archive Execution Write Plan — v01

**Date:** 2026-06-12
**Prepared by:** Larry, Team Orchestrator
**Type:** Execution write plan — persisted for audit trail and Owner review
**Placement:** G2 — file inside `20260612_Core_DL Control Inventory/`
**Status:** Awaiting Owner authorization. No execution performed.

**Revision note:** This file persists the Pilot A execution write plan that was previously
returned in chat only. It exists to repair the audit-trail and review-context gap before
Owner authorization.

**Amendment note (2026-06-12):** Three execution safety details corrected per Owner instruction:
(1) archive target collision preflight added as Section 2.6;
(2) DB update replaced with per-id transaction that rolls back on any rowcount error (Section 4.1);
(3) commit only executes if all 5 per-id updates return exactly 1 row.

**Read-only declaration:** No archive, no lifecycle updates, no routing, no sweep, no Batch 2,
no Learning Candidate triage, no dashboard work, no folder creation was performed during
the preparation of this file.

---

## 1. Approved Pilot A Folders

| # | Folder | Lifecycle id | Current DB state |
|---|---|---|---|
| 1 | `20260612_Core_DL Batch 1 Archive Execution Plan` | 70 | active |
| 2 | `20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal` | 71 | active |
| 3 | `20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal` | 44 | pending_lifecycle_decision |
| 4 | `20260607_Core_DL Smoke Test Recovery Report` | 43 | pending_lifecycle_decision |
| 5 | `20260607_Core_Deliverable Lifecycle Hardening Phase B Triage` | 54 | pending_lifecycle_decision |

Authorized batch size: 5. No additional folders may be added without a new Owner decision.

---

## 2. Preflight Checks

Run all checks before any archive action. Halt if any check fails.

### 2.1 Filesystem — Folders Exist in Active Deliverables

```bash
for f in \
  '20260612_Core_DL Batch 1 Archive Execution Plan' \
  '20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal' \
  '20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal' \
  '20260607_Core_DL Smoke Test Recovery Report' \
  '20260607_Core_Deliverable Lifecycle Hardening Phase B Triage'; do
  [ -d "/opt/myPKA/Deliverables/$f" ] \
    && echo "EXISTS: $f" \
    || echo "MISSING — HALT: $f"
done
```

Expected: 5 × `EXISTS`. Any `MISSING` = halt before any mv.

Pre-execution result (confirmed 2026-06-12): all 5 EXIST.

### 2.2 Filesystem — Archive Target is Writable

```bash
[ -w /opt/myPKA/Deliverables/Archive/ ] && echo "WRITABLE" || echo "NOT WRITABLE — HALT"
```

Expected: `WRITABLE`.

Pre-execution result (confirmed 2026-06-12): WRITABLE.

### 2.3 Lifecycle Records — All 5 Present

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
cur = conn.cursor()
cur.execute(
    "SELECT id, artifact_name, state_gl017, owner_decision "
    "FROM deliverable_lifecycle WHERE id IN (70, 71, 44, 43, 54) ORDER BY id"
)
for row in cur.fetchall():
    print(row)
```

Expected: 5 rows returned. If any id is missing = halt.

Pre-execution result (confirmed 2026-06-12):

| id | artifact_name | state_gl017 | owner_decision |
|---|---|---|---|
| 43 | 20260607_Core_DL Smoke Test Recovery Report | pending_lifecycle_decision | null |
| 44 | 20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal | pending_lifecycle_decision | null |
| 54 | 20260607_Core_Deliverable Lifecycle Hardening Phase B Triage | pending_lifecycle_decision | null |
| 70 | 20260612_Core_DL Batch 1 Archive Execution Plan | active | null |
| 71 | 20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal | active | GL-017 correction pending: G2 candidate for Control Inventory, not standalone |

### 2.4 Live References — No SOP, GL, or CLAUDE.md References Any of the 5 Folders

```bash
grep -rl \
  '20260612_Core_DL Batch 1 Archive Execution Plan\|20260612_Core_DL Post-Batch-1\|20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test\|20260607_Core_DL Smoke Test Recovery\|20260607_Core_Deliverable Lifecycle Hardening Phase B' \
  /opt/myPKA/Team\ Knowledge/Core/Guidelines/ \
  /opt/myPKA/Team\ Knowledge/Core/SOPs/ \
  /opt/myPKA/CLAUDE.md 2>/dev/null \
  || echo "NO LIVE REFERENCES FOUND"
```

Expected: `NO LIVE REFERENCES FOUND`. Any match = halt and inspect before proceeding.

Pre-execution result (confirmed 2026-06-12): NO LIVE REFERENCES FOUND.

### 2.5 Open Team Tasks — None Reference Any of the 5 Folders

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
cur = conn.cursor()
terms = [
    'Batch 1 Archive Execution Plan',
    'Post-Batch-1',
    'Smoke Test Proposal',
    'Smoke Test Recovery',
    'Hardening Phase B'
]
for t in terms:
    cur.execute(
        "SELECT id, title, status FROM team_tasks "
        "WHERE title LIKE ? AND status != 'completed'",
        ('%' + t + '%',)
    )
    rows = cur.fetchall()
    if rows:
        for r in rows:
            print('OPEN TASK — HALT:', r)
    else:
        print('CLEAR:', t)
```

Expected: 5 × `CLEAR`. Any `OPEN TASK` = halt and resolve before proceeding.

Pre-execution result (confirmed 2026-06-12): all 5 CLEAR.

### 2.6 Archive Target Collision — No Target Already Exists in Archive

For each of the 5 approved folders, verify the corresponding target does NOT already exist
in `Deliverables/Archive/`. A pre-existing target would cause `mv` to merge or overwrite.

```bash
for f in \
  '20260612_Core_DL Batch 1 Archive Execution Plan' \
  '20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal' \
  '20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal' \
  '20260607_Core_DL Smoke Test Recovery Report' \
  '20260607_Core_Deliverable Lifecycle Hardening Phase B Triage'; do
  [ ! -d "/opt/myPKA/Deliverables/Archive/$f" ] \
    && echo "NO COLLISION: $f" \
    || echo "COLLISION — HALT: $f"
done
```

Expected: 5 × `NO COLLISION`. Any `COLLISION` = halt before any mv. Report which target
already exists and do not proceed until Owner resolves.

---

## 3. Physical Archive Actions

Execute in order. After each `mv`, run the post-step check before continuing.
A single failed post-step check halts the entire plan.

### Step 1 — Folder 1

```bash
mv "/opt/myPKA/Deliverables/20260612_Core_DL Batch 1 Archive Execution Plan" \
   "/opt/myPKA/Deliverables/Archive/20260612_Core_DL Batch 1 Archive Execution Plan"
```

Post-step check:

```bash
[ ! -d "/opt/myPKA/Deliverables/20260612_Core_DL Batch 1 Archive Execution Plan" ] \
  && [ -d "/opt/myPKA/Deliverables/Archive/20260612_Core_DL Batch 1 Archive Execution Plan" ] \
  && echo "STEP 1 OK" || echo "STEP 1 FAILED — HALT"
```

### Step 2 — Folder 2

```bash
mv "/opt/myPKA/Deliverables/20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal" \
   "/opt/myPKA/Deliverables/Archive/20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal"
```

Post-step check:

```bash
[ ! -d "/opt/myPKA/Deliverables/20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal" ] \
  && [ -d "/opt/myPKA/Deliverables/Archive/20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal" ] \
  && echo "STEP 2 OK" || echo "STEP 2 FAILED — HALT"
```

### Step 3 — Folder 3

```bash
mv "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal"
```

Post-step check:

```bash
[ ! -d "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal" ] \
  && [ -d "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal" ] \
  && echo "STEP 3 OK" || echo "STEP 3 FAILED — HALT"
```

### Step 4 — Folder 4

```bash
mv "/opt/myPKA/Deliverables/20260607_Core_DL Smoke Test Recovery Report" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_DL Smoke Test Recovery Report"
```

Post-step check:

```bash
[ ! -d "/opt/myPKA/Deliverables/20260607_Core_DL Smoke Test Recovery Report" ] \
  && [ -d "/opt/myPKA/Deliverables/Archive/20260607_Core_DL Smoke Test Recovery Report" ] \
  && echo "STEP 4 OK" || echo "STEP 4 FAILED — HALT"
```

### Step 5 — Folder 5

```bash
mv "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Phase B Triage" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Hardening Phase B Triage"
```

Post-step check:

```bash
[ ! -d "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Phase B Triage" ] \
  && [ -d "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Hardening Phase B Triage" ] \
  && echo "STEP 5 OK" || echo "STEP 5 FAILED — HALT"
```

---

## 4. Lifecycle DB Updates

Execute only after all 5 mv operations and all 5 post-step checks pass.

### 4.1 Per-Id Updates — One Transaction

Each id is updated individually. If any update returns rowcount other than exactly 1,
the entire transaction rolls back and execution halts. Commit only executes if all 5
per-id updates return rowcount = 1.

```python
import sqlite3

conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
cur = conn.cursor()

ids = (70, 71, 44, 43, 54)
failed = []

try:
    for record_id in ids:
        cur.execute(
            "UPDATE deliverable_lifecycle "
            "SET state_gl017 = 'archived', owner_decision = 'archive' "
            "WHERE id = ?",
            (record_id,)
        )
        if cur.rowcount == 1:
            print(f'ID {record_id}: 1 row updated — OK')
        else:
            print(f'ID {record_id}: rowcount={cur.rowcount} — UNEXPECTED — marking for rollback')
            failed.append(record_id)

    if failed:
        conn.rollback()
        print(f'ROLLBACK complete. Failed ids: {failed}. No changes committed. HALT.')
    else:
        conn.commit()
        print('All 5 per-id updates committed.')

except Exception as e:
    conn.rollback()
    print(f'ERROR: {e} — rollback complete. HALT.')

finally:
    conn.close()
```

Expected: 5 × `1 row updated — OK`, followed by `All 5 per-id updates committed.`
Any `UNEXPECTED`, `ROLLBACK`, or `ERROR` line = halt and report to Owner. Do not proceed.

### 4.2 Post-Commit Verification Per Record

Run only after Section 4.1 reports `All 5 per-id updates committed.`

```python
import sqlite3

conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
cur = conn.cursor()
for record_id in (70, 71, 44, 43, 54):
    cur.execute(
        "SELECT id, state_gl017, owner_decision "
        "FROM deliverable_lifecycle WHERE id = ?",
        (record_id,)
    )
    row = cur.fetchone()
    if row and row[1] == 'archived' and row[2] == 'archive':
        print(f'ID {record_id}: VERIFIED — archived')
    else:
        print(f'ID {record_id}: MISMATCH — HALT — got: {row}')
conn.close()
```

Expected: 5 × `VERIFIED — archived`. Any `MISMATCH` = halt and report.

---

## 5. Verification Steps

Run after Phase 4 completes.

### 5.1 All 5 Folders Present in Archive

```bash
for f in \
  'Archive/20260612_Core_DL Batch 1 Archive Execution Plan' \
  'Archive/20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal' \
  'Archive/20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal' \
  'Archive/20260607_Core_DL Smoke Test Recovery Report' \
  'Archive/20260607_Core_Deliverable Lifecycle Hardening Phase B Triage'; do
  [ -d "/opt/myPKA/Deliverables/$f" ] \
    && echo "IN ARCHIVE: $f" \
    || echo "MISSING FROM ARCHIVE: $f"
done
```

Expected: 5 × `IN ARCHIVE`.

### 5.2 All 5 Folders Absent from Active Deliverables

```bash
for f in \
  '20260612_Core_DL Batch 1 Archive Execution Plan' \
  '20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal' \
  '20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal' \
  '20260607_Core_DL Smoke Test Recovery Report' \
  '20260607_Core_Deliverable Lifecycle Hardening Phase B Triage'; do
  [ ! -d "/opt/myPKA/Deliverables/$f" ] \
    && echo "GONE: $f" \
    || echo "STILL ACTIVE — HALT: $f"
done
```

Expected: 5 × `GONE`.

### 5.3 Active Lifecycle Record Count

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM deliverable_lifecycle WHERE state_gl017 != 'archived'")
count = cur.fetchone()[0]
print('Active records:', count)
conn.close()
```

Expected: 38 (baseline 43 minus 5 Pilot A folders).

### 5.4 No Unintended Actions

| Check | Expected |
|---|---|
| No newly moved folder in `Archive/` other than the 5 approved targets | Confirm by diffing Archive/ folder count before and after: delta must equal exactly 5 |
| No writes outside the 5 approved source paths, their 5 Archive target paths, and `team-knowledge.db` | Confirmed by inspection |
| No new folders in active `Deliverables/` | 0 new folders |
| No routing performed | Confirmed |
| No dashboard work | Confirmed |
| No Learning Candidate triage | Confirmed |
| No Batch 2 execution | Confirmed |
| No lifecycle records updated outside ids 70, 71, 44, 43, 54 | Confirm via: `SELECT COUNT(*) FROM deliverable_lifecycle WHERE state_gl017='archived' AND owner_decision='archive'` — delta from pre-execution count must equal exactly 5 |

---

## 6. Stop Conditions

Halt immediately and report to Owner if any of the following occur. Do not proceed past a
failed stop check under any circumstances.

| Condition | Action |
|---|---|
| Any preflight check fails (folder missing, record missing, live reference found, open task found) | Stop before any mv. Report which check failed. |
| Any `mv` command returns a non-zero exit code | Stop. Report step number and error. Do not continue to next folder. |
| Post-step check shows folder still present in active `Deliverables/` | Stop. Report step number. Do not continue. |
| Post-step check shows folder not present in `Archive/` | Stop. Report step number. Do not continue. |
| Any per-id UPDATE returns rowcount other than 1 | Rollback entire transaction. Stop. Report which id failed. Do not commit. |
| Per-record verification shows any id not returning `archived` / `archive` | Stop. Report which id failed. |
| Active lifecycle record count after execution is not 38 | Report discrepancy. Do not proceed to any further batch. |
| Any folder outside the 5 approved targets is moved during execution | Stop. Treat as critical error. Report immediately. |

---

## 7. Final Report Format

After successful execution, report to Owner in this exact format:

```
Pilot A — Execution complete

Folders archived (5):
  1. 20260612_Core_DL Batch 1 Archive Execution Plan
  2. 20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal
  3. 20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal
  4. 20260607_Core_DL Smoke Test Recovery Report
  5. 20260607_Core_Deliverable Lifecycle Hardening Phase B Triage

Lifecycle records updated (5): ids 43, 44, 54, 70, 71 → state_gl017=archived, owner_decision=archive

Active D-folder count before Pilot A: 43
Active D-folder count after Pilot A:  38

Stop conditions triggered: none
Unintended actions: none

Non-actions confirmed:
  - No routing performed
  - No new folders created
  - No Learning Candidate triage
  - No dashboard work
  - No Batch 2 execution
  - No sweep
  - No writes outside the 5 approved source paths, 5 Archive target paths, and team-knowledge.db
```

---

## 8. Explicit Non-Actions

This write plan performs no action. The following were not performed during its preparation
and must not be performed during its execution beyond what is explicitly stated above:

- No archive action (execution requires Owner authorization)
- No lifecycle record update
- No routing of any file to PKM, Team Knowledge, or any domain knowledge base
- No Learning Candidate triage
- No Batch 2 execution
- No sweep
- No dashboard work
- No new folders created
- No files created other than this write plan
- No modification to any D-folder outside the 5 approved Pilot A targets
- No writes to any database other than the 5 approved lifecycle record updates in `team-knowledge.db`

---

Delivered on: 2026-06-12
Delivered at: `Deliverables/20260612_Core_DL Control Inventory/20260612_pilot-a-archive-execution-write-plan-v01.md`
