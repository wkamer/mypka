# LC Naming Alignment Impact Assessment — v05

**Date:** 2026-06-07
**Author:** Larry
**Supersedes:** lc-naming-alignment-impact-assessment-v04.md
**Status:** Read-only assessment — no files modified, no databases updated
**Scope:** Learning Candidate Lifecycle simplification, naming alignment, table verification, architecture assessment
**Goal model:** `Captured → Triaged → Processed → Closed`

---

## 1. Executive Verdict

V04 was returned for one correction: a decision-sequencing inconsistency in Section 12. V04 correctly stated that Q1 and Q2 only unblock Batch 3 and that Batches 1 and 2 do not depend on them — but then listed Q1 and Q2 as Batch 1 pre-conditions alongside Decision A. V05 corrects this throughout.

The sequencing is now unambiguous:
- Decision A (architecture confirmation) is the only pre-condition for Batch 1.
- Q1 and Q2 are pre-conditions for Batch 3 only.
- Batches 1 and 2 do not depend on Q1 or Q2.

A second correction: v04 used inconsistent language around the central learning_candidates architecture — calling it "Owner preferred direction" in some places and "confirmed" in others. V05 uses consistent language throughout: **Owner preferred direction, pending explicit confirmation before Batch 1.**

All other findings, corrections, and decisions from v04 are carried forward unchanged.

---

## 2. Owner-Confirmed Model

### 2.1 Lifecycle states

```
captured → triaged → processed → closed
```

| Value | Definition |
|---|---|
| `captured` | LC registered. Not yet reviewed. Larry owns. |
| `triaged` | LC reviewed. Category confirmed, level confirmed, routing determined. |
| `processed` | Action taken. Outcome recorded in `processed_outcome`. |
| `closed` | LC concluded. No further action. |

Valid transitions: `captured → triaged → processed → closed`.
No silent expiry. No implicit approval. No transition without deliberate action.

### 2.2 Terminology decisions (confirmed)

| Term | Definition |
|---|---|
| LC | Learning Candidate |
| GL | Guideline |
| Graduation Candidate | Classification or routing qualification during Triage or Process — stored in `triage_routing`, not a lifecycle state, not a separate system |
| Team Learning | A possible `processed_outcome` value — not a lifecycle state |
| Landing | Not a formal lifecycle term |
| Process / Processed | Formal wording |

### 2.3 SSOT for learnings

`learning_candidates` = canonical learning lifecycle store and audit trail. Owner preferred direction: centralized in `team-knowledge.db` only, pending explicit confirmation before Batch 1 (see Section 7).
`team_log` = chronological operational log — not a canonical learning store.
`team_learnings` = does not exist.
`agent_learnings` = legacy or absorbable — see Section 8.

---

## 3. Database / Table Findings (Verified — Carried from v03)

### 3.1 Verification note

All schemas were verified using Python's `sqlite3` module. The `sqlite3` CLI silently fails on file paths containing spaces. All v02 "no tables" statements were wrong and have been corrected since v03.

### 3.2 Database inventory

| Database | Path | Size | Tables | Notes |
|---|---|---|---|---|
| team-knowledge.db | `/opt/myPKA/Team Knowledge/team-knowledge.db` | 272K | 7 | Primary domain DB — contains `learning_candidates` |
| personal.db | `/opt/myPKA/PKM/personal.db` | 192K | 14 | Personal domain |
| kamer-ecommerce.db | `/opt/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db` | 60K | 5 | Kamer E-commerce domain |
| geldstroom-regie.db | `/opt/myPKA/Team Knowledge/Geldstroom Regie/geldstroom-regie.db` | 48K | 5 | Geldstroom Regie domain |
| UMC memory | `postgresql://mypka:...` | N/A | tool_logs, memory_summaries | PostgreSQL — separate infrastructure |

### 3.3 Table presence by database

| Table | team-knowledge.db | personal.db | kamer-ecommerce.db | geldstroom-regie.db |
|---|---|---|---|---|
| `session_logs` | 174 rows | 59 rows | 9 rows | 11 rows |
| `team_log` | 90 rows | 1 row | 4 rows | 0 rows |
| `agent_learnings` | 40 rows | 7 rows | 9 rows | 0 rows |
| `delegation_outcomes` | 53 rows | 0 rows | 0 rows | 0 rows |
| `team_tasks` | 77 rows | 28 rows | 40 rows | 27 rows |
| `learning_candidates` | **1 row (old schema)** | absent | absent | absent |
| `deliverable_lifecycle` | 21 rows | absent | absent | absent |
| `team_learnings` | absent | absent | absent | absent |

`memory_summaries` and `tool_logs` exist only in the PostgreSQL UMC database.

### 3.4 Existing `learning_candidates` row — verified data

**Current schema (as implemented, old status values):**
```sql
CREATE TABLE learning_candidates (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    title            TEXT NOT NULL,
    description      TEXT,
    level            INTEGER NOT NULL CHECK(level = 2),
    category         TEXT,
    flagged_by       TEXT NOT NULL,
    flagged_at       TEXT NOT NULL DEFAULT (datetime('now')),
    session_id       INTEGER REFERENCES session_logs(id),
    status           TEXT NOT NULL DEFAULT 'pending'
                         CHECK(status IN ('pending','surfaced','approved','rejected','promoted')),
    surfaced_at      TEXT,
    surfaced_session INTEGER REFERENCES session_logs(id),
    resolved_at      TEXT,
    resolution       TEXT,
    owner            TEXT NOT NULL DEFAULT 'larry',
    max_days_pending INTEGER NOT NULL DEFAULT 3,
    created_at       TEXT NOT NULL DEFAULT (datetime('now'))
)
```

**Row id=4 (the only row):**

| Field | Value |
|---|---|
| id | 4 |
| title | "Governance checkpoints bypassed when Owner drives implementation interactively — CP invocation required even under Owner-directed pace" |
| status | `promoted` |
| flagged_by | `iris` |
| flagged_at | 2026-06-07 |
| category | CAT-3 |
| level | 2 |
| description | "During Deliverable Lifecycle Phase 1 implementation on 2026-06-07, all five governance checkpoints (CP-1 through CP-4 and the Iris pre-implementation check) were not invoked..." |

---

## 4. Corrected Graduation Candidate Mapping

### 4.1 The inconsistency corrected in v04 (carried forward)

The original v03 error was: mapping old status `promoted` to `processed_outcome = 'graduation_candidate'`. This contradicts the Owner-confirmed model. Graduation Candidate is a classification made at Triage, stored in `triage_routing`. `processed_outcome` captures what actually happened after processing.

### 4.2 Correct model

**`triage_routing`** — determined at Triage. What kind of routing does this LC require?

| Value | Meaning |
|---|---|
| `graduation_candidate` | LC warrants structural escalation to SOP, GL, AGENT.md, CLAUDE.md, or equivalent governed document |
| `standard` | Normal processing path |
| `urgent` | Must be processed in the same session as Triage |

**`processed_outcome`** — determined at Processing. What actually happened? See Section 5.

### 4.3 Correct migration mapping for row id=4

Row id=4 was flagged by Iris, classified as requiring structural escalation, and resulted in the Pace Independence Rule being added to SOP-019 Section 3.

| Field | Old value | Correct new value | Rationale |
|---|---|---|---|
| `status` | `promoted` | `closed` | LC is in terminal state — escalation completed |
| `triage_routing` | (did not exist) | `graduation_candidate` | LC was classified at Triage as requiring structural escalation |
| `processed_outcome` | (did not exist) | `sop_update` | Actual outcome: SOP-019 was updated |
| `learning_scope` | (did not exist) | `governance` | Governance-scope observation |
| `source_domain` | (did not exist) | `core` | Originated in core governance domain |
| `resolution` | NULL | "Pace Independence Rule added to SOP-019 Section 3 on 2026-06-07. Flagged by Iris during Deliverable Lifecycle Phase 1 implementation. Escalated and applied via Larry in same session." | Human-readable record |

---

## 5. Corrected `processed_outcome` and `triage_routing` Model

### 5.1 `triage_routing` — classification field

```sql
triage_routing TEXT CHECK(triage_routing IN (
    'graduation_candidate',
    'standard',
    'urgent'
))
```

`graduation_candidate` lives here. It is a routing decision made at Triage, not a processing result. Nullable — when NULL, interpretation is `standard`.

### 5.2 `processed_outcome` — result field

`graduation_candidate` is not in this enum.

```sql
processed_outcome TEXT CHECK(processed_outcome IN (
    'team_learning',
    'agent_learning',
    'guideline_update',
    'sop_update',
    'agent_instruction_update',
    'claude_instruction_update',
    'backlog_item',
    'deliverable_lifecycle_item',
    'rejected',
    'deferred',
    'no_action'
))
```

| Value | Meaning |
|---|---|
| `team_learning` | Owner approved. Team applies behavioral change going forward. |
| `agent_learning` | Owner approved. Specific agent applies behavioral change. Used with `target_agent`. |
| `guideline_update` | Escalated. Resulted in a GL update via SOP-019. |
| `sop_update` | Escalated. Resulted in a SOP update via SOP-019. |
| `agent_instruction_update` | Escalated. Resulted in an AGENT.md update. |
| `claude_instruction_update` | Escalated. Resulted in a CLAUDE.md update. |
| `backlog_item` | Escalated. Deferred as backlog item for a future governance cycle. |
| `deliverable_lifecycle_item` | Escalated. Routed to the Deliverable Lifecycle system. |
| `rejected` | Owner rejected. Discarded. |
| `deferred` | Owner deferred. Re-surface at a later date. |
| `no_action` | Owner reviewed. No action warranted. |

### 5.3 Relationship between the two fields

These fields are orthogonal:

| Example | `triage_routing` | `processed_outcome` |
|---|---|---|
| Iris flags governance gap → Pace Independence Rule added to SOP-019 | `graduation_candidate` | `sop_update` |
| Agent flags pattern → Owner approves behavior | `standard` | `team_learning` |
| Agent flags observation → Owner rejects | `standard` | `rejected` |
| Urgent CAT-3 → CLAUDE.md updated | `urgent` | `claude_instruction_update` |
| Graduation candidate → new Guideline created | `graduation_candidate` | `guideline_update` |

---

## 6. Corrected Migration Approach and SQL Direction

### 6.1 Why migration is required

The `learning_candidates` table exists in `team-knowledge.db` with 1 live row and old schema values. SQLite does not support altering CHECK constraints in place. Migration uses the create-copy-drop-rename pattern.

### 6.2 Migration SQL (corrected)

```sql
-- Step 1: Create new table with updated schema
CREATE TABLE learning_candidates_v2 (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    title            TEXT NOT NULL,
    description      TEXT,
    level            INTEGER NOT NULL CHECK(level = 2),
    category         TEXT,
    flagged_by       TEXT NOT NULL,
    flagged_at       TEXT NOT NULL DEFAULT (datetime('now')),
    session_id       INTEGER REFERENCES session_logs(id),
    status           TEXT NOT NULL DEFAULT 'captured'
                         CHECK(status IN ('captured','triaged','processed','closed')),
    triaged_at       TEXT,
    triaged_session  INTEGER REFERENCES session_logs(id),
    processed_at     TEXT,
    processed_outcome TEXT CHECK(processed_outcome IN (
        'team_learning','agent_learning',
        'guideline_update','sop_update',
        'agent_instruction_update','claude_instruction_update',
        'backlog_item','deliverable_lifecycle_item',
        'rejected','deferred','no_action'
    )),
    learning_scope   TEXT CHECK(learning_scope IN (
        'team','agent','governance','process','session','tooling','owner_interaction'
    )),
    target_agent     TEXT,
    triage_routing   TEXT CHECK(triage_routing IN (
        'graduation_candidate','standard','urgent'
    )),
    source_domain    TEXT CHECK(source_domain IN (
        'core','personal','kamer_ecommerce','geldstroom_regie','cross_domain'
    )),
    affected_domain  TEXT,
    target_database  TEXT,
    source_reference TEXT,
    resolved_at      TEXT,
    resolution       TEXT,
    owner            TEXT NOT NULL DEFAULT 'larry',
    max_days_captured INTEGER NOT NULL DEFAULT 3,
    created_at       TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Step 2: Migrate existing row (id=4)
INSERT INTO learning_candidates_v2 (
    id, title, description, level, category,
    flagged_by, flagged_at, session_id,
    status,
    triage_routing,
    processed_outcome,
    learning_scope,
    source_domain,
    resolved_at, resolution,
    owner, max_days_captured, created_at
)
SELECT
    id, title, description, level, category,
    flagged_by, flagged_at, session_id,
    'closed',
    'graduation_candidate',
    'sop_update',
    'governance',
    'core',
    resolved_at,
    'Pace Independence Rule added to SOP-019 Section 3 on 2026-06-07. '
    || 'Flagged by Iris during Deliverable Lifecycle Phase 1 implementation. '
    || 'Escalated and applied via Larry in same session.',
    owner,
    max_days_pending,
    created_at
FROM learning_candidates;

-- Step 3: Drop old table
DROP TABLE learning_candidates;

-- Step 4: Rename
ALTER TABLE learning_candidates_v2 RENAME TO learning_candidates;
```

### 6.3 Pre-check requirement

The migration script must include conditional logic:
- If `learning_candidates` does not exist → run CREATE only (skip INSERT migration)
- If `learning_candidates` exists → run full migration
- If `learning_candidates_v2` already exists → abort and report conflict

The domain context fields (`source_domain`, `affected_domain`, `target_database`, `source_reference`) are included in the migration SQL above. They are added to the schema when Decision A is confirmed. If Decision A is not confirmed before Batch 1, these four fields are removed from the DDL until that decision is made.

---

## 7. Learning Candidates Architecture Assessment: Central vs Per-Domain

### 7.1 Background

`learning_candidates` currently exists only in `team-knowledge.db`. The three domain databases do not have this table. The **Owner preferred direction** is centralization. This direction is pending explicit Owner confirmation before Batch 1 is specified.

### 7.2 Why centralizing in `team-knowledge.db` is preferable

**Single source of truth:** Larry is the sole owner of all LCs after flagging. Larry's operational base is `team-knowledge.db`. Placing all LCs in his database aligns ownership with storage location.

**Cross-domain learnings:** Many behavioral observations cross domain boundaries. A per-domain table forces an arbitrary domain assignment for cross-domain LCs, creating duplication or orphaned records.

**Sweep simplicity:** The /close-session LC sweep queries `learning_candidates` for overdue rows. With one central table, this is a single query. Per-domain tables would require four queries across four databases, complicating the sweep with no benefit.

**Governance coherence:** All LCs go through the same governance path regardless of domain of origin: flag → Larry registers → Owner reviews. Centralizing the store reflects that governance coherence.

**Audit trail:** A single table provides a complete team-wide learning history. Per-domain tables create siloed histories that require manual merging for team-level retrospectives.

### 7.3 Risks of per-domain `learning_candidates` tables

| Risk | Severity | Explanation |
|---|---|---|
| Schema drift | High | Each domain database may evolve the schema independently. The standardized LC model breaks down if domains diverge. |
| Duplicate LCs | High | A cross-domain observation may be registered in multiple domain databases, creating conflicting records. |
| Governance fragmentation | Medium | Larry must sweep 4 databases at /close-session instead of 1. Error probability increases. |
| Owner interaction complexity | Medium | Surfacing LCs at /close-session becomes a 4-database join instead of a single query. |
| Cross-domain blindness | Low | Domain specialists reviewing their local database would not see LCs from other domains, even when those LCs affect their behavior. |

### 7.4 Required domain context fields

To make a central table useful for domain-originated learnings, four fields should be added to the schema:

| Field | Type | Purpose | Example values |
|---|---|---|---|
| `source_domain` | TEXT CHECK(enum) | Which domain the observation originated from | `core`, `personal`, `kamer_ecommerce`, `geldstroom_regie`, `cross_domain` |
| `affected_domain` | TEXT | Which domain(s) the learning applies to — may differ from source | Same enum values, or comma-separated for cross-domain |
| `target_database` | TEXT | Which domain database should receive the behavioral update when the LC is processed | `team-knowledge.db`, `personal.db`, etc. |
| `source_reference` | TEXT | Free text pointer to the session, task, or artifact that generated the observation | Session log ID, task ID, deliverable name |

**`source_domain` enum values:**

| Value | Covers |
|---|---|
| `core` | Larry, Iris, Nolan, Pax, Kai — team infrastructure and governance |
| `personal` | Sienna, Penn, Lena — personal domain |
| `kamer_ecommerce` | Vera, Nova, Sasha, Remy, Zara, Bo — Kamer E-commerce domain |
| `geldstroom_regie` | Finn and Geldstroom-specific agents |
| `cross_domain` | Observation originates from or affects multiple domains simultaneously |

### 7.5 How a domain-specific learning should be recorded

When a specialist working in a domain context identifies a behavioral observation:

1. Specialist flags with: title, description, category, `source_domain = '<their domain>'`
2. Ownership transfers to Larry immediately
3. Larry registers the LC in `team-knowledge.db`
4. At Triage: Larry sets `triage_routing`, `affected_domain`, `target_database`
5. At Processing: Larry applies the outcome to the correct database/file as indicated by `target_database` and `processed_outcome`

### 7.6 Effect on /close-session and LC sweep behavior

No change to the sweep query structure. The sweep already queries `team-knowledge.db` only. The central architecture is the correct setup. Domain context fields enable grouping by domain when surfacing LCs to the Owner: "2 LCs from kamer_ecommerce, 1 from core" — display enhancement only.

### 7.7 Architecture decision placement

**Owner preferred direction:** Centralize `learning_candidates` in `team-knowledge.db` only. Domain context captured via `source_domain`, `affected_domain`, `target_database`, `source_reference`.

**Status:** Pending explicit Owner confirmation before Batch 1.

If the Owner confirms this direction, the domain context fields are included in the Batch 1 DDL. If the Owner does not confirm, those four fields are removed from the Batch 1 DDL and the architecture decision is deferred to a separate design session.

---

## 8. Table Consolidation Assessment

### 8.1 `learning_candidates` — canonical SSOT

**State:** Exists in team-knowledge.db only. 1 live row with old schema. Migration required (Section 6).
**Post-consolidation role:** Central SSOT for all team-wide and domain-originated learnings.
**Architecture:** Owner preferred direction: centralized in team-knowledge.db only, pending confirmation. Domain databases will not receive their own tables.
**Verdict:** Keep. Canonical. Centralized (pending Decision A).

### 8.2 `team_log` — operational log

**State:** Exists in all four databases. 90 rows in team-knowledge.db, 4 in kamer-ecommerce.db, 1 in personal.db, 0 in geldstroom-regie.db.
**Schema:** id, log_date, entry_type, specialist, content, session_log_id, created_at. No structured outcome fields.
**Role:** Chronological operational record of team events. Non-canonical for learnings.
**Verdict:** Keep as operational log. Open question Q1 applies (Section 11).

### 8.3 `team_learnings` — does not exist

Confirmed absent from all four databases and all active codebase files. No action.

### 8.4 `agent_learnings` — legacy

**State:** Exists in all four databases. 40 rows in team-knowledge.db, 7 in personal.db, 9 in kamer-ecommerce.db, 0 in geldstroom-regie.db.

**Actual schema (verified):**
```sql
agent_slug, learning_date, what_worked, what_to_improve, session_log_id, created_at
```

**Schema gap:** No `tags` column. The `graduation_candidate` tag mechanism documented in Larry AGENT.md and CLAUDE.md has no column backing it in the implemented table. The Kennisgraduatie mechanism is documented but unimplemented.

**Actual content:** Session-level retrospective reflections (what worked / what to improve per session). Not behavioral observations pending Owner approval. Not aligned with the LC lifecycle model.

**Going forward:** New behavioral observations should go to `learning_candidates`. `agent_learnings` should be deprecated for new writes. Existing rows are historical records — no mandatory migration.

**Verdict:** Legacy. Deprecated for new writes after Batch 3. Open question Q2 applies (Section 11).

---

## 9. Updated Impact Table

All v04 items confirmed. Items marked **[v05 corrected]** replace a v04 item. Items marked **[v05 new]** are new.

### 9.1 GL-022 — confirmed

Items 1–7 (Section 3, 5, 6, 7 rewrites). Batch 1. No change.

### 9.2 Write-List v05 — W-1 DDL — confirmed

Items 8–13, 13b from v04. Confirmed.

| 13c [v05 confirmed] | Domain context fields `source_domain`, `affected_domain`, `target_database`, `source_reference` | Include in Batch 1 DDL pending Decision A. Remove from DDL if Decision A is not confirmed before Batch 1 is specified. |

### 9.3 /close-session Steps 1, 1b, 3b, 4, 5 — confirmed

Items 14–29 from v04. No change.

### 9.4 GL-021 — confirmed

Items 30–31. Batch 2. No change.

### 9.5 gl-index.md — confirmed

Item 32. Batch 1. No change.

### 9.6 Larry AGENT.md — confirmed

Items 33–35. Batch 3. No change.

### 9.7 `agent_learnings` schema gap — confirmed

Item 36b. Batch 3. No change.

### 9.8 Specialist AGENT.md files — confirmed

Item 36 (14+ files). Batch 3. No change.

### 9.9 CLAUDE.md — confirmed

Items 37–39. Batch 3. No change.

### 9.10 Migration SQL — confirmed from v04

Items M-1 through M-4 confirmed. `triage_routing = 'graduation_candidate'`, `processed_outcome = 'sop_update'` for id=4.

### 9.11 No change required — confirmed

Iris AGENT.md LC Flag format, GL-020, SOP-019 footer, CLAUDE.md informal references, archived deliverables.

---

## 10. Updated Batch Plan — Iris Explicitly Named

The safest path is three batches, with Batch 3 deferred pending Q1 and Q2. Batch 1 requires Decision A. Batches 1 and 2 do not require Q1 or Q2.

### Batch 1 — Model definition + migration

**Pre-condition:** Decision A — Owner confirms that `learning_candidates` lives only in `team-knowledge.db`, with domain context captured via `source_domain`, `affected_domain`, `target_database`, `source_reference`.

**Governance path:** Larry prepares the Batch 1 write-list. Iris performs the required review gate per SOP-019. The Owner then authorizes or rejects implementation per SOP-019 CP-1 through CP-4. Implementation proceeds only after Owner authorization.

**Files:**
- GL-022 — Section 3, 5, 6, 7 rewrite
- `learning_candidates` — migration script (create-copy-drop-rename, Section 6)
- gl-index.md — GL-022 description update

**Nature:** Naming + behavioral + DDL migration.
**Data at risk:** 1 row in `learning_candidates`. Migration maps `promoted → closed`, adds `triage_routing = 'graduation_candidate'`, `processed_outcome = 'sop_update'`.
**Affected:** 3 files + 1 database table.
**Does not depend on Q1 or Q2.**

### Batch 2 — Technical alignment

**Pre-condition:** Batch 1 complete and migration verified.

**Governance path:** Larry prepares the Batch 2 write-list. Iris performs the required review gate per SOP-019. The Owner then authorizes or rejects implementation per SOP-019 CP-1 through CP-4. Implementation proceeds only after Owner authorization.

**Files:**
- /close-session Steps 1 and 3b — SQL and Python update
- GL-021 — Section 7 description update

**Nature:** Naming + behavioral.
**Data at risk:** None — SQL query and Python code changes only.
**Affected:** 3 files.
**Does not depend on Q1 or Q2.**

### Batch 3 — Consolidation and behavioral cleanup (deferred)

**Pre-conditions:** Q1 and Q2 answered by Owner (see Section 11). Batches 1 and 2 complete.

**Governance path:** Larry prepares the Batch 3 write-list. Iris performs the required review gate per SOP-019. The Owner then authorizes or rejects implementation per SOP-019 CP-1 through CP-4. Given the breadth (20+ files including 14+ AGENT.md files), the 14+ AGENT.md updates may be grouped as a single bulk execution batch to reduce the number of governance cycles.

**Files in scope:** CLAUDE.md, Larry AGENT.md, 14+ specialist AGENT.md files, /close-session Steps 4 and 5, SOP-009.

**Nature:** Behavioral and naming.
**Affected:** 20+ files.

---

## 11. Open Technical-Behavioral Questions

### Q1 — team_log dual-write (Batch 3 blocker)

**Context:** `team_log` is actively used (90 rows in team-knowledge.db). /close-session Step 4 writes a `team_log` row when a team-level pattern is noted. When an LC is processed with `processed_outcome = 'team_learning'`, the LC record becomes the SSOT. The Step 4 write captures a similar observation but unstructured and without Owner approval.

Under the central architecture, `team_log` is distributed across all four databases while `learning_candidates` is centralized in team-knowledge.db. A `team_log` entry in a domain database can serve as an operational reference for that domain's specialists, even when the learning itself is governed in team-knowledge.db.

**Options:**

| Option | Description |
|---|---|
| A | `learning_candidates` is the sole learning store. Step 4 is redesigned to write `team_log` only for operational events that are not behavioral learnings (session markers, infrastructure events). |
| B | Both records are created: `learning_candidates` for the governed learning, `team_log` for the operational context. The `team_log` row references the LC `id` as a link. |
| C | No change to Step 4. `team_log` and `learning_candidates` operate as parallel records serving different purposes. `team_log` is unreviewed operational context; `learning_candidates` is the governed learning register. |

### Q2 — agent_learnings future (Batch 3 blocker)

**Context:** `agent_learnings` has a session-reflection schema (`what_worked`, `what_to_improve`) with no `tags` column and 56 live rows across databases. Under the central architecture, domain databases will not evolve `agent_learnings` into a learning lifecycle store.

**Options:**

| Option | Description |
|---|---|
| A (preferred under central architecture) | Deprecate `agent_learnings` for new writes. All new behavioral observations go to `learning_candidates` in team-knowledge.db. Existing rows are retained as historical records. CLAUDE.md and AGENT.md files updated in Batch 3. |
| B | Retain `agent_learnings` as a session-quality retrospective table alongside `learning_candidates`. CLAUDE.md updated to make the distinction explicit: `agent_learnings` = session reflection, unstructured, no Owner approval; `learning_candidates` = behavioral observation, governed. |
| C | Selective migration: `what_to_improve` entries describing structural changes become LCs; operational notes stay or are discarded. Then retire the table. |

The central architecture makes Option A the natural fit — domain `agent_learnings` tables would otherwise become an inconsistency alongside a centralized `learning_candidates`.

---

## 12. Recommendation for Next Step After v05

### 12.1 Sequencing — corrected

**Before Batch 1:**
Owner confirms Decision A:
- `learning_candidates` lives only in `team-knowledge.db`
- Domain context captured via `source_domain`, `affected_domain`, `target_database`, `source_reference`

**Then:**
- Larry prepares the Batch 1 write-list
- Iris performs the required review gate per SOP-019
- Owner authorizes or rejects Batch 1 per SOP-019 CP-1 through CP-4

**Before Batch 3 (independent of Batch 1 timing):**
- Owner answers Q1 and Q2

**Q1 and Q2 are not required before Batch 1. Batches 1 and 2 do not depend on Q1 or Q2.**

### 12.2 Full recommended sequence

1. **Owner confirms Decision A.**
   Explicit statement: "learning_candidates lives only in team-knowledge.db with source_domain, affected_domain, target_database, source_reference fields."

2. **Owner answers Q1 and Q2** (can happen in parallel with or after Decision A — does not block Batch 1).

3. **Larry prepares Batch 1 write-list.** Contents: GL-022 rewrite, migration SQL for `learning_candidates` (including domain context fields per Decision A), gl-index.md update.

4. **Iris reviews Batch 1 write-list** per SOP-019 review gate. Iris provides: verdict, risk, exact next prompt for Owner.

5. **Owner authorizes Batch 1** per SOP-019 CP-1 through CP-4.

6. **Execute Batch 1.** Migration runs, GL-022 is live with new states, gl-index updated.

7. **Larry prepares Batch 2 write-list.** Contents: /close-session SQL and Python changes, GL-021 description update.

8. **Iris reviews Batch 2 write-list.** Owner authorizes. Execute Batch 2.

9. **After Q1 and Q2 are confirmed: Larry prepares Batch 3 write-list.** Iris reviews. Owner authorizes. Execute Batch 3.

---

## 13. V04 Correction Summary

| V04 statement | Correction in v05 |
|---|---|
| Section 12: "Two decisions required before Batch 1: Decision A and Q1/Q2" | Incorrect sequencing. Decision A is the only Batch 1 pre-condition. Q1 and Q2 are Batch 3 pre-conditions only. |
| Various: "Owner preferred direction confirmed" for central architecture | Inconsistent. V05 uses consistent language throughout: "Owner preferred direction, pending explicit confirmation before Batch 1." |
| Section 2.3: "Centralized in team-knowledge.db only (see Section 7)" without qualification | Updated to: "Owner preferred direction: centralized in team-knowledge.db only, pending explicit confirmation before Batch 1." |

---

## 14. Change Count Summary

| Batch | Items | Files + DB | Nature | Governance | Pre-condition | Status |
|---|---|---|---|---|---|---|
| Batch 1 | 9 | 3 files + 1 DB migration | Naming + Behavioral + Migration | Larry → Iris review → Owner authorization | Decision A | Ready after Decision A |
| Batch 2 | 9 | 3 files | Naming + Behavioral | Larry → Iris review → Owner authorization | Batch 1 complete | Ready after Batch 1 |
| Batch 3 | 23+ | 20+ files | Naming + Behavioral | Larry → Iris review → Owner authorization | Q1 + Q2 answered | Deferred |
| No change needed | 14 items | — | — | — | — | Confirmed |

**Total active conflicts: 41 items across 26 active files and 1 database.**
**Open design questions: 2 (Q1, Q2 — technical-behavioral — Batch 3 blockers only).**
**Batch 1 pre-condition: Decision A only.**
**No conceptual model questions remain open.**

---

Delivered on: 2026-06-07
Delivered at: /opt/myPKA/Deliverables/20260607_Core_LC Naming Alignment Impact Assessment/lc-naming-alignment-impact-assessment-v05.md
