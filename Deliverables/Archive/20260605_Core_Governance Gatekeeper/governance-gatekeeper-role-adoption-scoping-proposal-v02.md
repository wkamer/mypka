# Governance Gatekeeper / Owner Review Advisor — Role Adoption Scoping Proposal v02

**Status:** Awaiting Owner decision.
**Date:** 2026-06-06
**Prepared by:** Nolan, HR Specialist

---

## Revision Notes (v01 to v02)

- v01 defaulted to "practice only" as the recommendation without fairly presenting the alternatives. v02 presents all three options with equal weight.
- v01 compressed Options B and C into a single "Named persona" option. v02 separates them: a lightweight Gatekeeper persona (B) is distinct from an Owner Review Advisor role (C).
- v01 stated "no Pax brief required" without explanation. v02 addresses the Pax brief question explicitly per option, with reasoning.
- v01 described immediate AGENT.md creation after Owner choice. v02 corrects this: persona creation requires a separate implementation proposal and explicit Owner approval before any file is created.
- v01 did not include Overhead, Risk of governance bloat, or Smallest safe next step as separate fields per option. v02 adds all required fields.

---

## Procedural foundation (already live)

- GL-019 — Governance Gatekeeper Principles (Live)
- SOP-019 — Governance Gatekeeper Procedure (Live)
- CLAUDE.md standing instruction (Live)

All three options build on this foundation. None require changes to GL-019, SOP-019, or CLAUDE.md.

---

## Option A — Practice only

**Purpose**
The Governance Gatekeeper function runs as a structured behavior invoked by Larry. No persona, no separate agent.

**Responsibilities**
Larry invokes the Gatekeeper per CLAUDE.md, SOP-019, and GL-019 at CP-1 through CP-4. Larry produces the gate block as part of his orchestration role.

**What stays with Larry**
Everything. Invocation, context provision, gate block production, session log recording, blocked gate handling, and procedural override recording.

**Pros**
- Zero overhead to implement — foundation is already live.
- No additional agent maintenance, no AGENT.md, no index entry.
- Simpler session context: one agent owns the full governance thread.

**Cons**
- Larry is both the orchestrator and the gatekeeper in the same session. Self-checking has inherent blind spots.
- No independent voice to detect when Larry misses an invocation or provides incomplete context.
- Governance quality depends entirely on Larry's discipline in any given session.

**Overhead**
None beyond current practice.

**Risk of governance bloat**
Lowest. No new agent, no new files, no new handoffs.

**Smallest safe next step**
None required. The foundation is live and Larry is already authorized to invoke.

**Required Owner approval**
Confirm: "Option A."

---

## Option B — Named lightweight Gatekeeper persona

**Purpose**
A separate persona exists solely to receive invocations from Larry and produce gate blocks at CP-1 through CP-4. The scope is identical to the current GL-019 / SOP-019 function. The persona adds no broader review capability.

**Responsibilities**
- Receive invocation from Larry at the correct checkpoint.
- Check only what is explicitly declared in the active session context.
- Detect the six GL-019 failure modes.
- Produce one gate block per checkpoint — fixed format, maximum 5 lines.
- State "Hard boundary. This block cannot be overridden." when a hard boundary is violated.

**What stays with Larry**
Invoking the Gatekeeper at the correct moment. Providing complete declared context per SOP-019 Section 3. Surfacing gate blocks to the Owner without modification. Recording every invocation in the session log. Resolving or escalating blocked gates. Recording procedural overrides.

**Pros**
- Separates the orchestrator and the gatekeeper into distinct voices. Reduces self-checking risk.
- Named invocation makes governance discipline visible and auditable.
- Minimal AGENT.md: no domain knowledge section required. The function is structural, not knowledge-intensive.

**Cons**
- Adds one agent to maintain (AGENT.md, folder, index entry, smoke test).
- Adds a handoff step per checkpoint — small overhead but present.
- Does not address scenarios where the Owner wants independent review of Larry's governance output. That is Option C.

**Overhead**
One AGENT.md file, one folder, one agent-index entry, one smoke test. Ongoing: none beyond what Larry already performs.

**Risk of governance bloat**
Low. The persona scope is tightly bounded by GL-019 and SOP-019. Expansion requires Owner-approved GL-019 revision.

**Pax brief question**
A Pax brief is not recommended for Option B. The Gatekeeper persona operates on declared session context only — it does not apply domain knowledge. It executes a fixed structural procedure already fully documented in GL-019 and SOP-019. There is no knowledge domain to research. The AGENT.md would contain identity, responsibilities, Never Does, hard boundaries, collaboration, and pointers to GL-019 and SOP-019. Nolan recommends proceeding without Pax for Option B, but the final decision on Pax involvement requires Owner confirmation.

**Smallest safe next step**
Owner confirms Option B. Nolan delivers a separate implementation proposal describing the AGENT.md structure, folder name, smoke test scenario, and index update. Owner approves the implementation proposal before any file is created.

**Required Owner approval**
Two steps: (1) Confirm "Option B." (2) Approve the separate implementation proposal before execution.

---

## Option C — Owner Review Advisor

**Purpose**
A separate role that helps the Owner independently review Larry's governance output. The Advisor does not produce gate blocks. It reads what Larry has produced and surfaces risks, scope creep, missing approvals, stale paths, count mismatches, and exact next prompts — from the Owner's perspective, not Larry's.

**Responsibilities**
- Receive governance output from Larry (gate blocks, session log entries, DP records).
- Check for risks, gaps, and inconsistencies that Larry may have missed or under-flagged.
- Surface findings to the Owner in plain language — not in gate block format.
- Identify missing approvals, stale path references, count mismatches, scope creep, and premature file writes as seen from the Owner's vantage point.
- Provide exact next prompts the Owner can use to proceed, redirect, or escalate.

**What stays with Larry**
Governance procedure execution. Gate block production. Session log recording. Blocked gate handling. Procedural override recording. The Advisor does not replace any of Larry's governance duties — it adds an independent review layer above them.

**Pros**
- Gives the Owner an independent check on Larry's governance discipline without having to read GL-019 or SOP-019 themselves.
- Catches patterns Larry may miss (repeated procedural overrides, accumulating stale paths, scope creep across sessions).
- Strengthens Owner control over complex multi-session governance trajectories.

**Cons**
- Highest overhead of the three options. Requires a meaningful AGENT.md, domain knowledge (governance frameworks, Owner-side review methodology), Pax brief, smoke test.
- Adds a second agent in the governance chain — increases handoff complexity.
- Risk of conflicting signals if the Advisor and Larry produce different assessments of the same gate.
- Only useful if governance trajectories are long and complex enough to warrant independent review. For simple single-session proposals, the overhead exceeds the value.

**Overhead**
Full hiring flow: Pax brief, AGENT.md with domain knowledge, folder, index entry, smoke test. Ongoing: the Advisor must be kept current with GL-019 and SOP-019 revisions.

**Risk of governance bloat**
Medium to high. The Advisor scope is broader than a gate block producer. Without clear boundaries in the AGENT.md, the role risks expanding into governance execution rather than governance review.

**Pax brief question**
A Pax brief is recommended for Option C. The Owner Review Advisor role requires domain knowledge in governance review methodology — how to read governance output critically, what patterns indicate systemic risk, and how to present findings to an owner without creating decision fatigue. This is a knowledge-intensive function, unlike Option B. Nolan recommends Pax researches governance review frameworks and Owner-facing audit methodology before the AGENT.md is written. The final decision on Pax involvement requires Owner confirmation.

**Smallest safe next step**
Owner confirms Option C. Larry briefs Pax on the research scope. Pax delivers a domain brief. Nolan delivers a separate implementation proposal based on the Pax brief. Owner approves the implementation proposal before any file is created.

**Required Owner approval**
Three steps: (1) Confirm "Option C." (2) Approve Pax brief scope before research begins. (3) Approve implementation proposal before execution.

---

## Hard boundaries (all options)

These apply under every option and cannot be overridden by any instruction including Owner instruction:

- No file reads, opens, or filesystem scans of any kind.
- No grep or search operations.
- No Auto-Learning design, Codex evaluation, or automation design.
- No Core AI Team Audit reopening.
- No new agent design or database design beyond what is explicitly approved per option.
- No file writes or index updates.

---

## Owner decision required

Confirm one of the following before any action is taken:

- **Option A** — Practice only. No further action.
- **Option B** — Named lightweight Gatekeeper persona. Separate implementation proposal follows.
- **Option C** — Owner Review Advisor. Pax brief first, then separate implementation proposal.

No implementation begins before explicit Owner confirmation.

---

*Delivered on: 2026-06-06*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper/governance-gatekeeper-role-adoption-scoping-proposal-v02.md*
