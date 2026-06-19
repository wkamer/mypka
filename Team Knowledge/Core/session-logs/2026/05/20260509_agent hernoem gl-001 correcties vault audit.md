# Agent hernoem, CLAUDE.md verrijking, GL-001 correcties, vault audit

**Date:** 2026-05-09
**Session ID:** 38
**Topics:** naamgeving, vault-audit, agent-structuur, gl-001

## Summary

Alle agent CLAUDE.md bestanden hernoemd naar AGENT.md. Root CLAUDE.md verrijkt met Progress Over Perfection, Hard Rules, Larry's Three Duties en "never say no hire for it" principe vanuit scaffold. GL-001 gecorrigeerd: P-Naam, T-Naam, KE-Naam, G-Titel (map), Python snake_case. Alle conflicterende memories gesynchroniseerd naar GL-001 als SSOT. Vault-audit: 41 violations gevonden, alle niet-script violations opgelost.

## Decisions

- Agent instructiebestanden heten AGENT.md (niet AGENTS.md of CLAUDE.md)
- GL-001 is SSOT voor naamgeving — memories volgen GL-001, niet andersom
- Goals worden mappen: G-Titel/
- Python scripts: snake_case; PowerShell: kebab-case
- INCOME AND EXPENSES.md hoort bij Key Elements, niet Documents

## Actions taken

- 8 agent CLAUDE.md → AGENT.md hernoemd
- agent-index.md bijgewerkt
- Root CLAUDE.md: 3 secties toegevoegd vanuit scaffold
- GL-001 bijgewerkt: Goal convention + Python snake_case
- 5 memory bestanden gecorrigeerd naar GL-001
- 33 session logs verplaatst naar YYYY/MM/ nesting
- Image 20260502 hernoemd (koppeltekens → spaties)
- Geldstroom one pager _v1 suffix verwijderd
- INCOME AND EXPENSES.md → KE-Finance data.md in Key Elements
- Penn: journal entry Kyara geschreven, CRM stub aangemaakt

## Delegations

- Penn — journal entry over Kyara en scheiding

## Open items

- /start-session en /close-session skills verwijzen nog naar oude paden
- session_open.py controleren op nieuwe DB-paden
