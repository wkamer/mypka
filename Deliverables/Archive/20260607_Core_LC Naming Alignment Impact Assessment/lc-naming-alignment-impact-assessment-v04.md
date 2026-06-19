# LC Naming Alignment Impact Assessment — v04

**Date:** 2026-06-07
**Author:** Larry
**Supersedes:** lc-naming-alignment-impact-assessment-v03.md
**Status:** Read-only assessment — no files modified, no databases updated
**Scope:** Learning Candidate Lifecycle simplification, naming alignment, table verification, architecture assessment
**Goal model:** `Captured → Triaged → Processed → Closed`

---

## 1. Executive Verdict

V03 contained one conceptual inconsistency: the existing LC row (id=4, old status `promoted`) was mapped to `processed_outcome = 'graduation_candidate'`. This contradicts the Owner-confirmed model in which Graduation Candidate is a classification or routing qualification stored in `triage_routing`, not a processing result stored in `processed_outcome`. V04 corrects this throughout.

V03 also referenced "governance (SOP-019 CP-1 through CP-4)" without naming Iris explicitly. V04 makes Iris explicit in every governance path statement.

V04 adds a new architecture assessment section on whether `learning_candidates` should be centralized in `team-knowledge.db` only or distributed across domain databases, per Owner direction.

All verified database findings from v03 are carried forward unchanged. The Owner-confirmed model is unchanged.

**Changes in v04 vs v03:**
- Section 4 (new): Corrected Graduation Candidate mapping
- Section 5 (new): Corrected `processed_outcome` and `triage_routing` model
- Section 6 (new): Corrected migration SQL
- Section 7 (new): Learning Candidates architecture assessment
- Sections 9–11: Updated impact table, batch plan (Iris named), open questions refined

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

`learning_candidates` = canonical learning lifecycle store and audit trail. Centralized in `team-knowledge.db` only (see Section 7).
`team_log` = chronological operational log — not a canonical learning store.
`team_learnings` = does not exist.
`agent_learnings` = legacy or absorbable — see Section 8.

---

## 3. Database / Table Findings (Verified — Carried from v03)

### 3.1 Verification note

All schemas were verified using Python's `sqlite3` module. The `sqlite3` CLI silently fails on paths with spaces. All v02 "no tables" statements were wrong.

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

**Current schema (as implemented, with old status values):**
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

### 4.1 The inconsistency in v03

V03 mapped the existing row (old status: `promoted`) to:
- `status = 'closed'`
- `processed_outcome = 'graduation_candidate'`

This is incorrect. The Owner-confirmed model places Graduation Candidate in `triage_routing` as a classification, not in `processed_outcome` as a processing result. `processed_outcome` captures what actually happened after the LC was processed.

### 4.2 Correct conceptual model

Two separate fields, two separate concerns:

**`triage_routing`** — determined at Triage. What kind of routing does this LC require?

| Value | Meaning |
|---|---|
| `graduation_candidate` | LC warrants structural escalation: a change to SOP, GL, AGENT.md, CLAUDE.md, or equivalent governed document |
| `standard` | Normal processing path |
| `urgent` | Must be processed in the same session as Triage |

**`processed_outcome`** — determined at Processing. What actually happened?

See Section 5 for the full enum.

### 4.3 Correct migration mapping for row id=4

Row id=4 was flagged by Iris, classified as requiring structural escalation, and resulted in the Pace Independence Rule being added to SOP-019 Section 3.

| Field | Old value | Correct new value | Rationale |
|---|---|---|---|
| `status` | `promoted` | `closed` | LC is in terminal state — escalation completed |
| `triage_routing` | (field did not exist) | `graduation_candidate` | The LC was classified at Triage as requiring structural escalation |
| `processed_outcome` | (field did not exist) | `sop_update` | The actual outcome: SOP-019 was updated |
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

`graduation_candidate` lives here. It is a routing decision made at Triage, not a processing result.

Nullable. Default interpretation when NULL: `standard`.

### 5.2 `processed_outcome` — result field

`graduation_candidate` is explicitly NOT in this enum.

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

Notes on individual values:

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

### 5.3 Relationship between `triage_routing` and `processed_outcome`

These fields are orthogonal. An LC can have any combination:

| Example | `triage_routing` | `processed_outcome` |
|---|---|---|
| Iris flags a governance gap → Pace Independence Rule added | `graduation_candidate` | `sop_update` |
| Agent flags pattern for Owner approval → behavior applied | `standard` | `team_learning` |
| Agent flags behavior → Owner rejects | `standard` | `rejected` |
| Critical CAT-3 observation in same session | `urgent` | `claude_instruction_update` |
| Graduation candidate → becomes a new GL | `graduation_candidate` | `guideline_update` |

The `triage_routing = 'graduation_candidate'` classification signals that the LC needs escalation. The `processed_outcome` records what the escalation produced.

---

## 6. Corrected Migration Approach and SQL Direction

### 6.1 Why migration is required

SQLite does not support altering CHECK constraints in place. The `learning_candidates` table has 1 live row with old schema values. The migration must use the create-copy-drop-rename pattern.

### 6.2 Corrected migration SQL

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
    source_reference TEXT,
    resolved_at      TEXT,
    resolution       TEXT,
    owner            TEXT NOT NULL DEFAULT 'larry',
    max_days_captured INTEGER NOT NULL DEFAULT 3,
    created_at       TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Step 2: Migrate existing row (id=4)
-- Old: status='promoted' (terminal — escalation completed)
-- New: status='closed', triage_routing='graduation_candidate', processed_outcome='sop_update'
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

The migration script must include a pre-check:
- If `learning_candidates` does not exist → run CREATE only (skip the INSERT migration step)
- If `learning_candidates` exists → run the full migration
- If `learning_candidates_v2` already exists → abort and report conflict

The original Write-List v05 had an abort-if-table-exists pre-check. That pre-check must be replaced with the above conditional logic.

---

## 7. Learning Candidates Architecture Assessment: Central vs Per-Domain

### 7.1 Background

`learning_candidates` currently exists only in `team-knowledge.db` (1 row). The three domain databases (personal.db, kamer-ecommerce.db, geldstroom-regie.db) do not have a `learning_candidates` table. The Owner's preferred direction is to keep it centralized. This section assesses that direction.

### 7.2 Why centralizing in `team-knowledge.db` is preferable

**Single source of truth:** Larry is the sole owner of all LCs after flagging (GL-022 Section 4). Larry's operational base is `team-knowledge.db`. Placing all LCs in his database aligns ownership with storage location. No cross-database ownership ambiguity.

**Cross-domain learnings:** Many behavioral observations cross domain boundaries. A pattern observed during a Kamer E-commerce session may affect how Larry orchestrates across all domains, or how Nolan writes AGENT.md files. A per-domain table would force an arbitrary domain assignment for cross-domain LCs, creating duplication or orphaned records.

**Sweep simplicity:** The /close-session LC sweep queries `learning_candidates` for overdue rows. With one central table, this is a single query. With per-domain tables, the sweep would require four queries across four databases, a UNION-style result, and cross-database status updates — adding complexity for no benefit.

**Governance coherence:** All LCs go through the same governance path: flag → Larry registers → Owner reviews. This process is domain-agnostic. Centralizing the store reflects that governance coherence.

**Audit trail:** A single table provides a complete team-wide learning history in one place. Per-domain tables create siloed histories that require manual merging for team-level retrospectives.

### 7.3 Risks of per-domain `learning_candidates` tables

| Risk | Severity | Explanation |
|---|---|---|
| Schema drift | High | Each domain database may evolve the schema at different times. The standardized LC lifecycle model breaks down if personal.db and kamer-ecommerce.db have different column sets. |
| Duplicate LCs | High | A cross-domain observation may be registered in both the personal and kamer_ecommerce databases, creating conflicting records with no way to deduplicate. |
| Governance fragmentation | Medium | Larry must sweep 4 databases at /close-session instead of 1. Error probability increases. |
| Owner interaction complexity | Medium | Surfacing LCs to the Owner at /close-session becomes a 4-database join instead of a single query. |
| Cross-domain blindness | Low | Domain specialists reviewing their domain database would not see LCs from other domains, even if those LCs affect their behavior. |

### 7.4 Required domain context fields

To make a central table useful for domain-originated learnings, four fields should be added to the `learning_candidates` schema:

| Field | Type | Purpose | Example values |
|---|---|---|---|
| `source_domain` | TEXT CHECK(enum) | Which domain the observation originated from | `core`, `personal`, `kamer_ecommerce`, `geldstroom_regie`, `cross_domain` |
| `affected_domain` | TEXT (free text or enum) | Which domain(s) the learning applies to — may differ from source | Can be a comma-separated list for cross-domain LCs, or same as `source_domain` |
| `target_database` | TEXT | Which domain database should receive the behavioral update when the LC is processed | `team-knowledge.db`, `personal.db`, `kamer e-commerce.db`, `geldstroom-regie.db` |
| `source_reference` | TEXT | Free text pointer to the session, task, or artifact that generated the observation | Session log ID, task ID, deliverable name |

**Domain enum values for `source_domain`:**

| Value | Covers |
|---|---|
| `core` | Larry, Iris, Nolan, Pax, Kai — team infrastructure and governance |
| `personal` | Sienna, Penn, Lena — personal domain |
| `kamer_ecommerce` | Vera, Nova, Sasha, Remy, Zara, Bo — Kamer E-commerce domain |
| `geldstroom_regie` | Finn and Geldstroom-specific agents — Geldstroom Regie domain |
| `cross_domain` | Observation originates from or affects multiple domains simultaneously |

### 7.5 How a domain-specific learning should be recorded

When a specialist working in a domain context identifies a behavioral observation:

1. Specialist flags the observation with: title, description, category (GL-020 CAT), `source_domain = '<their domain>'`
2. Ownership transfers to Larry immediately
3. Larry registers the LC in `team-knowledge.db` (central location)
4. At Triage: Larry sets `triage_routing`, `affected_domain`, `target_database`
5. At Processing: Larry applies the outcome to the correct database/file as indicated by `target_database` and `processed_outcome`

Example: Nova (Kamer E-commerce) flags an observation about order processing. LC is stored in `team-knowledge.db` with `source_domain = 'kamer_ecommerce'`, `target_database = 'kamer e-commerce.db'`. When processed with `processed_outcome = 'agent_instruction_update'`, the update is applied to Nova's AGENT.md.

### 7.6 Effect on /close-session and LC sweep behavior

No change to the sweep query. The sweep already queries `team-knowledge.db` only. The central architecture is already the correct setup. Domain context fields (`source_domain`, `affected_domain`) are filter/display enhancements, not structural changes to the sweep logic.

The only behavioral addition: when surfacing LCs to the Owner at /close-session, the domain context fields allow Larry to group or label LCs by domain — "2 LCs from kamer_ecommerce, 1 from core" — without changing the query structure.

### 7.7 Architecture decision and Batch 1 placement

**Owner preferred direction confirmed:** Central table in `team-knowledge.db` only.

The domain context fields (`source_domain`, `affected_domain`, `target_database`, `source_reference`) are schema additions. They have no behavioral dependency and can be included in the Batch 1 DDL without requiring any additional governance cycle.

However, they require the Owner to explicitly confirm centralization before Batch 1 is written, since this is an architecture-level decision (not just a naming correction). The recommendation is to resolve the architecture direction as an explicit Owner decision before the Batch 1 write-list is prepared.

**Recommendation:** Include `source_domain`, `affected_domain`, `target_database`, and `source_reference` fields in the Batch 1 DDL once the Owner confirms the centralized architecture. This avoids a second migration later.

---

## 8. Table Consolidation Assessment

### 8.1 `learning_candidates` — canonical SSOT

**State:** Exists in team-knowledge.db only. 1 live row with old schema. Migration required (see Section 6).
**Post-consolidation role:** Central SSOT for all team-wide and domain-originated learnings.
**Domain databases:** Will not receive their own `learning_candidates` tables. Domain context is captured via `source_domain` and `affected_domain` fields in the central table.
**Verdict:** Keep. Canonical. Centralized.

### 8.2 `team_log` — operational log

**State:** Exists in all four databases. 90 rows in team-knowledge.db, 4 in kamer-ecommerce.db, 1 in personal.db.
**Schema:** id, log_date, entry_type, specialist, content, session_log_id, created_at. No structured outcome fields.
**Role:** Chronological operational record of team events. Written at /close-session Step 4 when a team-level pattern is noted.
**Overlap with `learning_candidates`:** The `team_log` Step 4 write and an LC with `processed_outcome = 'team_learning'` both capture team-level observations, but at different governance levels. `team_log` is unreviewed; `learning_candidates` is Owner-approved.
**Verdict:** Keep as operational log. Non-canonical for learnings. Open question Q1 applies (see Section 11).

### 8.3 `team_learnings` — does not exist

Confirmed absent from all four databases and all active codebase files. No action.

### 8.4 `agent_learnings` — legacy

**State:** Exists in all four databases. 40 rows in team-knowledge.db, 7 in personal.db, 9 in kamer-ecommerce.db, 0 in geldstroom-regie.db.

**Actual schema (verified):**
```sql
agent_slug, learning_date, what_worked, what_to_improve, session_log_id, created_at
```

**Schema gap:** No `tags` column. The `graduation_candidate` tag mechanism documented in Larry AGENT.md and CLAUDE.md has no column to write to. The mechanism is documented but unimplemented.

**Actual content:** Session-level retrospective reflections (what worked / what to improve per session). Not behavioral observations pending Owner approval. Not aligned with the LC lifecycle model.

**Going forward:** New behavioral observations should go to `learning_candidates`. `agent_learnings` should be deprecated for new writes (Q2). Existing rows are historical records — no mandatory migration.

**Verdict:** Legacy. Preferred direction: deprecate for new writes. Existing rows are retained as historical records. Open question Q2 applies (see Section 11).

---

## 9. Updated Impact Table

All v03 items confirmed unless marked **[v04 corrected]**.

### 9.1 GL-022 — confirmed from v03

Items 1–7 (Section 3, 5, 6, 7 rewrites). Batch 1. No change.

### 9.2 Write-List v05 — W-1 DDL

| # | Item | Update in v04 |
|---|---|---|
| 8 | `status` CHECK | No change: `('captured','triaged','processed','closed')` |
| 9 | `status` DEFAULT | No change: `DEFAULT 'captured'` |
| 10 | `surfaced_at` → `triaged_at` | No change |
| 11 | `surfaced_session` → `triaged_session` | No change |
| 12 | `max_days_pending` → `max_days_captured` | No change |
| 13 | Add `processed_outcome`, `processed_at`, `learning_scope`, `target_agent`, `triage_routing` | No change |
| 13b | Migration required (not fresh CREATE) | No change |
| 13c [v04 new] | Add `source_domain`, `affected_domain`, `target_database`, `source_reference` fields | New — pending Owner confirmation of central architecture (Section 7.7) |

### 9.3 /close-session — Steps 1, 1b, 3b, 4, 5 — confirmed from v03

Items 14–29. No change.

### 9.4 GL-021 — confirmed from v03

Items 30–31. Batch 2. No change.

### 9.5 gl-index.md — confirmed from v03

Item 32. Batch 1. No change.

### 9.6 Larry AGENT.md — confirmed from v03

Items 33–35. Batch 3. No change.

### 9.7 `agent_learnings` schema gap — confirmed from v03

Item 36b. Batch 3. No change.

### 9.8 All specialist AGENT.md files — confirmed from v03

Item 36 (14+ files). Batch 3. No change.

### 9.9 CLAUDE.md — confirmed from v03

Items 37–39. Batch 3. No change.

### 9.10 Migration SQL — corrected [v04 corrected]

| # | Item | V03 | V04 correction |
|---|---|---|---|
| M-1 [v04 corrected] | `processed_outcome` in migration | `'graduation_candidate'` | Removed. `processed_outcome` for id=4 must be `'sop_update'`. |
| M-2 [v04 corrected] | `triage_routing` in migration | Not set | `'graduation_candidate'` — the classification that drove escalation |
| M-3 [v04 new] | `source_domain` in migration | Not present | `'core'` — observation originated in core governance |
| M-4 [v04 new] | `learning_scope` in migration | Not set | `'governance'` — governance-scope observation |

### 9.11 No change required — confirmed from v03

Iris AGENT.md LC Flag format, GL-020, SOP-019 footer, CLAUDE.md informal references, archived deliverables.

---

## 10. Updated Batch Plan — Iris Explicitly Named

The safest path is three batches, with Batch 3 deferred pending resolution of Q1 and Q2 and pending Owner confirmation of the central learning_candidates architecture.

### Batch 1 — Model definition + migration

**Scope:** GL-022 rewrite, `learning_candidates` DDL migration, gl-index update.

**Governance path:** Larry prepares the Batch 1 write-list. Iris performs the required review gate per SOP-019. The Owner then authorizes or rejects implementation per SOP-019 CP-1 through CP-4. Implementation proceeds only after Owner authorization.

**Files:**
- GL-022 — Section 3, 5, 6, 7 rewrite
- `learning_candidates` — migration script (create-copy-drop-rename, see Section 6)
- gl-index.md — GL-022 description update

**Pending decision:** Include `source_domain`, `affected_domain`, `target_database`, `source_reference` fields in Batch 1 DDL once Owner confirms central architecture (Section 7.7). This is a pre-condition for the Batch 1 write-list.

**Nature:** Naming + behavioral + DDL migration.
**Data at risk:** 1 row in `learning_candidates`. Migration maps `promoted → closed`, adds `triage_routing = 'graduation_candidate'`, `processed_outcome = 'sop_update'`.
**Affected:** 3 files + 1 database table.

### Batch 2 — Technical alignment

**Scope:** /close-session Steps 1 and 3b SQL alignment, GL-021 description update.

**Governance path:** Larry prepares the Batch 2 write-list. Iris performs the required review gate per SOP-019. The Owner then authorizes or rejects implementation per SOP-019 CP-1 through CP-4. Implementation proceeds only after Owner authorization.

**Dependency:** Batch 1 must be complete and the migration verified before Batch 2 SQL references the new column names.

**Nature:** Naming + behavioral (resolve_lc function update).
**Data at risk:** None — SQL query and Python code changes only.
**Affected:** 3 files.

### Batch 3 — Consolidation and behavioral cleanup (deferred)

**Deferred pending Q1 and Q2 (see Section 11).**

**Governance path when ready:** Larry prepares the Batch 3 write-list. Given the breadth of files (20+ including 14+ AGENT.md files), Iris performs the required review gate. The Owner authorizes per SOP-019. The 14+ AGENT.md updates may be grouped as a single bulk execution batch to reduce the number of governance cycles.

**Files in scope:** CLAUDE.md, Larry AGENT.md, 14+ specialist AGENT.md files, /close-session Steps 4 and 5, SOP-009.

**Nature:** Behavioral and naming.
**Affected:** 20+ files.

---

## 11. Open Technical-Behavioral Questions

### Q1 — team_log dual-write behavior (Batch 3 blocker)

**Context:** `team_log` is actively used (90 rows in team-knowledge.db, written at /close-session Step 4). When an LC is processed with `processed_outcome = 'team_learning'`, the LC in team-knowledge.db becomes the SSOT for the learning. The `team_log` Step 4 write captures the same type of observation — but unstructured and without Owner approval.

**Updated context with central architecture:** Since `learning_candidates` is centralized in team-knowledge.db, and `team_log` is distributed across all four databases, the `team_log` write in domain databases (kamer-ecommerce.db, personal.db, etc.) continues to serve as a local operational log for that domain's session activity, even after an LC is processed in team-knowledge.db. The two records are in different databases and serve different roles.

**Options:**

| Option | Description |
|---|---|
| A | `learning_candidates` is the sole learning store. Step 4 is redesigned to write `team_log` only for operational events that are not behavioral learnings (session markers, infrastructure events, procedural notes). |
| B | Both records are created: `learning_candidates` for the governed learning, `team_log` for the operational context. The `team_log` row references the LC `id` as a link. |
| C | No change to Step 4. `team_log` and `learning_candidates` remain parallel, serving different purposes. `team_log` is the operational context log; `learning_candidates` is the governed learning register. |

### Q2 — agent_learnings future (Batch 3 blocker)

**Context:** `agent_learnings` has a session-reflection schema (`what_worked`, `what_to_improve`) with no `tags` column. It is used for retrospective quality notes, not behavioral observations pending Owner approval. 56 live rows across databases.

**Updated context with central architecture:** Under centralization, `agent_learnings` in domain databases clearly cannot evolve into a learning lifecycle store. New behavioral observations from domain specialists should go directly to `learning_candidates` in team-knowledge.db. This makes Option A the natural fit.

**Options:**

| Option | Description |
|---|---|
| A (preferred) | Deprecate `agent_learnings` for new writes. All new behavioral observations go to `learning_candidates`. Existing rows are retained as historical records. CLAUDE.md and AGENT.md files are updated in Batch 3. |
| B | Retain `agent_learnings` as a session-quality retrospective table alongside `learning_candidates`. Update CLAUDE.md to make the distinction explicit: `agent_learnings` = session reflection, unstructured, no Owner approval; `learning_candidates` = behavioral observation, governed. |
| C | Selective migration: `what_to_improve` entries describing structural changes become LCs; operational notes stay or are discarded. Then retire the table. |

The central architecture direction reduces ambiguity: Option A is the cleanest path.

---

## 12. Recommendation for Next Step After v04

### 12.1 Two decisions required before Batch 1 can be specified

**Decision A — Architecture confirmation:**
Owner explicitly confirms: `learning_candidates` lives only in `team-knowledge.db`. Domain context is captured via `source_domain`, `affected_domain`, `target_database`, `source_reference` fields in the central table. These fields are included in the Batch 1 DDL.

**Decision B — Q1 and Q2:**
Owner selects an option for each (A, B, or C). These unblock Batch 3 scope. Batches 1 and 2 do not depend on Q1 and Q2.

### 12.2 Recommended sequence after decisions

1. **Owner confirms Decision A and answers Q1/Q2.**

2. **Prepare Batch 1 write-list.** Larry prepares a write-list covering: GL-022 rewrite, migration SQL for `learning_candidates` (including domain context fields), gl-index.md update. This is the first artifact submitted to Iris for review.

3. **Iris reviews Batch 1 write-list** per SOP-019 review gate. Iris provides: verdict, risk, exact next prompt for Owner.

4. **Owner authorizes Batch 1** per SOP-019 CP-1 through CP-4.

5. **Execute Batch 1.** Migration runs, GL-022 is live with new states, gl-index is updated.

6. **Prepare Batch 2 write-list.** Larry prepares /close-session and GL-021 changes. Submitted to Iris for review.

7. **Iris reviews Batch 2 write-list.** Owner authorizes. Execute.

8. **Prepare Batch 3 write-list** (after Q1 and Q2 are confirmed). Iris reviews. Owner authorizes. Execute.

---

## 13. V03 Correction Summary

| V03 statement | Correction in v04 |
|---|---|
| Existing row id=4 maps to `processed_outcome = 'graduation_candidate'` | Incorrect. `graduation_candidate` belongs in `triage_routing`. For id=4: `triage_routing = 'graduation_candidate'`, `processed_outcome = 'sop_update'`. |
| `processed_outcome` enum included `graduation_candidate` | Removed. The enum contains processing results only (see Section 5.2). |
| Migration SQL used `'graduation_candidate'` as `processed_outcome` value | Corrected. Migration SQL now sets `triage_routing = 'graduation_candidate'` and `processed_outcome = 'sop_update'` for id=4. |
| Governance path referred to "SOP-019 CP-1 through CP-4" without naming Iris | Corrected. All batch governance paths now explicitly name Larry (write-list preparation), Iris (review gate), and Owner (authorization). |
| No architecture assessment for central vs per-domain `learning_candidates` | Added as Section 7. |

---

## 14. Change Count Summary

| Batch | Items | Files + DB | Nature | Governance | Status |
|---|---|---|---|---|---|
| Batch 1 | 9 (incl. domain context fields) | 3 files + 1 DB migration | Naming + Behavioral + Migration | Larry → Iris review → Owner authorization | Ready after Decision A |
| Batch 2 | 9 | 3 files | Naming + Behavioral | Larry → Iris review → Owner authorization | Ready after Batch 1 |
| Batch 3 | 23+ | 20+ files | Naming + Behavioral | Larry → Iris review → Owner authorization | Deferred — Q1 and Q2 |
| No change needed | 14 items | — | — | — | Confirmed |

**Total active conflicts: 41 items across 26 active files and 1 database.**
**Open design questions: 2 (Q1, Q2 — technical-behavioral only).**
**Pre-conditions for Batch 1: Decision A (architecture confirmation) required.**
**No conceptual model questions remain open.**

---

Delivered on: 2026-06-07
Delivered at: /opt/myPKA/Deliverables/20260607_Core_LC Naming Alignment Impact Assessment/lc-naming-alignment-impact-assessment-v04.md
