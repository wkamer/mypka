# GL-025 — Todoist Projects Reference

**Applies to:** Larry and all agents that create or route tasks to Todoist
**Source:** Migrated from CLAUDE.md Task Systems section — team_task 113

---

## Todoist — Owner's Personal Task Manager

Todoist is owner-facing only. Agents write to Todoist on the owner's behalf. Owner acts on Todoist tasks. Agents never act on Todoist tasks themselves.

| Domain | Todoist project | ID |
|--------|----------------|----|
| Personal tasks | `👤 PERSONAL` | `6cFcm2MpmHvc2F3H` |
| Personal projects | `👤 PROJECTS` | `6c8XR7HXhgMWMWwj` |
| Kamer E-commerce | `💼 KAMER E-COMMERCE` | `6fC99W283Jw2cjV2` |
| Kamer E-commerce projects | submap | `6gfFMpGVh5WJHPCx` |
| Geldstroom Regie | `💼 GELDSTROOM REGIE` | `6gfFMpHcMCQvPQpc` |
| Geldstroom Regie projects | submap | `6gfFMpmXQ3RCGgMC` |

**API base:** `https://api.todoist.com/api/v1/`

**Move task:** `POST /api/v1/tasks/{id}/move` with `project_id` + `section_id`. PATCH/POST on task does not move it.

**Resource tasks:** Use `* ` prefix (asterisk + space) so the task renders without a checkbox.

**File path in task description:** `[Open](file://raspberrypi.local/myPKA/path%20with%20spaces/)`

---

## team_tasks — Internal Delegation Tracker

`team_tasks` is an internal table in `team-knowledge.db`. It tracks work delegated between Larry and specialists. The owner never acts on team_tasks entries. These are agent-to-agent records, not owner tasks.

---

## Changelog

- 2026-06-29 (Larry): Created. Migrated from CLAUDE.md Task Systems section as part of CLAUDE.md runtime cleanup — team_task 113, Iris review 2026-06-29.
