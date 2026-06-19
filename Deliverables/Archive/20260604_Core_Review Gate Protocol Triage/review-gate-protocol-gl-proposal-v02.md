# Review Gate Protocol — GL Proposal v02

**File:** `Deliverables/20260604_Core_Review Gate Protocol Triage/review-gate-protocol-gl-proposal-v02.md`
**Date:** 2026-06-04
**Prepared by:** Larry, Team Orchestrator
**Status:** Formal proposal v02 — awaiting Owner decision
**Supersedes:** `review-gate-protocol-gl-proposal-v01.md`
**Paired with:** `review-gate-protocol-sop-proposal-v02.md`

**Governance:** This document is read-only. No GL file creation, no index update, no system-file
change, no database write, no backlog update, and no further governance work may be executed
without Owner Walter Kamer's explicit approval.

---

## Revision Notes — v01 to v02

Per SOP-015 discipline, all changes from v01 are listed here. No other content was changed.

| # | Change | Location |
|---|---|---|
| 1 | Added `**Owner:** Walter Kamer` directly before `**Maintainer:** Larry, Team Orchestrator` in the exact GL-016 content | Section 4 — exact GL content header |
| 2 | Replaced Owner decision options with a safer set that removes SOP-016-only implementation as a normal executable option while GL-016 does not yet exist on disk | Section 10 — Owner Decision Options |
| 3 | Updated Section 7 (Relationship to the Paired SOP Proposal) to reflect the revised option set | Section 7 |

---

## 1. Proposed GL Identity

| Field | Value |
|---|---|
| Proposed GL number | GL-016 |
| Basis for number | GL-015 is the current highest entry in `Team Knowledge/Core/Guidelines/gl-index.md` as of 2026-06-04. GL-016 is the next available number. |
| Proposed filename | `GL-016_Review Gate for Governance-Relevant Deliverables.md` |
| Proposed canonical path | `Team Knowledge/Core/Guidelines/GL-016_Review Gate for Governance-Relevant Deliverables.md` |
| Paired SOP | SOP-016 — Review Gate Procedure for Governance-Relevant Deliverables (see `review-gate-protocol-sop-proposal-v02.md`) |
| Execution order | GL-016 must be created first. GL-016 post-checks must pass. SOP-016 may only be implemented after GL-016 exists on disk and post-checks pass. If GL-016 implementation fails, SOP-016 implementation must not start. |

---

## 2. Implementation Scope

If Owner Walter Kamer approves this GL proposal for implementation, the following actions are
performed — no more, no less:

1. Create the file `Team Knowledge/Core/Guidelines/GL-016_Review Gate for Governance-Relevant Deliverables.md` with the exact content from Section 4.
2. Add one row to `Team Knowledge/Core/Guidelines/gl-index.md` as specified in Section 5.

**Nothing else is created, modified, or deleted by this implementation.**

---

## 3. Explicit Exclusions

The following are explicitly not part of this GL implementation:

- No SOP-016 file is created (separate proposal and approval required; GL-016 must exist and pass post-checks first)
- No update to GL-014 or any other GL
- No update to SOP-015 or any other SOP
- No AGENT.md files modified
- No CLAUDE.md modified
- No database writes
- No UMC or memory-db entries
- No team_tasks or team_log entries
- No Workstream files created or modified
- No scripts modified

---

## 4. Exact Full GL Content

The following is the verbatim text that will be written to
`Team Knowledge/Core/Guidelines/GL-016_Review Gate for Governance-Relevant Deliverables.md`
if this proposal is approved. No word, heading, or line may be changed at execution time.
Any amendment requires a new proposal version per SOP-015.

---

```
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
```

---

## 5. Exact gl-index.md Update Text

The following row is appended to the table in
`Team Knowledge/Core/Guidelines/gl-index.md` exactly as written. No changes at execution time.

```
| GL-016 | [[GL-016_Review Gate for Governance-Relevant Deliverables]] | Principle: governance-relevant deliverables require a review gate before execution or closure — tool-agnostic, applies to all AI systems, agents, tools, and human-assisted workflows |
```

---

## 6. Post-Check Plan

After implementation, the executing agent confirms all of the following before reporting complete:

| # | Check | Pass condition |
|---|---|---|
| 1 | File exists | `Team Knowledge/Core/Guidelines/GL-016_Review Gate for Governance-Relevant Deliverables.md` exists on disk |
| 2 | File content integrity | File content matches Section 4 of this proposal verbatim |
| 3 | GL number | File contains `GL-016` in the heading — not GL-015, GL-017, or any other number |
| 4 | Owner field present | File contains `**Owner:** Walter Kamer` before `**Maintainer:**` |
| 5 | gl-index.md updated | The GL-016 row from Section 5 is present in `gl-index.md` |
| 6 | No other files modified | No other file in the vault was touched during implementation |
| 7 | No database writes | No team_tasks, team_log, UMC, or memory-db entries were written |

---

## 7. Relationship to the Paired SOP Proposal

This GL proposal and `review-gate-protocol-sop-proposal-v02.md` form a paired set.

- GL-016 establishes the principle that SOP-016 implements.
- SOP-016 references GL-016 by name and number.
- If Owner approves Option B (paired implementation), GL-016 must be created first and all
  post-checks must pass before SOP-016 implementation begins.
- If Owner approves Option A (GL-016 only), SOP-016 remains a pending proposal and may be
  submitted for approval in a later session after GL-016 is confirmed on disk.
- SOP-016-only implementation while GL-016 does not exist on disk is not a valid execution path.

---

## 8. Optional Future Reference Updates — Separate Decision Items

The following updates would strengthen the operating model but are not part of this proposal.
Each requires a separate Owner decision and its own proposal cycle. No action is taken on these
from this proposal.

| Update | Why | When |
|---|---|---|
| Add a reference to GL-016 in GL-014 (AI Team Governance) | GL-014 is the current top-level governance reference; a link to GL-016 makes the review gate discoverable from there | After GL-016 is approved and on disk |
| Add a review gate reminder to relevant AGENT.md files | Agents that produce governance deliverables benefit from an explicit pointer | After SOP-016 is approved |
| Add GL-016 reference to CLAUDE.md | Strengthens enforcement at the orchestration layer | After both GL-016 and SOP-016 are approved |

---

## 9. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| GL number collision — another GL is created as GL-016 before this proposal is implemented | Verify gl-index.md immediately before implementation; if GL-016 is taken, reissue this proposal with the correct next available number |
| GL content is amended at execution time without a new proposal version | SOP-015 governs: any change to the approved exact text requires a new proposal version and separate Owner approval before execution |
| SOP-016 is implemented before GL-016 exists | The execution order rule in Section 1 and post-check 1 in the SOP-016 proposal prohibit this; the paired option (Option B) enforces the sequence explicitly |
| GL becomes stale after new AI systems are added | Knowledge Currency section in the GL specifies the refresh trigger |

---

## 10. Owner Decision Options

| Option | Action |
|---|---|
| **A** | Approve GL-016 implementation only — create the file and update gl-index.md as specified. SOP-016 remains a pending proposal and may be submitted for separate approval in a later session once GL-016 is confirmed on disk. |
| **B** | Approve paired implementation — GL-016 first, post-checks pass, then SOP-016 **(recommended)** |
| **C** | Request amendments to this GL proposal — specify which sections require changes; a v03 will be prepared |
| **D** | Defer both proposals |
| **E** | Reject |

**Note:** SOP-016-only implementation (without GL-016 on disk) is not presented as an option in
this proposal. SOP-016 references GL-016 by name and number. Implementing SOP-016 before GL-016
exists would produce a broken reference and is not a valid execution path.

---

*Delivered on: 2026-06-04*
*Delivered at: Deliverables/20260604_Core_Review Gate Protocol Triage/review-gate-protocol-gl-proposal-v02.md*
