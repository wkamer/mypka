# CLAUDE.md Amendment Proposal: Governance Deliverable File-First Rule

**Version:** v01
**Date:** 2026-06-12
**Author:** Governance Assistant
**Status:** Proposal v01 rev2, awaiting Owner decisions B and C before any CLAUDE.md edit
**Revision note:** GL-021 write authorization boundary added to Section 5 per Owner correction 2026-06-12
**Containment folder:** 20260612_Core_DL Control Inventory
**Blocks:** Any CLAUDE.md edit implementing this rule

---

## 1. Observed Problem

On 2026-06-12, during the D-folder operating model session, Claude produced a complete
governance deliverable (D-folder Operating Model Proposal v01) as chat output only.
The proposal answered eight governance questions, classified 34 D-folders into five
categories, and ended with an Owner decision request. No file was written. No persisted
artifact exists for this governance output.

This is a governance behavior gap. The Owner cannot reference the proposal by file path.
The proposal is not auditable. It is not recoverable if the session context is lost. It
cannot be linked from the deliverable_lifecycle registry. It cannot be versioned.

The behavior was not blocked by any existing CLAUDE.md rule because the Execution
Persistence Rule applies only to execution actions (file writes, database changes, archive
operations), not to the production of governance deliverables.

---

## 2. Existing CLAUDE.md Rule Coverage

The following rules exist and were in effect at the time of the gap:

**Execution Persistence Rule (CLAUDE.md, Operational Conventions)**
Scope: every execution that changes files, folders, database records, routing, archive
state, lifecycle state, SOPs, Guidelines, CLAUDE.md, memory summaries, or task state.
Requirement: persisted write plan before authorization; persisted execution report after
execution.
Gap: does not apply to governance deliverables that are produced before any execution
begins. A proposal is not execution. An operating model is not execution. An assessment
is not execution.

**Granularity Gate (CLAUDE.md, Hard Rules)**
Scope: controls whether a new D-folder is created (G1) or a file is placed inside an
existing folder (G2).
Gap: the Granularity Gate governs folder creation, not file creation. It does not require
that an output be written to a file at all. A G2 determination means "place this as a
file in an existing folder" but there is no rule that prevents Claude from delivering the
output as chat text instead of a file.

**Deliverable Registration (CLAUDE.md, Hard Rules)**
Scope: every new primary deliverable folder (G1) must be registered in
deliverable_lifecycle before content is created.
Gap: registration applies to folders. There is no registration requirement for governance
files placed inside existing folders (G2 outputs). There is no rule that requires the
file to exist before the Owner reviews the content.

**Write Authorization Boundary (GL-021)**
Scope: every write action requires Owner confirmation. Read-only steps must declare
themselves read-only.
Gap: producing a governance deliverable as chat output bypasses the file-write path
entirely. No write authorization is sought because no file is written. The rule does not
address the inverse failure: that a governance output is never persisted at all.

**Summary of coverage gap:**
No existing rule requires that governance deliverables (proposals, operating models,
assessments, decision records, reviews, write plans, audit records) be written to a
file before or at the time of delivery. The Execution Persistence Rule covers outputs
after execution. The Granularity Gate covers folder creation. Neither covers the
production of the governance deliverable itself.

---

## 3. Identified Gap

**Gap statement:**

Claude can produce a complete governance deliverable as chat output, receive Owner
approval or rejection based on that chat output, and close the session with no persisted
artifact. This is structurally equivalent to the Execution Persistence gap that the
Execution Persistence Rule was written to close, but it occurs one phase earlier: at the
point of governance deliverable production, not at the point of execution.

**Consequences of the gap:**

1. Governance decisions made on chat-only proposals are not auditable.
2. Chat content is lost on session close or compaction. The proposal cannot be recovered.
3. The deliverable_lifecycle registry has no record of the governance artifact.
4. Versioning is impossible. A revised proposal cannot supersede a chat-only v01.
5. Other specialists cannot read the proposal. Only the Owner and Claude have access to
   the chat context.
6. The gap creates an inconsistency: write plans and execution reports must be files,
   but the governance proposals that authorize them do not have to be.

---

## 4. Proposed Smallest Safe CLAUDE.md Amendment

**Approach:** add one new rule section, "Governance Deliverable File-First Rule", to the
Hard Rules block in CLAUDE.md. Placement: immediately after the Execution Persistence Rule.

This is the smallest safe amendment because:
- It adds one rule only.
- It does not modify any existing rule.
- It does not change the Granularity Gate, the Execution Persistence Rule, or the
  Deliverable Registration rule.
- It is scoped narrowly to governance deliverables. It does not apply to routine chat
  confirmations, status updates, or questions.

---

## 5. Exact Proposed Wording

The following text is proposed verbatim for insertion into CLAUDE.md immediately after
the Execution Persistence Rule section:

---

### Governance Deliverable File-First Rule

For every governance deliverable produced during a session: the content must be written
to a file before or at the same time as it is presented to the Owner for review or
approval.

A governance deliverable is any output that:
- presents a proposal, operating model, assessment, or decision record for Owner review,
- will be referenced in a subsequent execution step (write plan, archive action, database
  update, CLAUDE.md edit, SOP or GL change), or
- classifies artifacts, defines categories, or establishes rules that govern future
  team behavior.

**File location:** apply GL-017 Granularity Gate first.
- If G1: create a new D-folder, register in deliverable_lifecycle, write the file inside.
- If G2: write the file inside the most relevant existing D-folder. No new folder needed.

**Write authorization — GL-021 not overridden:** this rule does not override GL-021.
Writing a governance deliverable to a file is a write action and requires Owner
authorization before the file is written.

Standard sequence when producing a governance deliverable:
1. Claude determines the output is a governance deliverable and identifies the target
   file path (via the GL-017 gate above).
2. Claude presents a minimal file-write proposal: proposed file path and one-line
   description of the content. Claude does not output the full governance deliverable
   content in chat at this step.
3. Claude asks for Owner authorization of the exact file write path.
4. After Owner authorizes: Claude writes the governance deliverable to that file and
   responds in chat with a short confirmation and the exact file path only.

Exception: if the Owner's prompt already explicitly authorized the exact target file
path (for example, "write it to X" or by specifying the path in the task brief), Claude
may write directly without a separate authorization step. A general instruction to
produce a deliverable is not explicit authorization of a specific file path.

**Chat output:** a short confirmation (title, file path, one-line description) is
sufficient chat output after the file is written. The full governance content must be
in the file, not in chat.

**Waiver:** Owner may explicitly instruct chat-only delivery for a specific deliverable.
State the waiver in chat before producing the output. No standing waiver applies.

**Violation trigger:** if Claude produces governance deliverable content in chat without a
corresponding persisted file, the next action before any further work is to write the
file and confirm the path to the Owner. Governance decisions made on chat-only content
are not considered authorized until the file exists.

---

## 6. Scope of the Rule

**In scope (must be written to a file before or at delivery):**
- Operating model proposals
- Assessment documents (granularity, usability, architecture, eligibility)
- Triage reports and decision inventories
- Decision records
- Write plans and write proposals
- Audit records and execution reports
- Batch scope proposals
- GL, SOP, and WS amendment proposals
- Phase proposals and phase design documents
- Review documents (Iris review, governance review, Owner review)
- Any output the Owner is asked to approve, confirm, or reject

**Out of scope (chat-only is acceptable):**
- Short confirmations: "Done. File written at [path]."
- Status updates: "Preflight complete, no issues found."
- Clarifying questions: "Should this apply to CAT-4 only or to all categories?"
- Routing confirmations: "Delegating to Kai, team_tasks row inserted."
- Read-only findings that do not ask for Owner approval or decision.
- Single-line acknowledgements of Owner instructions.

---

## 7. Examples

**Must be a file (governance deliverable):**

- D-folder Operating Model Proposal v01 (the output that triggered this gap): a
  complete classification of 34 folders into 5 categories, with operating rules for
  each, answering 8 governance questions, and ending with an Owner approval request.
  This must be written to a file before the Owner is asked to confirm.

- Batch 2 Write Plan: a list of 21 folders with per-folder archive actions and
  batch-stop conditions. Must be a file before Owner authorization.

- GL-013 Resolution Proposal: proposed wording for GL-013 additions. Must be a file
  before Owner reviews and approves.

- DLH Phase C Proposal: a multi-step execution proposal. Must be a file before Owner
  approves the phase.

**Acceptable as chat-only:**

- "Preflight complete. The target folder exists and has 21 files."
- "team_task 94 is confirmed open. Status: open."
- "Should I include CAT-3 folders in the Batch 2 write plan?"
- "File written at Deliverables/20260612_Core_DL Control Inventory/proposal-v01.md."
- "No archive, no DB updates, no new folders created."

---

## 8. Risks and Rollback

**Risk 1: Rule applied too broadly**
If every output is treated as a governance deliverable, Claude will write files for
routine confirmations. This creates folder clutter.
Mitigation: the scope definition in Section 6 is explicit. Chat-only is acceptable for
confirmations, questions, and status updates. The rule triggers on "presented for Owner
approval or decision" as the key criterion.

**Risk 2: File write adds latency before Owner review**
If Claude must write a file before showing content, the Owner waits slightly longer.
Mitigation: the GL-017 Granularity Gate already handles G2 placement. For G2 outputs,
writing a file into an existing folder adds seconds only. For G1 outputs, folder
creation and registration already apply.

**Risk 3: Waiver is used too often**
If Owner grants standing waivers frequently, the rule is bypassed systematically.
Mitigation: the rule states explicitly that no standing waiver applies. Each waiver is
per-deliverable and must be stated before output.

**Rollback:** if the rule produces unintended behavior after adoption, the rule section
can be removed from CLAUDE.md in one targeted edit. No other rules are modified. No
database changes are required to roll back.

---

## 9. Exact Owner Decision Needed Before Editing CLAUDE.md

Three decisions are required:

**Decision A:** Do you accept the gap analysis in Section 3 as accurate? (Yes, No, or
correction.)

**Decision B:** Do you accept the proposed rule wording in Section 5 as the amendment
to insert into CLAUDE.md? (Yes, No, or correction. If correction: provide the specific
change and a corrected v02 will be produced.)

**Decision C:** Do you authorize Claude to edit CLAUDE.md with the exact text in Section
5, placed immediately after the Execution Persistence Rule? (Yes or No. Authorization
is required per GL-021 before any CLAUDE.md write action begins.)

All three decisions must be Yes before any CLAUDE.md edit is made.

---

**Delivered on:** 2026-06-12
**Delivered at:** Deliverables/20260612_Core_DL Control Inventory/20260612_claudemd-governance-deliverable-file-first-rule-proposal-v01.md
