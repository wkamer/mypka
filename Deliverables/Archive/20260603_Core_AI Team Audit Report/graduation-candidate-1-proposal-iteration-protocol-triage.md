# Graduation Candidate 1 — Triage Report: Proposal Iteration Protocol for System File Changes

**Status:** Proposal only — no implementation  
**Date:** 2026-06-03  
**Author:** Larry (orchestrator)  
**Source session:** B-021C Secure Credential Recovery close-session  
**Confirmed for triage by:** Owner Walter Kamer  
**Requires Owner decision:** see §8 Owner Decision Options

---

## 1. Purpose

During the B-021C-A trajectory, a repeatable multi-round proposal pattern emerged:

- v0.2 proposal written
- Owner review produces exact corrections to wording and scope
- v0.3 proposal written (proposal-only, supersedes v0.2)
- Owner review produces further corrections
- v0.4 proposal written (proposal-only, supersedes v0.3)
- Owner gives explicit version-specific approval for v0.4
- Execution proceeds against the exact approved version
- Execution report links back to the approved proposal version

This pattern is not currently documented anywhere in the team's SOPs, Guidelines, or Workstreams. Each proposal iteration was managed ad hoc, with rules carried in conversation context only. A governance candidate exists: formalising this pattern as a reusable procedure prevents future agents from collapsing proposal rounds, mixing approved and superseded versions, or executing against the wrong version.

This triage report assesses where and whether to formalise it.

---

## 2. Governance Basis

| Item | Reference |
|---|---|
| Approval gates for SOP/GL changes | GL-014 §1 — Only after explicit Owner approval |
| Changelog protocol | GL-014 §5 — Date, agent, backlog ID, description, approval required |
| SOP taxonomy | CLAUDE.md — Atomic procedures, one job, one file |
| Guideline taxonomy | CLAUDE.md — Static reference info |
| Graduation candidate auto-creation prohibited | CLAUDE.md — Wait for Owner confirmation per number |
| No implementation without Owner approval | GL-014 §1 and CLAUDE.md |

---

## 3. Candidate Description

**Pattern observed across B-021C-A (v0.2 → v0.3 → v0.4):**

1. An initial proposal is written (proposal-only deliverable)
2. Owner reviews and returns exact corrections — wording, scope, structure
3. A revised proposal is written, clearly versioned, clearly marked as superseding the prior version
4. Execution against a superseded version is prohibited — version-specific approval is required
5. After approval, execution uses exact text from the approved version
6. The execution report explicitly references the approved proposal version
7. Between proposal rounds, agents do not execute, do not modify target files, do not create backlog items, and do not log partial progress as complete

**What makes this pattern stable enough for formalisation:**
- It repeated across three proposal rounds for a single backlog item
- It was implicitly enforced by Owner corrections — meaning the team was expected to follow it but had no documented rule
- The failure modes (executing against superseded version, skipping version gate, collapsing rounds) are realistic and have non-trivial consequences
- The pattern is domain-independent: it applies equally to SOP, GL, Workstream, and AGENT.md changes

---

## 4. Triage: Best Canonical Destination

### 4.1 Options Assessed

| Option | Assessment |
|---|---|
| **a. Update to existing SOP** | No existing SOP covers proposal iteration methodology. SOP-001 covers disaster recovery; SOP-014 covers session context hygiene. Neither is the right host. |
| **b. New standalone SOP** | Strong fit. The pattern is atomic (one job: iterate proposals safely), reusable (applies to any multi-round system file change), and procedural (ordered steps). This is the defining characteristic of a SOP in this team's taxonomy. |
| **c. Part of existing GL** | GL-014 §1 covers approval gates (what needs approval) and §5 covers changelog protocol (how to record changes). Neither covers how to structure multi-round proposal iteration. Extending GL-014 with a new section is possible but risks bloating a governance reference document with procedural detail that belongs in a SOP. |
| **d. Part of a future Graduation Candidate Triage Protocol** | This triage report is itself a meta-level artefact. Embedding the proposal iteration pattern inside a triage protocol would create circular structure and reduce discoverability. |
| **e. Backlog item for later** | Viable if Owner judges formalisation as low priority. The pattern works without documentation — it has been enforced by convention. Risk: future agents operating without session context will not know the rules. |

### 4.2 Recommendation

**Option b — New standalone SOP** is the best canonical destination.

Rationale:
- The pattern is atomic: one job, clear start and end, ordered steps, defined gating conditions
- It is reusable across all system file change types (SOP, GL, WS, AGENT.md)
- It is distinct from GL-014's approval gates (what) — this SOP would cover the iteration method (how)
- A SOP reference in agent briefings is more actionable than a GL reference during active proposal work
- Naming: `SOP-0XX_Proposal Iteration Protocol for System File Changes`

The next available SOP number must be confirmed from `Team Knowledge/Core/SOPs/sop-index.md` before implementation. This triage does not assign a number.

---

## 5. Draft Protocol — Proposal Only

**Note:** The text below is a draft for Owner review. It is not a final SOP. It may not be implemented without separate Owner Walter Kamer approval.

---

### DRAFT: Proposal Iteration Protocol for System File Changes

**Applies to:** Any proposed change to SOP, GL, Workstream, or AGENT.md files that requires Owner approval and may go through multiple review rounds.

**Does not apply to:** Single-round proposals that receive approval on first submission without corrections.

---

**Step 1 — Write the initial proposal**

- Mark the document clearly: `Status: Proposal only — no implementation`
- Include: version number (v0.1 or first substantive version), date, author, backlog item reference, approval gate statement
- Write to the audit deliverables folder or domain deliverables folder — never to the target file
- Do not modify the target file

**Step 2 — Submit for Owner review**

- Present the deliverable path and short summary only
- Do not paste the full proposal in chat
- Await Owner feedback before any further action

**Step 3 — Apply Owner corrections in a new version**

- Write a new versioned file (e.g., v0.3) — do not overwrite the prior version
- Mark the new version as superseding the prior: `Version: vX.X (supersedes vX.X-1)`
- In the Purpose section of the new version, state what correction was made and why
- The prior version remains in the deliverables folder unchanged as an audit trail
- Do not execute against the superseded version under any circumstance

**Step 4 — Repeat Steps 2–3 until Owner approves a specific version**

- Each round produces a new versioned deliverable
- Each round waits for Owner response before proceeding
- Between rounds, the agent does not: modify target files, create backlog items, write team_log entries marking the item as complete, or execute any part of the proposed change

**Step 5 — Receive version-specific Owner approval**

- Approval must name the exact version: "approve B-021C-A v0.4" — not "approve B-021C-A"
- Approval of a prior version does not carry forward to a revised version
- If the Owner says "go" without naming a version: confirm which version is approved before executing

**Step 6 — Execute against the exact approved version**

- Use the approved proposal as the execution specification
- For text changes: use exact text match as specified in the proposal — do not paraphrase, adapt, or improve
- If an exact match fails during execution: stop and report — do not improvise

**Step 7 — Write the execution report**

- The execution report must explicitly reference the approved proposal version: file path and version number
- The execution report must confirm which changes were applied
- The execution report must confirm what was not executed (exclusions)

**Step 8 — Confirm completion**

- Mark the backlog item complete only after post-checks pass
- Update team_tasks status only after execution report is written

---

**What agents must not do during proposal iteration:**

- Execute any change to a target file before version-specific Owner approval
- Use a superseded version as an execution specification
- Merge corrections from multiple review rounds into a single undocumented edit
- Skip the execution report
- Mark a backlog item complete before execution is confirmed
- Treat "looks good" or "proceed" as version-specific approval — always confirm the version

---

## 6. Scope Boundaries

### In scope (if formalised)

- Multi-round proposals for SOP, GL, Workstream, and AGENT.md changes
- Any system file change that goes through Owner review before execution
- Any backlog item that generates multiple proposal deliverable versions

### Out of scope

- Single-round proposals approved on first submission
- Proposals that are rejected outright without revision
- Execution methodology for individual change types (e.g., how to apply a specific Edit command) — that belongs in the relevant SOP or execution guidance
- Credential handling, permission changes, or live system changes — those remain governed by GL-014 §3

---

## 7. Risks and Mitigations

| Risk | Level | Mitigation |
|---|---|---|
| Future agent executes against a superseded proposal version | High | Step 5 gate: version-specific approval required, named explicitly |
| Agent collapses multiple review rounds into one undocumented edit | Medium | Step 3: each correction produces a new versioned file; prior versions are never overwritten |
| Owner approval phrasing is ambiguous ("looks good") | Medium | Step 5: agent must confirm version before executing |
| SOP becomes too abstract to be actionable | Low | Draft is procedural and step-by-step; implementation review can tighten language |
| SOP conflicts with GL-014 approval gate wording | Low | SOP complements GL-014 §1 (what needs approval); no overlap on the how |
| No one reads a new SOP if agents are not briefed | Medium | Briefing rule in CLAUDE.md: agents reference canonical SOP path in delegation briefs |

---

## 8. Owner Decision Options

| Option | Description |
|---|---|
| **A — Approve formal implementation proposal** | Larry writes a formal implementation proposal for the new SOP (title, number from sop-index, exact file content, index update). Owner approves that proposal before any file is created. |
| **B — Request amendments to this triage** | Owner returns corrections to the draft protocol in §5 or the canonical destination recommendation in §4. Larry revises the triage report. |
| **C — Defer** | No action taken now. The pattern continues to operate by convention. Revisit when a future multi-round proposal occurs. |
| **D — Reject** | The pattern does not need formalisation. Convention and Owner correction during active sessions are sufficient governance. |

**Larry's recommendation: Option A.**

The pattern has already been enforced implicitly across B-021C-A. Formalising it as a SOP removes reliance on session context and gives future agents a canonical reference. The implementation proposal required for Option A is low-risk and documentation-only.

---

## 9. Approval Gate

No implementation may happen without separate, explicit Owner Walter Kamer approval.

This triage report is a proposal and assessment only. No SOP file has been created. No GL has been modified. No backlog item has been registered. No team_log entry has been written for this candidate beyond the close-session graduation candidate record.

Any implementation (Option A) requires a separate implementation proposal that Owner Walter Kamer reviews and approves before any file is created or modified.

---

*Delivered on: 2026-06-03*  
*Delivered at: Deliverables/20260603_Core_AI Team Audit Report/graduation-candidate-1-proposal-iteration-protocol-triage.md*
