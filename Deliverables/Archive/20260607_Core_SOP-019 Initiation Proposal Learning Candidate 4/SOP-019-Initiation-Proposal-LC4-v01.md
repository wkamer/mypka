# SOP-019 Initiation Proposal — Learning Candidate 4

**Type:** Governance Initiation Proposal
**Version:** v01
**Status:** Draft — Awaiting Iris Review
**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-07
**Learning Candidate id:** 4
**Learning Candidate title:** Governance checkpoints bypassed when Owner drives implementation interactively — CP invocation required even under Owner-directed pace
**Learning Candidate category:** CAT-3
**Learning Candidate status:** Promoted

---

## 1. Existence Check: Does SOP-019 Already Exist?

**Finding: Yes. SOP-019 exists.**

Path: `Team Knowledge/Core/SOPs/SOP-019_Governance Gatekeeper Procedure.md`
Created: 2026-06-06
Status: Live
Maintainer: Larry, Team Orchestrator

SOP-019 is a live, active document. This proposal is NOT for creating SOP-019 from scratch. It is for a targeted amendment to an existing live SOP.

This corrects the assumption carried in from the prior session that "SOP-019 may not yet exist as a file." It does exist.

---

## 2. Correct Structural Route

**Route: Targeted amendment to existing SOP-019 — not a new creation.**

Because SOP-019 is live, the structural route follows SOP-015 (Proposal Iteration Protocol for System File Changes) for a controlled amendment:

1. This proposal (scoping and content definition — read-only)
2. Iris review of the proposed amendment text (advisory)
3. Larry presents reviewed proposal to Owner
4. Owner authorization (yes / no / correction)
5. Larry amends SOP-019 with the exact approved text
6. Larry updates SOP-index.md (last_modified date, changelog entry)
7. Session log records the amendment

No new SOP number is required. No new GL number is required for Phase 1.

---

## 3. What SOP-019 Should Govern (With Amendment)

### Current scope (already in SOP-019)

- Invocation triggers for CP-1 through CP-4
- Context Constraint: Gatekeeper operates only on explicitly provided session context
- Blocked gate handling
- Procedural override handling (Section 5)
- Hard boundary handling
- Session log recording

### Gap identified by Learning Candidate 4

Section 3 currently states:

> "Larry invokes the Gatekeeper before the corresponding action begins. The Gatekeeper is not invoked after the fact."

This correctly defines the timing of invocation but does NOT explicitly state that CP invocation is independent of who is driving the session pace. When an Owner is directing a session interactively — saying "just proceed" or sequencing steps as direct instructions — Larry may experience conversational pressure to skip formal invocation. The SOP currently provides no explicit protection against this behavioral pattern.

### Proposed amendment to SOP-019

Add a new sub-rule to Section 3 (Invocation Procedure), inserted immediately after the opening statement of Section 3, titled **Pace Independence Rule**:

---

**Pace Independence Rule:** CP invocation is independent of session pace and instruction source. Larry invokes the relevant checkpoint before the corresponding action begins, regardless of whether the Owner is driving the session interactively, directing steps in sequence, or explicitly instructing Larry to proceed. Owner-directed pace does not exempt Larry from checkpoint invocation. The Owner may issue a procedural override after invocation (see Section 5), but the invocation itself is never skipped.

---

The amendment is one paragraph. No new sections. No new failure modes. No structural change to existing sections.

---

## 4. How CP Checkpoints Must Be Invoked in Owner-Directed Interactive Governance Flows

The Pace Independence Rule makes explicit what is currently only implied:

- **CP-1** is invoked before any DP step begins, even if the Owner opens the conversation at that DP step directly without prior context.
- **CP-2** is invoked before each DP step is executed, even if the Owner is sequencing steps in rapid succession without pausing between them.
- **CP-3** is invoked before the Review Gate is opened, even if the Owner says "open the Review Gate now."
- **CP-4** is invoked before lifecycle execution begins, even if the Owner says "start lifecycle execution."

In all cases: invocation happens first, the gate is checked, then the Owner may proceed or issue a procedural override. Invocation is never post-hoc and never skipped.

When the gate produces a clear result with no flags, the invocation adds minimal friction. The rule protects against undetected bypasses, not against efficient flow.

---

## 5. Where Iris Review Must Appear in the Flow

Per GL-021 Section 5, the required sequence for any CAT-3 governance action is:

1. Larry prepares a complete proposal (this document)
2. **Iris reviews the proposal** — advisory; assesses alignment with GL-020, safety, risk, and execution boundaries
3. Larry presents the reviewed proposal to the Owner, with Iris findings noted
4. Owner confirms: yes / no / correction
5. Larry executes only after step 4

Iris review is mandatory before Owner authorization for this amendment because:

- It modifies a live governance SOP
- It introduces a behavioral constraint on Larry specifically in Owner-directed interactive conditions
- The amendment text must be assessed for unintended friction, scope expansion, or conflict with existing SOP-019 sections, particularly Section 5 (Procedural Override Handling)

**Iris does not authorize. Iris reviews and advises. Owner authorizes.**

If Iris is not available when this proposal is presented, Larry presents the proposal to the Owner without Iris review and states this explicitly. Owner authorization is still required.

---

## 6. Files That May Require Updates

### Phase 1 — This amendment only

| File | Required change | Notes |
|---|---|---|
| `Team Knowledge/Core/SOPs/SOP-019_Governance Gatekeeper Procedure.md` | Insert Pace Independence Rule paragraph into Section 3, after opening statement | Exact text defined in Section 3 of this proposal |
| `Team Knowledge/Core/SOPs/SOP-index.md` | Update last_modified date; add changelog entry for SOP-019 | After SOP amendment is written, not before |

### Phase 2 — Out of scope for Phase 1, each requires separate Owner decision

| File | Potential change | Rationale |
|---|---|---|
| `Team Knowledge/Core/Guidelines/GL-019_Governance Gatekeeper Principles.md` | Add cross-reference note to Section 2 (Invocation Triggers) linking to the Pace Independence Rule | Principle is in the SOP; a GL-019 reference note improves discoverability |
| `CLAUDE.md` (Governance Gatekeeper section, line 302-306) | Add one-line note: CP invocation required even under Owner-directed pace | Currently references SOP-019 without naming this specific scenario |
| Larry AGENT.md (if governance behavior is specified there) | Add behavioral rule: pace independence for CP invocation | Agents read their own AGENT.md, not CLAUDE.md |
| Iris AGENT.md | No change required — Iris role is advisory, not procedural | Confirmed no change needed from this amendment |

**Note on CLAUDE.md:** CLAUDE.md already references SOP-019 at line 303 and states "Do not proceed past a blocked gate without Owner resolution." Once SOP-019 carries the Pace Independence Rule, the reference in CLAUDE.md inherits it implicitly. A CLAUDE.md addendum is useful reinforcement but is not a Phase 1 dependency.

---

## 7. Agent Roles

| Agent | Role |
|---|---|
| Larry | Author and maintainer of SOP-019. Prepares this proposal. Implements the amendment after Owner authorization. Writes session log. |
| Iris | Reviews this proposal before Owner authorization. Advisory only. Assesses alignment with GL-020, safety, and execution boundaries. Does not authorize. |
| Nolan | Not required for Phase 1. Involved in Phase 2 if AGENT.md files or CLAUDE.md behavioral rules require corresponding updates. |
| Kai | Not involved. This amendment is governance, not infrastructure. |

---

## 8. Out of Scope for Phase 1

The following are explicitly out of scope for the first implementation:

1. Creating a new SOP number — SOP-019 already exists
2. Rewriting SOP-019 in full — this is a targeted one-paragraph amendment
3. Amending GL-019 (Governance Gatekeeper Principles) — Phase 2
4. Updating CLAUDE.md — Phase 2
5. Updating any AGENT.md files — Phase 2
6. Adding a new failure mode to GL-019 Section 5 — the existing "Missing approval" failure mode covers the downstream consequence; a new failure mode is not required for Phase 1
7. Updating the Learning Candidate status in the database — separate write action, after implementation is complete
8. Any change to GL-021, GL-022, SOP-015, SOP-016, SOP-017, or SOP-018
9. Any command file updates
10. Any Todoist tasks or UMC writes before Owner authorization

---

## 9. Risks to Control

| Risk | Description | Control |
|---|---|---|
| Over-rigidity | Pace Independence Rule creates excessive friction in fast-moving Owner-directed sessions | The rule is minimal: invocation must happen; if the gate is clear, the action adds one implicit check. Friction is proportional to flag count, not invocation itself. |
| Conflation with procedural override | Owner may interpret this as redundant with Section 5 | Not redundant. Section 5 governs what happens after CP is invoked and a flag raised. The Pace Independence Rule governs whether invocation happens at all. Sequential guards, not duplicates. |
| Scope creep in amendment text | Amendment grows beyond one rule and introduces new failure modes or criteria | Scope is fixed: one paragraph, one rule. No new failure modes. No new checkpoints. |
| Conflict with Context Constraint (Section 2) | Risk that the new rule interacts with the constraint that Gatekeeper operates only on declared context | Confirmed orthogonal. Section 2 governs what the Gatekeeper may check. The Pace Independence Rule governs when Larry invokes. No overlap. |
| Retrospective application | Rule might be read as requiring re-invocation for prior sessions | Amendment applies from the date of implementation forward. No retrospective application. |

---

## 10. Exact Next Owner Action

This proposal is complete and read-only. No files have been modified.

The required next step is Iris review. After Iris delivers findings, Larry presents the reviewed proposal to the Owner.

**Iris review prompt (exact text for Larry to use):**

> Iris, please review the SOP-019 amendment proposal at `Deliverables/20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4/SOP-019-Initiation-Proposal-LC4-v01.md`. The proposal adds a Pace Independence Rule to SOP-019 Section 3. Review for: (1) alignment with GL-020 intent classification, (2) conflict with existing SOP-019 sections, especially Section 2 (Context Constraint) and Section 5 (Procedural Override), (3) unintended scope expansion, (4) execution risk. This is advisory review only. Do not authorize. Return your findings for Larry to present to the Owner.

**After Iris review, the Owner confirms with one of three responses:**

- **Yes** — proceed with the amendment as proposed
- **No** — do not proceed; proposal is closed
- **Correction** — specify what to change; Larry creates v02 and Iris reviews again before re-presenting

---

*Prepared: 2026-06-07*
*Delivered on: 2026-06-07*
*Delivered at: 08:33*
