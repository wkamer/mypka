# SOP-019 — Governance Gatekeeper Procedure

**Type:** Standard Operating Procedure
**Maintainer:** Larry, Team Orchestrator
**Created:** 2026-06-06
**Status:** Live
**Basis:** GL-019 — Governance Gatekeeper Principles; Governance Gatekeeper Contract v02 (accepted 2026-06-05)

---

## 1. Purpose

This SOP defines the step-by-step procedure for Larry to invoke the Governance Gatekeeper at each of the four checkpoints before a governance action proceeds.

For principles, gate block format, allowed checks, forbidden checks, failure modes, and hard boundaries: see `[[GL-019_Governance Gatekeeper Principles]]`.

---

## 2. Context Constraint (Mandatory)

The Gatekeeper operates exclusively on information explicitly provided in the active session context.

This means:

- RCP information may only be used when explicitly stated in the active session context. The Gatekeeper must not open, read, search, scan, or verify the RCP file itself.
- Lifecycle packet information may only be used when explicitly stated in the active session context. The Gatekeeper must not open, read, search, scan, or verify any lifecycle packet file.
- Canonical path information (GL-004) may only be used when both the referenced path and the expected canonical path are explicitly stated in the active session context. The Gatekeeper must not open GL-004 or any other file to verify paths.
- No folder, file, index, or database may be opened, read, or searched to perform any check.

If required information is absent from the active session context, the Gatekeeper raises a missing required declared context flag, blocks the gate, and states what context must be provided. The Gatekeeper does not investigate to find the missing information.

Every flag raised by this SOP maps to one of the six GL-019 Section 5 failure modes (count mismatch, missing approval, stale path, scope creep, premature file write, recursive cleanup loop) or to missing required declared context. This SOP introduces no additional failure modes.

---

## 3. Invocation Procedure

Larry invokes the Gatekeeper before the corresponding action begins. The Gatekeeper is not invoked after the fact.

**Pace Independence Rule:** CP invocation is independent of session pace and instruction source. Larry invokes CP-1 before any DP step begins, CP-2 before each DP step is executed, CP-3 before the Review Gate is opened, and CP-4 before lifecycle execution begins — regardless of whether the Owner is driving the session interactively, directing steps in sequence, or explicitly instructing Larry to proceed. Owner-directed pace does not exempt Larry from any of these invocations. The Owner may issue a procedural override after invocation (see Section 5), but the invocation itself is never skipped.

### CP-1: Route Check

**Invoke before:** any DP step begins.

**Larry provides:**
- The stated SOP-018 route for the active proposal.
- Whether Owner approval for that route is recorded.

**Gatekeeper checks:**
1. Is a SOP-018 route explicitly stated? If not: flag — missing required declared context (route not stated).
2. Does the stated route have recorded Owner approval? If not: flag — missing approval.
3. Is any other red flag active that blocks proceeding?

**Output:** gate block per GL-019 Section 6.

---

### CP-2: DP Gate

**Invoke before:** each DP step is executed.

**Larry provides:**
- The current DP being requested.
- The recorded approval status of the previous DP.

**Gatekeeper checks:**
1. Is the previous DP recorded as approved? If not: flag — missing approval.
2. Is the DP sequence continuous (no skipped steps)? If not: flag — missing approval (sequence gap — skipped DP has no recorded approval).
3. Is any other blocking flag active?

**Output:** gate block per GL-019 Section 6.

---

### CP-3: Review Gate Pre-Check

**Invoke before:** the Review Gate is opened.

**Larry provides:**
- Whether the RCP is declared present and complete in the active session context.
- The stated entry criteria for the Review Gate.

**Gatekeeper checks:**
1. Is the RCP declared present and complete? If not: flag — missing required declared context (RCP not declared complete).
2. Does the declared RCP content meet the stated entry criteria? If not: flag — missing required declared context (declared RCP content does not meet stated entry criteria).
3. Is any other blocking flag active?

**Output:** gate block per GL-019 Section 6.

---

### CP-4: Lifecycle Gate

**Invoke before:** lifecycle execution begins.

**Larry provides:**
- Whether DP-5 is recorded as approved.
- Whether the lifecycle packet is declared present in the active session context.
- The declared artifact count from the lifecycle packet.

**Gatekeeper checks:**
1. Is DP-5 recorded as approved? If not: flag — missing DP-5 approval.
2. Is the lifecycle packet declared present? If not: flag — missing required declared context (lifecycle packet not declared).
3. Are both the expected artifact count and the actual artifact count explicitly declared in the active session context? If only one count is declared: flag — missing required declared context. If both are declared and they do not match: flag — count mismatch.
4. Is any other blocking flag active?

**Output:** gate block per GL-019 Section 6.

---

## 4. Blocked Gate Handling

When the gate is blocked:

1. The Gatekeeper produces a full 5-line gate block (per GL-019 Section 6).
2. Larry surfaces the gate block to the Owner without modification.
3. Larry does not proceed past the blocked gate.
4. The Owner resolves the flag or issues a procedural override (see Section 5).
5. After resolution, Larry re-invokes the Gatekeeper at the same checkpoint before proceeding.
6. The Gatekeeper does not re-check without a new invocation.

---

## 5. Procedural Override Handling

The Owner may override a procedural gate block with an explicit instruction.

Procedural overrides apply to: missing sequence confirmation, timing friction, non-critical ordering issues, and similar procedural concerns that do not touch hard boundaries.

When a procedural override is issued:
1. The Gatekeeper acknowledges and clears the procedural block.
2. Larry records the override in the session log: date, checkpoint, flag overridden, Owner instruction text.
3. Larry proceeds to the next step.
4. The override applies to that gate instance only. It does not carry forward.

---

## 6. Hard Boundary Handling

Hard boundaries cannot be overridden by any instruction, including explicit Owner instruction.

When a blocked gate is caused by a hard boundary violation:

1. The Gatekeeper states: "Hard boundary. This block cannot be overridden."
2. Larry does not proceed.
3. Larry surfaces the hard boundary block to the Owner.
4. No further action is taken until the underlying violation is resolved.

For the full list of hard boundaries: see GL-019 Section 4 and Section 7.

---

## 7. Session Log Recording

Larry records the following in the session log for every Gatekeeper invocation:

- Checkpoint invoked (CP-1 through CP-4).
- Gate result: clear or blocked.
- Flags raised (if any).
- Whether a procedural override was issued and by whom.
- Whether a hard boundary block was encountered.

---

## 8. Track Artifact Placement

Artifacts produced during a SOP-019 track (initiation proposals, Iris review reports,
execution reports, correction notes) are files inside the track's primary deliverable
folder, not standalone deliverable folders.

The track's primary deliverable folder is the folder that represents the output the
track was opened to produce or amend. If no primary deliverable folder exists for the
track at initiation, create one at that point.

File placement within the track folder:
- Initiation proposal: `initiation-proposal-v01.md` (and v02, v03 as iterations)
- Iris review report: `review-[track-description]-v01.md`
- Execution report: `er-[track-description]-v01.md`
- Correction note: `correction-note-v01.md`

Exception: if the track produces a new primary deliverable (a new GL, SOP, or
AGENT.md) that will be independently cited, that output is a new folder in its own
right per GL-017 Section 2.1. The initiation proposal and execution report for the
track remain as files inside the track's deliverable folder, not inside the new GL/SOP
folder.

---

*Created: 2026-06-06*
*Last modified: 2026-06-08 — Track Artifact Placement rule added as Section 8 (DL Granularity Rules)*
