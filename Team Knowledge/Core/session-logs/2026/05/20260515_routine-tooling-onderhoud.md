# Routine & tooling onderhoud — 2026-05-15

**DB:** `Team Knowledge/team-knowledge.db` — session_log id: 50
**Agent:** larry
**Topics:** routine, tooling, sop, daily-planning, memory

## Summary

Sessie 2026-05-15: groot onderhoud aan routines en tooling. db_helper.py aangemaakt voor relatieve DB-paden. SOP-001 Disaster Recovery herschreven als platform-agnostisch (Windows/macOS/Linux/Pi). start-daily-planning volledig herschreven naar Daily Planning V1 SOP (12 stappen, top-down, Highlight+Supporting). Consistentiecheck toegevoegd aan alle routines (start-morning/afternoon/end-of-day). Memory-junction geborgd in DR. Feedback memory: always journal, numbered choices, goal movement numbered, inline option format.

## Decisions

- Daily Planning V1 is SSOT voor alle taakbeheer in routines
- Routines bevatten geen taakbeheer meer zelf
- Morning routine mag organisch groeien (geen vaste blokken per dag)
- Altijd journalen na dag reflectie (geen vraag)

## Actions taken

- db_helper.py aangemaakt
- SOP-001 platform-agnostisch herschreven
- start-daily-planning volledig herschreven (12 stappen)
- Consistentiecheck toegevoegd aan alle 3 start-routines
- Memory feedback opgeslagen: numbered choices, always journal, goal movement numbered
- Afternoon Routine gemist gelogd in session_logs

## Delegations

Penn — journaalentry 2026-05-15

## Open items

- Raspberry Pi 5 setup nog te doen (plan klaar via Nolan: piped-munching-tarjan.md)
