# Architecture Triage: Memory Domain Routing
**Type:** Read-only architecture triage
**Status:** Awaiting Owner decision
**Date:** 2026-06-04
**Prepared by:** Larry — Team Orchestrator
**Scope:** Multi-database memory setup and autonomous team learning routing

---

## 1. Executive Summary

The multi-database setup is **conceptually sound** and the original design decision was correct. Domain separation protects privacy, enables failure isolation, and reflects real ownership boundaries. However, **the routing protocol exists only in CLAUDE.md** and is not enforced at the agent level. As a result, `team-knowledge.db` is acting as a de facto catch-all: it contains agent learnings from all seven domains. The routing rule is being violated in practice by nearly every non-core specialist.

This is not a design flaw. It is a governance gap: the rule exists but has no enforcement layer.

---

## 2. Memory Stores Inventory

### 2.1 SQLite Operational Databases (SSOT)

| Database | Path | Tables | Purpose |
|---|---|---|---|
| `personal.db` | `PKM/personal.db` | 14 | Personal domain: journal, people, habits, session logs, tasks |
| `team-knowledge.db` | `Team Knowledge/team-knowledge.db` | 6 | Core/infrastructure: team governance, SOPs, Larry/Pax/Nolan/Kai |
| `kamer-ecommerce.db` | `Team Knowledge/Kamer E-commerce/kamer e-commerce.db` | 6 | Kamer E-commerce domain |
| `geldstroom-regie.db` | `Team Knowledge/Geldstroom Regie/geldstroom-regie.db` | 6 | Geldstroom Regie domain |

All four share the same governance schema: `session_logs`, `agent_learnings`, `team_log`, `team_tasks`, `delegation_outcomes`. `personal.db` additionally holds domain-specific tables (journal, people, habits, daily_growth, notes, documents, contact_interactions).

### 2.2 PostgreSQL Unified Memory Core (semantic read-index)

| Store | Tables | Purpose |
|---|---|---|
| `memory-db` (PostgreSQL + pgvector) | `tool_logs`, `memory_summaries`, `conversational_memory`, `memory_entities`, `memory_knowledge` | Semantic read-index and vector store; explicitly NOT the SSOT |

GL-013 explicitly states: "SQLite blijft SSOT. PostgreSQL is uitsluitend een lees-index en vector store — geen schrijfdoel voor operationele data." The two layers are intentionally separate and serve different functions.

---

## 3. Routing Documentation Status

### 3.1 What is documented

**CLAUDE.md (Larry's operational rules) — routing table exists:**

| Agent | Database |
|---|---|
| Penn, Sienna | `personal.db` |
| Sasha, Vera | `kamer e-commerce.db` |
| Finn | `geldstroom-regie.db` |
| Larry, Nolan, Pax | `team-knowledge.db` |

**CLAUDE.md — UMC domain routing table exists:**

| Agent / Domain | domain= | source_type= |
|---|---|---|
| Larry, Nolan, Pax, Kai | `core` | `knowledge` |
| Penn (journal) | `personal` | `journal` |
| Sienna | `personal` | `knowledge` |
| Marcus | `personal` | `project` |
| Sasha, Vera | `kamer-ecommerce` | `knowledge` |
| Finn | `geldstroom-regie` | `knowledge` |

**GL-013** covers PostgreSQL stack architecture and SQLite SSOT principle. Does not specify which agents route where.

**SOP-007** covers operational procedures for Memory Core. Domain routing not addressed.

**GL-014** covers AI team governance at a high level. Domain routing not addressed.

### 3.2 What is NOT documented

- No standalone GL or SOP defines the complete domain routing protocol in one place
- Individual AGENT.md files do not contain routing rules (agents read their own AGENT.md, not CLAUDE.md)
- No cross-domain learning mechanism is defined anywhere
- No remediation procedure exists for detected misrouting

---

## 4. Actual Data Findings

### 4.1 Row counts across all databases

| Database | session_logs | agent_learnings | team_log | team_tasks |
|---|---|---|---|---|
| `personal.db` | 55 | 7 | 1 | 28 |
| `team-knowledge.db` | 145 | 39 | 75 | 64 |
| `kamer-ecommerce.db` | 9 | 9 | 4 | 40 |
| `geldstroom-regie.db` | 11 | 0 | 0 | 27 |

### 4.2 Agent slug distribution in agent_learnings

**team-knowledge.db** (expected: larry, nolan, pax only):
`pax(6), nolan(5), vera(4), marcus(4), iris(4), sienna(3), kai(3), sasha(2), nova(2), larry(2), zara(1), penny(1), penn(1), finn(1)`

Cross-domain contamination confirmed: vera, sasha, nova, zara belong in `kamer-ecommerce.db`; finn belongs in `geldstroom-regie.db`; sienna, penn belong in `personal.db`; marcus belongs in `personal.db`.

**personal.db** agent_learnings (expected: penn, sienna only):
`sienna(4), iris(2), penn(1)` — correct agents, but iris is unrecognised (likely a deprecated or renamed specialist)

**geldstroom-regie.db** agent_learnings:
`0 rows` — Finn has never written a learning back. Domain is learning-dead.

### 4.3 Session log attribution

All 55 `personal.db` session_logs have `agent_slug = NULL`. No session is attributed to an agent, making it impossible to query "which specialist ran this session."

`team-knowledge.db` session_logs include: `penn(39)` — Penn is a personal domain specialist; 39 of her session logs are in the wrong database.

### 4.4 Summary of detected violations

| Violation | Severity | Detail |
|---|---|---|
| Cross-domain agent_learnings in team-knowledge.db | High | 7 non-core specialists have written learnings here |
| Penn session logs in team-knowledge.db | High | 39 entries; personal agent in core DB |
| geldstroom-regie.db learning-dead | Medium | 0 agent_learnings; Finn not writing back |
| session_logs agent_slug NULL in personal.db | Medium | 55 unattributed sessions |
| iris entries (deprecated agent) in personal.db | Low | Likely historical; not active |

---

## 5. Assessment

**Is the multi-database setup sound?**

**Yes — the design is correct.** Four separate SQLite databases for four real ownership domains is the right architecture for this system. Reasons:

1. **Privacy isolation works.** Personal domain data (journal, habits, health, people) is physically separate from business data.
2. **Failure domain isolation works.** A corrupted kamer-ecommerce.db does not affect personal.db.
3. **Ownership is clear.** Each database maps to a real stakeholder boundary: personal life, team infrastructure, commerce, financial advisory.
4. **The UMC layer adds semantic search without undermining the SSOT.** GL-013's decision to keep PostgreSQL as read-index only was correct.

**What is not sound:**

The routing rule exists in one place (CLAUDE.md) and is not visible to agents when they are running. Individual specialists read their own AGENT.md. The routing rule is not in any specialist's AGENT.md. This means every specialist that writes learnings is making a routing decision without the rule in scope.

**Classification: Sound but needs a routing protocol.**

The architecture is correct. The enforcement layer is missing.

---

## 6. Proposed High-Level Routing Model

```
Learning type               Write to                  UMC domain tag
─────────────────────────────────────────────────────────────────────
Personal domain learning    personal.db               personal
(Penn, Sienna, Marcus)

Team governance learning    team-knowledge.db         core
(Larry, Nolan, Pax, Kai)

Kamer E-commerce learning   kamer-ecommerce.db        kamer-ecommerce
(Sasha, Vera, Remy, Nova,
 Bo, Zara)

Geldstroom Regie learning   geldstroom-regie.db       geldstroom-regie
(Finn)

Cross-domain learning       → Larry surfaces to owner → owner decides
(e.g. pricing insight        which DB receives it;
 relevant to both KE         never auto-written to
 and personal finance)       multiple DBs
```

**Cross-domain principle:** Cross-domain learnings are not written automatically to multiple databases. Larry surfaces the insight to the owner. The owner decides the canonical home. The receiving DB gets the entry. The other domain gets a `[[wikilink]]` reference or a summary note — not a copy.

**UMC write pattern:** The `domain=` tag in `memory_summaries` and `memory_knowledge` follows the same routing table. An agent never writes UMC entries with a domain other than its own.

---

## 7. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| team-knowledge.db becomes permanent catch-all | High (already happening) | Medium | Routing rule in each agent's AGENT.md |
| Geldstroom-regie domain never learns | High (confirmed: 0 rows) | High | Routing rule + explicit Finn write-back in AGENT.md |
| Cross-domain insight lost entirely | Medium | High | Defined cross-domain protocol; Larry surfaces, owner decides |
| Personal data in business DB | Low (not detected yet) | High | Routing rule as hard constraint in AGENT.md |
| Routing rule in CLAUDE.md gets out of sync with AGENT.md | Medium | Medium | Single source in GL; AGENT.md references GL, does not duplicate |

---

## 8. Owner Decision Options

**Option A — Approve preparing a formal proposal for a Memory Domain Routing Protocol (GL)**

Larry prepares a proposal for a new GL document that defines the complete domain routing protocol in one place. All agent AGENT.md files receive a routing directive that references the GL. The proposal follows SOP-015 (versioned proposal, owner review before execution).

*Recommended.*

**Option B — Request amendments to this triage**

Owner identifies gaps, missing angles, or incorrect assumptions in this report. Larry revises before any proposal is prepared.

**Option C — Defer and continue the audit backlog**

Accept the findings, take no action now. The routing violations continue to accumulate. Revisit when the audit backlog clears.

**Option D — Reject as unnecessary**

Accept the current state. The routing violations are tolerable and CLAUDE.md is sufficient as the single routing authority.

---

## 9. Recommendation

**Option A.** The routing violations are active and accumulating. `team-knowledge.db` already contains learnings from 11 different specialists across all four domains. The Geldstroom domain has zero learnings despite 11 sessions. These are not theoretical risks — they are live gaps measured today.

The fix is low-effort: one GL document, one routing directive per AGENT.md. The proposal can be scoped, reviewed, and approved in a single session. The alternative is that cross-domain contamination grows with every session.

A routing protocol is a governance document, not an engineering project. It does not require new infrastructure, migrations, or code changes.

---

*Delivered on: 2026-06-04*
*Delivered at: Deliverables/20260604_Core_Architecture Triage Memory Domain Routing/triage-report.md*
