# n8n Workflow Runbook

**Eigenaar:** Kai — The Integration Architect
**n8n URL:** https://n8n.kmerbase.com (intern: http://localhost:5678)
**API key:** zie `/opt/n8n/mypka-ai-bridge.env` → `N8N_API_KEY`

---

## Domein-workflows

| ID | Naam | Status | Trigger |
|---|---|---|---|
| OkKsUhh7nu0wdqHR | Team | Actief | Webhook `POST /webhook/team-inbox` |
| 8yogebQ4BdHZV2Zp | Personal | Inactief (skelet) | — |
| xYImeiTf2OAPEm52 | Kamer E-commerce | Inactief (skelet) | — |
| 7GCHkPTGMZ6iBwsC | Geldstroom Regie | Inactief (skelet) | — |

---

## Team workflow — Team Inbox → Discord

**Wat het doet:** Zodra een nieuw bestand in `/opt/myPKA/Team Inbox/` verschijnt, post de workflow een Discord-notificatie in channel `1505520574024388691`.

**Architectuur:**
```
inotifywait (host) → POST /webhook/team-inbox → n8n Team workflow → Discord API
```

**Onderdelen:**

| Bestand | Locatie | Doel |
|---|---|---|
| `team-inbox-watcher.sh` | `/opt/n8n/` | inotifywait → webhook caller |
| `team-inbox-watcher.service` | `/etc/systemd/system/` | Systemd service (autostart) |

**Service beheer:**
```bash
systemctl status team-inbox-watcher
systemctl restart team-inbox-watcher
journalctl -u team-inbox-watcher -f
```

**Testen:**
```bash
touch "/opt/myPKA/Team Inbox/test-$(date +%s).txt"
# Verwacht: Discord-bericht binnen 2 seconden
```

---

## Uitbreiden

### Nieuw proces toevoegen aan een domein-workflow
1. Open n8n UI → workflow van het domein
2. Voeg nodes toe na de trigger of als parallelle tak
3. Activeer de workflow als die nog inactief was

### Nieuw domein-proces via API
Gebruik het script `Team Knowledge/Core/Scripts/create_n8n_domain_workflows.py` als referentie. Voeg een PUT-call toe voor het betreffende workflow-ID.

---

*Aangemaakt: 2026-05-18 | Kai*
