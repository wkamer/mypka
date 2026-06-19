# DL Batch 1 — Archive Execution Plan v01

**Date:** 2026-06-12
**Prepared by:** Larry, Team Orchestrator
**Type:** Execution plan — read-only
**Status:** Awaiting Owner approval before execution
**Source inventory:** `Deliverables/20260612_Core_DL Control Inventory/dl-control-inventory-v02.md`

**Governance note:** This document is read-only. No files, folders, databases, or indexes
have been or will be modified by this document. Execution requires explicit Owner approval.

---

## 1. Pre-Execution Dependency Check Results

All checks verified as of 2026-06-12.

| Check | Result |
|---|---|
| All 15 source folders exist | PASS — all OK |
| Archive name collisions | PASS — all CLEAR (0 collisions) |
| All 15 folders have DB records | PASS |
| INDEX.md lists 14 of 15 folders | EXPECTED — item 15 not in INDEX.md (DB already shows `archived`) |
| Active operational cross-references | NONE — see Section 5 |

---

## 2. Exact File Move Operations

Execute in order. All moves are atomic directory renames within the same filesystem.

**Base paths:**
- Source base: `/opt/myPKA/Deliverables/`
- Destination base: `/opt/myPKA/Deliverables/Archive/`

**Command template:**
```bash
mv "/opt/myPKA/Deliverables/<FOLDER>" "/opt/myPKA/Deliverables/Archive/<FOLDER>"
```

### Batch 1 — Learning Candidate chain (14 folders)

| # | Folder | Files in folder |
|---|---|---|
| 1 | `20260603_Core_B-021C Closure Record` | 1 |
| 2 | `20260606_Core_LC Lifecycle Phase 1 Write-List v05` | 1 |
| 3 | `20260607_Core_LC Batch 1 Write-List` | 1 |
| 4 | `20260607_Core_LC Batch 1 Execution Report` | 1 |
| 5 | `20260607_Core_LC Batch 2 Write-List` | 6 |
| 6 | `20260607_Core_LC Batch 2 Execution Report` | 2 |
| 7 | `20260607_Core_LC Naming Alignment Impact Assessment` | 5 |
| 8 | `20260607_Core_LC Triage Write-Plan` | 7 |
| 9 | `20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion` | 1 |
| 10 | `20260607_Core_LC-5-6-7 Processed to Closed Assessment` | 1 |
| 11 | `20260607_Core_LC-9 Closure Report` | 1 |
| 12 | `20260607_Core_LCL Session Start Verification` | 3 |
| 13 | `20260607_Core_Post-SOP-019 Session Start Verification` | 1 |
| 14 | `20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4` | 1 |

### Batch 1a — DB discrepancy fix (1 folder, move only)

| # | Folder | Files in folder | Note |
|---|---|---|---|
| 15 | `20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal` | 1 | DB state already `archived`; physical move only |

**Total folders to move: 15**
**Total files inside those folders: 36**

### Exact shell commands (ready to execute)

```bash
mv "/opt/myPKA/Deliverables/20260603_Core_B-021C Closure Record" \
   "/opt/myPKA/Deliverables/Archive/20260603_Core_B-021C Closure Record"

mv "/opt/myPKA/Deliverables/20260606_Core_LC Lifecycle Phase 1 Write-List v05" \
   "/opt/myPKA/Deliverables/Archive/20260606_Core_LC Lifecycle Phase 1 Write-List v05"

mv "/opt/myPKA/Deliverables/20260607_Core_LC Batch 1 Write-List" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Batch 1 Write-List"

mv "/opt/myPKA/Deliverables/20260607_Core_LC Batch 1 Execution Report" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Batch 1 Execution Report"

mv "/opt/myPKA/Deliverables/20260607_Core_LC Batch 2 Write-List" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Batch 2 Write-List"

mv "/opt/myPKA/Deliverables/20260607_Core_LC Batch 2 Execution Report" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Batch 2 Execution Report"

mv "/opt/myPKA/Deliverables/20260607_Core_LC Naming Alignment Impact Assessment" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Naming Alignment Impact Assessment"

mv "/opt/myPKA/Deliverables/20260607_Core_LC Triage Write-Plan" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Triage Write-Plan"

mv "/opt/myPKA/Deliverables/20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion"

mv "/opt/myPKA/Deliverables/20260607_Core_LC-5-6-7 Processed to Closed Assessment" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_LC-5-6-7 Processed to Closed Assessment"

mv "/opt/myPKA/Deliverables/20260607_Core_LC-9 Closure Report" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_LC-9 Closure Report"

mv "/opt/myPKA/Deliverables/20260607_Core_LCL Session Start Verification" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_LCL Session Start Verification"

mv "/opt/myPKA/Deliverables/20260607_Core_Post-SOP-019 Session Start Verification" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_Post-SOP-019 Session Start Verification"

mv "/opt/myPKA/Deliverables/20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4"

mv "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal"
```

---

## 3. Expected Database Updates

**Database:** `/opt/myPKA/Team Knowledge/team-knowledge.db`
**Table:** `deliverable_lifecycle`

### Items 1–14: state transition + owner decision

```sql
UPDATE deliverable_lifecycle
SET state_gl017 = 'archived',
    owner_decision = 'archive'
WHERE artifact_name IN (
  '20260603_Core_B-021C Closure Record',
  '20260606_Core_LC Lifecycle Phase 1 Write-List v05',
  '20260607_Core_LC Batch 1 Write-List',
  '20260607_Core_LC Batch 1 Execution Report',
  '20260607_Core_LC Batch 2 Write-List',
  '20260607_Core_LC Batch 2 Execution Report',
  '20260607_Core_LC Naming Alignment Impact Assessment',
  '20260607_Core_LC Triage Write-Plan',
  '20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion',
  '20260607_Core_LC-5-6-7 Processed to Closed Assessment',
  '20260607_Core_LC-9 Closure Report',
  '20260607_Core_LCL Session Start Verification',
  '20260607_Core_Post-SOP-019 Session Start Verification',
  '20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4'
);
```

**Expected rows affected: 14**

### Item 15: owner decision only (state already `archived`)

```sql
UPDATE deliverable_lifecycle
SET owner_decision = 'archive'
WHERE artifact_name = '20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal';
```

**Expected rows affected: 1**

### DB state before / after (per record)

| id | Folder (short) | state before | state after | od before | od after |
|---|---|---|---|---|---|
| 9 | B-021C Closure Record | pending_lifecycle_decision | archived | None | archive |
| 17 | LC Phase 1 Write-List v05 | pending_lifecycle_decision | archived | None | archive |
| 26 | LC Batch 1 Write-List | pending_lifecycle_decision | archived | None | archive |
| 27 | LC Batch 1 Execution Report | pending_lifecycle_decision | archived | None | archive |
| 28 | LC Batch 2 Write-List | pending_lifecycle_decision | archived | None | archive |
| 29 | LC Batch 2 Execution Report | pending_lifecycle_decision | archived | None | archive |
| 31 | LC Naming Alignment | pending_lifecycle_decision | archived | None | archive |
| 30 | LC Triage Write-Plan | pending_lifecycle_decision | archived | None | archive |
| 32 | LC-4 SOP-019 Retrospective | pending_lifecycle_decision | archived | None | archive |
| 33 | LC-5-6-7 Processed to Closed | pending_lifecycle_decision | archived | None | archive |
| 34 | LC-9 Closure Report | pending_lifecycle_decision | archived | None | archive |
| 35 | LCL Session Start Verification | pending_lifecycle_decision | archived | None | archive |
| 37 | Post-SOP-019 Verification | pending_lifecycle_decision | archived | None | archive |
| 38 | SOP-019 Initiation Proposal LC-4 | pending_lifecycle_decision | archived | None | archive |
| 51 | DL Naming Artifact Proposal | archived (no change) | archived | None | archive |

---

## 4. INDEX.md Update

INDEX.md is maintained by `Team Knowledge/Core/Scripts/generate_deliverable_index.py`.

After all file moves complete: regenerate INDEX.md.

```bash
python3 "Team Knowledge/Core/Scripts/generate_deliverable_index.py"
```

**Expected outcome:**
- 14 entries removed (items 1–14; item 15 was not in INDEX.md)
- Active folder count: 55 → 40
- pending_lifecycle_decision count reduced by 14

---

## 5. Cross-Reference Assessment

Cross-references to batch items were found in the following files outside this batch.
None are operational dependencies. All are historical references in process artifacts.

| Referencing file | Batch items referenced | Referencing folder classification | Impact |
|---|---|---|---|
| `Final Governance State Verification/final-governance-state-verification-v01.md` | LC-4 SOP-019, LC-9 Closure Report, Post-SOP-019 | retain_for_audit | References become historical; file is a point-in-time snapshot — no action needed |
| `DLH Discovery and Proposal/phase-a-execution-report-v01.md` | Post-SOP-019, SOP-019 Initiation Proposal | archive_candidate (future batch) | Folder itself is an archive candidate; stale refs will be archived together |
| `Auto-Processing Phase 1 Design/phase1-design.md` | B-021C Closure Record | needs_owner_decision | Historical reference to a completed item; no operational dependency |
| `DL Pending Decision Inventory/dl-batch-archive-execution-plan-v01.md` | LC Phase 1 Write-List, LC Batch 1+2 Write-Lists, LC Naming Alignment, LC Triage Write-Plan, SOP-019 Initiation | needs_owner_decision | Prior execution plan listing these as archive candidates; references are consistent with archiving |
| `DL Pending Decision Inventory/dl-count-reconciliation-analysis-v01.md` | LC Phase 1 Write-List | needs_owner_decision | Historical count reference; no operational dependency |

**Conclusion:** No cross-reference blocks execution. References in retain_for_audit and needs_owner_decision folders are historical and will remain valid as path references pointing to Archive/.

---

## 6. Rollback Plan

If any move fails mid-batch, stop and execute the reverse moves for all completed items.

### Rollback shell commands

```bash
# Reverse each completed move — execute only for items that were moved
mv "/opt/myPKA/Deliverables/Archive/20260603_Core_B-021C Closure Record" \
   "/opt/myPKA/Deliverables/20260603_Core_B-021C Closure Record"

mv "/opt/myPKA/Deliverables/Archive/20260606_Core_LC Lifecycle Phase 1 Write-List v05" \
   "/opt/myPKA/Deliverables/20260606_Core_LC Lifecycle Phase 1 Write-List v05"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Batch 1 Write-List" \
   "/opt/myPKA/Deliverables/20260607_Core_LC Batch 1 Write-List"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Batch 1 Execution Report" \
   "/opt/myPKA/Deliverables/20260607_Core_LC Batch 1 Execution Report"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Batch 2 Write-List" \
   "/opt/myPKA/Deliverables/20260607_Core_LC Batch 2 Write-List"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Batch 2 Execution Report" \
   "/opt/myPKA/Deliverables/20260607_Core_LC Batch 2 Execution Report"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Naming Alignment Impact Assessment" \
   "/opt/myPKA/Deliverables/20260607_Core_LC Naming Alignment Impact Assessment"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_LC Triage Write-Plan" \
   "/opt/myPKA/Deliverables/20260607_Core_LC Triage Write-Plan"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion" \
   "/opt/myPKA/Deliverables/20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_LC-5-6-7 Processed to Closed Assessment" \
   "/opt/myPKA/Deliverables/20260607_Core_LC-5-6-7 Processed to Closed Assessment"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_LC-9 Closure Report" \
   "/opt/myPKA/Deliverables/20260607_Core_LC-9 Closure Report"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_LCL Session Start Verification" \
   "/opt/myPKA/Deliverables/20260607_Core_LCL Session Start Verification"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_Post-SOP-019 Session Start Verification" \
   "/opt/myPKA/Deliverables/20260607_Core_Post-SOP-019 Session Start Verification"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4" \
   "/opt/myPKA/Deliverables/20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4"

mv "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal" \
   "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal"
```

### DB rollback

```sql
UPDATE deliverable_lifecycle
SET state_gl017 = 'pending_lifecycle_decision',
    owner_decision = NULL
WHERE artifact_name IN (
  '20260603_Core_B-021C Closure Record',
  '20260606_Core_LC Lifecycle Phase 1 Write-List v05',
  '20260607_Core_LC Batch 1 Write-List',
  '20260607_Core_LC Batch 1 Execution Report',
  '20260607_Core_LC Batch 2 Write-List',
  '20260607_Core_LC Batch 2 Execution Report',
  '20260607_Core_LC Naming Alignment Impact Assessment',
  '20260607_Core_LC Triage Write-Plan',
  '20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion',
  '20260607_Core_LC-5-6-7 Processed to Closed Assessment',
  '20260607_Core_LC-9 Closure Report',
  '20260607_Core_LCL Session Start Verification',
  '20260607_Core_Post-SOP-019 Session Start Verification',
  '20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4'
);

-- Item 15: restore owner_decision only (state was already archived before this batch)
UPDATE deliverable_lifecycle
SET owner_decision = NULL
WHERE artifact_name = '20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal';
```

Then regenerate INDEX.md.

---

## 7. Post-Execution Verification Steps

Run these checks in order after execution. Each must pass before confirming completion.

### Step 1 — Source folders absent

```bash
python3 << 'EOF'
import os
base = '/opt/myPKA/Deliverables'
batch = [
  '20260603_Core_B-021C Closure Record',
  '20260606_Core_LC Lifecycle Phase 1 Write-List v05',
  '20260607_Core_LC Batch 1 Write-List',
  '20260607_Core_LC Batch 1 Execution Report',
  '20260607_Core_LC Batch 2 Write-List',
  '20260607_Core_LC Batch 2 Execution Report',
  '20260607_Core_LC Naming Alignment Impact Assessment',
  '20260607_Core_LC Triage Write-Plan',
  '20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion',
  '20260607_Core_LC-5-6-7 Processed to Closed Assessment',
  '20260607_Core_LC-9 Closure Report',
  '20260607_Core_LCL Session Start Verification',
  '20260607_Core_Post-SOP-019 Session Start Verification',
  '20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4',
  '20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal',
]
for f in batch:
    still_present = os.path.isdir(os.path.join(base, f))
    print(f'[{"FAIL - still present" if still_present else "PASS"}] {f}')
EOF
```

### Step 2 — Destination folders present

```bash
python3 << 'EOF'
import os
archive = '/opt/myPKA/Deliverables/Archive'
batch = [
  '20260603_Core_B-021C Closure Record',
  '20260606_Core_LC Lifecycle Phase 1 Write-List v05',
  '20260607_Core_LC Batch 1 Write-List',
  '20260607_Core_LC Batch 1 Execution Report',
  '20260607_Core_LC Batch 2 Write-List',
  '20260607_Core_LC Batch 2 Execution Report',
  '20260607_Core_LC Naming Alignment Impact Assessment',
  '20260607_Core_LC Triage Write-Plan',
  '20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion',
  '20260607_Core_LC-5-6-7 Processed to Closed Assessment',
  '20260607_Core_LC-9 Closure Report',
  '20260607_Core_LCL Session Start Verification',
  '20260607_Core_Post-SOP-019 Session Start Verification',
  '20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4',
  '20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal',
]
for f in batch:
    present = os.path.isdir(os.path.join(archive, f))
    print(f'[{"PASS" if present else "FAIL - missing"}] {f}')
EOF
```

### Step 3 — DB state confirmed

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
cur = conn.cursor()
cur.execute("""
  SELECT artifact_name, state_gl017, owner_decision
  FROM deliverable_lifecycle
  WHERE artifact_name IN (
    '20260603_Core_B-021C Closure Record',
    '20260606_Core_LC Lifecycle Phase 1 Write-List v05',
    '20260607_Core_LC Batch 1 Write-List',
    '20260607_Core_LC Batch 1 Execution Report',
    '20260607_Core_LC Batch 2 Write-List',
    '20260607_Core_LC Batch 2 Execution Report',
    '20260607_Core_LC Naming Alignment Impact Assessment',
    '20260607_Core_LC Triage Write-Plan',
    '20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion',
    '20260607_Core_LC-5-6-7 Processed to Closed Assessment',
    '20260607_Core_LC-9 Closure Report',
    '20260607_Core_LCL Session Start Verification',
    '20260607_Core_Post-SOP-019 Session Start Verification',
    '20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4',
    '20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal'
  )
""")
for r in cur.fetchall():
    state_ok = r[1] == 'archived'
    od_ok = r[2] == 'archive'
    print(f'[{"PASS" if state_ok and od_ok else "FAIL"}] state={r[1]} od={r[2]} | {r[0]}')
conn.close()
```

**Expected: 15 PASS**

### Step 4 — INDEX.md count

After `generate_deliverable_index.py` runs:
- Active folder count must be ≤ 41 (55 minus 14; item 15 was not in INDEX.md)
- No entries for any of the 14 moved folders

### Step 5 — Active folder total

```bash
ls /opt/myPKA/Deliverables/ | grep -v '^Archive$' | grep -v '^INDEX' | grep -v '^README' | wc -l
```

**Expected result: 40** (55 − 15)

---

## 8. Execution Authorization Requirement

This plan requires explicit Owner approval before any step is executed.

Owner approval authorizes:
1. All 15 file moves (Sections 2)
2. All 15 DB updates (Section 3)
3. INDEX.md regeneration (Section 4)

Approval of this plan does NOT authorize future batches.

---

Delivered on: 2026-06-12
Delivered at: Deliverables/20260612_Core_DL Batch 1 Archive Execution Plan/dl-batch1-archive-execution-plan-v01.md
