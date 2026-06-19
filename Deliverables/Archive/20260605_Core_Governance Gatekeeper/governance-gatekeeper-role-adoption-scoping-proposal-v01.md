# Governance Gatekeeper / Owner Review Advisor — Role Adoption Scoping Proposal v01

**Status:** Awaiting Owner decision.
**Date:** 2026-06-06
**Prepared by:** Nolan, HR Specialist

---

## 1. Separate role or Larry-invoked practice?

Recommendation: keep it as a Larry-invoked governance practice, not a separate role.

Rationale: the Gatekeeper function is a structured prompt behavior, not a knowledge-intensive domain. It operates on declared session context only, reads nothing, and produces a maximum 5-line output. The entire function is already documented in GL-019 and SOP-019. A separate persona adds overhead (AGENT.md, folder, index entry, hiring flow) for a function that has no domain knowledge requirement and no autonomous judgment. The added structure would exceed the actual need.

If the Owner wishes a named persona for auditability or invocation clarity, that is a valid alternative — see Question 8.

---

## 2. Role purpose (if separate)

If Owner decides a separate persona is warranted:

> The Governance Gatekeeper is a decision compressor that sits at each of four checkpoints in the SOP-018 governance flow. It produces one gate block per checkpoint — maximum five lines — so Larry and the Owner can proceed, redirect, or stop with minimal review time.

---

## 3. Responsibilities (if separate)

- Receive invocation from Larry at CP-1 through CP-4 per SOP-019.
- Check only what is explicitly declared in the active session context.
- Detect the six GL-019 failure modes.
- Produce one gate block per checkpoint — fixed format, maximum 5 lines.
- State "Hard boundary. This block cannot be overridden." when a hard boundary is violated.

---

## 4. Responsibilities that stay with Larry

Regardless of whether a separate persona is created:

- Invoking the Gatekeeper at the correct checkpoint before action proceeds.
- Providing the declared context the Gatekeeper needs per SOP-019 Section 3.
- Surfacing gate blocks to the Owner without modification.
- Recording every invocation in the session log per SOP-019 Section 7.
- Resolving or escalating blocked gates.
- Recording procedural overrides.

---

## 5. Hard boundaries

These apply whether the Gatekeeper is a practice or a persona. None can be overridden by any instruction including Owner instruction:

- No file reads, opens, or filesystem scans of any kind.
- No grep or search operations.
- No Auto-Learning design, Codex evaluation, or automation design.
- No Core AI Team Audit reopening.
- No new agent design or database design.
- No file writes or index updates.

---

## 6. How this role uses GL-019 and SOP-019 without expanding scope

- GL-019 defines allowed checks, forbidden checks, failure modes, gate block format, and hard boundaries. The role executes within that boundary only — it does not interpret, extend, or supplement GL-019.
- SOP-019 defines the exact invocation procedure per checkpoint. The role follows SOP-019 step by step with no additions.
- Any extension to what the Gatekeeper may check requires an Owner-approved revision to GL-019 first — not a change to the role's behavior.

---

## 7. Smallest safe adoption step

If the practice approach (no separate persona) is confirmed: no further action needed. The procedural foundation is live. Larry invokes per CLAUDE.md standing instruction.

If a separate persona is confirmed: Nolan writes a minimal AGENT.md. The Gatekeeper has no domain knowledge requirement (it checks declared state, not a domain). The AGENT.md would contain: identity, responsibilities, Never Does, hard boundaries, collaboration, and a pointer to GL-019 and SOP-019. No Pax brief needed — this is a structured behavior role, not a knowledge domain hire.

Hiring flow if persona is confirmed:
1. Owner confirms persona decision.
2. Nolan writes AGENT.md directly (no Pax brief required — no domain knowledge section needed).
3. Folder created: `Team/[Name] - The Governance Gatekeeper/`
4. `agent-index.md` updated.
5. Smoke test: present a sample checkpoint scenario, verify output matches GL-019 Section 6 format exactly.

---

## 8. Owner approval required before any action

The Owner must decide one of two options before anything is created or assigned:

**Option A — Practice only (recommended)**
The Gatekeeper remains a Larry-invoked structured behavior. No persona, no AGENT.md, no folder. No further action needed.

**Option B — Named persona**
A minimal AGENT.md persona is created. No domain knowledge section. Hiring flow as described in Question 7.

Owner confirmation required: "Option A" or "Option B." No implementation begins before explicit confirmation.

---

*Delivered on: 2026-06-06*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper/governance-gatekeeper-role-adoption-scoping-proposal-v01.md*
