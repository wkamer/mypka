# SOP-020 — Project Creation

**Owner:** Larry (orchestration) + Marcus (classification + setup)
**Trigger:** Owner confirms a new initiative via Sienna, Marcus has run ICOR classification, owner approves project creation
**Source:** Migrated from CLAUDE.md Project Creation section — team_task 113

---

## When This SOP Applies

A project is created only after:
1. Sienna confirms the initiative is deliberate (not impulse)
2. Marcus has classified it via ICOR
3. Owner has confirmed the classification

Never create a project without prior classification. Never create blind.

---

## Step-by-Step

**Step 1 — Fetch existing projects**
Check Todoist and the relevant domain project index before creating anything. Confirm the project does not already exist under a different name.

**Step 2 — Create Todoist project**
Create under the correct parent project using the IDs from [[GL-025_todoist-projects]].

Add a Resources section to the Todoist project immediately:
- `* 🎯 G-Naam` — links to the associated Goal (if any)
- `* 📅 Event` — links to any relevant deadline or event (if any)
- `* 📂 P-Naam` — links to the project folder on disk

Resource tasks use the `* ` prefix (asterisk + space) so they render without a checkbox.

File path format in task description: `[Open](file://raspberrypi.local/myPKA/path%20with%20spaces/)`

**Step 3 — Create project folder**
Personal domain: `PKM/My Life/Projects/P-Projectnaam/`
Business domain: use the domain equivalent path from [[GL-004_Canonical paths]].

Folder naming convention: `P-Projectnaam` — see [[GL-001_File naming conventions]].

**Step 4 — Create project.md**
Use the project template from `Team Knowledge/Templates/`. See `Team Knowledge/Templates/INDEX.md` for the correct template.

**Step 5 — Register in project-index.md**
Add one row to the relevant `project-index.md` file for the domain.

---

## Quick Reference

| Item | Format |
|------|--------|
| Folder name | `P-Projectnaam` |
| Todoist IDs | [[GL-025_todoist-projects]] |
| Folder paths | [[GL-004_Canonical paths]] |
| File template | `Team Knowledge/Templates/INDEX.md` |

---

## Changelog

- 2026-06-29 (Larry): Created. Migrated from CLAUDE.md Project Creation section as part of CLAUDE.md runtime cleanup — team_task 113, Iris review 2026-06-29. SOP-019 was already assigned (archived Governance Gatekeeper Procedure); Owner confirmed SOP-020 as replacement number.
