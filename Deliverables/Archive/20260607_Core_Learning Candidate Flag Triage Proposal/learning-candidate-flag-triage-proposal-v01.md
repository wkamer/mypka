# Learning Candidate Flag — Triage Proposal v01

> **Superseded by v02.** This version contains a mixed-language section 10 and conflates the triage decision with promotion approval. See `learning-candidate-flag-triage-proposal-v02.md`.

**Document type:** Read-only triage proposal
**Date:** 2026-06-07
**Author:** Larry (Team Orchestrator)
**Status:** Superseded — see v02
**Related task:** team_tasks id 73
**Related records:**
- `Team Knowledge/Core/session-logs/2026/06/20260607_deliverable-lifecycle-phase-1-governance-exception-record.md`
- `Deliverables/20260607_Core_DL Phase 1 Retroactive Iris Review/`

---

## 1. Summary of the Issue

During the Deliverable Lifecycle Phase 1 implementation on 2026-06-07, Iris conducted a retroactive Governance Gatekeeper review and issued a Learning Candidate Flag (CAT-3):

> "Governance checkpoints bypassed when Owner drives implementation interactively. Workflow requires explicit CP invocation even under Owner-directed pace."

All five governance checkpoints (CP-1, CP-2, CP-3, CP-4, and the Iris pre-implementation check) were not invoked. Individual write steps received explicit Owner authorization throughout the session, but no formal Governance Gatekeeper protocol was followed. The implementation stands; no rollback required. The exception is documented in the Governance Exception Record.

This triage determines how the Learning Candidate Flag should be handled: as a Learning Candidate, as a Graduation Candidate, as a direct SOP-019 structural correction proposal, or as another bounded governance action.

---

## 2. Why the Missed Iris Gate Matters

The Iris pre-implementation gate serves two distinct functions that are not interchangeable:

**Advisory review:** Iris assesses whether a proposal is safe, aligned with GL-020, and within execution boundaries before writes begin. Without it, the team has no pre-implementation safety assessment on record.

**Documentation of intent:** The review creates a record that the pre-implementation state was evaluated before any writes. Retroactive reviews are available as a fallback but cannot substitute for the pre-implementation record structurally.

The same logic applies to CP-1 through CP-4: these checkpoints define the formal decision trail (route confirmation, decision point approval, review gate opening, lifecycle gate confirmation). Without them, the implementation has an execution record but no formal governance decision record.

The retroactive Iris review confirmed the implementation was correct. Correctness does not substitute for the process. The governance system cannot assume retroactive reviews will always be available or always reach the same conclusion.

**Related structural finding (out of scope for this triage):**
The CLAUDE.md governance rule says "invoke the Gatekeeper at the relevant checkpoint (CP-1 through CP-4) per SOP-019" but no SOP-019 file exists at `Team Knowledge/Core/SOPs/`. The rule references a document that is absent. This is flagged here as an observation, not as part of this triage decision.

---

## 3. Impacted Governance Areas

| Area | Nature of impact |
|---|---|
| CLAUDE.md Governance Gatekeeper rule | Rule requires CP invocation but does not define behavior for Owner-directed interactive flows |
| SOP-019 (Governance Gatekeeper SOP) | Does not exist as a file — referenced in CLAUDE.md and GL-021 but absent from `Team Knowledge/Core/SOPs/` |
| GL-019 (Governance Gatekeeper Principles) | Referenced in GL-021 — may contain relevant procedure definitions; not read in this triage |
| GL-021 Section 5 | Defines the mandatory CAT-3 sequence: Larry prepares, Iris reviews, Owner confirms, execute |
| GL-022 | Governs the Learning Candidate lifecycle; applies to this flag and this triage |
| Iris pre-check procedure | No documented definition of what Iris pre-check invocation looks like in interactive Owner-directed flows |

---

## 4. Recommended Classification

**Recommendation: Learning Candidate (Level 2).**

### Why not Level 1 (autonomous)

A Level 1 learning is applied autonomously by the team member going forward without Owner input. This observation cannot be Level 1: the question of whether formal CP checkpoints must be invoked when the Owner is driving pace interactively is a governance design question. Owner input is required. Autonomous application is not appropriate.

### Why not immediately Level 3 / direct SOP-019 structural correction

A direct SOP-019 structural correction proposal presupposes that the structural change is defined. It is not yet defined. The Owner must first decide whether interactive Owner-directed flows always require formal CP invocation or whether a lightweight exception mode is appropriate. The specific structural change depends on that decision. Producing a structural correction without that input would mean the team designs the governance rule without Owner authorization — which is itself a governance violation.

Additionally, SOP-019 does not exist as a file. The action would be to create SOP-019, not to correct it. Creating a new SOP requires the governance rule to be established first via Owner decision.

### Why Level 2

The observation qualifies as Level 2 because:
- It requires Owner input before any behavioral rule is established.
- The gap is systemic (all checkpoints missed) but not immediately structurally correctable without Owner input on intent.

The appropriate path is: register as Level 2, surface to Owner in this session (CAT-3 surfacing rule: same session as flagging, no delay), then Owner decides on the next step separately.

### On "Graduation Candidate"

The term Graduation Candidate does not appear in GL-022 or in any current formal governance document. The closest formal mapping is: a Level 2 Learning Candidate flagged for immediate promotion to SOP-019. This triage treats it as equivalent to the Level 2 + promotion route. If the Owner intends Graduation Candidate to be a formal classification distinct from Level 2, the governance system currently has no mechanism for it, and establishing it would itself require a structural correction. This triage does not recommend creating a new classification.

### On "another bounded governance action"

Not recommended. The observation fits the Learning Candidate framework as defined in GL-022. Adding a new governance category for this case would increase complexity without improving resolution.

---

## 5. Recommended Route

The route is split into two separate decisions. This triage covers Decision 1 only.

### Decision 1 — Triage classification (this session, Owner action now)

1. Owner confirms triage: register as Learning Candidate (Level 2).
2. Larry prepares a registration proposal. Iris reviews. Owner authorizes. Larry registers the Learning Candidate in the `learning_candidates` table (team-knowledge.db), status set to `surfaced`.
3. Larry surfaces the Learning Candidate to the Owner in this session (CAT-3 rule: same session as flagging, no delay).
4. team_tasks id 73 remains open until registration and surfacing are both complete.

### Decision 2 — Next step after surfacing (separate Owner decision, not yet approved)

After surfacing, the Owner will separately decide: approve / reject / promote.

Promotion to SOP-019 is the recommended likely next decision. It is not approved by this triage. If the Owner promotes:
- Larry initiates SOP-019 creation (CAT-3 structural action).
- Larry prepares structural proposal. Iris reviews. Owner authorizes. Kai implements if database work is involved. Nolan updates AGENT.md files if agent behavior rules are changed.
- team_tasks id 73 is closed after registration and surfacing are confirmed complete, not after the SOP-019 route concludes.

---

## 6. Whether Iris Review Is Required Before Any Implementation

**For this triage proposal:** No. A triage proposal is read-only. It is Larry's advisory work, not an implementation. No write actions are involved.

**For the next implementation step (Learning Candidate registration):** Yes. Per GL-021 Section 5 Rule 3, the mandatory CAT-3 sequence applies:
1. Larry prepares a complete proposal (this document covers the triage; a registration proposal follows).
2. Iris reviews the registration proposal.
3. Larry presents the reviewed proposal to the Owner.
4. Owner confirms.
5. Larry executes.

Iris has not reviewed the Learning Candidate registration proposal yet. That is a separate next step.

---

## 7. Files and Systems That May Eventually Need Updates

None of the following are changed now. These are read-only forward-looking pointers.

| File or system | Why it may change |
|---|---|
| `team-knowledge.db` table `learning_candidates` | Learning Candidate row INSERT after Owner confirms registration |
| `team-knowledge.db` table `team_tasks` | task id 73: status set to completed after registration |
| `Team Knowledge/Core/SOPs/SOP-019_Governance Gatekeeper SOP.md` | To be created if promoted — this file does not exist yet |
| CLAUDE.md Governance Gatekeeper section | May be updated to define CP invocation behavior in interactive Owner-directed flows |
| `Team Knowledge/Core/Guidelines/GL-019_Governance Gatekeeper Principles.md` | May need extension if principles are updated to cover interactive flows |
| Iris AGENT.md | May receive a behavioral rule for pre-check invocation in interactive flows |
| SOP index (`Team Knowledge/Core/SOPs/sop-index.md`) | Must be updated if SOP-019 is created |

---

## 8. What Must Not Be Changed Yet

- No files modified.
- No database rows inserted or updated (no Learning Candidate row, no team_tasks update).
- SOP-019 not created.
- CLAUDE.md not changed.
- GL-019 not changed.
- Iris AGENT.md not changed.
- team_tasks id 73 not closed.
- No write actions of any kind until Owner confirms triage and then separately confirms each subsequent step.

---

## 9. Can the Owner Answer with Yes, No, or Correction?

Yes. This proposal presents one recommendation with a clear next action. The Owner does not need to elaborate to proceed.

- **Ja:** Learning Candidate (Level 2) is the correct classification. Larry proceeds to prepare a registration proposal for Iris review. team_tasks id 73 stays open. Promotion to SOP-019 is not yet decided.
- **Nee:** The recommended classification is rejected. Larry asks for the preferred alternative before any action.
- **Correctie:** The Owner adjusts the classification. Larry incorporates and confirms before proceeding.

---

## 10. Exact Next Owner Action

> **Bevestig de triage-classificatie:**
>
> 1. Registreer dit als Learning Candidate (Level 2).
> 2. Surface het in dezelfde sessie omdat het CAT-3 is.
> 3. Houd team_tasks id 73 open totdat registratie en surfacing zijn afgerond.
>
> Promotie naar SOP-019 is de aanbevolen vervolgstap na surfacing — maar wordt pas beslist in de volgende Owner-actie.
>
> Antwoord: ja / nee / correctie.

---

*Delivered on: 2026-06-07*
*Delivered at: Team Orchestrator — Larry*
