# Governance Gatekeeper / Owner Review Advisor — Implementation Proposal v01

**Type:** Implementation proposal. Not an implementation.
**Basis:** Contract v02, accepted 2026-06-05, plus acceptance note.
**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-05
**Status:** Awaiting Owner approval.
**Lean Governance Mode:** Active

---

## Basis

This proposal is grounded in the accepted Contract v02 and the following acceptance note:

> Where the Contract refers to the active RCP, the Gatekeeper may only use RCP information that is explicitly provided in the active session context. The Gatekeeper must not open, read, search, scan, or verify the RCP file itself.

This acceptance note is incorporated into the scope of all three proposed artefacts below.

---

## Proposed Artefacts

Three artefacts. Nothing is created until each receives explicit Owner approval.

| # | Type | Proposed file name | Location |
|---|---|---|---|
| 1 | GL file | `GL-019_Governance Gatekeeper Principles.md` | `Team Knowledge/Core/Guidelines/` |
| 2 | SOP file | `SOP-019_Governance Gatekeeper Procedure.md` | `Team Knowledge/Core/SOPs/` |
| 3 | CLAUDE.md addition | Standing instruction block | `CLAUDE.md` — Larry's operational conventions section |

GL-019 and SOP-019 numbers are based on the known last-used numbers GL-018 and SOP-018. Exact numbers to be confirmed at implementation time.

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
- Invocation procedure (that is SOP-019's scope).
- Larry-specific behavioural instructions (that is the CLAUDE.md addition's scope).

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
- Principles or format definitions (those are GL-019's scope).
- Auto-Learning flows, Codex evaluation, or audit procedures.

---

## Artefact 3 — CLAUDE.md Standing Instruction

**Target location:** `CLAUDE.md` — Larry's operational conventions section, under a new subsection: `### Governance Gatekeeper`

**Scope — exact instruction to be added:**

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
- Modify any existing GL, SOP, or guideline other than adding the new files.
- Reopen Core AI Team Audit items.
- Implement Codex evaluation.
- Add automation, hooks, or scheduled processes.
- Touch any file outside the three artefacts listed above.

---

## Approval Required

All three artefacts require a single explicit Owner approval before implementation begins. Proposed approval text:

> "Approved. Implementeer GL-019, SOP-019, en de CLAUDE.md toevoeging voor de Governance Gatekeeper per implementatievoorstel v01."

Implementation follows SOP-015 (Proposal Iteration Protocol) and SOP-017 (Deliverable Lifecycle). Each artefact is written, read back, and confirmed before the next is started.

---

## Risk Controls

| Risk | Control |
|---|---|
| GL or SOP scope drifts beyond Contract v02 | Each artefact is read back to Owner after writing. Any deviation from the Contract is flagged before proceeding to the next artefact. |
| CLAUDE.md addition breaks existing behavioural rules | The addition is a new subsection only. No existing text is modified. Read back before confirming. |
| GL-019 or SOP-019 number conflicts with an existing file | Numbers confirmed at implementation time before writing. If a conflict exists, next available number is used and reported to Owner. |
| Hard boundary list in GL-019 diverges from Contract v02 | GL-019 hard boundary list is copied verbatim from Contract v02 Section 3 and Section 7. No paraphrasing. |

---

## Rollback Approach

If any artefact is found to be incorrect after writing:

- The file is corrected via a revision, following SOP-015.
- The CLAUDE.md addition is edited to match the corrected GL-019 reference if needed.
- No other files are touched.

If the implementation is rejected in full after partial execution:

- Written files are moved to `Deliverables/Archive/` as inactive artefacts.
- The CLAUDE.md addition, if already written, is removed.
- No other cleanup is required. No audit trail is lost.

---

## Owner Decision Prompt

**Approve and proceed to implementation:**
> "Approved. Implementeer GL-019, SOP-019, en de CLAUDE.md toevoeging voor de Governance Gatekeeper per implementatievoorstel v01."

**Redirect or park:**
> "Voorstel v01 geaccepteerd als richting. Parkeer voor nu."

---

*Delivered on: 2026-06-05*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper Implementation Proposal v01/governance-gatekeeper-implementation-proposal-v01.md*
