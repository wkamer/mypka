# LC Naming Alignment Impact Assessment — v03

**Date:** 2026-06-07
**Author:** Larry
**Supersedes:** lc-naming-alignment-impact-assessment-v02.md
**Status:** Read-only assessment — no files modified, no databases updated
**Scope:** Learning Candidate Lifecycle simplification, naming alignment, table verification
**Goal model:** `Captured → Triaged → Processed → Closed`

---

## 1. Executive Verdict

V02 contained a critical database finding error. The statement "all four domain databases exist as files but contain no tables" was wrong. The error was caused by the `sqlite3` CLI silently failing on file paths containing spaces. V03 corrects this using Python's `sqlite3` module, which handles these paths correctly.

**Correction scope:** Section 3 (database findings) is completely replaced. Sections 4–5 (conceptual and naming corrections) are confirmed unchanged. Section 6 (table consolidation) is updated with verified schemas and row counts. Section 7 (schema direction) is updated to reflect a migration requirement, not a fresh CREATE. Section 8 (impact table) adds migration risk items. Section 9 (batch plan) updates Batch 1 risk accordingly.

All Owner-confirmed decisions from v02 remain unchanged.

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

### 2.2 Terminology decisions (confirmed)

| Term | Definition |
|---|---|
| LC | Learning Candidate |
| GL | Guideline (KE prefix reserved for Key Element files) |
| Graduation Candidate | Classification or routing qualification during Triage or Process — not a separate lifecycle |
| Team Learning | A possible `processed_outcome` — not a lifecycle state |
| Landing | Not the formal lifecycle term — not to be used |
| Process / Processed | Formal wording |

### 2.3 SSOT for learnings

`learning_candidates` = canonical learning lifecycle store and audit trail.
`team_log` = chronological operational log — not a canonical learning store.
`team_learnings` = not canonical (does not exist — see Section 3).
`agent_learnings` = legacy or absorbable — see Section 6.

---

## 3. Database / Table Findings — Verified

### 3.1 Verification method

All schemas were verified using Python's `sqlite3` module directly against the database files. The `sqlite3` CLI was silently failing on file paths containing spaces, producing empty output. All v02 statements claiming "no tables implemented" are incorrect and replaced below.

### 3.2 Database file inventory

| Database | Path | File size | Last written | File type |
|---|---|---|---|---|
| team-knowledge.db | `/opt/myPKA/Team Knowledge/team-knowledge.db` | 272K | 2026-06-07 | SQLite 3.x |
| personal.db | `/opt/myPKA/PKM/personal.db` | 192K | 2026-06-07 | SQLite 3.x |
| kamer-ecommerce.db | `/opt/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db` | 60K | 2026-06-03 | SQLite 3.x |
| geldstroom-regie.db | `/opt/myPKA/Team Knowledge/Geldstroom Regie/geldstroom-regie.db` | 48K | 2026-06-03 | SQLite 3.x |
| UMC memory database | PostgreSQL via `postgresql://mypka:...` | N/A | N/A | PostgreSQL |

The UMC memory database is PostgreSQL, not SQLite. It is a separate infrastructure component. Its tables (`tool_logs`, `memory_summaries`) are unrelated to the LC lifecycle.

### 3.3 `team-knowledge.db` — verified schema and row counts

| Table | Row count | Status |
|---|---|---|
| `session_logs` | 174 | Active |
| `team_log` | 90 | Active |
| `agent_learnings` | 40 | Active |
| `delegation_outcomes` | 53 | Active |
| `team_tasks` | 77 | Active |
| `deliverable_lifecycle` | 21 | Active |
| `learning_candidates` | 1 | Active — OLD schema |

**`learning_candidates` DDL (current — as implemented):**
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

**Existing row (id=4):**
- Title: "Governance checkpoints bypassed when Owner drives implementation interactively — CP invocation required even under Owner-directed pace"
- Status: `promoted`
- Flagged by: `iris`
- Flagged at: 2026-06-07
- Category: CAT-3, Level: 2
- Description: Deliverable Lifecycle Phase 1 governance checkpoints not invoked (per SOP-019 amendment session today)

This is the LC that was promoted to Level 3 and resulted in the Pace Independence Rule added to SOP-019. It is in a terminal state. In the new lifecycle model it maps to `closed` with `processed_outcome = 'graduation_candidate'` (the escalation produced a confirmed structural change).

**`agent_learnings` DDL (current — identical across all databases):**
```sql
CREATE TABLE agent_learnings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_slug TEXT NOT NULL,
    learning_date DATE NOT NULL,
    what_worked TEXT,
    what_to_improve TEXT,
    session_log_id INTEGER REFERENCES session_logs(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

**`team_log` DDL (current — identical across all databases):**
```sql
CREATE TABLE team_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_date DATE NOT NULL,
    entry_type TEXT,
    specialist TEXT,
    content TEXT NOT NULL,
    session_log_id INTEGER REFERENCES session_logs(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

**`delegation_outcomes` DDL (current):**
```sql
CREATE TABLE delegation_outcomes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    delegation_date DATE NOT NULL,
    from_agent TEXT DEFAULT 'larry',
    to_agent TEXT NOT NULL,
    brief_summary TEXT,
    outcome TEXT,
    duration_text TEXT,
    session_log_id INTEGER REFERENCES session_logs(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

**`deliverable_lifecycle` DDL (current):**
```sql
CREATE TABLE deliverable_lifecycle (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    artifact_name       TEXT NOT NULL UNIQUE,
    artifact_type       TEXT NOT NULL,
    state               TEXT NOT NULL DEFAULT 'ready',
    proposed_destination TEXT,
    destination_domain  TEXT,
    processing_notes    TEXT,
    superseded_by       TEXT,
    source_session      TEXT,
    agent               TEXT,
    registered_at       TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    state_changed_at    TEXT,
    processed_at        TEXT,
    owner_decision      TEXT,
    owner_decision_at   TEXT
)
```

**`session_logs` DDL (current):**
```sql
CREATE TABLE session_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_date DATE NOT NULL,
    session_title TEXT,
    duration_text TEXT,
    topics TEXT,
    summary TEXT,
    decisions TEXT,
    actions_taken TEXT,
    delegations TEXT,
    open_items TEXT,
    raw_content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    agent_slug TEXT
)
```

### 3.4 `personal.db` — verified schema and row counts

| Table | Row count | Notes |
|---|---|---|
| `session_logs` | 59 | Active |
| `team_tasks` | 28 | Active |
| `team_log` | 1 | Active |
| `agent_learnings` | 7 | Active |
| `delegation_outcomes` | 0 | Empty |
| `journal` | 65 | Active — personal domain |
| `people` | unknown | Active — CRM |
| `contact_interactions` | 48 | Active — CRM |
| `daily_growth` | 11 | Active — health tracking |
| `habits` | 1 | Active |
| `documents` | 1 | Active |
| `document_mentions` | 1 | Active |
| `notes` | unknown | Active |

`learning_candidates` is NOT present in `personal.db`.
`deliverable_lifecycle` is NOT present in `personal.db`.

### 3.5 `kamer-ecommerce.db` — verified schema and row counts

| Table | Row count | Notes |
|---|---|---|
| `session_logs` | 9 | Active |
| `team_tasks` | 40 | Active |
| `team_log` | 4 | Active |
| `agent_learnings` | 9 | Active |
| `delegation_outcomes` | 0 | Empty |

`learning_candidates` is NOT present in `kamer-ecommerce.db`.
`deliverable_lifecycle` is NOT present in `kamer-ecommerce.db`.

### 3.6 `geldstroom-regie.db` — verified schema and row counts

| Table | Row count | Notes |
|---|---|---|
| `session_logs` | 11 | Active |
| `team_tasks` | 27 | Active |
| `team_log` | 0 | Created, empty |
| `agent_learnings` | 0 | Created, empty |
| `delegation_outcomes` | 0 | Created, empty |

`learning_candidates` is NOT present in `geldstroom-regie.db`.
`deliverable_lifecycle` is NOT present in `geldstroom-regie.db`.

### 3.7 Table presence by database — summary

| Table | team-knowledge.db | personal.db | kamer-ecommerce.db | geldstroom-regie.db |
|---|---|---|---|---|
| `session_logs` | Yes, 174 rows | Yes, 59 rows | Yes, 9 rows | Yes, 11 rows |
| `team_log` | Yes, 90 rows | Yes, 1 row | Yes, 4 rows | Yes, 0 rows |
| `agent_learnings` | Yes, 40 rows | Yes, 7 rows | Yes, 9 rows | Yes, 0 rows |
| `delegation_outcomes` | Yes, 53 rows | Yes, 0 rows | Yes, 0 rows | Yes, 0 rows |
| `team_tasks` | Yes, 77 rows | Yes, 28 rows | Yes, 40 rows | Yes, 27 rows |
| `learning_candidates` | **Yes, 1 row** | No | No | No |
| `deliverable_lifecycle` | **Yes, 21 rows** | No | No | No |

### 3.8 Tables searched and not found anywhere

| Table | Conclusion |
|---|---|
| `team_learnings` | Does not exist in any database. Confirmed absent. |
| `memory_summaries` | Exists in PostgreSQL UMC database only — not in SQLite domain databases. |
| `tool_logs` | Exists in PostgreSQL UMC database only — not in SQLite domain databases. |

---

## 4. Conceptual Corrections from v01

Unchanged from v02. See v02 Section 4 for full text.

Key points:
- Team Learning is a confirmed `processed_outcome` value, not an open conceptual question
- Graduation Candidate is a confirmed classification/routing qualification, not an open conceptual question
- Step 5 of /close-session retains the "Graduation candidates" concept but execution should feed the LC lifecycle, not bypass it
- Remaining questions are technical-behavioral only (Q1 and Q2 — see Section 10)

---

## 5. Naming Corrections from v01

Unchanged from v02. Key items:

- Implementation path: three batches, with Batch 3 deferred
- Print labels: `Learning Candidates captured: {total}, Learning Candidates overdue_for_triage: {overdue}` and `Learning Candidates triaged: {updated}`
- Decision verb: `escalate` not `promote-to-sop`
- Decision keys in `resolve_lc`: `apply`, `reject`, `escalate`

---

## 6. Table Consolidation Assessment — Updated

### 6.1 `learning_candidates` — canonical SSOT (table exists, 1 row, OLD schema)

**State:** Table exists in `team-knowledge.db` only. 1 live row, status `promoted`. The schema uses old status values and lacks the new fields required by the Owner's model.

**Migration required:** Yes. SQLite does not support ALTER COLUMN to change CHECK constraints. The migration path for Batch 1 is:
1. CREATE new table `learning_candidates_new` with updated schema
2. INSERT SELECT from `learning_candidates` with status remapping (`promoted` → `closed`, `processed_outcome = 'graduation_candidate'`)
3. DROP TABLE `learning_candidates`
4. ALTER TABLE `learning_candidates_new` RENAME TO `learning_candidates`
5. Recreate indexes if needed

The 1 existing row has status `promoted` and represents a completed governance escalation (Iris flagged, promoted to SOP-019, SOP-019 amendment executed today). In the new model: `status = 'closed'`, `processed_outcome = 'graduation_candidate'`.

**Present in domain databases:** team-knowledge.db only. `personal.db`, `kamer-ecommerce.db`, `geldstroom-regie.db` do not have this table. No migration needed for those.

**Role after consolidation:** Canonical SSOT for learning lifecycle across all domains. Whether to extend `learning_candidates` to the other domain databases is a separate design question (outside scope of this assessment).

### 6.2 `team_log` — operational log, non-canonical (table exists, live data)

**State:** Exists in all four databases. Active use: 90 rows in team-knowledge.db, 4 in kamer-ecommerce.db, 1 in personal.db.

**Schema:** Minimal — id, log_date, entry_type, specialist, content, session_log_id, created_at. No structured outcome fields.

**Purpose:** Chronological operational record of team events, patterns, and session-level observations. Functions as a timestamped log of what happened at team level.

**Overlap with LC `processed_outcome = 'team_learning'`:** The `team_log` is written at /close-session Step 4 when "a new pattern or insight emerged that affects team level." This is operationally close to what an LC with `processed_outcome = 'team_learning'` captures. The distinction is one of governance: `team_log` is unreviewed and unstructured; `learning_candidates` is governed with Owner approval.

**Verdict:** Keep as operational log. Non-canonical for learnings. The open question (Q1) is whether Step 4 writes become redundant once `learning_candidates` is the SSOT — see Section 10.

### 6.3 `team_learnings` — does not exist

Confirmed absent from all four databases and from all active codebase files. No action required.

### 6.4 `agent_learnings` — legacy, schema divergence found (table exists, live data)

**State:** Exists in all four databases. 40 rows in team-knowledge.db, 7 in personal.db, 9 in kamer-ecommerce.db.

**Actual schema (verified):**
```sql
agent_slug TEXT NOT NULL
learning_date DATE NOT NULL
what_worked TEXT
what_to_improve TEXT
session_log_id INTEGER REFERENCES session_logs(id)
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```

**Schema divergence finding:** CLAUDE.md and Larry AGENT.md describe a `graduation_candidate` tag being written to `agent_learnings.tags`. The actual schema has no `tags` column. The Kennisgraduatie mechanism referencing `tags = 'graduation_candidate'` has no column to write to in the implemented table. This is a pre-existing gap between documented intent and actual implementation — not introduced by the LC simplification.

**Actual content observed (last 5 rows, team-knowledge.db):**
The table is used as a session reflection log: `what_worked` captures what went well in a session, `what_to_improve` captures improvement areas. Examples: "Iris review as a gate caught scope ambiguity," "Mail-IDs in project.md tijdlijn altijd als klikbare link opnemen," etc.

This pattern is a retrospective quality note, not a behavioral observation pending Owner approval. It is closer to a team_log entry than to an LC.

**Consequence for absorption assessment:**

The `agent_learnings` table, as actually implemented and used, does NOT currently produce LC-type records. It produces session reflection notes. The two use cases break down as:

| Content type in `agent_learnings` | Absorption target |
|---|---|
| `what_to_improve` entries with structural behavioral change ("should always do X") | Absorbable as LC: `learning_scope = 'agent'`, `target_agent = agent_slug`, `flagged_by = agent_slug` |
| `what_worked` entries (operational quality notes, no behavioral change) | Belongs in `team_log` or discarded |
| `what_to_improve` entries with minor operational notes | `team_log` territory or discard |

Going forward: new behavioral observations that require Owner review should be written directly to `learning_candidates`. The `agent_learnings` table can be deprecated for new writes once the LC workflow is established.

The 56 existing rows across databases (team-knowledge.db: 40, personal.db: 7, kamer-ecommerce.db: 9) are historical records. No migration of existing rows into `learning_candidates` is required unless the Owner explicitly wishes to retroactively process them.

**Verdict:** Legacy. The `graduation_candidate` tag mechanism described in CLAUDE.md is unimplemented (no `tags` column). New behavioral observations should go to `learning_candidates` going forward. The Kennisgraduatie block in Larry AGENT.md must be updated to reflect this (Batch 3). Existing rows are historical records — no retroactive migration needed.

---

## 7. Recommended `learning_candidates` Schema Direction — Updated

The main change from v02 is that this is now a **migration of an existing table with 1 live row**, not a fresh CREATE. The schema direction itself is unchanged.

### 7.1 Migration approach

SQLite does not support altering CHECK constraints in place. The migration must use the create-copy-drop-rename pattern:

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
        'team_learning','agent_learning','guideline_update','sop_update',
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
    resolved_at      TEXT,
    resolution       TEXT,
    owner            TEXT NOT NULL DEFAULT 'larry',
    max_days_captured INTEGER NOT NULL DEFAULT 3,
    created_at       TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Step 2: Migrate existing row
-- id=4, status='promoted' → 'closed', processed_outcome='graduation_candidate'
INSERT INTO learning_candidates_v2 (
    id, title, description, level, category,
    flagged_by, flagged_at, session_id,
    status, processed_outcome, resolved_at, resolution,
    owner, max_days_captured, created_at
)
SELECT
    id, title, description, level, category,
    flagged_by, flagged_at, session_id,
    'closed',                           -- was: promoted
    'graduation_candidate',             -- new field
    resolved_at, resolution,
    owner,
    max_days_pending,                   -- rename
    created_at
FROM learning_candidates;

-- Step 3: Drop old table
DROP TABLE learning_candidates;

-- Step 4: Rename
ALTER TABLE learning_candidates_v2 RENAME TO learning_candidates;
```

### 7.2 New field summary (confirmed from v02)

| New field | Type | Purpose |
|---|---|---|
| `processed_outcome` | TEXT CHECK(enum) | What action was taken — replaces `approved/rejected/promoted` terminal statuses |
| `processed_at` | TEXT | Timestamp of transition to `processed` |
| `learning_scope` | TEXT CHECK(enum) | Scope type: team, agent, governance, process, session, tooling, owner_interaction |
| `target_agent` | TEXT (nullable) | Agent slug when `learning_scope = 'agent'` |
| `triage_routing` | TEXT CHECK(enum) | Routing qualifier at triage: graduation_candidate, standard, urgent |

### 7.3 Removed and renamed fields

| Change | Old name | New name | Reason |
|---|---|---|---|
| Rename | `surfaced_at` | `triaged_at` | Aligns with new state name |
| Rename | `surfaced_session` | `triaged_session` | Aligns with new state name |
| Rename | `max_days_pending` | `max_days_captured` | Aligns with new state name |
| Removed (implicit) | `approved/rejected/promoted` status values | `processed_outcome` enum | Outcome separated from status |

### 7.4 `closure_reason` assessment (confirmed from v02)

Not needed. The `processed_outcome` enum plus the existing `resolution` free-text field is sufficient. Drop `closure_reason`.

---

## 8. Updated Impact Table

Items where the database verification changes the v02 assessment are marked **[v03 update]**.

### 8.1 GL-022 — no change from v02

Items 1–7 from v02 are confirmed. All GL-022 Section 3, 5, 6, and 7 rewrites remain Batch 1.

### 8.2 Write-List v05 — W-1 DDL — updated [v03 update]

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 8 | W-1 DDL `status` CHECK | `('pending','surfaced','approved','rejected','promoted')` | Yes | `('captured','triaged','processed','closed')` | **High** | Naming | 1 |
| 9 | W-1 DDL `status` DEFAULT | `DEFAULT 'pending'` | Yes | `DEFAULT 'captured'` | High | Naming | 1 |
| 10 | W-1 `surfaced_at` | `surfaced_at TEXT` | Yes | `triaged_at TEXT` | Low | Naming | 1 |
| 11 | W-1 `surfaced_session` | `surfaced_session INTEGER` | Yes | `triaged_session INTEGER` | Low | Naming | 1 |
| 12 | W-1 `max_days_pending` | `max_days_pending INTEGER` | Yes | `max_days_captured INTEGER` | Low | Naming | 1 |
| 13 | W-1 missing columns | No `processed_outcome`, `processed_at`, `learning_scope`, `target_agent`, `triage_routing` | Yes | Add all five | High | Behavioral | 1 |
| 13b [v03 update] | W-1 structure | Written as fresh `CREATE TABLE` | Yes — table already exists | Must be rewritten as migration script (create-copy-drop-rename pattern, see Section 7.1). Pre-check must detect existing table and migrate rather than abort. | **High** | Behavioral | 1 |

### 8.3 /close-session — Steps 1 and 1b — confirmed from v02

Items 14–17 confirmed. See v02 Section 8.3 and 8.4.

### 8.4 /close-session — Step 3b — confirmed from v02

Items 19–27 confirmed. See v02 Section 8.5.

### 8.5 /close-session — Steps 4 and 5 — confirmed from v02

Items 18, 28–29 deferred to Batch 3. See v02 Section 8.6 and 8.7.

### 8.6 GL-021 — confirmed from v02

Items 30–31 confirmed. Batch 2.

### 8.7 gl-index.md — confirmed from v02

Item 32 confirmed. Batch 1.

### 8.8 Larry AGENT.md — updated [v03 update]

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 33 | Kennisgraduatie block | `graduation_candidate` tag in `agent_learnings` | Yes | The `tags` column does not exist in the actual `agent_learnings` schema. The Kennisgraduatie mechanism is documented but unimplemented. After Batch 3: replace with LC-based escalation using `triage_routing = 'graduation_candidate'` | Medium | Both | 3 |
| 33b [v03 update] | Kennisgraduatie block | References `agent_learnings.tags` | Additional finding: this column does not exist. The block describes a non-functional mechanism. | No data is at risk but the documentation is incorrect. | Medium | Both | 3 |
| 34 | Database pointer | `agent_learnings — Specialist self-improvement notes` | Yes — after absorption | Remove or redirect in Batch 3 | Low | Naming | 3 |
| 35 | Boilerplate write list | "session_logs, agent_learnings, team_log..." | Yes — after absorption | Remove `agent_learnings` after Batch 3 | Low | Naming | 3 |

### 8.9 `agent_learnings` schema — new finding [v03 update]

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 36b [v03 update] | `agent_learnings` actual schema | No `tags` column, no `graduation_candidate` support | Yes — CLAUDE.md and Larry AGENT.md describe writing `tags = 'graduation_candidate'` to this table, but the column does not exist | Existing rows are unaffected (retrospective reflections). Going forward: new behavioral learnings should be written to `learning_candidates`, not `agent_learnings`. Existing rows are historical — no mandatory migration. | Medium | Behavioral | 3 |

### 8.10 All specialist AGENT.md files — confirmed from v02

Item 36 (14+ files, boilerplate agent_learnings reference). Batch 3.

### 8.11 CLAUDE.md — updated [v03 update]

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 37 | Session log rule line 67 | "write one row to `agent_learnings` and one row to `delegation_outcomes`" | Yes — after absorption | Remove agent_learnings write; delegation notes remain in `delegation_outcomes` | Medium | Behavioral | 3 |
| 37b [v03 update] | Same line | The `agent_learnings` write per delegation is described as mandatory | Finding: the `agent_learnings` schema uses `what_worked/what_to_improve` fields that do not map cleanly to per-delegation notes. The actual rows are session-level reflections, not per-delegation notes. The documented purpose and actual usage diverge. | Medium | Behavioral | 3 |
| 38 | Language rule line 322 | `agent_learnings` in table list | Yes — after absorption | Remove from list | Low | Naming | 3 |
| 39 | Teamgroei section line 526 | "Log naar `agent_learnings` in de domein-database" | Yes — after absorption | Replace with "Register as Learning Candidate in `learning_candidates`" | High | Behavioral | 3 |

### 8.12 No change required — confirmed

Same as v02 Section 8.14. Includes: Iris AGENT.md, GL-020, SOP-019 footer, CLAUDE.md informal references, all archived deliverables.

---

## 9. Updated Batch Plan

The safest path is three batches, with Batch 3 deferred pending resolution of two technical-behavioral design questions.

### Batch 1 — Model definition + migration

**Scope:** Updated GL-022 definition, DDL migration of `learning_candidates`, gl-index update.

**Key update from v02:** Batch 1 now includes a live table migration, not just document changes and a fresh CREATE. The 1 existing row must be migrated correctly. Pre-check logic must detect the existing table and execute the migration path, not the creation path.

**Files:**
- GL-022 — Section 3, 5, 6, 7 rewrite
- Write-List W-1 DDL — replace CREATE script with migration script
- gl-index.md — GL-022 entry description update

**Nature:** Naming + behavioral (new fields) + DDL migration.
**Governance gate:** CAT-3 required.
**Data at risk:** 1 row in `learning_candidates`. Migration maps `promoted` → `closed` with `processed_outcome = 'graduation_candidate'`. No data loss.
**Affected file count:** 3 (plus the live database)
**Dependency:** None — this is the foundation.

### Batch 2 — Technical alignment

**Scope:** /close-session Steps 1 and 3b SQL alignment, GL-021 description update.

**No change from v02.** Items 14–17, 19–27, 30–31.

**Dependency:** Batch 1 must be complete.
**Governance gate:** CAT-3 required.
**Data at risk:** None — SQL query changes only.
**Affected file count:** 3

### Batch 3 — Consolidation and behavioral cleanup (deferred)

**Deferred pending Q1 and Q2 (see Section 10).**

**Files in scope:**
- CLAUDE.md (items 37–39)
- Larry AGENT.md (items 33–35)
- 14+ specialist AGENT.md files (item 36)
- /close-session Steps 4 and 5 (items 18, 28–29)
- SOP-009 (item 40)

**Additional v03 finding:** The `agent_learnings` existing rows (56 total across databases) are historical session reflections. No retroactive migration into `learning_candidates` is required. Going forward, new behavioral observations should go directly to `learning_candidates`.

**Nature:** Behavioral and naming. Broadest change set.
**Governance gate:** CAT-3 per file. Consider grouping the 14+ AGENT.md updates as a single bulk proposal.
**Affected file count:** 20+

---

## 10. Open Design Questions

Only questions that remain genuinely open after Owner clarification.

### Q1 — team_log dual-write (Batch 3 blocker)

The `team_log` table exists with 90 rows in team-knowledge.db and is actively used. When an LC is processed with `processed_outcome = 'team_learning'`:

**Option A:** `learning_candidates` is the sole store. Step 4 of /close-session is redesigned to write `team_log` only for operational events that are not learnings (procedural changes, infrastructure events, session markers).

**Option B:** Both: `learning_candidates` record is the SSOT; a `team_log` row is also created as a lightweight reference with a link back to the LC `id`. Step 4 writes both records.

**Option C:** `team_log` continues exactly as-is. The LC system and `team_log` operate as parallel records: the LC is governed, the `team_log` entry is operational context. No behavioral change to Step 4.

The answer determines how Step 4 is rewritten and whether the team_log write behavior changes.

### Q2 — agent_learnings going forward (Batch 3 blocker)

Given the verified finding that `agent_learnings` is a session-level reflection table (what_worked/what_to_improve) with 56 live rows and no `tags` column:

**Option A:** Deprecate `agent_learnings` for new writes. All new behavioral observations go to `learning_candidates`. Existing rows stay as historical records. Remove the mandatory write from CLAUDE.md and AGENT.md files.

**Option B:** Retain `agent_learnings` as a session-level retrospective table alongside `learning_candidates`. The two tables serve different purposes: `agent_learnings` = session quality reflection (unstructured, no Owner approval needed); `learning_candidates` = behavioral change register (structured, Owner approval required). CLAUDE.md is updated to distinguish the two.

**Option C:** Migrate existing rows selectively — only `what_to_improve` entries describing structural behavioral changes become LCs; operational notes stay or are discarded. Then retire the table.

---

## 11. Recommendation for Next Step After v03

V03 is the complete, verified read-only assessment. The Owner's conceptual model is confirmed. Database findings are now accurate.

**Recommended sequence:**

1. **Owner answers Q1 and Q2.** These are the only remaining decisions before Batch 3 can be fully specified. Batches 1 and 2 do not depend on them.

2. **Prepare Batch 1 write-list.** Fully specifiable now. Key difference from the original Write-List v05: the W-1 script must be a migration (create-copy-drop-rename), not a fresh CREATE. The existing 1-row table must be handled.

3. **Run Batch 1 through governance** (SOP-019 CP-1 through CP-4).

4. **After Batch 1:** Prepare and run Batch 2.

5. **After Q1 and Q2 are answered:** Prepare Batch 3 write-list.

---

## 12. V02 Correction Summary

| V02 statement | Correct state |
|---|---|
| "all four domain databases exist as files but contain no tables" | Incorrect. All four databases have tables and live data. |
| "`team-knowledge.db` has no tables" | Incorrect. Has 7 tables including `learning_candidates` (1 row), `session_logs` (174 rows), `team_log` (90 rows), `agent_learnings` (40 rows). |
| "`personal.db` has no tables" | Incorrect. Has 14 tables including `journal` (65 rows), `session_logs` (59 rows), `agent_learnings` (7 rows). |
| "`kamer-ecommerce.db` has no tables" | Incorrect. Has 5 tables including `session_logs` (9 rows), `agent_learnings` (9 rows). |
| "`geldstroom-regie.db` has no tables" | Incorrect. Has 5 tables including `session_logs` (11 rows). |
| "`learning_candidates` has not been created yet" | Incorrect. Table exists in `team-knowledge.db` with 1 live row using old schema. |
| "No data migration is required" | Partially incorrect. `learning_candidates` has 1 row requiring migration. Other tables are unaffected. |
| "`agent_learnings` has a `tags` field for graduation_candidate" | Incorrect. No `tags` column exists in the actual schema. The Kennisgraduatie mechanism is documented but unimplemented. |
| "The only CREATE TABLE statements in the codebase are in memory-db/init.sql" | Incorrect. All domain databases have live table structures. The source DDL for those tables is not in visible .sql files — they were created directly from scripts or session commands. |

---

## 13. Change Count Summary

| Batch | Items | Files + DB | Nature | Governance | Status |
|---|---|---|---|---|---|
| Batch 1 | 8 | 3 files + 1 DB migration | Naming + Behavioral + Migration | CAT-3 | Ready to specify |
| Batch 2 | 9 | 3 files | Naming + Behavioral | CAT-3 | Ready to specify (after Batch 1) |
| Batch 3 | 23+ | 20+ files | Naming + Behavioral | CAT-3 per file | Deferred — Q1 and Q2 |
| No change needed | 14 items | — | — | — | Confirmed |

**Total active conflicts: 40 items across 26 active files and 1 database.**
**Open design questions: 2 (technical-behavioral only).**
**No conceptual model questions remain open.**

---

Delivered on: 2026-06-07
Delivered at: /opt/myPKA/Deliverables/20260607_Core_LC Naming Alignment Impact Assessment/lc-naming-alignment-impact-assessment-v03.md
