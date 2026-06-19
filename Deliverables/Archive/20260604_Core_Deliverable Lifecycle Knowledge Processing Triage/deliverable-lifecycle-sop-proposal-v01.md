# Proposal: SOP-017 — Deliverable Lifecycle, Knowledge Processing, and Archiving Procedure

**File:** `Deliverables/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage/deliverable-lifecycle-sop-proposal-v01.md`
**Date:** 2026-06-04
**Prepared by:** Larry, Team Orchestrator
**Proposal version:** v01
**Status:** Proposal-only — awaiting Owner approval

**Governance:** This document is read-only. No SOP file creation, index update, or any system change may be executed without explicit Owner Walter Kamer approval of this proposal. This is a proposal document only.

---

## 1. Confirmed SOP Number

**SOP-017**

Confirmed from `Team Knowledge/Core/SOPs/SOP-index.md` on 2026-06-04. The current highest SOP number is SOP-016. SOP-017 is the next available number.

---

## 2. Proposed Filename

`SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md`

---

## 3. Proposed Canonical Path

`Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md`

---

## 4. Exact SOP Content

The content between the markers below is the exact text to be written to the SOP file if this proposal is approved. No variation, paraphrasing, or partial execution is permitted. Implementation executes exactly this content.

---

[BEGIN SOP-017 FILE CONTENT]

# SOP-017: Deliverable Lifecycle, Knowledge Processing, and Archiving Procedure

**File:** `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md`
**Owner:** Walter Kamer
**Maintainer:** Larry, Team Orchestrator
**Status:** Active
**Version:** 1.0
**Created:** 2026-06-04

---

## 1. Purpose and Relationship to GL-017

This SOP defines how to execute lifecycle decisions for myPKA AI team deliverables. It is the operational counterpart to GL-017 (Deliverable Lifecycle, Knowledge Processing, and Archiving), which defines the lifecycle principles and states.

This SOP defines procedures only. It does not redefine the lifecycle states, core principles, or relationship hierarchy established in GL-017. Readers should consult GL-017 for the authoritative list of lifecycle states and the twelve core principles governing all lifecycle processing.

This SOP is downstream of GL-016 (Review Gate for Governance-Relevant Deliverables) and SOP-016 (Review Gate Procedure for Governance-Relevant Deliverables). The review gate must complete before this SOP activates.

---

## 2. Prerequisites

This SOP may not be executed unless all of the following conditions are met:

1. The deliverable has been submitted to and passed the review gate per GL-016 and SOP-016.
2. The Owner has made an explicit acceptance decision for the deliverable.
3. The deliverable state has been confirmed as Accepted as Done per GL-017.

If any condition is not met: stop. Surface the missing condition to the Owner. Do not proceed with any processing, archiving, or knowledge extraction action.

---

## 3. Trigger Moments

This SOP is activated at the following moments. Activation surfaces a processing decision to the orchestrator and Owner. It does not automatically initiate processing.

| Trigger | What to do |
|---|---|
| Deliverable accepted as Done (primary trigger) | Apply decision rules R1 through R10. Present candidates to Owner. Wait for approval. |
| Newer version of a deliverable accepted as Done | Previous version is a candidate for Superseded state. Apply R2. Present to Owner. |
| Execution report accepted as Done | Apply decision rules. Common outcome: Authoritative (R1) or retain in place (R9). |
| Closure report accepted as Done | Apply decision rules. Common outcomes: Authoritative (R1) and Lessons learned candidate (R3). |
| Triage report accepted as Done | Apply decision rules. Common outcome: Authoritative (R1) as the initiating reference for its initiative. |
| Decision packet accepted as Done | Apply decision rules. Common outcome: Personal or business decision record (R4 or R5). |
| Owner requests lifecycle review of a specific deliverable | Apply decision rules R1 through R10. Present candidates. Wait for approval. |

---

## 4. Lifecycle Decision Workflow

Execute the following phases in order. Do not skip phases. Do not combine phases.

### Phase 1: Prerequisite Verification

**Step 1.** Confirm the deliverable has passed the review gate per SOP-016. If not, stop and surface to Owner.

**Step 2.** Confirm the Owner has made an acceptance decision. If not, stop and surface to Owner.

**Step 3.** Record the deliverable path, domain, type, and current state.

### Phase 2: Rule Application

**Step 4.** Apply decision rules R1 through R10 from Section 6 in order. A deliverable may satisfy multiple rules.

**Step 5.** Record which rules apply and the candidate processing destination for each.

### Phase 3: Cross-Domain Check

**Step 6.** Review all candidate destinations. If any candidate destination spans more than one domain (personal and business, or two business domains), flag it. Do not propose second-domain processing until Owner has explicitly approved the routing.

**Step 7.** For cross-domain content: surface to Owner with the full routing proposal before proceeding. Apply GL-015 routing rules. Apply SSOT Golden Rule: one home, references only.

### Phase 4: Owner Proposal

**Step 8.** Present all processing destination candidates to the Owner. For each candidate, state:
- The rule that triggered it (R1 through R10)
- The exact destination (file path, database, or folder path)
- The agent who would execute it
- The expected action (write, index, mark state, move, extract)

**Step 9.** Wait for explicit Owner approval for each candidate destination. Unapproved destinations are not executed.

### Phase 5: Execution

**Step 10.** Execute only the Owner-approved processing destinations.

**Step 11.** Follow GL-015 for all database writes. Confirm domain and source_type before writing.

**Step 12.** Follow SOP-015 for any new GL, SOP, Workstream, or AGENT.md updates that result from lifecycle processing. These are separate proposals requiring separate Owner approval.

**Step 13.** Retain the source deliverable in its current Deliverables folder location unless archiving was explicitly approved and a formal proposal was prepared per EX-6.

**Step 14.** Run the Safeguards Checklist from Section 13 before and after execution.

### Phase 6: State Update and Reporting

**Step 15.** Update the deliverable state to reflect completed actions per the lifecycle states in GL-017.

**Step 16.** Write an execution report per the requirements in Section 16.

**Step 17.** If the execution report itself is a governance-relevant deliverable, submit it to the review gate per GL-016 and SOP-016 before accepting it as Done.

---

## 5. Processing Destination Catalog

Each accepted deliverable is assessed against the following destinations. A deliverable may have multiple applicable destinations. Each destination requires a separate Owner-approved action.

| Destination | Description | Executing agent | Owner approval required |
|---|---|---|---|
| Authoritative source | Stays in Deliverables folder; designated as canonical reference; indexed; not moved or modified | Larry designates; Owner confirms | Yes — designation confirmation |
| PKM — Personal Knowledge Management | Personal decisions, personal insights, personal lessons written to PKM | Penn or Sienna | Yes — before any write |
| BKM — Kamer E-commerce | Business knowledge for Kamer E-commerce domain written to KB | Nova, Vera, Sasha, or Zara | Yes — before any write |
| BKM — Geldstroom Regie | Business knowledge for Geldstroom Regie domain written to KB | Finn | Yes — before any write |
| Governance reference | Governance decisions or team-level patterns indexed by Larry; no file move | Larry | Yes — before indexing |
| Personal decision record | A specific Owner decision logged for future reference | Sienna or Marcus | Yes — before write; domain: personal |
| Business decision record | A domain-specific business decision logged | Domain specialist | Yes — before write |
| Lesson learned | Durable insight for one or more specialist agents; extracted to agent_learnings via Nolan; AGENT.md update via separate SOP-015 proposal | Nolan | Yes — before agent_learnings write; separate approval for AGENT.md |
| Project note | Content relevant to an active project; added to project.md or project KB by Marcus | Marcus | Yes — before write |
| Workstream note | Content relevant to a workstream; added via separate proposal per SOP-015 | Kai or domain specialist | Yes — separate SOP-015 proposal required |
| Reference note | Indexed as a future lookup reference; no file move required | Larry | Yes — before indexing |
| Backlog candidate | Registered as a future proposal candidate only after Owner approval | Larry | Yes — registration requires approval |
| Archive | Moved to Archive folder after all references are identified and preserved; formal proposal required | Larry | Yes — formal proposal per EX-6 required |

---

## 6. Decision Rules R1 Through R10

Apply rules in order. A deliverable may satisfy multiple rules. For each satisfied rule, record the candidate destination and surface it to the Owner in Phase 4.

**R1 — Authoritative source protection.**
Condition: The deliverable is the canonical reference for an active governance item, active project, accepted GL, accepted SOP, or canonical process decision.
Action: Propose Authoritative designation to Owner. Owner confirms. Index in place. Do not move, archive, or delete without a new proposal.

**R2 — Supersession.**
Condition: A newer accepted version of the same deliverable exists.
Action: Propose Superseded state for the older version. Preserve the file. Update any references pointing to the older version to point to the newer version. Do not delete the older version.

**R3 — Lessons learned candidate.**
Condition: The deliverable contains a pattern, error, correction, or insight relevant to one or more specialist agents.
Action: Surface to Nolan for agent_learnings extraction. Owner approval required before any write. AGENT.md updates are prepared as separate proposals per SOP-015.

**R4 — Governance reference.**
Condition: The deliverable contains a decision or pattern relevant to the team operating model.
Action: Larry indexes as governance reference. Owner approval required before any GL or SOP update that the deliverable might inform.

**R5 — Personal knowledge candidate.**
Condition: The deliverable contains personal insights, personal decisions, or personal lessons by Owner Walter Kamer.
Action: Surface to Sienna or Penn. Owner approval required before any PKM write.

**R6 — Business knowledge candidate.**
Condition: The deliverable contains domain-specific operational knowledge relevant to Kamer E-commerce or Geldstroom Regie.
Action: Surface to the appropriate domain specialist. Owner approval required before any BKM write.

**R7 — Project note candidate.**
Condition: The deliverable contains information relevant to an active project.
Action: Surface to Marcus. Owner approval required before any write to project.md or project KB.

**R8 — Archive eligible.**
Condition: The deliverable is not authoritative, is not referenced by other active documents, and all references to it have been preserved or are absent.
Action: Prepare formal archive proposal per EX-6. Owner approval required before any file move.

**R9 — Retain in place.**
Condition: The deliverable is authoritative, is referenced by other documents, or has not been fully assessed yet.
Action: No action. Retain in Deliverables folder. Record retain decision in execution report.

**R10 — No action required.**
Condition: The deliverable is a working artifact (superseded draft, intermediate proposal round replaced by a later version) that produced no standalone value.
Action: Mark Superseded. Record in execution report. No further action.

**Default rule:** If no processing rule clearly applies, apply R9 (retain in place). Never archive or delete by default.

---

## 7. Personal Processing Flow

Applies when R5 is satisfied and Owner has approved a PKM write.

1. Identify the personal content: personal decisions, personal insights, personal lessons, or personal reflections by Owner Walter Kamer.
2. Confirm the exact PKM destination file or section (e.g., `PKM/My Life/Key Elements/KE-Finance data.md`, a specific journal entry, or a CRM file).
3. Present to Owner: destination file, content to be extracted, extracting agent.
4. Wait for explicit Owner approval.
5. Penn or Sienna executes the extraction and writes to the confirmed destination.
6. GL-015 routing: domain: personal, source_type: knowledge (or journal if the content is reflective).
7. Retain source deliverable in Deliverables folder. Do not delete or move it.
8. Write execution report per Section 16.

---

## 8. Business Processing Flow

Applies when R6 is satisfied and Owner has approved a BKM write.

1. Identify the business content: operational knowledge, process findings, pricing analysis, domain patterns, or strategic insights.
2. Determine the domain: Kamer E-commerce or Geldstroom Regie.
3. Confirm the exact BKM destination file or section within `Team Knowledge/Kamer E-commerce/` or `Team Knowledge/Geldstroom Regie/`.
4. Present to Owner: domain, destination file, content to be extracted, extracting agent.
5. Wait for explicit Owner approval.
6. Domain specialist executes (Nova, Vera, Sasha, or Zara for Kamer E-commerce; Finn for Geldstroom Regie).
7. GL-015 routing: domain: kamer-ecommerce or geldstroom-regie, source_type: knowledge.
8. Retain source deliverable in Deliverables folder. Do not delete or move it.
9. Write execution report per Section 16.

---

## 9. Governance Processing Flow

Applies when R3 or R4 is satisfied.

1. Identify the governance content type:
   - Lessons learned for one or more specialist agents (R3)
   - Governance reference to index (R4)
   - Content that may inform a GL or SOP update (R4)

2. For lessons learned (R3):
   a. Surface to Nolan with the specific content and the target agent(s).
   b. Wait for Owner approval.
   c. Nolan prepares agent_learnings entries as a proposal document.
   d. The proposal enters the review gate per GL-016 and SOP-016 before being written.
   e. After Owner approval of the proposal, Nolan writes to agent_learnings in the appropriate domain database per GL-015.
   f. AGENT.md updates are prepared as a separate proposal per SOP-015. They require separate Owner approval and are not executed as part of this lifecycle action.

3. For governance references (R4):
   a. Larry indexes the reference.
   b. If the content suggests a GL or SOP update, Larry prepares a separate proposal per SOP-015.
   c. No GL, SOP, or AGENT.md is updated automatically as a result of lifecycle processing.

4. Retain source deliverable in Deliverables folder. Do not delete or move it.
5. Write execution report per Section 16.

---

## 10. Archive and Superseded Handling

### Superseded

A deliverable is marked Superseded when a newer accepted version of the same deliverable exists (R2) or when a deliverable is an intermediate working artifact (R10).

Steps:
1. Confirm the newer version is accepted as Done.
2. Identify all documents that reference the older version.
3. Update those references to point to the newer version, or add a note that the older version is superseded by the newer one.
4. Update the older version's state to Superseded.
5. Do not delete the older version. Retain it in its current location.
6. Write execution report.

### Archiving

A deliverable is archived when it is no longer in active use, is not authoritative, and all references to it have been preserved (R8).

Archiving requires a formal proposal per EX-6 before any file is moved. The proposal must contain:
- Source path (exact current file path)
- Target path (exact archive destination path)
- Reason for archiving
- Reference preservation plan (list of all documents that reference this deliverable, and how references are preserved)
- Rollback or restore plan (how to undo the move if needed)
- Post-check plan (how to verify the archive was successful and all references are intact)

No archive action may be executed without Owner approval of the formal proposal.

After archiving:
- The source file is moved to the Archive folder.
- All references are updated to the new path or annotated with the archive status.
- The deliverable state is updated to Archived.
- An execution report is written.

---

## 11. Authoritative Source Handling

### Designation

A deliverable is designated as Authoritative when it is the canonical reference for an active governance item, project, accepted GL, accepted SOP, or canonical process decision.

Steps to designate:
1. Larry identifies the candidate and confirms the designation basis (which governance item or topic does this deliverable authoritatively define?).
2. Larry presents the designation proposal to Owner: deliverable path, designation basis, protections that will apply.
3. Owner confirms.
4. Larry records the Authoritative designation in the execution report.

Authoritative status cannot be auto-assigned. It requires explicit Owner confirmation.

### Protections

A deliverable designated as Authoritative:
- May not be deleted.
- May not be moved or renamed without a formal proposal and explicit Owner approval.
- May not be archived without a formal proposal specifying why the authoritative reference is no longer needed and what replaces it.
- May not be superseded without Owner approval of the newer version as its replacement.

These protections survive project closure, session boundaries, and agent changes.

### Updating or Superseding an Authoritative Source

If a newer version is prepared and accepted:
1. The newer version enters the review gate per GL-016 and SOP-016.
2. After Owner acceptance of the newer version, the older version's Authoritative status is reassigned to the newer version.
3. The older version's state is updated to Superseded.
4. References are updated to point to the newer version.
5. The older version is retained and not deleted.

---

## 12. Domain Routing

All database writes resulting from lifecycle processing must follow GL-015 (Memory Domain Routing Protocol). This table aligns lifecycle processing destinations with GL-015 routing.

| Content type | Domain | Database | GL-015 source_type |
|---|---|---|---|
| Personal insights, personal decisions | personal | personal.db | knowledge |
| Personal journal reflections | personal | personal.db | journal |
| Kamer E-commerce operational knowledge | kamer-ecommerce | kamer e-commerce.db | knowledge |
| Geldstroom Regie operational knowledge | geldstroom-regie | geldstroom-regie.db | knowledge |
| Governance decisions, team patterns | core | team-knowledge.db | knowledge |
| Lessons learned for a specialist agent | matches agent domain per GL-015 | domain-appropriate database per GL-015 | knowledge |
| Cross-domain content | surface to Owner before any write | Owner decides routing | Owner decides |

If a conflict exists between this table and GL-015, GL-015 takes precedence. No lifecycle processing write may override GL-015 routing rules.

---

## 13. Safeguards Checklist

Run this checklist before executing any processing action and again after execution to confirm no side effects occurred.

**Pre-execution:**

- [ ] Review gate has completed for this deliverable (SOP-016 ran; Owner decision recorded)
- [ ] Owner approval obtained for this specific processing destination
- [ ] Source deliverable path confirmed and recorded
- [ ] Processing destination confirmed (exact file path, database table, or folder path)
- [ ] If file move or archive: all references to the source deliverable have been identified and a preservation plan is in place
- [ ] If database write: domain and source_type confirmed per GL-015
- [ ] If AGENT.md update: a separate proposal has been prepared and approved per SOP-015 (not executing inline)
- [ ] If GL or SOP update: a separate proposal has been prepared and approved per SOP-015 (not executing inline)
- [ ] Cross-domain content: Owner has been informed and has explicitly approved the routing
- [ ] No secrets, credentials, tokens, or API keys are in the processing scope
- [ ] Execution report will be written documenting all actions taken

**Post-execution:**

- [ ] Source deliverable is retained in Deliverables folder (not deleted or moved unless archiving was explicitly approved)
- [ ] Processing destination contains the extracted content as approved
- [ ] No other files were modified beyond the approved scope
- [ ] No database writes occurred beyond the approved write
- [ ] Execution report is written and complete per Section 16

---

## 14. Explicit Rules

The following rules are hard constraints. They apply regardless of context, session, or agent. No exception is permitted without explicit Owner direction.

**EX-1: Review Gate prerequisite.**
Lifecycle processing starts only after the applicable Review Gate has completed per GL-016 and SOP-016 and the deliverable has an Owner acceptance decision. A deliverable without an Owner acceptance decision is not eligible for lifecycle processing, archiving, or knowledge extraction.

**EX-2: Owner approval for each processing destination.**
A deliverable may be processed into PKM, BKM, decision records, lessons learned, project notes, workstream notes, or references only after Owner approval of that specific processing destination. Approval for one destination does not cover other destinations. Each destination requires its own approval.

**EX-3: No database write without Owner approval.**
Writing to agent_learnings, personal.db, team-knowledge.db, kamer e-commerce.db, geldstroom-regie.db, UMC, memory-db, or any other database requires explicit Owner approval before the write executes. This applies regardless of which agent is executing or which routine triggered the lifecycle review.

**EX-4: System file changes require separate proposals.**
Updating AGENT.md files, SOPs, GLs, Workstreams, or CLAUDE.md requires a separate proposal and exact Owner approval per SOP-015. These updates must not happen automatically as part of lifecycle processing. Lifecycle processing may identify the need for such updates, but identification is not authorization.

**EX-5: Lessons learned require separate approval before writing.**
A lesson learned may be proposed and surfaced from a deliverable as part of lifecycle processing. It must not be written to agent_learnings or to any AGENT.md file without explicit Owner approval and the appropriate procedure per SOP-015. Surfacing a lesson learned is not the same as writing it.

**EX-6: Archiving and file moves require a formal proposal.**
Archiving or moving any deliverable — including moving it to an Archive folder, renaming it, or relocating it within the Deliverables structure — requires a formal proposal containing all of the following before any file is moved:
- Source path (exact current file path)
- Target path (exact destination file path)
- Reason (why this deliverable is being moved)
- Reference preservation plan (what documents reference this file and how those references will be preserved)
- Rollback or restore plan (how to undo the move if needed)
- Post-check plan (how to verify the move was successful and references are intact)

No move may be executed without Owner approval of the complete proposal.

---

## 15. Worked Examples

### Example 1: Approved proposal superseded by a later version

**Context:** A GL proposal v01 was reviewed and accepted. Owner then requested amendments. A v02 was prepared, reviewed, accepted, and implemented. v01 is no longer the current version.

**Processing decision:**
- v01 state: Superseded
- v02 state: Accepted as Done, then Authoritative (it is the canonical record of the accepted proposal and implementation)
- Decision rules applied: R2 (Supersession) for v01; R1 (Authoritative source protection) for v02

**Steps executed:**
1. Confirm v02 is accepted as Done.
2. Identify documents referencing v01. Update or annotate those references to point to v02 as the accepted version.
3. Update v01 state to Superseded. Retain v01 file in its current location. Do not delete.
4. Larry proposes Authoritative designation for v02. Owner confirms.
5. Update v02 state to Authoritative. Index v02 as canonical reference.
6. Write execution report: records v01 path (Superseded), v02 path (Authoritative), reference updates made, date.

**No database write. No PKM extraction. No archiving. No AGENT.md update.**

---

### Example 2: Execution report accepted as Done and kept as authoritative source

**Context:** The Core AI Team Audit execution report is accepted as Done. The report is the canonical record of audit findings and actions taken. No knowledge extraction is requested at this time.

**Processing decision:**
- State: Accepted as Done, then Authoritative
- Decision rule applied: R1 (Authoritative source protection)

**Steps executed:**
1. Apply decision rules. R1 applies: the audit execution report is the canonical reference for the Core AI Team Audit.
2. Larry proposes to Owner: "The audit execution report is the canonical reference for the Core AI Team Audit. I propose designating it as Authoritative."
3. Owner confirms.
4. State updated to Authoritative. File stays in Deliverables folder. Not archived. Not moved.
5. Write execution report: records designation, file path, date, basis for Authoritative status.

**No PKM extraction, no database write, no lessons learned extraction (unless Owner separately requests it).**

---

### Example 3: Closure report processed into lessons learned and retained as authoritative source

**Context:** A project closure report contains identifiable patterns relevant to Marcus (project management) and Kai (infrastructure cleanup). The report is accepted as Done. Owner requests lessons learned extraction.

**Processing decision:**
- State: Accepted as Done, then Authoritative and Processed
- Decision rules applied: R1 (Authoritative), R3 (Lessons learned candidate for Marcus and Kai)

**Steps executed:**
1. Apply decision rules. R1 and R3 both apply.
2. Larry proposes Authoritative designation. Owner confirms.
3. Larry identifies lesson candidates and presents to Owner: specific insights, target agents (Marcus, Kai), proposed agent_learnings content.
4. Owner approves lessons learned extraction.
5. Larry briefs Nolan with the specific lessons and target agents.
6. Nolan prepares agent_learnings proposal entries as a proposal document.
7. Nolan's proposal enters the review gate per GL-016 and SOP-016 before being written.
8. Owner approves the proposal.
9. Nolan writes to agent_learnings in the appropriate domain database per GL-015.
10. AGENT.md updates for Marcus and Kai are prepared as separate proposals per SOP-015. Owner reviews and approves each separately. Executed after approval.
11. Source closure report retained. State updated to Authoritative and Processed.
12. Write execution report: records all actions taken, agent_learnings write confirmation, paths to AGENT.md update proposals, date.

**Source file not deleted. Two separate approval gates: one for agent_learnings, one per AGENT.md file updated.**

---

### Example 4: Business deliverable processed into Kamer E-commerce BKM

**Context:** Nova has delivered a pricing analysis report for Kamer E-commerce. The report is accepted as Done. Owner approves knowledge extraction to the Kamer E-commerce knowledge base.

**Processing decision:**
- State: Accepted as Done, then Processed
- Decision rule applied: R6 (Business knowledge candidate, domain: kamer-ecommerce)

**Steps executed:**
1. Apply decision rules. R6 applies.
2. Larry proposes to Owner: "This pricing analysis contains operational knowledge relevant to the Kamer E-commerce knowledge base. Proposed destination: [specific file in Team Knowledge/Kamer E-commerce/]. Extracting agent: Nova."
3. Owner approves.
4. Nova extracts and writes the relevant knowledge to the designated KB file.
5. GL-015 routing: domain: kamer-ecommerce, source_type: knowledge.
6. Source report retained in Deliverables folder. State updated to Processed.
7. Write execution report: records destination file, content extracted, date, extracting agent, GL-015 routing applied.

**Source file not deleted or moved.**

---

### Example 5: Personal deliverable processed into PKM

**Context:** A triage report on Owner Walter Kamer's personal finance goals contains personal decisions and insights. The report is accepted as Done. Owner approves extraction to PKM.

**Processing decision:**
- State: Accepted as Done, then Processed
- Decision rule applied: R5 (Personal knowledge candidate, domain: personal)

**Steps executed:**
1. Apply decision rules. R5 applies.
2. Larry proposes to Owner: "This triage report contains personal decisions relevant to PKM. Proposed destination: [specific section or file in PKM/My Life/Key Elements/]. Extracting agent: Sienna."
3. Owner approves.
4. Sienna extracts the personal decisions and writes to the designated PKM file.
5. GL-015 routing: domain: personal, source_type: knowledge.
6. Source triage report retained in Deliverables folder. State updated to Processed.
7. Write execution report: records destination file, content extracted, date, extracting agent, GL-015 routing applied.

**Source file not deleted or moved.**

---

## 16. Execution Report Requirements

Every lifecycle processing action that changes a deliverable's state, performs a write, or moves a file must be documented in an execution report. The execution report is itself a deliverable and enters the review gate per GL-016 and SOP-016 before being accepted as Done.

An execution report for a lifecycle action must contain:

1. **Deliverable path** — exact current file path of the deliverable that was processed
2. **State before processing** — the lifecycle state before this action
3. **State after processing** — the lifecycle state(s) after this action
4. **Processing actions taken** — list each action taken; one action per line
5. **Processing destinations** — exact file path or database table for each action
6. **Decision rules applied** — list each rule (R1 through R10) that triggered an action
7. **Owner approval reference** — session date and the approval statement or confirmation received
8. **Executing agent** — which agent executed each action
9. **Date executed** — the date each action was taken
10. **References updated** — list all documents whose references were updated (if any file moves or supersessions occurred)
11. **Post-check result** — confirmation that the source deliverable is retained, no unintended side effects occurred, and the safeguards checklist passed
12. **Next steps** — any pending actions that were identified but not yet executed (e.g., pending AGENT.md proposal, pending SOP-015 proposal)

---

## 17. Owner Decision Options for Individual Lifecycle Actions

When a processing candidate is presented to the Owner for a specific deliverable, the Owner may choose:

| Option | Action |
|---|---|
| Approve this destination | Processing executes for this destination only |
| Approve all proposed destinations | All candidates in the current proposal execute |
| Approve some destinations | Specify which; remaining candidates are held pending further review |
| Defer this destination | Destination is noted but not acted on; revisit in a future session |
| Reject this destination | Destination is not processed; recorded in execution report as not applicable |
| Request amendments to the proposal | Revised proposal prepared; original proposal is not executed |

[END SOP-017 FILE CONTENT]

---

## 5. Exact sop-index.md Update Text

The following row is to be appended to the SOP table in `Team Knowledge/Core/SOPs/SOP-index.md` immediately after the SOP-016 row, if this proposal is approved. No other rows in SOP-index.md are to be modified.

Row to append:

```
| Deliverable Lifecycle, Knowledge Processing, and Archiving Procedure | `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md` | Step-by-step lifecycle processing procedure — trigger moments, decision rules R1–R10, processing destination catalog, personal/business/governance flows, safeguards checklist, six explicit rules, worked examples |
```

---

## 6. Pairing Notes

This proposal is paired with GL-017 proposal (`deliverable-lifecycle-gl-proposal-v01.md`).

**Separation of concerns:**
- GL-017 defines principles: lifecycle states, core principles P1 through P12, authoritative source protections, and cross-domain routing principles.
- SOP-017 defines procedures: trigger moments, lifecycle decision workflow phases, processing destination catalog, decision rules R1 through R10, personal/business/governance processing flows, archive and superseded handling, authoritative source handling, domain routing table, safeguards checklist, six explicit rules, worked examples, and execution report requirements.
- The two documents do not duplicate each other. The SOP references the GL but does not restate the GL's principles or states.

**Dependency on GL-017:**
SOP-017 requires GL-017 to exist before SOP-017 is implemented. SOP-017 references GL-017 Section 3 for the authoritative list of lifecycle states and GL-017 Section 4 for the core principles that govern all lifecycle processing. Without GL-017, these references are unresolved.

**Recommended execution order:**
GL-017 must be implemented and post-checked before SOP-017 is implemented. If GL-017 post-checks fail, SOP-017 must not be implemented until GL-017 is corrected and confirmed. This is the same pattern as GL-016 and SOP-016.

**Cross-references if both are approved:**
- SOP-017 Section 1 references GL-017 as the upstream principle.
- GL-017 Section 5 references SOP-017 as the operational counterpart (anticipatory reference in GL-017 that resolves when SOP-017 is created).

---

## 7. Implementation Scope

If this proposal is approved (and GL-017 post-checks have been confirmed), exactly the following actions are in scope:

1. Create `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md` with the exact content from Section 4.
2. Append the SOP-017 row to `Team Knowledge/Core/SOPs/SOP-index.md` per Section 5.
3. Read back both files to confirm contents match the approved proposal exactly.
4. Report post-check result to Owner.

No other actions are in scope.

---

## 8. Explicit Exclusions

The following are explicitly excluded from SOP-017 implementation:

- Implementing GL-017 (must already be complete before SOP-017 is implemented)
- Updating GL-016
- Updating SOP-016
- Updating GL-015
- Updating SOP-015
- Updating CLAUDE.md
- Writing to any database (personal.db, team-knowledge.db, kamer e-commerce.db, geldstroom-regie.db, UMC, memory-db)
- Updating any AGENT.md file
- Processing any existing deliverable into PKM or BKM as part of this implementation
- Archiving any existing deliverable
- Creating any backlog item
- Writing team_tasks or team_log entries
- Executing any lifecycle processing action on any deliverable as part of SOP-017 implementation itself

---

## 9. Post-Check Plan

After SOP-017 is implemented, the following checks are performed before declaring implementation complete:

1. Read back `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md`. Confirm all sections, decision rules, worked examples, explicit rules, and the processing destination catalog match the approved content in Section 4 exactly.
2. Read back `Team Knowledge/Core/SOPs/SOP-index.md`. Confirm the SOP-017 row is present, correctly formatted, and no other rows were modified.
3. Confirm no other files were modified during implementation.
4. Confirm no database writes occurred.
5. Report post-check result to Owner: file path, SOP number, index row, confirmation of no side effects.

---

## 10. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| SOP-017 number taken between proposal preparation and implementation | Re-confirm SOP-index.md immediately before file creation during implementation |
| SOP-017 implemented before GL-017 post-checks are confirmed | Implementation scope and pairing notes both state this explicitly. Confirm GL-017 post-check report before proceeding |
| SOP content overlaps with GL-017 principle content | SOP-017 references GL-017 for states and principles; it does not restate them. Reviewer should flag any principle-level content found in the SOP text before approving |
| Worked examples interpreted as authorization to execute those examples | Worked examples in Section 15 are illustrative only. They do not authorize any processing action on any existing deliverable |
| Optional future updates (GL-016, SOP-016) executed automatically | Section 8 explicitly marks these as excluded |

---

## 11. Owner Decision Options

| Option | Action |
|---|---|
| **A** | Approve GL-017 implementation only. SOP-017 reviewed and decided separately at a later time. |
| **B** | Approve paired implementation. GL-017 implemented first. SOP-017 implemented after GL-017 post-checks are confirmed to Owner. |
| **C** | Request amendments. Specify which sections require changes. A v02 will be prepared per SOP-015. |
| **D** | Defer. |
| **E** | Reject. |

---

*Delivered on: 2026-06-04*
*Delivered at: Deliverables/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage/deliverable-lifecycle-sop-proposal-v01.md*
