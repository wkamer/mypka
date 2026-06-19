# GL-016 — Review Gate for Governance-Relevant Deliverables

**Owner:** Walter Kamer
**Maintainer:** Larry, Team Orchestrator
**Created:** 2026-06-04
**Scope:** All AI systems, agents, tools, scripts, automations, orchestration layers, and
human-assisted workflows operating within the myPKA AI team

---

## 1. Purpose

Any governance-relevant deliverable produced by any system, agent, tool, script, automation,
orchestration layer, or human-assisted workflow must pass through a controlled review gate before
execution, closure, escalation, or Owner decision is treated as final.

The review gate exists to detect and prevent:

- Scope drift — work performed outside the authorized scope
- Stale status sources — lower-precedence documents overriding authoritative ones
- Incorrect open or closed item status
- Out-of-scope modifications
- Secret exposure risk
- Premature execution
- Unclear or absent next steps
- Missing post-checks

---

## 2. Scope — Deliverables That Require a Review Gate

The following deliverable types require a review gate regardless of which system, agent, tool,
or workflow produced them:

| Deliverable type | Review gate required |
|---|---|
| Proposals (new) | Yes |
| Revised proposals | Yes |
| Execution reports | Yes |
| Status reports | Yes |
| Closure reports | Yes |
| Graduation candidates | Yes |
| Remediation plans | Yes |
| Migration plans | Yes |
| Rollback plans | Yes |
| System-file changes | Yes — SOP-015 applies in addition |
| Database changes | Yes |
| Automation changes | Yes |

Not in scope: conversational clarifications, single-turn read-only lookups with no downstream
action, and session log drafts awaiting routine Owner approval.

---

## 3. Core Principle — Tool-Agnostic Mandate

The review gate is tool-agnostic. It applies regardless of which AI system, agent, tool, script,
automation, orchestration layer, or human-assisted workflow produced the deliverable. The
principle does not depend on Claude, ChatGPT, Codex, n8n, MCP, or any specific implementation.

Any system, agent, tool, or workflow that produces a governance-relevant deliverable is the
producer. Any system, agent, role, or person that evaluates the deliverable before Owner decision
is the reviewer. The roles are separable from the tools that fill them.

---

## 4. Review Gate Rules

**Rule 1 — No self-execution**
Systems, tools, scripts, agents, and automations may recommend, but must not execute the
recommendation without explicit Owner Walter Kamer approval. A passing self-review or internal
review does not constitute Owner approval.

**Rule 2 — Copy-ready next instruction**
Every review outcome that requires a next action must include a copy-ready next instruction or
prompt. The Owner must not need to construct the next step from memory or inference.

**Rule 3 — Source precedence**
When status sources conflict, apply this order from highest to lowest authority:

1. Owner acceptance or final acknowledgement
2. Execution report with final status confirmation
3. team_tasks status
4. Current backlog proposal
5. Older backlog proposals or session summaries

Lower-authority sources must not override higher-authority sources. When the highest-authority
source available clearly resolves the status, the determination is final.

**Rule 4 — Role separation**
Producer, reviewer, orchestrator, and Owner decision roles must be separated whenever possible.
When a single system or agent must act as both producer and reviewer (single-system fallback),
this must be explicitly declared and the hard stop conditions from SOP-016 apply without exception.

---

## 5. Phase Definitions

These phases are distinct. Each has a defined endpoint. No phase may automatically trigger the
next. Owner approval is required to advance from one phase to the next for governance-relevant
deliverables.

| Phase | Definition | Endpoint |
|---|---|---|
| Triage | Assess a question or gap; determine the right instrument or next step | Owner approves recommended path |
| Proposal preparation | Draft a formal proposal describing scope, method, risks, and decision options | Owner receives proposal for review |
| Review | Apply review checks against a deliverable; return findings | Owner receives findings and decision options |
| Execution | Implement the approved proposal exactly as specified | Execution report produced |
| Administrative closure | Update administrative records to reflect completed status | Record updated; no content changes |
| Final closure | Issue a formal closure declaration; produce closure deliverable | Closure report accepted by Owner |

---

## 6. Relationship to SOP-016

SOP-016 (Review Gate Procedure for Governance-Relevant Deliverables) implements this principle.
It defines the three operating modes, the review package format, the 13 review checks, the Owner
decision options, and the hard stop conditions.

This GL states the principle. SOP-016 states the procedure. Neither duplicates the other. When
applying the review gate, consult SOP-016 for step-by-step execution and consult this GL for the
governing principle.

---

## 7. Relationship to SOP-015

SOP-015 (Proposal Iteration Protocol for System File Changes) governs the iterative proposal
process for system-file change proposals. SOP-015 applies within the scope of this guideline when
the deliverable is a system-file change proposal. This GL is the overarching standard; SOP-015 is
the specific procedure for one deliverable type within it. When both apply, SOP-015 governs the
proposal iteration; this GL governs the review gate.

---

## 8. Knowledge Currency

**Refresh frequency:** Review when a new AI system or agent type is added to the team, when a new
deliverable type is introduced to the operating model, or at annual team review.

**Refresh signals:**
- A new AI system produces deliverables not covered by the scope table in Section 2
- A review failure occurs that this guideline would not have detected
- SOP-016 or SOP-015 are updated in ways that affect the principle stated here
- A new operating mode is required beyond the three defined in SOP-016
