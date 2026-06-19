# Proposal: SOP-017 — Deliverable Lifecycle, Knowledge Processing, and Archiving Procedure

**File:** `Deliverables/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage/deliverable-lifecycle-sop-proposal-v02.md`
**Date:** 2026-06-05
**Prepared by:** Larry, Team Orchestrator
**Proposal version:** v02
**Supersedes:** `deliverable-lifecycle-sop-proposal-v01.md`
**Status:** Proposal-only — awaiting Owner approval

**Governance:** This document is read-only. No SOP file creation, index update, or any system change may be executed without explicit Owner Walter Kamer approval of this proposal. This is a proposal document only.

---

## Revision Notes: v01 to v02

| # | Amendment | Sections affected in SOP content |
|---|---|---|
| 1 | Lifecycle state model fixed throughout. All worked examples updated to use primary state + lifecycle markers. No more combined state descriptions such as "Authoritative and Processed". State transitions recorded in execution reports only (see Amendment 3). | Section 1; Phase 6 Step 15; Section 11; Section 15 (all five examples) |
| 2 | Scope tightened. SOP now explicitly references GL-017 Section 3.2 for post-acceptance primary states and Section 3.3 for markers. Pre-acceptance states are not referenced as SOP-017 scope. | Section 1 |
| 3 | Reference updates and state updates clarified as writes. Superseded handling rewritten: state transitions recorded in execution report only; reference identification recorded in execution report; reference updates require explicit Owner approval per file; system file updates require SOP-015 proposal. Same rule applied to archive post-handling and authoritative source supersession. | Section 10 (complete rewrite); Section 11 (supersession sub-section); Decision Rule R2 revised |
| 4 | Anti-recursion rule added as EX-7. Phase 6 Step 17 updated. Section 16 updated with anti-recursion note. | EX-7 new; Phase 6 Step 17; Section 16 |
| 5 | Decision packet trigger rule mapping corrected. Decision packets now mapped to R4 (governance), R5 (personal), R6 (business) as applicable. | Section 3 trigger table row |
| 6 | Cross-domain tightened. One-home-domain rule added to personal and business processing flows. Phase 3 strengthened. Decision Rule R1 action updated. | Section 7; Section 8; Phase 3 |
| 7 | Indexing and reference notes clarified. Governance reference and Reference note entries in processing catalog updated: execution report is the default record; no separate file write without Owner approval of exact target. Governance processing flow step 3a updated. Decision Rule R4 action updated. | Section 5; Section 9 step 3a; Decision Rule R4 |
| 8 | Index row format verified. Verification note added to Section 5. Risk entry added. | Section 5; Section 10 |

---

## 1. Confirmed SOP Number

**SOP-017**

Confirmed from `Team Knowledge/Core/SOPs/SOP-index.md` on 2026-06-04. The current highest SOP number is SOP-016. SOP-017 is the next available number.

> **Implementation note:** Re-confirm `SOP-index.md` immediately before file creation at the time of implementation to ensure SOP-017 has not been taken.

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
**Created:** 2026-06-05

---

## 1. Purpose and Relationship to GL-017

This SOP defines how to execute lifecycle decisions for myPKA AI team deliverables. It is the operational counterpart to GL-017 (Deliverable Lifecycle, Knowledge Processing, and Archiving), which defines the lifecycle principles, the post-acceptance primary state model, and the lifecycle marker model.

This SOP defines procedures only. It does not redefine the lifecycle state model or core principles established in GL-017. Readers should consult:
- GL-017 Section 3.2 for the authoritative list of post-acceptance primary states
- GL-017 Section 3.3 for the authoritative list of lifecycle markers
- GL-017 Section 4 for the core principles (P1 through P13) governing all lifecycle processing

A deliverable holds exactly one primary state at any time. Lifecycle markers are additive and coexist with the primary state. Assigning a marker does not change the primary state. All state transitions and marker assignments are recorded in the execution report; they are not written into source deliverable files unless Owner explicitly approves a visible status note in the source file.

This SOP is downstream of GL-016 (Review Gate for Governance-Relevant Deliverables) and SOP-016 (Review Gate Procedure for Governance-Relevant Deliverables). The review gate must complete before this SOP activates.

---

## 2. Prerequisites

This SOP may not be executed unless all of the following conditions are met:

1. The deliverable has been submitted to and passed the review gate per GL-016 and SOP-016.
2. The Owner has made an explicit acceptance decision for the deliverable.
3. The deliverable primary state has been confirmed as Accepted as Done per GL-017 Section 3.2.

If any condition is not met: stop. Surface the missing condition to the Owner. Do not proceed with any processing, archiving, or knowledge extraction action.

---

## 3. Trigger Moments

This SOP is activated at the following moments. Activation surfaces a processing decision to the orchestrator and Owner. It does not automatically initiate processing.

| Trigger | What to do |
|---|---|
| Deliverable accepted as Done (primary trigger) | Apply decision rules R1 through R10. Present candidates to Owner. Wait for approval. |
| Newer version of a deliverable accepted as Done | Previous version is a candidate for Superseded primary state. Apply R2. Present to Owner. |
| Execution report accepted as Done | Apply decision rules. Common outcome: Indexed marker (R4) or retain in place (R9). Apply EX-7 to determine if a further execution report is required. |
| Closure report accepted as Done | Apply decision rules. Common outcomes: Authoritative marker (R1) and Lessons learned candidate (R3). |
| Triage report accepted as Done | Apply decision rules. Common outcome: Authoritative marker (R1) as the initiating reference for its initiative. |
| Decision packet accepted as Done | Apply decision rules. Common outcomes: R4 (governance decision or reference), R5 (personal decision record or personal knowledge), R6 (business decision record or business knowledge). Apply whichever rules the content satisfies. |
| Owner requests lifecycle review of a specific deliverable | Apply decision rules R1 through R10. Present candidates. Wait for approval. |

---

## 4. Lifecycle Decision Workflow

Execute the following phases in order. Do not skip phases. Do not combine phases.

### Phase 1: Prerequisite Verification

**Step 1.** Confirm the deliverable has passed the review gate per SOP-016. If not, stop and surface to Owner.

**Step 2.** Confirm the Owner has made an acceptance decision. If not, stop and surface to Owner.

**Step 3.** Record the deliverable path, domain, type, and current primary state.

### Phase 2: Rule Application

**Step 4.** Apply decision rules R1 through R10 from Section 6 in order. A deliverable may satisfy multiple rules.

**Step 5.** Record which rules apply and the candidate processing destination or marker assignment for each.

### Phase 3: Cross-Domain Check

**Step 6.** Review all candidate destinations. If any candidate destination involves content relevant to more than one domain (personal and business, or two business domains), flag it. One domain is selected as the canonical home before any routing proposal is made. Other domains receive references to the home location, not copies.

**Step 7.** For cross-domain content: surface to Owner with the full routing proposal, identifying the proposed home domain and the reference plan for other domains. Apply GL-015 routing rules. Apply SSOT Golden Rule: one home, references only. Do not propose second-domain extraction without explicit Owner approval for the exception.

### Phase 4: Owner Proposal

**Step 8.** Present all processing destination candidates and marker assignment candidates to the Owner. For each candidate, state:
- The rule that triggered it (R1 through R10)
- The exact destination (file path, database, or folder path) for any write action
- The marker to be assigned (if applicable)
- The agent who would execute any write
- The expected action (write, record in execution report, mark state, move, extract)

For lifecycle execution reports that are accepted as Done, apply EX-7 before presenting candidates.

**Step 9.** Wait for explicit Owner approval for each candidate. Unapproved candidates are not executed.

### Phase 5: Execution

**Step 10.** Execute only the Owner-approved processing destinations and marker assignments.

**Step 11.** Follow GL-015 for all database writes. Confirm domain and source_type before writing.

**Step 12.** Follow SOP-015 for any new GL, SOP, Workstream, or AGENT.md updates that result from lifecycle processing. These are separate proposals requiring separate Owner approval. They are not executed inline as part of lifecycle processing.

**Step 13.** Retain the source deliverable in its current Deliverables folder location unless archiving was explicitly approved and a formal proposal was prepared per EX-6.

**Step 14.** Run the Safeguards Checklist from Section 13 before and after execution.

### Phase 6: State Recording and Reporting

**Step 15.** Record the deliverable's primary state (which may remain as Accepted as Done) and assign applicable lifecycle markers per GL-017 Section 3.3. Record both in the execution report. Do not write state or marker designations into the source deliverable file unless Owner explicitly approves a visible status note in that file.

**Step 16.** Write an execution report per the requirements in Section 16.

**Step 17.** If the execution report itself is a governance-relevant deliverable, submit it to the review gate per GL-016 and SOP-016 before accepting it as Done. After it is accepted as Done, apply EX-7 to determine whether a further execution report is required for that report.

---

## 5. Processing Destination Catalog

Each accepted deliverable is assessed against the following destinations. A deliverable may have multiple applicable destinations. Each destination requires a separate Owner-approved action.

| Destination | Description | Executing agent | Owner approval required |
|---|---|---|---|
| Authoritative marker | Deliverable designated as canonical reference; Authoritative marker assigned; deliverable stays in Deliverables folder; not moved or modified | Larry proposes; Owner confirms | Yes — confirmation of marker assignment |
| PKM — Personal Knowledge Management | Personal decisions, personal insights, or personal lessons extracted and written to PKM | Penn or Sienna | Yes — before any write; home domain check required |
| BKM — Kamer E-commerce | Business knowledge for Kamer E-commerce domain extracted and written to KB | Nova, Vera, Sasha, or Zara | Yes — before any write; home domain check required |
| BKM — Geldstroom Regie | Business knowledge for Geldstroom Regie domain extracted and written to KB | Finn | Yes — before any write; home domain check required |
| Governance reference | Governance decisions or team-level patterns recorded in the execution report; Indexed marker assigned; no separate file write unless Owner approves an exact target | Larry | Yes — before any write beyond the execution report |
| Personal decision record | A specific Owner decision identified and proposed for logging; write requires Owner approval of the exact target | Sienna or Marcus | Yes — before write; domain: personal |
| Business decision record | A domain-specific business decision identified and proposed for logging; write requires Owner approval of the exact target | Domain specialist | Yes — before write |
| Lesson learned | Durable insight for one or more specialist agents; proposed to Nolan for agent_learnings extraction; write requires Owner approval; AGENT.md update via separate SOP-015 proposal | Nolan | Yes — before agent_learnings write; separate approval for AGENT.md |
| Project note | Content relevant to an active project; proposed to Marcus for write to project.md or project KB | Marcus | Yes — before write |
| Workstream note | Content relevant to a workstream; added via separate SOP-015 proposal | Kai or domain specialist | Yes — separate SOP-015 proposal required |
| Reference note | Identified as a future lookup reference; recorded in the execution report; Indexed marker assigned; no separate file write unless Owner approves an exact target | Larry | Yes — before any write beyond the execution report |
| Backlog candidate | Registered as a future proposal candidate only after Owner approval | Larry | Yes — registration requires approval |
| Archive | Moved to Archive folder after all references are identified and recorded; formal proposal required per EX-6 | Larry | Yes — formal proposal per EX-6 required before any file move |

---

## 6. Decision Rules R1 Through R10

Apply rules in order. A deliverable may satisfy multiple rules. For each satisfied rule, record the candidate destination or marker assignment and surface it to the Owner in Phase 4.

**R1 — Authoritative source protection.**
Condition: The deliverable is the canonical reference for an active governance item, active project, accepted GL, accepted SOP, or canonical process decision.
Action: Propose Authoritative marker assignment to Owner. Owner confirms. Record the marker assignment in the execution report. The execution report is the governance record; no separate index file is written without Owner approval of the exact target. Do not move, archive, or delete this deliverable without a new formal proposal.

**R2 — Supersession.**
Condition: A newer accepted version of the same deliverable exists.
Action: Record the Superseded primary state transition in the execution report for the older version. Do not write to the older version source file. Identify all documents that reference the older version and record this list in the execution report. Assign the Reference Preserved marker. Present reference update candidates to Owner per file; do not update any reference without explicit Owner approval. System file reference updates require a separate SOP-015 proposal. Do not delete the older version.

**R3 — Lessons learned candidate.**
Condition: The deliverable contains a pattern, error, correction, or insight relevant to one or more specialist agents.
Action: Surface to Nolan for agent_learnings extraction proposal. Owner approval required before any write. AGENT.md updates are prepared as separate proposals per SOP-015.

**R4 — Governance reference.**
Condition: The deliverable contains a decision or pattern relevant to the team operating model.
Action: Record the governance reference in the execution report. Assign the Indexed marker. No separate file write occurs without Owner approval of the exact target file and content. If the content suggests a GL or SOP update, prepare a separate proposal per SOP-015.

**R5 — Personal knowledge candidate.**
Condition: The deliverable contains personal insights, personal decisions, or personal lessons by Owner Walter Kamer.
Action: Surface to Sienna or Penn with the proposed home domain (personal) and content to be extracted. Owner approval required before any PKM write. Apply one-home-domain rule: if content is also relevant to a business domain, surface the cross-domain question to Owner first.

**R6 — Business knowledge candidate.**
Condition: The deliverable contains domain-specific operational knowledge relevant to Kamer E-commerce or Geldstroom Regie.
Action: Surface to the appropriate domain specialist with the proposed home domain and content to be extracted. Owner approval required before any BKM write. Apply one-home-domain rule: if content is also relevant to another domain, surface the cross-domain question to Owner first.

**R7 — Project note candidate.**
Condition: The deliverable contains information relevant to an active project.
Action: Surface to Marcus with the proposed destination (project.md or project KB file and section). Owner approval required before any write.

**R8 — Archive eligible.**
Condition: The deliverable is not carrying the Authoritative marker, is not referenced by other active documents, and all references to it have been identified and preserved or are absent.
Action: Prepare formal archive proposal per EX-6. Owner approval required before any file move.

**R9 — Retain in place.**
Condition: The deliverable carries the Authoritative marker, is referenced by other documents, or has not been fully assessed yet.
Action: No action. Retain in Deliverables folder. Record retain decision and basis in execution report.

**R10 — No action required.**
Condition: The deliverable is a working artifact (superseded draft, intermediate proposal round replaced by a later version) that produced no standalone value.
Action: Record the Superseded primary state transition in the execution report. Do not write to the source file. No further action.

**Default rule:** If no processing rule clearly applies, apply R9 (retain in place). Never archive or delete by default.

---

## 7. Personal Processing Flow

Applies when R5 is satisfied and Owner has approved a PKM write.

1. Identify the personal content: personal decisions, personal insights, personal lessons, or personal reflections by Owner Walter Kamer.
2. Apply the one-home-domain rule: if the content is also relevant to a business domain, surface the cross-domain question to Owner before proceeding. One domain is the canonical home. Other domains receive a reference to the home location, not a copy. Do not proceed to step 3 until the home domain is confirmed as personal.
3. Confirm the exact PKM destination file or section (for example `PKM/My Life/Key Elements/KE-Finance data.md`, a specific journal entry, or a CRM file).
4. Present to Owner: proposed home domain (personal), destination file, content to be extracted, extracting agent.
5. Wait for explicit Owner approval.
6. Penn or Sienna executes the extraction and writes to the confirmed destination.
7. GL-015 routing: domain: personal, source_type: knowledge (or journal if the content is reflective).
8. Retain source deliverable in Deliverables folder. Do not delete or move it.
9. Assign Knowledge Extracted marker to source deliverable. Record in execution report.
10. Write execution report per Section 16.

---

## 8. Business Processing Flow

Applies when R6 is satisfied and Owner has approved a BKM write.

1. Identify the business content: operational knowledge, process findings, pricing analysis, domain patterns, or strategic insights.
2. Determine the home domain: Kamer E-commerce or Geldstroom Regie.
3. Apply the one-home-domain rule: if the content is also relevant to the personal domain or to the other business domain, surface the cross-domain question to Owner before proceeding. One domain is the canonical home. Other domains receive a reference, not a copy. Do not proceed to step 4 until the home domain is confirmed.
4. Confirm the exact BKM destination file or section within `Team Knowledge/Kamer E-commerce/` or `Team Knowledge/Geldstroom Regie/`.
5. Present to Owner: home domain, destination file, content to be extracted, extracting agent.
6. Wait for explicit Owner approval.
7. Domain specialist executes (Nova, Vera, Sasha, or Zara for Kamer E-commerce; Finn for Geldstroom Regie).
8. GL-015 routing: domain: kamer-ecommerce or geldstroom-regie, source_type: knowledge.
9. Retain source deliverable in Deliverables folder. Do not delete or move it.
10. Assign Knowledge Extracted marker to source deliverable. Record in execution report.
11. Write execution report per Section 16.

---

## 9. Governance Processing Flow

Applies when R3 or R4 is satisfied.

1. Identify the governance content type:
   - Lessons learned for one or more specialist agents (R3)
   - Governance reference to record (R4)
   - Content that may inform a GL or SOP update (R4)

2. For lessons learned (R3):
   a. Surface to Nolan with the specific content and the target agent(s).
   b. Wait for Owner approval.
   c. Nolan prepares agent_learnings entries as a proposal document.
   d. The proposal enters the review gate per GL-016 and SOP-016 before being written.
   e. After Owner approval of the proposal, Nolan writes to agent_learnings in the appropriate domain database per GL-015.
   f. AGENT.md updates are prepared as a separate proposal per SOP-015. They require separate Owner approval and are not executed as part of this lifecycle action.

3. For governance references (R4):
   a. Larry records the governance reference in the execution report. The execution report is the default governance record. No separate index file or reference registry write occurs without Owner approval of the exact target file and content. If Owner approves a separate write, specify the exact target before executing.
   b. Assign the Indexed marker to the source deliverable. Record in execution report.
   c. If the content suggests a GL or SOP update, Larry prepares a separate proposal per SOP-015. No GL, SOP, or AGENT.md is updated automatically.

4. Retain source deliverable in Deliverables folder. Do not delete or move it.
5. Write execution report per Section 16.

---

## 10. Archive and Superseded Handling

### Superseded

A deliverable receives the Superseded primary state when a newer accepted version of the same deliverable exists (R2) or when a deliverable is an intermediate working artifact with no standalone value (R10).

Steps:

1. Confirm the newer version is accepted as Done.
2. Record the Superseded primary state transition in the execution report for the older version. This is the authoritative governance record of the transition. Do not write to the older version source file unless Owner explicitly approves a visible status note in that file.
3. Identify all documents that reference the older version. Record this identification list in the execution report. Assign the Reference Preserved marker to the older version. Record in execution report.
4. Present reference update candidates to Owner: for each document that references the older version, state the file, the current reference text, and the proposed change. Wait for explicit Owner approval per file.
5. For each Owner-approved reference update:
   - If the target file is a system file (GL, SOP, Workstream, AGENT.md, CLAUDE.md): prepare a separate proposal per SOP-015 before executing. Do not update system file references inline.
   - If the target file is a non-system file (project.md, notes, deliverable, etc.): execute the approved update.
6. If Owner does not approve reference updates at this time: record in the execution report that references were identified but updates are pending Owner decision.
7. Retain the older version in its current location. Do not delete.
8. Write execution report documenting: primary state transition recorded, reference identification list, approved reference updates executed (if any), pending reference updates (if any), marker assignments.

### Archiving

A deliverable receives the Archived primary state when it is no longer in active use, does not carry the Authoritative marker, and all references to it have been identified (R8).

Archiving requires a formal proposal per EX-6 before any file is moved. The proposal must contain:
- Source path (exact current file path)
- Target path (exact archive destination path)
- Reason for archiving
- Reference preservation plan (list of all documents that reference this deliverable and how references will be preserved or updated)
- Rollback or restore plan (how to undo the move if needed)
- Post-check plan (how to verify the archive was successful and all references are intact)

No archive action may be executed without Owner approval of the complete formal proposal.

After the archive move is executed:
- Record the Archived primary state transition in the execution report. Do not write to the source file; the execution report is the governance record.
- Reference updates in other files follow the same rules as Superseded handling: explicit Owner approval per file; system file updates require SOP-015 proposal.
- Write execution report documenting all actions.

---

## 11. Authoritative Source Handling

### Designation

A deliverable receives the Authoritative marker when it is the canonical reference for an active governance item, project, accepted GL, accepted SOP, or canonical process decision.

Steps to designate:

1. Larry identifies the candidate and confirms the designation basis (which governance item or topic does this deliverable authoritatively define?).
2. Larry presents the proposal to Owner: deliverable path, designation basis, protections that will apply.
3. Owner confirms.
4. Larry assigns the Authoritative marker and records the designation in the execution report. The execution report is the governance record of the marker assignment. No visible marker is written to the source deliverable file unless Owner explicitly approves a visible status note.

The Authoritative marker cannot be auto-assigned. It requires explicit Owner confirmation.

### Protections

A deliverable carrying the Authoritative marker:
- May not be deleted.
- May not be moved or renamed without a formal proposal and explicit Owner approval.
- May not be archived without a formal proposal specifying why the authoritative reference is no longer needed and what replaces it.
- May not have its Authoritative marker removed without Owner approval of the newer version as its replacement.

These protections survive project closure, session boundaries, and agent changes.

### Transferring the Authoritative Marker to a Newer Version

If a newer version is prepared and accepted:

1. The newer version enters the review gate per GL-016 and SOP-016.
2. After Owner acceptance of the newer version, Larry proposes to Owner: transfer the Authoritative marker from the older version to the newer version.
3. Owner confirms the transfer.
4. Larry records the transfer in the execution report: older version loses Authoritative marker (primary state transitions to Superseded); newer version receives Authoritative marker (primary state is Accepted as Done). Both changes recorded in execution report. No write to either source file without Owner approval of a visible status note.
5. Larry identifies documents referencing the older version and presents reference update candidates to Owner. Reference updates follow the same rules as Superseded handling in Section 10.
6. The older version is retained and not deleted.

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
| Cross-domain content | surface to Owner; one home domain selected | home domain database per GL-015 | Owner decides |

If a conflict exists between this table and GL-015, GL-015 takes precedence. No lifecycle processing write may override GL-015 routing rules.

---

## 13. Safeguards Checklist

Run this checklist before executing any processing action and again after execution to confirm no side effects occurred.

**Pre-execution:**

- [ ] Review gate has completed for this deliverable (SOP-016 ran; Owner decision recorded)
- [ ] Owner approval obtained for this specific processing destination or marker assignment
- [ ] Source deliverable path confirmed and recorded
- [ ] Processing destination confirmed (exact file path, database table, or folder path) for any write action
- [ ] If file move or archive: all references to the source deliverable have been identified and a preservation plan is confirmed; formal proposal per EX-6 approved
- [ ] If database write: domain and source_type confirmed per GL-015
- [ ] If AGENT.md update: a separate proposal has been prepared and approved per SOP-015 (not executing inline)
- [ ] If GL or SOP update: a separate proposal has been prepared and approved per SOP-015 (not executing inline)
- [ ] Cross-domain content: home domain confirmed; Owner has explicitly approved routing; no second-domain extraction without exception approval
- [ ] No secrets, credentials, tokens, or API keys are in the processing scope
- [ ] State transition or marker assignment: will be recorded in execution report only; no write to source file without Owner approval of a visible status note
- [ ] Reference updates planned: each target file has Owner approval; system file updates have SOP-015 proposals ready

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
Archiving or moving any deliverable requires a formal proposal containing all of the following before any file is moved:
- Source path (exact current file path)
- Target path (exact destination file path)
- Reason (why this deliverable is being moved)
- Reference preservation plan (what documents reference this file and how those references will be preserved)
- Rollback or restore plan (how to undo the move if needed)
- Post-check plan (how to verify the move was successful and references are intact)

No move may be executed without Owner approval of the complete proposal.

**EX-7: Anti-recursion rule for lifecycle execution reports.**
A lifecycle execution report that is accepted as Done receives a lightweight lifecycle decision by default. The default decision is: primary state Accepted as Done, Indexed marker assigned (the report is the governance record for its own lifecycle action), no further action required. If this is the decision and no additional write, move, extraction, archive, reference update, or system change is requested or approved, no new lifecycle execution report is required for this report. A new lifecycle execution report is required only when a further lifecycle action on this report changes its primary state, writes content to PKM/BKM/a database, updates references in other files, moves or archives the report, or performs approved extraction. This rule prevents infinite regress of execution reports generating further execution reports.

---

## 15. Worked Examples

Worked examples are illustrative only. They do not authorize any processing action on any existing deliverable.

### Example 1: Approved proposal superseded by a later version

**Context:** A GL proposal v01 was reviewed and accepted. Owner then requested amendments. A v02 was prepared, reviewed, accepted, and implemented. v01 is no longer the current version.

**Processing decision:**
- v01 primary state: Superseded; Marker: Reference Preserved
- v02 primary state: Accepted as Done; Marker: Authoritative
- Decision rules applied: R2 (Supersession) for v01; R1 (Authoritative marker) for v02

**Steps executed:**
1. Confirm v02 is accepted as Done.
2. Record v01 primary state as Superseded in the execution report. Do not write to v01 source file. Assign Reference Preserved marker to v01. Record in execution report.
3. Identify documents referencing v01. Record identification list in execution report.
4. Present reference update candidates to Owner per file. Wait for explicit approval.
5. For each Owner-approved update: if target is a system file, prepare SOP-015 proposal. If target is a non-system file, execute the update.
6. Larry proposes Authoritative marker for v02 to Owner. Owner confirms.
7. Assign Authoritative marker to v02. Record in execution report. The execution report is the governance record of both marker assignments.
8. Write execution report: v01 path (primary state: Superseded, Marker: Reference Preserved), v02 path (primary state: Accepted as Done, Marker: Authoritative), reference identification list, approved/pending reference updates, date.

**No database write. No PKM extraction. No archiving. No AGENT.md update. No write to any source file unless Owner approved a visible status note.**

---

### Example 2: Execution report accepted as Done and kept as authoritative source

**Context:** The Core AI Team Audit execution report is accepted as Done. The report is the canonical record of audit findings and actions taken. No knowledge extraction is requested at this time.

**Processing decision:**
- Primary state: Accepted as Done; Marker: Authoritative
- Decision rule applied: R1 (Authoritative marker)

**Steps executed:**
1. Apply decision rules. R1 applies: the audit execution report is the canonical reference for the Core AI Team Audit.
2. Larry proposes to Owner: "The audit execution report is the canonical reference for the Core AI Team Audit. I propose assigning the Authoritative marker."
3. Owner confirms.
4. Assign Authoritative marker. Record in execution report: path, marker assignment basis, date.
5. File stays in Deliverables folder. Not archived. Not moved. No write to source file.
6. Apply EX-7: this execution report is now accepted as Done. Default decision: Indexed marker, no further action. No new execution report required.

**No PKM extraction. No database write. No lessons learned extraction unless Owner separately requests it.**

---

### Example 3: Closure report processed into lessons learned and retained as authoritative source

**Context:** A project closure report contains identifiable patterns relevant to Marcus (project management) and Kai (infrastructure cleanup). The report is accepted as Done. Owner requests lessons learned extraction.

**Processing decision:**
- Primary state: Accepted as Done
- Markers: Authoritative; Knowledge Extracted (agent_learnings, session 2026-06-05)
- Decision rules applied: R1 (Authoritative marker); R3 (Lessons learned candidate for Marcus and Kai)

**Steps executed:**
1. Apply decision rules. R1 and R3 both apply.
2. Larry proposes Authoritative marker assignment to Owner. Owner confirms. Record in execution report. No write to source file.
3. Larry identifies lesson candidates and presents to Owner: specific insights, target agents (Marcus, Kai), proposed agent_learnings content.
4. Owner approves lessons learned extraction.
5. Larry briefs Nolan with the specific lessons and target agents.
6. Nolan prepares agent_learnings entries as a proposal document.
7. Nolan's proposal enters the review gate per GL-016 and SOP-016 before being written.
8. Owner approves the proposal.
9. Nolan writes to agent_learnings in the appropriate domain database per GL-015.
10. Assign Knowledge Extracted marker to source closure report. Record in execution report.
11. AGENT.md updates for Marcus and Kai are prepared as separate proposals per SOP-015. Owner reviews and approves each separately before execution.
12. Source closure report retained. Primary state: Accepted as Done. Markers: Authoritative; Knowledge Extracted (agent_learnings). Both markers recorded in execution report.
13. Write execution report: all actions taken, agent_learnings write confirmation, paths to AGENT.md update proposals, date.

**Source file not deleted. Two separate approval gates: one for agent_learnings, one per AGENT.md file updated. No write to the source file without Owner approval of a visible status note.**

---

### Example 4: Business deliverable processed into Kamer E-commerce BKM

**Context:** Nova has delivered a pricing analysis report for Kamer E-commerce. The report is accepted as Done. Owner approves knowledge extraction to the Kamer E-commerce knowledge base.

**Processing decision:**
- Primary state: Accepted as Done
- Marker: Knowledge Extracted (Kamer E-commerce KB, session 2026-06-05)
- Decision rule applied: R6 (Business knowledge candidate, home domain: kamer-ecommerce)

**Steps executed:**
1. Apply decision rules. R6 applies.
2. Cross-domain check: pricing analysis is Kamer E-commerce domain only. No cross-domain routing needed.
3. Larry proposes to Owner: "This pricing analysis contains operational knowledge relevant to the Kamer E-commerce knowledge base. Proposed destination: [specific file in Team Knowledge/Kamer E-commerce/]. Extracting agent: Nova."
4. Owner approves.
5. Nova extracts and writes the relevant knowledge to the designated KB file.
6. GL-015 routing: domain: kamer-ecommerce, source_type: knowledge.
7. Source report retained in Deliverables folder. Primary state: Accepted as Done. Marker: Knowledge Extracted. Marker recorded in execution report. No write to source file.
8. Write execution report: destination file, content extracted, date, extracting agent, GL-015 routing applied, marker assignment.

**Source file not deleted or moved.**

---

### Example 5: Personal deliverable processed into PKM

**Context:** A triage report on Owner Walter Kamer's personal finance goals contains personal decisions and insights. The report is accepted as Done. Owner approves extraction to PKM.

**Processing decision:**
- Primary state: Accepted as Done
- Marker: Knowledge Extracted (PKM, session 2026-06-05)
- Decision rule applied: R5 (Personal knowledge candidate, home domain: personal)

**Steps executed:**
1. Apply decision rules. R5 applies.
2. Cross-domain check: personal finance decisions are personal domain only. No cross-domain routing needed.
3. Larry proposes to Owner: "This triage report contains personal decisions relevant to PKM. Proposed home domain: personal. Proposed destination: [specific section or file in PKM/My Life/Key Elements/]. Extracting agent: Sienna."
4. Owner approves.
5. Sienna extracts the personal decisions and writes to the designated PKM file.
6. GL-015 routing: domain: personal, source_type: knowledge.
7. Source triage report retained in Deliverables folder. Primary state: Accepted as Done. Marker: Knowledge Extracted. Marker recorded in execution report. No write to source file.
8. Write execution report: destination file, content extracted, date, extracting agent, GL-015 routing applied, marker assignment.

**Source file not deleted or moved.**

---

## 16. Execution Report Requirements

Every lifecycle processing action that changes a deliverable's primary state, assigns a lifecycle marker, performs a write, or moves a file must be documented in an execution report. The execution report is itself a deliverable and enters the review gate per GL-016 and SOP-016 before being accepted as Done. After a lifecycle execution report is accepted as Done, apply EX-7 to determine whether a further execution report is required for that report.

An execution report for a lifecycle action must contain:

1. **Deliverable path** — exact current file path of the deliverable that was processed
2. **Primary state before** — the primary state before this action (per GL-017 Section 3.2)
3. **Primary state after** — the primary state after this action; if unchanged, state that explicitly (e.g., "primary state remains Accepted as Done")
4. **Lifecycle markers assigned** — list each marker assigned in this action and the rule or decision that triggered it
5. **Processing actions taken** — list each action taken; one action per line
6. **Processing destinations** — exact file path or database table for each write action
7. **Decision rules applied** — list each rule (R1 through R10) that triggered an action
8. **Owner approval reference** — session date and the approval statement or confirmation received
9. **Executing agent** — which agent executed each action
10. **Date executed** — the date each action was taken
11. **References identified** — list all documents found to reference this deliverable; separately list: (a) approved reference updates executed, (b) pending reference updates awaiting Owner decision
12. **Post-check result** — confirmation that the source deliverable is retained, no unintended side effects occurred, and the safeguards checklist passed
13. **Next steps** — any pending actions identified but not yet executed (for example pending AGENT.md proposal, pending SOP-015 proposal, pending reference updates)

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
| Deliverable Lifecycle, Knowledge Processing, and Archiving Procedure | `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md` | Step-by-step lifecycle processing procedure — trigger moments, decision rules R1–R10, processing destination catalog, personal/business/governance flows, safeguards checklist, explicit rules EX-1 through EX-7, worked examples |
```

**Format verification:** The row format above was verified against `SOP-index.md` as read on 2026-06-04 in the current session. The existing format is: `| SOP Name | \`File Path\` | Purpose |`. Note: the SOP index does not include a number column; the number is encoded in the file path only. Implementation must re-confirm the existing SOP-index.md format immediately before appending, as the format is the authoritative source.

---

## 6. Pairing Notes

This proposal is paired with GL-017 proposal (`deliverable-lifecycle-gl-proposal-v02.md`).

**Separation of concerns:**
- GL-017 defines principles: post-acceptance primary states, lifecycle markers, core principles P1 through P13, authoritative source protections, and cross-domain routing principles.
- SOP-017 defines procedures: trigger moments, lifecycle decision workflow phases, processing destination catalog, decision rules R1 through R10, personal/business/governance processing flows, archive and superseded handling, authoritative source handling, domain routing table, safeguards checklist, explicit rules EX-1 through EX-7, worked examples, and execution report requirements.
- The two documents do not duplicate each other. The SOP references GL-017 for the state model and principles.

**Dependency on GL-017:**
SOP-017 requires GL-017 to exist before SOP-017 is implemented. SOP-017 references GL-017 Sections 3.2, 3.3, and 4 for the lifecycle model and governing principles. Without GL-017, those references are unresolved.

**Recommended execution order:**
GL-017 must be implemented and post-checked before SOP-017 is implemented. If GL-017 post-checks fail, SOP-017 must not be implemented until GL-017 is corrected and confirmed. This is the same pattern as GL-016 and SOP-016.

**Cross-references if both are approved:**
- SOP-017 Section 1 references GL-017 as the upstream principle.
- GL-017 Section 5 references SOP-017 as the operational counterpart (anticipatory reference in GL-017 that resolves when SOP-017 is created).

---

## 7. Implementation Scope

If this proposal is approved (and GL-017 post-checks have been confirmed to Owner), exactly the following actions are in scope:

1. Create `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md` with the exact content from Section 4.
2. Append the SOP-017 row to `Team Knowledge/Core/SOPs/SOP-index.md` per Section 5, after re-confirming the existing format.
3. Read back both files to confirm contents match the approved proposal exactly.
4. Report post-check result to Owner.

No other actions are in scope.

---

## 8. Explicit Exclusions

The following are explicitly excluded from SOP-017 implementation:

- Implementing GL-017 (must already be complete and post-checked before SOP-017 is implemented)
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

1. Read back `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md`. Confirm all sections, decision rules, explicit rules EX-1 through EX-7, worked examples, the processing destination catalog, and the safeguards checklist match the approved content in Section 4 exactly.
2. Read back `Team Knowledge/Core/SOPs/SOP-index.md`. Confirm the SOP-017 row is present, correctly formatted, and no other rows were modified.
3. Confirm no other files were modified during implementation.
4. Confirm no database writes occurred.
5. Report post-check result to Owner: file path, SOP number, index row, confirmation of no side effects.

---

## 10. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| SOP-017 number taken between proposal preparation and implementation | Re-confirm SOP-index.md immediately before file creation during implementation |
| SOP-index.md format changed between proposal preparation and implementation | Implementation must re-confirm the existing format before appending; the proposed row format is based on the format read on 2026-06-04 |
| SOP-017 implemented before GL-017 post-checks are confirmed | Implementation scope and pairing notes both state this explicitly; confirm GL-017 post-check report before proceeding |
| SOP content overlaps with GL-017 principle content | SOP-017 references GL-017 for states and principles; it does not restate them. Reviewer should flag any principle-level content in the SOP text before approving |
| Worked examples interpreted as authorization to execute those examples | Section 15 explicitly states worked examples are illustrative only |
| Optional future updates (GL-016, SOP-016) executed automatically | Section 8 explicitly marks these as excluded |

---

## 11. Owner Decision Options

| Option | Action |
|---|---|
| **A** | Approve GL-017 implementation only. SOP-017 reviewed and decided separately at a later time. |
| **B** | Approve paired implementation. GL-017 implemented first. SOP-017 implemented after GL-017 post-checks are confirmed to Owner. |
| **C** | Request amendments. Specify which sections require changes. A v03 will be prepared per SOP-015. |
| **D** | Defer. |
| **E** | Reject. |

---

*Delivered on: 2026-06-05*
*Delivered at: Deliverables/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage/deliverable-lifecycle-sop-proposal-v02.md*
