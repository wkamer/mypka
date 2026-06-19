---
date: 2026-05-18
session_title: n8n workflow architectuur & Team Inbox notificaties
topics: n8n · discord · integratie · gl-006
db: Team Knowledge/team-knowledge.db · session_log id 65
---

# n8n workflow architectuur & Team Inbox notificaties

## Samenvatting

Kai heeft 4 domein-workflows aangemaakt in n8n via de REST API (Team actief, Personal/KE/GR als skelet). De Team workflow gebruikt een webhook trigger — inotifywait op de host detecteert nieuwe bestanden in Team Inbox en roept de webhook aan. Discord notificaties gaan naar `🔔 ┃ team-notifications`. Source-detectie ingebouwd via marker-bestanden: Discord uploads krijgen Source "Discord", directe plaatsingen Source "Direct". GL-006 Notification Format geborgd als universeel teamstandaard met vier velden: Source, Subject, Status, Message.

## Besluiten

- n8n per domein één workflow
- GL-006 als universeel notification format (Source · Subject · Status · Message)
- Marker-bestand aanpak voor source-detectie
- `┃` (box drawing vertical) als standaard scheidingsteken in Discord channel namen

## Acties

- 4 n8n workflows aangemaakt via REST API
- `team-inbox-watcher` systemd service geïnstalleerd
- `mypka-discord-bridge.py` uitgebreid met file upload + marker logica
- GL-006 aangemaakt en geïndexeerd
- `Team Knowledge/Core/Integrations/n8n-workflows.md` runbook geschreven

## Delegaties

- Kai — n8n workflow architectuur (afgerond)

## Open items

—
