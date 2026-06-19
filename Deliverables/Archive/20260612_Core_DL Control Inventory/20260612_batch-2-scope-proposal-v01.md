# Batch 2 Scope Proposal v01

**Date:** 2026-06-12
**Author:** Governance Assistant
**Status:** Draft for Owner review
**Task reference:** team_task 94
**Placement:** G2 — file inside `20260612_Core_DL Control Inventory/`
**Basis:** Live inventory verification completed 2026-06-12 (read-only)
**Operating model reference:** `20260612_d-folder-operating-model-proposal-v02.md` (approved)

---

This file is a proposal only. No execution is authorized by this document.

Owner approval of this proposal authorizes the Batch 2 scope only.
It does not authorize archive execution, DB writes, routing, or any other action.
Execution requires a separate Batch 2 write plan, authorized by Owner.

---

## 1. Live Verification Confirmation

The following was confirmed in a read-only scan on 2026-06-12:

| Check | Result |
|---|---|
| Filesystem active D-folders | 34 |
| DB active records (`deliverable_lifecycle` WHERE state != 'archived') | 34 |
| Filesystem / DB match | Yes |
| Unregistered folders (filesystem active, not in DB) | 0 |

**Pilot archive integrity — 9 folders confirmed absent from active:**

| Lifecycle id | Folder | Status |
|---|---|---|
| 43 | `20260607_Core_DL Smoke Test Recovery Report` | Correctly absent |
| 44 | `20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal` | Correctly absent |
| 47 | `20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal` | Correctly absent |
| 54 | `20260607_Core_Deliverable Lifecycle Hardening Phase B Triage` | Correctly absent |
| 64 | `20260608_Core_UMC Archive Eligibility Chain Process Review` | Correctly absent |
| 65 | `20260608_Core_R1-R5 Prioritization Assessment` | Correctly absent |
| 66 | `20260608_Core_Phase 1 Proposal R1 R5 v01` | Correctly absent |
| 70 | `20260612_Core_DL Batch 1 Archive Execution Plan` | Correctly absent |
| 71 | `20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal` | Correctly absent |

---

## 2. Proposed Batch 2 Scope

**Exactly 3 folders.** All confirmed active on filesystem and in DB.
No GL-013 dependency. No live governance reference identified in pre-pilot inventory.

| # | Lifecycle id | Folder | Archive rationale |
|---|---|---|---|
| 1 | 60 | `20260608_Core_UMC Archive Eligibility Analysis 20260530` | UMC eligibility chain closed; no routing target; process artifact |
| 2 | 61 | `20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen` | P2/P5 governance triage chain closed; no routing target; process artifact |
| 3 | 68 | `20260608_Core_Phase 1 Proposal R1 R5 v02` | Phase 1 R1-R5 accepted; superseded work complete; process artifact |

**Batch size: 3** — within the 5-folder maximum defined in the approved operating model (Section 3.7).

---

## 3. Explicit Exclusions

The following folders are explicitly excluded from this Batch 2 scope:

| Lifecycle id | Folder | Reason for exclusion |
|---|---|---|
| 47 | `20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal` | Already archived (Pilot B retry) |
| 64 | `20260608_Core_UMC Archive Eligibility Chain Process Review` | Already archived (Pilot B retry) |
| 65 | `20260608_Core_R1-R5 Prioritization Assessment` | Already archived (Pilot B retry) |
| 66 | `20260608_Core_Phase 1 Proposal R1 R5 v01` | Already archived (Pilot B retry) |
| 62 | `20260608_Core_Retention Assessment P2 P5 UMC` | Frozen — GL-013 open signal in assessment.md |
| 63 | `20260608_Core_Write Proposal GL-013 Additions P2 P5` | Conditional — pending GL-013 implementation confirmation |
| All Category A | ids 12, 69 | Active work — must remain active |
| All Category C | ids 2, 3, 6, 7, 8, 18, 19, 45, 50, 52, 59 | Owner decision required before any action |
| All Category D | ids 10, 11, 13, 14, 16, 36, 40, 41, 42, 46, 53, 55, 56, 57, 58, 67 | Frozen pending per-item Owner review |

---

## 4. What Owner Approval of This Proposal Authorizes

Owner approval of this proposal authorizes **scope only**:

- The 3 folders listed in Section 2 are confirmed as the Batch 2 archive scope.
- No archive execution is authorized by this approval.
- No DB writes are authorized by this approval.
- No move commands are authorized by this approval.

**What approval does NOT authorize:**
- Archive execution (move to `Deliverables/Archive/`)
- DB state updates (`state_gl017 = 'archived'`)
- Any action on excluded folders
- GL-013 resolution
- Category C or D reclassification

---

## 5. Next Required Step After Owner Approval

After Owner approves this scope proposal:

**Step 1 — Batch 2 write plan (separate authorization required):**
Larry prepares a Batch 2 write plan file (G2: inside this containment folder) specifying:
- Exact move commands for each of the 3 folders
- Exact DB UPDATE statements for each of the 3 lifecycle records
- Stop rules per the approved operating model (Section 3.7)
- Execution report requirement

Owner reviews and explicitly authorizes the write plan before any execution begins.

**Step 2 — Batch 2 execution:**
After write plan authorization: Larry executes, writes an execution report (G2: inside
this containment folder), and reports completion to Owner.

**GL-013 handling:**
id 62 and id 63 remain excluded from all Batch 2 work regardless of step.
GL-013 resolution is a separate governance action not triggered by this batch.

---

## 6. Explicit Non-Actions Confirmation

The following actions were NOT performed during the preparation of this document:

- No archive of any D-folder
- No routing of any file
- No update to any `deliverable_lifecycle` record
- No `team_tasks` update
- No Batch 2 execution
- No dashboard work
- No new D-folder created
- No new folders created (this file is G2 inside the existing containment folder)
- No DB writes of any kind
- No modification to any existing D-folder
- No edit to any SOP, GL, or CLAUDE.md
- No modification to operating model proposal v01 or v02
- No GL-013 resolution
- No Learning Candidate triage
- No Deliverable Lifecycle sweep

---

Delivered on: 2026-06-12
Delivered at: `Deliverables/20260612_Core_DL Control Inventory/20260612_batch-2-scope-proposal-v01.md`
