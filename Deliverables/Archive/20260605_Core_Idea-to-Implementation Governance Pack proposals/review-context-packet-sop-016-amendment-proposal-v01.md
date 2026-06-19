# PROPOSAL — SOP-016 Amendment: Mandatory Review Context Packet

**Proposal status:** Draft v01
**Prepared by:** Larry (Team Orchestrator)
**Date:** 2026-06-05
**For:** Owner Walter Kamer
**Amends:** `SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md`
**Governance baseline:** GL-014, GL-015, GL-016, GL-017, SOP-015, SOP-016, SOP-017

---

> **PROPOSAL ONLY.**
> Nothing in this document is implemented, active, or authoritative until the Owner explicitly approves it. SOP-016 is not modified by this proposal document. No system files are created, modified, or moved. No indexes are updated. No execution follows from this document without explicit Owner approval.

> **Exact-text amendment.** If approved, this proposal authorizes the addition of one new section to SOP-016 and minor amendments to Sections 3, 4, and 5 of SOP-016. The exact text of all additions is specified below. No other changes are made.

---

## Purpose of this Proposal

SOP-016 defines three review modes and 13 review checks. It does not define the format of the context package that makes a review self-contained and portable across tools, systems, and reviewers.

Without a mandatory Review Context Packet (RCP), a reviewer who is:

- A new AI system with no session history
- A different tool (ChatGPT, Gemini, a future system)
- A human reviewer unfamiliar with the myPKA system
- The same AI system in a fresh session

...cannot reconstruct the governance context needed to apply the 13 checks reliably. The reviewer must either make assumptions, ask clarifying questions, or stop — all of which defeat the purpose of a portable governance review gate.

This amendment adds a mandatory Review Context Packet to SOP-016. The RCP is a structured document that must accompany every governance-relevant review. It provides everything a reviewer needs to complete a review independently of prior chat memory.

---

## Current State of SOP-016

SOP-016 currently defines:

- Section 1: Purpose
- Section 2: Role Definitions
- Section 3: Mode 1 — External Review (5 steps)
- Section 4: Mode 2 — Internal Multi-Agent Review
- Section 5: Mode 3 — Single-System Fallback
- Section 6: Review Checks (13 checks)
- Section 7: Owner Decision Options
- Section 8: Worked Examples
- Section 9: Relationship to SOP-015
- Section 10: Knowledge Currency

Mode 1, Step 1 currently defines the review package as:

> "The orchestrator assembles the review package, which includes: deliverable path, deliverable type, governance baseline, relevant active GLs and SOPs, review scope, non-goals, known dependencies, and any hard exclusions."

This definition is correct but not structured as a mandatory portable format.

---

## Proposed Amendment

### What changes

1. A new Section 11 is added: **Review Context Packet (RCP)** — defines the mandatory format, required fields, and usage instructions.
2. Section 3 (Mode 1), Step 1 is amended to reference the RCP as a required input.
3. Section 4 (Mode 2), Procedure is amended to require RCP preparation before review package is distributed.
4. Section 5 (Mode 3), Step 1 is amended to require RCP preparation before self-review begins.
5. Section 8 (Worked Examples) is amended to add one new example demonstrating RCP usage (Example 4).

### What does not change

- The 13 review checks (Section 6) are not modified.
- The Owner Decision Options (Section 7) are not modified.
- The Role Definitions (Section 2) are not modified.
- The scope of SOP-016 is not modified.
- No GL files are modified.
- No other SOPs are modified.

---

## Proposed Section 11 — Review Context Packet (RCP)

The following is the exact proposed text for the new Section 11. This text is not active. It is presented for Owner review.

---

### 11. Review Context Packet (RCP)

#### 11.1 Purpose

A Review Context Packet (RCP) is a structured document that makes a governance-relevant review self-contained and portable. A reviewer presented with the RCP and the deliverable under review must be able to complete the full 13-check review without accessing any prior chat history, session memory, or system-specific state.

This requirement applies regardless of which system performs the review: a new AI session, a different AI tool, a human reviewer, or the same system in a different context.

#### 11.2 When an RCP Is Required

An RCP is required for every review in which the deliverable is any of the following:

- A proposal authorizing implementation (any route from SOP-018)
- A proposal for a system-file change (SOP-015 deliverable)
- An execution report for a High or Critical impact action
- A closure report
- Any amendment to a GL, SOP, Workstream, AGENT.md, or CLAUDE.md
- Any cross-domain deliverable (S10 scenario class per SOP-018)
- Any security-sensitive deliverable (S9 scenario class per SOP-018)

An RCP is not required for routine status reports, Low-impact execution confirmations, or single-check action records. The Maintainer determines whether an RCP is required and documents the determination in the session log.

#### 11.3 Mandatory RCP Fields

An RCP must contain all of the following fields. Fields may not be omitted. If a field is not applicable, state "Not applicable" with a one-line reason.

| # | Field | Required content |
|---|---|---|
| 1 | Review purpose | One sentence: what decision does this review enable? |
| 2 | Deliverable path | Exact file path(s) of the deliverable(s) under review |
| 3 | Deliverable type | Proposal / Execution report / Closure report / Amendment / Other (specify) |
| 4 | Owner | Walter Kamer |
| 5 | Maintainer | Larry (Team Orchestrator) |
| 6 | Governance baseline | List of all active GLs and SOPs by number and title at the time of review |
| 7 | Relevant active GLs and SOPs | The specific GLs and SOPs that the reviewer must apply or verify against for this review |
| 8 | Review scope | Exact list of what the reviewer must evaluate — not broader than the deliverable |
| 9 | Non-goals | Explicit list of what the reviewer must not evaluate, modify, or recommend |
| 10 | Hard exclusions | Actions that must not occur during or as a result of this review — stated as prohibitions |
| 11 | Allowed Owner decisions | List the applicable options from SOP-016 Section 7 |
| 12 | Required reviewer checks | The 13 standard checks from Section 6 plus any additional checks specific to this deliverable |
| 13 | Required output format | The format the reviewer must use to return findings: pass/fail per check, uncertainty list, hard stop list, Owner decision packet |
| 14 | Known dependencies | Files, databases, prior decisions, or external systems that the deliverable depends on |
| 15 | Canonical source files | The authoritative source documents the reviewer must use — exact paths; not summaries |
| 16 | Execution allowed | Yes / No. State explicitly whether any execution may occur as a result of this review, or whether this review produces findings only. |
| 17 | Lifecycle processing in scope | Yes / No. State explicitly whether lifecycle decisions (SOP-017) are in scope for this review session. |
| 18 | Prior memory disclaimer | "The reviewer must not rely on any prior chat history, session memory, or accumulated tool context. All context required for this review is contained in this RCP and the deliverable under review. If the reviewer requires information not present in this RCP, the reviewer must stop and request it from the Maintainer before proceeding." |

#### 11.4 RCP Template

The following template must be used when preparing an RCP. All fields are mandatory. Omissions are not permitted.

```markdown
## Review Context Packet

**RCP version:** [version number, e.g. v01]
**Prepared by:** [name]
**Date:** [YYYY-MM-DD]
**Review session:** [session identifier or date]

---

### Field 1 — Review Purpose
[One sentence: what decision does this review enable?]

### Field 2 — Deliverable Path
[Exact file path(s)]

### Field 3 — Deliverable Type
[Proposal / Execution report / Closure report / Amendment / Other]

### Field 4 — Owner
Walter Kamer

### Field 5 — Maintainer
Larry (Team Orchestrator)

### Field 6 — Governance Baseline
[List all active GLs and SOPs by number and title]

### Field 7 — Relevant Active GLs and SOPs
[The specific GLs and SOPs that apply to this review]

### Field 8 — Review Scope
[Exact list of what the reviewer must evaluate]

### Field 9 — Non-Goals
[Explicit list of what the reviewer must not evaluate, modify, or recommend]

### Field 10 — Hard Exclusions
[Actions that must not occur during or as a result of this review]

### Field 11 — Allowed Owner Decisions
[List applicable options from SOP-016 Section 7]

### Field 12 — Required Reviewer Checks
[The 13 standard checks plus any additional checks specific to this deliverable]

### Field 13 — Required Output Format
[The format the reviewer must use to return findings]

### Field 14 — Known Dependencies
[Files, databases, prior decisions, or external systems]

### Field 15 — Canonical Source Files
[Exact paths of the authoritative source documents the reviewer must use]

### Field 16 — Execution Allowed
[Yes / No — state explicitly]

### Field 17 — Lifecycle Processing in Scope
[Yes / No — state explicitly]

### Field 18 — Prior Memory Disclaimer
The reviewer must not rely on any prior chat history, session memory, or accumulated tool context. All context required for this review is contained in this RCP and the deliverable under review. If the reviewer requires information not present in this RCP, the reviewer must stop and request it from the Maintainer before proceeding.
```

#### 11.5 RCP Usage Instructions

**For the Maintainer (Larry):**

1. Determine whether an RCP is required per Section 11.2.
2. If required: prepare the RCP before the review package is assembled or distributed.
3. Include the RCP in the review package alongside the deliverable.
4. Record in the session log: RCP prepared (yes/no), RCP version, review date.
5. If the RCP is not required: record the determination in the session log with a one-line reason.

**For the Reviewer:**

1. Read the RCP in full before reading the deliverable.
2. Verify that all 18 fields are present. If any field is absent or states "Not applicable" without a reason, stop and request completion from the Maintainer.
3. Apply only the checks listed in Field 12. Do not apply checks outside this scope.
4. Do not access prior chat history, session memory, or system-specific state. All required context is in the RCP.
5. Return findings in the format specified in Field 13.
6. If you require information not in the RCP: stop and request it from the Maintainer. Do not infer or assume.

**For the Owner:**

1. The RCP is a support document. The Owner does not need to read the RCP to make a decision.
2. The Owner decision options are listed in Field 11.
3. If the Owner notices that the RCP is missing or incomplete, the Owner may decline to review the deliverable until the RCP is corrected.

---

## Proposed Amendments to Existing SOP-016 Sections

### Amendment to Section 3 (Mode 1), Step 1

**Current text (excerpt):**
> "The orchestrator assembles the review package, which includes: deliverable path, deliverable type, governance baseline, relevant active GLs and SOPs, review scope, non-goals, known dependencies, and any hard exclusions."

**Proposed addition (new sentence at the end of Step 1):**
> "For deliverables that require an RCP per Section 11.2, the orchestrator must prepare the RCP using the template in Section 11.4 before assembling the review package. The RCP must be included in the review package. The review package is not complete without the RCP when one is required."

### Amendment to Section 4 (Mode 2), Procedure

**Proposed addition (new step at the beginning of the Mode 2 procedure):**
> "Step 0 — RCP preparation. Before distributing the review package to internal reviewers, the orchestrator prepares the RCP per Section 11. The RCP is distributed to all reviewers alongside the deliverable. Reviewers must read the RCP before reading the deliverable."

### Amendment to Section 5 (Mode 3), Step 1

**Current text:**
> "Step 1 — Declare fallback mode: The system explicitly states that Mode 3 is being used and why no external reviewer or additional agent is available."

**Proposed addition (sentence appended to Step 1):**
> "If the deliverable requires an RCP per Section 11.2, the system prepares and states the RCP in full before applying any review checks. A Mode 3 review without a required RCP is not valid."

---

## Proposed New Worked Example (Section 8, Example 4)

The following example demonstrates RCP usage for a governance-relevant idea-routing proposal.

---

### Example 4 — Proposal Review with Review Context Packet

**Scenario:** A proposal for a new script (S2, Medium impact) has been prepared. The proposal modifies one existing integration handler. The Maintainer determines an RCP is required because a system file is modified.

**Review Context Packet (abbreviated):**

- Field 1: Determine whether the integration handler modification proposal is complete, in-scope, and safe to approve.
- Field 2: `Deliverables/20260605_Core_New integration handler/handler-proposal-v01.md`
- Field 3: Proposal
- Field 6: GL-001 through GL-018 (pending), SOP-015 through SOP-018 (pending)
- Field 7: GL-016 (review gate principles), SOP-016 (this procedure), SOP-018 (idea routing — pending)
- Field 8: Review the proposal document at Field 2 for scope accuracy, correctness, and completeness.
- Field 9: Do not review the implementation itself. Do not test the script. Do not assess business value.
- Field 10: No files may be created or modified. No execution may begin. No database writes.
- Field 11: Approve execution / Request amendments / Defer / Reject
- Field 16: No — execution is not allowed; this review produces findings only.
- Field 17: No — lifecycle processing is not in scope for this review.
- Field 18: Prior memory disclaimer (full text per Section 11.4).

**Review outcome:** Reviewer applies 13 checks and returns pass/fail per check. Orchestrator packages findings and Owner decision options. Owner decides.

---

## Acceptance Criteria

This amendment proposal is acceptable when all of the following are true:

1. The 18 mandatory RCP fields are complete, non-overlapping, and together sufficient to enable a fully independent review.
2. The RCP template in Section 11.4 correctly implements all 18 fields.
3. The trigger conditions in Section 11.2 are consistent with the scope of deliverables that enter the review gate per GL-016.
4. The amendments to Sections 3, 4, and 5 are minimal — they add only the RCP requirement and do not change any existing review logic.
5. The new worked Example 4 correctly demonstrates RCP preparation and usage.
6. No changes are made to the 13 review checks (Section 6).
7. No changes are made to the Owner Decision Options (Section 7).
8. The amendment does not change the scope of SOP-016 or the definition of a governance-relevant deliverable.
9. The exact amendment text specified above is the only change made to SOP-016 if approved.
10. No execution has occurred as a result of this proposal document.

---

## Owner Decision Options

| Option | Action |
|---|---|
| Approve this amendment | SOP-016 may be modified with the exact text specified; no other changes |
| Request amendments | Specific changes to the amendment required; revised v02 prepared; SOP-016 not modified until approved |
| Approve with modifications | Owner states exact modifications; v02 created before SOP-016 is modified |
| Defer | Proposal noted; no action until Owner names a condition for revisit |
| Reject | Amendment not accepted; SOP-016 remains unchanged |

---

Delivered on: 2026-06-05
Delivered at: Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/
