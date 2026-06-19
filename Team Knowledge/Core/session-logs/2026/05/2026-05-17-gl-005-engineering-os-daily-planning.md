# End-of-Day Routine — Engineering OS & Daily Planning — 17 mei 2026

**Date:** 2026-05-17
**Agent:** Larry
**Topics:** routine, end-of-day, gl-005, engineering, daily-planning

## Summary

GL-005 AI Engineering Operating System aangemaakt als teamwijde engineering standaard, bewaakt door Larry. Todoist API bug gevonden en opgelost: `due_date=None` werkt niet, `due_string="no date"` is de correcte methode. Statusline bijgewerkt via statusline-setup agent. Daily Planning workflow voor Todoist uitgewerkt via persistente scripts.

## Decisions

- GL-005 Engineering OS ingevoerd als teamwijde standaard
- `due_string="no date"` is canonical methode voor backlog in Todoist API
- Bestaande planning scripts zijn technische schuld (geen tests, typing, linting)

## Actions taken

- GL-005 aangemaakt in `Team Knowledge/Core/Guidelines/`
- `gl-index.md` bijgewerkt
- `get_all_today_tasks.py`, `get_tomorrow_tasks.py`, planning scripts aangemaakt
- Todoist `due_date=None` bug opgelost
- Statusline fix uitgevoerd

## Delegations

Penn — journal entry Kyara

## Open items

Planning scripts voldoen niet aan GL-005 standaard (geen tests, mypy, ruff). Cleanup nodig.

---

*Delivered on:* 2026-05-17
