# PROPOSAL — GL-018: Idea Routing and Implementation Governance Principles

**Proposal status:** Draft v01
**Prepared by:** Larry (Team Orchestrator)
**Date:** 2026-06-05
**For:** Owner Walter Kamer
**Governance baseline:** GL-014, GL-015, GL-016, GL-017, SOP-015, SOP-016, SOP-017
**Proposed GL number:** GL-018
**Proposed filename:** `GL-018_Idea Routing and Implementation Governance Principles.md`

---

> **PROPOSAL ONLY.**
> Nothing in this document is implemented, active, or authoritative until the Owner explicitly approves it. No system files are modified by this document. No indexes are updated. No GL file is created. No execution follows from this document without explicit Owner approval.

---

## Purpose of this Proposal

The myPKA governance system defines how to review governance-relevant deliverables (GL-016, SOP-016), what happens to accepted deliverables (GL-017, SOP-017), and how system-file change proposals are iterated (SOP-015). It does not define how an idea moves from intake to the correct implementation path.

Without this definition, two failure modes recur:

1. **Premature implementation.** An idea is expressed and execution begins immediately — without classification, proposal, or Review Gate.
2. **Over-governance.** A small, reversible idea is subjected to a full SOP-015 proposal cycle, creating disproportionate overhead and slowing useful work.

This proposal defines GL-018 — a new guideline that closes this gap by stating the governing principles for idea routing and implementation governance across the full myPKA AI team.

---

## Proposed GL-018 Content

The following is the complete proposed content of GL-018. This content is not active. It is presented for Owner review.

---

# GL-018 — Idea Routing and Implementation Governance Principles

---

## 1. Purpose

Any idea introduced into the myPKA AI team — by the Owner, a specialist, an integration, or an automated trigger — must be triaged before work begins. Triage determines the correct route: direct execution, proposal preparation, research, or parking. The route determines which governance instruments apply.

This guideline exists to prevent:

- **Premature implementation** — execution before a proposal has been reviewed and approved
- **Over-governance** — forcing a full proposal cycle onto ideas that do not require it
- **Route ambiguity** — uncertainty about which specialist, which deliverable type, and which approval step applies
- **Context loss** — implementation decisions that cannot be reviewed independently of the conversation that produced them

---

## 2. Scope

This guideline applies to every idea, request, question, or gap signal that enters the myPKA AI team through any channel:

- Owner messages during any routine or session
- Inbox items in `Team Inbox/`
- Integration-triggered signals and alerts
- Specialist-identified gaps or pattern findings
- Automated monitoring outputs
- Notes or observations added to any team document

An idea is any expressed desire, identified problem, observed gap, or proposed change — regardless of size, domain, or source.

---

## 3. Non-Goals

This guideline does not:

- Define the step-by-step routing procedure — that is SOP-018
- Replace or modify SOP-015 (Proposal Iteration Protocol for System File Changes)
- Replace or modify GL-016 (Review Gate Principles) or SOP-016 (Review Gate Procedure)
- Replace or modify GL-017 (Deliverable Lifecycle Principles) or SOP-017 (Lifecycle Procedure)
- Replace or modify GL-015 (Memory Domain Routing Protocol)
- Define memory routing rules or database write authorization
- Define the format of any specific deliverable type
- Define specialist assignment logic beyond maintainer routing responsibility

---

## 4. Core Principles

**P1 — Every idea is triaged.**
Triage may be automatic for Low-impact ideas. Triage results are never suppressed or skipped. Every idea receives a visible classification, even if the classification is "insufficient information — clarification required."

**P2 — Not every idea becomes a proposal.**
Ideas that use an existing capability without any modification do not require a proposal. The threshold for a proposal is: the idea requires creating, modifying, or replacing a system component, governance instrument, integration, script, database record type, or agent behavior.

**P3 — Triage may be automatic; implementation may not.**
A maintainer or specialist may automatically classify an idea and recommend a route. No implementation step — not a single file write, database insert, system-file change, or integration action — may proceed without explicit Owner approval of the relevant deliverable or action.

**P4 — Every idea is classified before work starts.**
Classification assigns: a scenario class (S1 through S10 as defined in SOP-018), an impact label (Low, Medium, High, or Critical), and a required route. Work does not begin until classification is complete and the Owner has either confirmed the route or approved direct execution for Low-impact ideas.

**P5 — Risk labels escalate the required route.**
As the impact label increases, the required governance instruments increase. A Low-impact idea may route directly to execution with Owner confirmation. A Critical-impact idea requires a proposal, a Review Gate (Mode 1 external review preferred), an implementation report, and a lifecycle decision.

**P6 — Every implementation-enabling deliverable enters Review Gate.**
Any deliverable that authorizes implementation — a proposal, a plan, a specification, an amendment — must pass through the review gate defined in GL-016 and SOP-016 before implementation begins.

**P7 — No implementation without required Owner approval.**
Owner Walter Kamer is the sole decision authority for implementation approval. No agent, system, automation, or routine may bypass this requirement. An approved triage is not an approved implementation. An approved route is not an approved deliverable.

**P8 — Every accepted implementation-enabling deliverable receives a Lifecycle decision.**
Once an implementation-enabling deliverable is accepted by the Owner, it enters the lifecycle process defined in GL-017 and SOP-017. This principle does not create new lifecycle rules; it connects idea-routing outputs to the existing lifecycle process.

**P9 — Every governance-relevant review must be self-contained.**
A governance-relevant review must provide all context needed for the reviewer to function independently of prior chat history, session memory, or knowledge of specific tools. Review Context Packets are mandatory for governance-relevant idea-routing deliverables (see SOP-016 amendment and SOP-018).

**P10 — Scope gates protect the classification.**
Once an idea has been classified and a route approved, the scope of that route is fixed. Adding work to an in-progress route requires re-triage. Mid-route scope additions are not permitted without explicit Owner approval of the expanded scope.

---

## 5. System-Agnostic and Tool-Agnostic Operation

This guideline applies regardless of which AI system, agent, tool, or workflow executes the triage. The scenario classification, impact labels, and required governance instruments are defined by the idea's content and risk profile — not by the tool processing it.

Any competent reviewer or future AI system provided with:

- This guideline (GL-018)
- The routing procedure (SOP-018)
- The relevant governance baseline (list of active GLs and SOPs)
- The idea description

must be able to:

1. Classify the idea into a scenario class (S1 through S10)
2. Assign an impact label (Low, Medium, High, or Critical)
3. Determine the required route
4. Identify the required deliverable types and Owner decision points
5. Determine whether a Review Gate applies and in which mode

No prior chat context, tool-specific memory, or system-specific state is required to make these determinations. Self-containment is a design requirement, not a preference.

---

## 6. Owner and Maintainer Responsibilities

### Owner (Walter Kamer)

- Approves the route for ideas that require explicit confirmation
- Approves all implementation-enabling deliverables before implementation begins
- Makes the final implementation decision (approve, request amendments, defer, reject)
- May park, reject, or defer any idea at any stage without justification required
- Is the sole decision authority — this authority may not be delegated to any agent, system, or automated workflow

### Maintainer (Larry)

- Performs or routes triage for every incoming idea
- Assigns scenario class, impact label, and recommended route
- Presents the classification to the Owner for confirmation on all Medium, High, and Critical ideas
- Delegates to the appropriate specialist once the route is confirmed
- Tracks ideas through the routing pipeline using team_tasks in the appropriate domain database
- Surfaces blocked, stalled, or unresolved ideas at session close
- Is responsible for ensuring Review Context Packets are prepared for all governance-relevant reviews

---

## 7. Relationship to Existing Governance

| Instrument | Relationship to GL-018 |
|---|---|
| GL-014 — AI Team Governance | GL-018 operates within the approval gates and escalation principles defined by GL-014. GL-018 does not modify GL-014. |
| GL-015 — Memory Domain Routing | Memory writes triggered by idea routing follow GL-015 routing rules without exception. GL-018 does not modify GL-015. |
| SOP-015 — Proposal Iteration Protocol | System-file changes identified through idea routing follow SOP-015 when the idea is classified as scenario S8 or when any route produces a system-file change proposal. GL-018 does not modify SOP-015. |
| GL-016 — Review Gate Principles | Every implementation-enabling deliverable produced through idea routing enters the review gate per GL-016. GL-018 does not modify GL-016. |
| SOP-016 — Review Gate Procedure | Review gate execution follows SOP-016, including the Review Context Packet section added by the SOP-016 amendment in this governance pack. GL-018 does not modify the existing sections of SOP-016. |
| GL-017 — Lifecycle Principles | Accepted implementation-enabling deliverables enter the lifecycle per GL-017. GL-018 does not modify GL-017. |
| SOP-017 — Lifecycle Procedure | Lifecycle processing of accepted deliverables follows SOP-017. GL-018 does not modify SOP-017. |
| SOP-018 — Idea Routing Procedure | SOP-018 is the operational procedure that implements the principles stated in this GL. GL-018 states the principles. SOP-018 states the procedure. Neither duplicates the other. |

GL-018 adds a routing layer upstream of the existing governance chain. It does not supersede, override, or shortcut any existing instrument.

---

## 8. Knowledge Currency

| Field | Value |
|---|---|
| Last reviewed | 2026-06-05 |
| Review frequency | When any referenced governance instrument is updated; when a new recurring scenario class is identified in practice that does not fit S1–S10 |
| Owner-directed exceptions | Any exception to the principles in this GL requires explicit Owner approval and a Changelog entry |

---

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-06-05 | v01 | Initial proposal — prepared for Owner review |

---

## Proposed GL Index Entry

> **Note:** This is a proposal. The entry below must not be added to `gl-index.md` until the Owner has approved this proposal and the GL-018 file has been created and confirmed.

Proposed addition to `Team Knowledge/Core/Guidelines/gl-index.md`:

```
| GL-018 | [[GL-018_Idea Routing and Implementation Governance Principles]] | Principle: every idea is triaged and classified before work starts — scenario classes S1–S10, impact labels, route requirements, and the full idea-to-implementation governance chain |
```

---

## Acceptance Criteria

This proposal is acceptable when all of the following are true:

1. Principles P1 through P10 are internally consistent and do not conflict with GL-014, GL-015, GL-016, GL-017, or SOP-015.
2. The Scope section correctly captures all input channels without over-reaching into procedural detail.
3. The Non-goals section correctly excludes all content that belongs in existing governance instruments or in SOP-018.
4. Owner and Maintainer responsibilities are correctly separated — no Owner responsibilities assigned to the Maintainer and vice versa.
5. The Relationship to Existing Governance table is accurate with respect to the current governance baseline (GL-001 through GL-017, SOP-001 through SOP-017).
6. The System-Agnostic section provides sufficient criteria for a future AI system to classify an idea without prior chat context.
7. The proposed GL number GL-018 is confirmed as the next available number in the guidelines index (verified: GL-017 is currently the highest).
8. The proposed filename `GL-018_Idea Routing and Implementation Governance Principles.md` follows GL-001 naming conventions.
9. No execution has occurred as a result of this proposal document.

---

## Owner Decision Options

| Option | Action |
|---|---|
| Approve this proposal | GL-018 file may be created; gl-index.md may be updated; SOP-018 creation may proceed |
| Request amendments | Specific changes required; revised v02 proposal prepared; GL-018 not created until new version is approved |
| Approve with modifications | Owner states exact modifications in this session; v02 created before GL-018 is written |
| Defer | Proposal noted; no action until Owner names a condition for revisit |
| Reject | Proposal not accepted; reason stated; GL-018 not created |

---

Delivered on: 2026-06-05
Delivered at: Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/
