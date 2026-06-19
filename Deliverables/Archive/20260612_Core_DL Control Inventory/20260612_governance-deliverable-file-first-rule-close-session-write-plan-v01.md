# Close-Session Write Plan: Governance Deliverable File-First Rule Amendment

**Version:** v01
**Date:** 2026-06-12
**Author:** Governance Assistant
**Status:** Write plan, awaiting Owner authorization before execution
**Containment folder:** 20260612_Core_DL Control Inventory
**Execution report required:** None (close-session writes are not subject to a separate execution report per SOP; the Markdown mirror serves as the audit artifact)

---

## 1. Authorized Write Actions

Three write actions only. No other writes.

| ID | Action | Target |
|---|---|---|
| W-1 | INSERT session_logs row | `/opt/myPKA/Team Knowledge/team-knowledge.db` |
| W-2 | Write Markdown mirror | `Team Knowledge/Core/session-logs/2026/06/2026-06-12-governance-deliverable-file-first-rule-amendment.md` |
| W-3 | UMC write_summary | UMC memory layer, domain=core, source_type=knowledge |

---

## 2. W-1: session_logs INSERT

Table: `session_logs` in `Team Knowledge/team-knowledge.db`

Fields:

- **session_date:** 2026-06-12
- **session_title:** Governance Deliverable File-First Rule CLAUDE.md Amendment
- **duration_text:** Single session, 2026-06-12
- **topics:** DLH, governance-amendment, CLAUDE.md, file-first-rule
- **summary:** Session continued myPKA Deliverable Lifecycle control recovery. A governance behavior gap was identified: the D-folder Operating Model Proposal was produced as chat-only output with no persisted file. To close this systemic gap, a Governance Deliverable File-First Rule was proposed, reviewed across three decision rounds (gap analysis, rule wording with GL-021 boundary, CLAUDE.md authorization), and implemented. The CLAUDE.md edit passed all 6 preflight and 6 verification checks, inserting the new rule at line 622 immediately after the Execution Persistence Rule. Execution report v01 contained an audit wording defect corrected in v02, accepted as the authoritative record.
- **decisions:** 1. D-folder Operating Model Proposal v01 (chat-only) identified as governance gap requiring systemic rule fix. 2. Governance Deliverable File-First Rule accepted: Decision A gap analysis accepted, Decision B rule wording accepted including GL-021 write authorization boundary, Decision C CLAUDE.md edit authorized per write plan. 3. Execution report v02 supersedes v01 for audit interpretation (non-actions wording corrected). 4. team_log row removed from close-session scope (not authorized). 5. team_task 92 remains open. 6. team_task 94 remains open. 7. Todoist Owner decisions 6-11 remain open.
- **actions_taken:** 1. Written: governance-deliverable-file-first-rule-proposal-v01.md in containment folder (two correction rounds: author and delivered-at fields, then GL-021 write authorization wording). 2. Written: governance-deliverable-file-first-rule-write-plan-v01.md in containment folder. 3. Edited: CLAUDE.md (+48 lines, Governance Deliverable File-First Rule inserted at line 622, immediately after Execution Persistence Rule). 4. Written: execution-report-v01.md (audit defect: non-actions wording). 5. Written: execution-report-v02.md (corrected, accepted as authoritative). 6. Written: governance-deliverable-file-first-rule-close-session-write-plan-v01.md (this file, after chat-only write plan violation corrected).
- **delegations:** None
- **open_items:** 1. team_task 92: Owner decision on pause or continue cleanup (open). 2. team_task 94: D-folder operating model not yet persisted as file; chat-only proposal precedes new rule but must be written to file before Owner approval is valid under Governance Deliverable File-First Rule. 3. Todoist Owner decisions items 6-11: open.
- **agent_slug:** larry

---

## 3. W-2: Markdown Mirror

Path: `Team Knowledge/Core/session-logs/2026/06/2026-06-12-governance-deliverable-file-first-rule-amendment.md`

Content mirrors the session_logs row from W-1 exactly, formatted as Markdown with standard session log template (date, title, topics, summary, decisions, actions taken, delegations, open items).

---

## 4. W-3: UMC write_summary

Required by CLAUDE.md UMC section: "Bij elke /close-* routine: mm.write_summary() met sessiesamenvatting. Domein + source_type altijd meegeven."

Parameters:
- domain: core
- source_type: knowledge
- content: session summary from W-1

---

## 5. Explicit Non-Actions

- No CLAUDE.md edit.
- No new D-folder.
- No folder creation.
- No database mutations other than W-1 and W-3.
- No archive actions.
- No Batch 2.
- No dashboard work.
- No GL-013 resolution.
- No routing.
- No Learning Candidate triage.
- No Deliverable Lifecycle sweep.
- No team_tasks status updates (team_task 92 and 94 remain open, untouched).
- No team_log row.
- No agent_learnings rows.
- No delegation_outcomes rows.

---

## 6. Stop Conditions

| ID | Condition | Action |
|---|---|---|
| SC-1 | session_logs INSERT fails | Stop. Report to Owner. Do not proceed to W-2 or W-3. |
| SC-2 | Markdown mirror target folder does not exist | Stop. Report to Owner. |
| SC-3 | UMC not reachable | Skip W-3 only. Report: UMC niet bereikbaar. W-1 and W-2 still proceed. |

---

**Delivered on:** 2026-06-12
**Delivered at:** Deliverables/20260612_Core_DL Control Inventory/20260612_governance-deliverable-file-first-rule-close-session-write-plan-v01.md
