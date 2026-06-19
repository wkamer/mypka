# PROPOSAL — SOP-018: Idea-to-Implementation Routing Procedure

**Proposal status:** Draft v01
**Prepared by:** Larry (Team Orchestrator)
**Date:** 2026-06-05
**For:** Owner Walter Kamer
**Governance baseline:** GL-014, GL-015, GL-016, GL-017, GL-018 (pending approval), SOP-015, SOP-016, SOP-017
**Proposed SOP number:** SOP-018
**Proposed filename:** `SOP-018_Idea-to-Implementation Routing Procedure.md`

---

> **PROPOSAL ONLY.**
> Nothing in this document is implemented, active, or authoritative until the Owner explicitly approves it. No system files are modified. No indexes are updated. No SOP file is created. No execution follows from this document without explicit Owner approval.

> **GL-018 dependency.** SOP-018 implements the principles stated in GL-018. This SOP proposal assumes GL-018 has been approved or is reviewed concurrently. If GL-018 is not approved, this SOP proposal must be revised or withdrawn.

---

## Purpose of this Proposal

SOP-016 and SOP-017 govern what happens after a governance-relevant deliverable exists. SOP-015 governs how system-file change proposals are iterated. No existing SOP defines how an idea moves from intake to the correct implementation path.

This proposal defines SOP-018 — the step-by-step procedure for routing any idea from intake through classification, route selection, proposal preparation (where required), Review Gate, implementation, and lifecycle decision.

---

## Proposed SOP-018 Content

The following is the complete proposed content of SOP-018. This content is not active. It is presented for Owner review.

---

# SOP-018 — Idea-to-Implementation Routing Procedure

---

## 1. Purpose and Relationship to GL-018

This SOP defines the operational procedure for routing every idea — from intake through classification, route selection, required deliverable preparation, Owner decision points, Review Gate, implementation approval, implementation reporting, and lifecycle decision.

This SOP implements the principles stated in GL-018 (Idea Routing and Implementation Governance Principles). GL-018 states the why and the what. This SOP states the how and when.

This SOP is tool-agnostic and system-agnostic. It applies to any system, agent, tool, script, automation, orchestration layer, or human-assisted workflow that processes ideas within the myPKA AI team.

---

## 2. Role Definitions

| Role | Responsibility |
|---|---|
| Owner | Walter Kamer. Provides all approval decisions. Sole decision authority for route confirmation, proposal acceptance, implementation authorization, and lifecycle decisions. Not delegable. |
| Maintainer | Larry (Team Orchestrator). Receives every idea, performs or routes triage, assigns classification, delegates to the appropriate specialist, tracks pipeline state, surfaces open items at session close. |
| Specialist | The assigned team member responsible for producing the deliverable for the assigned route. Identified during classification. |
| Reviewer | The agent or external system that reviews the deliverable per SOP-016 before Owner decision. Must not be the same as the producer for governance-critical deliverables. |

---

## 3. Prerequisites

Before applying this SOP:

1. The idea must have a source (Owner, Inbox, integration, specialist-identified, automated signal).
2. The Maintainer must have received the idea in the current session.
3. The governance baseline must be known: GL-014 through GL-018 (pending), SOP-015 through SOP-018 (pending).

If the governance baseline is not current (a referenced GL or SOP is not available), stop and surface to Owner before proceeding.

---

## 4. Idea Intake

**Step 1.** When an idea is introduced — by any channel — record it with the following minimum fields before any routing decision:

| Field | Definition |
|---|---|
| Idea text | The exact words or signal as received. Not paraphrased. |
| Source | Owner / Inbox / Integration / Specialist / Automated |
| Domain | Personal / Kamer E-commerce / Geldstroom Regie / Core / Unknown |
| Date received | ISO date: YYYY-MM-DD |
| Session ID | Current session identifier |

**Step 2.** Do not begin any work on the idea before classification is complete.

---

## 5. Minimum Information Required for Classification

Classification requires at least:

- A description of what is wanted or what problem exists
- Sufficient domain context to determine whether an existing system component is involved

If any of the following are absent, the idea is classified as **Vague** and Section 6 applies:

- The domain cannot be determined
- The scope cannot be estimated (is this a one-line fix or a new system?)
- The impacted system component cannot be identified (which integration? which script? which workflow?)

---

## 6. Handling Vague Ideas

A vague idea is an idea that cannot be classified because minimum information is missing.

**Step 1.** State exactly which information is missing. Do not guess. Do not attempt to infer the classification from partial information.

**Step 2.** Ask the Owner exactly one clarifying question per missing field.

**Step 3.** Do not begin any research, drafting, or scoping work before the missing information is provided.

**Step 4.** Once minimum information is provided, re-enter at Section 4 (Intake) with the updated information.

**Prohibited action:** Assigning a provisional classification and beginning work while waiting for clarification. The idea is unclassified until classification is complete.

---

## 7. Scenario Classification

Every idea is assigned exactly one primary scenario class. If the idea spans multiple classes, assign the highest-impact class as primary and record secondary classes.

### S1 — Use Existing Capability

| Field | Value |
|---|---|
| Definition | The idea asks to use a capability that already exists and is already working, without any modification to the system component. |
| Example | "Show me today's open Todoist tasks using the existing overview script." |
| Primary route | Route A — Direct execution with Owner confirmation |
| Required Owner decision | Confirm direct execution |
| Review Gate applies | No — unless the action produces a governance-relevant deliverable |
| Implementation report applies | No |
| Lifecycle decision applies | No — unless the action produces an accepted governance-relevant deliverable |
| Escalation triggers | If the existing capability is found to require modification before use, re-classify as S2 or S5 |
| Prohibited automatic actions | Modifying any system component. Beginning execution before Owner confirmation. |

---

### S2 — Extend Existing Capability

| Field | Value |
|---|---|
| Definition | The idea asks for a minor addition or enhancement to an existing integration, script, workflow, or capability. The core component remains intact; a new field, output, or behavior is added. |
| Example | "Add a 'project name' column to the existing daily task overview output." |
| Primary route | Route C — Standard proposal → Review Gate → Execution → Implementation report |
| Required Owner decision | Approve proposal; approve execution |
| Review Gate applies | Yes — any modification to a system file triggers Review Gate |
| Implementation report applies | Yes |
| Lifecycle decision applies | Yes |
| Escalation triggers | If the extension requires modifying governance files (AGENT.md, SOPs, GLs): escalate to S8 and Route D. If the extension introduces new dependencies or external calls: escalate to High impact. |
| Prohibited automatic actions | Modifying any script or system file before proposal approval. Skipping Review Gate for system-file modifications. |

---

### S3 — New Idea on Existing Solution

| Field | Value |
|---|---|
| Definition | A new use case, configuration, channel, or data type that uses an existing system (tool, service, integration) without modifying the integration itself. New behavior is added to the existing infrastructure. |
| Example | "Add a weekly digest channel to the existing Discord integration for session log summaries." |
| Primary route | Route C — Standard proposal → Review Gate → Execution → Implementation report |
| Required Owner decision | Approve proposal; approve execution |
| Review Gate applies | Yes |
| Implementation report applies | Yes |
| Lifecycle decision applies | Yes |
| Escalation triggers | If the new use case requires changes to the integration code: re-classify as S2. If it requires new external accounts or credentials: escalate to S9. |
| Prohibited automatic actions | Creating channels, webhooks, configurations, or connections before proposal approval. |

---

### S4 — New Idea on New Solution

| Field | Value |
|---|---|
| Definition | A new capability that requires a new integration, tool, external service, or system that does not currently exist in the myPKA team. |
| Example | "Build a new integration with a project management tool to mirror all project.md files." |
| Primary route | Route E — Research-first (Pax research brief → Proposal → Review Gate → Execution → Implementation report) |
| Required Owner decision | Approve research scope; approve proposal; approve execution |
| Review Gate applies | Yes — at proposal and at execution report |
| Implementation report applies | Yes |
| Lifecycle decision applies | Yes |
| Escalation triggers | If research reveals security dependencies: add S9 secondary class. If the new solution affects multiple domains: add S10 secondary class. |
| Prohibited automatic actions | Beginning implementation before research brief is delivered and proposal is approved. Installing external tools or services without Owner approval. |

---

### S5 — Fix Existing Solution

| Field | Value |
|---|---|
| Definition | A known bug, regression, or broken behavior in an existing script, integration, workflow, or capability. The intended behavior is known; it is currently not functioning as designed. |
| Example | "The morning routine skill does not properly close the Brain Zen step when there are no calendar items." |
| Primary route | Route C — Standard proposal (diagnosis + fix description) → Review Gate → Execution → Implementation report |
| Required Owner decision | Approve fix proposal; confirm fix scope |
| Review Gate applies | Yes — any system file modification requires Review Gate |
| Implementation report applies | Yes |
| Lifecycle decision applies | Yes |
| Escalation triggers | If the fix reveals a deeper architectural problem: re-classify as S6. If the fix requires governance document changes: add S8. If root cause is security-related: add S9. |
| Prohibited automatic actions | Applying a fix directly without a proposal. Fixing scope beyond the stated defect without re-triage. |

---

### S6 — Replace Existing Solution

| Field | Value |
|---|---|
| Definition | An existing implementation is to be replaced in its entirety with a different approach. The existing component is retired; a new component takes its place. |
| Example | "Replace the current Python archiving script with a dedicated handler in the meta integration." |
| Primary route | Route C — Standard proposal (must include: reason for replacement, supersession plan for old component, migration plan) → Review Gate → Execution → Implementation report |
| Required Owner decision | Approve proposal (including supersession and migration plan); approve execution |
| Review Gate applies | Yes — always; replacement is high-impact |
| Implementation report applies | Yes — must confirm that old component is superseded and references are updated |
| Lifecycle decision applies | Yes — old component enters lifecycle as Superseded state per SOP-017 R2 |
| Escalation triggers | If the replacement requires data migration: escalate to High and add explicit rollback plan to proposal. If it affects another domain: add S10. |
| Prohibited automatic actions | Deleting or disabling the old component before the replacement is confirmed working. Skipping the supersession plan. |

---

### S7 — Structure Existing Solution

| Field | Value |
|---|---|
| Definition | Existing work exists but lacks documentation, naming convention compliance, folder structure, indexing, or governance alignment. No new capability is added; the existing work is organized and brought into compliance. |
| Example | "The Deliverables folder has inconsistent naming — some folders use Dutch, some English. Standardize." |
| Primary route | Route C — Standard proposal (scope of changes + before/after state) → Review Gate → Execution → Implementation report |
| Required Owner decision | Approve proposal; confirm scope of affected files |
| Review Gate applies | Yes — structural changes affect references and paths |
| Implementation report applies | Yes — must list all files moved or renamed |
| Lifecycle decision applies | Yes |
| Escalation triggers | If structural work requires modifying CLAUDE.md or governance documents: escalate to S8. If it affects more than one domain: add S10. |
| Prohibited automatic actions | Renaming or moving files before the complete scope is approved. Updating references in undisclosed files. |

---

### S8 — Governance-Relevant Idea

| Field | Value |
|---|---|
| Definition | The idea affects the team governance structure: GLs, SOPs, Workstreams, CLAUDE.md, AGENT.md files, naming conventions, approval gates, or team operating rules. |
| Example | "Add a mandatory 'context_window_tokens' field to all session_logs entries." |
| Primary route | Route D — SOP-015 Proposal Iteration Protocol → Review Gate → Execution → Implementation report |
| Required Owner decision | Approve proposal per SOP-015; approve execution; confirm exact text before any system file is modified |
| Review Gate applies | Yes — always; governance document changes are always governance-critical |
| Implementation report applies | Yes |
| Lifecycle decision applies | Yes |
| Escalation triggers | If the governance change has security implications: add S9. If it affects multiple domains or agents simultaneously: add S10. |
| Prohibited automatic actions | Modifying any GL, SOP, Workstream, AGENT.md, or CLAUDE.md before SOP-015 proposal is approved. Treating a verbal agreement as an approved proposal. |

---

### S9 — Security-Sensitive Idea

| Field | Value |
|---|---|
| Definition | The idea involves credentials, API keys, tokens, OAuth flows, access controls, external exposure, sensitive data storage, or any action where a failure could expose private information or compromise system integrity. |
| Example | "Cache the Google OAuth refresh token in the UMC PostgreSQL database for faster API access." |
| Primary route | Route F — Security proposal (must include: data classification, storage location, access scope, risk assessment, rollback plan) → Mode 1 Review Gate preferred → Execution → Implementation report with explicit security confirmation |
| Required Owner decision | Approve security proposal; approve execution with explicit security sign-off |
| Review Gate applies | Yes — always; Mode 1 (external review) preferred; Mode 3 (self-review) not sufficient for Critical security impact |
| Implementation report applies | Yes — must include confirmation that no credentials are exposed |
| Lifecycle decision applies | Yes |
| Escalation triggers | Any discovery during implementation of additional credential exposure: stop immediately, surface to Owner before continuing. |
| Prohibited automatic actions | Storing any credential, token, or key without explicit Owner approval of the exact storage location and access scope. Running any code that touches credentials before proposal approval. |

---

### S10 — Cross-Domain Idea

| Field | Value |
|---|---|
| Definition | The idea affects two or more domains simultaneously (Personal, Kamer E-commerce, Geldstroom Regie, Core) or requires coordination across two or more specialists. |
| Example | "Create a unified morning digest combining personal Todoist tasks, Kamer E-commerce open orders, and Geldstroom Regie payment reminders." |
| Primary route | Sienna Priority Gate (is this deliberate?) → Marcus ICOR classification → Multi-agent proposal → Mode 2 Review Gate preferred → Execution → Implementation report |
| Required Owner decision | Confirm deliberate (Sienna gate); confirm ICOR classification (Marcus); approve proposal; approve execution |
| Review Gate applies | Yes — always; Mode 2 (multi-agent review) preferred |
| Implementation report applies | Yes — must cover all affected domains |
| Lifecycle decision applies | Yes — domain routing per GL-015 for knowledge extraction |
| Escalation triggers | If any domain component is security-sensitive: add S9. If the idea requires new external services: add S4. |
| Prohibited automatic actions | Bypassing the Sienna Priority Gate. Beginning work across domains without ICOR classification. Writing to multiple domain databases in a single operation without explicit multi-domain approval. |

---

## 8. Impact Labels

Every classified idea also receives an impact label. Impact labels escalate the required governance instruments independently of the scenario class.

| Label | Criteria | Effect |
|---|---|---|
| **Low** | No system file changes; no database writes; fully reversible; single-step action; affects one session only | Route A permitted; no proposal required; Owner confirmation sufficient |
| **Medium** | Requires script modification, new configuration, or operational procedure change; no governance document changes; reversible with documented steps | Route B or C required; proposal required; Review Gate required if system files are touched |
| **High** | Requires new integration, new solution, governance document change, or replacement of an existing component; affects multiple sessions or multiple specialists | Route C, D, or E required; full proposal required; Review Gate required; implementation report required |
| **Critical** | Security-sensitive; irreversible without significant recovery effort; involves credentials, external exposure, or cross-domain database writes; affects production systems | Route F or Route C with security review required; Mode 1 Review Gate preferred; implementation report with explicit confirmation required |

If a scenario class and impact label conflict (e.g., S1 classified as Critical because an existing capability touches credentials), the higher-governance requirement prevails.

---

## 9. Route Definitions

| Route | Name | Steps |
|---|---|---|
| **Route A** | Direct execution | Owner confirmation → Execution (no proposal required) |
| **Route B** | Lightweight proposal | Short proposal (what / why / how / risks / Owner decision options) → Owner approval → Execution → No formal report required (action recorded in session log) |
| **Route C** | Standard proposal | Full proposal → Review Gate (SOP-016) → Owner approval → Execution → Implementation report → Lifecycle decision (SOP-017) |
| **Route D** | Governance proposal | SOP-015 iteration protocol → Review Gate → Owner approval → Execution → Implementation report → Lifecycle decision |
| **Route E** | Research-first | Pax research brief (scope approved by Owner) → Full proposal → Review Gate → Owner approval → Execution → Implementation report → Lifecycle decision |
| **Route F** | Security review | Security proposal (with data classification, risk assessment, rollback plan) → Mode 1 Review Gate preferred → Owner approval → Execution → Implementation report with security confirmation → Lifecycle decision |

---

## 10. Route Selection Matrix

Use this matrix to determine the default route. Apply the higher-governance requirement when scenario class and impact label produce different route requirements.

| Scenario | Low | Medium | High | Critical |
|---|---|---|---|---|
| S1 — Use existing | Route A | Route A | Route B | Route F |
| S2 — Extend existing | Route B | Route C | Route C | Route C + S9 if applicable |
| S3 — New on existing | Route B | Route C | Route C | Route C + S9 if applicable |
| S4 — New on new | Route C | Route C | Route E | Route E + S9 if applicable |
| S5 — Fix | Route B | Route C | Route C | Route C |
| S6 — Replace | Route C | Route C | Route C | Route C |
| S7 — Structure | Route B | Route C | Route C | Route C |
| S8 — Governance | Route D | Route D | Route D | Route D |
| S9 — Security | Route F | Route F | Route F | Route F |
| S10 — Cross-domain | Route C | Route C | Route C | Route C + Mode 2 RG |

---

## 11. Required Deliverable Types

| Route | Required deliverable types |
|---|---|
| Route A | No deliverable required. Action recorded in session log. |
| Route B | Short proposal document (minimum: what / why / how / risks / Owner decision options) |
| Route C | Full proposal document; execution report; closure report (if the implementation constitutes a closable project) |
| Route D | SOP-015 versioned proposal; Review Gate package; execution report; closure report |
| Route E | Pax research brief; full proposal; execution report; closure report |
| Route F | Security proposal; Review Gate package (Mode 1 preferred); execution report with security confirmation |

All Route C, D, E, and F deliverables that are accepted enter the SOP-017 lifecycle process.

---

## 12. Owner Decision Points

The Owner must make an explicit decision at the following points. No automatic advancement between points is permitted.

| Point | Trigger | Required decision |
|---|---|---|
| DP-1 | Classification complete — Medium or higher impact | Confirm or reject the route recommendation |
| DP-2 | Research brief delivered (Route E only) | Approve research scope before proposal begins |
| DP-3 | Proposal or amendment delivered | Accept / request amendments / defer / reject |
| DP-4 | Review Gate complete | Accept / request amendments / defer / reject (per SOP-016 Section 7) |
| DP-5 | Implementation ready | Confirm implementation may begin |
| DP-6 | Implementation report delivered | Accept as Done / request amendments / raise finding |
| DP-7 | Lifecycle decision required (SOP-017) | Approve each processing destination individually |

For Route A (direct execution), only DP-5 applies (Owner confirmation before execution).
For Route B (lightweight proposal), DP-3 and DP-5 apply.

---

## 13. Review Gate Triggers

A Review Gate per SOP-016 is required when any of the following conditions are true:

1. The deliverable is a proposal that authorizes implementation (any route except A)
2. The deliverable modifies any system file: AGENT.md, SOP, GL, Workstream, CLAUDE.md, or any canonical path file
3. The deliverable includes a migration, replacement, or supersession plan
4. The deliverable includes credential handling or security-relevant configuration
5. The deliverable is a multi-domain action (S10)
6. The impact label is High or Critical regardless of scenario class

Review Gate mode selection:
- Mode 1 (External review): preferred for S9 Critical, S8, and any deliverable that modifies governance documents
- Mode 2 (Internal multi-agent): preferred for S10 (cross-domain)
- Mode 3 (Single-system fallback): permitted only when no external reviewer or additional agent is available; hard stop conditions per SOP-016 Section 5 apply

---

## 14. Implementation Approval Requirements

Implementation may not begin until all of the following are true:

1. The proposal has been accepted by the Owner (DP-3 passed)
2. The Review Gate has passed (DP-4 passed)
3. The Owner has explicitly confirmed implementation may begin (DP-5 passed)
4. For S9 ideas: explicit Owner sign-off on the security risk assessment
5. For S10 ideas: explicit Owner approval of the multi-domain scope

An accepted proposal without an explicit implementation confirmation (DP-5) is not an authorization to begin implementation.

---

## 15. Implementation Report Requirements

Every Route C, D, E, or F implementation produces an implementation report. The implementation report must include:

| Field | Requirement |
|---|---|
| Deliverable path | Exact file path of the implementation report |
| Scope completed | List every action taken; one line per action |
| Scope not completed | List every approved action that was not taken and why |
| Files created | Exact paths of all files created |
| Files modified | Exact paths of all files modified, with before/after state summary |
| Files moved or deleted | Exact source and destination paths |
| Database records written | Database name, table name, record ID (if applicable) |
| Tests or verifications performed | List each verification and its result |
| Known issues or deviations | Any deviation from the approved proposal; reason and impact stated |
| Required follow-up | List any open items that require a separate action or triage |
| Post-check results | Results of all post-checks specified in the proposal |

The implementation report must not include any system file content, credentials, or sensitive data beyond what is needed to confirm scope completion.

---

## 16. Lifecycle Decision Requirements

Every accepted implementation-enabling deliverable (Route C, D, E, F) enters the SOP-017 lifecycle process after Owner acceptance.

The Maintainer is responsible for ensuring the lifecycle process is initiated. The Maintainer does not execute lifecycle processing unilaterally — it surfaces candidates to the Owner per SOP-017 Phase 4.

Lifecycle decisions must be completed before the session in which the deliverable was accepted is closed, unless the Owner explicitly defers the lifecycle decision to a named future session.

---

## 17. Explicit Exclusions

The following actions are prohibited under this SOP regardless of route, scenario class, impact label, or session context:

**EX-1:** No implementation step may begin before the Owner has made DP-5 (implementation confirmation).

**EX-2:** No system file (GL, SOP, Workstream, AGENT.md, CLAUDE.md) may be modified as part of any route except S8/Route D, and only after SOP-015 approval.

**EX-3:** No credential, token, API key, or OAuth material may be stored, logged, or written to any system as part of any route except S9/Route F, and only after explicit Owner security sign-off.

**EX-4:** No multi-domain database write (writing to more than one domain database in a single action) may occur without explicit multi-domain Owner approval.

**EX-5:** No idea may be classified and routed without presenting the classification to the Owner for Medium, High, or Critical impact ideas. Low-impact ideas may proceed to Route A with Owner confirmation only.

**EX-6:** No scope expansion may occur mid-route without re-triage and Owner approval of the expanded scope.

**EX-7:** No idea may remain unclassified for more than one session without being surfaced to the Owner as an open item.

**EX-8:** No vague idea may be "resolved" by guessing the classification. Vague ideas require clarification per Section 6.

---

## 18. Hard Rules

The following rules are hard constraints that apply regardless of context, session, agent, or tool:

**HR-1:** Triage may be automatic; implementation may not.

**HR-2:** An approved route is not an approved proposal. An approved proposal is not an approved implementation. Each decision point requires its own explicit Owner approval.

**HR-3:** Any review of a governance-relevant deliverable produced by this SOP must include a Review Context Packet per the SOP-016 amendment in this governance pack.

**HR-4:** A classified idea that has been parked, deferred, or rejected may not be re-opened without Owner confirmation.

**HR-5:** The scenario class and impact label are assigned by the Maintainer. The Owner may override either assignment at any decision point.

---

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-06-05 | v01 | Initial proposal — prepared for Owner review |

---

## Proposed SOP Index Entry

> **Note:** This is a proposal. The entry below must not be added to `SOP-index.md` until the Owner has approved this proposal and the SOP-018 file has been created and confirmed.

Proposed addition to `Team Knowledge/Core/SOPs/SOP-index.md`:

```
| SOP-018 | [[SOP-018_Idea-to-Implementation Routing Procedure]] | Procedure: idea intake, scenario classification (S1–S10), impact labels, route selection (A–F), Owner decision points, Review Gate triggers, implementation approval, implementation report requirements, and lifecycle decision trigger |
```

---

## Acceptance Criteria

This proposal is acceptable when all of the following are true:

1. The 10 scenario classes (S1–S10) cover every common idea type without significant overlap or uncovered cases.
2. The 4 impact labels (Low, Medium, High, Critical) are mutually exclusive and exhaustive for practical purposes.
3. The 6 routes (A–F) are mutually exclusive and correctly mapped to scenario × impact combinations in the Route Selection Matrix.
4. The 7 Owner Decision Points (DP-1 through DP-7) correctly separate Owner decisions from Maintainer actions and do not allow any automatic advancement.
5. Review Gate triggers are consistent with GL-016 scope criteria and do not conflict with SOP-016.
6. Implementation report requirements are sufficient to enable independent verification after execution.
7. All 8 explicit exclusions (EX-1 through EX-8) and 5 hard rules (HR-1 through HR-5) are internally consistent and do not conflict with GL-014, GL-015, GL-016, GL-017, SOP-015, SOP-016, or SOP-017.
8. The proposed SOP number SOP-018 is confirmed as the next available number in the SOP index (verified: SOP-017 is currently the highest).
9. The proposed filename follows GL-001 naming conventions.
10. No execution has occurred as a result of this proposal document.

---

## Owner Decision Options

| Option | Action |
|---|---|
| Approve this proposal | SOP-018 file may be created; SOP-index.md may be updated |
| Request amendments | Specific changes required; revised v02 proposal prepared; SOP-018 not created until new version is approved |
| Approve with modifications | Owner states exact modifications; v02 created before SOP-018 is written |
| Defer | Proposal noted; no action until Owner names a condition for revisit |
| Reject | Proposal not accepted; reason stated; SOP-018 not created |

---

Delivered on: 2026-06-05
Delivered at: Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/
