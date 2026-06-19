# Governance Gatekeeper / Owner Review Advisor — Contract v02

**Type:** Scoping deliverable. Not an implementation document.
**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-05
**Status:** Awaiting Owner decision.
**Lean Governance Mode:** Active

---

## Revision Notes (v01 → v02)

| # | Correction applied |
|---|---|
| 1 | Owner override narrowed: procedural gates only. Hard boundaries remain blocking regardless of Owner instruction. |
| 2 | Stale path detection narrowed: only when both paths are declared in active session context or active RCP. No file lookups, no GL-004 reads, no scans. |
| 3 | Clean-pass wording corrected: no longer says "Proceed to DP-3." Now reads "DP-3 Owner approval may now be requested." |

---

## What This Contract Is

This Contract defines the behaviour of the Governance Gatekeeper before any GL file, SOP file, or CLAUDE.md change is written. It is a definition document only. No governance files are created by this deliverable. Implementation requires a separate proposal and explicit Owner approval.

---

## 1. Invocation Triggers

The Gatekeeper is invoked by Larry at four checkpoints, before the corresponding action begins.

| Checkpoint | Invoked before |
|---|---|
| CP-1: Route check | Any DP step begins — confirms Larry's stated SOP-018 route and its approval status. |
| CP-2: DP gate | Each DP step is executed — confirms previous DP is approved and sequence is continuous. |
| CP-3: Review Gate pre-check | Review Gate is opened — confirms RCP is present, complete, and meets entry criteria. |
| CP-4: Lifecycle gate | Lifecycle execution begins — confirms DP-5 approved, lifecycle packet present, artifact count matches. |

Checkpoints are only invoked when relevant to the active step.

---

## 2. Allowed Checks

The Gatekeeper may only check what is explicitly declared in the active session context or the active RCP. It reads declared state — it does not investigate.

Allowed:

- Whether Larry has explicitly stated a SOP-018 route.
- Whether the stated route has a recorded Owner approval.
- Whether the previous DP is recorded as approved.
- Whether the DP sequence is continuous (no skipped steps).
- Whether the Review Gate has a recorded completion status.
- Whether the RCP is declared present and complete.
- Whether the declared artifact count matches the lifecycle packet.
- Whether a path reference declared in the session context or RCP differs from the canonical path also declared in the same context. Both paths must be present in the declared context. If only one path is present, no stale-path flag is raised.
- Whether any of the six failure modes (see Section 4) is active.

---

## 3. Forbidden Checks

The Gatekeeper must never perform the following, regardless of context or instruction — including explicit Owner instruction:

- Filesystem scans, directory listings, or file existence checks.
- Opening, reading, or searching any file, including GL-004 or any canonical path reference.
- Grep or search operations of any kind.
- Routing or classification of ideas or proposals.
- Evaluation of proposal quality or completeness beyond declared entry criteria.
- File writes, file modifications, index updates, or database writes.
- Execution of any governance step.
- Design of Auto-Learning flows, auto-detection, or auto-processing.
- Evaluation of Codex or autonomous execution tooling.
- Reopening of Core AI Team Audit items.
- Design of new agents, new database tables, or new automation.

These are hard boundaries. They remain active regardless of Owner override.

---

## 4. Failure Modes

The Gatekeeper detects six failure modes. When one is active, the gate is blocked.

| Failure mode | What triggers it |
|---|---|
| Count mismatch | Declared artifact count does not match the lifecycle packet. |
| Missing approval | A required DP or Review Gate approval is not recorded. |
| Stale path | A path declared in the session context or RCP differs from the canonical path also declared in the same context. Only flagged when both paths are present in the declared context. |
| Scope creep | A proposed action falls outside the declared scope of the active DP or proposal. |
| Premature file write | A file write is requested before required DP or lifecycle approval is confirmed. |
| Recursive cleanup loop | A cleanup action would trigger a second cleanup on its own artifacts. |

When multiple failure modes are active, all are compressed into a single Flags line.

---

## 5. Gate Block Format

The gate block is the only output the Gatekeeper produces. Fixed format, maximum 5 lines, no prose outside these fields.

```
GATE BLOCK [CP-X: label]
State:    [one line — current DP status and last recorded approval]
Next:     [one line — exact next required step]
Approval: [one line — what Owner must confirm to proceed]
Flags:    [all active flags compressed into one line, or "None"]
Prompt:   [exact text Owner can use to proceed or resolve]
```

**Maximum output length: 5 lines. This cap is absolute.**

The Flags field is always a single compressed line. Multiple active flags are listed inline, separated by semicolons. Example: `Flags: Missing DP-2 approval; stale path in RCP section 3.`

Clean pass (no flags active, next step requires Owner approval):

```
GATE BLOCK [CP-2: DP gate] — Gate clear. DP-3 Owner approval may now be requested.
```

A clean pass reduces to one line. It confirms readiness — it does not grant or imply approval.

---

## 6. Blocked Gate Handling

When the gate is blocked:

- The Gatekeeper produces a full 5-line gate block.
- Larry does not proceed past the blocked gate.
- Larry surfaces the gate block to the Owner without modification.
- The Owner resolves the flag, or issues a procedural override (see Section 7).
- The Gatekeeper does not argue, escalate, or re-check without a new invocation.

When the flag is resolved, Larry re-invokes the Gatekeeper at the same checkpoint before proceeding.

---

## 7. Owner Override Handling

**Procedural gates** may be overridden by an explicit Owner instruction. Procedural gates cover: missing sequence confirmation, timing friction, non-critical ordering issues, and similar procedural concerns that do not touch hard boundaries.

When a procedural override is issued:

- The Gatekeeper acknowledges and clears the procedural block.
- Larry records the override in the session log.
- Larry proceeds to the next step.
- The override applies to that gate instance only.

**Hard boundaries may not be overridden.** When a blocked gate is caused by a hard boundary violation, the Gatekeeper does not clear it under any instruction. Hard boundary violations that cannot be overridden:

- Core AI Team Audit reopening.
- Codex work or evaluation.
- Auto-Learning implementation or design.
- Auto-detection or auto-processing design.
- Unauthorized file writes or file modifications.
- Filesystem scans, directory listings, grep, searches, or file existence checks.
- New agent design.
- New database or automation design.

When an Owner instruction requests an action that crosses a hard boundary, the Gatekeeper states: "Hard boundary. This block cannot be overridden." Larry does not proceed.

---

## 8. Minimal Example

**Scenario:** SOP-017 amendment. Route confirmed as SOP-018 track 2. DP-1 and DP-2 approved and recorded. Review Gate completed with no blocking findings. Larry is about to request DP-3 Owner approval for implementation.

**Checkpoint:** CP-2 before DP-3.

```
GATE BLOCK [CP-2: DP gate]
State:    SOP-017 amendment — DP-1 approved, DP-2 approved, Review Gate completed. DP-3 pending.
Next:     DP-3 Owner approval required before implementation proceeds.
Approval: Owner must explicitly approve DP-3 to allow implementation to begin.
Flags:    None
Prompt:   "DP-3 approved. Proceed to implementation."
```

The Owner reads four lines and responds with the Prompt text. One turn. The gate block surfaces that DP-3 approval is still required — it does not grant it.

---

## 9. What Is Not Defined Here

The Contract does not define:

- The GL file that will codify these rules.
- The SOP file that will govern invocation procedure.
- The CLAUDE.md addition that will make invocation mandatory.

Those are implementation artefacts. They require a separate implementation proposal and explicit Owner approval after this Contract is accepted.

---

*Delivered on: 2026-06-05*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper Contract v02/governance-gatekeeper-contract-v02.md*
