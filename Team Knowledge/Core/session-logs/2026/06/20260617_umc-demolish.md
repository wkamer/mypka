# Session Log — 2026-06-17

**Slug:** umc-demolish
**Agent:** Larry
**Domain:** Core

## What happened

UMC infrastructuur volledig verwijderd na bevestiging dat 234 markdown session log mirrors bestaan (periode 2026-04-30 tot 2026-06-17).

## Removed

- Docker container `memory-db` (pgvector/pgvector:pg16)
- Docker volume `memory_db_data`
- `/opt/mypka-memory/` (venv + docker-compose)
- `Team Knowledge/Core/Integrations/memory-db/` (memory_manager.py, memory_config.py, alle scripts)

## Not removed

- Ollama — niet bereikbaar, skip
- WhatsApp export handler — UMC-aanroep is non-fatal, werkt gewoon door
- AGENT.md UMC-referenties — non-urgent, open item

## Open items

- Clean UMC references from specialist AGENT.md files (non-urgent)
