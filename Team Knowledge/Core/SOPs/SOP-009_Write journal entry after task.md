# SOP-009 — Write Journal Entry After Task

**Owner:** Every specialist (self-executed after any task that produced a durable insight)
**Trigger:** Task closing — if something durable was learned

---

## Purpose

Distill task experience into durable specialist memory. A journal entry is not a task summary — it is a permanent insight the specialist will carry into every future relevant task. The test: would knowing this before the task have changed how it was approached?

---

## When to write a journal entry

Write one if any of these are true:
- A decision was made that will recur in future tasks
- A tool, API, or integration behaved unexpectedly — and the fix is reusable
- A pattern emerged that the specialist should recognize immediately next time
- The owner gave feedback that changed approach (positive or negative)
- A mistake was made that a prior would have prevented

Do NOT write an entry for:
- Routine task execution with no new insight
- One-off decisions that will never recur
- Information already captured in a GL, SOP, or WS

---

## Procedure

1. **Name the insight** — one sentence that IS the title. Direct and specific.
   - Good: "Todoist /move endpoint requires both project_id and section_id — PATCH on task ignores project_id"
   - Bad: "Todoist API has quirks"

2. **Create the file** at `Team/<your-name>/journal/YYYY-MM-DD_<slug>.md`
   - Use the template at `Team/<your-name>/journal/_template.md`

3. **Fill the four sections:**
   - `## What I learned` — the insight, direct, no hedging
   - `## When this applies` — specific conditions that activate this insight
   - `## When this does NOT apply` — exceptions and edge cases
   - `## Evidence` — `[[wikilinks]]` to the session log, task, or external doc

4. **Link back to the task** — update `linked_journal_entries` in the task row with the new entry slug

5. **Evaluate graduation** — if this insight is "set-in-stone" (permanent rule for the team, not just this specialist), flag it as a graduation candidate at `/close-session`

---

## Quality bar

A journal entry is durable memory. Write it as if you will read it in 6 months with no other context. If the insight is not clear without context, rewrite until it is.

---

*Created: 2026-06-03 | Owner: all specialists*
