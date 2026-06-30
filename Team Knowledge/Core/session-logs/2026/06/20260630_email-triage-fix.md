# Email Triage Fix — PATH + Markdown Fence

**Date:** 2026-06-30
**Agent:** Larry
**Domain:** Team

## What happened

Run Triage in het dashboard toonde alleen de seed mail na klikken op de knop. Alle echte inbox emails kregen `triage_error` status en werden niet getoond in de UI.

Root cause was dubbel:

1. **PATH issue** — de backend systemd service draait met `PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin`. `/home/admin/.local/bin` ontbreekt. De `_call_ai()` functie in `ai.py` riep `["claude", "-p", prompt]` aan, wat `FileNotFoundError` gooide. Die exception werd silent gecatcht en het email kreeg `triage_error`.

2. **Markdown fence issue** — na de PATH fix faalden nog 7 emails. Claude antwoordt soms met JSON gewrapped in markdown fences (` ```json ... ``` `) ondanks de system prompt. `json.loads()` faalde op de ruwe output.

**Larry routing failure:** Larry heeft zelf diagnose gedaan, bestanden gelezen en code gewijzigd in plaats van direct naar Devon te routen. Dit is buiten Larry's rol.

## Decisions

- Absolute path `/home/admin/.local/bin/claude` gebruiken in `ai.py` in plaats van `claude`
- Regex toegevoegd aan `_call_ai()` om markdown fences te strippen voor `json.loads()`

## Actions taken

- `ai.py` gewijzigd: absolute claude path + fence stripping
- Backend herstart via `mypka-dashboard-backend.service`
- Seed mail (`smoke-test-001`, Sarah Manager) verwijderd uit DB inclusief 8 action rows
- Run triage uitgevoerd: 24/24 inbox emails nu pending
- Commit 4301673 gepusht

## Open items

Geen.
