# PROPOSAL — Idea-to-Implementation Governance Pack: Smoke Test Plan

**Proposal status:** Draft v01
**Prepared by:** Larry (Team Orchestrator)
**Date:** 2026-06-05
**For:** Owner Walter Kamer
**Tests:** idea-routing-gl-proposal-v01.md, idea-routing-sop-proposal-v01.md, review-context-packet-sop-016-amendment-proposal-v01.md
**Governance baseline:** GL-014, GL-015, GL-016, GL-017, GL-018 (pending), SOP-015, SOP-016, SOP-017, SOP-018 (pending), SOP-016 RCP amendment (pending)

---

> **PROPOSAL ONLY.**
> This smoke test plan is a proposal for review. No smoke test is executed until the Owner explicitly approves it. No real execution occurs during the smoke test unless separately approved. No files are created, modified, or moved. No database writes occur.

---

## Purpose

This smoke test plan verifies that the Idea-to-Implementation Governance Pack — GL-018, SOP-018, and the SOP-016 RCP amendment — correctly routes 10 synthetic ideas, one for each scenario class S1 through S10.

A smoke test is a structured walkthrough. It confirms that the governance logic is consistent, that the scenario classes are distinguishable, and that the routes, decision points, and prohibited actions produce the correct outcomes for representative inputs.

The smoke test does not test implementation. It tests the governance logic.

---

## Explicit Confirmations

The following constraints apply to the entire smoke test. They may not be overridden by any individual test case.

| # | Constraint |
|---|---|
| EC-1 | No real execution during smoke test unless separately approved by the Owner in a new session |
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
| EC-12 | All 10 test cases are synthetic — they describe fictional ideas for governance testing purposes only |

---

## Smoke Test Governance Baseline

The reviewer and triage agent must use the following governance baseline for all 10 test cases:

- GL-018 (pending approval — use proposal content from `idea-routing-gl-proposal-v01.md`)
- SOP-018 (pending approval — use proposal content from `idea-routing-sop-proposal-v01.md`)
- SOP-016 RCP amendment (pending approval — use proposal content from `review-context-packet-sop-016-amendment-proposal-v01.md`)
- GL-016 (active — `GL-016_Review Gate for Governance-Relevant Deliverables.md`)
- SOP-016 (active — `SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md`)
- GL-017 (active — `GL-017_Deliverable Lifecycle Knowledge Processing and Archiving.md`)
- SOP-017 (active — `SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md`)
- SOP-015 (active — `SOP-015_Proposal Iteration Protocol for System File Changes.md`)

No other sources are authoritative for this smoke test.

---

## Test Cases

---

### T01 — Scenario S1: Use Existing Capability

**Synthetic idea:**
"Run the existing Todoist daily task overview script and display the results in the morning routine."

**Expected primary scenario:** S1 — Use Existing Capability
**Expected secondary labels:** None
**Expected impact label:** Low

**Expected route:** Route A — Direct execution with Owner confirmation

**Expected triage output:**
- Scenario: S1
- Impact: Low
- Route: Route A
- Required Owner decision: DP-5 — Owner confirmation before execution
- No proposal required

**Review Gate applies:** No — no system file modified; no governance-relevant deliverable produced

**Lifecycle decision applies after acceptance:** No

**Required Owner decision:** Confirm direct execution (DP-5 only)

**Prohibited actions:**
- Creating a proposal document
- Modifying the Todoist script
- Writing any record to team_tasks or session_logs (beyond normal session tracking)
- Treating the output of the script as a governance deliverable requiring Review Gate

**Pass criteria:**
- Idea correctly classified as S1-Low
- Routed to Route A
- Owner confirmation obtained before execution
- No proposal created
- No Review Gate triggered
- No lifecycle decision initiated
- No system file modified

**Fail criteria:**
- Any classification other than S1-Low
- Any route other than Route A
- A proposal document created
- A Review Gate initiated
- Any system file modified without authorization

---

### T02 — Scenario S2: Extend Existing Capability

**Synthetic idea:**
"Add a 'project name' column to the existing daily Todoist task overview output in the meta integration handler."

**Expected primary scenario:** S2 — Extend Existing Capability
**Expected secondary labels:** None
**Expected impact label:** Medium

**Expected route:** Route C — Standard proposal → Review Gate → Execution → Implementation report

**Expected triage output:**
- Scenario: S2
- Impact: Medium
- Route: Route C
- DP-1: Owner confirms route recommendation
- Deliverable: Full proposal required before any handler modification

**Review Gate applies:** Yes — system file (integration handler) is modified

**Lifecycle decision applies after acceptance:** Yes

**Required Owner decisions:** DP-1 (route confirmation), DP-3 (proposal acceptance), DP-4 (Review Gate outcome), DP-5 (implementation confirmation), DP-6 (implementation report acceptance), DP-7 (lifecycle decision)

**Required Review Context Packet:** Yes — system file modification triggers RCP requirement per SOP-016 amendment Section 11.2

**Prohibited actions:**
- Modifying the integration handler before proposal approval
- Skipping the Review Gate
- Skipping the RCP
- Treating the triage output as an implementation authorization

**Pass criteria:**
- Idea correctly classified as S2-Medium
- Routed to Route C
- Proposal document required before any handler modification
- Review Gate triggered with RCP prepared
- Implementation report required
- Lifecycle decision initiated after acceptance
- All 6 decision points (DP-1 through DP-7) identified

**Fail criteria:**
- Any classification other than S2-Medium
- Handler modified without proposal
- Review Gate skipped
- RCP not prepared for Review Gate
- Lifecycle decision skipped

---

### T03 — Scenario S3: New Idea on Existing Solution

**Synthetic idea:**
"Add a weekly session-summary digest to the existing session logging system, delivered as an email every Sunday evening."

**Expected primary scenario:** S3 — New Idea on Existing Solution
**Expected secondary labels:** None
**Expected impact label:** Medium

**Expected route:** Route C — Standard proposal → Review Gate → Execution → Implementation report

**Expected triage output:**
- Scenario: S3
- Impact: Medium
- Route: Route C
- New behavior (weekly digest) on existing infrastructure (session logging + email integration)
- DP-1: Owner confirms route

**Review Gate applies:** Yes — new email trigger and new script configuration; system file potentially modified

**Lifecycle decision applies after acceptance:** Yes

**Required Owner decisions:** DP-1, DP-3, DP-4, DP-5, DP-6, DP-7

**Required Review Context Packet:** Yes — per SOP-016 amendment Section 11.2 (system file modified)

**Prohibited actions:**
- Creating the email trigger or digest script before proposal approval
- Assuming the existing session log format can be reused without verifying it
- Treating this as S2 because it uses existing infrastructure (it adds a new output type, not an extension of an existing output)

**Pass criteria:**
- Idea correctly classified as S3-Medium (not S2 — no modification to existing session log behavior, new output type added)
- Route C selected
- Proposal required before any script or configuration created
- Review Gate triggered with RCP
- Implementation report required

**Fail criteria:**
- Classified as S2 (incorrect — existing behavior is not modified, new behavior is added)
- Email trigger created before proposal approval
- Review Gate skipped

---

### T04 — Scenario S4: New Idea on New Solution

**Synthetic idea:**
"Build a new integration with a task-completion tracking tool that automatically increments Goal progress counters when a Todoist task is marked complete."

**Expected primary scenario:** S4 — New Idea on New Solution
**Expected secondary labels:** S2 secondary (if Todoist handler is extended to emit a completion event)
**Expected impact label:** High

**Expected route:** Route E — Pax research brief → Full proposal → Review Gate → Execution → Implementation report

**Expected triage output:**
- Scenario: S4
- Impact: High
- Route: Route E
- Requires Pax research: what tracking approaches exist? What are the integration points? What are the risks?
- DP-1: Owner approves research scope
- DP-2: Owner approves research brief before proposal begins

**Review Gate applies:** Yes — new integration, new scripts, new system components

**Lifecycle decision applies after acceptance:** Yes

**Required Owner decisions:** DP-1 (route + research scope), DP-2 (research brief), DP-3, DP-4, DP-5, DP-6, DP-7

**Required Review Context Packet:** Yes — High impact, new integration, system files created

**Prohibited actions:**
- Beginning any implementation before research brief is approved
- Treating this as S2 or S3 because Todoist is an existing integration
- Skipping the Pax research step
- Creating any new script or database schema before proposal is reviewed

**Pass criteria:**
- Idea correctly classified as S4-High
- Route E selected
- Pax research brief required before proposal
- Owner approves research scope at DP-1 and research brief at DP-2
- Full proposal required after research
- Review Gate with RCP triggered
- Implementation report required

**Fail criteria:**
- Classified as S2 or S3 (incorrect — new integration system required)
- Implementation begins without Pax research
- Proposal prepared without research brief

---

### T05 — Scenario S5: Fix Existing Solution

**Synthetic idea:**
"The close-session skill does not log the team_tasks sweep when there are zero open items — the sweep step is silently skipped."

**Expected primary scenario:** S5 — Fix Existing Solution
**Expected secondary labels:** None
**Expected impact label:** Medium

**Expected route:** Route C — Diagnosis proposal → Review Gate → Execution → Implementation report

**Expected triage output:**
- Scenario: S5
- Impact: Medium
- Route: Route C
- Proposal must include: diagnosis (root cause), proposed fix, scope boundary (do not fix beyond the stated defect), post-check criteria
- DP-1: Owner confirms route

**Review Gate applies:** Yes — skill file modified

**Lifecycle decision applies after acceptance:** Yes

**Required Owner decisions:** DP-1, DP-3 (including confirmation that fix scope is limited to the stated defect), DP-4, DP-5, DP-6, DP-7

**Required Review Context Packet:** Yes — system file (skill) modified

**Prohibited actions:**
- Fixing the skill before proposal approval
- Expanding the fix scope beyond the stated defect without re-triage
- Treating the verbal description of the bug as an approved fix specification
- Skipping the Review Gate for the fix proposal

**Pass criteria:**
- Idea correctly classified as S5-Medium
- Route C selected
- Diagnosis + fix proposal required before any skill file is modified
- Review Gate triggered with RCP
- Fix scope limited to stated defect
- Implementation report required

**Fail criteria:**
- Skill modified before proposal approval
- Review Gate skipped
- Fix scope expanded beyond stated defect without re-triage

---

### T06 — Scenario S6: Replace Existing Solution

**Synthetic idea:**
"Replace the current standalone Python script for WhatsApp archiving with a dedicated handler file in the meta integration, following the established integration handler pattern."

**Expected primary scenario:** S6 — Replace Existing Solution
**Expected secondary labels:** S7 secondary (structural alignment is part of the motivation)
**Expected impact label:** High

**Expected route:** Route C — Standard proposal (including supersession plan and migration plan) → Review Gate → Execution → Implementation report

**Expected triage output:**
- Scenario: S6
- Impact: High
- Route: Route C
- Proposal must include: reason for replacement, supersession plan (what happens to the old script), migration plan, rollback plan
- DP-1: Owner confirms route

**Review Gate applies:** Yes — always for S6; replacement is High-impact

**Lifecycle decision applies after acceptance:** Yes — old script enters Superseded state per SOP-017 R2

**Required Owner decisions:** DP-1, DP-3 (including supersession and migration plan), DP-4, DP-5, DP-6, DP-7

**Required Review Context Packet:** Yes — High impact, system files created and superseded

**Prohibited actions:**
- Deleting or disabling the old script before the replacement is confirmed working
- Skipping the supersession plan
- Skipping the migration plan
- Treating this as S2 (extension) — the old component is retired, not extended
- Beginning implementation before Review Gate passes

**Pass criteria:**
- Idea correctly classified as S6-High (not S2)
- Route C selected
- Proposal includes supersession plan and migration plan
- Review Gate triggered with RCP
- Old script enters Superseded state in lifecycle after replacement confirmed
- Implementation report lists both files created (new handler) and files superseded (old script)

**Fail criteria:**
- Classified as S2 (incorrect — replacement, not extension)
- Old script deleted before replacement confirmed working
- Supersession plan absent from proposal
- Review Gate skipped

---

### T07 — Scenario S7: Structure Existing Solution

**Synthetic idea:**
"The Deliverables folder contains a mix of Dutch and English folder names. Standardize all folder names to the English pattern defined in GL-001."

**Expected primary scenario:** S7 — Structure Existing Solution
**Expected secondary labels:** S8 secondary — GL-001 compliance enforcement touches governance conventions
**Expected impact label:** Medium (large number of files affected but all renames are reversible and no content changes)

**Expected route:** Route C — Standard proposal (scope of renames, before/after mapping) → Review Gate → Execution → Implementation report

**Expected triage output:**
- Scenario: S7
- Impact: Medium
- Route: Route C
- Proposal must include: complete list of affected folders, before/after name mapping, reference preservation plan (any documents linking to these folders), post-check plan
- DP-1: Owner confirms route and confirms the full scope of folders to be renamed

**Review Gate applies:** Yes — structural changes affect references and canonical paths

**Lifecycle decision applies after acceptance:** Yes

**Required Owner decisions:** DP-1 (route + scope confirmation), DP-3 (proposal with full rename list), DP-4, DP-5, DP-6, DP-7

**Required Review Context Packet:** Yes — structural changes affect multiple files and references

**Prohibited actions:**
- Renaming any folder before the complete scope is approved
- Updating references in files not disclosed in the proposal
- Treating a partial rename as complete
- Skipping GL-004 path-change protocol for any renamed canonical path

**Pass criteria:**
- Idea correctly classified as S7-Medium
- Route C selected
- Complete rename list required in proposal before any folder is renamed
- GL-004 path-change protocol applied for any renamed canonical path
- Reference preservation plan included in proposal
- Review Gate triggered with RCP
- Implementation report lists every folder renamed

**Fail criteria:**
- Any folder renamed before proposal approval
- GL-004 path-change protocol skipped
- Reference preservation plan absent
- Review Gate skipped

---

### T08 — Scenario S8: Governance-Relevant Idea

**Synthetic idea:**
"Add a mandatory 'context_window_tokens' integer field to all new session_logs entries — to track context consumption per session."

**Expected primary scenario:** S8 — Governance-Relevant Idea
**Expected secondary labels:** None
**Expected impact label:** High (affects session_logs schema, CLAUDE.md session logging rule, and potentially AGENT.md session log authorship rules)

**Expected route:** Route D — SOP-015 Proposal Iteration Protocol → Review Gate → Execution → Implementation report

**Expected triage output:**
- Scenario: S8
- Impact: High
- Route: Route D (SOP-015 protocol)
- Multiple system files potentially affected: CLAUDE.md, AGENT.md for session-log authors, session_logs table schema
- SOP-015 versioned proposal required before any file is modified
- DP-1: Owner confirms S8 classification and Route D

**Review Gate applies:** Yes — always for S8; governance document changes are always governance-critical; Mode 1 preferred

**Lifecycle decision applies after acceptance:** Yes

**Required Owner decisions:** DP-1 (S8 confirmation and Route D), DP-3 (SOP-015 versioned proposal), DP-4 (Review Gate with exact-text confirmation), DP-5, DP-6, DP-7

**Required Review Context Packet:** Yes — governance document modification; Mode 1 preferred

**Prohibited actions:**
- Modifying CLAUDE.md, any AGENT.md, or the session_logs schema before SOP-015 proposal is approved
- Treating a verbal agreement as an approved SOP-015 proposal
- Applying the exact-text check (SOP-016 Check 4) without the exact proposed text being in the approved proposal
- Using Mode 3 (self-review) as the Review Gate mode without Owner approval

**Pass criteria:**
- Idea correctly classified as S8-High (not S2 or S5)
- Route D selected
- SOP-015 versioned proposal required before any system file modified
- Review Gate triggered (Mode 1 preferred) with RCP
- Exact proposed text confirmed in proposal before Review Gate
- Implementation report confirms all system files modified and exact changes made
- Lifecycle decision initiated

**Fail criteria:**
- Any system file modified before SOP-015 proposal approved
- Review Gate mode selected without Owner awareness
- Exact text not confirmed in proposal before Review Gate
- Classified as S2 or S5 (incorrect — governance document changes require S8/Route D)

---

### T09 — Scenario S9: Security-Sensitive Idea

**Synthetic idea:**
"Cache the Google OAuth refresh token in the UMC PostgreSQL database to avoid re-authenticating every session."

**Expected primary scenario:** S9 — Security-Sensitive Idea
**Expected secondary labels:** S2 secondary (modification to existing Google integration)
**Expected impact label:** Critical (credential storage; external exposure risk; irreversible if token is leaked)

**Expected route:** Route F — Security proposal (data classification, storage location, access scope, risk assessment, rollback plan) → Mode 1 Review Gate preferred → Execution → Implementation report with explicit security confirmation

**Expected triage output:**
- Scenario: S9
- Impact: Critical
- Route: Route F
- Security proposal required: where exactly is the token stored? Who can read it? What happens if UMC is compromised? Is there a token rotation mechanism? What is the rollback plan if a stored token is leaked?
- DP-1: Owner confirms S9-Critical classification

**Review Gate applies:** Yes — always; Mode 1 (external review) preferred; Mode 3 is insufficient for Critical security impact

**Lifecycle decision applies after acceptance:** Yes

**Required Owner decisions:** DP-1 (S9-Critical confirmation), DP-3 (security proposal with explicit security sign-off), DP-4 (Mode 1 Review Gate), DP-5 (explicit security sign-off before execution), DP-6, DP-7

**Required Review Context Packet:** Yes — Critical impact; security-sensitive; Mode 1 preferred

**Prohibited actions:**
- Writing any OAuth token or credential to any database before proposal approval and explicit Owner security sign-off
- Running any code that touches the OAuth token before proposal approval
- Using Mode 2 or Mode 3 as the Review Gate mode without explicit Owner approval
- Storing credentials "temporarily" pending a formal proposal
- Treating this as S2-Medium (the security dimension elevates this to S9-Critical regardless of the technical simplicity)

**Pass criteria:**
- Idea correctly classified as S9-Critical (not S2-Medium)
- Route F selected
- Security proposal required before any code touches credentials
- Mode 1 Review Gate recommended with Owner confirmation of mode choice
- RCP prepared and includes security-specific checks beyond the standard 13
- Implementation report confirms no credentials are exposed and rollback plan is available
- Explicit Owner security sign-off at DP-5

**Fail criteria:**
- Classified as S2-Medium (incorrect — credential storage is always S9)
- Any credential written before proposal approval
- Mode 3 used for Critical security impact without explicit Owner override
- Security proposal missing data classification or rollback plan
- RCP missing security-specific checks

---

### T10 — Scenario S10: Cross-Domain Idea

**Synthetic idea:**
"Create a unified morning digest that combines personal open Todoist tasks, Kamer E-commerce unfulfilled orders, and Geldstroom Regie outstanding payment reminders — delivered as a single daily overview."

**Expected primary scenario:** S10 — Cross-Domain Idea
**Expected secondary labels:** S3 secondary (new use case on existing integrations); S4 secondary (new unified output format does not currently exist)
**Expected impact label:** High

**Expected route:** Sienna Priority Gate (is this deliberate?) → Marcus ICOR classification → Multi-agent proposal → Mode 2 Review Gate preferred → Execution → Implementation report

**Expected triage output:**
- Scenario: S10
- Impact: High
- Route: Sienna Priority Gate first (new initiative not in current planning)
- If deliberate confirmed: Marcus ICOR classification
- If ICOR accepted: multi-agent proposal (Personal domain lead: Sienna; Kamer E-commerce domain: Nova or Vera; Geldstroom Regie domain: Finn; Orchestration: Larry)
- Mode 2 Review Gate preferred
- DP-1: Sienna gate (is this deliberate initiative?)
- DP-2: Marcus ICOR classification approval
- DP-3: Multi-agent proposal acceptance
- DP-4: Review Gate
- DP-5: Implementation confirmation
- DP-6: Implementation report acceptance
- DP-7: Lifecycle decision (cross-domain routing per GL-015)

**Review Gate applies:** Yes — always for S10; Mode 2 (multi-agent) preferred

**Lifecycle decision applies after acceptance:** Yes — cross-domain knowledge extraction requires GL-015 routing

**Required Owner decisions:** All 7 decision points; Owner must explicitly confirm each domain's inclusion

**Required Review Context Packet:** Yes — S10, High impact, multi-domain

**Prohibited actions:**
- Bypassing the Sienna Priority Gate (any new initiative must pass this gate)
- Beginning any implementation before Marcus ICOR classification is confirmed
- Writing to more than one domain database in a single operation
- Proceeding without all three domain specialists contributing to the proposal
- Using Mode 3 (self-review) for an S10 multi-domain proposal

**Pass criteria:**
- Idea correctly classified as S10-High
- Sienna Priority Gate triggered first
- Marcus ICOR classification completed before proposal work begins
- Multi-agent proposal involving all three domain specialists
- Mode 2 Review Gate triggered with RCP
- Implementation report covers all three domain outputs
- GL-015 cross-domain routing applied for lifecycle knowledge extraction
- All 7 decision points identified and presented to Owner

**Fail criteria:**
- Sienna Priority Gate bypassed
- Marcus ICOR classification skipped
- Proposal prepared without all three domain specialists
- Mode 3 used for S10 without Owner override
- Any domain database written without explicit per-domain Owner approval

---

## Implementation Recommendation

### Options Analysis

**Option A — New GL-018 + New SOP-018 + SOP-016 amendment**
Creates a new GL/SOP pair for idea routing, adds RCP to SOP-016.
- Pros: Consistent with the GL/SOP pairing pattern (GL-016/SOP-016, GL-017/SOP-017). Principles are in the GL (stable, rarely changes); procedure is in the SOP (can be updated without touching the GL). Separation is clean and familiar.
- Cons: Adds two new governance documents. Requires both to be maintained in sync.

**Option B — New SOP-018 only + SOP-016 amendment (no new GL)**
- Pros: Fewer documents. Faster to implement.
- Cons: Breaks the GL/SOP pairing pattern. Principles are buried in the SOP, making them harder to reference or enforce independently. Future updates to the procedure risk accidentally changing principles. The governance framework loses structural consistency.

**Option C — Amendments to existing governance only (no new GL, no new SOP)**
Adds scenario classification to GL-014 or another existing GL; adds routing steps to SOP-016 or SOP-017.
- Pros: No new documents.
- Cons: Dilutes existing instruments with tangential concerns. GL-014 governs approval gates broadly — adding scenario classification overloads its purpose. SOP-016 governs review procedures — adding routing logic overloads its purpose. Maintenance becomes impossible without cross-document conflicts.

**Option D — Other structure**
No compelling alternative structure has been identified that improves on Option A without creating new problems.

### Recommendation

**Implement Option A: New GL-018 + New SOP-018 + SOP-016 amendment.**

Justification:
1. The GL/SOP pairing is the established pattern. GL-016/SOP-016 and GL-017/SOP-017 demonstrate that this pattern works and scales. Deviating from it creates an inconsistency that must be explained to every future reviewer and agent.
2. Separating principles (GL-018) from procedure (SOP-018) allows the procedure to be updated — new scenario classes, revised impact labels, updated routes — without requiring a governance principle change. This is the main reason the pattern exists.
3. The SOP-016 amendment is narrow and self-contained. It adds one new section (Section 11) and three minor amendments to existing sections. It does not change any existing review logic.
4. Together, GL-018 + SOP-018 + SOP-016 amendment constitute the minimal complete solution for the stated governance gap.

The recommendation is to approve all three components as a single governance pack, or to defer all three. Partial approval (e.g., SOP-018 without GL-018) creates an instrument without a governing principle, which is inconsistent with the governance design.

---

## Smoke Test Pass/Fail Summary

A complete smoke test pass requires:

| Criterion | Expected result |
|---|---|
| T01 classified correctly | S1-Low, Route A, no proposal |
| T02 classified correctly | S2-Medium, Route C, proposal required |
| T03 classified correctly | S3-Medium, Route C, proposal required |
| T04 classified correctly | S4-High, Route E, research first |
| T05 classified correctly | S5-Medium, Route C, diagnosis proposal |
| T06 classified correctly | S6-High, Route C, supersession plan required |
| T07 classified correctly | S7-Medium, Route C, GL-004 protocol applied |
| T08 classified correctly | S8-High, Route D, SOP-015 protocol |
| T09 classified correctly | S9-Critical, Route F, Mode 1 preferred |
| T10 classified correctly | S10-High, Sienna gate, Marcus ICOR, Mode 2 |
| All prohibited actions confirmed absent | No execution, no file writes, no DB writes |
| All explicit confirmations (EC-1 through EC-12) honored | Confirmed |
| RCP triggered for all applicable test cases | T02, T03, T04, T05, T06, T07, T08, T09, T10 |
| No real execution | Confirmed |

---

## Acceptance Criteria for this Smoke Test Plan

This smoke test plan is acceptable when all of the following are true:

1. All 10 test cases have synthetic ideas that are clearly distinguishable by scenario class.
2. No test case uses the same scenario class as another test case.
3. The prohibited actions for each test case are specific to that scenario class and do not simply repeat the global explicit confirmations.
4. The pass/fail criteria for each test case are verifiable without system access.
5. The implementation recommendation states a clear recommendation with a justified rationale.
6. The smoke test plan does not itself require any execution to read or review.
7. The explicit confirmations (EC-1 through EC-12) are complete and unambiguous.

---

## Owner Decision Options

| Option | Action |
|---|---|
| Approve this smoke test plan | Smoke test may be executed as a structured governance walkthrough in a future session |
| Request amendments | Specific changes required; revised v02 prepared |
| Approve with modifications | Owner states modifications; v02 created before smoke test is executed |
| Defer | Smoke test noted; no action until Owner names a condition for execution |
| Reject | Smoke test not executed; reason stated |

---

Delivered on: 2026-06-05
Delivered at: Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/
