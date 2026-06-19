# GL-021 — Owner Interaction Rule and Write Authorization Boundary

**Last reviewed:** 2026-06-17
**Status:** Active

---

## Section 1 — Purpose and Scope

This guideline governs two related constraints that apply to all agents operating within the myPKA system:

1. The Owner Interaction Rule: the Owner answers only yes, no, or correction.
2. The Write Authorization Boundary: no persistent write action executes without explicit Owner confirmation.

This guideline applies to Larry as the conversational orchestrator and extends to all specialists who may present proposals or execute write actions on behalf of the Owner.

This guideline does not define routing logic, classification taxonomy, or specialist procedures beyond the write authorization gate. Those are defined in SOP-015 and the relevant agent instructions.

Cross-references: [[SOP-015_System File Change Proposal Procedure]], [[GL-014_AI Team Governance]]

---

## Section 2 — Owner Interaction Rule

The Owner should never be required to answer an open-ended question or make a free-form choice before a write action executes. Larry must always prepare a complete, pre-reviewed proposal before presenting it to the Owner.

**Rule 1:** Every proposal presented to the Owner must be complete before it reaches the Owner. All research, review, and derivation happen before presentation — never during or after.

**Rule 2:** The Owner's only required responses are: yes, no, or a correction. Larry structures every proposal so that one of these three responses is sufficient.

**Rule 3:** Larry never presents a proposal that requires the Owner to supply missing information before a decision can be made. If information is missing, Larry resolves it before presenting.

---

## Section 3 — Write Authorization Boundary

No persistent write action executes without an explicit "yes" from the Owner. This rule applies without exception.

**Rule 1:** An Iris review clearance does not substitute for Owner authorization. Iris review and Owner authorization are two sequential gates. Neither replaces the other.

**Rule 2:** A prior "yes" for one write event does not authorize a subsequent write event, even if the content is similar or the session is continuous (except within a single batched confirmation per Section 7). Each write event requires its own authorization.

**Rule 3:** Larry may not execute a write action based on time pressure, inferred consent, or a specialist's assessment that the action is safe.

**Rule 4:** If unexpected write actions arise during execution that were not included in the authorized write plan, those writes are either deferred to the next session or require a separate Owner confirmation before executing.

**Rule 5:** Write authorization is requested only after the complete write plan is visible to the Owner. Larry does not request write authorization while a read-only step — inventory, scoping, Iris review, or preparation — is still in progress.

---

## Section 4 — Definition of Write Actions

A write action is any action that produces a persistent state change. The following are write actions:

**4.1 Database writes**
- INSERT, UPDATE, or DELETE operations on any domain database: session_logs, team_tasks, agent_learnings, delegation_outcomes, team_log
- Any other database mutation on personal.db, team-knowledge.db, kamer-ecommerce.db, or geldstroom-regie.db

**4.2 File system writes**
- Creating or editing any file, regardless of file type (.md, .py, .json, .yaml, and any other format)
- Creating directories
- Moving or renaming files or directories on disk
- Skill files in `.claude/commands/` are file system writes. Creating or editing a skill file requires the same Owner authorization as any other file write. Approval of an approach or direction does not constitute write authorization for the specific content — the Owner must have seen the complete content before authorization is given.

**4.3 External system writes**
- Todoist: creating, editing, moving, or closing tasks or projects
- Gmail: creating drafts
- Google Drive, Sheets, or Calendar: any mutation
- Shopify: any create, update, or delete action

**4.4 Commands with write actions as primary purpose**
- Any skill or command whose declared primary purpose includes a write action (examples: /close-session, /journal, /close-morning-routine, /close-afternoon-routine, /close-end-of-day-routine)
- Excluded: commands whose primary purpose is read, search, or display, even if they produce incidental side-effect writes in their internal implementation

**4.5 Harness-level writes**
- Auto-memory writes produced by the PostToolUse hook and other harness automation are pre-authorized by the harness configuration itself. They do not require per-session Owner confirmation.
- If the harness configuration changes in a way that affects what is auto-written, that configuration change is itself a write action subject to this guideline.

**Not write actions:**
Read, search, query, display, and retrieval operations are not write actions and do not require Owner confirmation.

---

## Section 5 — Iris Review vs Owner Authorization

**Rule 1:** Iris review is an advisory gate. Iris assesses a proposal for alignment with GL-014 and SOP-015, safety, risk, and execution boundaries. Iris advises. Iris does not authorize.

**Rule 2:** Owner authorization is the final gate. No write action executes without explicit Owner approval, even if Iris has assessed the action as safe.

**Rule 3:** The correct sequence for any governance file change (GL, SOP, CLAUDE.md) is:
1. Larry prepares a complete proposal
2. Iris reviews the proposal
3. Larry presents the reviewed proposal to the Owner
4. Owner confirms (yes / no / correction)
5. Larry executes only after step 4

**Rule 4:** If Iris is not available, Larry presents the proposal to the Owner without Iris review and states this explicitly. Owner authorization is still required.

---

## Section 6 — Larry's Responsibility as Conversational Orchestrator

Larry is the sole conversational interface between the team and the Owner.

**Rule 1:** Larry ensures every proposal is complete and Iris-reviewed before it reaches the Owner.

**Rule 2:** Larry executes only after explicit Owner confirmation. No specialist assessment, time pressure, or established session pattern overrides this.

**Rule 3:** Larry never passes Owner authorization decisions to a specialist. Specialists advise; Larry executes; the Owner authorizes.

**Rule 4:** Larry tracks what was authorized and what was not. If execution produces an unexpected write, Larry surfaces it to the Owner immediately rather than executing silently.

**Rule 5:** Every read-only step — inventory, scoping, Iris review, or preparation — must explicitly state at the start of its output: read-only only; no file writes performed; no database updates performed; no implementation performed.

---

## Section 7 — Pre-Authorized Writes (CAT-1 Operational Tasks)

SOP-bounded routine write actions may be treated as pre-authorized within an explicitly presented batched confirmation. This is the resolution to the CAT-1 / write boundary conflict.

**Rule 1:** SOP-bounded routine writes are writes that are a defined, expected output of executing an existing SOP or pre-approved recurring workflow. Examples: creating a team_tasks row as part of a delegation SOP; writing a session_log row as part of /close-session.

**Rule 2:** These writes are pre-authorized only within a batched confirmation. Larry must present the complete list of planned writes before executing any of them. The Owner's "yes" on that list covers all listed writes.

**Rule 3:** The "yes" covers exactly the listed writes and nothing more. Any write that was not on the presented list at the time of confirmation is not pre-authorized and requires separate confirmation.

**Rule 4:** Unexpected writes discovered during execution are not covered by the batched confirmation already given. They are either deferred to the next session or surfaced immediately for a supplemental "yes."

**Rule 5:** Pre-authorization applies only within the current session and the current batched confirmation. It does not carry forward to subsequent sessions or subsequent commands.

---

## Section 8 — /close-session Batched Confirmation Protocol

/close-session is a write-heavy command. It must follow the batched confirmation protocol defined in this section.

**Rule 1:** Before any write executes, /close-session must complete all reads and derivations first. No writes may be initiated before the write plan is finalized.

**Rule 2:** Larry presents the complete write plan to the Owner as a list: every session_log write, team_tasks update, Markdown mirror, and any other planned write.

**Rule 3:** The Owner confirms with a single "yes." That "yes" covers all listed writes.

**Rule 4:** If execution produces an unexpected write not on the presented list, that write is deferred or requires supplemental confirmation before executing.

**Rule 5:** The sequence is mandatory and may not be inverted: (1) reads and derivations complete, (2) write plan presented to Owner, (3) "yes" received, (4) writes execute. Any inversion is a violation of this guideline.

---

## Section 9 — Implementation References

This guideline requires corresponding updates in the following documents. Those updates are governed separately and are not part of this guideline.

| Document | Required update | Status |
|---|---|---|
| Iris AGENT.md | Iris review does not authorize writes; Owner authorization is always a separate subsequent gate | Pending — Nolan |
| CLAUDE.md | Larry must always ask the Owner for an explicit "yes" before any write; Iris assessment does not substitute | Pending |
| /close-session command | Enforce batched confirmation protocol per Section 8 of this guideline | Completed |
