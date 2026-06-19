# Graduation Candidate 1 — SOP-015 Formal Implementation Proposal

**Status:** Proposal only — no implementation  
**Date:** 2026-06-03  
**Author:** Larry (orchestrator)  
**Based on:** Graduation Candidate 1 Triage v02 (approved Option A)  
**Requires Owner decision:** see §9 Owner Decision Options

---

## 1. Purpose

Owner Walter Kamer approved Option A from the graduation candidate triage v02: prepare a formal implementation proposal for the Proposal Iteration Protocol for System File Changes. This document is that proposal. It contains the exact file content, exact index update, and a set of optional reference updates as separate Owner decision items.

No implementation may happen without Owner Walter Kamer's explicit approval of this proposal.

---

## 2. Governance Basis

| Item | Reference |
|---|---|
| SOP changes require Owner approval | GL-014 §1 |
| Changelog protocol | GL-014 §5 — date, agent, backlog ID, description, approval |
| Canonical paths | GL-004 |
| SOP taxonomy | CLAUDE.md — atomic procedures, one job, one file |
| Graduation candidate auto-creation prohibited | CLAUDE.md — confirmation required per number |
| No implementation without Owner approval | GL-014 §1 and CLAUDE.md |

---

## 3. Proposed SOP Identity

| Field | Value |
|---|---|
| SOP number | SOP-015 |
| Filename | `SOP-015_Proposal Iteration Protocol for System File Changes.md` |
| Canonical path | `Team Knowledge/Core/SOPs/SOP-015_Proposal Iteration Protocol for System File Changes.md` |
| Next available number confirmed from | `Team Knowledge/Core/SOPs/SOP-index.md` — highest present is SOP-014 |

---

## 4. Proposed SOP Content — Exact Full Text

The text below is the exact content to be written to the new file if approved. It is reproduced here in full so Owner Walter Kamer can review every word before approving.

---

```
# SOP-015 Proposal Iteration Protocol for System File Changes

**Applies to:** Any proposed change to SOP, GL, Workstream, or AGENT.md files that
requires Owner approval and goes through multiple review rounds before execution is approved.

**Does not apply to (iteration workflow):** Single-round proposals that receive Owner
approval on first submission without corrections. Single-round proposals remain fully
subject to Owner approval governance under GL-014 §1. They are not subject to the
multi-round iteration procedures described in this SOP.

---

## Purpose

Document the repeatable pattern for iterating on system-file change proposals safely:
versioning, Owner correction tracking, superseded version handling, version-specific
approval gating, and execution against the exact approved version only.

---

## Proposal Document Structure

Every proposal deliverable — including all revised versions — uses this structure:

```
# [Item ID] [Description] Proposal vX.X

**Status:** Proposal only — no implementation
**Version:** vX.X (supersedes vX.X-1)    ← omit on the first version
**Date:** YYYY-MM-DD
**Author:** [Agent slug]
**Backlog item:** [ID]
**Requires approval by:** Owner Walter Kamer — see Approval Gate

---

## Revision Notes    ← include from v2 onward; omit on the first version

- [Correction 1 applied in this version — linked to Owner feedback]
- [Correction 2 applied in this version — linked to Owner feedback]

---

## 1. Purpose

[Why this change is needed. Stable across versions unless scope changes.
Do not describe what changed between versions here — that belongs in Revision Notes.]

[... remaining proposal sections ...]

---

## Approval Gate

No implementation may happen until Owner Walter Kamer explicitly approves [Item] vX.X.
Approval of a prior version does not carry forward to this version.
```

---

## Step 1 — Write the Initial Proposal

1. Set status field to: `Proposal only — no implementation`
2. Start versioning at v0.1 or the first substantive version; label clearly
3. Include an explicit `## Approval Gate` section naming the exact version
4. Deliver to the audit or domain deliverables folder — never write to the target system file
5. Do not modify the target file at any point during Step 1

---

## Step 2 — Submit for Owner Review

1. Present in chat: deliverable path, status, short summary, files inspected, deviations or blockers, recommended next step
2. Do not paste the full proposal in chat
3. Await Owner feedback before any further action

---

## Step 3 — Apply Corrections in a New Versioned Proposal

1. Write a new versioned file — do not overwrite or edit the prior version file
2. Mark in the header: `Version: vX.X (supersedes vX.X-1)`
3. Add `## Revision Notes` section immediately after the header block: list each correction applied and the Owner feedback it addresses
4. Keep `## Purpose` focused on why the change is needed — not on what changed between versions
5. Leave the prior version file unchanged in the deliverables folder as an audit trail
6. Do not execute against any prior version under any circumstance

---

## Step 4 — Repeat Steps 2–3 Until Owner Approves a Specific Version

During proposal iteration, the agent must not:

- Modify the target file (SOP, GL, WS, AGENT.md)
- Execute any part of the proposed change
- Create Todoist tasks or team_tasks rows that register the item as in-progress or complete
- Write team_log entries marking the item as complete or partially complete
- Treat Owner feedback as implicit approval — feedback triggers a new version, not execution
- Treat a general "go" or "looks good" as version-specific approval

---

## Step 5 — Receive Version-Specific Owner Approval

1. Approval must name the exact version: e.g., "approve B-021C-A v0.4" — not "approve B-021C-A"
2. If the Owner says "go" or "proceed" without naming a version: confirm which version is approved before executing
3. Approval of a prior version does not carry forward to a revised version

---

## Step 6 — Execute Against the Exact Approved Version

1. Use the approved proposal deliverable as the sole execution specification
2. For text changes to system files: apply the exact text written in the approved proposal — do not paraphrase, adapt, or improve
3. If an exact text match fails during execution: stop and report to Owner — do not improvise a substitute
4. Make no changes beyond the approved scope — if a related improvement is noticed, note it in the execution report as a future candidate, not as an immediate change

---

## Step 7 — Write the Execution Report

The execution report must include:

1. Explicit reference to the approved proposal: file path and version number
2. Confirmation of each change applied, with exact method used
3. Confirmation of what was not executed (exclusions)
4. Confirmation of any deviations, or the statement "No deviations"
5. Post-check results confirming the target file matches the approved text

---

## Step 8 — Confirm Completion

1. Mark the backlog item complete only after post-checks pass and the execution report is written
2. Update team_tasks status only after the execution report confirms all checks passed
3. Write audit trail entries (team_log, UMC) only after Step 7 is complete

---

## Changelog

- 2026-06-03 (Larry, B-021C graduation candidate 1): SOP-015 created — Proposal Iteration
  Protocol for System File Changes. Approved by Owner Walter Kamer.
```

---

## 5. Proposed SOP-index.md Update — Exact Text

**Target file:** `Team Knowledge/Core/SOPs/SOP-index.md`

**Exact text to append** (new row at the end of the table):

```
| Proposal Iteration Protocol for System File Changes | `Team Knowledge/Core/SOPs/SOP-015_Proposal Iteration Protocol for System File Changes.md` | Multi-round proposal iteration discipline for SOP, GL, Workstream, and AGENT.md changes — versioning, Revision Notes, Owner approval gating, and execution against the approved version only |
```

---

## 6. Optional Reference Updates

The following reference updates are not part of the core SOP-015 implementation scope. Each is a separate Owner decision item. Owner Walter Kamer may approve any combination independently, or none.

### Optional Item 1 — CLAUDE.md Reference

**Rationale:** CLAUDE.md is the primary instruction file read by all agents. Adding a pointer to SOP-015 ensures agents encounter it during operational context loading, not only when searching the SOP folder.

**Proposed insertion location:** Under `## Operational Conventions (Always Active)`, as a new bullet in the relevant conventions block or as a standalone line.

**Exact proposed text:**

```
- When a system-file change proposal requires multiple Owner review rounds: follow
  `[[SOP-015_Proposal Iteration Protocol for System File Changes]]` — versioned
  proposals, Revision Notes per round, version-specific approval, exact-text execution.
```

**Scope:** One line added to CLAUDE.md. No other changes.

---

### Optional Item 2 — GL-014 Cross-Reference

**Rationale:** GL-014 §1 lists what requires Owner approval. Adding a cross-reference to SOP-015 in that section directs agents from "this needs approval" (GL-014) to "here is how to iterate on a multi-round proposal" (SOP-015).

**Proposed insertion location:** At the end of GL-014 §1 (`## 1. Approval-gates`), after the existing approval lists.

**Exact proposed text:**

```
For system-file changes that require multiple proposal rounds before approval:
see `[[SOP-015_Proposal Iteration Protocol for System File Changes]]`.
```

**Scope:** Two lines added to GL-014 §1. No other changes.

---

## 7. Implementation Scope

### Core scope (requires Owner approval to execute)

| Action | File |
|---|---|
| Create new file with exact content from §4 | `Team Knowledge/Core/SOPs/SOP-015_Proposal Iteration Protocol for System File Changes.md` |
| Append one row to SOP-index table | `Team Knowledge/Core/SOPs/SOP-index.md` |

### Optional scope (each requires separate Owner approval decision)

| Action | File |
|---|---|
| Optional Item 1: Add one line | `CLAUDE.md` |
| Optional Item 2: Add two lines | `Team Knowledge/Core/Guidelines/GL-014_AI Team Governance.md` |

### Explicit exclusions

- No other files are modified
- No GL-005, GL-004, or other GL files are modified unless Owner approves a separate optional item
- No AGENT.md files are modified
- No Workstream files are modified
- No scripts are modified
- No databases are modified (except required audit trail entries after execution)
- No credentials, `.env` files, or live system changes
- No team_tasks or team_log entries until after execution is confirmed

---

## 8. Post-Check Plan

After execution (if approved), the executor must verify:

1. `SOP-015_Proposal Iteration Protocol for System File Changes.md` exists at the canonical path
2. File content matches §4 exactly — spot-check: Purpose, Step 5, Approval Gate, Changelog
3. `SOP-index.md` contains the new SOP-015 row
4. Step 12c in SOP-001 is unchanged (unrelated file — confirm no accidental edit)
5. No secret values appear in SOP-015
6. If Optional Items were approved: verify the exact added text in CLAUDE.md and/or GL-014

---

## 9. Risks and Mitigations

| Risk | Level | Mitigation |
|---|---|---|
| SOP-015 content drifts from accepted triage v02 during implementation | Low | §4 contains the exact full text; executor uses it verbatim |
| SOP number conflicts with an undiscovered file | Very low | `ls` of SOPs folder confirmed SOP-014 is the highest; no SOP-015 file exists |
| SOP-index row uses wrong file path | Low | Exact row text provided in §5; executor uses exact text match |
| Optional items approved but applied inconsistently | Low | Each optional item has exact proposed text; scope is one or two lines only |
| SOP becomes stale if proposal patterns evolve | Low | Changelog section in SOP-015 enables future updates via normal SOP change process |

---

## 10. Owner Decision Options

| Option | Description |
|---|---|
| **A — Approve SOP implementation only** | Execute core scope only: create SOP-015 and update SOP-index.md. Optional Items 1 and 2 are not executed. |
| **B — Approve SOP implementation plus optional reference updates** | Execute core scope plus any combination of Optional Item 1 (CLAUDE.md), Optional Item 2 (GL-014), or both. Owner names which optional items are approved. |
| **C — Request amendments** | Owner returns corrections to the proposed SOP content in §4, the index update in §5, or any other section. Larry produces a revised proposal. No implementation until a version is approved. |
| **D — Defer** | No action taken now. Triage v02 remains on record. |
| **E — Reject** | SOP-015 is not created. Pattern continues by convention only. |

**Larry's recommendation: Option B — core scope plus Optional Item 1 (CLAUDE.md).**

Optional Item 2 (GL-014) is lower priority: agents who read GL-014 §1 are already in the approval-gate context and are unlikely to miss SOP-015. Optional Item 1 (CLAUDE.md) is higher priority because CLAUDE.md is the primary context document for all agents and a one-line reference there maximises discoverability at the lowest risk.

---

## 11. Approval Gate

No implementation may happen until Owner Walter Kamer explicitly approves this proposal.

Approving Option A from the triage report (preparing this proposal) does not constitute implementation approval. Implementation requires a separate explicit decision from the options in §10.

This document is a proposal only. No files have been created or modified. SOP-015 does not yet exist. SOP-index.md has not been updated.

---

*Delivered on: 2026-06-03*  
*Delivered at: Deliverables/20260603_Core_AI Team Audit Report/graduation-candidate-1-sop-015-implementation-proposal.md*
