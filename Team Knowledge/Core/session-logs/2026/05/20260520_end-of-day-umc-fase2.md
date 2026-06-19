# End-of-Day Routine — UMC Fase 2 — 2026-05-20

**Session date:** 2026-05-20
**Topics:** umc, infrastructure, memory, planning, team-learning

## Summary

Vandaag volledig besteed aan de bouw van Unified Memory Core (UMC) Fase 2 voor myPKA. Entity memory geïmplementeerd met upsert-logica en backfill van 36 journal entries (75 entities). Knowledge base geïndexeerd: 758 chunks uit SOPs, Guidelines, Workstreams, AGENT.md, Goals en Key Elements. Conversational memory geïntegreerd in alle close-routines via daily-routines thread. Ollama llama3.2:3b geïnstalleerd als lokale LLM, Anthropic API ingesteld als primair voor entity extraction en summarisatie. ANTHROPIC_API_KEY opgeslagen in /opt/mypka-memory/.env. Daily Planning skill en CLAUDE.md aangescherpt: Highlight-regel nu als verplicht checkpoint geborgd.

## Decisions

- Anthropic API primair boven Ollama voor entity extraction (snelheid)
- OLLAMA_KEEP_ALIVE=30m ingesteld in docker-compose
- Conversational memory thread 'daily-routines' als feed voor alle routines
- Highlight-regel aangescherpt in skill én CLAUDE.md

## Actions taken

- knowledge_indexer.py gebouwd en uitgevoerd (758 chunks)
- entity_backfill.py gebouwd en uitgevoerd (75 entities uit 36 journals)
- memory_manager.py: upsert voor entities, idempotency voor knowledge chunks, Anthropic als primair
- memory_config.py: load_anthropic_key() toegevoegd
- Alle close-routines bijgewerkt met conversational memory write_message
- start-morning-routine bijgewerkt met daily-routines feed
- SOP-001 bijgewerkt met entity backfill restore stap
- CLAUDE.md uitgebreid met Fase 2 regels
- Penn AGENT.md: entity memory stap toegevoegd
- start-daily-planning.md: verplicht checkpoint Stap 6 toegevoegd
- Daily Planning morgen klaargezet: Highlight les 93 MR

## Delegations

Geen

## Open items

- Twee Wendy speedys doorgeschoven naar 2026-05-21
- Borg Tricolarae template naamgevingen doorgeschoven naar 2026-05-21
