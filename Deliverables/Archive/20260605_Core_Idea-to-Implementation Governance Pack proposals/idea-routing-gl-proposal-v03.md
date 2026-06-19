# PROPOSAL — GL-018: Idea Routing and Implementation Governance Principles

**Proposal status:** Draft v03
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

## Revision Summary (v01 to v02)

The following changes were made in response to the Owner's v01 amendment request:

1. **P11 added** — Idea routing does not authorize persistent writes. Transient session capture is permitted; any persistent database write requires either a pre-approved routine or explicit Owner approval.
2. **Maintainer responsibilities corrected** — "Tracks using team_tasks" removed; replaced with "Tracks using transient session context."
3. **Section 9 added** — Required Companion Sources. Lists all documents that must accompany any review of a GL-018-governed deliverable.
4. **Section 10 added** — Pack-level Implementation Order. Brief reference to required implementation sequence.
5. **Relationship table updated** — GL-014, GL-001, and GL-004 marked as required companion sources.
6. **Numbering re-confirmation note added** — Proposed GL-018 number must be re-confirmed immediately before implementation.
7. **Acceptance criteria updated** — Include P11, companion sources, and implementation order check.

---

## Revision Summary (v02 to v03)

The following changes were made in response to the Owner's v02 amendment request:

1. **Section 10 (Pack-level Implementation Order) removed from GL-018 content** — The implementation order applies only during the initial governance pack rollout. This ephemeral note does not belong in the permanent GL-018 document. The implementation order is retained in this proposal document as proposal context only (see "Pack-level Implementation Order" section below, outside the GL-018 content boundary). The final GL-018 file will contain Sections 1 through 9 and the Changelog only.
2. **GL-018 content Changelog updated** — v03 entry notes the removal of Section 10.
3. **Acceptance criterion 9 updated** — Confirms the implementation order is proposal context only, not part of the final GL-018 content.

---

## Purpose of this Proposal

The myPKA governance system defines how to review governance-relevant deliverables (GL-016, SOP-016), what happens to accepted deliverables (GL-017, SOP-017), and how system-file change proposals are iterated (SOP-015). It does not define how an idea moves from intake to the correct implementation path.

Without this definition, two failure modes recur:

1. **Premature implementation.** An idea is expressed and execution begins immediately — without classification, proposal, or Review Gate.
2. **Over-governance.** A small, reversible idea is subjected to a full SOP-015 proposal cycle, creating disproportionate overhead and slowing useful work.

This proposal defines GL-018 — a new guideline that closes this gap by stating the governing principles for idea routing and implementation governance across the full myPKA AI team.

---

## Pack-level Implementation Order

> **Proposal context only — not part of the final GL-018 file.**
> This section describes the required implementation sequence for the Idea-to-Implementation Governance Pack. It does not appear in the final GL-018 document. After the pack is fully implemented and post-checked, this proposal document serves as the historical record of the implementation order.

This GL is part of the Idea-to-Implementation Governance Pack. The pack must be implemented in the following order:

1. GL-018 (this document) — implemented and post-checked first
2. SOP-018 — implemented and post-checked after GL-018 is confirmed
3. SOP-016 RCP amendment — implemented and post-checked after SOP-018 is confirmed
4. Smoke test — executed only if Owner separately approves in a dedicated session after all three above are confirmed

Skipping or reordering these steps is not permitted. The smoke test may not run on pending governance documents. Full implementation and post-check requirements are defined in the companion smoke test plan.

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
- Replace or modify GL-017 (Lifecycle Principles) or SOP-017 (Lifecycle Procedure)
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
Any deliverable that authorizes implementation — a proposal, a plan, a specification, an amendment — must pass through the review gate defined in GL-016 and SOP-016 before implementation begins. The exception to full Review Gate application is defined in SOP-018 Section 9 for lightweight proposals meeting all Route B conditions.

**P7 — No implementation without required Owner approval.**
Owner Walter Kamer is the sole decision authority for implementation approval. No agent, system, automation, or routine may bypass this requirement. An approved triage is not an approved implementation. An approved route is not an approved deliverable. An accepted proposal is not an implementation confirmation.

**P8 — Every accepted implementation-enabling deliverable receives a Lifecycle decision.**
Once an implementation-enabling deliverable is accepted by the Owner, it enters the lifecycle process defined in GL-017 and SOP-017. This principle does not create new lifecycle rules; it connects idea-routing outputs to the existing lifecycle process.

**P9 — Every governance-relevant review must be self-contained.**
A governance-relevant review must provide all context needed for the reviewer to function independently of prior chat history, session memory, or knowledge of specific tools. Review Context Packets are mandatory for governance-relevant idea-routing deliverables (see SOP-016 amendment and SOP-018 Section 3a). All companion sources listed in Section 9 of this GL must be included in the Review Context Packet.

**P10 — Scope gates protect the classification.**
Once an idea has been classified and a route approved, the scope of that route is fixed. Adding work to an in-progress route requires re-triage. Mid-route scope additions are not permitted without explicit Owner approval of the expanded scope.

**P11 — Idea routing does not authorize persistent writes.**
The intake, classification, and route selection steps may capture idea information transiently in session context. Transient capture is permitted. Persistent writes to any database — team_tasks, session_logs, agent_learnings, UMC, personal.db, kamer e-commerce.db, geldstroom-regie.db, or any other database — are not authorized by idea routing itself. Persistent tracking may occur only if:
(a) the write falls under a pre-approved routine that governs the current session, or
(b) the Owner explicitly approves the specific write in the current session.

---

## 5. System-Agnostic and Tool-Agnostic Operation

This guideline applies regardless of which AI system, agent, tool, or workflow executes the triage. The scenario classification, impact labels, and required governance instruments are defined by the idea's content and risk profile — not by the tool processing it.

Any competent reviewer or future AI system, when provided with:

- This guideline (GL-018)
- The routing procedure (SOP-018)
- The companion sources listed in Section 9 of this GL
- The idea description

must be able to:

1. Classify the idea into a scenario class (S1 through S10)
2. Assign an impact label (Low, Medium, High, or Critical)
3. Determine the required route
4. Identify the required deliverable types and Owner decision points
5. Determine whether a Review Gate applies and in which mode

No prior chat context, tool-specific memory, or system-specific state is required. Self-containment is a design requirement, not a preference. Companion sources must be explicitly provided — never assumed to be available through accumulated context.

---

## 6. Owner and Maintainer Responsibilities

### Owner (Walter Kamer)

- Approves the route for ideas that require explicit confirmation
- Approves all implementation-enabling deliverables after Review Gate completion (where required)
- Makes the final implementation decision (approve, request amendments, defer, reject)
- Provides a separate, explicit implementation confirmation before execution begins
- May park, reject, or defer any idea at any stage without justification required
- Is the sole decision authority — this authority may not be delegated to any agent, system, or automated workflow

### Maintainer (currently: Larry)

- Performs or routes triage for every incoming idea
- Assigns scenario class, impact label, and recommended route
- Presents the classification to the Owner for confirmation on all Medium, High, and Critical ideas
- Delegates to the appropriate specialist once the route is confirmed
- Tracks ideas through the routing pipeline using transient session context only; persistent tracking requires pre-approved routine or explicit Owner approval
- Surfaces blocked, stalled, or unresolved ideas at session close
- Ensures Review Context Packets are prepared for all governance-relevant reviews
- Ensures all companion sources listed in Section 9 are included in the Review Context Packet

---

## 7. Relationship to Existing Governance

| Instrument | Relationship to GL-018 | Required companion source |
|---|---|---|
| GL-014 — AI Team Governance | GL-018 operates within the approval gates and escalation principles defined by GL-014. GL-018 does not modify GL-014. | Yes — must be provided in the RCP |
| GL-015 — Memory Domain Routing | Memory writes triggered by idea routing follow GL-015 routing rules without exception. GL-018 does not modify GL-015. | No |
| SOP-015 — Proposal Iteration Protocol | System-file changes identified through idea routing follow SOP-015 when the idea is classified as scenario S8 or when any route produces a system-file change proposal. GL-018 does not modify SOP-015. | Yes — for Route D and S8 reviews |
| GL-016 — Review Gate Principles | Every implementation-enabling deliverable produced through idea routing enters the review gate per GL-016, subject to the Route B conditions in SOP-018 Section 9. GL-018 does not modify GL-016. | Yes — must be provided in the RCP |
| SOP-016 — Review Gate Procedure | Review gate execution follows SOP-016, including the Review Context Packet section added by the SOP-016 amendment. GL-018 does not modify the existing sections of SOP-016. | Yes — must be provided in the RCP |
| GL-017 — Lifecycle Principles | Accepted implementation-enabling deliverables enter the lifecycle per GL-017. GL-018 does not modify GL-017. | Yes — for lifecycle decisions |
| SOP-017 — Lifecycle Procedure | Lifecycle processing of accepted deliverables follows SOP-017. GL-018 does not modify SOP-017. | Yes — for lifecycle decisions |
| SOP-018 — Idea Routing Procedure | SOP-018 is the operational procedure that implements the principles stated in this GL. GL-018 states the principles. SOP-018 states the procedure. Neither duplicates the other. | Yes — must be provided in the RCP |
| GL-001 — File Naming Conventions | Proposed GL-018 filename and all proposal filenames must comply with GL-001. | Yes — for filename compliance |
| GL-004 — Canonical Paths | Structural ideas (scenario S7) that rename or move canonical paths must follow GL-004 or its active successor. | Yes — for S7 reviews |

GL-018 adds a routing layer upstream of the existing governance chain. It does not supersede, override, or shortcut any existing instrument.

---

## 8. Knowledge Currency

| Field | Value |
|---|---|
| Last reviewed | 2026-06-05 |
| Review frequency | When any referenced governance instrument is updated; when a new recurring scenario class is identified in practice that does not fit S1–S10 |
| Owner-directed exceptions | Any exception to the principles in this GL requires explicit Owner approval and a Changelog entry |

---

## 9. Required Companion Sources

Any review of a deliverable produced under GL-018 governance must include the following documents in the Review Context Packet. These documents are referenced — not defined — within GL-018. A reviewer without access to these documents cannot independently verify compliance.

| Document | Required for |
|---|---|
| SOP-018 — Idea-to-Implementation Routing Procedure (pending) | All reviews — implements the principles of this GL |
| GL-016 — Review Gate Principles | All reviews — defines when a Review Gate is required |
| SOP-016 — Review Gate Procedure | All reviews — defines the 13 checks and Owner decision options |
| GL-017 — Deliverable Lifecycle Principles | All lifecycle-capable reviews |
| SOP-017 — Lifecycle Procedure | All lifecycle-capable reviews |
| SOP-015 — Proposal Iteration Protocol | Route D reviews and any S8 review |
| GL-014 — AI Team Governance | All reviews — defines approval gates and escalation |
| Active file naming conventions (currently: GL-001) | All reviews where a filename is proposed |
| Active canonical paths reference (currently: GL-004) | Reviews involving S7 (structural) ideas or path changes |

When any of the above documents is in a pending-proposal state (not yet implemented), the pending proposal file must be provided as the companion source and its pending status must be stated in the Review Context Packet.

---

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-06-05 | v01 | Initial proposal |
| 2026-06-05 | v02 | Added P11 (persistent writes); corrected Maintainer responsibilities; added Section 9 (Companion Sources); added Section 10 (Implementation Order); updated relationship table with companion source designations; added numbering re-confirmation requirement; updated acceptance criteria |
| 2026-06-05 | v03 | Removed Section 10 (Pack-level Implementation Order) from GL-018 content; implementation order retained as proposal context only — not part of the final GL-018 document; GL-018 content ends after Section 9 |

---

## Numbering Re-confirmation Note

The proposed GL number GL-018 is based on the current highest GL in the guidelines index (GL-017) at the time this proposal was prepared. This number must be re-confirmed immediately before implementation by checking the live `gl-index.md` file. If any new GL has been added between now and implementation, the proposed number must be updated accordingly. Do not create the GL file before the number is re-confirmed.

---

## Proposed GL Index Entry

> **Note:** This is a proposal. The entry below must not be added to `gl-index.md` until the Owner has approved this proposal, the GL number has been re-confirmed, and the GL-018 file has been created and post-checked.

Proposed addition to `Team Knowledge/Core/Guidelines/gl-index.md`:

```
| GL-018 | [[GL-018_Idea Routing and Implementation Governance Principles]] | Principle: every idea is triaged and classified before work starts — scenario classes S1–S10, impact labels, route requirements, and the full idea-to-implementation governance chain |
```

---

## Acceptance Criteria

This proposal is acceptable when all of the following are true:

1. Principles P1 through P11 are internally consistent and do not conflict with GL-014, GL-015, GL-016, GL-017, or SOP-015.
2. P11 (persistent writes) is clear and unambiguous: transient capture is permitted; persistent writes require pre-approved routine or explicit Owner approval.
3. The Maintainer responsibility for pipeline tracking is correctly stated as transient-only.
4. The Scope section correctly captures all input channels without over-reaching into procedural detail.
5. The Non-goals section correctly excludes all content that belongs in SOP-018 or existing governance instruments.
6. Owner and Maintainer responsibilities are correctly separated — no Owner responsibilities assigned to the Maintainer and vice versa.
7. The Relationship to Existing Governance table correctly identifies which instruments are required companion sources.
8. Section 9 (Required Companion Sources) is complete and actionable: a reviewer with these documents and the idea description can independently classify and route the idea.
9. The Pack-level Implementation Order is retained as proposal context in the proposal wrapper and is not included in the final GL-018 content. The four-step implementation sequence is correctly stated in the proposal wrapper.
10. The System-Agnostic section provides sufficient criteria for a future AI system to classify an idea without prior chat context.
11. The proposed GL number GL-018 is proposed-only; re-confirmation note is present.
12. The proposed filename `GL-018_Idea Routing and Implementation Governance Principles.md` follows GL-001 naming conventions (to be verified against live GL-001 at implementation time).
13. No execution has occurred as a result of this proposal document.

---

## Owner Decision Options

| Option | Action |
|---|---|
| Approve this proposal | GL-018 file may be created after number re-confirmation; gl-index.md may be updated; SOP-018 creation may proceed |
| Request amendments | Specific changes required; revised v04 proposal prepared; GL-018 not created until approved |
| Approve with modifications | Owner states exact modifications; v04 created before GL-018 is written |
| Defer | Proposal noted; no action until Owner names a condition for revisit |
| Reject | Proposal not accepted; reason stated; GL-018 not created |

---

## Proposal Changelog

| Date | Version | Change |
|---|---|---|
| 2026-06-05 | v01 | Initial proposal |
| 2026-06-05 | v02 | Added P11 (persistent writes); corrected Maintainer responsibilities; added Section 9 (Companion Sources); added Section 10 (Implementation Order); updated relationship table with companion source designations; added numbering re-confirmation requirement; updated acceptance criteria |
| 2026-06-05 | v03 | Moved Pack-level Implementation Order from GL-018 Section 10 to proposal context only; GL-018 content ends after Section 9; acceptance criterion 9 updated; Owner Decision Options reference v04 for next amendment round |

---

Delivered on: 2026-06-05
Delivered at: Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/
