# PROPOSAL — SOP-016 Amendment: Mandatory Review Context Packet

**Proposal status:** Draft v03
**Prepared by:** Larry (Team Orchestrator)
**Date:** 2026-06-05
**For:** Owner Walter Kamer
**Amends:** `SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md`
**Governance baseline:** GL-014, GL-015, GL-016, GL-017, SOP-015, SOP-016, SOP-017

---

> **PROPOSAL ONLY.**
> Nothing in this document is implemented, active, or authoritative until the Owner explicitly approves it. SOP-016 is not modified by this proposal document. No system files are created, modified, or moved. No indexes are updated. No execution follows from this document without explicit Owner approval.

> **Exact-text amendment.** If approved, this proposal authorizes the addition of one new section to SOP-016 and minor amendments to Sections 3, 4, and 5 of SOP-016. The exact text of all additions is specified below. No other changes are made.

> **Implementation dependency.** This amendment depends on SOP-018 for the definitions of S9 and S10 scenario classes referenced in Section 11.2. This amendment must be implemented after GL-018 and SOP-018 are both implemented and post-checked. If SOP-018 is not yet active, Section 11.2 applies in a reduced form as defined in Section 11.6.

---

## Revision Summary (v01 to v02)

The following changes were made in response to the Owner's v01 amendment request:

1. **Implementation dependency made explicit** — Added upfront notice and Section 11.6 defining the pre-SOP-018 behavior of this amendment.
2. **Implementation order stated** — Four-step sequence: GL-018 → SOP-018 → this amendment → smoke test.
3. **Section 11.2 amended** — S9/S10 references now include explicit "per SOP-018" qualifier and are excluded when SOP-018 is not yet active.
4. **Section 11.6 added** — Implementation Dependency and Pre-SOP-018 Behavior.
5. **Section 11.7 added** — Companion Files for Governance Pack Reviews. Lists the four pack documents that must appear in Field 15 of the RCP when reviewing any governance-pack deliverable.
6. **RCP template Field 15 updated** — Added companion files note for governance pack reviews.
7. **RCP template Field 18 strengthened** — Explicitly states the reviewer must not rely on prior chat context or accumulated tool memory.
8. **Worked Example 4 updated** — DP references aligned with SOP-018 v02 sequence (DP-1 through DP-6).
9. **Acceptance criteria updated** — Include dependency, pre-SOP-018 behavior, companion files section.

---

## Revision Summary (v02 to v03)

The following changes were made in response to the Owner's v02 amendment request:

1. **Worked Example 4 corrected** — The v02 example incorrectly framed S2-Medium as Route B first, then escalated to Route C via escalation condition 1. This was inconsistent with the route selection matrix in SOP-018 Section 10, which maps S2-Medium directly to Route C. The example has been rewritten: S2-Medium routes directly to Route C per the route matrix; no Route B check is applied. The integration handler is correctly identified as an operational system file (per SOP-018 Section 2.4). The step-by-step and abbreviated RCP are updated accordingly.
2. **Section 11.7 companion file paths updated** — All four companion document paths updated from v02 to v03 versions.
3. **Acceptance criterion 8 updated** — Now verifies that Example 4 correctly shows S2-Medium routing directly to Route C (not via Route B escalation).

---

## Purpose of this Proposal

SOP-016 defines three review modes and 13 review checks. It does not define the format of the context package that makes a review self-contained and portable across tools, systems, and reviewers.

Without a mandatory Review Context Packet (RCP), a reviewer who is:

- A new AI system with no session history
- A different tool (ChatGPT, Gemini, a future system)
- A human reviewer unfamiliar with the myPKA system
- The same AI system in a fresh session

...cannot reconstruct the governance context needed to apply the 13 checks reliably. The reviewer must either make assumptions, ask clarifying questions, or stop — all of which defeat the purpose of a portable governance review gate.

This amendment adds a mandatory Review Context Packet to SOP-016. The RCP is a structured document that must accompany every qualifying governance-relevant review. It provides everything a reviewer needs to complete a review independently of prior chat memory.

---

## Implementation Order

This amendment is part of the Idea-to-Implementation Governance Pack. The pack must be implemented in the following order:

| Step | Action |
|---|---|
| 1 | Implement GL-018 and post-check |
| 2 | Implement SOP-018 and post-check |
| 3 | Implement this SOP-016 RCP amendment and post-check |
| 4 | Execute smoke test — only if separately approved by Owner in a dedicated session |

This amendment must not be applied to SOP-016 before steps 1 and 2 are complete. Full implementation and post-check requirements are defined in the companion smoke test plan.

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
- Section 8: Worked Examples (3 examples)
- Section 9: Relationship to SOP-015
- Section 10: Knowledge Currency

Mode 1, Step 1 currently defines the review package as including: deliverable path, deliverable type, governance baseline, relevant active GLs and SOPs, review scope, non-goals, known dependencies, and hard exclusions. This definition is correct but not structured as a mandatory portable format. There is no requirement that the review package be self-contained for a fresh reviewer with no prior session context.

---

## Proposed Amendment

### What changes

1. A new Section 11 is added: **Review Context Packet (RCP)** — defines the mandatory format, required fields, and usage instructions.
2. Section 3 (Mode 1), Step 1 is amended: RCP required before review package is distributed.
3. Section 4 (Mode 2), Procedure is amended: RCP required before package is distributed to internal reviewers.
4. Section 5 (Mode 3), Step 1 is amended: RCP required before self-review begins.
5. Section 8 (Worked Examples) is amended: new Example 4 demonstrating RCP usage.

### What does not change

- The 13 review checks (Section 6) are not modified.
- The Owner Decision Options (Section 7) are not modified.
- The Role Definitions (Section 2) are not modified.
- The scope of SOP-016 is not modified.
- No GL files are modified.
- No other SOPs are modified.

---

## Proposed Section 11 — Review Context Packet (RCP)

The following is the exact proposed text for the new Section 11.

---

### 11. Review Context Packet (RCP)

#### 11.1 Purpose

A Review Context Packet (RCP) is a structured document that makes a governance-relevant review self-contained and portable. A reviewer presented with the RCP and the deliverable under review must be able to complete the full review without accessing any prior chat history, session memory, or accumulated tool context.

This requirement applies regardless of which system performs the review: a new AI session, a different AI tool, a human reviewer, or the same system in a different context. The RCP is the complete context. Nothing outside the RCP and the deliverable is authoritative for the review.

#### 11.2 When an RCP Is Required

An RCP is required for every review in which the deliverable is any of the following:

- A proposal authorizing implementation (from any route per the active idea routing procedure, if one is in effect)
- A proposal for a system-file change (SOP-015 deliverable)
- An execution report for a High or Critical impact action
- A closure report
- Any amendment to a GL, SOP, Workstream, AGENT.md, or CLAUDE.md
- Any cross-domain deliverable (S10 scenario class per SOP-018, when SOP-018 is active; when SOP-018 is not yet active, apply the GL-016 scope criteria for cross-domain deliverables)
- Any security-sensitive deliverable (S9 scenario class per SOP-018, when SOP-018 is active; when SOP-018 is not yet active, apply the GL-016 scope criteria for security-sensitive deliverables)

An RCP is not required for routine status reports, Low-impact execution confirmations, or single-check action records. The Maintainer determines whether an RCP is required and records the determination in the session context.

#### 11.3 Mandatory RCP Fields

An RCP must contain all of the following fields. Fields may not be omitted. If a field is not applicable, state "Not applicable" with a one-line reason.

| # | Field | Required content |
|---|---|---|
| 1 | Review purpose | One sentence: what decision does this review enable? |
| 2 | Deliverable path | Exact file path(s) of the deliverable(s) under review |
| 3 | Deliverable type | Proposal / Execution report / Closure report / Amendment / Other (specify) |
| 4 | Owner | Walter Kamer |
| 5 | Maintainer | Current Maintainer role holder (currently: Larry) |
| 6 | Governance baseline | List of all active GLs and SOPs by number and title at the time of review; include any pending proposals used for this review and state their pending status |
| 7 | Relevant active GLs and SOPs | The specific GLs and SOPs the reviewer must apply or verify against for this review |
| 8 | Review scope | Exact list of what the reviewer must evaluate — not broader than the deliverable |
| 9 | Non-goals | Explicit list of what the reviewer must not evaluate, modify, or recommend |
| 10 | Hard exclusions | Actions that must not occur during or as a result of this review — stated as prohibitions |
| 11 | Allowed Owner decisions | List the applicable options from SOP-016 Section 7 |
| 12 | Required reviewer checks | The 13 standard checks from Section 6 plus any additional checks specific to this deliverable |
| 13 | Required output format | The format the reviewer must use to return findings: pass/fail per check, uncertainty list, hard stop list, Owner decision packet |
| 14 | Known dependencies | Files, databases, prior decisions, or external systems the deliverable depends on |
| 15 | Canonical source files | The authoritative source documents the reviewer must use — exact paths; not summaries. When reviewing a deliverable in the Idea-to-Implementation Governance Pack, include all companion pack documents per Section 11.7. |
| 16 | Execution allowed | Yes / No — state explicitly whether any execution may occur as a result of this review |
| 17 | Lifecycle processing in scope | Yes / No — state explicitly whether lifecycle decisions (SOP-017) are in scope for this review session |
| 18 | Prior memory disclaimer | The full text specified in Section 11.4 Field 18 — this field must appear verbatim and may not be paraphrased |

#### 11.4 RCP Template

The following template must be used when preparing an RCP. All 18 fields are mandatory.

```markdown
## Review Context Packet

**RCP version:** [version number, e.g. v01]
**Prepared by:** [Maintainer name]
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
[Current Maintainer role holder]

### Field 6 — Governance Baseline
[List all active GLs and SOPs by number and title. For any pending proposal used in this review, state: "PENDING — [filename]".]

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
[The 13 standard checks (Section 6) plus any additional checks. List each check by number and name.]

### Field 13 — Required Output Format
[The format the reviewer must use to return findings: pass/fail per check, uncertainty list, hard stop list, Owner decision packet]

### Field 14 — Known Dependencies
[Files, databases, prior decisions, or external systems]

### Field 15 — Canonical Source Files
[Exact paths of the authoritative source documents the reviewer must use.
If this is a governance pack review, include all four companion documents per Section 11.7.]

### Field 16 — Execution Allowed
[Yes / No — state explicitly]

### Field 17 — Lifecycle Processing in Scope
[Yes / No — state explicitly]

### Field 18 — Prior Memory Disclaimer
The reviewer must not rely on any prior chat history, session memory, or accumulated tool context. All context required for this review is contained in this RCP and the deliverable under review. If the reviewer requires information not present in this RCP and the deliverable, the reviewer must stop and request it from the Maintainer before proceeding. Inferring missing context from prior conversations or tool state is not permitted and will invalidate the review findings.
```

#### 11.5 RCP Usage Instructions

**For the Maintainer:**

1. Determine whether an RCP is required per Section 11.2.
2. If required: prepare the RCP before the review package is assembled or distributed.
3. Include the RCP in the review package alongside the deliverable.
4. Record in session context: RCP prepared (yes/no), RCP version, review date, determination rationale.
5. If not required: record the determination in session context with a one-line reason.

**For the Reviewer:**

1. Read the RCP in full before reading the deliverable.
2. Verify that all 18 fields are present and complete. If any field is absent or states "Not applicable" without a reason: stop and request completion from the Maintainer.
3. Apply only the checks listed in Field 12. Do not apply checks outside this scope.
4. Do not access prior chat history, session memory, or accumulated tool context. All required context is in the RCP and the deliverable.
5. Return findings in the format specified in Field 13.
6. If you require information not in the RCP or the deliverable: stop and request it from the Maintainer. Do not infer or assume.
7. Do not execute any action whose authorization is not explicit in Field 16 (Execution Allowed).

**For the Owner:**

1. The RCP is a support document. The Owner reviews findings and decision options — not the RCP itself.
2. Decision options are listed in Field 11.
3. If the Owner notices that the RCP is missing or incomplete, the Owner may decline to review the deliverable until the RCP is corrected.

#### 11.6 Implementation Dependency and Pre-SOP-018 Behavior

This amendment depends on SOP-018 for the definitions of scenario classes S9 (security-sensitive) and S10 (cross-domain) referenced in Section 11.2.

**Implementation order (mandatory):**

1. GL-018 implemented and post-checked
2. SOP-018 implemented and post-checked
3. This SOP-016 RCP amendment implemented and post-checked
4. Smoke test executed — only if separately approved by Owner in a dedicated session

This amendment must not be applied to SOP-016 before steps 1 and 2 are complete.

**Pre-SOP-018 behavior (if this amendment is applied before SOP-018 is active):**

This situation must not arise if the implementation order above is followed. If for any reason this amendment is evaluated before SOP-018 is active, the following reduced behavior applies:

- The Section 11.2 condition "any cross-domain deliverable (S10 scenario class per SOP-018)" does not apply. Instead, use the GL-016 scope criteria to determine whether a cross-domain deliverable requires an RCP.
- The Section 11.2 condition "any security-sensitive deliverable (S9 scenario class per SOP-018)" does not apply. Instead, use the GL-016 scope criteria to determine whether a security-sensitive deliverable requires an RCP.
- All other Section 11.2 conditions apply regardless of SOP-018 status.
- Field 6 (Governance Baseline) must state: "SOP-018 is not yet active" and list the pending proposal path.

#### 11.7 Companion Files for Governance Pack Reviews

When reviewing any deliverable that is part of the Idea-to-Implementation Governance Pack (GL-018 proposal, SOP-018 proposal, this amendment, or the smoke test plan), Field 15 (Canonical Source Files) of the RCP must include all four companion documents listed below. The reviewer must read these documents before applying review checks. Their pending status must be stated.

| Companion document | Path | Status at time of this proposal |
|---|---|---|
| GL-018 proposal | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/idea-routing-gl-proposal-v03.md` | PENDING — not yet implemented |
| SOP-018 proposal | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/idea-routing-sop-proposal-v03.md` | PENDING — not yet implemented |
| SOP-016 RCP amendment proposal | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/review-context-packet-sop-016-amendment-proposal-v03.md` | PENDING — not yet implemented |
| Smoke test plan | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/idea-routing-smoke-test-plan-v03.md` | PENDING — not yet executed |

After implementation, update the paths in Field 15 to the canonical locations of the implemented documents.

---

## Proposed Amendments to Existing SOP-016 Sections

### Amendment to Section 3 (Mode 1), Step 1

**Current text (excerpt):**
> "The orchestrator assembles the review package, which includes: deliverable path, deliverable type, governance baseline, relevant active GLs and SOPs, review scope, non-goals, known dependencies, and any hard exclusions."

**Proposed addition (new sentences appended to Step 1):**
> "For deliverables that require an RCP per Section 11.2, the orchestrator must prepare the RCP using the template in Section 11.4 before assembling the review package. The completed RCP must be included in the review package. The review package is not complete without the RCP when one is required. Pending proposals used for context must be listed in Field 6 of the RCP with their pending status stated."

### Amendment to Section 4 (Mode 2), Procedure

**Proposed addition (new step inserted before the first step of the Mode 2 procedure):**
> "Step 0 — RCP preparation. Before distributing the review package to internal reviewers, the orchestrator prepares the RCP per Section 11. The RCP is distributed to all reviewers alongside the deliverable. Reviewers must read the RCP before reading the deliverable. The review does not begin until all reviewers confirm the RCP is complete."

### Amendment to Section 5 (Mode 3), Step 1

**Current text:**
> "Step 1 — Declare fallback mode: The system explicitly states that Mode 3 is being used and why no external reviewer or additional agent is available."

**Proposed addition (sentence appended to Step 1):**
> "If the deliverable requires an RCP per Section 11.2, the system prepares and states the RCP in full before applying any review checks. A Mode 3 review without a required RCP is not valid and may not be presented to the Owner as a completed review."

---

## Proposed New Worked Example (Section 8, Example 4)

### Example 4 — Proposal Review with Review Context Packet (v03)

**Scenario:** A proposal for a script extension (S2, Medium impact) has been prepared. The Maintainer consults the route selection matrix: S2-Medium maps directly to Route C. No Route B check is required; the route matrix assigns Route C for S2-Medium independently of any escalation condition. The proposal modifies an existing Todoist integration handler, which is an operational system file (per SOP-018 Section 2.4). The operational system file modification triggers the Review Gate per SOP-018 Section 13. An RCP is required.

**Step-by-step:**

1. Maintainer classifies the idea: S2-Medium.
2. Maintainer consults route matrix (SOP-018 Section 10): S2-Medium → Route C (direct).
3. Maintainer prepares a full proposal (Route C).
4. Maintainer prepares the RCP per Section 11.4.
5. Maintainer assembles the review package: RCP + proposal.
6. Review Gate executed (Mode 1 or Mode 2 per availability and impact).
7. Reviewer reads RCP first; then reads proposal; applies 13 checks; returns findings.
8. Maintainer packages Owner decision packet: proposal + findings + Owner decision options.
9. Owner makes DP-3 decision (post-Review Gate): Accept.
10. Owner makes DP-4 decision (separate step): Confirm implementation may begin.

**Abbreviated RCP for this example:**

- Field 1: Determine whether the script extension proposal is complete, in-scope, and safe to proceed to implementation.
- Field 2: `[exact path of proposal file]`
- Field 3: Proposal (Route C, S2-Medium)
- Field 6: GL-016, SOP-016, GL-018 (PENDING), SOP-018 (PENDING)
- Field 8: Review the proposal at Field 2 for scope accuracy, operational system file change completeness, and review check compliance.
- Field 9: Do not review the implementation. Do not test the script. Do not assess business value.
- Field 10: No files may be created or modified. No execution may begin. No database writes.
- Field 11: Accept / Request amendments / Defer / Reject (per SOP-016 Section 7)
- Field 16: No — execution is not allowed; this review produces findings only.
- Field 17: No — lifecycle processing is not in scope.
- Field 18: Prior memory disclaimer (full verbatim text per Section 11.4).

---

## Acceptance Criteria

This amendment proposal is acceptable when all of the following are true:

1. The 18 mandatory RCP fields in Section 11.3 are complete, non-overlapping, and together sufficient to enable a fully independent review without prior context.
2. The RCP template in Section 11.4 correctly implements all 18 fields, including the verbatim Field 18 disclaimer.
3. Section 11.2 trigger conditions are consistent with the GL-016 scope criteria for governance-relevant deliverables.
4. Section 11.2 correctly qualifies S9 and S10 references as "per SOP-018, when active."
5. Section 11.6 correctly defines the pre-SOP-018 behavior for Section 11.2.
6. Section 11.7 lists all four governance-pack companion documents with their current v03 paths and pending status.
7. The amendments to Sections 3, 4, and 5 are minimal — they add only the RCP requirement and do not change any existing review logic.
8. Worked Example 4 correctly shows S2-Medium routing directly to Route C per the route selection matrix (no Route B escalation); the integration handler is correctly identified as an operational system file; DP-3 is Owner decision post-Review Gate; DP-4 is a separate implementation confirmation.
9. No changes are made to the 13 review checks (Section 6).
10. No changes are made to the Owner Decision Options (Section 7).
11. The amendment does not change the scope of SOP-016 or the definition of a governance-relevant deliverable.
12. The exact amendment text specified above is the only change made to SOP-016 if approved.
13. No execution has occurred as a result of this proposal document.

---

## Owner Decision Options

| Option | Action |
|---|---|
| Approve this amendment | SOP-016 may be modified with the exact text specified — after GL-018 and SOP-018 are confirmed |
| Request amendments | Specific changes required; revised v04 prepared; SOP-016 not modified until approved |
| Approve with modifications | Owner states exact modifications; v04 created before SOP-016 is modified |
| Defer | Proposal noted; no action until Owner names a condition for revisit |
| Reject | Amendment not accepted; SOP-016 remains unchanged |

---

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-06-05 | v01 | Initial proposal |
| 2026-06-05 | v02 | Made implementation dependency explicit; added Section 11.6 (pre-SOP-018 behavior); added Section 11.7 (companion files); strengthened Field 18; updated Example 4 to v02 DP sequence; updated acceptance criteria |
| 2026-06-05 | v03 | Corrected Example 4: removed Route B escalation narrative; S2-Medium routes directly to Route C per route matrix; integration handler identified as operational system file per SOP-018 Section 2.4; updated Section 11.7 companion file paths to v03; updated acceptance criterion 8 |

---

Delivered on: 2026-06-05
Delivered at: Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/
