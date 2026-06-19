# DL Batch Archive Execution Plan — v01

**Scope declaration:** READ-ONLY document. This file contains the plan only. No folder moves, no file writes, no database updates have been or will be executed from this document. Write authorization is requested separately before any execution step begins.

**Author:** Larry  
**Date:** 2026-06-08  
**Status:** Ready for owner authorization

---

## 1. Context

This plan covers the remaining archive candidates from the DL Pending Decision Inventory (`dl-pending-decision-inventory-v01.md`). It follows the completion of:
- Owner Decision Batch (2 archived, 2 retained)
- Lifecycle Review Batch (Task 85 archived, Task 86 archived)

The inventory recommended **19 items** for archive. All 19 are currently in `Deliverables/`. None have been moved yet.

---

## 2. Count Discrepancy — Verified

The prior session summary stated "15 archive candidates remain unprocessed." This is incorrect.

**Verified count: 19.**

Source of truth: `dl-pending-decision-inventory-v01.md` Section 2 ("By Recommended Disposition"), and `lifecycle-review-recommendation-v01.md` Note on Remaining Inventory ("19 archive candidates not yet processed"). Filesystem check confirms all 19 are present in `Deliverables/` and 0 are in `Deliverables/Archive/`.

The session summary appears to have undercounted by 4. The count of 19 is used throughout this plan.

---

## 3. Candidate List — Verified Current State

All 19 folders exist in `/opt/myPKA/Deliverables/`. None are pre-archived.

| # | Inventory item | Folder | Workstream | Type | Safe to archive |
|---|---|---|---|---|---|
| 1 | 1 | 20260606_Core_LC Lifecycle Phase 1 Write-List v05 | DLH | write_list | Yes |
| 2 | 2 | 20260607_Core_Auto-Processing Deliverable Lifecycle Discovery | DLH | proposal | Yes |
| 3 | 3 | 20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design | DLH | proposal | Yes |
| 4 | 4 | 20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal | DLH | proposal | Yes |
| 5 | 6 | 20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal | DLH | proposal | Yes |
| 6 | 7 | 20260607_Core_LC Batch 1 Write-List | DLH | write_list | Yes |
| 7 | 8 | 20260607_Core_LC Batch 2 Write-List | DLH | write_list | Yes |
| 8 | 9 | 20260607_Core_LC Triage Write-Plan | DLH | write_list | Yes |
| 9 | 13 | 20260608_Core_DL Post-Granularity Usability Assessment | DLH | assessment | Yes |
| 10 | 14 | 20260608_Core_DL Usability Assessment Owner Perspective | DLH | assessment | Yes |
| 11 | 15 | 20260608_Core_DL Visibility Architecture Assessment | DLH | assessment | Yes |
| 12 | 19 | 20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4 | GG | proposal | Yes |
| 13 | 21 | 20260530_Core_UMC diagnose en aanbevelingen | UMC | triage_document | **FLAG — see Section 4** |
| 14 | 23 | 20260604_Core_Deliverable Lifecycle Knowledge Processing Triage | Standalone | triage_document | Yes |
| 15 | 25 | 20260607_Core_DL Phase 1 Retroactive Iris Review | Standalone | triage_document | Yes |
| 16 | 26 | 20260607_Core_Deliverable Lifecycle Backlog Processing Batch 1 Proposal | Standalone | proposal | Yes |
| 17 | 27 | 20260607_Core_LC Naming Alignment Impact Assessment | Standalone | assessment | Yes |
| 18 | 28 | 20260607_Core_Learning Candidate Flag Triage Proposal | Standalone | proposal | Yes |
| 19 | 29 | 20260607_Core_team-tasks-id-76-assessment | Standalone | triage_document | Yes |

---

## 4. Flags — Items Requiring Owner Decision Before Execution

### FLAG — Item 13: 20260530_Core_UMC diagnose en aanbevelingen

- **Inventory recommendation:** archive
- **Rationale in inventory:** UMC is operational. Diagnosis findings absorbed.
- **Risk:** The parallel item `20260520_Core_Unified Memory Core architectuurschets` (inventory item 20) was elevated to "owner decision required" precisely because Larry could not confirm whether UMC architecture was captured in active KE files. `UMC diagnose en aanbevelingen` has the same risk profile: if the diagnosis recommendations are NOT captured in a KE file (KE-Memory or equivalent), archiving permanently removes the only record of those recommendations.
- **What this flag requires:** Before archiving this item, verify whether the UMC diagnosis recommendations are captured in an active KE file. If yes: safe to archive. If no: route content to Kai or Sienna for KE capture first.
- **Default if unresolved:** exclude from batch; archive separately after verification.

---

## 5. Batch Composition

**Total candidates:** 19  
**Clean for batch execution (no flags):** 18 (all except item 13)  
**Flagged (excluded from batch until resolved):** 1 (item 13)

The execution plan below covers all 19. The executor must skip item 13 unless the owner has explicitly resolved the flag before the execution step begins.

---

## 6. Batch-Stop Rules

These rules govern the execution step. The executor must apply them during the move phase.

**BSR-1 — Existence check before move.** Before each `mv` command: confirm the source folder exists in `Deliverables/`. If a folder is missing (already moved or deleted), do not treat as success — log as anomaly and continue only after flagging to Larry.

**BSR-2 — No partial batch.** If any `mv` command fails (permission error, path error, unexpected state), halt the batch. Do not continue with remaining items. Report the failure point and current state to Larry before resuming.

**BSR-3 — Database update only after move phase complete.** Do not execute any SQL until all `mv` commands for the batch have completed and the post-check on folder locations passes.

**BSR-4 — Flag item 13 gate.** Item 13 (`20260530_Core_UMC diagnose en aanbevelingen`) must be explicitly authorized by the owner before inclusion in the batch. If not explicitly authorized, skip. Do not infer authorization from a general "execute the batch" instruction.

**BSR-5 — INDEX.md regeneration is final step.** Run `generate_deliverable_index.py` only after all SQL updates are complete.

---

## 7. Exact Execution Steps

### Phase A — Folder Moves (18 clean items)

Execute in sequence. Each command is a single-folder move.

```bash
BASE="/opt/myPKA/Deliverables"
ARCHIVE="/opt/myPKA/Deliverables/Archive"

mv "$BASE/20260606_Core_LC Lifecycle Phase 1 Write-List v05" "$ARCHIVE/"
mv "$BASE/20260607_Core_Auto-Processing Deliverable Lifecycle Discovery" "$ARCHIVE/"
mv "$BASE/20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design" "$ARCHIVE/"
mv "$BASE/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal" "$ARCHIVE/"
mv "$BASE/20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal" "$ARCHIVE/"
mv "$BASE/20260607_Core_LC Batch 1 Write-List" "$ARCHIVE/"
mv "$BASE/20260607_Core_LC Batch 2 Write-List" "$ARCHIVE/"
mv "$BASE/20260607_Core_LC Triage Write-Plan" "$ARCHIVE/"
mv "$BASE/20260608_Core_DL Post-Granularity Usability Assessment" "$ARCHIVE/"
mv "$BASE/20260608_Core_DL Usability Assessment Owner Perspective" "$ARCHIVE/"
mv "$BASE/20260608_Core_DL Visibility Architecture Assessment" "$ARCHIVE/"
mv "$BASE/20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4" "$ARCHIVE/"
# Item 13 (UMC diagnose) — SKIPPED unless flag resolved by owner
mv "$BASE/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage" "$ARCHIVE/"
mv "$BASE/20260607_Core_DL Phase 1 Retroactive Iris Review" "$ARCHIVE/"
mv "$BASE/20260607_Core_Deliverable Lifecycle Backlog Processing Batch 1 Proposal" "$ARCHIVE/"
mv "$BASE/20260607_Core_LC Naming Alignment Impact Assessment" "$ARCHIVE/"
mv "$BASE/20260607_Core_Learning Candidate Flag Triage Proposal" "$ARCHIVE/"
mv "$BASE/20260607_Core_team-tasks-id-76-assessment" "$ARCHIVE/"
```

If item 13 flag is resolved before execution, insert this line after item 12:
```bash
mv "$BASE/20260530_Core_UMC diagnose en aanbevelingen" "$ARCHIVE/"
```

### Phase B — Post-Move Verification

Confirm all moved folders are absent from `Deliverables/` and present in `Archive/`:

```bash
python3 -c "
import os
base = '/opt/myPKA/Deliverables'
archive = '/opt/myPKA/Deliverables/Archive'
moved = [
    '20260606_Core_LC Lifecycle Phase 1 Write-List v05',
    '20260607_Core_Auto-Processing Deliverable Lifecycle Discovery',
    '20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design',
    '20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal',
    '20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal',
    '20260607_Core_LC Batch 1 Write-List',
    '20260607_Core_LC Batch 2 Write-List',
    '20260607_Core_LC Triage Write-Plan',
    '20260608_Core_DL Post-Granularity Usability Assessment',
    '20260608_Core_DL Usability Assessment Owner Perspective',
    '20260608_Core_DL Visibility Architecture Assessment',
    '20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4',
    '20260604_Core_Deliverable Lifecycle Knowledge Processing Triage',
    '20260607_Core_DL Phase 1 Retroactive Iris Review',
    '20260607_Core_Deliverable Lifecycle Backlog Processing Batch 1 Proposal',
    '20260607_Core_LC Naming Alignment Impact Assessment',
    '20260607_Core_Learning Candidate Flag Triage Proposal',
    '20260607_Core_team-tasks-id-76-assessment',
]
# Add UMC diagnose if flag was resolved:
# moved.append('20260530_Core_UMC diagnose en aanbevelingen')

print('Folder | Source absent | Archive present | OK')
for f in moved:
    src_absent = not os.path.isdir(os.path.join(base, f))
    arc_present = os.path.isdir(os.path.join(archive, f))
    ok = src_absent and arc_present
    print(f'{f[:60]} | {src_absent} | {arc_present} | {ok}')
"
```

All rows must show `True | True | True`. Any False = halt and report.

### Phase C — Database Updates

Run only after Phase B passes completely.

```python
import sys, os
sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
from memory_config import get_dsn
import sqlite3

db_path = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

folders_to_archive = [
    '20260606_Core_LC Lifecycle Phase 1 Write-List v05',
    '20260607_Core_Auto-Processing Deliverable Lifecycle Discovery',
    '20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design',
    '20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal',
    '20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal',
    '20260607_Core_LC Batch 1 Write-List',
    '20260607_Core_LC Batch 2 Write-List',
    '20260607_Core_LC Triage Write-Plan',
    '20260608_Core_DL Post-Granularity Usability Assessment',
    '20260608_Core_DL Usability Assessment Owner Perspective',
    '20260608_Core_DL Visibility Architecture Assessment',
    '20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4',
    # '20260530_Core_UMC diagnose en aanbevelingen',  # add only if flag resolved
    '20260604_Core_Deliverable Lifecycle Knowledge Processing Triage',
    '20260607_Core_DL Phase 1 Retroactive Iris Review',
    '20260607_Core_Deliverable Lifecycle Backlog Processing Batch 1 Proposal',
    '20260607_Core_LC Naming Alignment Impact Assessment',
    '20260607_Core_Learning Candidate Flag Triage Proposal',
    '20260607_Core_team-tasks-id-76-assessment',
]

for folder in folders_to_archive:
    cur.execute(
        "UPDATE deliverable_lifecycle SET state_gl017='archived', owner_decision='archive', updated_at=datetime('now') WHERE artifact_name=?",
        (folder,)
    )
    print(f'Updated: {cur.rowcount} row(s) — {folder}')

conn.commit()
conn.close()
print('Done.')
```

Expected: 1 row updated per folder. If rowcount=0 for any item: flag for retroactive registration.

### Phase D — INDEX.md Regeneration

```bash
python3 "Team Knowledge/Core/Scripts/generate_deliverable_index.py"
```

Confirm the summary line shows a reduced pending-decisions count and increased archive count.

---

## 8. Post-Check Summary

| Check | Expected | Method |
|---|---|---|
| All 18 folders absent from `Deliverables/` | True | Phase B script |
| All 18 folders present in `Deliverables/Archive/` | True | Phase B script |
| deliverable_lifecycle: state='archived' for all 18 | 1 row updated each | Phase C output |
| INDEX.md regenerated, counts updated | Pending decisions reduced by 18 (or 19 if item 13 included) | Phase D output |
| Item 13 explicitly excluded unless flag resolved | Confirmed by executor | Manual check |

---

## 9. Remaining Open Items After Execution

After this batch executes (18 items), the following items remain unresolved from the original 29-item inventory:

| Item | Folder | Status |
|---|---|---|
| 5 | 20260607_Core_Deliverable Lifecycle Hardening Phase B Triage | Retained |
| 10 | 20260607_Core_SOP-019 LC-6 Execution Briefing Rule | Archived (done) |
| 11 | 20260608_Core_DL Hardening Phase C Proposal v01 | Retained |
| 12 | 20260608_Core_DL Hardening Task 85 Architecture Assessment | Archived (done) |
| 16 | 20260608_Core_DLH GL-001 and GL-004 Amendment Proposal v01 | Retained — awaiting authorization |
| 17 | 20260608_Core_DLH Task 86 Naming Standard Reassessment | Archived (done) |
| 18 | 20260604_Core_Review Gate Protocol Triage | Retained |
| 20 | 20260520_Core_Unified Memory Core architectuurschets | Archived (done) |
| 22 | 20260604_Core_Architecture Triage Memory Domain Routing | Retained |
| 24 | 20260604_Core_Graduation Candidate Parked - Context-mode MCP Fix | Retained — awaiting reactivation trigger |
| 13 | 20260530_Core_UMC diagnose en aanbevelingen | Pending flag resolution |

The 17-item Addendum (items with `state_gl017 = pending_lifecycle_decision`, not flagged DECISION PENDING) is out of scope for this batch. Those require a separate lifecycle pass.

---

Delivered on: 2026-06-08  
Delivered at: DL Pending Decision Inventory deliverable folder (G2 — file within existing deliverable)
