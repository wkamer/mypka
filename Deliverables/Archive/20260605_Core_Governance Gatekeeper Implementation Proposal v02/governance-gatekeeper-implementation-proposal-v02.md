# Governance Gatekeeper / Owner Review Advisor — Implementation Proposal v02

**Type:** Implementation proposal. Not an implementation.
**Basis:** Contract v02, accepted 2026-06-05, plus acceptance note.
**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-05
**Status:** Awaiting Owner approval.
**Lean Governance Mode:** Active

---

## Revision Notes (v01 → v02)

| # | Correction applied |
|---|---|
| 1 | Pre-implementation number check added as a mandatory first step before any file write. |
| 2 | Auto-selection of alternate numbers removed. Conflict stops implementation and returns to Owner. |
| 3 | Approval text updated: authorization is conditional on confirmed number availability. |
| 4 | Rollback corrected: newly created Core governance files are removed or reverted in place. They are not moved to Deliverables/Archive. |
| 5 | Scope unchanged: one GL, one SOP, one CLAUDE.md addition, nothing else. |

---

## Basis

This proposal is grounded in the accepted Contract v02 and the following acceptance note:

> Where the Contract refers to the active RCP, the Gatekeeper may only use RCP information that is explicitly provided in the active session context. The Gatekeeper must not open, read, search, scan, or verify the RCP file itself.

This acceptance note is incorporated into the scope of all three proposed artefacts.

---

## Proposed Artefacts

Three artefacts. Nothing is created until Owner approval is granted and the pre-implementation number check passes.

| # | Type | Proposed file name | Location |
|---|---|---|---|
| 1 | GL file | `GL-019_Governance Gatekeeper Principles.md` | `Team Knowledge/Core/Guidelines/` |
| 2 | SOP file | `SOP-019_Governance Gatekeeper Procedure.md` | `Team Knowledge/Core/SOPs/` |
| 3 | CLAUDE.md addition | Standing instruction block | `CLAUDE.md` — Larry's operational conventions section |

---

## Pre-Implementation Number Check (Mandatory)

Before any file write begins, Larry must confirm that GL-019 and SOP-019 are both available.

**Check procedure:**
1. Confirm no file named `GL-019_*.md` exists in `Team Knowledge/Core/Guidelines/`.
2. Confirm no file named `SOP-019_*.md` exists in `Team Knowledge/Core/SOPs/`.

**If both numbers are available:** Implementation proceeds per the approved proposal.

**If either number is unavailable:** Implementation stops immediately. Larry returns to Owner with a report of the conflict and a corrected proposal or explicit re-approval request. Larry may not silently use GL-020, SOP-020, or any other number. A number change requires a new Owner approval.

---

## Artefact 1 — GL-019: Governance Gatekeeper Principles

**File target:** `Team Knowledge/Core/Guidelines/GL-019_Governance Gatekeeper Principles.md`

**Scope:**
- Definition of the Gatekeeper role and its purpose as a decision compressor.
- The four checkpoints (CP-1 through CP-4) and their invocation triggers.
- The complete list of allowed checks.
- The complete list of forbidden checks, including hard boundaries.
- The gate block format and 5-line maximum cap.
- The Flags field compression rule.
- Hard boundary list with the explicit statement that these cannot be overridden.
- The acceptance note: Gatekeeper reads only RCP information explicitly provided in the active session context. No file reads.

**This GL does not contain:**
- Invocation procedure (SOP-019 scope).
- Larry-specific behavioural instructions (CLAUDE.md addition scope).

---

## Artefact 2 — SOP-019: Governance Gatekeeper Procedure

**File target:** `Team Knowledge/Core/SOPs/SOP-019_Governance Gatekeeper Procedure.md`

**Scope:**
- Step-by-step procedure for Larry to invoke the Gatekeeper at each checkpoint.
- How to surface a gate block to the Owner.
- How a blocked gate is resolved: Owner resolves the flag, or issues a procedural override.
- How a procedural override is recorded in the session log.
- How a hard boundary block is communicated: "Hard boundary. This block cannot be overridden."
- Re-invocation rule: Larry re-invokes at the same checkpoint after a flag is resolved.
- Reference to GL-019 for principles, format, and hard boundaries.
- Reference to Contract v02 as the accepted design basis.

**This SOP does not contain:**
- Principles or format definitions (GL-019 scope).
- Auto-Learning flows, Codex evaluation, or audit procedures.

---

## Artefact 3 — CLAUDE.md Standing Instruction

**Target location:** `CLAUDE.md` — Larry's operational conventions section, under a new subsection: `### Governance Gatekeeper`

**Exact instruction to be added:**

```
### Governance Gatekeeper

Before executing any DP step, opening the Review Gate, or initiating lifecycle execution:
invoke the Gatekeeper at the relevant checkpoint (CP-1 through CP-4) per SOP-019.
Do not proceed past a blocked gate without Owner resolution.
Hard boundaries may not be overridden. Procedural gates may be overridden by explicit Owner instruction.
Record all overrides in the session log.
```

**This addition does not change any other section of CLAUDE.md.**

---

## Non-Goals

This implementation does not:

- Define Auto-Learning detection or processing flows.
- Design new agents or new database tables.
- Modify any existing GL or SOP other than adding the two new files.
- Reopen Core AI Team Audit items.
- Implement Codex evaluation.
- Add automation, hooks, or scheduled processes.
- Touch any file outside the three artefacts listed above.

---

## Approval Required

Owner approval authorizes implementation only if both GL-019 and SOP-019 are confirmed available by the pre-implementation number check. If either number is unavailable, the approval does not authorize implementation under alternate numbering. Larry stops and returns to Owner.

**Proposed approval text:**

> "Approved. Voer de pre-implementatie nummercheck uit. Als GL-019 en SOP-019 beide beschikbaar zijn, implementeer dan GL-019, SOP-019, en de CLAUDE.md toevoeging voor de Governance Gatekeeper per implementatievoorstel v02. Als een van beide nummers bezet is, stop dan en keer terug met een gecorrigeerd voorstel."

Implementation follows SOP-015 (Proposal Iteration Protocol) and SOP-017 (Deliverable Lifecycle). Each artefact is written, read back, and confirmed before the next is started.

---

## Risk Controls

| Risk | Control |
|---|---|
| GL or SOP number conflict | Pre-implementation check before any write. Conflict stops implementation and returns to Owner. No silent re-numbering. |
| GL or SOP scope drifts beyond Contract v02 | Each artefact is read back to Owner after writing. Any deviation flagged before proceeding. |
| CLAUDE.md addition breaks existing behavioural rules | New subsection only. No existing text modified. Read back before confirming. |
| Hard boundary list in GL-019 diverges from Contract v02 | Hard boundary list copied verbatim from Contract v02 Sections 3 and 7. No paraphrasing. |

---

## Rollback Approach

**Partial or full rollback of GL-019 or SOP-019:**
Remove the created file from its Core governance location (`Team Knowledge/Core/Guidelines/` or `Team Knowledge/Core/SOPs/`). Do not move these files to Deliverables/Archive. Core governance files that have not been accepted do not belong in Archive.

**Rollback of CLAUDE.md addition:**
Remove the exact `### Governance Gatekeeper` block that was added. Leave the rest of CLAUDE.md unchanged. No other edits.

**Order of rollback:**
Reverse the order of implementation: CLAUDE.md addition first, then SOP-019, then GL-019.

---

## Owner Decision Prompt

**Approve and proceed:**
> "Approved. Voer de pre-implementatie nummercheck uit. Als GL-019 en SOP-019 beide beschikbaar zijn, implementeer dan GL-019, SOP-019, en de CLAUDE.md toevoeging voor de Governance Gatekeeper per implementatievoorstel v02. Als een van beide nummers bezet is, stop dan en keer terug met een gecorrigeerd voorstel."

**Redirect or park:**
> "Voorstel v02 geaccepteerd als richting. Parkeer voor nu."

---

*Delivered on: 2026-06-05*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper Implementation Proposal v02/governance-gatekeeper-implementation-proposal-v02.md*
