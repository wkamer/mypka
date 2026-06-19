# GL-015 — Memory Domain Routing Protocol

**Status:** Active
**Owner:** Walter Kamer
**Maintainer:** Larry, Team Orchestrator
**Date:** 2026-06-04
**Related:** [[GL-013_Memory Core Architecture]], [[GL-014_AI Team Governance]]

---

## Purpose

This document is the single authoritative routing protocol for all agent writes across
the myPKA memory stores. It defines which agent writes to which SQLite database, how
the Unified Memory Core (UMC) domain tags are assigned, and how cross-domain learnings
are handled. Active agents should reference this document from their AGENT.md instead
of duplicating routing rules.

---

## 1. Store Architecture and SSOT Principle

### 1.1 SQLite Databases — Operational SSOT

The four SQLite databases are the sole sources of truth for all operational data. No
record is authoritative in any other store.

| Database | Path | Domain |
|---|---|---|
| `personal.db` | `PKM/personal.db` | Personal life |
| `team-knowledge.db` | `Team Knowledge/team-knowledge.db` | Team governance and infrastructure |
| `kamer-ecommerce.db` | `Team Knowledge/Kamer E-commerce/kamer e-commerce.db` | Kamer E-commerce |
| `geldstroom-regie.db` | `Team Knowledge/Geldstroom Regie/geldstroom-regie.db` | Geldstroom Regie |

Paths are canonical per [[GL-004_Canonical paths]]. If a path listed here conflicts with
GL-004, GL-004 wins; update this document to match.

### 1.2 PostgreSQL UMC — Semantic Read-Index Only

The Unified Memory Core (PostgreSQL + pgvector, `memory-db` container) is a semantic
read-index and vector store. It is never the write target for operational data. An agent
that writes to UMC does so in addition to its canonical SQLite database, not instead of
it. Per [[GL-013_Memory Core Architecture]]: SQLite is the authoritative operational
data store.

---

## 2. Agent-to-Database Routing Table

Every agent writes session_logs, agent_learnings, team_log, team_tasks, and
delegation_outcomes to exactly one SQLite database. The database is determined by the
agent's domain, not by the topic of the session.

When a display name in the Canonical SQLite Database column and the Path in Section 1.1
differ, the Path in Section 1.1 is authoritative.

| Agent | Domain | Canonical SQLite Database |
|---|---|---|
| Larry | Core / Orchestration | `team-knowledge.db` |
| Pax | Core / Research | `team-knowledge.db` |
| Nolan | Core / Documentation | `team-knowledge.db` |
| Kai | Core / Infrastructure | `team-knowledge.db` |
| Penn | Personal | `personal.db` |
| Sienna | Personal | `personal.db` |
| Marcus | Personal / Project Management | `personal.db` |
| Lena | Personal / Health | `personal.db` |
| Sasha | Kamer E-commerce | `kamer-ecommerce.db` |
| Vera | Kamer E-commerce | `kamer-ecommerce.db` |
| Remy | Kamer E-commerce | `kamer-ecommerce.db` |
| Nova | Kamer E-commerce | `kamer-ecommerce.db` |
| Bo | Kamer E-commerce | `kamer-ecommerce.db` |
| Zara | Kamer E-commerce | `kamer-ecommerce.db` |
| Finn | Geldstroom Regie | `geldstroom-regie.db` |

**Rule:** When a new specialist is hired, Larry assigns a canonical database in this table
before the specialist is activated. A specialist without a routing assignment in this
table is not yet authorized to write operational records.

**Rule:** An agent never writes to a database outside its canonical assignment, even when
the session topic is relevant to another domain.

---

## 3. UMC Domain Tags and source_type

When an agent writes to the UMC (memory_summaries, memory_knowledge), the `domain` and
`source_type` fields must match the agent's canonical domain. An agent never tags a UMC
write with a domain other than its own.

| Agent | domain= | source_type= |
|---|---|---|
| Larry, Pax, Nolan, Kai | `core` | `knowledge` |
| Penn (journal entries) | `personal` | `journal` |
| Penn (entity extraction) | — | via extract_and_store_entities |
| Sienna | `personal` | `knowledge` |
| Marcus | `personal` | `project` |
| Lena | `personal` | `knowledge` |
| Sasha | `kamer-ecommerce` | `knowledge` |
| Vera | `kamer-ecommerce` | `knowledge` |
| Remy | `kamer-ecommerce` | `knowledge` |
| Nova | `kamer-ecommerce` | `knowledge` |
| Bo | `kamer-ecommerce` | `knowledge` |
| Zara | `kamer-ecommerce` | `knowledge` |
| Finn | `geldstroom-regie` | `knowledge` |
| WhatsApp (automated) | `personal` | `whatsapp` |

session_log writes to UMC use source_type `session_log`. agent_learning writes use
source_type `agent_learning`. Other source_type values are defined in
[[GL-013_Memory Core Architecture]].

---

## 4. Cross-Domain Learnings

### 4.1 Definition

A cross-domain learning is an insight, decision, or pattern that originates in one
domain's session but has material relevance to one or more other domains.

Example: Sasha discovers a pricing pattern in Kamer E-commerce that also affects
Walter's personal financial planning tracked under personal.db.

### 4.2 Rule — No Automatic Multi-Database Writes

An agent never autonomously writes a learning to more than one database. Cross-domain
learnings are not auto-propagated.

### 4.3 Rule — Larry Surfaces, Owner Decides

When an agent identifies a learning with cross-domain relevance:
1. The agent writes the learning to its own canonical database (mandatory).
2. The agent flags the cross-domain relevance to Larry in the same session.
3. Larry surfaces the insight to the Owner in the same or next session.
4. The Owner decides: which domain receives the learning as a second write, if any.
5. If the Owner approves a second write: the receiving domain's canonical agent executes
   the write — not the originating agent.
6. The non-canonical domain may receive a reference note or summary only, never a
   duplicate of the full learning record, unless the Owner explicitly approves a full
   second write.

### 4.4 Rule — Session Close Escalation for Unresolved Cross-Domain Candidates

If an agent identifies a cross-domain learning candidate and cannot surface it to Larry
in the current session, the agent records it in the session close summary or escalation
note. No new task, team_tasks row, remediation item, or second database write is created
without an established routine or explicit Owner approval. Larry surfaces the candidate
to Owner Walter Kamer at the next available session.

---

## 5. Historical Data

### 5.1 Non-Remediation Principle

This GL governs new writes only. Historical records that predate this document — including
misrouted agent_learnings, session logs written to the wrong database, NULL agent_slug
values, and entries from deprecated or renamed agent slugs — are not remediated as part
of this GL's implementation.

### 5.2 Reason

Retroactive remediation of historical records is a separate project requiring a dedicated
proposal, Owner approval, a tested migration script, a rollback plan, and a post-check
protocol. Bundling remediation with routing governance would couple two independent
concerns and increase implementation risk.

### 5.3 Future Remediation Candidates

The following items are registered as candidates for a separate future remediation
proposal. They are not in scope here.

| Item | Database | Detail |
|---|---|---|
| Misrouted agent_learnings | team-knowledge.db | Learnings from non-core specialists (vera, sasha, nova, zara, marcus, sienna, penn, finn, iris) — confirmed in triage 2026-06-04 |
| Penn session logs in wrong DB | team-knowledge.db | 39 session_logs attributed to agent_slug=penn — personal agent in core DB |
| NULL agent_slug in session_logs | personal.db | 55 rows with no agent attribution — makes domain queries unreliable |
| Deprecated agent slug | personal.db / team-knowledge.db | agent_slug=iris present in both DBs — not a current active specialist |
| Geldstroom Regie learning-dead | geldstroom-regie.db | 0 agent_learnings despite 11 sessions — Finn is not writing back; requires investigation |

These items are visible in the triage report at:
`Deliverables/20260604_Core_Architecture Triage Memory Domain Routing/triage-report.md`

---

## 6. Enforcement

### 6.1 AGENT.md Pointer (see Proposal Section 4)

Each active specialist's AGENT.md may contain a routing pointer section that names this
document and states the agent's canonical database. The pointer is added as part of this
GL's optional implementation scope, subject to separate approval.

### 6.2 Larry's Weekly Sweep

At End-of-Day Routine every Friday, Larry checks for agent_learnings entries in
`team-knowledge.db` with agent_slug values that do not belong to core agents (Larry,
Pax, Nolan, Kai). Any such entries are surfaced to the Owner as routing violations
during the weekly sweep.

### 6.3 New Agent Onboarding

Before a new specialist is activated, Larry assigns the canonical database and adds the
agent to the routing table in this document (Section 2) as part of the standard hiring
flow per [[SOP-003_How to hire a new team member]].

---

## Changelog

- 2026-06-04 (Larry, GL-015): Initial version created. Approved by Owner Walter Kamer.
