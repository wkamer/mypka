# Idea-to-Implementation Governance Pack — Regression Test Reference

**Created:** 2026-06-05
**Maintained by:** Larry (Team Orchestrator)
**Type:** Non-authoritative Core governance regression reference

> **This is not a GL, SOP, or Workstream.** It is a regression test reference document. It is not an authoritative source for governance rules. The authoritative sources are:
> - `Team Knowledge/Core/Guidelines/GL-018_Idea Routing and Implementation Governance Principles.md`
> - `Team Knowledge/Core/SOPs/SOP-018_Idea-to-Implementation Routing Procedure.md`
> - `Team Knowledge/Core/SOPs/SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md` (amended)
>
> This document is not added to gl-index.md or SOP-index.md.
>
> **Usage note:** When GL-018, SOP-018, or SOP-016 Section 11 is amended, re-run T01 through T10 as a logical walkthrough against the amended documents and record the results in a new dated section at the end of this document. Compare against the initial baseline (2026-06-05) to detect any regressions in governance logic.

---

## Test Assumptions and Definitions

This section makes the regression test self-contained. A reviewer with this section and the three live governance documents can execute the test without prior chat context.

### Active Governance Baseline

The following documents must be current before running the regression test:

- GL-018 — Idea Routing and Implementation Governance Principles
- SOP-018 — Idea-to-Implementation Routing Procedure
- SOP-016 (amended) — Review Gate Procedure for Governance-Relevant Deliverables (including Section 11 RCP)
- GL-016 — Review Gate for Governance-Relevant Deliverables
- GL-017 — Deliverable Lifecycle Knowledge Processing and Archiving
- SOP-015 — Proposal Iteration Protocol for System File Changes
- SOP-017 — Deliverable Lifecycle Procedure
- GL-014 — AI Team Governance
- GL-001 — File Naming Conventions (active file naming conventions reference)
- GL-004 — Canonical Paths (active canonical paths reference)

### File Category Definitions (SOP-018 Section 2.4)

| Category | Includes | Governance requirement |
|---|---|---|
| Governance file | GLs, SOPs, Workstreams, AGENT.md, CLAUDE.md, governance indexes (gl-index.md, SOP-index.md, agent-index.md), and any other document that defines team operating rules, approval gates, or governance instruments | S8 / Route D required. SOP-015 applies. |
| Operational system file | Scripts, handlers, integration files, skill files, configuration files, and operational code files | Route C or higher required. Subject to Review Gate, DP-3, and DP-4. |

### Route Definitions (SOP-018 Section 9)

| Route | Name | Review Gate required |
|---|---|---|
| Route A | Direct execution: Owner confirmation (DP-4) → Execution | No |
| Route B | Lightweight proposal: Short proposal → Owner direct review → Owner DP-3 decision → Implementation confirmation (DP-4) → Execution | No — unless any escalation condition is true |
| Route C | Standard proposal: Full proposal → Review Gate → Owner DP-3 decision → DP-4 → Execution → Implementation report → Lifecycle decision | Yes |
| Route D | Governance proposal: SOP-015 versioned proposal → Review Gate → Owner DP-3 decision → DP-4 → Execution → Implementation report → Lifecycle decision | Yes |
| Route E | Research-first: Research role brief (Owner approves scope at DP-2) → Full proposal → Review Gate → Owner DP-3 → DP-4 → Execution → Implementation report → Lifecycle decision | Yes |
| Route F | Security review: Security proposal → Mode 1 Review Gate preferred → Owner DP-3 (with security sign-off) → DP-4 (with security sign-off) → Execution → Implementation report → Lifecycle decision | Yes |

**Route B escalation conditions (SOP-018 Section 9):**

| Condition | Escalation |
|---|---|
| 1a. Governance file created, modified, or deleted | → Route D |
| 1b. Operational system file created, modified, or deleted | → Route C |
| 2. Persistent database write executed | → Route C |
| 3. Governance impact (change to team operating rules or governance instruments) | → Route D |
| 4. Security impact (credential handling, token storage, access control, external exposure) | → Route F |
| 5. Cross-domain impact (more than one domain affected) | → Route C |
| 6. External integration change (webhook, API endpoint, external service configuration) | → Route C |

**Route B scope:** Route B applies to Low-impact ideas only. Not available for Medium, High, or Critical impact. S1-High routes to Route C. Route B without escalation does not require a Review Gate and does not require an RCP unless the Owner explicitly requests one.

### Owner Decision Points (SOP-018 Section 12)

| DP | Trigger | Decision |
|---|---|---|
| DP-1 | Classification complete — Medium or higher impact | Owner confirms or redirects route recommendation |
| DP-2 | Research scope ready (Route E only) | Owner approves research scope before research begins |
| DP-3 | Proposal ready. For routes with Review Gate: Review Gate complete, findings assembled. For Route B without escalation: Owner reviews lightweight proposal directly. | Owner: accept / request amendments / defer / reject |
| DP-4 | Proposal accepted at DP-3 | Separate explicit implementation confirmation. DP-3 acceptance is not an implementation authorization. |
| DP-5 | Implementation complete | Owner accepts/rejects implementation report |
| DP-6 | Implementation report accepted at DP-5 | Owner approves each lifecycle processing destination |

**Route A:** DP-4 only.
**Route B without escalation:** DP-1, DP-3 (direct Owner review, no Review Gate package), DP-4 (separate from DP-3).
**Routes C, D:** DP-1, DP-3 (post-Review Gate), DP-4, DP-5, DP-6.
**Route E:** DP-1, DP-2 (research scope approval before research begins), DP-3 (post-Review Gate), DP-4, DP-5, DP-6.
**Route F:** DP-1, DP-3 (post-Review Gate with security sign-off), DP-4 (with security sign-off), DP-5, DP-6.

### Review Gate Modes (SOP-018 Section 2.3)

| Mode | Condition |
|---|---|
| Mode 1 — External review | Preferred for S8, S9, governance-critical deliverables |
| Mode 2 — Internal multi-agent | Preferred for S10 (cross-domain) |
| Mode 3 — Single-system fallback | Only when no external reviewer or additional agent is available. Not sufficient for Critical-impact deliverables. |

### Role-Based Definitions (SOP-018 Section 2.2)

| Role | Current assignment |
|---|---|
| Maintainer | Larry |
| Research role | Currently: Pax |
| Personal priority gate role | Currently: Sienna (existing operating rule; not created by SOP-018) |
| Project classification role | Currently: Marcus (existing operating rule; not created by SOP-018) |
| Domain specialist — Personal | Currently: Sienna |
| Domain specialist — Kamer E-commerce | Currently: Nova, Vera |
| Domain specialist — Geldstroom Regie | Currently: Finn |

---

## Test Cases T01 through T10

**Execution rules:** All test cases are logical walkthroughs only. No real execution. No file writes. No database writes. Classify each synthetic idea and verify the expected route, Owner decision points, Review Gate status, and RCP status.

---

### T01 — S1: Use Existing Capability

**Synthetic idea:** "Run the existing Todoist daily task overview script and display the results in the morning routine."

| Field | Expected |
|---|---|
| Scenario | S1 — Use Existing Capability |
| Impact | Low |
| Route | Route A |
| Owner DPs | DP-4 only |
| Review Gate | No |
| RCP | No |
| Lifecycle | No |

**Pass criteria:** Classified S1-Low; Route A; DP-4 only; no proposal, no Review Gate, no system file modified, no database write.
**Fail criteria:** Any classification other than S1-Low; Route other than A; proposal created; Review Gate triggered.

---

### T02 — S2: Extend Existing Capability

**Synthetic idea:** "Add a 'project name' column to the existing daily Todoist task overview script output."

**Clarification:** The overview script is a Todoist integration handler — an operational system file per SOP-018 Section 2.4. S2-Medium routes directly to Route C per the route matrix. No Route B check is applied.

| Field | Expected |
|---|---|
| Scenario | S2 — Extend Existing Capability |
| Impact | Medium |
| Route | Route C (direct per route matrix — no Route B check) |
| Owner DPs | DP-1, DP-3 (post-RG), DP-4, DP-5, DP-6 |
| Review Gate | Yes — operational system file modified |
| RCP | Yes — operational system file modification triggers RCP |
| Lifecycle | Yes |

**Pass criteria:** S2-Medium; Route C direct (no Route B check); full proposal required; Review Gate with RCP; DP-3 post-Review Gate; DP-4 separate.
**Fail criteria:** Route B applied; Review Gate skipped; RCP skipped; handler modified before DP-3.

---

### T03 — S3: New Idea on Existing Solution

**Synthetic idea:** "Add a weekly session-summary email digest to the existing session logging system, using the existing email integration."

| Field | Expected |
|---|---|
| Scenario | S3 — New Idea on Existing Solution |
| Impact | Medium |
| Route | Route C |
| Owner DPs | DP-1, DP-3 (post-RG), DP-4, DP-5, DP-6 |
| Review Gate | Yes |
| RCP | Yes |
| Lifecycle | Yes |

**Pass criteria:** S3-Medium (not S2 — core components not modified, new output type added); Route C; proposal before any configuration created; Review Gate with RCP; DP-3 post-Review Gate.
**Fail criteria:** Classified as S2; configuration created before DP-3; Review Gate skipped.

---

### T04 — S4: New Idea on New Solution

**Synthetic idea:** "Build a new integration with an external task-completion tracking service that automatically increments Goal progress counters when a Todoist task is marked complete."

| Field | Expected |
|---|---|
| Scenario | S4 — New Idea on New Solution |
| Secondary | S2 (if Todoist handler requires modification) |
| Impact | High |
| Route | Route E (research-first) |
| Owner DPs | DP-1 (route + classification), DP-2 (research scope approval before research begins), DP-3 (post-RG), DP-4, DP-5, DP-6 |
| Review Gate | Yes |
| RCP | Yes |
| Lifecycle | Yes |

**Pass criteria:** S4-High; Route E; DP-1 confirms route and classification; DP-2 approves research scope before research begins; research brief delivered after DP-2; proposal prepared after brief; DP-3 post-Review Gate; DP-4 separate.
**Fail criteria:** Classified S2 or S3; research begins before DP-2; proposal prepared without research brief; DP-2 treated as brief approval.

---

### T05 — S5: Fix Existing Solution

**Synthetic idea:** "The close-session skill does not log the team_tasks sweep step when there are zero open items — the sweep step is silently skipped."

| Field | Expected |
|---|---|
| Scenario | S5 — Fix Existing Solution |
| Impact | Medium |
| Route | Route C |
| Owner DPs | DP-1 (route + fix scope), DP-3 (post-RG), DP-4, DP-5, DP-6 |
| Review Gate | Yes — operational system file (skill) modified |
| RCP | Yes |
| Lifecycle | Yes |

**Pass criteria:** S5-Medium; Route C; diagnosis proposal (root cause + fix + scope boundary); Review Gate with RCP; fix scope confirmed at DP-1; DP-3 post-Review Gate.
**Fail criteria:** Skill modified before DP-3; Review Gate skipped; fix scope expanded without re-triage.

---

### T06 — S6: Replace Existing Solution

**Synthetic idea:** "Replace the current standalone Python archiving script with a dedicated handler file in the integration framework, following the established integration handler pattern."

| Field | Expected |
|---|---|
| Scenario | S6 — Replace Existing Solution |
| Secondary | S7 (structural alignment motivation) |
| Impact | High |
| Route | Route C (with supersession plan, migration plan, rollback plan) |
| Owner DPs | DP-1 (route + supersession + migration scope), DP-3 (post-RG), DP-4, DP-5 (confirm old superseded), DP-6 |
| Review Gate | Yes — always for S6 |
| RCP | Yes |
| Lifecycle | Yes — old script enters Superseded state per SOP-017 R2 |

**Pass criteria:** S6-High (not S2); proposal includes supersession + migration + rollback plan; old script not deleted before replacement confirmed; implementation report confirms old component superseded; lifecycle routes old script to Superseded.
**Fail criteria:** Classified S2; old script deleted before replacement confirmed; supersession plan absent.

---

### T07 — S7: Structure Existing Solution

**Synthetic idea:** "The Deliverables folder contains a mix of Dutch and English folder names. Standardize all folder names to the pattern defined in the active file naming conventions."

| Field | Expected |
|---|---|
| Scenario | S7 — Structure Existing Solution |
| Impact | Medium |
| Route | Route C |
| Owner DPs | DP-1 (route + complete folder scope), DP-3 (post-RG), DP-4, DP-5, DP-6 |
| Review Gate | Yes — structural changes affect references and canonical paths |
| RCP | Yes — GL-004 must be in RCP Field 15 |
| Lifecycle | Yes |

**Pass criteria:** S7-Medium; Route C; complete rename list in proposal; canonical paths reference (GL-004) in RCP Field 15; reference preservation plan included; Review Gate with RCP; implementation report lists every folder renamed.
**Fail criteria:** Any folder renamed before DP-3; canonical paths protocol skipped; reference preservation plan absent.

---

### T08 — S8: Governance-Relevant Idea

**Synthetic idea:** "Add a mandatory 'context_window_tokens' integer field to all new session_logs entries to track context consumption per session."

| Field | Expected |
|---|---|
| Scenario | S8 — Governance-Relevant Idea |
| Impact | High |
| Route | Route D (SOP-015 Proposal Iteration Protocol) |
| Owner DPs | DP-1 (S8 + Route D), DP-3 (post-RG, exact text confirmed), DP-4, DP-5, DP-6 |
| Review Gate | Yes — always; Mode 1 preferred |
| RCP | Yes — SOP-015 in Field 15 |
| Lifecycle | Yes |

**Pass criteria:** S8-High (not S2 or S5); Route D; SOP-015 versioned proposal before any governance file modified; Review Gate Mode 1 preferred with RCP; exact proposed text in proposal before Review Gate; DP-3 post-Review Gate.
**Fail criteria:** Any governance file modified before DP-3; Mode 3 used without Owner awareness; classified as S2 or S5.

---

### T09 — S9: Security-Sensitive Idea

**Synthetic idea:** "Cache the Google OAuth refresh token in the UMC PostgreSQL database to avoid re-authenticating every session."

| Field | Expected |
|---|---|
| Scenario | S9 — Security-Sensitive Idea |
| Secondary | S2 (Google integration handler modification) |
| Impact | Critical |
| Route | Route F |
| Owner DPs | DP-1 (S9-Critical), DP-3 (post-RG with security sign-off), DP-4 (with security sign-off), DP-5, DP-6 |
| Review Gate | Yes — always; Mode 1 preferred; Mode 3 insufficient for Critical |
| RCP | Yes — security-specific checks in Field 12 beyond standard 13 |
| Lifecycle | Yes |

**Pass criteria:** S9-Critical (not S2-Medium); Route F; security proposal required before any code touches credentials; Mode 1 recommended; RCP includes security-specific checks; explicit security sign-off at DP-3 and DP-4; implementation report confirms no credentials exposed and rollback plan available.
**Fail criteria:** Classified S2-Medium; any credential written before DP-3; Mode 3 without explicit Owner override; security proposal missing data classification or rollback plan.

---

### T10 — S10: Cross-Domain Idea

**Synthetic idea:** "Create a unified morning digest combining personal open Todoist tasks, Kamer E-commerce unfulfilled orders, and Geldstroom Regie outstanding payment reminders — delivered as a single daily overview."

| Field | Expected |
|---|---|
| Scenario | S10 — Cross-Domain Idea |
| Secondary | S3 (new use case on existing integrations), S4 (new unified output format) |
| Impact | High |
| Route | Route C with personal priority gate (Sienna, existing rule) and project classification (Marcus, existing rule) |
| Owner DPs | Gate check (existing rules), ICOR confirmation (existing rules), DP-1 (S10 scope), DP-3 (post-RG), DP-4, DP-5, DP-6 |
| Review Gate | Yes — always; Mode 2 preferred |
| RCP | Yes — GL-015 in Field 15 |
| Lifecycle | Yes — cross-domain knowledge extraction follows GL-015 routing |

**Pass criteria:** S10-High; Route C with existing-rule gates applied; personal priority gate triggered; project classification completed before proposal; multi-domain proposal covering all three specialists; Mode 2 Review Gate with RCP; GL-015 in Field 15; DP-3 post-Review Gate; implementation report covers all three domains; GL-015 routing applied for lifecycle.
**Fail criteria:** Personal priority gate bypassed; project classification skipped; proposal without all three specialists; Mode 3 without Owner override; any domain database written without per-domain Owner approval; gates described as new SOP-018 requirements.

---

## Pass/Fail Criteria Summary

A complete regression test pass requires all of the following:

| Criterion | Expected result |
|---|---|
| T01 correct | S1-Low, Route A, DP-4 only, no proposal |
| T02 correct | S2-Medium, Route C direct (no Route B check), operational system file, Review Gate, DP-3 post-RG |
| T03 correct | S3-Medium, Route C, DP-3 post-RG |
| T04 correct | S4-High, Route E, DP-2 scope approval before research, brief after DP-2, DP-3 post-RG |
| T05 correct | S5-Medium, Route C, diagnosis proposal, operational system file, DP-3 post-RG |
| T06 correct | S6-High, Route C, supersession plan required, old component → Superseded |
| T07 correct | S7-Medium, Route C, GL-004 in RCP Field 15 |
| T08 correct | S8-High, Route D, SOP-015 protocol, governance file protection, Mode 1 preferred |
| T09 correct | S9-Critical, Route F, Mode 1 preferred, security sign-off at DP-3 and DP-4 |
| T10 correct | S10-High, Route C, existing operating rule gates, Mode 2 preferred, GL-015 in RCP Field 15 |
| Route B / S2-Medium | T02: S2-Medium routes directly to Route C; no Route B check applied |
| S1-High routing | S1-High → Route C; Route B not assigned to any High-impact scenario |
| DP-2 sequencing | T04: DP-2 is scope approval; research brief delivered after DP-2 |
| DP-3 sequencing | DP-3 follows Review Gate in all test cases with Review Gate |
| DP-4 separation | DP-4 always separate from DP-3; DP-3 acceptance is not implementation authorization |
| Role-based agents | All test cases use role-based references |
| RCP triggered | T02 through T10 all have RCP required |
| Route B no RCP | Route B without escalation does not require RCP unless Owner explicitly requests one |
| Route B escalation | When any escalation condition is true, escalated route Review Gate and RCP rules apply in full |
| Explicit confirmations | EC-1 through EC-13 honored |

---

## Baseline Results — Initial Run (2026-06-05)

**Executed by:** Larry (Team Orchestrator)
**Date:** 2026-06-05
**Governance pack version:** v05 (GL-018, SOP-018, SOP-016 with RCP amendment — all live)
**Source report:** `step-4-smoke-test-execution-report.md` (now archived)

| Test case | Actual classification | Actual route | Pass/Fail |
|---|---|---|---|
| T01 | S1-Low | Route A | PASS |
| T02 | S2-Medium | Route C (direct, no Route B check) | PASS |
| T03 | S3-Medium | Route C | PASS |
| T04 | S4-High | Route E | PASS |
| T05 | S5-Medium | Route C | PASS |
| T06 | S6-High | Route C | PASS |
| T07 | S7-Medium | Route C | PASS |
| T08 | S8-High | Route D | PASS |
| T09 | S9-Critical | Route F | PASS |
| T10 | S10-High | Route C | PASS |

**All pass/fail criteria:** PASS (all 20 criteria met)
**Explicit confirmations EC-1 through EC-13:** All honored
**Route B without escalation:** Confirmed — no Review Gate, no RCP, DP-3 and DP-4 still required
**Route B escalation:** Confirmed — any escalation condition triggers full escalated-route governance

**Overall baseline verdict:** PASSED — all 10 test cases passed, all criteria met.

---

Delivered on: 2026-06-05
Delivered at: Team Knowledge/Core/Documents/
