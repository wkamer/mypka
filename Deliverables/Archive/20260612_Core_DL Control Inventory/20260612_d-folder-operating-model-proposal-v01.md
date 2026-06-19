# D-Folder Operating Model Proposal v01

**Date:** 2026-06-12
**Author:** Governance Assistant
**Status:** Draft for Owner review
**Task reference:** team_task 94
**Placement:** G2 — file inside `20260612_Core_DL Control Inventory/`

---

This file is a proposal only. No execution is authorized by this document.

---

## 1. Scope and Assumptions

**Scope:**
This proposal defines the operating model governing D-folder (deliverable folder) lifecycle
going forward: creation criteria, registration, routing rules, archive criteria, and Owner
decision gates. It also defines which categories of the current active D-folder population
are safe for archive pilots, which require Owner decision, which require routing before
archive, and which must remain active.

This proposal does not archive any folder, route any file, modify any database, or resolve
any open governance question.

**Assumptions:**
- The GL-017 Granularity Gate is active and authoritative for D-folder creation decisions.
- GL-021 (Write Authorization Boundary) governs all write actions including archive moves.
- The `deliverable_lifecycle` table in `team-knowledge.db` is the authoritative registry.
- Batch 2 is defined as the next batch of archive actions after Owner approval of this model.
- "Archive" means moving a D-folder to `Deliverables/Archive/` and updating `state_gl017`
  to `archived` in `deliverable_lifecycle`.

---

## 2. Current Confirmed State

**Active D-folder count: 34**

This count is confirmed as of 2026-06-12, post-Pilot-A and post-Pilot-B-retry.

| Reconciliation step | Count | Note |
|---|---|---|
| Inventory v01 baseline (pre-pilot) | 43 | Documented in `20260612_d-folder-operating-model-and-current-inventory-v01.md` |
| Pilot A archived | -4 | Lifecycle ids 47, 64, 65, 66 |
| Pilot B retry archived | -5 | Pilot B retry completed; one deviation noted post-SC-11 |
| **Current active** | **34** | Confirmed by Owner session brief |

**Lifecycle id 62 status:** unchanged. Remained active due to GL-013 open signal.
This is not resolved in this proposal. See Section 6.

**Zero unregistered folders.** All active D-folders have a `deliverable_lifecycle` record.

**Source document for full per-folder inventory:**
`20260612_Core_DL Control Inventory/20260612_d-folder-operating-model-and-current-inventory-v01.md`
That document contains the complete folder-by-folder table (43 folders at time of writing).
Current 34-folder state = that inventory minus the 9 archived in Pilot A and Pilot B retry.

---

## 3. Proposed D-Folder Operating Model

### 3.1 Creation Rule

A D-folder may only be created when the output passes the GL-017 G1 test.
G2 is the default: file inside an existing folder. A new folder requires an affirmative
answer to at least one of G1-A through G1-E. Uncertainty resolves to G2.

G1 criteria (any one sufficient):
- G1-A: Primary proposal independently approved or cited by Owner
- G1-B: Research brief, triage report, or architecture assessment
- G1-C: Formal closure report independently cited
- G1-D: Personal deliverable (PKM output)
- G1-E: Output explicitly approved by Owner as standalone

Process artifacts within an active cleanup cycle are always G2. No exceptions.
Dashboard scripts, monitoring tools, and reporting artifacts belong in
`Team Knowledge/Core/Scripts/` — not in D-folders — unless they independently pass G1.

### 3.2 Registration Requirement

Before creating any D-folder: INSERT one row into `deliverable_lifecycle` in `team-knowledge.db`.

Required fields at creation:
- `artifact_name`: exact folder name as created
- `artifact_type`: from canonical vocabulary
- `destination_domain`: Core / Personal / Kamer E-commerce / Geldstroom Regie
- `state_gl017`: `active`
- `workstream_code`: if known, otherwise NULL
- `owner_decision`: NULL

If the INSERT fails: note failure, create folder, add `team_tasks` row for retroactive
registration before session close. Registration is not optional.

### 3.3 Contents Requirement

Each D-folder must contain:
- The primary deliverable file(s)
- A `Delivered on:` and `Delivered at:` line at the bottom of each primary file

No required index file or README. Minimize folder overhead.

### 3.4 Versioning and Replacement

New version = new file inside the same D-folder (suffix: -v01, -v02, etc.).
New D-folder for a new version is only permitted if the new version independently passes G1.
When a file is superseded: add `Superseded by: [filename]` to the old file header.
The old file stays in the folder. Do not delete superseded versions.
Never create a parallel D-folder to hold a revision of existing work.

### 3.5 Routing Rules

Domain knowledge with permanent value must be routed before the D-folder is archived.

| Content type | Routing target |
|---|---|
| Personal domain knowledge | `PKM/My Life/Key Elements/` or `PKM/My Life/Projects/` |
| Kamer E-commerce knowledge | `Team Knowledge/Kamer E-commerce/` |
| Geldstroom Regie knowledge | `Team Knowledge/Geldstroom Regie/` |
| Core governance / SOPs / GLs | `Team Knowledge/Core/Guidelines/` or `SOPs/` |
| Process artifacts (write-lists, execution reports, proposals) | No routing target — archive directly |

Routing writes to a live system file. Owner confirmation required before each routing write.
Routing is a separate step from archiving. Sequence: route first, then confirm archive.

### 3.6 Archive Criteria

A D-folder may be archived when ALL of the following are true:
1. The underlying work or chain is definitively closed
2. Content has been routed to its permanent home, OR content type requires no routing
3. No live SOP, GL, or CLAUDE.md reference points to this folder as authoritative
4. Owner confirmation received for this specific folder or batch

### 3.7 Archive Batch Rules

- Maximum 5 folders per batch unless Owner explicitly approves a larger count.
- Halt the batch if any of the following occur:
  - A folder to be archived is referenced by a live SOP, GL, or CLAUDE.md
  - A DB anomaly is found (folder not matching lifecycle record)
  - Content is found that indicates the chain was not closed (open items, unresolved decisions)
  - Any GL-013 or other open governance signal is encountered in the folder
- A deviation from any stop rule must be reported to Owner before the batch continues.
- Batch completion requires a written execution report (G2: file inside containment folder).

### 3.8 Owner Decision Gates

Owner decision required before:
- Any routing write to a live system file
- Any archive of a folder where `owner_decision` is NULL and status is ambiguous
- Any batch exceeding 5 folders
- Any reclassification of a `registered_but_unclear` folder

Owner decision NOT required for:
- Read-only inventory and classification
- Proposing a next batch (this document)
- DB registration at folder creation (Larry executes as administration)

---

## 4. Folder Categories Going Forward

Based on the inventory in `20260612_d-folder-operating-model-and-current-inventory-v01.md`
and updated for the current 34-folder state, four categories apply going forward.

### Category A: Active Work — Must Remain Active

These folders are in live use. No action permitted.

| Folder | Reason |
|---|---|
| `20260604_Core_Graduation Candidate Parked - Context-mode MCP Fix` | Owner explicitly retained |
| `20260612_Core_DL Control Inventory` | Current containment area (self-referential) |

**Count: 2**

### Category B: Safe for Archive Pilot — Owner Confirmation Sufficient

These are closed process artifacts. No routing target. No live governance reference.
Owner batch confirmation is sufficient to archive.

Proposed as Batch 2 Sub-batch A (6 folders):

| Folder | Archive rationale |
|---|---|
| `20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal` | Phase A artifact; Phase C active; A definitively closed |
| `20260607_Core_Deliverable Lifecycle Hardening Phase B Triage` | Phase B complete; superseded by Phase C |
| `20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal` | Smoke test complete; recovery report exists |
| `20260607_Core_DL Smoke Test Recovery Report` | Paired with smoke test; chain closed |
| `20260612_Core_DL Batch 1 Archive Execution Plan` | Batch 1 complete; pure process artifact |
| `20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal` | Superseded by this operating model document |

**Count: 6**

Proposed as Batch 2 Sub-batch B (8 folders) — requires Sub-batch A confirmed first, and
GL-013 additions implementation confirmed:

| Folder | Archive rationale |
|---|---|
| `20260608_Core_UMC Archive Eligibility Analysis 20260530` | UMC chain closed |
| `20260608_Core_UMC Archive Eligibility Chain Process Review` | Paired with above |
| `20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen` | P2/P5 chain closed |
| `20260608_Core_Retention Assessment P2 P5 UMC` | Chain closed |
| `20260608_Core_Write Proposal GL-013 Additions P2 P5` | Requires GL-013 confirmation first |
| `20260608_Core_R1-R5 Prioritization Assessment` | R1-R5 chain closed |
| `20260608_Core_Phase 1 Proposal R1 R5 v01` | Superseded by v02 |
| `20260608_Core_Phase 1 Proposal R1 R5 v02` | Phase 1 accepted — confirm before archiving |

**Count: 8**

### Category C: Requires Owner Decision Before Any Action

These require an explicit Owner decision before routing or archiving.
No autonomous action on these folders.

**Routing required first (5 folders — domain knowledge):**

| Folder | Decision required |
|---|---|
| `20260513_Geldstroom Regie_One-pager methodiek` | Route to GR knowledge base, or archive without routing? |
| `20260519_Kamer E-commerce_Remy Research Week 21` | Route to KE knowledge base, or archive without routing? |
| `20260530_Personal_Blueprint weekschema en oefeningen` | Route to PKM Personal, or archive without routing? |
| `20260531_Personal_Health Monitoring Schema` | Route to PKM Personal, or archive without routing? |
| `20260531_Personal_Morning Mobility Routine` | Route to PKM Personal, or archive without routing? |

**Status confirmation required (6 folders):**

| Folder | Decision required |
|---|---|
| `20260607_Core_Auto-Processing Deliverable Lifecycle Discovery` | Continue, park, or archive? |
| `20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design` | Depends on decision above (same chain) |
| `20260607_Core_Deliverable Lifecycle Backlog Processing Batch 1 Proposal` | Superseded by actual Batch 1, or still open? |
| `20260608_Core_DL Pending Decision Inventory` | Were all 4 recommendations resolved? |
| `20260608_Core_DLH GL-001 and GL-004 Amendment Proposal v01` | Implemented, parked, or superseded? |
| `20260608_Core_DLH_GL-001_GL-004_Proposal_Review` | Paired with above — same decision |

**Count: 11**

### Category D: Registered but Unclear — Frozen Until Per-Item Owner Review

These have audit value as source documents for live governance rules, Iris review artifacts,
or authoritative decision records. Final disposition is not decided. No autonomous action.

| Folder | Retention reason |
|---|---|
| `20260604_Core_Architecture Triage Memory Domain Routing` | Source for GL-015 (referenced in CLAUDE.md) |
| `20260604_Core_Deliverable Lifecycle Knowledge Processing Triage` | Source for SOP-017 v01/v02 |
| `20260604_Core_Review Gate Protocol Triage` | Source for SOP-016 Review Gate Protocol |
| `20260605_Core_Lifecycle Decision Record GL-017 SOP-017` | Authoritative decision record (DB state stale) |
| `20260605_Core_SOP-017 Amendment Lifecycle Execution` | Execution report for SOP-017 amendment |
| `20260607_Core_DL Phase 1 Retroactive Iris Review` | Iris review artifact — governance retention |
| `20260607_Core_Final Governance State Verification` | Point-in-time governance snapshot |
| `20260607_Core_Learning Candidate Flag Triage Proposal` | Likely source for SOP-019 behavioral rules |
| `20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards` | Post-check script standards |
| `20260607_Core_team-tasks-id-76-assessment` | Assessment artifact; chain unclear |
| `20260608_Core_DL Granularity Assessment` | GL-017 amendment source; DB state stale |
| `20260608_Core_DL Hardening Phase C Proposal v01` | Phase C may still be active — do not touch |
| `20260608_Core_DL Post-Granularity Usability Assessment` | Informed Phase C design; audit value |
| `20260608_Core_DL Usability Assessment Owner Perspective` | Paired with above |
| `20260608_Core_DL Visibility Architecture Assessment` | May be referenced by future dashboard work |
| `20260608_Core_GL-013 Reconciliation Analysis` | Source for GL-013 additions proposal |

**Count: 16**

Note on lifecycle id 62 (`20260608_Core_GL-013 Reconciliation Analysis`): this folder
remained active due to a GL-013 open signal. See Section 6 for handling approach.

---

## 5. Category Summary

| Category | Label | Count | Action |
|---|---|---|---|
| A | Active Work — Must Remain Active | 2 | No action |
| B | Safe for Archive Pilot | 14 | Owner batch confirm sufficient |
| C | Requires Owner Decision | 11 | Decision required before any action |
| D | Registered but Unclear — Frozen | 16 | Per-item Owner review required |
| **Total active** | | **43** | (pre-pilot inventory baseline) |

**Post-pilot state (current):** 34 active. The 9 archived folders (Pilot A ids 47, 64, 65, 66
and Pilot B retry) are removed from the above categories. The per-item mapping in the
inventory document reflects the 43-folder pre-pilot baseline; individual category counts
above may be slightly lower in the live state. No material change to categories B, C, D.

---

## 6. GL-013 and Lifecycle id 62 — Handling Approach

**Lifecycle id 62** is `20260608_Core_GL-013 Reconciliation Analysis`.
It was held out of Pilot B retry because a GL-013 open signal was detected.

**This proposal does not resolve GL-013.**

The handling approach going forward:

1. GL-013 resolution is a separate governance action with its own authorization gate.
2. Lifecycle id 62 remains in Category D (frozen) until GL-013 status is explicitly confirmed.
3. If GL-013 is confirmed fully implemented and closed: id 62 may be reclassified to
   Category B (safe for archive) in the next inventory update. This requires Owner confirmation
   of GL-013 status, not autonomous reclassification.
4. If GL-013 remains open or partially open: id 62 must remain frozen until GL-013 is resolved.
5. No Batch 2 action touches id 62 unless its category is explicitly updated by Owner.

This approach isolates the GL-013 question from the broader cleanup progress. The 33 other
active folders can proceed through the operating model without waiting for GL-013.

---

## 7. Exact Approval Needed from Owner Before Batch 2

Before any Batch 2 archive action may begin, Owner must explicitly confirm:

**Required approvals:**

1. **Operating model approval:** "I approve the D-folder operating model as described in this
   proposal (v01). The four categories (A, B, C, D) and the archive criteria in Section 3.6
   are the authoritative operating rules going forward."

2. **Batch 2 Sub-batch A scope approval:** "I confirm the 6 folders listed in Category B
   Sub-batch A are safe to archive. Proceed with Sub-batch A."

3. **GL-013 isolation confirmed:** "I confirm lifecycle id 62 is frozen and will not be
   touched in Batch 2 until GL-013 status is separately resolved."

**Optional but recommended before Sub-batch A:**
- Confirm whether Phase C of DLH is still active (affects classification of
  `20260608_Core_DL Hardening Phase C Proposal v01`).

**Not required before Sub-batch A (may proceed after A):**
- GL-013 resolution
- Domain knowledge routing decisions (Category C, routing-required items)
- Per-item review of Category D folders

---

## 8. Smallest Safe Next Step After Owner Approval

After Owner provides the three approvals listed in Section 7:

1. Larry prepares a Batch 2 Sub-batch A write plan (G2: file inside this containment folder).
2. Write plan lists the 6 folders, the DB update for each, and the move commands.
3. Owner reviews and authorizes the write plan.
4. Larry executes Sub-batch A: move 6 folders to `Deliverables/Archive/`, update 6
   `deliverable_lifecycle` records to `state_gl017 = 'archived'`.
5. Larry writes an execution report (G2: file inside this containment folder).
6. Larry reports completion to Owner.

Sub-batch B does not start until Sub-batch A is confirmed complete and GL-013
additions implementation is verified.

---

## 9. Explicit Non-Actions Confirmation

The following actions were NOT performed during the preparation of this document:

- No archive of any D-folder
- No routing of any file
- No update to any `deliverable_lifecycle` record
- No `team_tasks` update
- No Batch 2 execution
- No dashboard work
- No new D-folder created
- No new folders created
- No DB writes of any kind
- No modification to any existing D-folder
- No edit to any SOP, GL, or CLAUDE.md
- No GL-013 resolution
- No Learning Candidate triage
- No Deliverable Lifecycle sweep

---

Delivered on: 2026-06-12
Delivered at: `Deliverables/20260612_Core_DL Control Inventory/20260612_d-folder-operating-model-proposal-v01.md`
