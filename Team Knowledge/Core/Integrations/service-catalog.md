# Service Catalog — myPKA Ecosysteem

**Eigenaar:** Kai — Infrastructure & Integration Architect
**Laatste update:** 2026-05-21 (whisper toegevoegd)
**Update-frequentie:** bij elke nieuwe service of wijziging

---

## Draaiende services

### n8n
| Veld | Waarde |
|---|---|
| Doel | Automation platform — alle workflows, webhooks en integraties |
| Type | Docker container |
| Image | `n8nio/n8n:latest` |
| Poort | 5678 (intern), extern via Cloudflare Tunnel |
| Externe URL | `https://n8n.kmerbase.com` |
| Afhankelijkheden | n8n-postgres |
| Volumes | `n8n_data:/home/node/.n8n`, `/opt/myPKA` (mount) |
| Backup | Volume backup vereist — **niet geconfigureerd** |
| Monitoring | **Niet geconfigureerd** — open item |
| Config | `/opt/n8n/docker-compose.yml` |

---

### n8n-postgres
| Veld | Waarde |
|---|---|
| Doel | PostgreSQL database voor n8n workflow-state en credentials |
| Type | Docker container |
| Image | `postgres:16-alpine` |
| Poort | 5432 (intern, niet publiek) |
| Volumes | `postgres_data:/var/lib/postgresql/data` |
| Backup | Volume backup vereist — **niet geconfigureerd** |
| Monitoring | Via n8n health (indirect) |
| Config | `/opt/n8n/docker-compose.yml` |

---

### memory-db
| Veld | Waarde |
|---|---|
| Doel | Vector store + tool output offloading voor het AI-agentsysteem (Memory Core Fase 1) |
| Type | Docker container |
| Image | `pgvector/pgvector:pg16` (ARM64-compatible) |
| Poort | 5432 (intern); optioneel 5433 op host voor script-toegang |
| Netwerk | `memory_internal` (geïsoleerd van n8n) |
| Volumes | `memory_db_data:/var/lib/postgresql/data` |
| Resource limits | 512 MB RAM, 0.50 CPU |
| Backup | `pg_dump` naar `/opt/myPKA/backups/memory-db/` — **zie SOP-007** |
| Monitoring | Healthcheck geconfigureerd; Uptime Kuma **niet geconfigureerd** |
| Config | `Team Knowledge/Core/Integrations/memory-db/docker-compose.yml` |
| Runbook | `[[SOP-007_Memory Core operaties]]` |
| ADR | `[[GL-013_Memory Core Architecture]]` |

---

### cloudflared
| Veld | Waarde |
|---|---|
| Doel | Cloudflare Tunnel — veilige externe toegang zonder open router-poorten |
| Type | Systemd service |
| Binaire | `/usr/bin/cloudflared` |
| Config | `/etc/cloudflared/config.yml` |
| Tunnel | `81fd0d06-fa9b-414b-9ee0-6286f2ce3935` |
| Routering | `n8n.kmerbase.com` → `http://127.0.0.1:5678` |
| Afhankelijkheden | n8n |
| Backup | Config in git vereist — **status onbekend** |
| Monitoring | **Niet geconfigureerd** — open item |

---

### mypka-ai-bridge
| Veld | Waarde |
|---|---|
| Doel | HTTP gateway die Claude Code CLI aanroept vanuit n8n — AI responses via HTTP |
| Type | Systemd service |
| Script | `/opt/n8n/mypka-ai-bridge.py` |
| Poort | 8765 (default via `BRIDGE_PORT` env var) |
| Afhankelijkheden | Claude Code CLI, `/opt/myPKA` |
| Backup | Script in `/opt/n8n/` — **niet in git** |
| Monitoring | **Niet geconfigureerd** |

---

### mypka-discord-bridge
| Veld | Waarde |
|---|---|
| Doel | Discord bot — berichten van Discord naar AI bridge en terug |
| Type | Systemd service |
| Script | `/opt/n8n/mypka-discord-bridge.py` |
| Runtime | Python venv (`/opt/n8n/venv`) |
| Afhankelijkheden | Discord bot token, mypka-ai-bridge |
| Backup | Script in `/opt/n8n/` — **niet in git** |
| Monitoring | **Niet geconfigureerd** |

---

### mypka-meta-bridge
| Veld | Waarde |
|---|---|
| Doel | HTTP wrapper voor Meta Graph API — gebruikt door n8n workflows |
| Type | Systemd service |
| Script | `/opt/n8n/mypka-meta-bridge.py` |
| Poort | 8766 (default via `BRIDGE_PORT` env var) |
| Afhankelijkheden | Meta Graph API credentials |
| Backup | Script in `/opt/n8n/` — **niet in git** |
| Monitoring | **Niet geconfigureerd** |

---

### team-inbox-watcher
| Veld | Waarde |
|---|---|
| Doel | Bewaakt `Team Inbox/` op nieuwe bestanden en stuurt webhook naar n8n |
| Type | Systemd service |
| Script | `/opt/n8n/team-inbox-watcher.sh` |
| Afhankelijkheden | inotifywait, n8n webhook |
| Backup | Script in `/opt/n8n/` — **niet in git** |
| Monitoring | Via n8n workflow (indirect) |

---

## Data stores

| Database | Pad | Eigenaar | Backup |
|---|---|---|---|
| personal.db | `/opt/myPKA/PKM/personal.db` | Sienna / Penn | **Niet geconfigureerd** |
| team-knowledge.db | `/opt/myPKA/Team Knowledge/team-knowledge.db` | Larry | **Niet geconfigureerd** |
| kamer e-commerce.db | `/opt/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db` | Sasha / Vera | **Niet geconfigureerd** |
| geldstroom-regie.db | `/opt/myPKA/Team Knowledge/Geldstroom Regie/geldstroom-regie.db` | Finn | **Niet geconfigureerd** |
| n8n-postgres | Docker volume `postgres_data` | Kai | **Niet geconfigureerd** |
| memory-db | Docker volume `memory_db_data` | Kai | pg_dump — zie SOP-007 |

---

### whisper (voice memo transcriptie)
| Veld | Waarde |
|---|---|
| Doel | Converteert .m4a voice memos naar Markdown transcripten in Team Inbox |
| Type | Python script (cron-driven via sync_handler.sh) |
| Handler | `Team Knowledge/Core/Integrations/whisper/transcribe_handler.py` |
| Python venv | `/opt/whisper/venv/` (eigen venv — handmatig aanmaken bij deploy) |
| Model | `faster-whisper small` op CPU (ARM64 compatible) |
| Input | `/opt/myPKA/Team Inbox/Recorded Audio/*.m4a` |
| Output | `/opt/myPKA/Team Inbox/YYYYMMDD_HHMMSS_voice-memo.md` |
| Trigger | Via `sync_handler.sh` (Dropbox integratie) — elke minuut |
| Logs | `Team Knowledge/Core/Integrations/whisper/logs/transcribe.log` |
| Auth | Geen — volledig lokaal |
| Backup | Script in myPKA — geen separate backup vereist |
| Monitoring | Niet geconfigureerd — log monitoring aanbevolen |
| Runbook | `Team Knowledge/Core/Integrations/whisper/runbook.md` |
| Config | `Team Knowledge/Core/Integrations/whisper/config.md` |

---

## Externe diensten (niet self-hosted)

| Dienst | Gebruik | Integratiemethode |
|---|---|---|
| Todoist | Owner task management | Sync API (REST) |
| Google Calendar | Agenda en events | google_helper.py (OAuth2) |
| Gmail | E-mail lezen en versturen | google_helper.py (OAuth2) |
| Discord | Team notificaties + DM interface | Bot (mypka-discord-bridge) |
| Telegram | Alternatief AI-interface | n8n workflow |
| Shopify (Tricolarae) | E-commerce store | Shopify Admin API (Sasha + Kai) |
| Dropbox | Voice memo transfer (iPhone → Team Inbox → Whisper transcriptie) | rclone OAuth2 (`dropbox:` remote) |
| Meta Graph API | Ads intelligence | mypka-meta-bridge |
| Cloudflare | DNS + Tunnel | cloudflared daemon |

---

## Open items (Kai actie vereist)

1. **Backup configureren** voor alle databases en Docker volumes — geen enkele service heeft actieve backup
2. **Monitoring** — Uptime Kuma deployen en alle services registreren
3. **Poortconflict verifiëren** — mypka-ai-bridge en larry-bridge hebben dezelfde standaardpoort (8765)
4. **Scripts in git** — alle `/opt/n8n/*.py` scripts behoren in version control
5. **Cloudflare Tunnel config in git** — huidige status onbekend
