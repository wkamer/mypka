# Lifecycle Control Baseline — Deliverable Lifecycle and Learning Candidate Lifecycle

**Date:** 2026-06-13
**Author:** Larry
**Session:** 2026-06-13 DL Control Recovery
**Type:** Read-only baseline report
**Status:** Final

---

## Infrastructure Check

- Disk vs DB alignment: 29/29 exact match — no unregistered folders, no orphans
- DB state distribution: 8 `active` + 21 `pending_lifecycle_decision` = 29 non-archived
- Total archived: 39
- Learning Candidates: 7 total, all 7 `closed` — no open candidates

---

## Task A: Deliverable Lifecycle Classification (29 items)

### Category 1 — Active Work (8 items)

| ID | Artifact Name | Type | Workstream | Owner Decision | Next Action | Write Plan Later |
|----|--------------|------|-----------|---------------|-------------|-----------------|
| 12 | 20260604_Core_Graduation Candidate Parked - Context-mode MCP Fix | triage_document | — | retain | No action until context-mode MCP fix resolved | No |
| 14 | 20260605_Core_Lifecycle Decision Record GL-017 SOP-017 | decision_record | DLH | NULL | Archive when DLH workstream fully complete | Yes |
| 50 | 20260608_Core_DLH GL-001 and GL-004 Amendment Proposal v01 | proposal | DLH | retain | Implement when amendment approved | Yes |
| 52 | 20260608_Core_DLH_GL-001_GL-004_Proposal_Review | status_report | DLH | NULL | Archive after proposal is implemented | Yes |
| 53 | 20260608_Core_DL Granularity Assessment | proposal | DLH | Owner approved v02 for implementation 2026-06-08 | Execute team_task 88 (GL-017, SOP-017, SOP-019, CLAUDE.md amendments) | Yes |
| 59 | 20260608_Core_DL Pending Decision Inventory | triage_document | DLH | NULL | Keep active as control reference; archive when all decisions resolved | No |
| 67 | 20260608_Core_GL-013 Reconciliation Analysis | assessment | — | NULL | Read folder contents to determine disposition; propose archive or next action | Yes |
| 69 | 20260612_Core_DL Control Inventory | triage_document | DLH | NULL | Keep active — current control session folder | No |

### Category 2 — Safe Archive Candidate (15 items)

All items in this category have completed their purpose. Ready for batch archive write plan.

| ID | Artifact Name | Type | Archive Rationale |
|----|--------------|------|-----------------|
| 2 | 20260513_Geldstroom Regie_One-pager methodiek | domain_knowledge_update | Old GR domain knowledge deliverable, no open actions |
| 3 | 20260519_Kamer E-commerce_Remy Research Week 21 | research_brief | Old KE research brief, superseded by newer content |
| 10 | 20260604_Core_Architecture Triage Memory Domain Routing | assessment | UMC implemented and operational; assessment served its purpose |
| 11 | 20260604_Core_Deliverable Lifecycle Knowledge Processing Triage | triage_document | Superseded by Phase 1 Design (ID=19) |
| 16 | 20260605_Core_SOP-017 Amendment Lifecycle Execution | domain_knowledge_update | Execution complete; SOP-017 was amended |
| 18 | 20260607_Core_Auto-Processing Deliverable Lifecycle Discovery | proposal | Superseded by Phase 1 Design (ID=19) |
| 36 | 20260607_Core_Learning Candidate Flag Triage Proposal | proposal | LC triage was executed; proposal served its purpose |
| 40 | 20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards | status_report | LC-5 and LC-7 are closed with processed outcomes |
| 41 | 20260607_Core_Final Governance State Verification | verification_report | Verification complete |
| 42 | 20260607_Core_DL Phase 1 Retroactive Iris Review | triage_document | Iris review complete and incorporated |
| 45 | 20260607_Core_Deliverable Lifecycle Backlog Processing Batch 1 Proposal | proposal | Batch 1 executed; IDs 60, 61, 62, 63, 68 archived |
| 55 | 20260608_Core_DL Hardening Phase C Proposal v01 | proposal | Phase C complete |
| 56 | 20260608_Core_DL Post-Granularity Usability Assessment | assessment | Phase C complete |
| 57 | 20260608_Core_DL Usability Assessment Owner Perspective | assessment | Phase C complete |
| 58 | 20260608_Core_DL Visibility Architecture Assessment | assessment | Phase C complete |

**Next action:** Single batch archive write plan for all 15 items (DB state_gl017 update + folder move to Archive). No individual Owner decisions required.

### Category 3 — Owner Decision Required (3 items)

| ID | Artifact Name | Type | Decision Needed |
|----|--------------|------|----------------|
| 6 | 20260530_Personal_Blueprint weekschema en oefeningen | domain_knowledge_update | Is this content actively in use? Route to Lena/Sienna for integration, or archive. |
| 7 | 20260531_Personal_Health Monitoring Schema | domain_knowledge_update | Same — active use or archive? |
| 8 | 20260531_Personal_Morning Mobility Routine | domain_knowledge_update | Same — active use or archive? |

**Next action:** Owner states disposition (active/archive) for each. Write plan required after decision.

### Category 4 — Blocked or Frozen (2 items)

| ID | Artifact Name | Blocker | Unblock Condition |
|----|--------------|---------|-----------------|
| 13 | 20260604_Core_Review Gate Protocol Triage | Workstream code GG — status and disposition unclear; folder contents not yet read | Read folder; identify whether GG workstream is active or superseded |
| 19 | 20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design | Deferred pending team_task 94: D-folder operating model decision | Resolve team_task 94 (tied to team_task 92: pause vs. continue Batch 2) |

**Next action:** ID=13 folder read in next session. ID=19 waits on team_task 94.

### Category 5 — Registered but Unclear (1 item)

| ID | Artifact Name | Observation |
|----|--------------|-------------|
| 46 | 20260607_Core_team-tasks-id-76-assessment | team_task 76 is completed (2026-06-07). Folder likely archiveable but requires folder read to confirm no residual open items. |

**Next action:** Read folder contents; propose archive if confirmed clean.

---

## Task B: Learning Candidate Lifecycle Baseline

### All 7 LCs closed — no open candidates

| LC | Status | Category | Routing | Outcome | Title (abbreviated) |
|----|--------|----------|---------|---------|-------------------|
| LC-4 | closed | CAT-3 | graduation_candidate | sop_update | CP invocation behavior in Owner-directed interactive flows |
| LC-5 | closed | CAT-3 | graduation_candidate | guideline_update | Verification script fragility in governance post-checks |
| LC-6 | closed | CAT-3 | graduation_candidate | claude_instruction_update | Batch-stop rules not inherited by executing brief |
| LC-7 | closed | CAT-3 | graduation_candidate | guideline_update | Post-check regex assumes branch order in resolve_lc |
| LC-8 | closed | CAT-3 | — | rejected | Compliance erosion risk for always-active briefing obligations |
| LC-9 | closed | CAT-2 | — | agent_learning | Session log version-history attribution error |
| LC-10 | closed | CAT-2 | standard | agent_learning | Outcome artifact missing on shorthand option selection |

**LC classification result:** all 7 — close as done.

### Graduation Implementation Gap

LC database is clean, but graduation implementation is incomplete. Four team_tasks are LC-derived and remain open:

| Task ID | Title | Scope |
|---------|-------|-------|
| 77 | Graduation candidate 1: add English-language rule for governance deliverables to appropriate GL | GL amendment |
| 78 | Graduation candidate 2: add versioning rule for governance proposal corrections to SOP-015 or appropriate GL | SOP-015 amendment |
| 80 | Write lc-triage-write-plan-v02.md — fix post-check scope and r[6]/r[7] print bug | LC tooling fix |
| 81 | Batch 3 write-list — deferred pending Q1 and Q2 answers | LC batch deferred |

Tasks 77 and 78 are the primary graduation blockers. Tasks 80 and 81 are deferred LC infrastructure.

---

## Task C: Control Recommendation

### Minimum viable operating loop

**Weekly Owner review (4 items max):**
1. Active D-folders with open implementation tasks: ID=53 (task 88), ID=50 (pending amendment)
2. Blocked items: is team_task 94 (D-folder operating model) ready to decide? Unlocks ID=19.
3. LC graduation tasks 77 and 78: any progress or assignment?
4. Safe Archive Candidate batch (15 items): ready — Owner confirms go/no-go for batch archive

**Triggers for a file-based write plan:**
- Any archive action (folder move + DB state_gl017 update to `archived`)
- Any GL, SOP, or CLAUDE.md amendment (tasks 77, 78, 88)
- LC batch write actions (tasks 80, 81 when unblocked)
- D-folder operating model decision and its downstream effects (task 94)
- Personal domain items 6, 7, 8 disposition after Owner decision

**Never chat-only:**
- DB state_gl017 updates
- Folder moves or archive actions
- GL, SOP, or CLAUDE.md edits
- LC graduation implementations
- Any write action touching more than 1 record or file

**Deferred — do not act until explicitly unblocked:**
- Batch 2 archive sweep (waits on team_task 92: pause vs. continue decision)
- Auto-processing Phase 1 implementation (waits on team_task 94: D-folder operating model)
- GL-013 reconciliation resolution (separate session; read folder first)
- Personal domain items 6, 7, 8 (route to Sienna/Lena when Owner is ready)
- LC tasks 80 and 81 (deferred pending Q1 and Q2 answers)

### Summary counts

| Category | Count |
|----------|-------|
| Active Work | 8 |
| Safe Archive Candidate | 15 |
| Owner Decision Required | 3 |
| Blocked or Frozen | 2 |
| Registered but Unclear | 1 |
| **Total non-archived** | **29** |

| LC Status | Count |
|-----------|-------|
| Closed (all) | 7 |
| Open graduation team_tasks | 4 |

---

Delivered on: 2026-06-13
Delivered at: Deliverables/20260612_Core_DL Control Inventory/20260613_lifecycle-control-baseline-dl-lc-v01.md
