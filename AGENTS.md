# AGENTS.md — myPKA System Context for Codex CLI

This file is the Codex CLI equivalent of CLAUDE.md. It is read automatically on startup and gives every Codex invocation full awareness of the myPKA system without requiring clarification rounds.

---

## What this system is

myPKA is a personal knowledge and action system running on a Raspberry Pi 5 (Linux 6.12, ARM64, bash) at `/opt/myPKA`. It is operated by a team of AI specialists coordinated by an orchestrator named Larry. The system covers personal life management, two business domains (Kamer E-commerce and Geldstroom Regie), and the infrastructure that connects them. Claude Code (claude-sonnet-4-6) is the primary AI runtime. Codex CLI is a secondary agent invoked for specific coding and infrastructure tasks.

---

## Directory map

All paths are absolute from `/opt/myPKA/`.

```
/opt/myPKA/
  CLAUDE.md                         Primary context file for Claude Code (authoritative team and routing rules)
  AGENTS.md                         This file — Codex CLI equivalent of CLAUDE.md
  Team/                             One folder per AI specialist, each with AGENT.md
  Team Inbox/                       Flat input queue — owner drops files here for processing (no subfolders)
  Team Knowledge/                   All shared domain knowledge, SOPs, guidelines, integrations
    Core/                           Cross-domain infrastructure and team-level knowledge
      active-context.md             Current goals, open items, last session — read at session start
      Guidelines/                   GL-NNN_*.md files — operating principles and architecture decisions
      SOPs/                         SOP-NNN_*.md files — step-by-step procedures
      Integrations/                 One folder per integration (google, discord, dropbox, meta, shopify, todoist, n8n, whisper, claude, mypka-ollama)
        ADRs/                       Architecture Decision Records
        service-catalog.md          Every running service: purpose, image, port, config, backup status
        integration-map.md          Which system connects to which, via which protocol
      Services/                     Internal daemons (e.g. team-inbox-watcher)
      Scripts/                      Shared utility scripts (db_helper.py, backup_sqlite_dbs.sh, etc.)
      Templates/                    Reusable file templates
      session-logs/                 YYYY/MM/YYYYMMDD_slug.md — mirror of session_logs DB rows
    Kamer E-commerce/               E-commerce business domain knowledge + DB
    Geldstroom Regie/               Financial coaching business domain knowledge + DB
  PKM/                              Personal Knowledge Management
    My Life/
      Goals/                        G-Title/ folders — one per active life goal
      Projects/                     P-Projectnaam/ folders — personal projects
      Topics/                       T-Onderwerp.md files — topic reference notes
      Key Elements/                 KE-Domein.md files — standing resources (finance, health, etc.)
      Ideas/                        Unprocessed ideas
      Habits/                       Habit tracking
  Deliverables/                     Active output artifacts — YYYYMMDD_Domain_beschrijving/
    Archive/                        Completed deliverables — folder name is the record
```

External services run under `/opt/` on the host:

```
/opt/n8n/                           n8n automation platform (Docker Compose)
/opt/memory-db/                     pgvector PostgreSQL for AI memory (Docker Compose)
```

---

## Naming conventions

| Type | Format | Example |
|---|---|---|
| Projects | `P-Projectnaam` | `P-Nieuwe Plek` |
| Goals | `G-Titel/` (folder) | `G-Scheiding volledig afgerond/` |
| Topics | `T-Onderwerp.md` | `T-AI.md` |
| Key Elements | `KE-Domein.md` | `KE-Finance data.md` |
| SOPs | `SOP-NNN_omschrijving.md` | `SOP-001_Disaster recovery.md` |
| Guidelines | `GL-NNN_omschrijving.md` | `GL-004_Canonical paths.md` |
| Deliverables | `YYYYMMDD_Domain_beschrijving/` | `20260603_Core_AI Team Audit Report/` |
| Session logs | `YYYYMMDD_slug.md` | `20260617_codex-setup.md` |
| ADRs | `ADR-NNN_title.md` | inside `Integrations/ADRs/` |

**Prefixes are meaningful and reserved.** Never use `KE-` for anything other than a Key Element file. Never use `SOP-` or `GL-` for freeform notes.

---

## Databases

Four SQLite databases. All paths relative to `/opt/myPKA/`.

| Database | Path | Owner | Purpose |
|---|---|---|---|
| team-knowledge.db | `Team Knowledge/team-knowledge.db` | Larry | Core team operations |
| personal.db | `PKM/personal.db` | Sienna, Penn | Owner's personal domain |
| kamer e-commerce.db | `Team Knowledge/Kamer E-commerce/kamer e-commerce.db` | Sasha, Vera | E-commerce business |
| geldstroom-regie.db | `Team Knowledge/Geldstroom Regie/geldstroom-regie.db` | Finn, Vera | Financial coaching business |

### team-knowledge.db — tables

| Table | Purpose |
|---|---|
| `session_logs` | Every AI session: date, title, summary, decisions, actions, open items, agent |
| `team_tasks` | Internal delegation tracker: title, assignee, status, priority, due_date, notes, linked_journal_entries |
| `team_log` | Structured log entries per specialist |
| `agent_learnings` | Per-agent learning records linked to session |
| `delegation_outcomes` | Outcomes of delegations between agents |
| `deliverable_lifecycle` | Lifecycle state of deliverable artifacts |
| `learning_candidates` | Flagged insights awaiting triage and graduation |

### personal.db — tables

personal.db carries the same structural tables as team-knowledge.db (`session_logs`, `team_log`, `agent_learnings`, `delegation_outcomes`, `team_tasks`) — these are replicated per database, not shared. In addition it has its own personal domain tables:

| Table | Purpose |
|---|---|
| `journal` | Penn's journal entries: date, slug, title, body, entry_type, mood, tags, markdown_path |
| `people` | CRM: name, voornaam, achternaam, birthday, last_contact, summary |
| `contact_interactions` | Interactions linked to people and journal entries |
| `daily_growth` | Daily check-ins: sport, slaap, eten, leren, miracle_roadmap_les |
| `documents` | Filed documents linked to people, with OCR text |
| `document_mentions` | Links documents to journal entries and notes |
| `habits` | Habit definitions and status |
| `notes` | Standalone notes with mention count and source tracking |

**Access via Python only** — `sqlite3` binary is not installed on this host. Use `python3 -c "import sqlite3; ..."` or a script that imports sqlite3.

---

## Integration scripts

Scripts live inside their integration folder, not in a shared Scripts/ root. Pattern:

```
Team Knowledge/Core/Integrations/<name>/
  config.md             Auth, usage, rate limits
  connection.py         Reusable auth/connection module
  *_handler.py / *.sh  Domain handlers at root level — no Scripts/ subfolder
  .env                  Credentials (never in git)
  .env.example          Template for credentials
  logs/                 All log output for this integration
```

Active integrations: `google`, `discord`, `dropbox`, `meta`, `shopify`, `todoist`, `n8n`, `whisper`, `claude`, `mypka-ollama`.

Key utility: `Team Knowledge/Core/Integrations/google/google_helper.py` — all Google API calls go through this. Never bypass it with direct API calls or MCP integrations.

Shared utility scripts: `Team Knowledge/Core/Scripts/` — db_helper.py, backup_sqlite_dbs.sh, add_task.py, complete_task.py, update_task.py, etc.

---

## Running services

| Service | Type | Purpose |
|---|---|---|
| n8n | Docker container | Automation platform, all workflows and webhooks |
| n8n-postgres | Docker container | PostgreSQL backing n8n state and credentials |
| memory-db | Docker container | pgvector PostgreSQL for AI memory (ARM64) |
| cloudflared | Docker container | Cloudflare Tunnel — sole external access path |
| mypka-ai-bridge | Systemd / Python | HTTP bridge from Discord/CLI to Claude API |
| mypka-discord-bridge | Systemd / Python | Discord bot forwarding messages to ai-bridge |
| mypka-meta-bridge | Systemd / Python | Meta (WhatsApp/Instagram) bridge |
| team-inbox-watcher | Systemd / Python | Watches Team Inbox/ and notifies team |

Config locations: n8n and memory-db at `/opt/n8n/` and `/opt/memory-db/` respectively. All service detail in `Team Knowledge/Core/Integrations/service-catalog.md`.

---

## What NEVER to delete or overwrite

These files and directories are the structural backbone of the system. Deleting or overwriting them without owner confirmation is an irreversible destructive action.

- `CLAUDE.md` — primary system prompt for Claude Code
- `AGENTS.md` — this file
- `Team Knowledge/Core/active-context.md` — live session state
- `Team Knowledge/Core/Guidelines/GL-004_Canonical paths.md` — authoritative path registry
- Any `AGENT.md` inside `Team/` — specialist definitions
- Any `*.db` file — databases contain all operational history
- `Team Knowledge/Core/Integrations/service-catalog.md` — service registry
- `Team Knowledge/Core/Integrations/integration-map.md` — integration map
- `PKM/My Life/Goals/` — owner's active life goals
- `Deliverables/` and `Deliverables/Archive/` — completed and active work artifacts

Never truncate, overwrite, or `DROP TABLE` on any database without an explicit owner instruction and a backup confirmed to exist.

---

## Dangerous operations — always require human confirmation

The following actions are irreversible on this live system. Propose, wait for confirmation, then execute.

1. **Delete or rename** any file in `Team/`, `Team Knowledge/Core/`, `PKM/My Life/Goals/`, or `Deliverables/`
2. **Modify a database schema** — `ALTER TABLE`, `DROP TABLE`, new columns on production tables
3. **Deploy or restart a Docker service** — affects live integrations
4. **Modify crontab** — currently active scheduled jobs
5. **Change any `.env` file** — credentials for live systems
6. **Push to any external system** (Todoist, Discord, Gmail, Shopify) in a non-read-only operation
7. **Modify `CLAUDE.md` or any `AGENT.md`** — changes team behavior immediately
8. **Touch `/opt/n8n/` or `/opt/memory-db/`** — production service configs

When uncertain whether an action is reversible: treat it as dangerous and ask first.

---

## Language rule

**System files, scripts, variable names, function names, database column names, and all console output must be in English.** No exceptions. Dutch appears only in owner-facing content (journal entries, project descriptions, personal notes, and the owner's own input). When writing code or scripts, all identifiers are English even when the surrounding context is Dutch.

---

## How Codex should behave on this system

- **Suggest mode by default.** This is a live personal system on production hardware. Propose changes and wait for confirmation before writing files, executing scripts, or modifying state.
- **Read before writing.** Always read an existing file before proposing edits. Never overwrite blind.
- **No full-auto on live integrations.** Any action that touches an external API, database, Docker service, or crontab requires an explicit go-ahead.
- **Check canonical paths first.** Before creating a new file or folder, verify it belongs at `Team Knowledge/Core/Guidelines/GL-004_Canonical paths.md`. Do not invent new top-level locations.
- **Use Python for SQLite, not the sqlite3 binary.** The sqlite3 CLI is not installed. Access databases via `python3` with `import sqlite3`.
- **Simplest solution first.** Before proposing n8n, a new service, or a new script, check whether an existing script, handler, or cron job can be extended. Overengineering is a failure mode on a single-host Raspberry Pi.
- **Never hardcode credentials.** All secrets go in `.env` files inside the relevant integration folder. Never in scripts, never in git.
- **Handlers at root level of integration folder.** No `Scripts/` subfolder inside integration folders. See `Team Knowledge/Core/Integrations/meta/` as the reference implementation.

---

## Relationship to CLAUDE.md

`CLAUDE.md` is the primary context file for Claude Code. It defines team structure, routing rules, task systems, naming conventions, and the three hard stops. AGENTS.md is its Codex CLI counterpart — it covers the same system but from an infrastructure and technical orientation.

If CLAUDE.md and AGENTS.md contradict each other on team or routing rules, CLAUDE.md takes precedence. If they contradict on technical architecture or file layout, AGENTS.md takes precedence as it was written from direct inspection of the live system.

When in doubt about team behavior, routing, or owner interaction patterns: read `CLAUDE.md`. When in doubt about where a file goes, what a database contains, or which script to call: this file is authoritative.
