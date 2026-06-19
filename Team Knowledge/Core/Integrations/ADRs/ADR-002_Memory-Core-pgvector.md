# ADR-002: Memory Core — pgvector als vector store

**Status:** Accepted
**Datum:** 2026-05-20
**Eigenaar:** Kai

---

## Context

Het myPKA agentsysteem heeft een persistent geheugen nodig voor:
1. Tool output offloading (Fase 1a)
2. Semantisch doorzoekbare summaries (Fase 1b)

Vereisten: ARM64, draait op Raspberry Pi 5 8GB, minimale extra services, lage memory footprint.

## Beslissing

PostgreSQL 16 met pgvector-extensie als vector store, in een aparte `memory-db` container. Embeddings lokaal via `all-MiniLM-L6-v2` (sentence-transformers). Geen externe embedding-API.

## Consequenties

Zie GL-010 voor volledig detail. Korte samenvatting:
- Eenvoudige stack: SQL + vector in één service
- ARM64-compatibel (pgvector/pgvector:pg16 publiceert linux/arm64)
- n8n-postgres blijft volledig onafhankelijk
- Embedding model (~90 MB) wordt lokaal geladen op eerste gebruik
