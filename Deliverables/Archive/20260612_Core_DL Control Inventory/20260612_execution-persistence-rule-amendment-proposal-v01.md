# Execution Persistence Rule — Governance Amendment Proposal v01

**Date:** 2026-06-12
**Prepared by:** Larry, Team Orchestrator
**Type:** Governance amendment proposal — read-only
**Placement:** G2 — file inside `20260612_Core_DL Control Inventory/`
**Status:** Awaiting Owner review and approval. No execution performed.

**Read-only declaration:** No files, folders, databases, lifecycle records, or indexes
were modified during the preparation of this document.

---

## 1. Problem Statement

Write plans and execution results are currently sometimes returned in chat only.
This creates audit-trail gaps that require retroactive repair (as happened with
Pilot A: two correction sessions needed after the fact).

The root cause is that existing conventions do not explicitly require persisted
audit artifacts for execution work. "No extra files" language in task constraints
was interpreted as blocking write plans and execution reports. It must not do so.

---

## 2. Where the Rule Should Be Added

**Primary location: `CLAUDE.md` — Operational Conventions section**

Rationale:
- CLAUDE.md is read by every agent at session start. A rule here applies immediately
  to all execution work across all domains without requiring agents to read a separate GL.
- The rule is short enough to embed directly without bloating the file.
- The existing "Session Context Hygiene" subsection is the closest related topic.
  The new section slots in after it.

**No separate GL or SOP required** for the minimal implementation. If the rule proves
to need domain-specific detail, a GL may be drafted later. That is a future decision.

**Exact insertion point in `CLAUDE.md`:**
After the subsection `### Session Context Hygiene` and before `### Google, Sheets & Email`.

---

## 3. Exact Text to Add

Add the following subsection verbatim after `### Session Context Hygiene`:

```
### Execution Persistence Rule

For every execution that changes files, folders, database records, routing, archive
state, lifecycle state, SOPs, Guidelines, CLAUDE.md, memory summaries, or task state:

1. A persisted write plan file is required before Owner authorization. Owner
   authorization must reference the persisted write plan file by path. Waiver
   requires explicit Owner instruction.
2. A persisted execution report file is required immediately after execution completes.
   Chat-only results are not sufficient. Waiver requires explicit Owner instruction.
3. "No extra files" or "no new files" constraints in a task brief never block write
   plans or execution reports. These are required audit artifacts, not task output.
4. Close-session summaries may reference execution but do not replace execution reports.
5. If execution completes without a persisted execution report, the next action before
   any further work is to repair the audit trail.
```

---

## 4. What the Text Does Not Change

- "No extra files" constraints for task output remain valid. The carve-out is narrow:
  write plans and execution reports only.
- G2 placement rule for audit artifacts is unchanged. Write plans and execution reports
  inside a cleanup cycle still go into the active containment folder, not standalone
  folders.
- Owner waiver is always available for both artifacts. This rule sets the default,
  not a hard gate.
- No change to how specialists handle borging. This rule applies to Larry-orchestrated
  execution briefings and to specialists who execute writes directly.

---

## 5. Smallest Safe Implementation Plan

Three steps. No parallel execution.

**Step 1 — Owner approves this proposal**
Owner confirms: (a) the exact text in Section 3, (b) the insertion point after
`### Session Context Hygiene`. If changes are needed, produce v02 before step 2.

**Step 2 — Write the amendment**
Larry edits `CLAUDE.md`. Single Edit operation. Exact text from Section 3. No other
changes to the file.

**Step 3 — Read back and confirm**
Larry reads the amended section back and confirms the text is correct. Reports the
result to Owner.

No GL, no SOP, no index update, no session log entry beyond what `/close-session`
already captures.

---

## 6. Explicit Non-Actions

The following were not performed during the preparation of this document and must not
be performed before Owner approves:

- No edit to `CLAUDE.md`
- No new GL or SOP created
- No archive action
- No lifecycle record update
- No routing
- No Learning Candidate triage
- No dashboard work
- No Batch 2 execution
- No sweep
- No new folders created

---

Delivered on: 2026-06-12
Delivered at: `Deliverables/20260612_Core_DL Control Inventory/20260612_execution-persistence-rule-amendment-proposal-v01.md`
