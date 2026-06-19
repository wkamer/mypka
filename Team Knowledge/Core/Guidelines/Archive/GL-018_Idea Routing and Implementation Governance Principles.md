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
When an implementation is accepted by the Owner at DP-5 (implementation report acceptance), the implementation-enabling deliverable enters the lifecycle process at DP-6 as defined in GL-017 and SOP-017. The lifecycle decision for the implementation route occurs after DP-5. Other accepted deliverables produced during idea routing — such as proposals, research briefs, review reports, or closure reports — may separately receive lifecycle processing under SOP-017 when accepted by the Owner as standalone deliverables. Lifecycle processing may not be executed without explicit Owner approval. This principle does not create new lifecycle rules; it connects idea-routing outputs to the existing lifecycle process.

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
| SOP-015 — Proposal Iteration Protocol | Governance file changes identified through idea routing follow SOP-015 when the idea is classified as scenario S8. Operational system file changes follow Route C or higher, subject to Review Gate, DP-3, and DP-4. For the distinction between governance files and operational system files, see SOP-018 Section 2.4. GL-018 does not modify SOP-015. | Yes — for Route D and S8 reviews |
| GL-016 — Review Gate Principles | Every implementation-enabling deliverable produced through idea routing enters the review gate per GL-016, subject to the Route B conditions in SOP-018 Section 9. GL-018 does not modify GL-016. | Yes — must be provided in the RCP |
| SOP-016 — Review Gate Procedure | Review gate execution follows SOP-016, including the Review Context Packet section added by the SOP-016 amendment. GL-018 does not modify the existing sections of SOP-016. | Yes — must be provided in the RCP |
| GL-017 — Lifecycle Principles | Accepted implementation-enabling deliverables enter the lifecycle per GL-017 after DP-5 acceptance. GL-018 does not modify GL-017. | Yes — for lifecycle decisions |
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
| 2026-06-05 | v04 | Updated P8 (lifecycle timing explicit: implementation-route lifecycle decision at DP-6 after DP-5; other accepted deliverables may receive SOP-017 lifecycle processing independently as standalone deliverables; lifecycle processing requires explicit Owner approval); updated SOP-015 row in Section 7 to distinguish governance file changes (S8/Route D/SOP-015) from operational system file changes (Route C or higher; cross-reference to SOP-018 Section 2.4); added acceptance criteria 14 and 15 |
| 2026-06-05 | v05 | No GL-018 content changes. Companion file references in proposal wrapper updated to v05 versions. |

---
