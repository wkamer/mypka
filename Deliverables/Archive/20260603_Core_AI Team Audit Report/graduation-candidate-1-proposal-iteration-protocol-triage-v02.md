# Graduation Candidate 1 — Triage Report v02: Proposal Iteration Protocol for System File Changes

**Status:** Proposal only — no implementation  
**Version:** v02 (supersedes v01)  
**Date:** 2026-06-03  
**Author:** Larry (orchestrator)  
**Source session:** B-021C Secure Credential Recovery close-session  
**Confirmed for triage by:** Owner Walter Kamer  
**Requires Owner decision:** see §8 Owner Decision Options

---

## Revision Notes

**Changes from v01:**

1. Clarified that the proposed SOP governs multi-round proposal iteration specifically. Core Owner approval governance (GL-014 §1) applies to all system-file proposals, including single-round proposals, regardless of this SOP.
2. Draft protocol updated: Owner corrections between proposal versions are now documented in a dedicated `## Revision Notes` section at the top of each revised proposal, not in the `## Purpose` section. Purpose remains focused on why the change is needed.
3. Option A tightened: approving Option A only authorizes Larry to prepare a formal implementation proposal for later Owner review. It does not create a SOP, update `sop-index.md`, write team_log, update team_tasks, or modify any system file.

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

This pattern is not currently documented anywhere in the team's SOPs, Guidelines, or Workstreams. Each proposal iteration was managed ad hoc, with rules carried in conversation context only. A governance candidate exists: formalising this pattern prevents future agents from collapsing proposal rounds, mixing approved and superseded versions, or executing against the wrong version.

**Important distinction:** The proposed SOP covers multi-round iteration discipline. It does not replace or reduce the core Owner approval requirement that already applies to all system-file proposals under GL-014 §1 — including single-round proposals.

This triage report assesses where and whether to formalise the multi-round iteration pattern.

---

## 2. Governance Basis

| Item | Reference |
|---|---|
| Approval gates for all SOP/GL changes | GL-014 §1 — Only after explicit Owner approval |
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
3. A revised proposal is written, clearly versioned, superseding the prior version, with corrections documented in a dedicated revision section
4. Execution against a superseded version is prohibited — version-specific approval is required
5. After approval, execution uses exact text from the approved version
6. The execution report explicitly references the approved proposal version
7. Between proposal rounds, agents do not execute, do not modify target files, do not create backlog items, and do not log partial progress as complete

**What makes this pattern stable enough for formalisation:**
- It repeated across three proposal rounds for a single backlog item
- It was implicitly enforced by Owner corrections — the team was expected to follow it but had no documented rule
- The failure modes (executing against a superseded version, skipping the version gate, collapsing rounds) are realistic and have non-trivial consequences
- The pattern is domain-independent: it applies equally to SOP, GL, Workstream, and AGENT.md changes

---

## 4. Triage: Best Canonical Destination

### 4.1 Options Assessed

| Option | Assessment |
|---|---|
| **a. Update to existing SOP** | No existing SOP covers proposal iteration methodology. SOP-001 covers disaster recovery; SOP-014 covers session context hygiene. Neither is the right host. |
| **b. New standalone SOP** | Strong fit. The pattern is atomic (one job: iterate proposals safely), reusable (applies to any multi-round system file change), and procedural (ordered steps with gating conditions). This matches the team's SOP definition: atomic procedure, one job, one file. |
| **c. Part of existing GL** | GL-014 §1 covers approval gates (what needs approval) and §5 covers changelog protocol (how to record changes). Neither covers how to structure multi-round proposal iteration. Extending GL-014 with procedural steps risks bloating a governance reference document with method detail that belongs in a SOP. |
| **d. Part of a future Graduation Candidate Triage Protocol** | This triage report is itself a meta-level artefact. Embedding the proposal iteration pattern inside a triage protocol would create circular structure and reduce discoverability. |
| **e. Backlog item for later** | Viable if Owner judges formalisation as low priority. The pattern works without documentation — it has been enforced by convention. Risk: future agents operating without session context will not know the rules. |

### 4.2 Recommendation

**Option b — New standalone SOP** remains the best canonical destination.

Rationale:
- The pattern is atomic: one job, clear start and end, ordered steps, defined gating conditions
- It is reusable across all system file change types (SOP, GL, WS, AGENT.md)
- It is distinct from GL-014's approval gates (what) — this SOP covers the iteration method (how)
- A SOP reference in agent briefings is more actionable than a GL reference during active proposal work
- Proposed working title: `SOP-0XX_Proposal Iteration Protocol for System File Changes`

The next available SOP number must be confirmed from `Team Knowledge/Core/SOPs/sop-index.md` before any implementation. This triage does not assign a number.

---

## 5. Draft Protocol — Proposal Only

**Note:** The text below is a draft for Owner review. It is not a final SOP and may not be implemented without separate Owner Walter Kamer approval.

---

### DRAFT: Proposal Iteration Protocol for System File Changes

**Applies to:** Any proposed change to SOP, GL, Workstream, or AGENT.md files that requires Owner approval and goes through multiple review rounds before execution is approved.

**Does not apply to (iteration workflow):** Single-round proposals that receive Owner approval on first submission without corrections. Single-round proposals remain fully subject to Owner approval governance under GL-014 §1 — they are simply not subject to the multi-round iteration procedures described in this SOP.

---

#### Proposal Document Structure

Every proposal deliverable — including revised versions — must use the following structure:

```
# [Item] Proposal vX.X

**Status:** Proposal only — no implementation
**Version:** vX.X (supersedes vX.X-1)  ← omit on first version
**Date:** YYYY-MM-DD
**Author:** [Agent]
**Backlog item:** [ID]
**Requires approval by:** Owner Walter Kamer

---

## Revision Notes  ← include from v2 onward; omit on first version

[List of corrections applied in this version, each linked to Owner feedback.
Do not describe WHY the change is needed here — that belongs in §1 Purpose.]

---

## 1. Purpose

[Why this change is needed. Static across versions unless scope changes.]

[... remaining sections ...]

## Approval Gate

No implementation may happen until Owner Walter Kamer explicitly approves [Item] vX.X.
Approval of a prior version does not carry forward to this version.
```

---

#### Step 1 — Write the Initial Proposal

- Status field: `Proposal only — no implementation`
- Version: start at v0.1 or the first substantive version; label clearly
- Include an explicit Approval Gate section naming the exact version
- Deliver to the audit or domain deliverables folder — never write to the target file
- Do not modify the target file

#### Step 2 — Submit for Owner Review

- Present only: deliverable path, status, short summary, files inspected, deviations, recommended next step
- Do not paste the full proposal in chat
- Await Owner feedback before any further action

#### Step 3 — Apply Corrections in a New Versioned Proposal

- Write a new versioned file (e.g., `...-v03.md`) — do not overwrite or edit the prior version
- Header: mark as superseding the prior version
- `## Revision Notes` section: list each correction applied and the Owner feedback it addresses
- `## Purpose` section: unchanged unless the fundamental scope changed — Purpose explains why, not what changed between versions
- The prior version remains in the deliverables folder unchanged as an audit trail
- Do not execute against any prior version under any circumstance

#### Step 4 — Repeat Steps 2–3 Until Owner Approves a Specific Version

Between proposal rounds, the agent must not:
- Modify the target file (SOP, GL, WS, AGENT.md)
- Execute any part of the proposed change
- Create backlog items or team_tasks rows related to this item
- Write team_log entries marking the item as complete or in progress
- Treat Owner feedback as implicit approval — feedback triggers a new version, not execution

#### Step 5 — Receive Version-Specific Owner Approval

- Approval must name the exact version: e.g., "approve B-021C-A v0.4"
- A general "go" or "looks good" without naming the version requires confirmation before execution
- Approval of a prior version does not carry forward to a revised version

#### Step 6 — Execute Against the Exact Approved Version

- Use the approved proposal as the sole execution specification
- For text changes: apply exact text as written in the approved proposal — do not paraphrase, adapt, or improve
- If an exact text match fails during execution: stop and report to Owner — do not improvise a substitute

#### Step 7 — Write the Execution Report

The execution report must include:
- Explicit reference to the approved proposal: file path and version number
- Confirmation of each change applied
- Confirmation of what was not executed (exclusions)
- Confirmation of any deviations, or the statement "No deviations"

#### Step 8 — Confirm Completion

- Mark the backlog item complete only after post-checks pass and the execution report is written
- Update team_tasks status only after the execution report confirms all checks passed

---

## 6. Scope Boundaries

### In scope for the multi-round iteration workflow

- Proposals for SOP, GL, Workstream, and AGENT.md changes that go through two or more Owner review rounds
- Any system file change that generates multiple versioned proposal deliverables before execution is approved

### Outside the iteration workflow — but still subject to Owner approval

- Single-round proposals approved on first submission without corrections
- Proposals rejected outright without revision
- These remain fully governed by GL-014 §1. The absence of multi-round iteration does not reduce the Owner approval requirement.

### Out of scope entirely

- Execution methodology for individual change types (e.g., how to apply a specific Edit command) — that belongs in the relevant SOP or execution guidance
- Credential handling, permission changes, or live system changes — governed by GL-014 §3
- Session logging and close-session procedures — governed by SOP-014 and close-session skill

---

## 7. Risks and Mitigations

| Risk | Level | Mitigation |
|---|---|---|
| Agent executes against a superseded proposal version | High | Step 5 gate: version-specific approval required, named explicitly; Approval Gate section in every proposal |
| Agent collapses multiple review rounds into one undocumented edit | Medium | Step 3: each correction produces a new versioned file; prior versions never overwritten |
| Owner approval phrasing is ambiguous ("looks good") | Medium | Step 5: agent must confirm exact version before executing |
| Revision Notes section omitted; corrections invisible in audit trail | Medium | Draft protocol mandates Revision Notes from v2 onward; execution report reviewer checks for it |
| SOP conflicts with GL-014 approval gate wording | Low | SOP complements GL-014 §1 (what needs approval); no content overlap on the how |
| Future agents not briefed on the SOP | Medium | Implementation proposal will include CLAUDE.md or GL-004 routing reference if Owner approves |

---

## 8. Owner Decision Options

| Option | Description |
|---|---|
| **A — Approve preparing a formal implementation proposal** | Larry prepares a formal implementation proposal: proposed SOP title, SOP number (confirmed from sop-index), exact file content, exact index update text, and changelog entry. That implementation proposal is a separate Owner-reviewed deliverable. Approving Option A does not create any file, does not update sop-index.md, does not write team_log, does not update team_tasks, and does not modify any system file. Implementation only proceeds after Owner explicitly approves the implementation proposal. |
| **B — Request amendments to this triage** | Owner returns corrections to the draft protocol in §5 or any other section. Larry produces a v03 triage report. No implementation until a triage version is approved. |
| **C — Defer** | No action taken now. The pattern continues to operate by convention. Revisit when a future multi-round proposal occurs. |
| **D — Reject** | The pattern does not need formalisation. Convention and Owner correction during active sessions are sufficient governance. |

**Larry's recommendation: Option A.**

The pattern has already been enforced implicitly across B-021C-A. Formalising it as a SOP removes reliance on session context and provides future agents with a canonical reference. Option A produces only a formal implementation proposal — a document, not a system change — so Owner retains full review control before anything is created.

---

## 9. Approval Gate

No implementation may happen without separate, explicit Owner Walter Kamer approval.

This triage report is a proposal and assessment only. No SOP file has been created. No GL has been modified. No backlog item has been registered. No team_log entry has been written for this candidate beyond the close-session graduation candidate record.

Approving Option A does not constitute implementation approval. It only authorises Larry to prepare a formal implementation proposal for Owner review.

---

*Delivered on: 2026-06-03*  
*Delivered at: Deliverables/20260603_Core_AI Team Audit Report/graduation-candidate-1-proposal-iteration-protocol-triage-v02.md*
