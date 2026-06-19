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
