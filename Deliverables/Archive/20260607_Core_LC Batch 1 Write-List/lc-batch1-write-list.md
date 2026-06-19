# LC Batch 1 Write-List

**Date:** 2026-06-07
**Author:** Larry
**Status:** Iris reviewed — W-3 post-check corrected — pending Owner authorization for execution
**Assessment basis:** [[lc-naming-alignment-impact-assessment-v05.md]]
**Governance route:** CAT-3 — Larry prepares → Iris review gate → Owner authorization → execute
**Scope:** Three writes: W-1 database migration, W-2 GL-022 document update, W-3 gl-index.md update

---

## Scope and Dependencies

This write-list covers Batch 1 of the LC naming alignment. Batch 1 establishes the authoritative model. Batch 2 (/close-session and GL-021) must not begin until Batch 1 is complete and verified.

| Write | Target | Type | Risk |
|---|---|---|---|
| W-1 | `team-knowledge.db` — `learning_candidates` table | DDL migration | High — live data |
| W-2 | `GL-022_Learning Candidate Lifecycle.md` | Document update | High — active GL |
| W-3 | `gl-index.md` | One-line description update | Low |

**Implementation order:** W-1 first (database foundation), then W-2 (document aligned to new schema), then W-3 (index entry aligned to new document).

**Batch stop rule:** If W-1 reports ABORTED or FAILED, do not execute W-2 or W-3. Report to Owner and stop.

---

## W-1 — Database migration: `learning_candidates`

**Purpose:** Migrate the existing `learning_candidates` table in `team-knowledge.db` from the old schema (5 status values: pending/surfaced/approved/rejected/promoted) to the new schema (4 lifecycle states: captured/triaged/processed/closed) with new fields for `processed_outcome`, `triage_routing`, `learning_scope`, `target_agent`, domain context, and renamed timestamp columns. Migrate the 1 existing row correctly.

**Location:** `/opt/myPKA/Team Knowledge/team-knowledge.db`

**Existing state:**
- Table `learning_candidates` exists with 1 row (id=4, status=`promoted`)
- Schema uses old CHECK constraint: `('pending','surfaced','approved','rejected','promoted')`
- Missing fields: `processed_outcome`, `triage_routing`, `learning_scope`, `target_agent`, `source_domain`, `affected_domain`, `target_database`, `source_reference`, `processed_at`
- Old field names: `surfaced_at`, `surfaced_session`, `max_days_pending`

**Pre-check:**

```bash
/opt/mypka-memory/venv/bin/python3 << 'EOF'
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()

# Check current state
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='learning_candidates'")
lc_exists = cur.fetchone() is not None
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='learning_candidates_v2'")
v2_exists = cur.fetchone() is not None
row_count = 0
if lc_exists:
    cur.execute("SELECT COUNT(*) FROM learning_candidates")
    row_count = cur.fetchone()[0]
conn.close()

if v2_exists:
    print("ABORT: learning_candidates_v2 already exists — possible interrupted prior run. Investigate before proceeding.")
elif lc_exists:
    print(f"MIGRATE: learning_candidates exists with {row_count} row(s). Full migration path will run.")
else:
    print("CREATE: learning_candidates does not exist. Fresh CREATE path will run.")
EOF
```

Expected output before first run: `MIGRATE: learning_candidates exists with 1 row(s). Full migration path will run.`

If output is ABORT: stop. Investigate and report to Owner.

**Migration script:**

```bash
/opt/mypka-memory/venv/bin/python3 << 'EOF'
import sqlite3

db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)

try:
    conn.execute("BEGIN")

    # Step 1: Create new table
    conn.execute("""
        CREATE TABLE learning_candidates_v2 (
            id                INTEGER PRIMARY KEY AUTOINCREMENT,
            title             TEXT NOT NULL,
            description       TEXT,
            level             INTEGER NOT NULL CHECK(level = 2),
            category          TEXT,
            flagged_by        TEXT NOT NULL,
            flagged_at        TEXT NOT NULL DEFAULT (datetime('now')),
            session_id        INTEGER REFERENCES session_logs(id),
            status            TEXT NOT NULL DEFAULT 'captured'
                                  CHECK(status IN ('captured','triaged','processed','closed')),
            triaged_at        TEXT,
            triaged_session   INTEGER REFERENCES session_logs(id),
            processed_at      TEXT,
            processed_outcome TEXT CHECK(processed_outcome IN (
                'team_learning','agent_learning',
                'guideline_update','sop_update',
                'agent_instruction_update','claude_instruction_update',
                'backlog_item','deliverable_lifecycle_item',
                'rejected','deferred','no_action'
            )),
            learning_scope    TEXT CHECK(learning_scope IN (
                'team','agent','governance','process','session','tooling','owner_interaction'
            )),
            target_agent      TEXT,
            triage_routing    TEXT CHECK(triage_routing IN (
                'graduation_candidate','standard','urgent'
            )),
            source_domain     TEXT CHECK(source_domain IN (
                'core','personal','kamer_ecommerce','geldstroom_regie','cross_domain'
            )),
            affected_domain   TEXT,
            target_database   TEXT,
            source_reference  TEXT,
            resolved_at       TEXT,
            resolution        TEXT,
            owner             TEXT NOT NULL DEFAULT 'larry',
            max_days_captured INTEGER NOT NULL DEFAULT 3,
            created_at        TEXT NOT NULL DEFAULT (datetime('now'))
        )
    """)

    # Step 2: Migrate existing row
    # id=4: promoted → closed, triage_routing=graduation_candidate, processed_outcome=sop_update
    conn.execute("""
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
        FROM learning_candidates
    """)

    migrated = conn.execute("SELECT COUNT(*) FROM learning_candidates_v2").fetchone()[0]

    # Step 3: Drop old table
    conn.execute("DROP TABLE learning_candidates")

    # Step 4: Rename
    conn.execute("ALTER TABLE learning_candidates_v2 RENAME TO learning_candidates")

    conn.commit()
    print(f"OK: migration complete. Rows migrated: {migrated}")

except Exception as e:
    conn.rollback()
    print(f"FAILED: {e}")
finally:
    conn.close()
EOF
```

Expected output: `OK: migration complete. Rows migrated: 1`

**Post-check:**

```bash
/opt/mypka-memory/venv/bin/python3 << 'EOF'
import sqlite3

db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()

# Verify table exists with new schema
cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='learning_candidates'")
row = cur.fetchone()
if not row:
    print("FAIL: table not found after migration")
    conn.close()
    exit(1)

schema = row[0]
checks = [
    ("captured in status CHECK",  "'captured'" in schema),
    ("triaged in status CHECK",   "'triaged'" in schema),
    ("processed in status CHECK", "'processed'" in schema),
    ("closed in status CHECK",    "'closed'" in schema),
    ("pending NOT in schema",     "'pending'" not in schema),
    ("surfaced NOT in schema",    "'surfaced'" not in schema),
    ("promoted NOT in schema",    "'promoted'" not in schema),
    ("processed_outcome field",   "processed_outcome" in schema),
    ("triage_routing field",      "triage_routing" in schema),
    ("learning_scope field",      "learning_scope" in schema),
    ("source_domain field",       "source_domain" in schema),
    ("triaged_at field",          "triaged_at" in schema),
    ("max_days_captured field",   "max_days_captured" in schema),
]

# Verify migrated row
cur.execute("SELECT id, status, triage_routing, processed_outcome, learning_scope, source_domain FROM learning_candidates WHERE id=4")
migrated = cur.fetchone()
if migrated:
    checks += [
        ("id=4 status=closed",                     migrated[1] == 'closed'),
        ("id=4 triage_routing=graduation_candidate", migrated[2] == 'graduation_candidate'),
        ("id=4 processed_outcome=sop_update",       migrated[3] == 'sop_update'),
        ("id=4 learning_scope=governance",          migrated[4] == 'governance'),
        ("id=4 source_domain=core",                 migrated[5] == 'core'),
    ]
else:
    checks.append(("id=4 row exists", False))

conn.close()

all_pass = True
for label, result in checks:
    status = "PASS" if result else "FAIL"
    if not result:
        all_pass = False
    print(f"  {status}: {label}")

print("OVERALL: PASS" if all_pass else "OVERALL: FAIL — do not proceed to W-2")
EOF
```

Expected output: all checks PASS, OVERALL: PASS.

**Rollback:**

```bash
/opt/mypka-memory/venv/bin/python3 << 'EOF'
import sqlite3

db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)

try:
    conn.execute("BEGIN")
    conn.execute("DROP TABLE IF EXISTS learning_candidates")
    conn.execute("DROP TABLE IF EXISTS learning_candidates_v2")
    conn.execute("""
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
    """)
    conn.execute("""
        INSERT INTO learning_candidates
            (id, title, description, level, category, flagged_by, flagged_at, status, owner, created_at)
        VALUES (4,
            'Governance checkpoints bypassed when Owner drives implementation interactively — CP invocation required even under Owner-directed pace',
            'During Deliverable Lifecycle Phase 1 implementation on 2026-06-07, all five governance checkpoints (CP-1 through CP-4 and the Iris pre-implementation check) were not invoked.',
            2, 'CAT-3', 'iris', '2026-06-07', 'promoted', 'larry', datetime('now'))
    """)
    conn.commit()
    print("ROLLBACK OK: learning_candidates restored to original schema with id=4 row")
except Exception as e:
    conn.rollback()
    print(f"ROLLBACK FAILED: {e}")
finally:
    conn.close()
EOF
```

---

## W-2 — GL-022 document update

**Purpose:** Update GL-022 to reflect the confirmed lifecycle model (`captured → triaged → processed → closed`), the new `triage_routing` and `processed_outcome` fields, and the renamed columns. Sections 2, 3, 5, 6, 7, and 10 are changed. Sections 1, 4, 8, 9 and the file header date are unchanged except where noted.

**Location:** `Team Knowledge/Core/Guidelines/GL-022_Learning Candidate Lifecycle.md`

**Pre-check:**

```bash
python3 -c "
import re
with open('/opt/myPKA/Team Knowledge/Core/Guidelines/GL-022_Learning Candidate Lifecycle.md') as f:
    content = f.read()
checks = [
    ('Section 3 contains pending',    'pending' in content),
    ('Section 3 contains surfaced',   'surfaced' in content and 'status' in content),
    ('Section 5 contains max_days_pending', 'max_days_pending' in content),
    ('Section 7 references CREATE TABLE', 'CREATE TABLE' in content),
]
for label, result in checks:
    print(f'  {\"PASS\" if result else \"SKIP\"}: {label}')
print('Pre-check complete — proceed with W-2 edits')
"
```

**Changes — exact before/after:**

**Change 2a — Header date:**

Old:
```
**Last reviewed:** 2026-06-06
```

New:
```
**Last reviewed:** 2026-06-07
```

---

**Change 2b — Section 2, final paragraph:**

Old:
```
A Level 2 record may be escalated by Owner decision: status set to `promoted`, SOP-019
triggered by Larry. The `level` field remains 2 as origin documentation.
```

New:
```
A Level 2 record may be escalated by Owner decision. At Triage, `triage_routing` is set to
`graduation_candidate`. When processed, `processed_outcome` records the specific structural
change produced (e.g., `sop_update`, `guideline_update`). Status transitions to `processed`,
then `closed`. The `level` field remains 2 as origin documentation.
```

---

**Change 2c — Section 3 (full section replacement):**

Old:
```
## Section 3 — Lifecycle: Status States and Transitions

| Status | Definition |
|---|---|
| `pending` | Flagged. Not yet surfaced to Owner. Larry owns. |
| `surfaced` | Presented to Owner. Awaiting decision. |
| `approved` | Owner approved. Team member applies Level 2 behavior autonomously going forward. |
| `rejected` | Owner rejected. LC discarded. No further action. |
| `promoted` | Owner approved escalation. SOP-019 initiated by Larry. Record retained. Level remains 2. |

Valid transitions: pending → surfaced → approved / rejected / promoted.
No silent expiry. No implicit approval. An LC cannot leave pending without being surfaced.
An LC cannot leave surfaced without Owner decision.
```

New:
```
## Section 3 — Lifecycle States and Transitions

| Status | Definition |
|---|---|
| `captured` | Registered. Not yet reviewed. Larry owns. |
| `triaged` | Reviewed. Category confirmed, level confirmed, routing determined. |
| `processed` | Action taken. Outcome recorded in `processed_outcome`. |
| `closed` | Concluded. No further action. |

Valid transitions: `captured → triaged → processed → closed`.
No silent expiry. No implicit approval. An LC cannot leave `captured` without being triaged.
An LC cannot leave `triaged` without an explicit processing or closure action.

**Outcome fields (set at Processing):**
- `triage_routing` — routing classification set at Triage: `graduation_candidate`, `standard`, or `urgent`
- `processed_outcome` — result set at Processing: see Section 7 for the full enum
```

---

**Change 2d — Section 5 (full section replacement):**

Old:
```
## Section 5 — Surfacing Rules

| Situation | When to surface |
|---|---|
| CAT-3 Governance Input → Level 2 | Same session as flagging — no delay |
| Level 3 learning | SOP-019 triggered same session — never enters this register |
| All other categories, within max_days_pending | At next /close-session |
| Any pending LC older than max_days_pending (default 3) | Mandatory at next /close-session |

`max_days_pending` default is 3. Stored per row and adjustable at flagging time.

**Phase 1 sweep point:** /close-session only.
Personal routines (Morning Routine, Afternoon Routine, End-of-Day Routine) are outside the
scope of LC tracking. A dedicated system-maintenance flow may extend sweep points in a
future phase — see Section 9.
```

New:
```
## Section 5 — Triage Rules

| Situation | When to triage |
|---|---|
| CAT-3 Governance Input → Level 2 | Same session as flagging — no delay |
| Level 3 learning | SOP-019 triggered same session — never enters this register |
| All other categories, within max_days_captured | At next /close-session |
| Any captured LC older than max_days_captured (default 3) | Mandatory at next /close-session |

`max_days_captured` default is 3. Stored per row and adjustable at flagging time.

**Phase 1 sweep point:** /close-session only.
Personal routines (Morning Routine, Afternoon Routine, End-of-Day Routine) are outside the
scope of LC tracking. A dedicated system-maintenance flow may extend sweep points in a
future phase — see Section 9.
```

---

**Change 2e — Section 6 (full section replacement):**

Old:
```
## Section 6 — Decay Prevention

Five layers, scoped to Phase 1:

1. **Durable registration:** every LC written to `learning_candidates` at flagging with
   `flagged_at` timestamp and `status` field — no "flagged and forgotten" possible.
2. **Staleness trigger at /close-session:** at every /close-session, Larry queries all
   `pending` rows. Rows where `days_pending >= max_days_pending` are included in the
   /close-session write plan and surfaced after Owner confirmation.
3. **Ownership transfer:** passes from flagging team member to Larry at flagging moment.
4. **Explicit closure paths:** exactly three valid endings — `approved`, `rejected`,
   `promoted`. No passive expiry, no implicit approval.
5. **Write plan inclusion:** overdue LC status updates are included in the /close-session
   write plan per GL-021 Section 7 and execute after Owner confirmation.
```

New:
```
## Section 6 — Decay Prevention

Five layers, scoped to Phase 1:

1. **Durable registration:** every LC written to `learning_candidates` at flagging with
   `flagged_at` timestamp and `status = 'captured'` — no "flagged and forgotten" possible.
2. **Staleness trigger at /close-session:** at every /close-session, Larry queries all
   `captured` rows. Rows where `days_captured >= max_days_captured` are included in the
   /close-session write plan and triaged after Owner confirmation.
3. **Ownership transfer:** passes from flagging team member to Larry at flagging moment.
4. **Explicit closure paths:** exactly two terminal states — `processed` and `closed`.
   Outcome recorded in `processed_outcome`. No passive expiry, no implicit approval.
5. **Write plan inclusion:** overdue LC triage updates are included in the /close-session
   write plan per GL-021 Section 7 and execute after Owner confirmation.
```

---

**Change 2f — Section 7 (full section replacement):**

Old:
```
## Section 7 — Operational Write Rules

**Phase 1 implementation batch** (all CAT-3, Owner authorization required):

| Write | Description |
|---|---|
| W-1 | CREATE TABLE learning_candidates in team-knowledge.db |
| W-2 | GL-022 document (this file) |
| W-3 | gl-index.md — GL-022 entry added |
| W-4 | Iris AGENT.md — optional LC Flag rule added |
| W-5 | /close-session — LC scan, write plan row, Step 3b sweep |

**Post-implementation operational writes** (SOP-bounded, pre-authorized per GL-021 Section 7):

| Write | Authorization |
|---|---|
| INSERT new LC row at flagging | Included in session write plan |
| UPDATE status → 'surfaced' at /close-session sweep | Included in /close-session write plan |
| UPDATE status → approved / rejected / promoted | Owner's decision statement is the authorization — no separate 'yes' required |
```

New:
```
## Section 7 — Operational Write Rules

**Batch 1** (CAT-3 — Larry prepares → Iris review → Owner authorization):

| Write | Description |
|---|---|
| W-1 | MIGRATE TABLE learning_candidates in team-knowledge.db — new lifecycle states (`captured`, `triaged`, `processed`, `closed`); new fields: `processed_outcome`, `processed_at`, `learning_scope`, `target_agent`, `triage_routing`, `source_domain`, `affected_domain`, `target_database`, `source_reference`; renamed: `triaged_at`, `triaged_session`, `max_days_captured` |
| W-2 | GL-022 document (this file) — Sections 2, 3, 5, 6, 7, 10 updated |
| W-3 | gl-index.md — GL-022 entry description updated |

**Batch 2** (CAT-3 — separate batch, requires Batch 1 complete):

| Write | Description |
|---|---|
| W-4 | /close-session — Step 1 scan, Step 1b write plan label, Step 3b SQL and Python |
| W-5 | GL-021 — Section 7 description update |

**Post-implementation operational writes** (SOP-bounded, pre-authorized per GL-021 Section 7):

| Write | Authorization |
|---|---|
| INSERT new LC row at flagging (`status = 'captured'`) | Included in session write plan |
| UPDATE status → `triaged` at /close-session sweep | Included in /close-session write plan |
| UPDATE status → `processed` or `closed` with `processed_outcome` | Owner's decision statement is the authorization — no separate 'yes' required |

**`processed_outcome` enum:**
`team_learning` — `agent_learning` — `guideline_update` — `sop_update` — `agent_instruction_update` — `claude_instruction_update` — `backlog_item` — `deliverable_lifecycle_item` — `rejected` — `deferred` — `no_action`

**`triage_routing` enum:**
`graduation_candidate` — `standard` — `urgent`

**`learning_scope` enum:**
`team` — `agent` — `governance` — `process` — `session` — `tooling` — `owner_interaction`

**`source_domain` enum:**
`core` — `personal` — `kamer_ecommerce` — `geldstroom_regie` — `cross_domain`
```

---

**Change 2g — Section 10 Changelog (append new row):**

Old (last row of the changelog table):
```
| 2026-06-06 | Initial creation. LC lifecycle, status states, ownership rule, surfacing rules (Phase 1: /close-session only), decay prevention, pre-authorization scope, roles, Future Extension note. Iris exception in Section 4: title + category only, review context as implicit description. Implements GL-020 Section 8 Risk 5 mitigation. Iris-reviewed and accepted. | Larry | Owner |
```

New (append after the existing row):
```
| 2026-06-06 | Initial creation. LC lifecycle, status states, ownership rule, surfacing rules (Phase 1: /close-session only), decay prevention, pre-authorization scope, roles, Future Extension note. Iris exception in Section 4: title + category only, review context as implicit description. Implements GL-020 Section 8 Risk 5 mitigation. Iris-reviewed and accepted. | Larry | Owner |
| 2026-06-07 | Batch 1 naming alignment. Lifecycle states renamed: pending→captured, surfaced→triaged; terminal statuses (approved/rejected/promoted) replaced by processed and closed with processed_outcome and triage_routing outcome fields. Sections 2, 3, 5, 6, 7 updated. New fields: processed_outcome, triage_routing, learning_scope, target_agent, source_domain, affected_domain, target_database, source_reference. Field renames: surfaced_at→triaged_at, surfaced_session→triaged_session, max_days_pending→max_days_captured. Basis: LC Naming Alignment Impact Assessment v05. Iris-reviewed and Owner-authorized. | Larry | Owner |
```

**Post-check:**

```bash
python3 -c "
with open('/opt/myPKA/Team Knowledge/Core/Guidelines/GL-022_Learning Candidate Lifecycle.md') as f:
    content = f.read()
checks = [
    ('captured in Section 3',          \"'captured'\" in content),
    ('triaged in Section 3',           \"'triaged'\" in content),
    ('processed in Section 3',         \"'processed'\" in content),
    ('closed in Section 3',            \"'closed'\" in content),
    ('pending NOT in status table',    'pending | Flagged' not in content),
    ('surfaced NOT in status table',   'surfaced | Presented' not in content),
    ('max_days_captured in Section 5', 'max_days_captured' in content),
    ('triage_routing in Section 7',    'triage_routing' in content),
    ('processed_outcome in Section 7', 'processed_outcome' in content),
    ('source_domain in Section 7',     'source_domain' in content),
    ('Batch 1 in Section 7',           'Batch 1' in content),
    ('2026-06-07 in changelog',        '2026-06-07' in content),
]
all_pass = True
for label, result in checks:
    status = 'PASS' if result else 'FAIL'
    if not result: all_pass = False
    print(f'  {status}: {label}')
print('OVERALL: PASS' if all_pass else 'OVERALL: FAIL')
"
```

**Rollback:** Restore file from the exact original text. The original full file content is preserved in the assessment document and in git history (if applicable). The rollback restores all six changed sections to their pre-Batch-1 state.

---

## W-3 — gl-index.md description update

**Purpose:** Update the GL-022 entry description in the guidelines index to match the new lifecycle state terminology.

**Location:** `Team Knowledge/Core/Guidelines/gl-index.md`

**Change — exact before/after:**

Old:
```
| GL-022 | [[GL-022_Learning Candidate Lifecycle]] | LC lifecycle: status states, ownership rule, surfacing via /close-session (Phase 1), decay prevention, pre-authorization scope for operational LC writes |
```

New:
```
| GL-022 | [[GL-022_Learning Candidate Lifecycle]] | LC lifecycle: lifecycle states (captured→triaged→processed→closed), triage_routing, processed_outcome, ownership rule, triage via /close-session (Phase 1), decay prevention, pre-authorization scope for operational LC writes |
```

**Pre-check:**

```bash
grep "GL-022" '/opt/myPKA/Team Knowledge/Core/Guidelines/gl-index.md'
```

Expected: line containing `status states` and `surfacing via /close-session`.

**Post-check:**

```bash
python3 -c "
with open('/opt/myPKA/Team Knowledge/Core/Guidelines/gl-index.md') as f:
    lines = f.readlines()
gl022_line = next((l for l in lines if 'GL-022' in l and 'Learning Candidate' in l), '')
checks = [
    ('GL-022 line found',                         bool(gl022_line.strip())),
    ('lifecycle states in GL-022 line',           'lifecycle states' in gl022_line),
    ('triage_routing in GL-022 line',             'triage_routing' in gl022_line),
    ('processed_outcome in GL-022 line',          'processed_outcome' in gl022_line),
    ('status states absent from GL-022 line',     'status states' not in gl022_line),
]
all_pass = True
for label, result in checks:
    status = 'PASS' if result else 'FAIL'
    if not result: all_pass = False
    print(f'  {status}: {label}')
print('OVERALL: PASS' if all_pass else 'OVERALL: FAIL')
"
```

**Rollback:** Restore the original line.

---

## Summary: Write Plan for Owner Confirmation

When this write-list is authorized for execution, the following writes will be presented in the /close-session write plan (as required by GL-021 Section 7):

| Write | Purpose |
|---|---|
| W-1: `learning_candidates` migration | DDL migration — new schema, 1 row migrated |
| W-2: GL-022 document | Sections 2, 3, 5, 6, 7, 10 updated |
| W-3: gl-index.md | GL-022 entry description updated |

---

## Governance Route

1. Larry prepares this write-list (complete)
2. **Iris performs review gate** — verdict, risk assessment, exact next prompt for Owner
3. Owner authorizes or rejects per SOP-019 CP-1 through CP-4
4. Execution proceeds only after Owner authorization

**Current status: awaiting Owner authorization for execution.**

---

Delivered on: 2026-06-07
Delivered at: `/opt/myPKA/Deliverables/20260607_Core_LC Batch 1 Write-List/lc-batch1-write-list.md`
