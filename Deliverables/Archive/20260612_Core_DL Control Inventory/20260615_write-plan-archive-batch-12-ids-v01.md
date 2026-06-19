# Write Plan — Archive Batch 12 IDs (DL Control Cleanup)

**Date:** 2026-06-15
**Prepared by:** Larry, Team Orchestrator
**Status:** Awaiting Owner authorization for execution
**Scope:** Folder moves + DB updates for exactly 12 deliverable_lifecycle items
**Basis:** Quick scan classification — no remaining active operational need confirmed

---

## 1. Items in Scope

| ID | Folder name | Current state_gl017 | Current owner_decision |
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

## 4. Execution Steps

### Step A — Folder Moves (12 moves, sequential)

Execute each mv in order. After each move: verify the folder no longer exists at source and exists at destination. If any single move fails: stop immediately, do not proceed to remaining moves or Step B, report to Owner.

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

### Step B — DB Update (only after all 12 moves succeed)

```sql
UPDATE deliverable_lifecycle
SET state_gl017 = 'archived',
    owner_decision = 'archived_cleanup_no_active_need'
WHERE id IN (10, 11, 13, 16, 36, 40, 41, 42, 55, 56, 57, 59);
```

**Batch-stop rule:** if rowcount != 12, rollback the UPDATE immediately and report to Owner before any further action.

---

## 5. Post-Execution Verification

### 5A — Folder check

Confirm all 12 folders are present in `Deliverables/Archive/` and absent from `Deliverables/`.

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
  [ -d "Deliverables/Archive/$f" ] && echo "OK: $f" || echo "MISSING: $f"
  [ -d "Deliverables/$f" ] && echo "STILL AT SOURCE: $f"
done
```

### 5B — DB check

```sql
SELECT id, state_gl017, owner_decision
FROM deliverable_lifecycle
WHERE id IN (10, 11, 13, 16, 36, 40, 41, 42, 55, 56, 57, 59)
ORDER BY id;
```

Expected: all 12 rows show `state_gl017 = 'archived'`, `owner_decision = 'archived_cleanup_no_active_need'`.

---

## 6. Out of Scope

- No content edits to any file inside any folder
- No borging writes
- No routing
- No Learning Candidate writes
- No Deliverable Lifecycle sweep
- No GL/SOP/CLAUDE.md edits
- No dashboard work
- No new D-folder

---

## 7. Execution Authorization

Owner must explicitly authorize execution before any folder move or DB update is performed.
This write plan does not constitute authorization.

---

*Delivered on: 2026-06-15*
*Delivered at: Deliverables/20260612_Core_DL Control Inventory/20260615_write-plan-archive-batch-12-ids-v01.md*
