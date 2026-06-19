# PROPOSAL — Idea-to-Implementation Governance Pack: Smoke Test Plan

**Proposal status:** Draft v04
**Prepared by:** Larry (Team Orchestrator)
**Date:** 2026-06-05
**For:** Owner Walter Kamer
**Tests:** idea-routing-gl-proposal-v04.md, idea-routing-sop-proposal-v04.md, review-context-packet-sop-016-amendment-proposal-v04.md
**Governance baseline:** GL-014, GL-015, GL-016, GL-017, GL-018 (pending), SOP-015, SOP-016, SOP-017, SOP-018 (pending), SOP-016 RCP amendment (pending)

---

> **PROPOSAL ONLY.**
> This smoke test plan is a proposal for review. No smoke test is executed by this document or by approval of this document. No real execution occurs during the smoke test unless Owner separately approves smoke test execution in a dedicated session. No files are created, modified, or moved.

---

## Revision Summary (v01 to v02)

The following changes were made in response to the Owner's v01 amendment request:

1. **Test Assumptions and Definitions section added** — Defines Route A–F, DP-1 through DP-6 (v02 sequence), Review Gate modes, role-based definitions, and hard exclusions. Makes the smoke test self-contained.
2. **T02 terminology corrected** — "meta integration handler" replaced with "Todoist integration handler" and clarified.
3. **T07 GL-004 reference corrected** — "GL-004 path-change protocol" replaced with "active canonical paths reference update protocol (currently: GL-004)"; GL-004 added to companion sources.
4. **T10 updated** — All named agent references replaced with role-based; personal priority gate and project classification described as existing behavioral rules, not new SOP-018 gates.
5. **All DP references updated** — All test cases now use v02 DP-1 through DP-6 sequence. DP-3 is post-Review Gate Owner decision; DP-4 is implementation confirmation.
6. **Pack-level Implementation Order section added** — Full implementation sequence with post-check requirements.
7. **Smoke Test Pass/Fail Summary updated** — Reflects role-based agents and v02 DP numbering.

---

## Revision Summary (v02 to v03)

The following changes were made in response to the Owner's v02 amendment request:

1. **T02 corrected — Route B / S2-Medium** — The v02 T02 incorrectly framed S2-Medium as Route B first, then escalated to Route C via escalation condition 1. The route matrix (SOP-018 Section 10) maps S2-Medium directly to Route C; no Route B check applies. T02 is rewritten: clarification paragraph updated (GL-007 reference corrected to GL-001; handler identified as an operational system file; Route B check removed); expected triage output corrected; pass criteria corrected; fail criteria corrected. The Route B escalation criterion in the Pass/Fail Summary is updated accordingly.
2. **T04 corrected — DP-2 sequencing** — The v02 T04 incorrectly described DP-1 as confirming "route and research scope" and DP-2 as "research brief approval." Per the required sequence: DP-1 confirms S4/Route E classification and route recommendation; DP-2 approves research scope before research begins; the research role delivers the brief after DP-2; the full proposal is prepared after the brief. T04 expected triage output, required Owner decisions, pass criteria, and fail criteria are updated.
3. **T05 updated — file category terminology** — "system file (skill)" replaced with "operational system file (skill)" per SOP-018 Section 2.4.
4. **T08 updated — file category terminology** — "system files" replaced with "governance files" in the governance-relevant context.
5. **Route B escalation conditions updated** — Condition 1 split into 1a (governance file → Route D) and 1b (operational system file → Route C), consistent with SOP-018 v03 Section 9 and Section 2.4.
6. **Pass/Fail Summary updated** — T02 and T04 entries corrected; Route B escalation criterion updated.
7. **Pending Proposals table updated** — All four file paths updated to v03 versions.
8. **Acceptance criterion 5 updated** — No longer verifies Route B escalation in T02; now verifies correct direct Route C assignment for S2-Medium.

---

## Revision Summary (v03 to v04)

The following changes were made in response to the Owner's v03 amendment request:

1. **Acceptance criterion 3 corrected** — Previously said "v02 DP numbering" inconsistently alongside a reference to "SOP-018 v03 sequence." Changed to: "All test cases use DP-1 through DP-6 per SOP-018 v04; no test case references a DP outside this sequence."
2. **T03 RCP note corrected** — "system file potentially modified" changed to "operational system file potentially modified."
3. **T04 RCP note corrected** — "system files created" changed to "operational system files created."
4. **Route Definitions section updated** — Added explicit Route B scope note: Route B applies to Low-impact ideas only and is not available for Medium, High, or Critical impact. Added note that S1-High routes to Route C per the corrected route matrix in SOP-018 v04.
5. **Pass/Fail Summary updated** — Added criterion confirming S1-High routes to Route C, not Route B.
6. **Pending Proposals table updated** — All four file paths updated from v03 to v04 versions.
7. **All SOP-018 version references updated** — "SOP-018 v03" references in Test Assumptions section headers updated to "SOP-018 v04."
8. **Acceptance criterion 13 added** — Verifies that the Route B scope note and Pass/Fail Summary correctly reflect the Low-impact restriction and S1-High routing to Route C.

---

## Purpose

This smoke test plan verifies that the Idea-to-Implementation Governance Pack — GL-018, SOP-018, and the SOP-016 RCP amendment — correctly routes 10 synthetic ideas, one for each scenario class S1 through S10.

A smoke test is a structured walkthrough. It confirms that the governance logic is consistent, scenario classes are distinguishable, and routes, decision points, and prohibited actions produce the correct outcomes for representative inputs.

The smoke test does not test implementation. It tests the governance logic.

---

## Explicit Confirmations

The following constraints apply to the entire smoke test. They may not be overridden by any individual test case.

| # | Constraint |
|---|---|
| EC-1 | No real execution during smoke test unless separately approved by Owner in a dedicated session |
| EC-2 | No files created, modified, moved, or archived as a result of the smoke test |
| EC-3 | No database writes (team_tasks, session_logs, agent_learnings, UMC, personal.db, kamer e-commerce.db, geldstroom-regie.db, or any other database) |
| EC-4 | No PKM extraction or knowledge write |
| EC-5 | No BKM extraction or knowledge write |
| EC-6 | No AGENT.md updates |
| EC-7 | No CLAUDE.md updates |
| EC-8 | No backlog item creation |
| EC-9 | No Telegram or integration changes |
| EC-10 | No SOP or GL modifications |
| EC-11 | No index file updates |
| EC-12 | All 10 test cases are synthetic — fictional ideas for governance logic testing only |
| EC-13 | No persistent write is authorized by the smoke test itself; all captures are transient |

---

## Test Assumptions and Definitions

This section makes the smoke test self-contained. A reviewer with this section, the four companion proposal documents, and the active governance baseline can execute the smoke test without any prior chat context.

### Active Governance Baseline

The following documents are active (implemented) at the time this smoke test plan was prepared:

- GL-016 — Review Gate for Governance-Relevant Deliverables
- SOP-016 — Review Gate Procedure for Governance-Relevant Deliverables
- GL-017 — Deliverable Lifecycle Knowledge Processing and Archiving
- SOP-017 — Deliverable Lifecycle Knowledge Processing and Archiving Procedure
- SOP-015 — Proposal Iteration Protocol for System File Changes
- GL-001 — File Naming Conventions (active file naming conventions reference)
- GL-004 — Canonical Paths (active canonical paths reference)
- GL-014 — AI Team Governance

### Pending Proposals Under Test

The following documents are pending approval. For smoke test purposes, use the v04 proposal content as the governance definition under test.

| Document | Path |
|---|---|
| GL-018 proposal v04 | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/idea-routing-gl-proposal-v04.md` |
| SOP-018 proposal v04 | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/idea-routing-sop-proposal-v04.md` |
| SOP-016 RCP amendment v04 | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/review-context-packet-sop-016-amendment-proposal-v04.md` |
| Smoke test plan v04 (this document) | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/idea-routing-smoke-test-plan-v04.md` |

### File Category Definitions (from SOP-018 v04 Section 2.4)

| Category | Includes | Governance requirement |
|---|---|---|
| Governance file | GLs, SOPs, Workstreams, AGENT.md, CLAUDE.md, governance indexes (gl-index.md, SOP-index.md, agent-index.md), and any other document that defines team operating rules, approval gates, or governance instruments | S8 / Route D required. SOP-015 Proposal Iteration Protocol applies. |
| Operational system file | Scripts, handlers, integration files, skill files, configuration files, and operational code files that are not governance files | Route C or higher required. Subject to Review Gate, DP-3, and DP-4. |

### Route Definitions (from SOP-018 v04 Section 9)

| Route | Name | Review Gate required |
|---|---|---|
| Route A | Direct execution: Owner confirmation → Execution | No |
| Route B | Lightweight proposal: Short proposal → Owner direct review → Owner DP-3 decision → Implementation confirmation (DP-4) → Execution | No — unless any escalation condition is true |
| Route C | Standard proposal: Full proposal → Review Gate → Owner DP-3 decision → Implementation confirmation (DP-4) → Execution → Implementation report → Lifecycle decision | Yes |
| Route D | Governance proposal: SOP-015 versioned proposal → Review Gate → Owner DP-3 decision → Implementation confirmation (DP-4) → Execution → Implementation report → Lifecycle decision | Yes |
| Route E | Research-first: Research role delivers research brief (Owner approves scope at DP-2) → Full proposal → Review Gate → Owner DP-3 decision → Implementation confirmation (DP-4) → Execution → Implementation report → Lifecycle decision | Yes |
| Route F | Security review: Security proposal → Mode 1 Review Gate preferred → Owner DP-3 decision → Implementation confirmation (DP-4, with security sign-off) → Execution → Implementation report with security confirmation → Lifecycle decision | Yes |

**Route B escalation conditions (from SOP-018 v04 Section 9):**
Route B escalates if any of the following is true:

1a. A governance file is created, modified, or deleted (governance files: GLs, SOPs, Workstreams, AGENT.md, CLAUDE.md, governance indexes — see SOP-018 Section 2.4) → escalates to Route D
1b. An operational system file is created, modified, or deleted (operational system files: scripts, handlers, integration files, skill files, configuration files — see SOP-018 Section 2.4) → escalates to Route C
2. A persistent database write is executed → escalates to Route C
3. A governance impact exists (change to team operating rules or governance instruments) → escalates to Route D
4. A security impact exists (credential handling, token storage, access control change, external exposure) → escalates to Route F
5. A cross-domain impact exists (action affects more than one domain) → escalates to Route C
6. An external integration change is required (webhook, API endpoint, external service configuration) → escalates to Route C

**Route B scope:** Route B applies to Low-impact ideas only. Route B is not available for Medium, High, or Critical impact. For S1-High scenarios, the route is Route C (full proposal required), not Route B. The Route Selection Matrix in SOP-018 v04 does not assign Route B to any Medium, High, or Critical cell.

### Owner Decision Points (from SOP-018 v04 Section 12)

| DP | Trigger | Decision required |
|---|---|---|
| DP-1 | Classification complete — Medium or higher impact | Owner confirms or redirects route recommendation |
| DP-2 | Research scope ready (Route E only) | Owner approves research scope before research begins |
| DP-3 | Proposal ready for Owner decision. For routes requiring Review Gate: Review Gate has been completed and findings assembled. For Route B without escalation: Owner reviews lightweight proposal directly. | Owner decides: accept / request amendments / defer / reject |
| DP-4 | Proposal accepted at DP-3 | Separate explicit implementation confirmation before execution begins. DP-3 acceptance is not an implementation authorization. |
| DP-5 | Implementation complete | Owner receives and accepts/rejects implementation report |
| DP-6 | Implementation report accepted | Owner approves each lifecycle processing destination |

**Route A:** Only DP-4.
**Route B without escalation:** DP-1, DP-3 (direct review), DP-4 (separate from DP-3).
**Route C, D:** DP-1, DP-3 (post-Review Gate), DP-4, DP-5, DP-6.
**Route E:** DP-1, DP-2 (research scope approval before research begins), DP-3 (post-Review Gate), DP-4, DP-5, DP-6.
**Route F:** DP-1, DP-3 (post-Review Gate with security sign-off), DP-4 (with security sign-off), DP-5, DP-6.

### Review Gate Modes (from SOP-018 v04 Section 2.3 and SOP-016)

| Mode | Condition | Definition |
|---|---|---|
| Mode 1 — External review | Preferred for S8, S9, governance-critical deliverables | A reviewer external to the producing agent applies the 13 review checks. Maintainer assembles RCP + review package, distributes, collects findings, packages Owner decision packet. |
| Mode 2 — Internal multi-agent review | Preferred for S10 (cross-domain) | Multiple internal agents with distinct roles review the deliverable. Role separation per SOP-016. Maintainer orchestrates. |
| Mode 3 — Single-system fallback | When no external reviewer or additional agent is available | Single system applies self-review checklist, surfaces all uncertainties, packages decision for Owner. Hard stop conditions per SOP-016 Section 5 apply. Not sufficient for Critical-impact deliverables. |

### Role-Based Definitions (from SOP-018 v04 Section 2)

| Role | Definition | Current assignment |
|---|---|---|
| Maintainer | Receives every idea, performs triage, routes to specialist, tracks pipeline. | Larry |
| Research role | Delivers domain research briefs for Route E (S4 scenario). | Currently: Pax |
| Personal priority gate role | Evaluates whether a new initiative is deliberate and aligned with Owner priorities. This is an existing behavioral rule in team operating instructions; not created by SOP-018. | Currently: Sienna |
| Project classification role | Assigns ICOR classification and project structure to confirmed initiatives. This is an existing behavioral rule in team operating instructions; not created by SOP-018. | Currently: Marcus |
| Domain specialist — Personal | Executes Personal domain deliverables. | Currently: Sienna |
| Domain specialist — Kamer E-commerce | Executes Kamer E-commerce domain deliverables. | Currently: Nova, Vera |
| Domain specialist — Geldstroom Regie | Executes Geldstroom Regie domain deliverables. | Currently: Finn |
| Reviewer | Applies SOP-016 review checks to a deliverable. Must not be the same as the producer for governance-critical deliverables. | Assigned per review |

### Hard Exclusions for Smoke Test

No action in a smoke test case may authorize, imply, or trigger:
- File creation, modification, or deletion
- Database writes of any kind
- Implementation of any kind
- Index updates
- AGENT.md or CLAUDE.md modifications
- SOP or GL modifications
- Backlog item creation
- External service changes

All findings are logical (correct/incorrect classification) only. No physical action results from the smoke test.

### Statement on Smoke Test Execution

This smoke test plan does not execute anything. Approval of this plan is not authorization to run the smoke test. Smoke test execution requires a separate Owner approval in a dedicated session, after GL-018, SOP-018, and the SOP-016 amendment are all implemented and post-checked.

---

## Test Cases

---

### T01 — Scenario S1: Use Existing Capability

**Synthetic idea:**
"Run the existing Todoist daily task overview script and display the results in the morning routine."

**Expected primary scenario:** S1 — Use Existing Capability
**Expected secondary labels:** None
**Expected impact label:** Low
**Expected route:** Route A

**Expected triage output:**
- S1-Low
- Route A
- DP-4: Owner confirmation before execution
- No proposal required

**Review Gate applies:** No
**RCP required:** No
**Lifecycle decision applies:** No

**Required Owner decisions:** DP-4 only (confirmation before execution)

**Prohibited actions:**
- Creating a proposal document
- Modifying the Todoist script
- Any database write
- Treating the output as a governance deliverable requiring Review Gate

**Pass criteria:**
- Classified S1-Low
- Route A selected
- Owner confirmation (DP-4) obtained before execution
- No proposal created; no Review Gate triggered; no system file modified; no database written

**Fail criteria:**
- Any classification other than S1-Low
- Route other than A; proposal created; Review Gate triggered; any system file modified

---

### T02 — Scenario S2: Extend Existing Capability

**Synthetic idea:**
"Add a 'project name' column to the existing daily Todoist task overview script output."

**Clarification:** The overview script is a handler in the Todoist integration — an operational system file per SOP-018 Section 2.4. The route selection matrix (SOP-018 Section 10) maps S2-Medium directly to Route C. No Route B check is required; the medium impact label independently assigns Route C. The operational system file modification triggers the Review Gate per SOP-018 Section 13. The handler file naming convention follows the active file naming conventions reference, currently GL-001.

**Expected primary scenario:** S2 — Extend Existing Capability
**Expected secondary labels:** None
**Expected impact label:** Medium
**Expected route:** Route C (direct — S2-Medium per route matrix; Route B does not apply to Medium-impact S2)

**Expected triage output:**
- S2-Medium
- Route C (direct per route matrix; no Route B check applied)
- DP-1: Owner confirms route

**Review Gate applies:** Yes — operational system file (Todoist integration handler) is modified
**RCP required:** Yes — operational system file modification triggers RCP per SOP-016 amendment Section 11.2
**Lifecycle decision applies:** Yes

**Required Owner decisions:** DP-1 (route confirmation), DP-3 (Owner decision post-Review Gate), DP-4 (implementation confirmation), DP-5 (implementation report), DP-6 (lifecycle)

**Prohibited actions:**
- Modifying the integration handler before DP-3
- Skipping the Review Gate
- Skipping the RCP
- Applying a Route B check to S2-Medium (route matrix assigns Route C directly)
- Using v01 DP sequence (e.g., treating proposal acceptance as occurring before Review Gate)
- Treating the triage output as an implementation authorization

**Pass criteria:**
- S2-Medium; Route C selected directly per route matrix (no Route B check)
- Full proposal required before handler modification
- Review Gate triggered with RCP
- Owner DP-3 decision made after Review Gate findings are returned
- Owner DP-4 confirmation separate from DP-3
- Implementation report required; lifecycle decision initiated

**Fail criteria:**
- Classified other than S2-Medium
- Handler modified before DP-3 Owner decision
- Route B applied (incorrect — route matrix maps S2-Medium to Route C directly)
- Review Gate or RCP skipped
- DP-3 treated as pre-Review Gate proposal acceptance

---

### T03 — Scenario S3: New Idea on Existing Solution

**Synthetic idea:**
"Add a weekly session-summary email digest to the existing session logging system, using the existing email integration."

**Expected primary scenario:** S3 — New Idea on Existing Solution
**Expected secondary labels:** None
**Expected impact label:** Medium
**Expected route:** Route C

**Expected triage output:**
- S3-Medium
- New behavior (weekly digest delivery) on existing infrastructure (session logging + email integration)
- DP-1: Owner confirms route

**Review Gate applies:** Yes
**RCP required:** Yes — operational system file potentially modified (new configuration or script)
**Lifecycle decision applies:** Yes

**Required Owner decisions:** DP-1, DP-3 (post-Review Gate), DP-4, DP-5, DP-6

**Prohibited actions:**
- Creating email trigger or digest configuration before DP-3
- Treating this as S2 (no modification to existing session log behavior — new output type added)

**Pass criteria:**
- S3-Medium (not S2 — core components not modified, new output type added)
- Route C selected
- Proposal required before any configuration created
- Review Gate triggered with RCP
- DP-3 occurs post-Review Gate; DP-4 is separate implementation confirmation

**Fail criteria:**
- Classified as S2 (incorrect)
- Configuration created before DP-3
- Review Gate skipped

---

### T04 — Scenario S4: New Idea on New Solution

**Synthetic idea:**
"Build a new integration with an external task-completion tracking service that automatically increments Goal progress counters when a Todoist task is marked complete."

**Expected primary scenario:** S4 — New Idea on New Solution
**Expected secondary labels:** S2 secondary (if Todoist handler requires modification to emit a completion event)
**Expected impact label:** High
**Expected route:** Route E (research-first)

**Expected triage output:**
- S4-High
- Route E
- Research role (currently: Pax) must deliver a research brief before proposal begins
- DP-1: Owner confirms S4/Route E classification and route recommendation
- DP-2: Owner approves research scope before research begins

**Review Gate applies:** Yes — at proposal and at execution report
**RCP required:** Yes — High impact, new integration, operational system files created
**Lifecycle decision applies:** Yes

**Required Owner decisions:** DP-1 (route and classification confirmation), DP-2 (research scope approval before research begins), DP-3 (post-Review Gate), DP-4, DP-5, DP-6

**Prohibited actions:**
- Beginning any research before DP-2 research scope is approved by the Owner
- Beginning any implementation before research brief is delivered and DP-3 Owner decision is made
- Treating this as S2 or S3 because Todoist is an existing integration (new external integration system required → S4)
- Skipping the research role brief
- Treating DP-2 as research brief approval (DP-2 is scope approval; brief is delivered after DP-2, not at DP-2)

**Pass criteria:**
- S4-High (not S2 or S3)
- Route E selected; DP-1 confirms route and classification
- DP-2 approves research scope before research begins
- Research role brief delivered after DP-2 scope approval; full proposal prepared after research brief
- Review Gate with RCP
- DP-3 post-Review Gate; DP-4 separate

**Fail criteria:**
- Classified as S2 or S3
- Research begins without DP-2 scope approval
- Proposal prepared without research brief
- DP-2 treated as research brief approval instead of scope approval

---

### T05 — Scenario S5: Fix Existing Solution

**Synthetic idea:**
"The close-session skill does not log the team_tasks sweep step when there are zero open items — the sweep step is silently skipped."

**Expected primary scenario:** S5 — Fix Existing Solution
**Expected secondary labels:** None
**Expected impact label:** Medium
**Expected route:** Route C

**Expected triage output:**
- S5-Medium
- Route C
- Proposal must include: diagnosis (root cause), proposed fix, scope boundary (fix limited to stated defect), post-check criteria
- DP-1: Owner confirms route and fix scope boundary

**Review Gate applies:** Yes — operational system file (skill) modified
**RCP required:** Yes — operational system file modification
**Lifecycle decision applies:** Yes

**Required Owner decisions:** DP-1 (route + fix scope confirmation), DP-3 (post-Review Gate), DP-4, DP-5, DP-6

**Prohibited actions:**
- Fixing the skill before DP-3 Owner decision
- Expanding fix scope beyond the stated defect without re-triage
- Treating the verbal description of the bug as an approved fix specification

**Pass criteria:**
- S5-Medium; Route C selected
- Diagnosis + fix proposal required before any skill file modified
- Review Gate triggered with RCP
- Fix scope confirmed as limited to stated defect at DP-1
- DP-3 post-Review Gate; DP-4 separate

**Fail criteria:**
- Skill modified before DP-3
- Review Gate skipped; fix scope expanded without re-triage

---

### T06 — Scenario S6: Replace Existing Solution

**Synthetic idea:**
"Replace the current standalone Python archiving script with a dedicated handler file in the integration framework, following the established integration handler pattern."

**Expected primary scenario:** S6 — Replace Existing Solution
**Expected secondary labels:** S7 secondary (structural alignment is part of the motivation)
**Expected impact label:** High
**Expected route:** Route C (must include supersession plan and migration plan)

**Expected triage output:**
- S6-High
- Route C
- Proposal must include: reason for replacement, supersession plan for old script, migration plan, rollback plan
- DP-1: Owner confirms route, supersession and migration plan scope

**Review Gate applies:** Yes — always for S6; High-impact by definition
**RCP required:** Yes — High impact, supersession plan
**Lifecycle decision applies:** Yes — old script enters Superseded state per SOP-017 R2

**Required Owner decisions:** DP-1 (route + supersession and migration plan), DP-3 (post-Review Gate), DP-4, DP-5 (must confirm old component superseded), DP-6

**Prohibited actions:**
- Deleting or disabling the old script before the replacement is confirmed working
- Skipping the supersession plan in the proposal
- Treating this as S2 (replacement, not extension)

**Pass criteria:**
- S6-High (not S2); Route C selected
- Proposal includes supersession plan and migration plan
- Old script enters Superseded state in lifecycle after replacement confirmed
- Implementation report lists files created (new handler) and files superseded (old script)

**Fail criteria:**
- Classified as S2; old script deleted before replacement confirmed; supersession plan absent

---

### T07 — Scenario S7: Structure Existing Solution

**Synthetic idea:**
"The Deliverables folder contains a mix of Dutch and English folder names. Standardize all folder names to the pattern defined in the active file naming conventions."

**Clarification:** Renaming Deliverables folders that are referenced in canonical paths requires the active canonical paths reference update protocol (currently GL-004). GL-004 must be listed as a required companion source in the RCP.

**Expected primary scenario:** S7 — Structure Existing Solution
**Expected secondary labels:** None
**Expected impact label:** Medium (large number of files affected; all renames reversible; no content changes)
**Expected route:** Route C

**Expected triage output:**
- S7-Medium
- Route C
- Proposal must include: complete list of affected folders, before/after name mapping, reference preservation plan, post-check plan
- DP-1: Owner confirms route and confirms the full scope of folders to be renamed

**Review Gate applies:** Yes — structural changes affect references and canonical paths
**RCP required:** Yes — structural changes affect multiple files and references; canonical paths reference (GL-004) must be in Field 15
**Lifecycle decision applies:** Yes

**Required Owner decisions:** DP-1 (route + complete folder scope), DP-3 (post-Review Gate), DP-4, DP-5, DP-6

**Companion source required in RCP Field 15:** Active canonical paths reference (currently: GL-004), because renamed folders may affect canonical path definitions.

**Prohibited actions:**
- Renaming any folder before DP-3 Owner decision
- Updating references in files not disclosed in the proposal
- Treating a partial rename as complete
- Failing to apply the canonical paths reference update protocol for renamed canonical paths
- Skipping the reference preservation plan

**Pass criteria:**
- S7-Medium; Route C selected
- Complete rename list in proposal before any folder renamed
- Canonical paths reference (GL-004 or current equivalent) applied for renamed canonical paths
- GL-004 listed in RCP Field 15 as required companion source
- Reference preservation plan included in proposal
- Review Gate triggered with RCP
- Implementation report lists every folder renamed

**Fail criteria:**
- Any folder renamed before DP-3 Owner decision
- Canonical paths reference protocol skipped
- Reference preservation plan absent
- Review Gate skipped

---

### T08 — Scenario S8: Governance-Relevant Idea

**Synthetic idea:**
"Add a mandatory 'context_window_tokens' integer field to all new session_logs entries to track context consumption per session."

**Expected primary scenario:** S8 — Governance-Relevant Idea
**Expected secondary labels:** None
**Expected impact label:** High (affects session_logs schema, team operating rules, and potentially AGENT.md session-log authorship rules)
**Expected route:** Route D (SOP-015 Proposal Iteration Protocol)

**Expected triage output:**
- S8-High
- Route D (SOP-015 protocol)
- Multiple governance files potentially affected: team operating instructions (CLAUDE.md), AGENT.md for session-log authors
- Schema change may also affect operational tooling
- SOP-015 versioned proposal required before any governance file is modified
- DP-1: Owner confirms S8 classification and Route D

**Review Gate applies:** Yes — always for S8; governance file changes are governance-critical; Mode 1 preferred
**RCP required:** Yes — governance file modification; Mode 1 preferred; SOP-015 must be in Field 15
**Lifecycle decision applies:** Yes

**Required Owner decisions:** DP-1 (S8 and Route D confirmation), DP-3 (post-Review Gate, exact text confirmed), DP-4 (implementation confirmation), DP-5, DP-6

**Prohibited actions:**
- Modifying CLAUDE.md, any AGENT.md, or the session_logs schema before DP-3 Owner decision
- Treating a verbal agreement as an approved SOP-015 proposal
- Applying the exact-text check (SOP-016 Check 4) without exact proposed text being in the accepted proposal
- Using Mode 3 for Review Gate without Owner override
- Classifying as S2 or S5 (governance file changes require S8/Route D)

**Pass criteria:**
- S8-High (not S2 or S5); Route D selected
- SOP-015 versioned proposal required before any governance file modified
- Review Gate (Mode 1 preferred) triggered with RCP; SOP-015 in Field 15
- Exact proposed text confirmed in proposal before Review Gate
- DP-3 post-Review Gate; DP-4 separate
- Implementation report confirms all governance files modified and exact changes made

**Fail criteria:**
- Any governance file modified before DP-3
- Mode 3 used without Owner awareness; exact text not confirmed
- Classified as S2 or S5

---

### T09 — Scenario S9: Security-Sensitive Idea

**Synthetic idea:**
"Cache the Google OAuth refresh token in the UMC PostgreSQL database to avoid re-authenticating every session."

**Expected primary scenario:** S9 — Security-Sensitive Idea
**Expected secondary labels:** S2 secondary (modification to existing Google integration handler)
**Expected impact label:** Critical (credential storage; external exposure risk; irreversible if token is leaked)
**Expected route:** Route F

**Expected triage output:**
- S9-Critical
- Route F
- Security proposal required: exact storage location, who can read the token, what happens if UMC is compromised, token rotation mechanism, rollback plan if token is leaked
- DP-1: Owner confirms S9-Critical classification

**Review Gate applies:** Yes — always; Mode 1 (external review) preferred; Mode 3 insufficient for Critical security impact
**RCP required:** Yes — Critical impact, security-sensitive, Mode 1 preferred; security-specific checks beyond standard 13 must be added in Field 12
**Lifecycle decision applies:** Yes

**Required Owner decisions:** DP-1 (S9-Critical), DP-3 (post-Review Gate with security sign-off), DP-4 (explicit implementation confirmation with security sign-off), DP-5, DP-6

**Prohibited actions:**
- Writing any OAuth token or credential to any database before DP-3 and explicit Owner security sign-off at DP-4
- Running any code that touches OAuth credentials before DP-3
- Using Mode 2 or Mode 3 as Review Gate mode without explicit Owner approval
- Treating this as S2-Medium (credential storage is always S9 regardless of technical simplicity)
- Storing credentials "temporarily" pending formal proposal

**Pass criteria:**
- S9-Critical (not S2-Medium); Route F selected
- Security proposal required before any code touches credentials
- Mode 1 Review Gate recommended; Owner confirms mode choice
- RCP includes security-specific checks in Field 12
- Implementation report confirms no credentials exposed and rollback plan available
- Explicit Owner security sign-off at DP-3 and DP-4

**Fail criteria:**
- Classified as S2-Medium; any credential written before DP-3; Mode 3 used without explicit Owner override; security proposal missing data classification or rollback plan

---

### T10 — Scenario S10: Cross-Domain Idea

**Synthetic idea:**
"Create a unified morning digest combining personal open Todoist tasks, Kamer E-commerce unfulfilled orders, and Geldstroom Regie outstanding payment reminders — delivered as a single daily overview."

**Expected primary scenario:** S10 — Cross-Domain Idea
**Expected secondary labels:** S3 secondary (new use case on existing integrations); S4 secondary (new unified output format does not currently exist)
**Expected impact label:** High
**Expected route:** Route C with personal priority gate check and project classification (both per existing operating rules, not new SOP-018 gates)

**Expected triage output:**
- S10-High
- Route C
- Before proposal preparation: personal priority gate role (currently: Sienna) evaluates whether this is a deliberate initiative per the team's operating instructions. This gate is triggered by any new initiative not in current planning; it is defined in the team's operating instructions, not in SOP-018.
- If deliberate confirmed: project classification role (currently: Marcus) assigns ICOR classification
- If ICOR accepted by Owner: multi-domain proposal (all three domain specialists assigned per role)
- Mode 2 Review Gate preferred
- DP-1: Owner confirms S10 classification and cross-domain scope

**Review Gate applies:** Yes — always for S10; Mode 2 (multi-agent review) preferred
**RCP required:** Yes — S10, High impact, multi-domain; GL-015 in Field 15
**Lifecycle decision applies:** Yes — cross-domain knowledge extraction follows GL-015 routing

**Required Owner decisions:**
- Gate check (per existing operating rules) — confirm deliberate
- ICOR classification confirmation (per existing operating rules) — confirm project classification
- DP-1 (S10 scope confirmation)
- DP-3 (post-Review Gate Owner decision on proposal)
- DP-4 (implementation confirmation)
- DP-5 (implementation report acceptance)
- DP-6 (lifecycle)

**Prohibited actions:**
- Bypassing the personal priority gate check when this idea constitutes a new initiative (per existing operating rules)
- Beginning proposal work without project classification when the gate is active
- Writing to more than one domain database in a single operation without explicit per-domain Owner approval
- Using Mode 3 for an S10 multi-domain deliverable without Owner override
- Treating the personal priority gate as a new gate created by SOP-018

**Pass criteria:**
- S10-High; Route C with existing-rule gates applied
- Personal priority gate role check triggered (existing behavioral rule, not SOP-018 gate)
- Project classification (existing behavioral rule) completed before proposal
- Multi-domain proposal covering all three domain specialists
- Mode 2 Review Gate triggered with RCP; GL-015 in Field 15
- DP-3 post-Review Gate; DP-4 separate
- Implementation report covers all three domain outputs
- GL-015 routing applied for lifecycle knowledge extraction

**Fail criteria:**
- Personal priority gate bypassed
- Project classification skipped when gate is active
- Proposal prepared without all three domain specialists
- Mode 3 used without Owner override
- Any domain database written without explicit per-domain Owner approval
- Gates described as new SOP-018 requirements (they are existing operating rules)

---

## Smoke Test Pass/Fail Summary

A complete smoke test pass requires:

| Criterion | Expected result |
|---|---|
| T01 classified correctly | S1-Low, Route A, DP-4 only, no proposal |
| T02 classified correctly | S2-Medium, Route C (direct per route matrix — no Route B check), operational system file modification, Review Gate, DP-3 post-RG |
| T03 classified correctly | S3-Medium, Route C, DP-3 post-RG |
| T04 classified correctly | S4-High, Route E, DP-2 research scope approval before research begins, brief delivered after DP-2, DP-3 post-RG |
| T05 classified correctly | S5-Medium, Route C, diagnosis proposal, operational system file modification, DP-3 post-RG |
| T06 classified correctly | S6-High, Route C, supersession plan required |
| T07 classified correctly | S7-Medium, Route C, canonical paths reference (GL-004) in RCP Field 15 |
| T08 classified correctly | S8-High, Route D, SOP-015 protocol, governance file protection, Mode 1 preferred |
| T09 classified correctly | S9-Critical, Route F, Mode 1 preferred, security sign-off at DP-4 |
| T10 classified correctly | S10-High, Route C, existing operating rule gates, Mode 2, GL-015 in RCP Field 15 |
| Route B / S2-Medium confirmed | T02 correctly shows S2-Medium routes directly to Route C without Route B check; Route B applies to Low-impact cases only |
| S1-High routing confirmed | S1-High routes to Route C (full proposal required); Route B is not assigned to any High-impact scenario |
| DP-2 sequencing confirmed | T04 correctly shows DP-2 as research scope approval; research brief delivered after DP-2, not at DP-2 |
| DP-3 sequencing confirmed | DP-3 follows Review Gate in all test cases with Review Gate |
| DP-4 separation confirmed | DP-4 is a separate step from DP-3 in all test cases; DP-3 acceptance is not an implementation authorization |
| Named agents replaced | All test cases use role-based references |
| RCP triggered correctly | T02–T10 all have RCP required |
| All explicit confirmations honored | EC-1 through EC-13 |

---

## Pack-level Implementation Order and Post-check Sequence

The governance pack must be implemented in the following order. Do not skip or reorder steps. Each step must be individually post-checked and confirmed by the Owner before the next step begins.

### Step 1 — Implement GL-018

**Actions:**
- Re-confirm GL-018 number against live `gl-index.md`
- Create `Team Knowledge/Core/Guidelines/GL-018_Idea Routing and Implementation Governance Principles.md` with exact content from the approved proposal (Sections 1 through 9 plus Changelog; the Pack-level Implementation Order section is proposal context only and does not appear in the final GL-018 file)
- Add GL-018 entry to `Team Knowledge/Core/Guidelines/gl-index.md`

**Post-check:**
- Read back the GL-018 file and confirm content matches approved proposal exactly (Sections 1–9 and Changelog; no Section 10)
- Read gl-index.md and confirm GL-018 entry is present and correctly formatted
- Confirm no other GL files were modified
- Confirm no other index files were modified
- Confirm GL-018 number is correct (no gap or conflict)
- Owner confirms Step 1 complete before Step 2 begins

### Step 2 — Implement SOP-018

**Actions:**
- Re-confirm SOP-018 number against live `SOP-index.md`
- Create `Team Knowledge/Core/SOPs/SOP-018_Idea-to-Implementation Routing Procedure.md` with exact content from the approved proposal
- Add SOP-018 entry to `Team Knowledge/Core/SOPs/SOP-index.md`

**Post-check:**
- Read back the SOP-018 file and confirm content matches approved proposal exactly
- Read SOP-index.md and confirm SOP-018 entry is present and correctly formatted
- Confirm no other SOP files were modified
- Confirm no other index files were modified
- Confirm SOP-018 number is correct (no gap or conflict)
- Owner confirms Step 2 complete before Step 3 begins

### Step 3 — Implement SOP-016 RCP Amendment

**Actions:**
- Apply the exact amendment text to `Team Knowledge/Core/SOPs/SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md`:
  - Add new Section 11 (Review Context Packet) with exact text from the approved amendment proposal
  - Amend Section 3 (Mode 1), Step 1 with exact addition text
  - Amend Section 4 (Mode 2) Procedure with exact Step 0 addition
  - Amend Section 5 (Mode 3), Step 1 with exact appended sentence
  - Add Example 4 to Section 8 (Worked Examples)

**Post-check:**
- Read back the modified SOP-016 file
- Confirm new Section 11 is present with all content from the approved proposal
- Confirm Section 3, 4, and 5 amendments are exactly as specified — no other sections changed
- Confirm Example 4 is present in Section 8
- Confirm no other sections of SOP-016 were changed
- Confirm SOP-016 section numbering is intact (1 through 10 unchanged; new Section 11 added)
- Owner confirms Step 3 complete before Step 4 is considered

### Step 4 — Execute Smoke Test (separately approved)

**Precondition:** Owner must separately and explicitly approve smoke test execution in a dedicated session. Approval of the smoke test plan proposal does not authorize execution.

**Actions (if and only if separately approved):**
- Execute all 10 smoke test cases as structured governance walkthroughs
- Record pass/fail result per case
- Record whether all explicit confirmations (EC-1 through EC-13) were honored
- Produce a smoke test execution report

**Post-check:**
- Confirm all 10 test cases pass
- Confirm no real execution occurred
- Confirm no files were created, modified, or archived
- Confirm no database writes occurred
- Owner accepts smoke test execution report

---

## Implementation Recommendation

**Recommendation: Implement Option A — new GL-018 + new SOP-018 + SOP-016 amendment.**

**Justification:**

1. **Consistent with established pattern.** The GL/SOP pairing (GL-016/SOP-016, GL-017/SOP-017) separates immutable principles (GL) from updatable procedure (SOP). GL-018 states the principles; SOP-018 states the procedure. This separation allows the procedure to be updated — new scenario classes, revised routes, corrected DPs — without requiring a governance principle change.

2. **SOP-016 amendment is narrow.** One new section (Section 11) and three minor additions to Sections 3, 4, and 5. No existing logic is changed.

3. **Minimal complete solution.** GL-018 + SOP-018 + SOP-016 amendment address the stated gap (idea-to-implementation routing) without diluting any existing governance instrument.

4. **Partial approval is not recommended.** SOP-018 without GL-018 creates an instrument without a governing principle. The GL/SOP pair must be implemented together. The SOP-016 amendment can technically stand alone but adds more value when SOP-018 is active (S9 and S10 conditions in Section 11.2).

5. **Smoke test is optional.** The smoke test validates the governance logic but is not required for the pack to be operational. It may be deferred or skipped without affecting the governance capability.

---

## Acceptance Criteria for this Smoke Test Plan

This smoke test plan is acceptable when all of the following are true:

1. All 10 test cases use synthetic ideas that are clearly distinguishable by scenario class.
2. No two test cases use the same primary scenario class.
3. All test cases use DP-1 through DP-6 per SOP-018 v04; no test case references a DP outside this sequence.
4. All test cases reference role-based agents; no test case hard-depends on a named agent.
5. T02 correctly classifies S2-Medium as Route C directly per the route matrix; no Route B check is applied; the Todoist integration handler is correctly identified as an operational system file; GL-001 is referenced as the active naming conventions reference.
6. T04 correctly shows DP-1 confirming route and classification only; DP-2 approving research scope before research begins; research brief delivered after DP-2.
7. T07 correctly references the active canonical paths reference (GL-004 or equivalent) as a required companion source in the RCP, not as an inline protocol.
8. T10 correctly identifies the personal priority gate and project classification as existing operating rules, not new SOP-018 gates.
9. The Test Assumptions and Definitions section is complete and provides all context needed for a fresh reviewer to execute the smoke test, including file category definitions from SOP-018 Section 2.4.
10. The Pack-level Implementation Order section defines all four steps with full post-check requirements, including the note that GL-018 Section 10 does not appear in the final GL-018 file.
11. The smoke test plan itself does not execute anything; approval is not authorization to run the test.
12. All 13 explicit confirmations (EC-1 through EC-13) are present and unambiguous.
13. The Route B scope note in the Test Assumptions section explicitly states that Route B applies to Low-impact ideas only and that S1-High routes to Route C. The Pass/Fail Summary includes a criterion confirming S1-High routing to Route C and confirming DP-4 is always a separate step from DP-3.

---

## Owner Decision Options

| Option | Action |
|---|---|
| Approve this smoke test plan | Smoke test may be executed in a dedicated future session — only after separate Owner approval of execution |
| Request amendments | Specific changes required; revised v05 prepared |
| Approve with modifications | Owner states modifications; v05 created before smoke test is considered for execution |
| Defer | Plan noted; no action until Owner names a condition for revisit |
| Reject | Smoke test not executed; reason stated |

---

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-06-05 | v01 | Initial proposal |
| 2026-06-05 | v02 | Added Test Assumptions and Definitions section; corrected T02 (Todoist integration handler); corrected T07 (canonical paths reference); updated T10 (role-based agents, existing operating rules); updated all DP references to v02 sequence; added Pack-level Implementation Order section; added EC-13; updated Pass/Fail Summary |
| 2026-06-05 | v03 | T02: corrected GL-007 → GL-001; removed Route B escalation framing; S2-Medium routes directly to Route C per route matrix; "operational system file" terminology used. T04: fixed DP-1 (route and classification confirmation only) and DP-2 (scope approval before research; brief delivered after DP-2). T05: "system file (skill)" → "operational system file (skill)". T08: "system files" → "governance files". Route B escalation conditions split into 1a (governance file → Route D) and 1b (operational system file → Route C). File category definitions added to Test Assumptions. Pass/Fail Summary updated for T02 and T04. Acceptance criterion 5 and 6 updated. Pending Proposals paths updated to v03. Step 1 post-check clarified (no Section 10 in GL-018 file). |
| 2026-06-05 | v04 | Acceptance criterion 3: "v02 DP numbering" corrected to "DP-1 through DP-6 per SOP-018 v04." T03 RCP note: "system file" → "operational system file." T04 RCP note: "system files" → "operational system files." Route Definitions: Route B scope note added (Low-impact only; not available for Medium/High/Critical; S1-High routes to Route C). Pass/Fail Summary: added "S1-High routing confirmed" criterion; added "DP-4 separation confirmed" row clarifying DP-3 acceptance is not implementation authorization. All SOP-018 version references updated from "v03" to "v04." Pending Proposals table: all paths updated to v04 versions. Acceptance criterion 13 added (Route B scope note and S1-High criterion in Pass/Fail Summary verified). |

---

Delivered on: 2026-06-05
Delivered at: Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/
