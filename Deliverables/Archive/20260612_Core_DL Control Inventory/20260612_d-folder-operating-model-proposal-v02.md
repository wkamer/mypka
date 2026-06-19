# D-Folder Operating Model Proposal v02

**Date:** 2026-06-12
**Author:** Governance Assistant
**Status:** Draft for Owner review
**Supersedes:** `20260612_d-folder-operating-model-proposal-v01.md` for Owner review and audit interpretation.
v01 is preserved unchanged as a historical artifact. v01 contained factual errors in the
pilot archive history and in the identity of lifecycle id 62. Do not use v01 for decisions.
**Task reference:** team_task 94
**Placement:** G2 — file inside `20260612_Core_DL Control Inventory/`

---

This file is a proposal only. No execution is authorized by this document.

---

## 1. Scope and Assumptions

**Scope:**
This proposal defines the operating model governing D-folder (deliverable folder) lifecycle
going forward: creation criteria, registration, routing rules, archive criteria, and Owner
decision gates. It identifies the current live D-folder state, the folder categories, and
the prerequisites that must be satisfied before Batch 2 scope can be approved.

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

| Reconciliation step | Count | Note |
|---|---|---|
| Inventory v01 baseline (pre-pilot) | 43 | Documented in `20260612_d-folder-operating-model-and-current-inventory-v01.md` |
| Pilot A archived | -5 | 5 folders; specific ids in Pilot A execution report |
| Pilot B v01 | 0 | Halted at SC-7; zero folders archived |
| Pilot B retry archived | -4 | Lifecycle ids 47, 64, 65, 66 |
| **Current active** | **34** | Confirmed by Owner session brief |

**Folders confirmed archived in Pilot B retry (4):**

| Lifecycle id | Folder |
|---|---|
| 47 | `20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal` |
| 64 | `20260608_Core_UMC Archive Eligibility Chain Process Review` |
| 65 | `20260608_Core_R1-R5 Prioritization Assessment` |
| 66 | `20260608_Core_Phase 1 Proposal R1 R5 v01` |

These four folders must not appear in any future Batch 2 scope. They are archived.

**Lifecycle id 62 status — frozen, unchanged:**
Lifecycle id 62 is `20260608_Core_Retention Assessment P2 P5 UMC`.
This folder remained active and unchanged because a GL-013 open signal was detected
in `assessment.md` during Pilot B retry. GL-013 is not resolved in this proposal.
See Section 6.

**Zero unregistered folders.** All 34 active D-folders have a `deliverable_lifecycle` record.

**Source document for full per-folder inventory (43-folder pre-pilot baseline):**
`20260612_Core_DL Control Inventory/20260612_d-folder-operating-model-and-current-inventory-v01.md`

**Important caveat on per-category live counts:**
The inventory document reflects the 43-folder pre-pilot baseline. The exact per-category
breakdown for the current 34-folder live state has not been verified by a read-only scan
since the pilots completed. Some folders from the v01 category assignments have been
archived (ids 47, 64, 65, 66 from Pilot B retry; 5 additional from Pilot A). The
per-category counts in Section 5 of this proposal are estimates only. A read-only live
inventory verification is required before any concrete Batch 2 folder list can be approved.

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
  - Content indicates the chain was not closed (open items, unresolved decisions)
  - Any GL-013 or other open governance signal is encountered in the folder
- A deviation from any stop rule must be reported to Owner before the batch continues.
- Batch completion requires a written execution report (G2: file inside containment folder).

### 3.8 Owner Decision Gates

Owner decision required before:
- Any routing write to a live system file
- Any archive of a folder where `owner_decision` is NULL and status is ambiguous
- Any batch exceeding 5 folders
- Any reclassification of a `registered_but_unclear` folder
- Approval of any concrete Batch 2 folder list

Owner decision NOT required for:
- Read-only inventory and classification
- Proposing operating model rules (this document)
- DB registration at folder creation (Larry executes as administration)

---

## 4. Folder Categories Going Forward

These categories apply to the operating model. They are derived from the pre-pilot inventory
(43 folders) and updated for known archived folders. Exact live counts are estimates.
Per-category live counts must be verified in a separate read-only step before Batch 2
scope approval.

### Category A: Active Work — Must Remain Active

| Folder | Reason |
|---|---|
| `20260604_Core_Graduation Candidate Parked - Context-mode MCP Fix` | Owner explicitly retained |
| `20260612_Core_DL Control Inventory` | Current containment area (self-referential) |

**Estimated live count: 2**

### Category B: Provisionally Safe for Archive — Verification Required Before Scope Approval

These were assessed as closed process artifacts in the pre-pilot inventory. Before any
folder from this category is included in a Batch 2 scope proposal, the following must be
confirmed for each folder:
- Still active (not already archived in Pilot A or Pilot B retry)
- No live governance reference found since the pre-pilot inventory was written

Known archived folders that must be excluded from any Batch 2 scope:
- `20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal` (archived, id 47)
- `20260608_Core_UMC Archive Eligibility Chain Process Review` (archived, id 64)
- `20260608_Core_R1-R5 Prioritization Assessment` (archived, id 65)
- `20260608_Core_Phase 1 Proposal R1 R5 v01` (archived, id 66)

Remaining provisionally safe candidates (to be verified in live inventory):
- `20260607_Core_Deliverable Lifecycle Hardening Phase B Triage`
- `20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal`
- `20260607_Core_DL Smoke Test Recovery Report`
- `20260612_Core_DL Batch 1 Archive Execution Plan`
- `20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal`
- `20260608_Core_UMC Archive Eligibility Analysis 20260530`
- `20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen`
- `20260608_Core_Write Proposal GL-013 Additions P2 P5`
- `20260608_Core_Phase 1 Proposal R1 R5 v02`

Note: `20260608_Core_Retention Assessment P2 P5 UMC` (id 62) is in this list in the
pre-pilot inventory but is FROZEN due to GL-013 signal. It must not be included in
any Batch 2 scope until GL-013 is resolved. See Section 6.

**Estimated live count: 9 candidates (excluding id 62 and the 4 already archived)**

### Category C: Requires Owner Decision Before Any Action

These require an explicit Owner decision before routing or archiving.

Domain knowledge — routing required first:
- `20260513_Geldstroom Regie_One-pager methodiek`
- `20260519_Kamer E-commerce_Remy Research Week 21`
- `20260530_Personal_Blueprint weekschema en oefeningen`
- `20260531_Personal_Health Monitoring Schema`
- `20260531_Personal_Morning Mobility Routine`

Status confirmation required:
- `20260607_Core_Auto-Processing Deliverable Lifecycle Discovery`
- `20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design`
- `20260607_Core_Deliverable Lifecycle Backlog Processing Batch 1 Proposal`
- `20260608_Core_DL Pending Decision Inventory`
- `20260608_Core_DLH GL-001 and GL-004 Amendment Proposal v01`
- `20260608_Core_DLH_GL-001_GL-004_Proposal_Review`

**Estimated live count: 11 (unchanged from pre-pilot inventory — no Pilot A or B items in this group)**

### Category D: Registered but Unclear — Frozen Until Per-Item Owner Review

These have audit value as source documents for live governance rules. No autonomous action.

Pre-pilot count: 16. Some Pilot A archived folders may have come from adjacent items.
Exact live count requires verification.

Folders known to still be active from this category:
- `20260604_Core_Architecture Triage Memory Domain Routing`
- `20260604_Core_Deliverable Lifecycle Knowledge Processing Triage`
- `20260604_Core_Review Gate Protocol Triage`
- `20260605_Core_Lifecycle Decision Record GL-017 SOP-017`
- `20260605_Core_SOP-017 Amendment Lifecycle Execution`
- `20260607_Core_DL Phase 1 Retroactive Iris Review`
- `20260607_Core_Final Governance State Verification`
- `20260607_Core_Learning Candidate Flag Triage Proposal`
- `20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards`
- `20260607_Core_team-tasks-id-76-assessment`
- `20260608_Core_DL Granularity Assessment`
- `20260608_Core_DL Hardening Phase C Proposal v01`
- `20260608_Core_DL Post-Granularity Usability Assessment`
- `20260608_Core_DL Usability Assessment Owner Perspective`
- `20260608_Core_DL Visibility Architecture Assessment`
- `20260608_Core_GL-013 Reconciliation Analysis`

**Estimated live count: up to 16 (Pilot A may have archived some — verify)**

---

## 5. Estimated Category Summary

These counts are estimates based on the pre-pilot 43-folder inventory minus known archived
folders. They are NOT verified live counts. A read-only live inventory scan is required
before these counts can be used for Batch 2 scope approval.

| Category | Label | Estimated live count |
|---|---|---|
| A | Active Work — Must Remain Active | 2 |
| B | Provisionally Safe (to verify) | ~9 candidates (excl. id 62) |
| C | Requires Owner Decision | ~11 |
| D | Registered but Unclear — Frozen | up to 16 |
| id 62 | Frozen — GL-013 signal | 1 |
| **Total active** | | **34** |

---

## 6. GL-013 and Lifecycle id 62 — Handling Approach

**Lifecycle id 62** is `20260608_Core_Retention Assessment P2 P5 UMC`.

This folder remained active and unchanged during Pilot B retry because a GL-013 open
signal was detected in `assessment.md`. The folder was explicitly excluded from the pilot.

**This proposal does not resolve GL-013.**

Handling approach:
1. GL-013 resolution is a separate governance action with its own authorization gate.
2. Lifecycle id 62 is frozen until GL-013 status is explicitly confirmed by Owner.
3. If GL-013 is confirmed fully implemented and closed: id 62 may be reclassified to
   Category B in a separate inventory update, after Owner confirmation. No autonomous
   reclassification.
4. If GL-013 remains open or partially open: id 62 remains frozen.
5. No Batch 2 action touches id 62 unless its category is explicitly updated by Owner after
   GL-013 resolution.
6. Batch 2 may proceed on all other eligible folders without waiting for GL-013.

---

## 7. Prerequisites Before Batch 2 Scope Approval

Before Owner can approve a concrete Batch 2 folder list, the following must be completed:

**Step 1 — Operating model approval (this document):**
Owner approves the D-folder operating model rules as defined in Sections 3 and 4.
This is the decision requested by this proposal.

**Step 2 — Read-only live inventory verification (separate step, not yet done):**
A read-only scan of the current 34-folder active state must be performed to:
- Confirm which Category B candidates are still active (not archived by Pilot A)
- Confirm no new live governance references exist for any candidate folder
- Produce a verified Batch 2 candidate list excluding all archived folders

This step requires Owner authorization for the read-only scan (read-only, no writes).

**Step 3 — Batch 2 scope proposal (after Step 2):**
After verification: Larry presents a confirmed Batch 2 folder list with no archived folders
in scope. Owner approves the scope.

**Step 4 — Batch 2 write plan (after Step 3):**
Larry prepares a write plan (G2: file inside this containment folder). Owner authorizes.

**Step 5 — Batch 2 execution:**
Larry executes, writes execution report, reports to Owner.

**GL-013 isolation confirmed:** id 62 is not in Batch 2 scope regardless of batch size.

---

## 8. Exact Approval Needed from Owner Now

This proposal requests exactly one approval:

**Operating model approval:**
"I approve the D-folder operating model rules as described in Sections 3 and 4 of
proposal v02. The four categories (A, B, C, D) and the archive criteria in Section 3.6
are the authoritative operating rules going forward. I confirm lifecycle id 62
(`20260608_Core_Retention Assessment P2 P5 UMC`) is frozen and will not be touched
in Batch 2 until GL-013 is separately resolved."

**Not requested in this proposal:**
- Approval of a concrete Batch 2 folder list (requires live verification first)
- GL-013 resolution
- Domain knowledge routing decisions

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
Delivered at: `Deliverables/20260612_Core_DL Control Inventory/20260612_d-folder-operating-model-proposal-v02.md`
