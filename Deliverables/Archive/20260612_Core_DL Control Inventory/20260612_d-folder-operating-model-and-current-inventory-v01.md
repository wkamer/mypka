# D-Folder Operating Model and Current Inventory — v01

**Date:** 2026-06-12
**Prepared by:** Larry, Team Orchestrator
**Task reference:** team_task 94
**Type:** Inventory and operating model proposal — read-only
**Scope:** All active D-folders in `Deliverables/` as of 2026-06-12, post-Batch-1
**Placement:** G2 — file inside `20260612_Core_DL Control Inventory/`

**Read-only declaration:** No files, folders, databases, lifecycle records, or indexes were
modified during the preparation of this document. No archive actions. No routing actions.
No Learning Candidate triage. No Batch 2 execution. No new folders created.
No dashboard work performed.

---

## 1. Current D-Folder Count

**Confirmed active D-folders as of 2026-06-12: 43**

The task brief estimated approximately 46. Actual count confirmed by filesystem scan: 43.

**Count reconciliation:**

| Step | Count | Note |
|---|---|---|
| Baseline at v02 inventory | 55 | All registered, 0 gaps |
| Batch 1 archived (LC chain + naming artifact) | -15 | Executed prior to this task |
| New 20260612 folders registered post-v02 | +3 | DL Control Inventory already in v02; 2 new post-batch |
| **Current active** | **43** | Confirmed via filesystem + lifecycle DB |

**Lifecycle DB confirmation:** `SELECT COUNT(*) FROM deliverable_lifecycle WHERE state_gl017 != 'archived'` returns 43.
All 43 active D-folders are registered in `deliverable_lifecycle`. Zero unregistered folders.

**DB anomaly noted (no action in this task):** 4 IDs (69-72) vs total record count of 68 — one record
was deleted (the Batch 2 Process Artifacts Archive Proposal, already correctly G2-filed to containment
area and marked archived in DB with `owner_decision = 'misclassified GL-017: G2 artifact, file moved to
20260612_Core_DL Control Inventory'`).

---

## 2. Folder-by-Folder Inventory Table

**Control status definitions used below:**

| Status | Meaning |
|---|---|
| `active_work` | In active use — do not touch |
| `ready_for_archive` | Closed chain, no routing target, Owner confirmation needed before moving |
| `owner_decision_needed` | Requires explicit Owner decision: route, park, or archive |
| `registered_but_unclear` | Registered in DB; retain for audit; final disposition not yet decided |

---

### 2A. Active Work (2)

| # | Folder | DB state | Lifecycle record | Proposed control status | Next action | Owner decision needed | Risk/ambiguity |
|---|---|---|---|---|---|---|---|
| 1 | `20260604_Core_Graduation Candidate Parked - Context-mode MCP Fix` | active, retain | Yes (id 12) | `active_work` | None — Owner explicitly retained | No | None |
| 2 | `20260612_Core_DL Control Inventory` | active | Yes (id 69) | `active_work` | None — current containment area | No | Self-referential; contains this file |

---

### 2B. Ready for Archive (14)

These are closed process artifacts. No routing target. Safe to archive after Owner confirmation.
Organized by chain.

**DLH Phase A/B process artifacts (4):**

| # | Folder | DB state | Lifecycle record | Proposed control status | Next action | Owner decision needed | Risk/ambiguity |
|---|---|---|---|---|---|---|---|
| 3 | `20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | Phase A artifact; Phase C now active |
| 4 | `20260607_Core_Deliverable Lifecycle Hardening Phase B Triage` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | Phase B complete; superseded by Phase C |
| 5 | `20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | Smoke test complete; recovery report exists |
| 6 | `20260607_Core_DL Smoke Test Recovery Report` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | Paired with smoke test proposal above |

**UMC Archive Eligibility chain (8):**

| # | Folder | DB state | Lifecycle record | Proposed control status | Next action | Owner decision needed | Risk/ambiguity |
|---|---|---|---|---|---|---|---|
| 7 | `20260608_Core_UMC Archive Eligibility Analysis 20260530` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | Chain complete; no live dependency |
| 8 | `20260608_Core_UMC Archive Eligibility Chain Process Review` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | Paired process review; same chain |
| 9 | `20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | P2/P5 governance chain closed |
| 10 | `20260608_Core_Retention Assessment P2 P5 UMC` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | Retention assessment complete |
| 11 | `20260608_Core_Write Proposal GL-013 Additions P2 P5` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | GL-013 additions were a proposal; confirm implemented |
| 12 | `20260608_Core_R1-R5 Prioritization Assessment` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | R1-R5 prioritization exercise complete |
| 13 | `20260608_Core_Phase 1 Proposal R1 R5 v01` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | v01 superseded by v02 |
| 14 | `20260608_Core_Phase 1 Proposal R1 R5 v02` | pending | Yes | `ready_for_archive` | Archive (Owner confirm) | Yes — batch confirm | Phase 1 R1-R5 proposal; confirm accepted |

**Post-batch process artifacts (2):**

| # | Folder | DB state | Lifecycle record | Proposed control status | Next action | Owner decision needed | Risk/ambiguity |
|---|---|---|---|---|---|---|---|
| 15 | `20260612_Core_DL Batch 1 Archive Execution Plan` | active | Yes (id 70) | `ready_for_archive` | Archive after operating model is approved | Yes | Batch 1 complete; no live dependency |
| 16 | `20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal` | active | Yes (id 71) | `ready_for_archive` | Archive after operating model is approved; superseded by this document | Yes | DB note flags GL-017 correction pending |

---

### 2C. Owner Decision Needed (11)

These require an explicit Owner decision before any action. Either they contain genuine
domain knowledge needing routing, or their status is ambiguous.

| # | Folder | DB state | Lifecycle record | Proposed control status | Decision required | Owner decision needed | Risk/ambiguity |
|---|---|---|---|---|---|---|---|
| 17 | `20260513_Geldstroom Regie_One-pager methodiek` | pending | Yes | `owner_decision_needed` | Route to GR knowledge base, or archive | Yes | Domain knowledge; routing plan approved but not yet executed |
| 18 | `20260519_Kamer E-commerce_Remy Research Week 21` | pending | Yes | `owner_decision_needed` | Route to KE knowledge base, or archive | Yes | Domain knowledge; routing plan approved but not yet executed |
| 19 | `20260530_Personal_Blueprint weekschema en oefeningen` | pending | Yes | `owner_decision_needed` | Route to PKM Personal, or archive | Yes | Domain knowledge; routing plan approved but not yet executed |
| 20 | `20260531_Personal_Health Monitoring Schema` | pending | Yes | `owner_decision_needed` | Route to PKM Personal, or archive | Yes | Domain knowledge; routing plan approved but not yet executed |
| 21 | `20260531_Personal_Morning Mobility Routine` | pending | Yes | `owner_decision_needed` | Route to PKM Personal, or archive | Yes | Domain knowledge; routing plan approved but not yet executed |
| 22 | `20260607_Core_Auto-Processing Deliverable Lifecycle Discovery` | pending | Yes | `owner_decision_needed` | Continue, park, or archive; future work not yet started | Yes | Proposal for unimplemented feature |
| 23 | `20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design` | pending | Yes | `owner_decision_needed` | Depends on decision for item 22 above; same chain | Yes | Paired with auto-processing discovery |
| 24 | `20260607_Core_Deliverable Lifecycle Backlog Processing Batch 1 Proposal` | pending | Yes | `owner_decision_needed` | Confirm: superseded by actual Batch 1 execution, or still open? | Yes | Unclear if this was the source for Batch 1 or a separate proposal |
| 25 | `20260608_Core_DL Pending Decision Inventory` | active | Yes | `owner_decision_needed` | Confirm: were all 4 recommendations resolved? | Yes | DB state: active, no owner_decision; session 192 reported 0 pending |
| 26 | `20260608_Core_DLH GL-001 and GL-004 Amendment Proposal v01` | pending | Yes | `owner_decision_needed` | Confirm: implemented, parked, or superseded? | Yes | DLH naming task archived; unclear if proposal was executed |
| 27 | `20260608_Core_DLH_GL-001_GL-004_Proposal_Review` | pending | Yes | `owner_decision_needed` | Paired with item 26; same decision | Yes | Review paired with amendment proposal above |

---

### 2D. Registered but Unclear — Retain for Audit (16)

These have audit value as source documents for live governance rules, Iris review artifacts,
or authoritative decision records. Do not archive without explicit Owner review per item.
Final disposition (permanent retain, route, or eventually archive) is not yet decided.

| # | Folder | DB state | Lifecycle record | Proposed control status | Notes | Owner decision needed |
|---|---|---|---|---|---|---|
| 28 | `20260604_Core_Architecture Triage Memory Domain Routing` | pending | Yes | `registered_but_unclear` | Source for GL-015 (referenced in CLAUDE.md); ongoing audit value | Eventually |
| 29 | `20260604_Core_Deliverable Lifecycle Knowledge Processing Triage` | pending | Yes | `registered_but_unclear` | Source for SOP-017 v01/v02; audit trail for SOP creation | Eventually |
| 30 | `20260604_Core_Review Gate Protocol Triage` | pending | Yes | `registered_but_unclear` | Source for SOP-016 Review Gate Protocol; implemented governance rule | Eventually |
| 31 | `20260605_Core_Lifecycle Decision Record GL-017 SOP-017` | active (stale) | Yes | `registered_but_unclear` | Authoritative decision record; DB state not updated; content complete per session 192 | DB update needed |
| 32 | `20260605_Core_SOP-017 Amendment Lifecycle Execution` | pending | Yes | `registered_but_unclear` | Execution report for SOP-017 Source Folder Closure Amendment; permanent audit trail | Eventually |
| 33 | `20260607_Core_DL Phase 1 Retroactive Iris Review` | pending | Yes | `registered_but_unclear` | Iris review artifact — governance: Iris reviews must be persisted | Retain long-term |
| 34 | `20260607_Core_Final Governance State Verification` | pending | Yes | `registered_but_unclear` | Point-in-time governance snapshot; historical reference value | Eventually |
| 35 | `20260607_Core_Learning Candidate Flag Triage Proposal` | pending | Yes | `registered_but_unclear` | Likely source for SOP-019 behavioral rules; conservative retention | Eventually |
| 36 | `20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards` | pending | Yes | `registered_but_unclear` | Post-check script standards; possibly referenced by active SOPs | Verify reference |
| 37 | `20260607_Core_team-tasks-id-76-assessment` | pending | Yes | `registered_but_unclear` | Assessment artifact; chain unclear without reading content | Clarify chain |
| 38 | `20260608_Core_DL Granularity Assessment` | active (stale) | Yes | `registered_but_unclear` | DB state stale; implementation complete per session 192; GL-017 amendment source | DB update needed |
| 39 | `20260608_Core_DL Hardening Phase C Proposal v01` | pending | Yes | `registered_but_unclear` | Phase C may still be in progress; may be `active_work` — verify before touching | Phase C status unclear |
| 40 | `20260608_Core_DL Post-Granularity Usability Assessment` | pending | Yes | `registered_but_unclear` | Usability assessment informed Phase C design; audit value | Eventually |
| 41 | `20260608_Core_DL Usability Assessment Owner Perspective` | pending | Yes | `registered_but_unclear` | Owner perspective artifact; paired with item 40 above | Eventually |
| 42 | `20260608_Core_DL Visibility Architecture Assessment` | pending | Yes | `registered_but_unclear` | Visibility architecture for dashboard work; may be referenced by future work | Verify reference |
| 43 | `20260608_Core_GL-013 Reconciliation Analysis` | pending | Yes | `registered_but_unclear` | GL-013 reconciliation; source for GL-013 additions proposal | Eventually |

---

## 3. Control Status Summary

| Control status | Count |
|---|---|
| `active_work` | 2 |
| `ready_for_archive` | 14 |
| `owner_decision_needed` | 11 |
| `registered_but_unclear` | 16 |
| **Total active D-folders** | **43** |
| Unregistered | 0 |
| Invalid or duplicate | 0 |

---

## 4. D-Folder Operating Model

Minimal rules. No governance expansion. Each rule below prevents a known failure mode.

### 4.1 When a D-Folder May Be Created

A D-folder may only be created when the output passes the GL-017 G1 test: it satisfies at
least one of G1-A through G1-E. G2 is the default — file inside an existing folder.

**G1 criteria (any one sufficient):**
- G1-A: Primary proposal independently approved or cited by Owner
- G1-B: Research brief, triage report, or architecture assessment
- G1-C: Formal closure report independently cited
- G1-D: Personal deliverable (PKM output)
- G1-E: Output explicitly approved by Owner as standalone

Process artifacts within an active cleanup cycle are always G2. No exceptions.
When in doubt: G2.

### 4.2 Required Registration

Before creating any D-folder: INSERT one row into `deliverable_lifecycle` in `team-knowledge.db`.

Fields required at creation:
- `artifact_name`: exact folder name
- `artifact_type`: from canonical vocabulary
- `state_gl017`: `active`
- `workstream_code`: if known (otherwise NULL)
- `owner_decision`: NULL at creation

If INSERT fails: note failure, create folder, add team_tasks row for retroactive registration
before session close.

### 4.3 Required Contents

Each D-folder must contain:
- At minimum: the primary deliverable file(s)
- A `Delivered on:` and `Delivered at:` line at the bottom of the primary file

No required index file. No required README. Minimize folder overhead.

### 4.4 Versioning and Replacement Rules

New version = new file inside the same D-folder (v01, v02, etc.).
New D-folder for a new version is only permitted if the new version independently qualifies as G1.

When a new version supersedes an old file: add a `Superseded by: [filename]` line to the old
file header. The old file stays in the folder — do not delete it.

Never create a parallel D-folder to hold a revised version of existing work.

### 4.5 Routing Rules

Domain knowledge with permanent value must be routed before the D-folder is archived:

| Content type | Routing target |
|---|---|
| Personal domain knowledge | `PKM/My Life/Key Elements/` or `PKM/My Life/Projects/` |
| Kamer E-commerce knowledge | `Team Knowledge/Kamer E-commerce/` |
| Geldstroom Regie knowledge | `Team Knowledge/Geldstroom Regie/` |
| Core governance / SOPs / GLs | `Team Knowledge/Core/Guidelines/` or `SOPs/` |
| Process artifacts (write-lists, exec reports) | No routing target — archive directly |

Routing writes to a live system file. Owner confirmation required before each routing write.

### 4.6 Archive Criteria

A D-folder may be archived when ALL of the following are true:
1. The underlying work or chain is definitively closed
2. Content has been routed to its permanent home, OR no routing target exists (process artifact)
3. No live governance rule, SOP, or CLAUDE.md reference points to this folder as authoritative
4. Owner confirmation received

### 4.7 Closure Criteria

A D-folder is closed when:
- Owner has explicitly confirmed the work is done, AND
- All derived actions from the folder are complete, AND
- Routing (if required) is complete

Closure does not automatically trigger archiving. Archive is a separate step requiring Owner confirm.

### 4.8 Owner Decision Gates

Owner decision is required before:
- Any routing write to a live system file
- Any archive of a folder with `owner_decision = NULL` and ambiguous status
- Any batch archive exceeding 5 folders
- Any change to `registered_but_unclear` folder status

Owner decision is NOT required for:
- Read-only inventory and classification (this document)
- Proposing a next batch (this document)
- DB registration at folder creation (Larry executes as administration)

### 4.9 Stop Rules — Folder Creep Prevention

**Stop rule 1:** No new D-folder for any process artifact produced within an active cleanup cycle.
All such outputs are G2 — file inside the active containment folder.

**Stop rule 2:** Maximum 5 folders per archive batch unless Owner explicitly approves a larger batch.
Rationale: larger batches create irreversible state before errors can be caught.

**Stop rule 3:** Halt batch if any of the following occur:
- A folder to be archived contains a file referenced by a live SOP, GL, or CLAUDE.md
- A DB anomaly is discovered (folder in batch not matching lifecycle record)
- Content found that indicates the chain was not closed (open items, unresolved decisions)

**Stop rule 4:** The `registered_but_unclear` group is frozen until Owner explicitly reviews each item.
No autonomous reclassification. No silent archiving.

**Stop rule 5:** No D-folder may be created for a dashboard, monitoring system, or reporting tool
unless it independently passes G1. Dashboards and scripts belong in `Team Knowledge/Core/Scripts/`
or the relevant integration folder.

---

## 5. Recommended Next Cleanup Batch

**Proposed Sub-batch A (6 folders) — smallest safe next action:**

| # | Folder | Rationale |
|---|---|---|
| 1 | `20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal` | Phase A artifact; Phase C now active; Phase A definitively closed |
| 2 | `20260607_Core_Deliverable Lifecycle Hardening Phase B Triage` | Phase B artifact; Phase C supersedes it |
| 3 | `20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal` | Smoke test complete; recovery report exists |
| 4 | `20260607_Core_DL Smoke Test Recovery Report` | Paired with smoke test; chain closed |
| 5 | `20260612_Core_DL Batch 1 Archive Execution Plan` | Batch 1 complete; execution plan is pure process artifact |
| 6 | `20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal` | Superseded by this operating model deliverable |

**Why these 6 are safest:**
- DLH Phase A/B folders: unambiguously superseded by Phase C. Phase C Proposal v01 exists in the
  active folder. No live governance rule points back to Phase A/B artifacts.
- Post-batch 20260612 folders: Batch 1 is complete. These folders document a completed action.
  Both are registered. No routing target.
- All 6 are process artifacts. No routing required. Owner confirmation sufficient.

**Proposed Sub-batch B (8 folders) — after Sub-batch A confirmed:**

| # | Folder | Rationale |
|---|---|---|
| 7 | `20260608_Core_UMC Archive Eligibility Analysis 20260530` | UMC chain closed |
| 8 | `20260608_Core_UMC Archive Eligibility Chain Process Review` | Paired with above |
| 9 | `20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen` | P2/P5 chain closed |
| 10 | `20260608_Core_Retention Assessment P2 P5 UMC` | Chain closed |
| 11 | `20260608_Core_Write Proposal GL-013 Additions P2 P5` | Confirm GL-013 implemented before archiving |
| 12 | `20260608_Core_R1-R5 Prioritization Assessment` | R1-R5 chain closed |
| 13 | `20260608_Core_Phase 1 Proposal R1 R5 v01` | Superseded by v02 |
| 14 | `20260608_Core_Phase 1 Proposal R1 R5 v02` | Confirm Phase 1 accepted before archiving |

**Prerequisite for Sub-batch B:** Owner confirms Sub-batch A complete and GL-013 additions were
implemented. Do not merge A and B into one action.

**Do not call this "Batch 2" unless Owner explicitly approves that label.**
These are proposed sub-batches for planning purposes only.

---

## 6. Open Owner Decisions Required

Before any cleanup action can proceed, the following decisions are pending:

**Immediate (block cleanup):**
1. Approve Sub-batch A proposal (6 folders listed above)
2. Confirm whether GL-013 additions were implemented (prerequisite for Sub-batch B)

**Domain knowledge routing (items 17-21 in inventory):**
3. Route GR One-pager methodiek to GR knowledge base, or archive
4. Route Kamer E-commerce Remy Research Week 21 to KE knowledge base, or archive
5. Route Personal Blueprint weekschema to PKM, or archive
6. Route Personal Health Monitoring Schema to PKM, or archive
7. Route Personal Morning Mobility Routine to PKM, or archive

**Status confirmation (items 22-27 in inventory):**
8. Auto-Processing Discovery and Phase 1 Design: continue, park, or archive?
9. Deliverable Lifecycle Backlog Processing Batch 1 Proposal: superseded or still open?
10. DL Pending Decision Inventory: were all 4 recommendations resolved?
11. DLH GL-001/GL-004 Amendment Proposal: implemented, parked, or superseded?

**Retain-for-audit (item 39 in inventory — blocking classification):**
12. Is Phase C of DLH still in progress? If yes, `20260608_Core_DL Hardening Phase C Proposal v01`
    must be reclassified as `active_work`. If Phase C is complete, it stays `registered_but_unclear`.

---

## 7. Explicit Non-Actions Confirmation

The following actions were NOT performed during the preparation of this deliverable:

- No archive of any D-folder
- No routing of any file to PKM, Team Knowledge, or any domain knowledge base
- No update to any `deliverable_lifecycle` record
- No Learning Candidate triage
- No Batch 2 execution
- No dashboard work
- No new D-folder created
- No new files created other than this deliverable
- No DB writes of any kind
- No modification to any existing D-folder
- No edit to any SOP, GL, or CLAUDE.md

This deliverable is a read-only inventory and proposal document only.

---

Delivered on: 2026-06-12
Delivered at: `Deliverables/20260612_Core_DL Control Inventory/20260612_d-folder-operating-model-and-current-inventory-v01.md`
