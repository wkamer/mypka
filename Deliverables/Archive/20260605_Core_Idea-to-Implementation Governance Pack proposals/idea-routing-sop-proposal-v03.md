# PROPOSAL — SOP-018: Idea-to-Implementation Routing Procedure

**Proposal status:** Draft v03
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

## Revision Summary (v01 to v02)

The following changes were made in response to the Owner's v01 amendment request:

1. **Section 2 expanded** — Role Definitions now includes role-based agent table (research, personal priority gate, project classification, domain specialist roles) and Review Gate Mode brief definitions. Named agents appear as current assignments, not permanent dependencies.
2. **Section 3a added** — Companion Sources: all documents a reviewer must have to independently review any SOP-018-governed deliverable.
3. **Section 4 amended** — Intake: explicit prohibition on persistent writes; transient capture only.
4. **Section 9 amended** — Route B escalation rule added with six explicit conditions. Route B auto-escalates to Route C or higher if any condition is true.
5. **Section 12 completely rewritten** — Owner Decision Points restructured. DP-3 and DP-4 renamed and resequenced: the Review Gate must execute before the Owner decides on the proposal. Sequence is now DP-1 through DP-6.
6. **Section 13 amended** — Review Gate Triggers: Route B reference updated.
7. **Section 14 added (new)** — Persistent Write Rules: standalone section; no persistent write is authorized by idea routing itself.
8. **Section 15 renumbered** — Implementation Approval Requirements: updated DP references.
9. **Explicit Exclusions** — EX-9 added (persistent writes not authorized by idea routing).
10. **Hard Rules** — HR-6 added (numbering re-confirmation required immediately before implementation).
11. **S4 updated** — "Pax research" replaced with "Research role (currently: Pax)."
12. **S10 updated** — All named agent references replaced with role-based; personal priority gate and project classification made traceable to existing operating rules, not new SOP-018 gates.
13. **Section 21 added** — Pack-level Implementation Order and post-check sequence.
14. **Numbering re-confirmation note added.**

---

## Revision Summary (v02 to v03)

The following changes were made in response to the Owner's v02 amendment request:

1. **Section 2.4 added** — File Category Definitions. Distinguishes governance files (GLs, SOPs, Workstreams, AGENT.md, CLAUDE.md, governance indexes, and other governance instruments) from operational system files (scripts, handlers, integration files, skill files, configuration files, and operational code files). Each category has a defined governance requirement. This distinction is used consistently throughout the SOP.
2. **Route B escalation condition 1 split into 1a and 1b** — Condition 1a: governance file created, modified, or deleted — escalates to Route D. Condition 1b: operational system file created, modified, or deleted — escalates to Route C. The original condition 2 through 6 are renumbered accordingly to 2 through 6 (unchanged). Escalation table updated.
3. **EX-2 updated** — Now explicitly distinguishes governance files from operational system files. Governance files remain protected by S8/Route D and SOP-015. Operational system files may be modified via Route C or higher after Review Gate, DP-3, and DP-4.
4. **Section 13 (Review Gate Triggers) condition 2 updated** — Now uses "governance file or operational system file" with reference to Section 2.4 definitions.
5. **S2 and S5 scenario language updated** — "system file" replaced with "operational system file" where the governance file distinction is relevant.
6. **S8 scenario language updated** — "system files" replaced with "governance files" where the governance protection rule applies.
7. **Section 13 final line updated** — Condition range updated to reflect 1a, 1b, 2–6.
8. **HR-7 updated** — "six Route B escalation conditions" replaced with "all Route B escalation conditions" to avoid a hard count that requires updating if conditions change.
9. **Revision Summary item 13 corrected** — v02 erroneously said "Section 22 added." Corrected to "Section 21 added."
10. **Acceptance Criteria item 12 corrected** — v02 erroneously said "All 7 explicit exclusions (EX-1 through EX-9)." Corrected to "All 9 explicit exclusions (EX-1 through EX-9)."

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

### 2.1 Governance Roles

| Role | Definition |
|---|---|
| Owner | Walter Kamer. Provides all approval decisions. Sole decision authority for route confirmation, proposal acceptance, implementation authorization, and lifecycle decisions. Not delegable. |
| Maintainer | The orchestration layer responsible for receiving every idea, performing or routing triage, assigning classification, delegating to the appropriate specialist, and tracking pipeline state. Current assignment: Larry. |
| Specialist | The team member assigned to produce the deliverable for the confirmed route. Identified during classification. |
| Reviewer | The agent, system, or person that evaluates the deliverable against the review checks per SOP-016. Must not be the same as the producer for governance-critical deliverables (per SOP-016 role separation rules). |

### 2.2 Named Role Assignments

These roles may be filled by different agents as the team evolves. The role name is the governance dependency. The current assignment is informational only.

| Role | Definition | Current assignment |
|---|---|---|
| Research role | Delivers domain research briefs before proposal preparation begins (Route E, S4). Reads primary sources directly; does not summarize from metadata or wrapper pages. | Currently: Pax |
| Personal priority gate role | Evaluates whether a new initiative in the personal or cross-domain space is deliberate and aligned with the Owner's current priorities before resources are committed. This gate exists in the team's operating instructions and is triggered for any new initiative not already in the current planning. SOP-018 references it; it is not created by SOP-018. | Currently: Sienna |
| Project classification role | Assigns ICOR classification and project structure to new initiatives confirmed as deliberate by the personal priority gate. SOP-018 references this role; it is not created by SOP-018. | Currently: Marcus |
| Domain specialist — Kamer E-commerce | The specialist responsible for Kamer E-commerce domain execution and deliverables. | Currently: Nova, Vera |
| Domain specialist — Geldstroom Regie | The specialist responsible for Geldstroom Regie domain execution and deliverables. | Currently: Finn |
| Domain specialist — Personal | The specialist responsible for Personal domain execution and deliverables. | Currently: Sienna |

### 2.3 Review Gate Mode Definitions

These modes are defined in SOP-016. Brief definitions are provided here for routing decisions. For full procedure, consult SOP-016 (required companion source).

| Mode | Condition | Definition |
|---|---|---|
| Mode 1 — External review | Preferred for S8, S9, governance-critical deliverables | A reviewer external to the producing agent applies the 13 review checks. The Maintainer assembles the review package (including RCP), distributes to the reviewer, collects findings, and packages the Owner decision packet. |
| Mode 2 — Internal multi-agent review | Preferred for S10 (cross-domain) | Multiple internal agents with distinct roles review the deliverable. Role separation rules per SOP-016 apply. Maintainer orchestrates. Preferred when the deliverable spans multiple domains or specialisms. |
| Mode 3 — Single-system fallback | Only when no external reviewer or additional agent is available | The producing system applies an explicit self-review checklist, surfaces all uncertainties, and packages a decision for the Owner. Hard stop conditions per SOP-016 Section 5 apply. Mode 3 is not sufficient for Critical-impact deliverables. |

### 2.4 File Category Definitions

This SOP distinguishes between two categories of system files. The category determines which route is required when the file is created, modified, or deleted.

| Category | Includes | Governance requirement |
|---|---|---|
| Governance file | GLs, SOPs, Workstreams, AGENT.md, CLAUDE.md, governance indexes (gl-index.md, SOP-index.md, agent-index.md), and any other document that defines team operating rules, approval gates, or governance instruments | S8 / Route D required. SOP-015 Proposal Iteration Protocol applies. |
| Operational system file | Scripts, handlers, integration files, skill files, configuration files, and operational code files that are not governance files | Route C or higher required. Subject to Review Gate, DP-3, and DP-4. |

When a change would affect both a governance file and an operational system file, the governance file requirement prevails: classify as S8 and use Route D.

---

## 3. Prerequisites

Before applying this SOP:

1. The idea must have a source (Owner, Inbox, integration, specialist-identified, automated signal).
2. The Maintainer must have received the idea in the current session.
3. The governance baseline must be known: GL-014 through GL-018 (pending), SOP-015 through SOP-018 (pending), plus companion sources listed in Section 3a.

If the governance baseline is not current (a referenced companion source is not available), stop and surface to Owner before proceeding.

---

## 3a. Companion Sources

The following documents must be provided to any reviewer applying this SOP. A reviewer without access to these documents cannot independently verify compliance. All companion sources must be listed in the Review Context Packet (Field 7 and Field 15) for any review of an SOP-018-governed deliverable.

| Document | Required for |
|---|---|
| GL-018 — Idea Routing and Implementation Governance Principles | All reviews — the principle document this SOP implements |
| GL-016 — Review Gate Principles | All reviews — defines when a Review Gate is required |
| SOP-016 — Review Gate Procedure | All reviews — defines the 13 checks and Owner decision options |
| GL-017 — Deliverable Lifecycle Principles | All lifecycle-capable reviews |
| SOP-017 — Deliverable Lifecycle Procedure | All lifecycle-capable reviews |
| SOP-015 — Proposal Iteration Protocol | Route D and any S8 review |
| GL-014 — AI Team Governance | All reviews — defines approval gates and escalation |
| Active file naming conventions (currently: GL-001) | All reviews where a filename is proposed |
| Active canonical paths reference (currently: GL-004) | Reviews involving S7 (structural) ideas or path changes |

When any companion source is in a pending-proposal state, provide the pending proposal file and state its pending status explicitly.

---

## 4. Idea Intake

**Step 1.** When an idea is introduced — by any channel — record the following fields in transient session context before any routing decision:

| Field | Definition |
|---|---|
| Idea text | The exact words or signal as received. Not paraphrased. |
| Source | Owner / Inbox / Integration / Specialist / Automated |
| Domain | Personal / Kamer E-commerce / Geldstroom Regie / Core / Unknown |
| Date received | ISO date: YYYY-MM-DD |
| Session identifier | Current session reference |

**Step 2.** Do not begin any work on the idea before classification is complete.

**Step 3 — Persistent write prohibition.** The Intake step does not authorize any persistent write. Recording the idea in session context is transient capture. Writing to team_tasks, session_logs, agent_learnings, UMC, personal.db, kamer e-commerce.db, geldstroom-regie.db, or any other database requires either: (a) a pre-approved routine that covers this session, or (b) explicit Owner approval of the specific write. See also Section 14.

---

## 5. Minimum Information Required for Classification

Classification requires at least:

- A description of what is wanted or what problem exists
- Sufficient domain context to determine whether an existing system component is involved

If any of the following are absent, the idea is classified as **Vague** and Section 6 applies:

- The domain cannot be determined
- The scope cannot be estimated (one-line fix vs. new system?)
- The impacted system component cannot be identified (which integration? which script? which workflow?)

---

## 6. Handling Vague Ideas

A vague idea is one that cannot be classified because minimum information is missing.

**Step 1.** State exactly which information is missing. Do not guess. Do not infer the classification from partial information.

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
| Escalation triggers | If the existing capability is found to require modification before use: re-classify as S2 or S5 |
| Prohibited automatic actions | Modifying any system component. Beginning execution before Owner confirmation. |

---

### S2 — Extend Existing Capability

| Field | Value |
|---|---|
| Definition | The idea asks for a minor addition or enhancement to an existing integration, script, workflow, or capability. The core component remains intact; a new field, output, or behavior is added. |
| Example | "Add a 'project name' column to the existing daily Todoist task overview script." |
| Primary route | Route C — Standard proposal → Review Gate → Owner decision → Execution → Implementation report |
| Required Owner decision | DP-3 (post-Review Gate); DP-4 (implementation confirmation) |
| Review Gate applies | Yes — any modification to an operational system file triggers Review Gate (see Section 2.4 for file category definitions) |
| Implementation report applies | Yes |
| Lifecycle decision applies | Yes |
| Escalation triggers | If extension requires modifying governance files (AGENT.md, SOPs, GLs): escalate to S8 and Route D. If extension introduces new external dependencies or credentials: escalate to S9 or add S9 secondary. |
| Prohibited automatic actions | Modifying any script or operational system file before proposal is reviewed and Owner decision at DP-3 is made. Skipping Review Gate for operational system file modifications. |

---

### S3 — New Idea on Existing Solution

| Field | Value |
|---|---|
| Definition | A new use case, configuration, channel, or data type that uses an existing system (tool, service, integration) without modifying the integration itself. New behavior is added to the existing infrastructure. |
| Example | "Add a weekly digest delivery to the existing session logging system using the existing email integration." |
| Primary route | Route C — Standard proposal → Review Gate → Owner decision → Execution → Implementation report |
| Required Owner decision | DP-3 (post-Review Gate); DP-4 (implementation confirmation) |
| Review Gate applies | Yes |
| Implementation report applies | Yes |
| Lifecycle decision applies | Yes |
| Escalation triggers | If the new use case requires changes to the integration code: re-classify as S2. If it requires new external accounts or credentials: add S9 secondary. |
| Prohibited automatic actions | Creating channels, webhooks, configurations, or connections before DP-3 Owner decision. |

---

### S4 — New Idea on New Solution

| Field | Value |
|---|---|
| Definition | A new capability that requires a new integration, tool, external service, or system that does not currently exist in the myPKA team. |
| Example | "Build a new integration with an external project tracking tool to mirror project.md files." |
| Primary route | Route E — Research role delivers research brief (scope approved by Owner at DP-2) → Full proposal → Review Gate → Owner decision → Execution → Implementation report |
| Required Owner decision | DP-1 (route confirmation); DP-2 (research scope approval before research begins); DP-3 (post-Review Gate); DP-4 (implementation confirmation) |
| Review Gate applies | Yes — at proposal and at execution report |
| Implementation report applies | Yes |
| Lifecycle decision applies | Yes |
| Escalation triggers | If research reveals security dependencies: add S9 secondary. If the new solution affects multiple domains: add S10 secondary. |
| Prohibited automatic actions | Beginning research before DP-2 research scope is approved. Beginning implementation before research brief is delivered and DP-3 Owner decision is made. Installing external tools or services without Owner approval. |

---

### S5 — Fix Existing Solution

| Field | Value |
|---|---|
| Definition | A known bug, regression, or broken behavior in an existing script, integration, workflow, or capability. The intended behavior is known; it is currently not functioning as designed. |
| Example | "The morning routine skill does not properly close the Brain Zen step when there are no calendar items." |
| Primary route | Route C — Diagnosis proposal (root cause + fix description) → Review Gate → Owner decision → Execution → Implementation report |
| Required Owner decision | DP-1 (route + fix scope confirmation); DP-3 (post-Review Gate); DP-4 (implementation confirmation) |
| Review Gate applies | Yes — any operational system file modification requires Review Gate (see Section 2.4) |
| Implementation report applies | Yes |
| Lifecycle decision applies | Yes |
| Escalation triggers | If the fix reveals a deeper architectural problem: re-classify as S6. If the fix requires governance file changes: add S8. If root cause is security-related: add S9. |
| Prohibited automatic actions | Applying a fix directly without a proposal. Fixing scope beyond the stated defect without re-triage. |

---

### S6 — Replace Existing Solution

| Field | Value |
|---|---|
| Definition | An existing implementation is to be replaced in its entirety with a different approach. The existing component is retired; a new component takes its place. |
| Example | "Replace the current standalone archiving script with a dedicated handler in the integration framework." |
| Primary route | Route C — Standard proposal (must include: reason for replacement, supersession plan, migration plan, rollback plan) → Review Gate → Owner decision → Execution → Implementation report |
| Required Owner decision | DP-1 (route + supersession and migration plan confirmation); DP-3 (post-Review Gate); DP-4 (implementation confirmation) |
| Review Gate applies | Yes — always; replacement is High-impact by definition |
| Implementation report applies | Yes — must confirm old component is superseded and references updated |
| Lifecycle decision applies | Yes — old component enters Superseded state per SOP-017 R2 |
| Escalation triggers | If replacement requires data migration: escalate to High and add rollback plan to proposal. If it affects another domain: add S10. |
| Prohibited automatic actions | Deleting or disabling the old component before the replacement is confirmed working. Skipping the supersession plan. |

---

### S7 — Structure Existing Solution

| Field | Value |
|---|---|
| Definition | Existing work exists but lacks documentation, naming convention compliance, folder structure, indexing, or governance alignment. No new capability is added; the existing work is organized and brought into compliance. |
| Example | "The Deliverables folder has inconsistent naming. Standardize all folder names to the active naming convention." |
| Primary route | Route C — Standard proposal (complete scope of changes + before/after state) → Review Gate → Owner decision → Execution → Implementation report |
| Required Owner decision | DP-1 (route + affected file scope confirmation); DP-3 (post-Review Gate); DP-4 (implementation confirmation) |
| Review Gate applies | Yes — structural changes affect references and the active canonical paths reference |
| Implementation report applies | Yes — must list all files moved or renamed |
| Lifecycle decision applies | Yes |
| Escalation triggers | If structural work requires modifying CLAUDE.md or governance files: escalate to S8. If it affects more than one domain: add S10. |
| Prohibited automatic actions | Renaming or moving files before the complete approved scope is confirmed. Updating references in undisclosed files. Applying path changes without following the active canonical paths reference update protocol. |

---

### S8 — Governance-Relevant Idea

| Field | Value |
|---|---|
| Definition | The idea affects the team governance structure: GLs, SOPs, Workstreams, CLAUDE.md, AGENT.md files, naming conventions, approval gates, or team operating rules. |
| Example | "Add a mandatory 'context_window_tokens' field to all new session_logs entries." |
| Primary route | Route D — SOP-015 Proposal Iteration Protocol → Review Gate → Owner decision → Execution → Implementation report |
| Required Owner decision | DP-1 (S8 classification and Route D confirmation); DP-3 (post-Review Gate, exact text confirmed); DP-4 (implementation confirmation) |
| Review Gate applies | Yes — always; governance file changes are governance-critical; Mode 1 preferred |
| Implementation report applies | Yes |
| Lifecycle decision applies | Yes |
| Escalation triggers | If the governance change has security implications: add S9. If it affects multiple domains or agents simultaneously: add S10. |
| Prohibited automatic actions | Modifying any governance file (GL, SOP, Workstream, AGENT.md, CLAUDE.md — see Section 2.4) before SOP-015 proposal is accepted at DP-3. Treating a verbal agreement as an approved proposal. Applying exact-text check without the exact proposed text being in the accepted proposal. |

---

### S9 — Security-Sensitive Idea

| Field | Value |
|---|---|
| Definition | The idea involves credentials, API keys, tokens, OAuth flows, access controls, external exposure, sensitive data storage, or any action where a failure could expose private information or compromise system integrity. |
| Example | "Cache the Google OAuth refresh token in the UMC database to avoid re-authenticating every session." |
| Primary route | Route F — Security proposal (must include: data classification, storage location, access scope, risk assessment, rollback plan) → Mode 1 Review Gate preferred → Owner decision → Execution → Implementation report with explicit security confirmation |
| Required Owner decision | DP-1 (S9-Critical classification confirmation); DP-3 (post-Review Gate with security sign-off); DP-4 (explicit implementation confirmation with security sign-off) |
| Review Gate applies | Yes — always; Mode 1 (external review) preferred; Mode 3 is not sufficient for Critical security impact |
| Implementation report applies | Yes — must confirm no credentials exposed and rollback plan is available |
| Lifecycle decision applies | Yes |
| Escalation triggers | Any discovery of additional credential exposure during implementation: stop immediately, surface to Owner. |
| Prohibited automatic actions | Storing any credential, token, or key without explicit Owner approval of the exact storage location and access scope. Running any code that touches credentials before DP-3 Owner decision. Using Mode 3 for Critical security impact without explicit Owner override. |

---

### S10 — Cross-Domain Idea

| Field | Value |
|---|---|
| Definition | The idea affects two or more domains simultaneously (Personal, Kamer E-commerce, Geldstroom Regie, Core) or requires coordination across two or more domain specialists. |
| Example | "Create a unified morning digest combining personal Todoist tasks, Kamer E-commerce open orders, and Geldstroom Regie payment reminders." |
| Primary route | Personal priority gate check (personal priority gate role) → Project classification (project classification role) → Multi-domain proposal (all affected domain specialists) → Mode 2 Review Gate preferred → Owner decision → Execution → Implementation report |
| Required Owner decision | DP-1 (cross-domain scope confirmation); confirmation at each gate per existing operating rules; DP-3 (post-Review Gate); DP-4 (implementation confirmation) |
| Review Gate applies | Yes — always; Mode 2 (multi-agent review) preferred |
| Implementation report applies | Yes — must cover all affected domains |
| Lifecycle decision applies | Yes — domain routing per GL-015 for knowledge extraction |
| Escalation triggers | If any domain component is security-sensitive: add S9. If the idea requires new external services: add S4. |
| Prohibited automatic actions | Bypassing the personal priority gate check when the idea constitutes a new initiative. Beginning work across domains without project classification. Writing to multiple domain databases in a single operation without explicit multi-domain Owner approval. |

> **Note on S10 gates.** The personal priority gate and the project classification gate referenced in S10's primary route are defined in the team's operating instructions (CLAUDE.md). These are existing behavioral rules triggered by any new initiative, not new gates created by SOP-018. If those rules are not active in the current system, S10 proceeds directly to multi-domain proposal preparation after Owner confirms the cross-domain scope at DP-1.

---

## 8. Impact Labels

Every classified idea receives an impact label. Impact labels escalate the required governance instruments independently of the scenario class.

| Label | Criteria | Effect |
|---|---|---|
| **Low** | No system file changes; no database writes; fully reversible; single-step action; affects one session only | Route A permitted; no proposal required; Owner confirmation sufficient |
| **Medium** | Requires script modification, new configuration, or operational procedure change; no governance file changes; reversible with documented steps | Route B or C required; proposal required; Review Gate required if any Review Gate trigger in Section 13 applies |
| **High** | Requires new integration, new solution, governance file change, or replacement of an existing component; affects multiple sessions or multiple specialists | Route C, D, or E required; full proposal required; Review Gate required; implementation report required |
| **Critical** | Security-sensitive; irreversible without significant recovery effort; involves credentials, external exposure, or cross-domain database writes; affects production systems | Route F required; Mode 1 Review Gate preferred; implementation report with explicit security confirmation required |

If a scenario class and impact label conflict (e.g., S1 classified as Critical because an existing capability touches credentials), the higher-governance requirement prevails. The Maintainer must document the escalation reason.

---

## 9. Route Definitions

| Route | Name | Steps | Review Gate required |
|---|---|---|---|
| **Route A** | Direct execution | Owner confirmation → Execution | No |
| **Route B** | Lightweight proposal | Short proposal → Owner direct review → Owner decision → Execution | No — unless escalation condition applies (see Route B note) |
| **Route C** | Standard proposal | Full proposal → Review Gate → Owner decision (DP-3) → Implementation confirmation (DP-4) → Execution → Implementation report → Lifecycle decision | Yes |
| **Route D** | Governance proposal | SOP-015 versioned proposal → Review Gate → Owner decision (DP-3) → Implementation confirmation (DP-4) → Execution → Implementation report → Lifecycle decision | Yes |
| **Route E** | Research-first | Research role delivers research brief (Owner approves scope at DP-2) → Full proposal → Review Gate → Owner decision (DP-3) → Implementation confirmation (DP-4) → Execution → Implementation report → Lifecycle decision | Yes |
| **Route F** | Security review | Security proposal (data classification, risk, rollback plan) → Mode 1 Review Gate preferred → Owner decision (DP-3) → Implementation confirmation (DP-4) → Execution → Implementation report with security confirmation → Lifecycle decision | Yes |

---

### Route B — Review Gate Escalation Rule

Route B may proceed without a full Review Gate per SOP-016 ONLY when all of the following conditions are confirmed false:

1a. No governance file is created, modified, or deleted (governance files: any GL, SOP, Workstream, AGENT.md, CLAUDE.md, governance index, or other governance instrument — see Section 2.4)
1b. No operational system file is created, modified, or deleted (operational system files: scripts, handlers, integration files, skill files, configuration files, and operational code files — see Section 2.4)
2. No persistent database write is executed (team_tasks, session_logs, agent_learnings, UMC, personal.db, kamer e-commerce.db, geldstroom-regie.db, or any database)
3. No governance impact (no change to team operating rules, approval gates, or governance instruments)
4. No security impact (no credential handling, no token storage, no access control change, no external exposure)
5. No cross-domain impact (action affects exactly one domain)
6. No external integration change (no webhook, API endpoint, or external service configuration)

If any condition above is true, Route B automatically escalates:

| Condition true | Escalation |
|---|---|
| Condition 1a (governance file) or condition 3 (governance impact) | Escalate to Route D |
| Condition 1b (operational system file), 2, 5, or 6 | Escalate to Route C |
| Condition 4 (security impact) | Escalate to Route F |

The Maintainer must record the escalation reason in the session context. An escalated Route B is treated as the target route (C, D, or F) for all subsequent steps.

---

## 10. Route Selection Matrix

Use this matrix to determine the default route. When scenario class and impact label produce different route requirements, the higher-governance requirement prevails.

| Scenario | Low | Medium | High | Critical |
|---|---|---|---|---|
| S1 — Use existing | Route A | Route A | Route B* | Route F |
| S2 — Extend existing | Route B* | Route C | Route C | Route C + S9 if applicable |
| S3 — New on existing | Route B* | Route C | Route C | Route C + S9 if applicable |
| S4 — New on new | Route C | Route C | Route E | Route E + S9 if applicable |
| S5 — Fix | Route B* | Route C | Route C | Route C |
| S6 — Replace | Route C | Route C | Route C | Route C |
| S7 — Structure | Route B* | Route C | Route C | Route C |
| S8 — Governance | Route D | Route D | Route D | Route D |
| S9 — Security | Route F | Route F | Route F | Route F |
| S10 — Cross-domain | Route C | Route C | Route C | Route C + Mode 2 RG |

*Route B is subject to the escalation rule in Section 9. If any Route B escalation condition is true, the route escalates as defined.

---

## 11. Required Deliverable Types

| Route | Required deliverable types |
|---|---|
| Route A | No deliverable required. Confirmation recorded in session context only (transient). |
| Route B | Short proposal document (minimum content: what / why / how / risks / Owner decision options). No formal report required if no escalation. Action recorded in session context (transient). |
| Route C | Full proposal document; execution report; closure report (if the implementation constitutes a closable project) |
| Route D | SOP-015 versioned proposal; Review Gate package; execution report; closure report |
| Route E | Research brief; full proposal; execution report; closure report |
| Route F | Security proposal; Review Gate package (Mode 1 preferred); execution report with security confirmation |

All Route C, D, E, and F deliverables that are accepted by the Owner enter the SOP-017 lifecycle process.

---

## 12. Owner Decision Points

The Owner must make an explicit decision at the following points. No automatic advancement between points is permitted.

| DP | Trigger | Required decision | Applies to |
|---|---|---|---|
| DP-1 | Classification complete — Medium or higher impact | Confirm or redirect the route recommendation | All except Route A |
| DP-2 | Research scope ready | Approve research scope before research begins | Route E only |
| DP-3 | Proposal ready for Owner decision. For routes requiring Review Gate: Review Gate has been executed per SOP-016, findings returned to Maintainer, and Owner decision packet assembled. For Route B without escalation triggers: Owner reviews lightweight proposal directly; no Review Gate package. | Accept / request amendments / defer / reject the proposal | All except Route A |
| DP-4 | Proposal accepted at DP-3 | Separate explicit implementation confirmation before execution begins | All |
| DP-5 | Implementation complete | Accept implementation report as Done / request amendments / raise finding | Route C, D, E, F |
| DP-6 | Implementation report accepted at DP-5 | Approve each lifecycle processing destination individually (per SOP-017) | Route C, D, E, F |

**Route A:** Only DP-4 (Owner confirmation before execution).

**Route B without escalation:** DP-1 (route confirmation), DP-3 (Owner reviews lightweight proposal directly), DP-4 (implementation confirmation).

**Route B with escalation:** Follow the DPs of the escalated route.

**Routes C, D, E:** DP-1, DP-3 (post-Review Gate), DP-4, DP-5, DP-6.

**Route E additionally:** DP-2 (research scope approval) before research begins; research brief delivered after DP-2; full proposal prepared after research brief; DP-3 after Review Gate.

**Route F:** DP-1, DP-3 (post-Review Gate with security sign-off), DP-4 (implementation confirmation with explicit security sign-off), DP-5, DP-6.

> **Critical sequencing note.** The Owner must not make the DP-3 decision before the Review Gate is complete (for routes requiring one). The Review Gate produces findings; the Owner decides based on those findings. A proposal presented to the Owner before the Review Gate is a draft for triage purposes only, not a decision-ready document. The Maintainer must not present DP-3 options before Review Gate findings are in hand.

---

## 13. Review Gate Triggers

A Review Gate per SOP-016 is required when any of the following conditions are true:

1. The deliverable is a proposal authorizing implementation (any route except Route A; Route B only if escalated)
2. The deliverable modifies any governance file (GL, SOP, Workstream, AGENT.md, CLAUDE.md, or any file in the active canonical paths reference) or any operational system file (script, handler, integration file, skill file, configuration file, or operational code file) — see Section 2.4 for definitions
3. The deliverable includes a migration, replacement, or supersession plan
4. The deliverable includes credential handling or security-relevant configuration
5. The deliverable is a multi-domain action (S10)
6. The impact label is High or Critical regardless of scenario class

Review Gate mode selection:
- Mode 1 (External review): preferred for S9 Critical, S8, and any deliverable that modifies governance files
- Mode 2 (Internal multi-agent): preferred for S10 (cross-domain)
- Mode 3 (Single-system fallback): permitted only when no external reviewer or additional agent is available; hard stop conditions per SOP-016 Section 5 apply; not sufficient for Critical-impact deliverables

Route B without any of conditions 1a, 1b, 2–6: Review Gate is not required. The Maintainer must confirm in writing that all Route B escalation conditions (Section 9) are false before treating it as Route B without Review Gate.

---

## 14. Persistent Write Rules

Idea routing does not authorize any persistent write. This rule applies at every stage: intake, classification, route selection, proposal preparation, and Review Gate.

**What is permitted:**
Transient capture of idea metadata in session context (idea text, source, domain, date, session identifier) is permitted without additional authorization.

**What requires authorization:**
Any persistent write to any of the following requires either a pre-approved routine covering the current session, or explicit Owner approval of the specific write in the current session:

- team_tasks (any domain database)
- session_logs (team-knowledge.db)
- agent_learnings (any domain database)
- UMC / memory-db (PostgreSQL)
- personal.db
- kamer e-commerce.db
- geldstroom-regie.db
- Any other database, knowledge store, or external service

**Clarification on existing routines:**
If the current session is governed by an active routine (e.g., close-session, end-of-day routine) that includes a team_tasks sweep or session_log write, that write is authorized by the routine — not by idea routing. The idea-routing process does not add authorization; it relies on pre-existing authorization.

---

## 15. Implementation Approval Requirements

Implementation may not begin until all of the following are true:

1. For routes with Review Gate (C, D, E, F): the Review Gate has been completed per SOP-016, and the Owner has made a DP-3 decision to accept the proposal.
2. For Route B without escalation: the Owner has made a DP-3 decision to accept the lightweight proposal.
3. The Owner has separately and explicitly confirmed implementation may begin (DP-4 passed). Proposal acceptance at DP-3 is not an implementation authorization.
4. For S9 ideas: explicit Owner security sign-off is part of the DP-4 confirmation.
5. For S10 ideas: Owner has confirmed approval for each domain scope individually.

---

## 16. Implementation Report Requirements

Every Route C, D, E, or F implementation produces an implementation report. The implementation report must include:

| Field | Requirement |
|---|---|
| Deliverable path | Exact file path of the implementation report |
| Scope completed | List every action taken; one line per action |
| Scope not completed | List every approved action not taken and why |
| Files created | Exact paths of all files created |
| Files modified | Exact paths of all files modified, with before/after state summary |
| Files moved or deleted | Exact source and destination paths |
| Database records written | Database name, table name, record ID (if applicable) |
| Tests or verifications performed | List each verification and its result |
| Known issues or deviations | Any deviation from the approved proposal; reason and impact stated |
| Required follow-up | List any open items requiring a separate action or triage |
| Post-check results | Results of all post-checks specified in the proposal |

The implementation report must not include system file content, credentials, or sensitive data beyond what is needed to confirm scope completion.

---

## 17. Lifecycle Decision Requirements

Every accepted implementation-enabling deliverable (Route C, D, E, F) enters the SOP-017 lifecycle process after Owner acceptance at DP-5.

The Maintainer surfaces lifecycle processing candidates to the Owner per SOP-017 Phase 4. The Maintainer does not execute lifecycle processing unilaterally.

Lifecycle decisions must be completed before the session is closed, unless the Owner explicitly defers the lifecycle decision to a named future session.

---

## 18. Explicit Exclusions

The following actions are prohibited under this SOP regardless of route, scenario class, impact label, or session context:

**EX-1:** No implementation step may begin before DP-4 (implementation confirmation) regardless of DP-3 outcome.

**EX-2:** No governance file (GL, SOP, Workstream, AGENT.md, CLAUDE.md, or other governance instrument — see Section 2.4) may be modified as part of any route except S8/Route D, and only after SOP-015 approval at DP-3. Operational system files (scripts, handlers, integration files, skill files, configuration files, and operational code files — see Section 2.4) may be modified via Route C or higher, subject to Review Gate, DP-3, and DP-4.

**EX-3:** No credential, token, API key, or OAuth material may be stored, logged, or written to any system as part of any route except S9/Route F, and only after explicit Owner security sign-off at DP-4.

**EX-4:** No multi-domain database write (writing to more than one domain database in a single action) may occur without explicit per-domain Owner approval.

**EX-5:** No idea may be classified and routed for Medium, High, or Critical impact without presenting the classification to the Owner at DP-1. Low-impact ideas may proceed to Route A with Owner confirmation at DP-4 only.

**EX-6:** No scope expansion may occur mid-route without re-triage and Owner approval of the expanded scope at DP-1.

**EX-7:** No idea may remain unclassified for more than one session without being surfaced to the Owner as an open item at session close.

**EX-8:** No vague idea may be "resolved" by guessing the classification. Vague ideas require clarification per Section 6.

**EX-9:** No persistent write may be executed as a result of idea routing itself. Persistent writes require a pre-approved routine or explicit Owner approval independent of the routing decision. See Section 14.

---

## 19. Hard Rules

The following rules are hard constraints that apply regardless of context, session, agent, or tool:

**HR-1:** Triage may be automatic; implementation may not.

**HR-2:** An approved route is not an approved proposal. An approved proposal (DP-3) is not an implementation confirmation. DP-4 is always a separate step.

**HR-3:** Any review of a governance-relevant deliverable produced by this SOP must include a Review Context Packet per the SOP-016 amendment and must include all companion sources listed in Section 3a.

**HR-4:** A classified idea that has been parked, deferred, or rejected may not be re-opened without Owner confirmation.

**HR-5:** The scenario class and impact label are assigned by the Maintainer. The Owner may override either assignment at any decision point.

**HR-6:** The proposed SOP-018 number must be re-confirmed against the live SOP-index.md immediately before implementation. Do not create the SOP file before the number is re-confirmed.

**HR-7:** Route B may not claim to be free of Review Gate triggers without the Maintainer explicitly confirming in writing that all Route B escalation conditions (Section 9) are false.

---

## 20. Changelog

| Date | Version | Change |
|---|---|---|
| 2026-06-05 | v01 | Initial proposal |
| 2026-06-05 | v02 | Added role-based agent table and Review Gate mode definitions to Section 2; added Section 3a (Companion Sources); amended Section 4 (persistent write prohibition); added Route B escalation rule to Section 9; restructured Section 12 (DPs) so Review Gate precedes Owner decision; added Section 14 (Persistent Write Rules); added EX-9 and HR-6, HR-7; updated S4 and S10 to role-based agents; added Section 21 (Pack-level Implementation Order); added numbering re-confirmation note |
| 2026-06-05 | v03 | Added Section 2.4 (File Category Definitions); split Route B condition 1 into 1a (governance file → Route D) and 1b (operational system file → Route C); updated escalation table; updated EX-2 to distinguish governance files from operational system files; updated Section 13 condition 2 and final line; updated S2, S5, S8 scenario language for file category consistency; corrected Revision Summary item 13 ("Section 22" → "Section 21"); corrected Acceptance Criteria item 12 ("7" → "9" explicit exclusions); updated HR-7 to remove hard count |

---

## 21. Pack-level Implementation Order

This SOP is part of the Idea-to-Implementation Governance Pack. The pack must be implemented in the following order. Do not skip or reorder steps.

| Step | Action | Post-check required |
|---|---|---|
| 1 | Implement GL-018 (create GL file, update gl-index.md) | Verify file content, index entry, no unintended changes |
| 2 | Implement SOP-018 (create SOP file, update SOP-index.md) | Verify file content, index entry, no unintended changes |
| 3 | Implement SOP-016 RCP amendment (modify SOP-016 with exact text specified) | Verify amendment applied correctly, no other sections changed, no new content beyond what is specified |
| 4 | Execute smoke test — only if Owner separately approves in a dedicated session | Confirm all 10 test cases pass; confirm all explicit confirmations honored |

Steps 1 through 3 must each be individually post-checked and confirmed by the Owner before the next step begins. The smoke test (step 4) is not authorized by approval of any of the three proposals unless the Owner explicitly approves smoke test execution as a separate action in a dedicated session.

Full post-check requirements per step are defined in the smoke test plan companion document.

---

## Numbering Re-confirmation Note

The proposed SOP number SOP-018 is based on the current highest SOP in the index (SOP-017) at the time this proposal was prepared. This number must be re-confirmed immediately before implementation by checking the live `SOP-index.md`. If any new SOP has been added between now and implementation, the proposed number must be updated accordingly. Do not create the SOP file before the number is re-confirmed.

---

## Proposed SOP Index Entry

> **Note:** This is a proposal. The entry below must not be added to `SOP-index.md` until the Owner has approved this proposal, the SOP number has been re-confirmed, and the SOP-018 file has been created and post-checked.

Proposed addition to `Team Knowledge/Core/SOPs/SOP-index.md`:

```
| SOP-018 | [[SOP-018_Idea-to-Implementation Routing Procedure]] | Procedure: idea intake, scenario classification (S1–S10), impact labels, route selection (A–F), Owner decision points DP-1 through DP-6, Review Gate triggers, persistent write rules, implementation approval, implementation report requirements, and lifecycle decision trigger |
```

---

## Acceptance Criteria

This proposal is acceptable when all of the following are true:

1. The 10 scenario classes (S1–S10) cover every common idea type without significant overlap or uncovered cases.
2. The 4 impact labels (Low, Medium, High, Critical) are mutually exclusive and exhaustive.
3. The 6 routes (A–F) are mutually exclusive and correctly mapped to scenario × impact combinations.
4. The Route B escalation rule (Section 9) is complete: conditions 1a, 1b, and 2–6 are stated; the escalation path for each is defined; governance files escalate to Route D and operational system files escalate to Route C.
5. The 6 Owner Decision Points (DP-1 through DP-6) correctly separate Owner decisions from Maintainer actions; no automatic advancement is possible.
6. DP-3 is correctly defined: for routes requiring Review Gate, DP-3 follows the Review Gate, not precedes it. The sequencing note in Section 12 is present and unambiguous.
7. Section 14 (Persistent Write Rules) is clear and unambiguous: transient capture is permitted; persistent writes require pre-approved routine or explicit Owner approval.
8. EX-9 is present and consistent with Section 14.
9. S4 references the research role, not a named agent.
10. S10 references role-based agents; the note about personal priority gate and project classification correctly traces these to existing operating rules, not new SOP-018 gates.
11. Section 3a (Companion Sources) is complete and actionable.
12. All 9 explicit exclusions (EX-1 through EX-9) and 7 hard rules (HR-1 through HR-7) are internally consistent and do not conflict with GL-014, GL-015, GL-016, GL-017, SOP-015, SOP-016, or SOP-017.
13. Section 2.4 (File Category Definitions) clearly distinguishes governance files from operational system files; the distinction is used consistently in EX-2, Section 13, Route B escalation, and scenario descriptions.
14. The proposed SOP number SOP-018 is proposal-only; re-confirmation note is present.
15. No execution has occurred as a result of this proposal document.

---

## Owner Decision Options

| Option | Action |
|---|---|
| Approve this proposal | SOP-018 file may be created after number re-confirmation; SOP-index.md may be updated |
| Request amendments | Specific changes required; revised v04 prepared; SOP-018 not created until approved |
| Approve with modifications | Owner states exact modifications; v04 created before SOP-018 is written |
| Defer | Proposal noted; no action until Owner names a condition for revisit |
| Reject | Proposal not accepted; reason stated; SOP-018 not created |

---

Delivered on: 2026-06-05
Delivered at: Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/
