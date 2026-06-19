# Governance Gatekeeper / Owner Review Advisor — Scoping Proposal v02

**Candidate:** A (from `Team Knowledge/Core/Documents/00_START_HERE_myPKA_Governance_and_Auto-Learning_Readiness.md`, Section 5A)
**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-05
**Status:** Scoping only. Awaiting Owner decision.
**Lean Governance Mode:** Active

---

## Revision Notes (v01 → v02)

| # | Correction applied |
|---|---|
| 1 | Next step reframed: Contract definition first, not implementation approval. |
| 2 | CP-1 corrected: Gatekeeper does not route or classify. Checks stated route and approval status only. |
| 3 | Gate block explicitly capped at 5 lines maximum. |
| 4 | Example scenario added (Section 10). |
| 5 | Hard boundaries section expanded and made explicit. |
| 6 | Section 10 now proposes Contract definition only — no GL, SOP, or CLAUDE.md approval requested. |

---

## Status Summary

| Field | Value |
|---|---|
| Core AI Team Audit | Formally closed. No remaining work. |
| Governance Foundation | Fully implemented and accepted (2026-06-05). |
| Candidate A status | Scoping proposal v02. Awaiting Owner decision on Contract definition. |
| This proposal | Scoping only. No implementation. No file writes. |

---

## 1. Purpose

The Gatekeeper is a decision compressor. It sits between a declared governance intent and the execution of that intent. Its only job is to produce a compact gate block that gives the Owner or Larry exactly the information needed to proceed, redirect, or stop — in five lines or fewer.

It does not govern. It does not execute. It does not produce reports or recommendations. It produces one gate block per checkpoint.

---

## 2. Responsibilities

- Read the declared current state from the RCP or active session context.
- Verify DP sequence continuity: no skipped DPs, no out-of-order execution.
- Confirm Review Gate status: completed, pending, or bypassed with stated justification.
- Check that required approvals exist before file writes or lifecycle actions are initiated.
- Detect active failure modes: count mismatch, missing approval, stale path, scope creep, premature file write, recursive cleanup loop.
- Produce a gate block of maximum 5 lines.
- Block the session from proceeding when a red flag is active and unresolved.

---

## 3. Non-Responsibilities

- Does not execute any governance step.
- Does not write files, create indexes, or update databases.
- Does not produce audit reports or lifecycle packets.
- Does not replace the Review Gate (SOP-016). It is a pre-check layer only.
- Does not route or classify ideas. Routing and classification belong to SOP-018 and Larry.
- Does not scan the filesystem or run grep loops.
- Does not reopen Core AI Team Audit items.
- Does not design Auto-Learning governance or auto-detection flows.
- Does not evaluate Codex or any autonomous execution tooling.
- Does not design new agents or new database tables.
- Does not monitor sessions autonomously or run without explicit invocation.

---

## 4. Decision Checkpoints

Four checkpoints. Each produces one gate block. Only the checkpoints relevant to the current action are invoked.

| Checkpoint | Trigger | What is checked |
|---|---|---|
| CP-1: Route check | Before any DP step begins. | Whether Larry has explicitly stated a SOP-018 route. Whether that route has recorded Owner approval. Whether any red flag blocks proceeding. Gatekeeper does not route or classify. |
| CP-2: DP gate | Before each DP step is executed. | Whether the previous DP is recorded as approved. Whether the sequence is continuous. Whether any blocking flag exists. |
| CP-3: Review Gate pre-check | Before Review Gate is opened. | Whether the RCP is present and complete. Whether it meets the stated entry criteria. Whether any blocking flag exists. |
| CP-4: Lifecycle gate | Before lifecycle execution begins. | Whether DP-5 is approved and recorded. Whether the lifecycle packet is present. Whether declared artifact count matches the packet. Whether any blocking flag exists. |

---

## 5. Token and Inventory Reduction

The direct cost of manual verification in governance sessions is repeated multi-turn status checks: route correct? approvals in place? artifact counts matching? Each cycle adds 300 to 800 tokens and fragments the Owner's attention.

The Gatekeeper eliminates this by:

- Reading declared state only. No filesystem scans. No directory listings. No grep loops.
- Producing one gate block per checkpoint, not a running narrative.
- Capping gate block output at 5 lines regardless of complexity.
- Omitting checkpoints that are not relevant to the active step.

If a checkpoint passes cleanly, the entire block is one line: `Gate clear. Proceed to [next step].`

---

## 6. Failure Mode Handling

**Count mismatch**
Gates CP-4. Reports: declared count and observed discrepancy. Does not investigate. Owner decides: recount, accept variance, or abort.

**Missing approval**
Gates CP-2, CP-3, CP-4. Reports: which DP or Review Gate approval is absent. Surfaces the exact approval prompt. Does not proceed.

**Stale path**
Gates any checkpoint where a path reference is checked. Reports: the stale path as stated in the RCP or proposal, and the current canonical path per GL-004. Does not correct. Owner decides.

**Scope creep**
Gates any checkpoint. Reports: the out-of-scope element. Names it. Proposes two options inline: (a) narrow to declared scope, or (b) park via SOP-018.

**Premature file write**
Gates CP-2 and CP-4. Reports: file write requested before required approval is confirmed. Blocks. Surfaces required approval.

**Recursive cleanup loop**
Gates CP-4. Reports: a cleanup action that would trigger a second cleanup action on its own artifacts. Names the loop. Recommends staging one action, closing it, then deciding on the next independently.

---

## 7. Interaction Model

**Larry and Gatekeeper:**
Larry invokes the Gatekeeper at each relevant checkpoint before briefing a specialist or initiating a governance action. The Gatekeeper returns a gate block. Larry surfaces it to the Owner. Larry does not proceed past a blocked gate without Owner resolution.

**Owner and Gatekeeper:**
The Owner sees one gate block per checkpoint. Maximum 5 lines. One required action: confirm, redirect, or resolve the flag. No inventories. No status narratives.

**Owner override:**
The Owner may override a blocked gate with an explicit instruction. The override is recorded in the session log. The Gatekeeper does not argue with an explicit Owner instruction.

---

## 8. Gate Block Format

Fixed format. Maximum 5 lines. No prose outside these fields.

```
GATE BLOCK [CP-X: label]
State:    [one line — current DP and approval status]
Next:     [one line — exact next allowed step]
Approval: [one line — what Owner must confirm to proceed]
Flags:    [one line per active flag, or "None"]
Prompt:   [exact text Owner can use to proceed or resolve]
```

Clean pass (no flags):

```
GATE BLOCK [CP-2: DP gate] — Gate clear. Proceed to DP-3.
```

---

## 9. Minimum Viable Definition Scope

Before any implementation can be proposed, the Gatekeeper needs a Contract. The Contract is a single short document that defines:

- When the Gatekeeper is invoked (which triggers, which checkpoints)
- What it may check (declared state, approval records, RCP completeness, artifact counts)
- What it must not check (filesystem, live grep, classification logic)
- The exact gate block format (see Section 8)
- The maximum output length (5 lines)
- How Owner approval is requested (Prompt field only — no inline requests)

The Contract is not a GL file. It is not a SOP. It is a definition document used to validate the design before any governance files are written. Implementation (GL, SOP, CLAUDE.md addition) is a separate step that requires a new proposal after the Contract is accepted.

---

## 10. Example Scenario

**Scenario:** A normal governance proposal is ready and Larry is about to proceed to DP-3 (Owner approval for implementation).

**Active context:** SOP-017 amendment. Route confirmed as SOP-018 track 2. DP-1 and DP-2 approved and recorded. RCP v03 accepted. Review Gate completed with no blocking findings.

**Gatekeeper invocation:** CP-2 before DP-3 execution.

```
GATE BLOCK [CP-2: DP gate]
State:    SOP-017 amendment — DP-1 approved, DP-2 approved, Review Gate completed (no blocking findings).
Next:     DP-3 — Owner approval for implementation.
Approval: Owner confirms: "Approved. Proceed to DP-3."
Flags:    None
Prompt:   "Approved. Proceed to DP-3 for the SOP-017 amendment."
```

The Owner reads four lines. Confirms or redirects. One turn.

---

## 11. Risks and Safeguards

| Risk | Safeguard |
|---|---|
| Gatekeeper adds overhead without value | Gate blocks capped at 5 lines. Clean passes reduce to one line. |
| Gatekeeper scope expands into Review Gate territory | Explicit non-responsibility in Contract: Gatekeeper checks readiness, not quality. |
| Gatekeeper is bypassed under time pressure | Standing invocation rule in Contract. Pattern visible in session logs. |
| Owner override creates untracked exceptions | Override recorded in session log. Not blocked — just logged. |
| Contract definition drifts into SOP-level detail | Contract is a definition document only. GL and SOP are the next step, after Contract acceptance. |

---

## 12. Hard Boundaries (Non-Negotiable)

These boundaries apply to the Gatekeeper in all future states, not only during scoping:

- No Core AI Team Audit reopening.
- No Codex work or evaluation.
- No Auto-Learning implementation or design.
- No auto-detection or auto-processing design.
- No file writes.
- No filesystem scans or directory listings.
- No grep loops.
- No recursive cleanup loops.
- No new agent design.
- No new database table design.

---

## 13. Recommended Next Owner Decision

This proposal is scoping only. It does not request approval for a GL file, a SOP file, or a CLAUDE.md change.

The single next step this proposal proposes is: define the Gatekeeper Contract.

**Contract definition is a short, standalone document.** It can be drafted in one session. It requires no implementation. It produces no governance files. Once accepted, it becomes the basis for a separate implementation proposal.

**Decision prompt — approve Contract definition:**
> "Akkoord met v02. Start de Gatekeeper Contract definitie. Scoping only. Geen implementatie, geen GL, geen SOP, geen CLAUDE.md wijziging."

**Decision prompt — redirect or park:**
> "V02 geaccepteerd als richting. Parkeer voor nu. We pakken dit op na [ander werk]."

---

*Delivered on: 2026-06-05*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper Scoping Proposal v02/governance-gatekeeper-scoping-proposal-v02.md*
