# Pilot B Archive Execution Write Plan — v02 (Retry after SC-7 halt)

**Date:** 2026-06-12
**Author:** Governance Assistant
**Status:** Awaiting Owner authorization
**Containment folder:** `Deliverables/20260612_Core_DL Control Inventory/`
**Supersedes:** `20260612_pilot-b-archive-execution-write-plan-v01.md`
**Execution Persistence Rule:** This write plan is required before Owner authorization.
A persisted execution report is required immediately after execution completes.

---

## 1. Context — Why v02 Exists

Pilot B v01 (`20260612_pilot-b-archive-execution-write-plan-v01.md`) halted correctly at SC-7
during preflight 3.6.

**Trigger:** lifecycle id 62 (`20260608_Core_Retention Assessment P2 P5 UMC`) — file
`assessment.md` contained `**Action required: Owner authorization to write to GL-013.**`
This is a live open item signal. GL-013 implementation status is unconfirmed. SC-7 applies.

**Owner instruction:** exclude id 62 from retry. Do not resolve GL-013 in this scope.

**id 62 state after halt:** unchanged. `state_gl017 = active`, `owner_decision = NULL`.
id 62 is not touched in this plan.

---

## 2. Current Assumption Verification

**Expected active D-folder count before retry:** 38

Verification at execution time:

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
count = conn.execute(
    "SELECT COUNT(*) FROM deliverable_lifecycle WHERE state_gl017 != 'archived'"
).fetchone()[0]
print(f"Non-archived in DB: {count}")
conn.close()
```

Expected: 38.
If not 38: STOP. Report discrepancy before continuing.

---

## 3. Retry Scope — 4 Folders

| # | Folder | Lifecycle id | Current state_gl017 | Owner decision |
|---|---|---|---|---|
| 1 | `20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal` | 47 | `pending_lifecycle_decision` | Batch confirm via this plan |
| 2 | `20260608_Core_UMC Archive Eligibility Chain Process Review` | 64 | `active` | Batch confirm via this plan |
| 3 | `20260608_Core_R1-R5 Prioritization Assessment` | 65 | `active` | Batch confirm via this plan |
| 4 | `20260608_Core_Phase 1 Proposal R1 R5 v01` | 66 | `active` | Batch confirm via this plan |

**Explicitly excluded:**

| Lifecycle id | Folder | Reason |
|---|---|---|
| 62 | `20260608_Core_Retention Assessment P2 P5 UMC` | SC-7 triggered in v01 preflight. Live GL-013 action signal in `assessment.md`. GL-013 status unconfirmed. Excluded per Owner instruction. |

---

## 4. Preflight Checks

Run all checks before any physical move. Stop on any failure.

### 4.1 Pre-execution D-folder count

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
count = conn.execute(
    "SELECT COUNT(*) FROM deliverable_lifecycle WHERE state_gl017 != 'archived'"
).fetchone()[0]
print(f"Non-archived in DB: {count}")
conn.close()
```

Expected: 38. If not 38: STOP.

### 4.2 Source folders exist in active Deliverables

```bash
ls "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal/"
ls "/opt/myPKA/Deliverables/20260608_Core_UMC Archive Eligibility Chain Process Review/"
ls "/opt/myPKA/Deliverables/20260608_Core_R1-R5 Prioritization Assessment/"
ls "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v01/"
```

Expected: all 4 return file listings without error. If any missing: STOP.

### 4.3 Archive targets do not already exist

```bash
ls "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_UMC Archive Eligibility Chain Process Review" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_R1-R5 Prioritization Assessment" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_Phase 1 Proposal R1 R5 v01" 2>&1
```

Expected: all 4 return "No such file or directory." If any exists: STOP.

### 4.4 Lifecycle records exist and match

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
ids = [47, 64, 65, 66]
for id_ in ids:
    row = conn.execute(
        "SELECT id, artifact_name, state_gl017 FROM deliverable_lifecycle WHERE id = ?",
        (id_,)
    ).fetchone()
    if row:
        print(f"OK: id {row[0]} | {row[1]} | state={row[2]}")
    else:
        print(f"FAIL: id {id_} — NOT FOUND")
conn.close()
```

Expected: each id returns exactly one row. If any missing: STOP.

### 4.5 No live SOP, GL, or CLAUDE.md references

```bash
grep -r "Deliverable Lifecycle Hardening Discovery and Proposal" \
  /opt/myPKA/Team\ Knowledge/Core/Guidelines/ \
  /opt/myPKA/Team\ Knowledge/Core/SOPs/ \
  /opt/myPKA/CLAUDE.md 2>/dev/null

grep -r "UMC Archive Eligibility Chain Process Review" \
  /opt/myPKA/Team\ Knowledge/Core/Guidelines/ \
  /opt/myPKA/Team\ Knowledge/Core/SOPs/ \
  /opt/myPKA/CLAUDE.md 2>/dev/null

grep -r "R1-R5 Prioritization Assessment" \
  /opt/myPKA/Team\ Knowledge/Core/Guidelines/ \
  /opt/myPKA/Team\ Knowledge/Core/SOPs/ \
  /opt/myPKA/CLAUDE.md 2>/dev/null

grep -r "Phase 1 Proposal R1 R5 v01" \
  /opt/myPKA/Team\ Knowledge/Core/Guidelines/ \
  /opt/myPKA/Team\ Knowledge/Core/SOPs/ \
  /opt/myPKA/CLAUDE.md 2>/dev/null
```

Expected: no output. If any match: STOP. Do not archive that folder.

### 4.6 No open team_task references

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
keywords = [
    (47, 'Hardening Discovery'),
    (64, 'Eligibility Chain Process Review'),
    (65, 'R1-R5 Prioritization'),
    (66, 'Phase 1 Proposal R1 R5 v01'),
]
for id_, kw in keywords:
    rows = conn.execute(
        "SELECT id, title, status FROM team_tasks WHERE title LIKE ? AND status != 'completed'",
        (f'%{kw}%',)
    ).fetchall()
    if rows:
        print(f"FAIL (id {id_}): open task found: {rows}")
    else:
        print(f"OK (id {id_}): no open tasks for '{kw}'")
conn.close()
```

Expected: all 4 return empty. If any open task found: STOP.

### 4.7 Folder contents — no live open item signals

```bash
grep -ri "TODO\|ACTION REQUIRED\|OPEN:\|DECISION NEEDED\|PENDING:" \
  "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal/" 2>/dev/null

grep -ri "TODO\|ACTION REQUIRED\|OPEN:\|DECISION NEEDED\|PENDING:" \
  "/opt/myPKA/Deliverables/20260608_Core_UMC Archive Eligibility Chain Process Review/" 2>/dev/null

grep -ri "TODO\|ACTION REQUIRED\|OPEN:\|DECISION NEEDED\|PENDING:" \
  "/opt/myPKA/Deliverables/20260608_Core_R1-R5 Prioritization Assessment/" 2>/dev/null

grep -ri "TODO\|ACTION REQUIRED\|OPEN:\|DECISION NEEDED\|PENDING:" \
  "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v01/" 2>/dev/null
```

Expected: no output, or hits assessed as historical governance rule prose (not standalone action items).
Evaluate each hit case by case. If any hit is a live open item: STOP.

**Known pattern from v01 preflight:** id 66 (`20260608_Core_Phase 1 Proposal R1 R5 v01`)
contains "action required" as part of embedded governance rule text
(`where the only action required is appending to an existing document`).
This was assessed in v01 as non-live prose. Not a SC-7 trigger.
Reconfirm assessment at execution time.

### 4.8 Archive folder writable

```bash
touch "/opt/myPKA/Deliverables/Archive/.writecheck" && \
  rm "/opt/myPKA/Deliverables/Archive/.writecheck" && \
  echo "Archive writable" || echo "Archive NOT writable — STOP"
```

Expected: "Archive writable." If not: STOP.

---

## 5. Exact Physical Archive Actions

Execute one folder at a time. Run post-step check after each move.
Stop immediately on any failure. Do not continue to the next folder.

**Archive base path:** `/opt/myPKA/Deliverables/Archive/`

### Step 1 — id 47

```bash
mv "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal"
```

Post-step check:

```bash
ls "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal/"
```

Expected: source returns "No such file or directory"; archive target lists files. If either fails: STOP.

---

### Step 2 — id 64

```bash
mv "/opt/myPKA/Deliverables/20260608_Core_UMC Archive Eligibility Chain Process Review" \
   "/opt/myPKA/Deliverables/Archive/20260608_Core_UMC Archive Eligibility Chain Process Review"
```

Post-step check:

```bash
ls "/opt/myPKA/Deliverables/20260608_Core_UMC Archive Eligibility Chain Process Review" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_UMC Archive Eligibility Chain Process Review/"
```

Expected: same pattern as Step 1. If either fails: STOP.

---

### Step 3 — id 65

```bash
mv "/opt/myPKA/Deliverables/20260608_Core_R1-R5 Prioritization Assessment" \
   "/opt/myPKA/Deliverables/Archive/20260608_Core_R1-R5 Prioritization Assessment"
```

Post-step check:

```bash
ls "/opt/myPKA/Deliverables/20260608_Core_R1-R5 Prioritization Assessment" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_R1-R5 Prioritization Assessment/"
```

Expected: same pattern as Step 1. If either fails: STOP.

---

### Step 4 — id 66

```bash
mv "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v01" \
   "/opt/myPKA/Deliverables/Archive/20260608_Core_Phase 1 Proposal R1 R5 v01"
```

Post-step check:

```bash
ls "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v01" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_Phase 1 Proposal R1 R5 v01/"
```

Expected: same pattern as Step 1. If either fails: STOP.

---

## 6. Exact Lifecycle DB Update Plan

Execute after all 4 physical moves complete and post-step checks pass.
All 4 updates inside one transaction.

```python
import sqlite3
from datetime import datetime

conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')

try:
    conn.execute("BEGIN TRANSACTION")

    approved_ids = [47, 64, 65, 66]
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    for id_ in approved_ids:
        result = conn.execute(
            """UPDATE deliverable_lifecycle
               SET state_gl017 = 'archived',
                   owner_decision = 'archive',
                   updated_at = ?
               WHERE id = ?""",
            (now, id_)
        )
        affected = result.rowcount
        if affected != 1:
            raise Exception(
                f"ROLLBACK TRIGGER: id {id_} affected {affected} rows (expected exactly 1)"
            )
        print(f"id {id_}: updated ({affected} row)")

    conn.execute("COMMIT")
    print("Transaction committed.")

except Exception as e:
    conn.execute("ROLLBACK")
    print(f"ROLLED BACK: {e}")
    raise

finally:
    conn.close()
```

Rules:
- Each id must affect exactly 1 row. If any id returns 0 or more than 1: ROLLBACK immediately.
- Commit only after all 4 ids update correctly.
- id 62 must NOT appear in this transaction. If it does: ROLLBACK. Stop. Report.
- If rollback triggered: STOP. Report exact error. Do not proceed to verification.

---

## 7. Verification Steps

### 7.1 Approved folders present in Archive

```bash
ls "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal/"
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_UMC Archive Eligibility Chain Process Review/"
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_R1-R5 Prioritization Assessment/"
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_Phase 1 Proposal R1 R5 v01/"
```

Expected: all 4 return file listings.

### 7.2 Approved folders absent from active Deliverables

```bash
ls "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal" 2>&1
ls "/opt/myPKA/Deliverables/20260608_Core_UMC Archive Eligibility Chain Process Review" 2>&1
ls "/opt/myPKA/Deliverables/20260608_Core_R1-R5 Prioritization Assessment" 2>&1
ls "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v01" 2>&1
```

Expected: all 4 return "No such file or directory."

### 7.3 id 62 unchanged

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
row = conn.execute(
    "SELECT id, artifact_name, state_gl017, owner_decision FROM deliverable_lifecycle WHERE id = 62"
).fetchone()
print(f"id 62: state={row[2]}, owner_decision={row[3]}")
conn.close()
```

Expected: `state_gl017 = active`, `owner_decision = None`. If changed: STOP. Report.

### 7.4 Active D-folder count decreased by exactly 4

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
count = conn.execute(
    "SELECT COUNT(*) FROM deliverable_lifecycle WHERE state_gl017 != 'archived'"
).fetchone()[0]
print(f"Non-archived in DB: {count}")
conn.close()
```

Expected: 34 (38 before retry minus 4 archived). If not 34: STOP.

### 7.5 Total active Deliverables entries

```bash
ls /opt/myPKA/Deliverables/ | grep -v '^Archive$' | wc -l
```

Expected: 36 (34 D-folders + INDEX.md + README.md). If not 36: STOP.

### 7.6 Non-actions confirmed

Verify the following did NOT happen during execution:
- No routing performed to any live system file
- No dashboard work started
- No Learning Candidate triage performed
- No Batch 2 started
- No sweep performed
- No lifecycle records updated outside approved ids 47, 64, 65, 66
- id 62 not touched
- No new D-folders created
- No `registered_but_unclear` folders touched
- No `owner_decision_needed` folders touched
- No domain knowledge folders touched
- GL-013 not resolved or written

---

## 8. Persisted Execution Report Requirement

After execution, immediately write a persisted execution report inside the containment folder.

**Required path:**
`Deliverables/20260612_Core_DL Control Inventory/20260612_pilot-b-retry-archive-execution-report-v01.md`

**Chat-only execution result is not sufficient.** Hard requirement per Execution Persistence Rule
(CLAUDE.md, live since 2026-06-12).

**Report must include:**
- v01 halt context (SC-7, id 62)
- Folders archived (names and lifecycle ids)
- Lifecycle records updated
- id 62 state confirmed unchanged
- Active D-folder count before and after
- Total Deliverables entries after
- Stop conditions triggered (or none)
- Unintended actions (or none)
- Non-actions confirmed
- Execution report path (self-reference)

---

## 9. Stop Conditions

| # | Stop condition |
|---|---|
| SC-1 | Active D-folder count before retry does not equal 38 |
| SC-2 | Any source folder (ids 47, 64, 65, 66) absent from active Deliverables |
| SC-3 | Any archive target already exists in Archive |
| SC-4 | Any lifecycle record missing for an approved id |
| SC-5 | Any grep returns a live SOP, GL, or CLAUDE.md reference to an approved folder |
| SC-6 | Any open team_task references an approved folder |
| SC-7 | Any folder content contains a live open item signal |
| SC-8 | Archive folder not writable |
| SC-9 | Any physical move fails or post-step check fails |
| SC-10 | DB update for any id affects 0 or more than 1 row (triggers rollback) |
| SC-11 | DB rollback triggered for any reason |
| SC-12 | id 62 appears in the DB transaction |
| SC-13 | Active D-folder count after execution is not exactly 34 |
| SC-14 | Total Deliverables entries after execution is not exactly 36 |
| SC-15 | Any lifecycle record outside approved ids 47, 64, 65, 66 was updated |
| SC-16 | id 62 state changed from pre-execution values |
| SC-17 | Execution report not written (Execution Persistence Rule violation) |

On any stop condition: halt all further execution, report exact condition and state to Owner,
await explicit instruction before continuing.

---

## 10. Associated Write-List

No associated write-list exists for this execution. Therefore no write-list batch-stop rules apply.
Batch-stop rules are defined in Section 9 of this write plan only.

---

Delivered on: 2026-06-12
Delivered at: `Deliverables/20260612_Core_DL Control Inventory/20260612_pilot-b-archive-execution-write-plan-v02.md`
