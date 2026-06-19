# Governance Gatekeeper / Owner Review Advisor — Scoping Proposal v01

**Candidate:** A (from `Team Knowledge/Core/Documents/00_START_HERE_myPKA_Governance_and_Auto-Learning_Readiness.md`, Section 5A)
**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-05
**Status:** Scoping only. Awaiting Owner decision.
**Lean Governance Mode:** Active

---

## Status Summary

| Field | Value |
|---|---|
| Core AI Team Audit | Formally closed. No remaining work. |
| Governance Foundation | Fully implemented and accepted (2026-06-05). |
| Candidate A status | Future workstream candidate. Not yet defined. No approval granted. |
| This proposal | Scoping only. No implementation. No file writes. |

---

## 1. Purpose

The Gatekeeper is a structured decision layer that runs before Larry or any specialist proceeds with a governance action. It surfaces the minimum information the Owner needs to approve or redirect: current DP state, route correctness, readiness for the next step, and active red flags.

It does not execute. It does not investigate. It does not produce reports. It produces a single compact block per request.

---

## 2. Responsibilities

- Read the declared current state from the RCP or session context.
- Verify DP sequence continuity (no skipped DPs, no out-of-order execution).
- Confirm Review Gate status (completed, pending, or bypassed with justification).
- Check that required approvals exist before file writes or lifecycle actions proceed.
- Detect the four common failure modes: count mismatch, missing approval, stale path, scope creep.
- Produce a compact gate block: current state / next allowed step / required approval / red flags / exact next prompt.
- Block the session from proceeding if a red flag is active and unresolved.

---

## 3. Non-Responsibilities

- Does not execute any governance step.
- Does not write files, create indexes, or update databases.
- Does not produce audit reports or lifecycle packets.
- Does not replace the Review Gate (SOP-016). It is a pre-check layer, not a review.
- Does not route ideas or classify proposals. That is SOP-018 / Larry's lane.
- Does not design Auto-Learning governance.
- Does not monitor ongoing sessions or run autonomously.

---

## 4. Decision Checkpoints

The Gatekeeper activates at four trigger points:

| Checkpoint | Trigger |
|---|---|
| CP-1: Route check | Before classification is confirmed. Verifies SOP-018 route is correct. |
| CP-2: DP gate | Before any DP step is executed. Confirms previous DP is approved and recorded. |
| CP-3: Review Gate pre-check | Before Review Gate is opened. Confirms RCP is complete and meets entry criteria. |
| CP-4: Lifecycle gate | Before lifecycle execution begins. Confirms DP-5 approved, lifecycle packet present, artifacts counted and matched. |

Each checkpoint produces one compact gate block. If all checks pass: "Gate clear. Proceed to [next step]." If a flag is active: "Gate blocked. [Reason]. Required action: [exact action]."

---

## 5. Token and Inventory Reduction

Current problem: the Owner spends multiple turns verifying route, DP sequence, artifact counts, and approval state. This adds 300 to 800 tokens per governance session in repeated inventories and status confirmations.

Gatekeeper solution:

- Reads declared state, not the filesystem. No directory scans. No grep loops.
- Produces one block per checkpoint, not a running narrative.
- Compresses the Owner's review to: read four lines, confirm or redirect.
- Skips checkpoints that are not relevant to the current action (CP-3 is not invoked during a DP-1 run).

Estimated saving: 40 to 60 percent fewer governance confirmation turns per session.

---

## 6. Failure Mode Handling

**Count mismatch**
Gate block reports: declared count vs. actual count (if verifiable from RCP) and blocks lifecycle execution. Does not investigate. Owner decides: recount, accept, or abort.

**Missing approval**
Gate block reports: which DP or Review Gate approval is missing. Does not proceed. Surfaces exact approval prompt for Owner.

**Stale path**
Gate block reports: path referenced in RCP or proposal does not match canonical paths in GL-004. Surfaces the stale reference and expected current path. Does not correct it. Owner decides.

**Scope creep**
Gate block reports: action proposed in session is outside the declared scope of the current DP or proposal. Names the out-of-scope element. Proposes two options: (a) narrow to declared scope, or (b) park as a new candidate via SOP-018.

**Premature file write**
Gate block reports: file write is requested before DP-4 or DP-5 approval is confirmed. Blocks. Surfaces required approval.

**Recursive cleanup loop**
Gate block reports: a cleanup or archiving action would trigger a second cleanup action on its own artifacts. Names the loop. Recommends: stage one action, close it, then decide on the next independently.

---

## 7. Interaction Model

**Larry and Gatekeeper:**
Larry invokes the Gatekeeper at each checkpoint before briefing a specialist or executing a governance step. The Gatekeeper returns a gate block. Larry reads it, surfaces it to the Owner, and waits. Larry does not proceed past a blocked gate without Owner resolution.

**Owner and Gatekeeper:**
The Owner sees one compact gate block per checkpoint. Four fields: current state, next allowed step, required approval, red flags. One action is required: confirm, redirect, or resolve the flag. No long inventories. No multi-paragraph status reviews.

**Format — gate block:**

```
GATE BLOCK [CP-X: type]
State:    [one line — current DP and approval status]
Next:     [one line — exact next allowed step]
Approval: [one line — what is required from Owner to proceed]
Flags:    [one line per flag, or "None"]
Prompt:   [exact text Owner can use to proceed]
```

---

## 8. Minimum Viable Implementation Scope

A minimum viable Gatekeeper requires:

1. A GL file defining the four checkpoints and the gate block format.
2. An SOP file defining when each checkpoint is invoked, what each check verifies, and how a blocked gate is resolved.
3. A standing instruction in Larry's CLAUDE.md to invoke the Gatekeeper at each checkpoint.
4. No new database tables. No new agents. No automation. Manual invocation only.

That is: one GL, one SOP, one CLAUDE.md addition. Nothing else.

---

## 9. Risks and Safeguards

| Risk | Safeguard |
|---|---|
| Gatekeeper adds process overhead without value | Gate blocks are capped at four lines each. If a checkpoint passes cleanly, the block is one line: "Gate clear. Proceed." |
| Gatekeeper becomes a substitute for Review Gate | Explicit non-responsibility in GL. Gatekeeper checks readiness; Review Gate evaluates quality. |
| Gatekeeper expands scope into Auto-Learning or Codex | Hard boundary in GL: Gatekeeper operates only on active governance flows. Auto-Learning and Codex are out of scope. |
| Gatekeeper blocks legitimate fast-path decisions | Owner can override a gate block with explicit instruction. Override is logged in session record. |
| Larry bypasses Gatekeeper under time pressure | Standing instruction in CLAUDE.md makes invocation mandatory. Pattern is visible in session logs. |

---

## 10. Recommended Next Owner Decision

**Recommendation:** Approve this scoping proposal and authorize one new proposal for the Gatekeeper GL and SOP files, following SOP-015 and SOP-018.

**Rationale:** The Gatekeeper is low-cost to define (one GL, one SOP, one CLAUDE.md addition), directly solves a proven pain point from the SOP-017 amendment flow, and does not require Auto-Learning, Codex, or any new agents or databases.

**What this does not authorize:** Implementation of Auto-Learning, Codex, candidate B, or candidate D.

---

## Next Owner Decision Prompt

**Approve:**
> "Approved. Start een nieuwe SOP-018 classificatie voor de Governance Gatekeeper GL en SOP. Scope: one GL defining checkpoints and gate block format, one SOP defining invocation rules and blocked-gate resolution. Follow SOP-015 and SOP-018. Do not implement Auto-Learning or Codex."

**Redirect:**
> "Not yet. Park this proposal and move to [other work]."

---

*Delivered on: 2026-06-05*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper Scoping Proposal v01/governance-gatekeeper-scoping-proposal-v01.md*
