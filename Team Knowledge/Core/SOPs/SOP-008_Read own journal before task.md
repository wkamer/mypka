# SOP-008 — Read Own Journal Before Task

**Owner:** Every specialist (self-executed before any task)
**Trigger:** Receiving a task from `team_tasks` that has `linked_journal_entries` populated

---

## Purpose

Load durable priors before executing a task. A specialist who ignores their own journal repeats mistakes and re-derives lessons already learned. A specialist who reads their journal before starting arrives with compounded experience.

---

## Procedure

1. **Open the task.** Read the `linked_journal_entries` field.
2. **For each entry listed:** open `Team/<your-name>/journal/<entry-slug>.md`
3. **Read three sections in full:**
   - `## What I learned` — the insight
   - `## When this applies` — confirm this task matches
   - `## When this does NOT apply` — check for exceptions
4. **Update the task `notes` field** with: `Priors loaded: [[entry-1]], [[entry-2]]`
   - This makes prior-loading auditable across sessions
5. **Proceed with the task**, carrying the priors as active context

## When no journal entries are linked

Proceed without prior-loading. After task completion, evaluate whether a journal entry should be written (see [[SOP-009_Write journal entry after task]]).

---

*Created: 2026-06-03 | Owner: all specialists*
