# GL-020 — Intent Classification Taxonomy

**Last reviewed:** 2026-06-06
**Status:** Active

---

## Section 1 — Purpose and Scope

This guideline governs the classification of Owner input before any routing, delegation, or execution occurs. Every Owner input belongs to exactly one intent category. Larry applies this taxonomy before acting.

This guideline does not govern: routing logic, specialist delegation procedures, session logging, or SOP execution. Those are defined in the relevant SOPs and agent instructions. This taxonomy is the classification layer only — it determines what kind of input something is, not what happens next in detail.

**Structural assumption SA-001** is documented in Section 8.

---

## Section 2 — The Six Intent Categories

### CAT-1 — Operational Task

A concrete, bounded action within an existing SOP or pre-approved flow. The action and scope are clear. No structural change implied.

**Rule 1:** The input names a specific action that matches an existing SOP, workflow, or recurring delegation pattern.
**Rule 2:** No structural change to the system is implied or possible as an outcome.

### CAT-2 — Information Request

The Owner wants to know something. No action follows from classification alone. Research, lookup, retrieval, or status check.

**Rule 1:** The input ends in a question, or the primary verb is "what", "how", "show me", "check", "find", "tell me", or "status".
**Rule 2:** The expected output is information only — no file write, no database update, no SOP change required.

### CAT-3 — Governance Input

The Owner is changing, proposing, or approving a structural rule, SOP, GL, agent behavior, automation boundary, or team structure. The output will modify how the system operates.

**Rule 1:** The input proposes, approves, rejects, or modifies a rule, SOP, GL, agent instruction, automation boundary, or team structure.
**Rule 2:** The output of acting on this input would change how any agent behaves or how the system operates going forward.
**Rule 3:** CAT-3 inputs always produce either a Level 2 candidate or a Level 3 candidate — never a Level 1 outcome. Apply the boundary criterion from Section 5 to determine which. If the team member's AGENT.md does not contain at least one explicit responsibilities statement AND at least one explicit boundary statement, escalate to Owner immediately regardless of apparent fit.

### CAT-4 — Project / Planning Input

The Owner is initiating, reviewing, or adjusting a project, goal, or planning artifact. Not execution.

**Rule 1:** The input introduces, adjusts, or reviews a project, goal, highlight, task, or planning artifact.
**Rule 2:** The input does not also propose a rule change — if it does, CAT-3 takes precedence.

### CAT-5 — Personal Reflection / Journal Input

The Owner shares a narrative, day reflection, observation, feeling, or life update. Routes to Penn immediately.

**Rule 1:** The input is a personal narrative, first-person observation, day recount, or emotional reflection.
**Rule 2:** The input is not asking for action, information, or a system change — it is sharing experience.

### CAT-6 — Ambiguous / Unclassifiable

Input cannot be reliably assigned to a single category. Larry must ask before routing.

**Rule 1:** Two or more categories apply to the same input and the rules above do not resolve the tie.
**Rule 2:** The input is too short or context-free to classify reliably (e.g., a single noun, a reference without explanation).

---

## Section 3 — Routing Table

| Category | Default Routing Target | Trigger Mechanism |
|---|---|---|
| CAT-1 Operational Task | Domain specialist per SOP (Sienna, Marcus, Kai, Penn) | Direct delegation from Larry |
| CAT-2 Information Request | Pax (research), Sienna (personal lookup), or Larry direct | Direct delegation or Larry direct |
| CAT-3 Governance Input | SOP-019 Governance Gate (Larry → Iris → Owner) | SOP-019 checkpoint sequence |
| CAT-4 Project / Planning Input | Sienna (behavioral gate) → Marcus (ICOR) → Larry (route) | Sienna Priority Gate mandatory |
| CAT-5 Personal Reflection / Journal Input | Penn immediately | /journal skill |
| CAT-6 Ambiguous / Unclassifiable | Larry holds — asks one clarification question | Clarification protocol (Section 7) |

---

## Section 4 — Approval Gate Table

| Category | Gate Level |
|---|---|
| CAT-1 Operational Task | Automatic action allowed within pre-approved SOP boundaries. Larry confirms when done. |
| CAT-2 Information Request | Automatic action allowed. No approval gate. Larry presents result. |
| CAT-3 Governance Input | Governance gate required. Sequence: classify → propose → Iris review → Owner approval → execute. No exceptions. |
| CAT-4 Project / Planning Input | Proposal required first. Sienna behavioral gate activates. Marcus ICOR classification required. Owner confirms before any artifact is created. |
| CAT-5 Personal Reflection / Journal Input | Automatic action allowed. Penn journals without asking. |
| CAT-6 Ambiguous / Unclassifiable | No action until clarified. After clarification, apply the gate of the resolved category. |

**Note — CAT-3 approval gate:** Iris review is an advisory gate and does not substitute for Owner authorization. These are two sequential gates — neither replaces the other. Authoritative definition: [[GL-021_Owner Interaction Rule and Write Authorization Boundary]], Section 5.

For learnings arising from handling each category, see Section 5 — Learning Level per Intent Category.

---

## Section 5 — Learning Level per Intent Category

### Learning Value Filter — Three Levels

**Level 1 — Direct experiential learning**
A team member learns from experience and applies it to improve future behavior within the same role. Owner approval is not required. No file changed. No SOP changed. No AGENT.md changed.

**Level 2 — Learning candidate**
A learning may be useful beyond the current moment. The responsible team member flags it as a candidate. Owner approval is only required if the candidate becomes structural. No file changed until Owner approves.

**Level 3 — Structural system learning**
A learning requires changes to SOPs, GLs, AGENT.md, CLAUDE.md, indexes, workflows, automations, databases, file structures, or formal role definitions. Owner approval is always required before any change.

### Level 1 / Level 2 Boundary Criterion

> Could a third party, reading only this team member's current AGENT.md without access to this session, have predicted this behavioral change from the existing role definition?
>
> Yes → Level 1. Apply autonomously.
> No → Level 2 candidate. Flag it.
> If the AGENT.md does not contain at least one explicit responsibilities statement AND at least one explicit boundary statement, the criterion cannot be applied; escalate to the Owner.

### Learning Level Mapping per Category

| Category | Label | Learning Level When a Learning Arises |
|---|---|---|
| CAT-1 | Operational Task | Level 1 — behavioral refinement within role; no structural implication |
| CAT-2 | Information Request | Level 1 or Level 2 — response patterns stay Level 1; exceptions that expose a role gap escalate to Level 2 |
| CAT-3 | Governance Input | Level 2 or Level 3 — never automatically Level 1 |
| CAT-4 | Project / Planning Input | Level 2 — every unhandled planning gap reveals a possible role boundary; Owner decides if structural |
| CAT-5 | Personal Reflection / Journal Input | Level 1 if within Penn's defined routing pattern; Level 2 if the pattern itself needs updating |
| CAT-6 | Ambiguous / Unclassifiable | Level 2 mandatory — ambiguity by definition cannot be resolved autonomously |

---

## Section 6 — Iris Review Threshold

**Iris review is mandatory when:**
- All CAT-3 Governance Input outputs, without exception
- Any proposed new SOP, GL, Workstream, or AGENT.md section
- Any proposed automation rule or auto-processing boundary change
- Any proposed change to the Iris review process itself (self-referential governance)
- Any output where Larry cannot confirm the action is fully reversible

**Escalation rule:** If an operational task produces an output that turns out to require structural change, Larry escalates to CAT-3 retroactively and triggers Iris review before presenting to Owner.

**Iris does NOT review:**
- CAT-1 actions within confirmed SOP boundaries
- CAT-2 information responses
- CAT-5 journal entries
- CAT-6 clarification questions

---

## Section 7 — Clarification Protocol

Larry asks a clarification question when any of the following conditions hold:

**Unclassifiable conditions:**
- The input matches two or more categories and the rules in Section 2 do not resolve the tie
- The input contains no verb or referent (e.g., "Pax", "this thing", "auto-learning")
- The input implies structural change but the scope is undefined (e.g., "fix this", "get this in order")

**Minimum clarification question format:**
One sentence. One question. Specific. Name the two candidate categories explicitly: "Are you asking me to [operational action] or to [change how the system works]?"

**What Larry must never do when uncertain:**
- Default to a lower-friction category (e.g., treating governance input as operational because it is faster)
- Execute and apologize afterward
- Ask more than one clarification question — if still unresolved, escalate to CAT-3 as the conservative default

---

## Section 8 — Known Misrouting Risks

### Risk 1 — Governance input classified as operational
**Probability / Impact:** Highest / Highest
**Failure mode:** Owner input sounds like a task ("get auto-learning in order") but proposes a structural change. Specialist begins execution, structural rules get embedded without governance gate, Owner approval is bypassed.
**Mitigation:** CAT-3 Rule 2 triggers on any output that would change how agents behave going forward. This rule is applied before any action is taken.

### Risk 2 — Reflection merged with governance
**Probability / Impact:** Medium / High
**Failure mode:** Owner shares a personal reflection containing a structural observation. Penn routes the reflection; the governance signal is lost.
**Mitigation:** CAT-5 routing explicitly flags observations that imply a system question. Penn borgs the reflection and flags the structural element to Larry as a separate item.

### Risk 3 — Project input bypassing behavioral gate
**Probability / Impact:** Medium / Medium
**Failure mode:** A new initiative framed as a planning update routes directly to Marcus, bypassing Sienna's behavioral gate check. Execution begins on an unvalidated new initiative.
**Mitigation:** CAT-4 routing always activates Sienna Priority Gate before Marcus or any execution.

### Risk 4 — Ambiguous input silently defaulted
**Probability / Impact:** Low / High cumulative
**Failure mode:** Larry cannot classify, picks the closest match without asking, and routes. Repeated small misroutes accumulate into structural drift.
**Mitigation:** CAT-6 is a hard stop. Larry never silently defaults. One question, always.

### Risk 5 — Level 2 Candidate Decay
**Probability / Impact:** Medium / Medium
**Failure mode:** A team member flags a Level 2 candidate but Owner approval is never sought and never tracked. Over time the team member treats the unresolved candidate as implicitly approved and applies it as Level 1. Structural drift accumulates without any change record.
**Mitigation:** A tracking mechanism for Level 2 candidates is to be defined in a separate implementation step pending Owner approval. Until that mechanism is in place, Level 2 candidates must be surfaced to the Owner within the session in which they are flagged.

### SA-001 — Structural Assumption
The Level 1 / Level 2 boundary criterion (Section 5) assumes that all myPKA AGENT.md files contain a Responsibilities section and a boundary section (Never Does or equivalent). In practice this is ensured by the hiring protocol (Pax → Nolan). If an AGENT.md lacks either, the criterion cannot be applied and the learning must be escalated to the Owner.

---

## Section 9 — Changelog

| Date | Change | By | Approval |
|---|---|---|---|
| 2026-06-06 | Initial creation. Six intent categories, routing table, approval gates, Iris review threshold, clarification protocol, misrouting risks. Based on Pax taxonomy preparation report + Learning Value Filter supplement. Iris reviewed and accepted all components. | Pax (research), Larry (scoping + authoring) | Owner |
| 2026-06-06 | Section 4: added note that Iris review does not substitute for Owner authorization; reference to GL-021 Section 5 added. | Larry | Owner |
