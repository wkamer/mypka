# P-Unified Memory Core

**Type:** Event-driven
**Event:** Memory Core live — 2026-05-20
**Status:** Active
**Started:** 2026-05-20
**Todoist:** 6ggjwhmF62h4MF5V

---

## Doel

Een Unified Memory Core bouwen voor het myPKA agent-systeem op basis van PostgreSQL + pgvector (Docker, ARM64). Vervangt de huidige statische memory-files door semantisch doorzoekbaar, persistent geheugen gedeeld door alle agents.

## Stack

- PostgreSQL 16 + pgvector (Docker: `pgvector/pgvector:pg16`)
- Sentence-transformers (lokale embeddings op Pi 5)
- Python retrieval laag
- Bestaande SQLite databases blijven parallel actief tijdens migratie

## Memory types (target)

1. Conversational Memory — sessie-logs per thread
2. Knowledge Base — doorzoekbare documenten + guidelines
3. Entity Memory — personen, systemen, relaties
4. Summary Memory — gecomprimeerde context voor lange sessies
5. Tool Log — offloaded tool-output, preview in context
6. Workflow Memory — geleerde actiepatronen (fase 2)
7. Toolbox Memory — semantische tool-discovery (fase 2)

## Hardware

Raspberry Pi 5 — 8GB RAM, 256GB NVMe, Docker actief

---

## Log

### 2026-05-20
- Project aangemaakt
- Architectuurschets uitstaat bij Pax
