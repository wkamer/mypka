# DL + LCL Control Inventory — 2026-06-16

**Purpose:** Narrow control inventory to identify the smallest safe next cleanup batches.
**Scope:** Inventory and classification only. No execution in this document.
**Produced by:** Larry
**Source session:** 2026-06-16

---

## Part 1: Deliverable Lifecycle (DL) Inventory

### 1.1 Active D-folders on disk

13 D-folders on disk (excluding Archive/, INDEX.md, README.md):

| Folder | Registered? | DL id | State/State_GL017 | Owner Decision |
|--------|-------------|-------|--------------------|----------------|
| 20260604_Core_Graduation Candidate Parked - Context-mode MCP Fix | Yes | 12 | ready / active | deferred |
| 20260605_Core_Lifecycle Decision Record GL-017 SOP-017 | Yes | 14 | active / closed | accepted_done |
| 20260607_Core_Auto-Processing Deliverable Lifecycle Discovery | Yes | 18 | ready / pending_lifecycle_decision | deferred |
| 20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design | Yes | 19 | ready / pending_lifecycle_decision | deferred |
| 20260607_Core_Deliverable Lifecycle Backlog Processing Batch 1 Proposal | Yes | 45 | ready / pending_lifecycle_decision | deferred |
| 20260607_Core_team-tasks-id-76-assessment | Yes | 46 | ready / pending_lifecycle_decision | deferred |
| 20260608_Core_DLH GL-001 and GL-004 Amendment Proposal v01 | Yes | 50 | active / active | retain |
| 20260608_Core_DLH_GL-001_GL-004_Proposal_Review | Yes | 52 | active / active | NULL |
| 20260608_Core_DL Visibility Architecture Assessment | Yes | 58 | ready / pending_lifecycle_decision | deferred |
| 20260608_Core_GL-013 Reconciliation Analysis | Yes | 67 | ready / active | deferred |
| 20260612_Core_DL Control Inventory | Yes | 69 | ready / active | NULL |
| 20260615_Core_Lifecycle Sweep Model Design | **NO** | — | — | — |
| 20260616_Core_Proactive Larry Trigger Library spec | Yes | 76 | ready / active | NULL |

### 1.2 Registered rows not matching a disk D-folder (non-archived)

These rows exist in deliverable_lifecycle but have no matching D-folder on disk and are not archived:

| DL id | artifact_name | Note |
|-------|--------------|------|
| 73 | lifecycle-sweep-model-design-v01 | File-level name, not D-folder convention. Likely inside 20260615 folder. |
| 74 | lifecycle-sweep-model-design-v02 | Same. |
| 75 | lifecycle-sweep-model-design-v03 | Same. |
| 72 | 20260612_Core_DL Batch 2 Process Artifacts Archive Proposal | owner_decision says G2-misclassified, file moved to DL Control Inventory. DB state still 'ready'. |
| 5 | 20260530_Core_UMC diagnose en aanbevelingen | state=ready, state_gl017=archived. Folder not on disk. In Archive? |
| 10 | 20260604_Core_Architecture Triage Memory Domain Routing | state=ready, state_gl017=archived. Folder not on disk. |
| 11 | 20260604_Core_Deliverable Lifecycle Knowledge Processing Triage | Same pattern. |
| 13 | 20260604_Core_Review Gate Protocol Triage | Same pattern. |
| 16 | 20260605_Core_SOP-017 Amendment Lifecycle Execution | Same pattern. |

### 1.3 State / state_gl017 mismatch analysis

OD-3 (team_tasks id 98) is open: "define state conflict precedence for deliverable_lifecycle rows where state and state_gl017 disagree." All mismatch repairs are blocked until OD-3 is resolved.

Primary mismatch patterns observed:
- ~15 rows: state='ready', state_gl017='archived' — most common conflict
- id 14: state='active', state_gl017='closed' — clear terminal mismatch

### 1.4 Metadata gaps

| DL id | artifact_name | Gap |
|-------|--------------|-----|
| 73, 74, 75 | lifecycle-sweep-model-design-v01/02/03 | artifact_name uses file convention, not D-folder convention |
| 52 | DLH_GL-001_GL-004_Proposal_Review | owner_decision = NULL, no decision on record |
| 69 | DL Control Inventory | owner_decision = NULL |
| 67, 12 | various | agent = NULL, source_session = NULL |
| Most rows pre-id-67 | various | agent = NULL, source_session = NULL |

### 1.5 Open team_tasks linked to DL

| id | Title | Blocker |
|----|-------|---------|
| 75 | Deliverable Folder & Versioning Rule | Governance decision pending |
| 84 | GL-022 Section 6 phrasing cleanup | Owner priority unclear |
| 87 | artifact_type migration sequence | Depends on naming standardization |
| 88 | Implement Granularity Rules Proposal v02 | Owner authorization pending |
| 92 | Owner to decide: pause cleanup or continue Batch 2 | Owner decision |
| 93 | Routing for 5 approved knowledge items | Owner decision |
| 94 | D-folder operating model before Batch 2 | Owner decision |
| 98 | OD-3: state conflict precedence | Open decision — gates bulk repair |
| 100 | Track 2: Post-Implementation Assurance Checklist | Not started |

### 1.6 INDEX.md currency

INDEX.md last written: 2026-06-16 11:17. One file added to spec folder after that timestamp. INDEX.md is slightly stale. Needs one-line regeneration.

### 1.7 DL Classification

**Metadata repair only (no Owner decision needed):**
- Register `20260615_Core_Lifecycle Sweep Model Design` as D-folder in deliverable_lifecycle
- Correct ids 73/74/75 artifact_names (verify file names vs D-folder convention)
- Refresh INDEX.md

**Needs Owner decision:**
- OD-3 (id 98) — resolves bulk state/state_gl017 repair
- id 92 (team_tasks) — pause or continue Batch 2?
- id 94 (team_tasks) — D-folder operating model
- id 52 — no owner_decision recorded; is review still active?
- id 72 — G2 misclassification acknowledged, DB not updated

**Needs verification:**
- ids 73/74/75 — confirm these are file-level references inside 20260615 D-folder, not standalone artifacts
- ids 5, 10, 11, 13, 16 — confirm whether folders are in Archive/ or folders were never created

**Safe archive candidates:**
- None. Archive actions blocked (out of scope per task, and OD-3 not resolved).

**Excluded / do not touch:**
- All rows with state='archived' AND state_gl017='archived' — clean
- state/state_gl017 field updates — blocked by OD-3
- Pre-existing unregistered folder (20260615) — note only; registration is safe but flagged separately

**Unregistered D-folders:**
- `20260615_Core_Lifecycle Sweep Model Design` — 1 folder, confirmed

---

## Part 2: Learning Candidate Lifecycle (LCL) Inventory

### 2.1 LC table state

Total: 7 rows. All status='closed'. Table is clean.

| id | Status | Title (summary) | Resolution |
|----|--------|-----------------|------------|
| 4 | closed | Governance checkpoints bypassed in Owner-directed flows | SOP-019 Section 3 updated |
| 5 | closed | Verification script fragility in governance post-checks | GL-005 updated |
| 6 | closed | Batch-stop rules not inherited by execution brief | CLAUDE.md updated |
| 7 | closed | Post-check regex assumes branch order | GL-005 updated |
| 8 | closed | Compliance erosion risk for briefing obligations | Rejected — monitored |
| 9 | closed | Session log version-history shift | agent_learnings id=51 |
| 10 | closed | Option execution omitted persisted outcome artifact | agent_learnings |

No missing IDs 1–3 (possible prior deletes or table started at 4). No open rows.

### 2.2 Open team_tasks relevant to LCL

| id | Title | Blocker |
|----|-------|---------|
| 77 | Graduation candidate 1: English-language rule for governance deliverables | Needs GL assignment + Owner |
| 78 | Graduation candidate 2: versioning rule for proposal corrections | Needs SOP-015 or GL assignment |
| 80 | Write lc-triage-write-plan-v02.md — fix post-check scope + r[6]/r[7] bug | Technical fix; needs execution |
| 81 | Batch 3 write-list — deferred pending Q1 and Q2 | Q1/Q2 not documented |

### 2.3 Deferred DL row related to LCL

| DL id | artifact_name | State | Note |
|-------|--------------|-------|------|
| 36 | 20260607_Core_Learning Candidate Flag Triage Proposal | ready / archived | Deferred. LC table now clean — may be superseded |

### 2.4 LCL Classification

**Safe close candidates:**
- None (all LCs already closed)

**Safe retention candidates:**
- None needed (table clean)

**Needs triage:**
- None

**Needs Owner decision:**
- id 81 (team_tasks): What were Q1 and Q2 blocking Batch 3? Owner input to answer or scrap.
- id 36 (DL): Learning Candidate Flag Triage Proposal — now superseded given clean LC table?
- ids 77, 78: graduation candidates — still a priority?

**Governance-impact candidates:**
- id 77: English-language rule → GL amendment required
- id 78: Versioning rule → SOP-015 or GL amendment required
- id 80: lc-triage-write-plan-v02.md — technical governance tooling fix

**Note — Track 2 improvement candidate:**
Post-implementation assurance checklist (team_tasks id 100, captured 2026-06-16) was not added to learning_candidates. It is currently a file-only + team_tasks capture. If it should enter the formal LCL, a new LC row should be inserted. Owner decision.

**Excluded / do not touch:**
- All closed LC rows (ids 4-10)
- id 80/81 without resolving Q1/Q2 context

---

## Top 3 Safest Next Actions

1. **Resolve OD-3** (team_tasks 98) — Owner decision on state/state_gl017 precedence. Gates the bulk of DL metadata repair. No file writes, no moves. One question, one answer.

2. **Register `20260615_Core_Lifecycle Sweep Model Design`** in deliverable_lifecycle — pure metadata INSERT, no file moves, no state changes, no Owner decision required. Eliminates the 1 unregistered D-folder.

3. **Clarify Q1 and Q2 for Batch 3** (team_tasks 81) — Owner input to either answer or scrap. Unblocks LCL team_tasks 80 and 81 without any file writes.

---

## What Must Not Be Touched

- Archive or move operations on any D-folder
- state or state_gl017 field updates before OD-3 is resolved
- team_tasks 80 and 81 before Q1/Q2 are clarified
- Pre-existing unregistered folder (20260615_Core_Lifecycle Sweep Model Design) — registration is safe; folder contents must not be moved or renamed
- ids 5, 10, 11, 13, 16 — do not update until Archive/ presence is verified
- id 91, 95 (team_tasks) — personal/legal domain, out of scope

---

Captured on: 2026-06-16
Captured at: session — DL + LCL Control Inventory narrow sweep
