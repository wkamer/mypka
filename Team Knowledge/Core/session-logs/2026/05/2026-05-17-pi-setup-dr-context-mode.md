---
session_id: 57
session_date: 2026-05-17
session_title: Pi setup — DR doorlopen, context-mode geïnstalleerd
agent_slug: larry
topics: disaster-recovery, raspberry-pi, context-mode, tooling
---

## Samenvatting

De DR voor het overzetten van myPKA naar de Raspberry Pi is stap voor stap doorgelopen. TODOIST_API_TOKEN is toegevoegd aan `~/.claude/settings.json`. Python Google-libs zijn geïnstalleerd via apt. De scottconverse context-mode plugin is vervangen door de originele mksglu/context-mode (v1.0.135). De DR is op drie punten bijgewerkt: juiste plugin-referentie, bug fix sectie verwijderd, en platform-specifieke apt-instructies voor Pi/Linux toegevoegd.

## Besluiten

- mksglu/context-mode is de standaard plugin, niet scottconverse
- Python Google-deps op Pi/Linux via apt, niet pip3

## Acties

- TODOIST_API_TOKEN toegevoegd aan `~/.claude/settings.json`
- Python Google-libs geïnstalleerd (`python3-google-auth`, `python3-google-auth-oauthlib`, `python3-googleapi`, `python3-google-api-core`)
- scottconverse context-mode verwijderd, mksglu/context-mode v1.0.135 geïnstalleerd
- `SOP-001_Disaster recovery.md` bijgewerkt op 3 punten

## Delegaties

- Sienna — Gmail inbox opgehaald (10 items, geen ongelezen)
- Sienna — Todoist taken opgehaald (5 taken voor 17 mei)

## Open items

- n8n nog niet geïnstalleerd (stap 11 DR)
- Claude Code herstart nodig voor context-mode activatie
