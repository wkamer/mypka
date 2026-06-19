# GL-010: Memory Core Architecture — Unified Memory Core Fase 1

**Status:** Accepted
**Datum:** 2026-05-20
**Eigenaar:** Kai — Infrastructure & Integration Architect
**Gerelateerd:** ADR-002 (zie `Team Knowledge/Core/Integrations/ADRs/ADR-002_Memory-Core-pgvector.md`)

---

## Context

Het myPKA AI-agentsysteem groeit in complexiteit. Elke sessie lekt tool-output en historische kennis onbeheerd de context window in. Dit veroorzaakt twee problemen:

1. **Token waste** — ruwe tool-output (SQL-resultaten, API-responses) neemt disproportioneel veel context in beslag.
2. **Geen semantisch geheugen** — agents kunnen historische sessies, projectkennis en learnings niet doorzoeken; alles moet elke keer opnieuw in de prompt.

Fase 1 pakt de twee gevallen met de hoogste token-ROI aan: tool output offloading en summary memory met vector search.

---

## Beslissing

### Stack

| Component | Keuze | Reden |
|---|---|---|
| Vector store | PostgreSQL 16 + pgvector | Geen extra service; SQL en vector in één; ARM64-compatible |
| Container | `pgvector/pgvector:pg16` | Officieel image; linux/arm64 manifest aanwezig |
| Embeddings | `all-MiniLM-L6-v2` via sentence-transformers | 384 dimensies; snel op CPU; lokaal, geen externe API-afhankelijkheid |
| LLM | Claude API | Bestaande keuze ecosysteem |

### Separatie

n8n behoudt zijn eigen `n8n-postgres` container. `memory-db` is een volledig aparte PostgreSQL-instantie. Failure domain isolatie: een crash in memory-db raakt n8n niet.

### SQLite blijft SSOT

De bestaande SQLite-databases (`personal.db`, `team-knowledge.db`, `kamer e-commerce.db`, `geldstroom-regie.db`) worden niet aangeraakt. PostgreSQL is uitsluitend een lees-index en vector store — geen schrijfdoel voor operationele data.

### Fasering

Alleen Fase 1 wordt nu geimplementeerd:
- **Fase 1a** — `tool_logs`: ruwe tool-output opslaan, preview in context houden
- **Fase 1b** — `memory_summaries`: gecomprimeerde sessie/project/learning summaries met embeddings

Fase 2 (volledige SQLite-migratie) is een apart toekomstig project.

---

## Alternatieven overwogen

| Alternatief | Reden afgewezen |
|---|---|
| Qdrant als vector store | Extra service, extra geheugen, extra beheer — niet gerechtvaardigd bij deze schaal |
| Weaviate / Chroma | Zelfde argument; PostgreSQL is al in gebruik in het ecosysteem |
| OpenAI text-embedding-ada-002 | Externe API-afhankelijkheid voor elk embedding-verzoek; kosten; privacy |
| Toevoegen aan n8n-postgres | Failure domains vermengen; schema-vervuiling in een service die Kai niet volledig beheert |

---

## Consequenties

**Voordelen:**
- Tool-output verlaat de context window; agents houden alleen de preview
- Semantische zoekopdrachten over historische sessies en learnings mogelijk
- Geen nieuwe infrastructure-categorie: PostgreSQL + Docker al bekend in het ecosysteem
- Embedding lokaal — geen externe API-afhankelijkheid, geen kosten per embedding

**Trade-offs:**
- Extra container op de Pi (512 MB memory limit); bij piekbelasting let op totaal RAM
- `sentence-transformers` eerste load is traag (~2-5 seconden); model wordt cached in geheugen
- pgvector HNSW-index bouwt incrementeel — zoekresultaten verbeteren naarmate meer summaries zijn toegevoegd
- Geen automatische sync van SQLite naar PostgreSQL — handmatige of gescripte import vereist voor bestaande data

---

## Beheer

- Runbook: `[[SOP-007_Memory Core operaties]]`
- Docker Compose: `Team Knowledge/Core/Integrations/memory-db/docker-compose.yml`
- Init SQL: `Team Knowledge/Core/Integrations/memory-db/init.sql`
- Python client: `Team Knowledge/Core/Scripts/memory_client.py`
- Env template: `Team Knowledge/Core/Integrations/memory-db/.env.template`

---

## Operational Model — Specialist UMC Writes

Specialists are invoked within Larry's session. They have no session boundary of their
own and therefore cannot call `write_summary` autonomously when finishing a task.

**How it works:**
- When a specialist completes a substantive task, she writes one handoff note to the
  session context (e.g., "Sasha completed Shopify product sync").
- The close-session routine reads the handoff notes and writes one composite UMC summary
  per domain active in the session, with the correct `source_type` per domain.
  See [[GL-015_Memory Domain Routing Protocol]] §3 for the canonical domain and
  source_type values per specialist.

The `## UMC` section is absent from individual AGENT.md files for this reason.
The close-session routine is the sole write point for `memory_summaries` originating
from specialist work.

---

## Known Gaps and Future Enhancements

### UMC Activity Monitoring

No mechanism currently exists to detect whether the UMC is receiving writes. A domain
can go silent without detection.

Requirement: a weekly automated check that counts UMC entries per domain per week and
sends an alert to Discord or Team Inbox when any domain has received no new entries for
7 or more days. Owner: Kai.
