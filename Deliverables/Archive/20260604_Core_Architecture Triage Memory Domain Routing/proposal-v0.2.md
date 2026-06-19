# Memory Domain Routing Protocol — GL-015 Proposal v0.2

**Status:** Proposal only — no implementation
**Version:** v0.2
**Date:** 2026-06-04
**Author:** larry
**Origin:** Architecture Triage Memory Domain Routing (2026-06-04), Option A approved by Owner Walter Kamer
**Previous version:** proposal-v0.1.md (reviewed 2026-06-04, amendments requested by Owner Walter Kamer)
**Requires approval by:** Owner Walter Kamer — see Approval Gate

---

## Revision Notes — v0.1 to v0.2

Six amendments applied per Owner Walter Kamer's review of v0.1 (2026-06-04):

| # | Amendment | Section(s) changed |
|---|---|---|
| R1 | Ownership model corrected: Owner = Walter Kamer, Maintainer = Larry | §2.2 GL header |
| R2 | Exact gl-index.md entry text, insertion location, and post-check added | §3 Implementation Scope |
| R3 | AGENT.md pointer section made execution-ready: exact file paths, exact final text per agent, exact insertion location, post-checks | §4.1 |
| R4 | CLAUDE.md option 4.2-A made execution-ready: exact current block, exact replacement text, exact method, post-check | §4.2 |
| R5 | GL §4.4 automatic team_tasks creation removed; replaced with governance-safe session-close escalation rule | §2.2 GL §4.4 |
| R6 | Dutch phrase "SQLite blijft SSOT." replaced with English equivalent | §2.2 GL §1.2 |

---

## 1. Purpose

The myPKA AI team operates four SQLite databases as operational sources of truth, separated by domain: personal, team governance, Kamer E-commerce, and Geldstroom Regie. A fifth store, the Unified Memory Core (PostgreSQL + pgvector), serves as a semantic read-index.

The routing rule for which agent writes to which database exists in CLAUDE.md (Larry's operational instructions) but not in individual AGENT.md files. Because agents read their own AGENT.md during execution, the routing rule is outside their active scope. As a result, autonomous team learning accumulates in `team-knowledge.db` regardless of which domain the learning belongs to.

This GL establishes a single, enforceable, authoritative routing protocol that all agents can reference from their own AGENT.md. It does not change the architecture. It governs how the existing architecture is used.

---

## 2. Proposed GL Document

### 2.1 GL Number and Filename

**GL number:** GL-015
**Filename:** `GL-015_Memory Domain Routing Protocol.md`
**Canonical path:** `Team Knowledge/Core/Guidelines/GL-015_Memory Domain Routing Protocol.md`

Per GL-001 naming convention: Title Case, spaces as separators, `GL-NNN_` prefix, `.md` extension.

### 2.2 Exact Full GL Content

The text below is the exact content to be written to the GL file if this proposal is approved. No paraphrase or adaptation during execution — apply verbatim.

---

```
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
are handled. Every agent's AGENT.md references this document rather than duplicating
routing rules.

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

Each active specialist's AGENT.md contains a routing pointer section that names this
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

- 2026-06-04 (Larry, GL-015 v0.1 proposal): Initial version. Pending Owner approval.
```

---

## 3. Implementation Scope

This proposal, if approved for core GL implementation, authorizes exactly the following two actions:

| # | Action | Target |
|---|---|---|
| 1 | Create GL-015 file with exact content from Section 2.2 | `Team Knowledge/Core/Guidelines/GL-015_Memory Domain Routing Protocol.md` |
| 2 | Add GL-015 entry to gl-index.md | `Team Knowledge/Core/Guidelines/gl-index.md` |

No other files are modified as part of core GL implementation.

### 3.1 Exact gl-index.md Update

**Target file:** `Team Knowledge/Core/Guidelines/gl-index.md`

**Current last row (to use as insertion anchor):**

```
| GL-014 | [[GL-014_AI Team Governance]] | Authoritative governance voor het myPKA AI-team: approval-gates, escalation, changelog-protocol, secret handling, SSOT-hiërarchie |
```

**Exact new row to append immediately after the GL-014 row:**

```
| GL-015 | [[GL-015_Memory Domain Routing Protocol]] | Gezaghebbend routeringsprotocol voor alle agent-schrijfoperaties — canonical database per agent, UMC-domein tags en cross-domain learning governance |
```

**Insertion method:** Edit `Team Knowledge/Core/Guidelines/gl-index.md` — append the row above on the line immediately following the GL-014 row. No other lines modified.

**Post-check:** Read `Team Knowledge/Core/Guidelines/gl-index.md`. Confirm:
- Row `| GL-015 |` is present
- Filename `[[GL-015_Memory Domain Routing Protocol]]` is correct
- Row appears after GL-014 and is the last row in the table

### Optional Items (separate approval items — see Section 4)

| # | Action | Target | Decision item |
|---|---|---|---|
| A | Add routing pointer section to each active specialist's AGENT.md | 15 AGENT.md files (see §4.1) | Decision item 4.1 |
| B | Replace CLAUDE.md inline routing block with GL-015 reference | `CLAUDE.md` | Decision item 4.2-A |

---

## 4. Optional Items — Separate Decision Points

### 4.1 AGENT.md Routing Pointer — Execution-Ready Specification

**Decision:** Owner may approve all 15 AGENT.md updates, a named subset, or none. A partial approval must list which agents are included.

**Proposed section text:** The following `## Memory Domain Routing` block is appended as the last section of each named AGENT.md file. The text is identical across agents except for the two substitution fields marked `[DATABASE_PATH]` and `[DOMAIN_VALUE]`.

**Insertion location for all files:** Append after the last existing top-level `##` section in the file. No existing content is removed or modified.

**Exact final text per agent (substitutions resolved, verbatim):**

---

**Bo, Remy, Nova, Sasha, Vera, Zara** — Kamer E-commerce domain:

```markdown
## Memory Domain Routing

This agent writes all operational records (session_logs, agent_learnings, team_log,
team_tasks, delegation_outcomes) exclusively to:
`Team Knowledge/Kamer E-commerce/kamer e-commerce.db`

Routing authority: [[GL-015_Memory Domain Routing Protocol]]

This agent never writes operational records to any other domain database, even when
the session topic is relevant to another domain. Cross-domain learnings are flagged
to Larry for Owner decision.

UMC domain tag: `kamer-ecommerce` — source_type per GL-015 Section 3.
```

Applies to:
- `Team/Bo - The Market Validator/AGENT.md`
- `Team/Nova - The E-commerce Operations Specialist/AGENT.md`
- `Team/Remy - The Product Intelligence Specialist/AGENT.md`
- `Team/Sasha - The Shopify Specialist/AGENT.md`
- `Team/Vera - The Portfolio Business Manager/AGENT.md`
- `Team/Zara - The Ads Intelligence Specialist/AGENT.md`

---

**Finn** — Geldstroom Regie domain:

```markdown
## Memory Domain Routing

This agent writes all operational records (session_logs, agent_learnings, team_log,
team_tasks, delegation_outcomes) exclusively to:
`Team Knowledge/Geldstroom Regie/geldstroom-regie.db`

Routing authority: [[GL-015_Memory Domain Routing Protocol]]

This agent never writes operational records to any other domain database, even when
the session topic is relevant to another domain. Cross-domain learnings are flagged
to Larry for Owner decision.

UMC domain tag: `geldstroom-regie` — source_type per GL-015 Section 3.
```

Applies to:
- `Team/Finn - The WordPress Specialist/AGENT.md`

---

**Larry, Kai, Nolan, Pax** — Core domain:

```markdown
## Memory Domain Routing

This agent writes all operational records (session_logs, agent_learnings, team_log,
team_tasks, delegation_outcomes) exclusively to:
`Team Knowledge/team-knowledge.db`

Routing authority: [[GL-015_Memory Domain Routing Protocol]]

This agent never writes operational records to any other domain database, even when
the session topic is relevant to another domain. Cross-domain learnings are flagged
to Larry for Owner decision.

UMC domain tag: `core` — source_type per GL-015 Section 3.
```

Applies to:
- `Team/Kai - The Infrastructure & Integration Architect/AGENT.md`
- `Team/Larry - The Orchestrator/AGENT.md`
- `Team/Nolan - The HR Specialist/AGENT.md`
- `Team/Pax - The Research Specialist/AGENT.md`

---

**Lena, Marcus, Penn, Sienna** — Personal domain:

```markdown
## Memory Domain Routing

This agent writes all operational records (session_logs, agent_learnings, team_log,
team_tasks, delegation_outcomes) exclusively to:
`PKM/personal.db`

Routing authority: [[GL-015_Memory Domain Routing Protocol]]

This agent never writes operational records to any other domain database, even when
the session topic is relevant to another domain. Cross-domain learnings are flagged
to Larry for Owner decision.

UMC domain tag: `personal` — source_type per GL-015 Section 3.
```

Applies to:
- `Team/Lena - The Health Coach/AGENT.md`
- `Team/Marcus - The Project Manager/AGENT.md`
- `Team/Penn - The Journal Writer/AGENT.md`
- `Team/Sienna - The Personal Assistant/AGENT.md`

---

**Post-check for each AGENT.md updated:**
Read the file. Confirm:
1. Section `## Memory Domain Routing` is present as the last section
2. Database path matches the agent's canonical database from the table above
3. UMC domain tag matches the agent's canonical domain
4. No other sections modified

**Complete list of AGENT.md files in scope (15 total):**

| Agent | File path (relative to /opt/myPKA) | Domain | DB |
|---|---|---|---|
| Bo | `Team/Bo - The Market Validator/AGENT.md` | Kamer E-commerce | `kamer-ecommerce.db` |
| Finn | `Team/Finn - The WordPress Specialist/AGENT.md` | Geldstroom Regie | `geldstroom-regie.db` |
| Kai | `Team/Kai - The Infrastructure & Integration Architect/AGENT.md` | Core | `team-knowledge.db` |
| Larry | `Team/Larry - The Orchestrator/AGENT.md` | Core | `team-knowledge.db` |
| Lena | `Team/Lena - The Health Coach/AGENT.md` | Personal | `personal.db` |
| Marcus | `Team/Marcus - The Project Manager/AGENT.md` | Personal | `personal.db` |
| Nolan | `Team/Nolan - The HR Specialist/AGENT.md` | Core | `team-knowledge.db` |
| Nova | `Team/Nova - The E-commerce Operations Specialist/AGENT.md` | Kamer E-commerce | `kamer-ecommerce.db` |
| Pax | `Team/Pax - The Research Specialist/AGENT.md` | Core | `team-knowledge.db` |
| Penn | `Team/Penn - The Journal Writer/AGENT.md` | Personal | `personal.db` |
| Remy | `Team/Remy - The Product Intelligence Specialist/AGENT.md` | Kamer E-commerce | `kamer-ecommerce.db` |
| Sasha | `Team/Sasha - The Shopify Specialist/AGENT.md` | Kamer E-commerce | `kamer-ecommerce.db` |
| Sienna | `Team/Sienna - The Personal Assistant/AGENT.md` | Personal | `personal.db` |
| Vera | `Team/Vera - The Portfolio Business Manager/AGENT.md` | Kamer E-commerce | `kamer-ecommerce.db` |
| Zara | `Team/Zara - The Ads Intelligence Specialist/AGENT.md` | Kamer E-commerce | `kamer-ecommerce.db` |

### 4.2 CLAUDE.md Inline Routing Block — Execution-Ready Specification

**Assessment:** The CLAUDE.md `### team_tasks` subsection contains two routing paragraphs that duplicate GL-015 Section 2. Option 4.2-A (replace with a single reference line) is recommended for SSOT compliance. Option 4.2-C (no change) is acceptable if the Owner prefers minimal CLAUDE.md changes in this round.

**Option 4.2-A — Replace inline routing block with GL-015 reference (Recommended)**

**Target file:** `/opt/myPKA/CLAUDE.md`

**Exact current block to replace** (two paragraphs appearing immediately after the team_tasks domain table):

```
Routing — team_tasks: Sienna/Penn → `PKM/personal.db`. Sasha/Vera → `Team Knowledge/Kamer E-commerce/kamer e-commerce.db`. Finn → `Team Knowledge/Geldstroom Regie/geldstroom-regie.db`. Pax/Nolan/Larry → `Team Knowledge/team-knowledge.db`.

Routing — agent_learnings and team_log: same domain rule applies. Personal agents (Penn, Sienna) write to `personal.db`. Business agents (Sasha, Vera) write to `kamer e-commerce.db`. Geldstroom agents (Finn) write to `geldstroom-regie.db`. Core agents (Larry, Nolan, Pax) write to `team-knowledge.db`. Never write all learnings to `team-knowledge.db` by default.
```

**Exact replacement text:**

```
Routing authority: [[GL-015_Memory Domain Routing Protocol]] — defines canonical database per agent, UMC domain tags, and cross-domain learning rules.
```

**Execution method:** Read `/opt/myPKA/CLAUDE.md` immediately before editing to confirm byte-exact match of the current block above. Then apply Edit: replace the two-paragraph block with the single reference line.

**Post-check:** Read `/opt/myPKA/CLAUDE.md`. Confirm:
1. Neither `Routing — team_tasks:` paragraph is present
2. Neither `Routing — agent_learnings and team_log:` paragraph is present
3. The reference line `Routing authority: [[GL-015_Memory Domain Routing Protocol]]` is present in the `### team_tasks` subsection, immediately after the domain table

**Option 4.2-B — Keep inline block, add reference line**
Add `See also: [[GL-015_Memory Domain Routing Protocol]]` after the existing second routing paragraph. Redundancy persists; acceptable as interim if Owner wants minimal disruption.

**Option 4.2-C — No change to CLAUDE.md**
Routing exists in two places. Tolerable if AGENT.md pointers (4.1) are approved, because agents will read GL-015 from their own AGENT.md.

**This is a separate decision item.** The Owner may approve 4.2-A, 4.2-B, 4.2-C, or defer independently of GL-015 and AGENT.md pointer decisions.

---

## 5. Explicit Exclusions

The following are explicitly outside scope for this proposal:

- Database schema changes
- Data migration of any kind
- Cleanup of misrouted historical records
- Repair of NULL agent_slug values in session_logs
- Remediation of deprecated agent slugs (iris, journal-agent)
- Investigation of Geldstroom Regie learning-dead state
- Script changes (memory_manager.py, db_helper.py, or any other script)
- Changes to PostgreSQL schema or init.sql
- Changes to n8n workflows
- Backlog item creation or closure
- team_log writes
- team_tasks writes
- UMC writes
- Any database write not explicitly authorized by Owner Walter Kamer

---

## 6. Post-Check Plan

After implementation (if approved), the following checks confirm correctness:

| Check | Method | Pass condition |
|---|---|---|
| GL-015 file exists at canonical path | `ls` | File present at `Team Knowledge/Core/Guidelines/GL-015_Memory Domain Routing Protocol.md` |
| GL-015 content matches proposal verbatim | Read file | Exact match to Section 2.2 of this proposal |
| gl-index.md contains GL-015 entry | Read file | Row present with `[[GL-015_Memory Domain Routing Protocol]]` after GL-014 row |
| No other files modified (core GL only) | File comparison | No changes outside GL-015 and gl-index.md |
| If AGENT.md pointers approved: each file contains routing section | Read each file | `## Memory Domain Routing` present with correct database path and domain tag |
| If CLAUDE.md 4.2-A approved: routing paragraphs replaced | Read CLAUDE.md | Reference line present; two routing paragraphs absent |

---

## 7. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| GL created but AGENT.md pointers not added; agents still cannot see routing rule | High (if 4.1 not approved) | Medium | Acceptable if Owner accepts CLAUDE.md as interim authority; weekly sweep in GL-015 §6.2 provides detection |
| CLAUDE.md routing table and GL-015 diverge over time | Medium (if 4.2-C chosen) | Medium | Larry's Librarian duty at session close flags SSOT violations |
| New specialist added without routing assignment | Low | Medium | GL-015 §6.3 makes routing assignment mandatory before activation |
| Geldstroom Regie remains learning-dead after GL creation | High | Medium | GL-015 documents the gap; remediation is a separate proposal |
| GL-015 content is correct but never enforced because agents do not read it | Medium | High | AGENT.md pointers (optional item 4.1) solve this; without them, enforcement depends on Larry's weekly sweep only |

---

## 8. Owner Decision Options

**Option A — Approve GL implementation only**
Create GL-015 and update gl-index.md per §3 of this proposal. No AGENT.md changes. No CLAUDE.md changes. Routing rule becomes authoritative but is not yet in agents' active read scope.

**Option B — Approve GL implementation plus selected optional pointer updates**
Create GL-015 and update gl-index.md. Additionally, approve one or more of:
- B1: AGENT.md pointers for all 15 agents (per §4.1 exact text)
- B2: AGENT.md pointers for a named subset of agents (Owner specifies which)
- B3-A: CLAUDE.md replacement per §4.2 Option 4.2-A
- B3-B: CLAUDE.md reference addition per §4.2 Option 4.2-B
Options B1/B2 and B3 may be combined independently.

**Option C — Request amendments**
Owner identifies gaps, incorrect routing assignments, or missing elements. Larry revises as v0.3 per SOP-015.

**Option D — Defer**
Accept the proposal but take no action now. Continue with other priorities. The routing violations in team-knowledge.db will continue to accumulate.

**Option E — Reject as unnecessary**
The current CLAUDE.md routing table is sufficient. No GL is created.

---

## 9. Recommended Option

**Option B: GL implementation + B1 (all AGENT.md pointers) + B3-A (CLAUDE.md replacement).**

Reasoning: GL-015 alone (Option A) establishes the rule but does not put it in agents' active scope. AGENT.md pointers (B1) are the enforcement layer — without them, the GL exists but agents running without Larry in scope will not see it. The CLAUDE.md replacement (B3-A) removes the duplicate inline routing paragraphs and makes GL-015 the single source of truth, consistent with the SSOT Golden Rule. Together these three actions close the governance gap identified in the triage without touching databases, scripts, or historical data.

If the Owner wants to minimize changes in this round: Option A is the safe minimum. AGENT.md pointers can follow as a second proposal.

---

## Approval Gate

No implementation may happen until Owner Walter Kamer explicitly approves this proposal by version.

Approval phrase: "approve GL-015 proposal v0.2"

- Approval of v0.1 does not carry over to v0.2
- Approval of the triage Option A does not constitute implementation approval
- A partial approval (e.g., "approve Option A only") is valid and scoped to the stated option
- Implementation of optional items requires explicit statement of which items (B1, B2, B3-A, B3-B) are approved

Governance:
- Owner: Walter Kamer
- Maintainer responsible for execution: Larry, Team Orchestrator
- First review, then implementation only after explicit Owner approval
- No implementation, correction, rollback, data cleanup, database write, backlog update, logging, migration, or further audit work may be executed without Owner Walter Kamer's explicit approval

---

*Delivered on: 2026-06-04*
*Delivered at: Deliverables/20260604_Core_Architecture Triage Memory Domain Routing/proposal-v0.2.md*
