# LC Triage Write-Plan v02

**Date:** 2026-06-07
**Author:** Larry
**Version:** v02
**Supersedes:** `lc-triage-write-plan.md` (v01)
**Status:** Pending Owner confirmation — not yet executed
**Scope:** Triage of registered LC id=5; registration and triage of two unregistered Iris-flagged candidates
**Database:** `team-knowledge.db` — `learning_candidates` table
**Lifecycle basis:** GL-022 — captured → triaged → processed → closed

**Changes vs v01:**
- Post-check: query scoped to exactly the three intended LCs (id=5, Candidate A, Candidate B) — no longer selects all `status = 'triaged'` rows
- Post-check: print statement corrected — `scope={r[6]}, domain={r[7]}` (was `scope={r[7]}, domain={r[7]}`)
- Post-check: status check corrected — `r[2] == 'triaged'` (was `r[1] == 'triaged' or r[2] == 'triaged'`, where r[1] is title)
- Post-check: added per-candidate scope and domain checks (Candidate A: governance/core; Candidate B: tooling/core)
- Post-check: added row-count assertion (exactly 3)
- Open Items section added

---

## Purpose

Three Learning Candidates require lifecycle progression in this session:

| # | LC | Current state | Target state |
|---|---|---|---|
| 1 | id=5 — Verification script fragility in governance post-checks | `captured` | `triaged` |
| 2 | Candidate A — Batch-stop rules not inherited by executing agent brief | Not yet registered | `captured` → `triaged` |
| 3 | Candidate B — Post-check regex assumes branch order | Not yet registered | `captured` → `triaged` |

All three are CAT-3. GL-022 Section 5 rule: CAT-3 → Level 2 → triage same session as flagging.

`processed_outcome` is not set in this write round. It is set only after the Owner issues a decision (apply / reject / escalate) per LC.

---

## Pre-check

Verifies current state before any writes execute.

```python
/opt/mypka-memory/venv/bin/python3 << 'EOF'
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()

# LC id=5 must be 'captured'
cur.execute("SELECT id, status, triage_routing FROM learning_candidates WHERE id=5")
row = cur.fetchone()
if not row:
    print("ABORT: LC id=5 not found")
elif row[1] != 'captured':
    print(f"ABORT: LC id=5 has status='{row[1]}', expected 'captured'")
else:
    print(f"PASS: LC id=5 status=captured, triage_routing={row[2]}")

# Candidate A must not already exist (title check)
cur.execute("""
    SELECT id FROM learning_candidates
    WHERE title LIKE '%Batch-stop rules%'
""")
if cur.fetchone():
    print("WARN: Candidate A may already be registered — verify before proceeding")
else:
    print("PASS: Candidate A not yet registered")

# Candidate B must not already exist (title check)
cur.execute("""
    SELECT id FROM learning_candidates
    WHERE title LIKE '%regex assumes branch order%'
""")
if cur.fetchone():
    print("WARN: Candidate B may already be registered — verify before proceeding")
else:
    print("PASS: Candidate B not yet registered")

conn.close()
EOF
```

Expected output: three PASS lines. On any ABORT or WARN: stop and report before executing.

---

## Write steps

All five steps execute inside a single transaction. On any exception: full rollback.

```python
/opt/mypka-memory/venv/bin/python3 << 'EOF'
import sqlite3

db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)

try:
    conn.execute("BEGIN")

    # Step 1: Triage LC id=5
    conn.execute("""
        UPDATE learning_candidates
        SET status         = 'triaged',
            triage_routing = 'standard',
            triaged_at     = datetime('now')
        WHERE id = 5
          AND status = 'captured'
    """)
    affected = conn.execute("SELECT changes()").fetchone()[0]
    if affected != 1:
        raise RuntimeError(f"Step 1 failed: expected 1 row updated, got {affected}")
    print("Step 1 OK: LC id=5 → triaged, triage_routing=standard")

    # Step 2: Register Candidate A as captured
    conn.execute("""
        INSERT INTO learning_candidates
            (title, description, level, category,
             flagged_by, flagged_at,
             status, learning_scope, source_domain,
             owner, max_days_captured, created_at)
        VALUES (
            'Batch-stop rules declared in write-lists are not automatically inherited by the executing agent brief',
            'During LC Batch 2 write-list reviews, Iris flagged that batch-stop rules are documented in the write-list but are not automatically included in the execution brief presented to the executor. If the executor does not read the full write-list, batch-stop rules are silently absent from the execution context. Larry must explicitly include batch-stop rules in every execution brief rather than relying on the executor to derive them from the write-list.',
            2, 'CAT-3',
            'iris', datetime('now'),
            'captured', 'governance', 'core',
            'larry', 3, datetime('now')
        )
    """)
    id_a = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"Step 2 OK: Candidate A registered as id={id_a}, status=captured")

    # Step 3: Triage Candidate A — CAT-3 same-session rule
    conn.execute("""
        UPDATE learning_candidates
        SET status         = 'triaged',
            triage_routing = 'standard',
            triaged_at     = datetime('now')
        WHERE id = ?
          AND status = 'captured'
    """, (id_a,))
    affected = conn.execute("SELECT changes()").fetchone()[0]
    if affected != 1:
        raise RuntimeError(f"Step 3 failed: expected 1 row updated, got {affected}")
    print(f"Step 3 OK: Candidate A id={id_a} → triaged, triage_routing=standard")

    # Step 4: Register Candidate B as captured
    conn.execute("""
        INSERT INTO learning_candidates
            (title, description, level, category,
             flagged_by, flagged_at,
             status, learning_scope, source_domain,
             owner, max_days_captured, created_at)
        VALUES (
            'Post-check regex assumes branch order in resolve_lc — silent False negatives if order differs',
            'During Batch 2 write-list v04 review, Iris flagged that the post-check regex for the reject branch uses re.search(r"elif decision == ''reject'':(.*?)elif decision == ''escalate''"), which assumes reject precedes escalate in the function body. If the branch order differs in the written file, the reject branch checks report False negatives silently, meaning a malformed reject path passes post-check undetected. Post-check scripts must not assume code structure order; use explicit named-group matching or extract the target function text before applying branch checks.',
            2, 'CAT-3',
            'iris', datetime('now'),
            'captured', 'tooling', 'core',
            'larry', 3, datetime('now')
        )
    """)
    id_b = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"Step 4 OK: Candidate B registered as id={id_b}, status=captured")

    # Step 5: Triage Candidate B — CAT-3 same-session rule
    conn.execute("""
        UPDATE learning_candidates
        SET status         = 'triaged',
            triage_routing = 'standard',
            triaged_at     = datetime('now')
        WHERE id = ?
          AND status = 'captured'
    """, (id_b,))
    affected = conn.execute("SELECT changes()").fetchone()[0]
    if affected != 1:
        raise RuntimeError(f"Step 5 failed: expected 1 row updated, got {affected}")
    print(f"Step 5 OK: Candidate B id={id_b} → triaged, triage_routing=standard")

    conn.commit()
    print(f"\nALL STEPS COMPLETE — ids: LC5, A={id_a}, B={id_b}")

except Exception as e:
    conn.rollback()
    print(f"\nFAILED — full rollback executed: {e}")
finally:
    conn.close()
EOF
```

---

## Post-check

Verifies final state of exactly the three intended LCs after writes.

Query is scoped to id=5 and the two candidates by title match — not a broad `WHERE status = 'triaged'`.

```python
/opt/mypka-memory/venv/bin/python3 << 'EOF'
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()

cur.execute("""
    SELECT id, title, status, triage_routing, triaged_at,
           processed_outcome, learning_scope, source_domain
    FROM learning_candidates
    WHERE id = 5
       OR title LIKE '%Batch-stop rules%'
       OR title LIKE '%regex assumes branch order%'
    ORDER BY id
""")
rows = cur.fetchall()
conn.close()

checks = []

# Exactly 3 rows — no more, no less
checks.append(("exactly 3 rows returned", len(rows) == 3))
print(f"Rows found: {len(rows)}")

for r in rows:
    id_, title, status, triage_routing, triaged_at, processed_outcome, learning_scope, source_domain = r
    print(f"\n  id={id_}: status={status}, triage_routing={triage_routing}, triaged_at={triaged_at}, processed_outcome={processed_outcome}")
    print(f"    scope={learning_scope}, domain={source_domain}")

    checks.append((f"id={id_} status=triaged",            status == 'triaged'))
    checks.append((f"id={id_} triage_routing=standard",   triage_routing == 'standard'))
    checks.append((f"id={id_} triaged_at set",            triaged_at is not None))
    checks.append((f"id={id_} processed_outcome is NULL", processed_outcome is None))

    # Candidate A: governance / core
    if 'Batch-stop' in title:
        checks.append((f"id={id_} (Candidate A) learning_scope=governance", learning_scope == 'governance'))
        checks.append((f"id={id_} (Candidate A) source_domain=core",        source_domain == 'core'))

    # Candidate B: tooling / core
    if 'regex assumes branch order' in title:
        checks.append((f"id={id_} (Candidate B) learning_scope=tooling", learning_scope == 'tooling'))
        checks.append((f"id={id_} (Candidate B) source_domain=core",     source_domain == 'core'))

# id=5 must be present in results
checks.append(("id=5 present in results", any(r[0] == 5 for r in rows)))

print()
all_pass = True
for label, result in checks:
    s = 'PASS' if result else 'FAIL'
    if not result:
        all_pass = False
    print(f"  {s}: {label}")
print("\nOVERALL: PASS" if all_pass else "\nOVERALL: FAIL")
EOF
```

Expected: exactly 3 rows, all `status = 'triaged'`, `triage_routing = 'standard'`, `triaged_at` set, `processed_outcome = NULL`. Candidate A: `learning_scope = 'governance'`, `source_domain = 'core'`. Candidate B: `learning_scope = 'tooling'`, `source_domain = 'core'`.

---

## Rollback / recovery

The transaction wraps all five steps. On any exception, `conn.rollback()` fires and no partial state is written.

Manual rollback if needed after commit:

```python
/opt/mypka-memory/venv/bin/python3 << 'EOF'
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
try:
    conn.execute("BEGIN")
    # Revert LC id=5 to captured
    conn.execute("""
        UPDATE learning_candidates
        SET status='captured', triage_routing=NULL, triaged_at=NULL
        WHERE id=5
    """)
    # Remove Candidate A and B (delete rows where title matches)
    conn.execute("""
        DELETE FROM learning_candidates
        WHERE title LIKE '%Batch-stop rules%'
           OR title LIKE '%regex assumes branch order%'
    """)
    conn.commit()
    print("ROLLBACK OK")
except Exception as e:
    conn.rollback()
    print(f"ROLLBACK FAILED: {e}")
finally:
    conn.close()
EOF
```

---

## After writes — Owner decisions

Once all three LCs are `triaged`, they are presented to the Owner:

| id | title | triage_routing | Awaiting decision |
|---|---|---|---|
| 5 | Verification script fragility in governance post-checks | standard | apply / reject / escalate |
| A | Batch-stop rules not inherited by executing agent brief | standard | apply / reject / escalate |
| B | Post-check regex assumes branch order | standard | apply / reject / escalate |

The Owner's decision statement per LC is the authorization for the follow-up UPDATE per GL-022 Section 7:
- `apply LC-{id}` → `status = 'processed'`, `processed_outcome = 'team_learning'` (or `agent_learning`)
- `reject LC-{id}` → `processed → closed`, `processed_outcome = 'rejected'`
- `escalate LC-{id}` → `triage_routing = 'graduation_candidate'`, status stays `triaged`, SOP-019 initiated

`processed_outcome` is not set until after the Owner decision.

---

## What this write-plan does NOT do

- Does not set `processed_outcome` at any point
- Does not move any LC to `processed` or `closed`
- Does not start Batch 3
- Does not modify GL files, /close-session, or any AGENT.md

---

## Open items — not actioned in this write-plan

These items are preserved for later Owner decision. No action is taken on them now.

**OI-1: Deliverable Lifecycle reliability**
File creation, versioning, persisted Iris review artifacts, and silent overwrite prevention must be improved. The current flow does not guarantee that Iris review outputs are persisted as artifacts, that version numbering is enforced, or that an existing file is never silently overwritten. To be addressed in a dedicated system-file change proposal.

**OI-2: Session-log naming consistency**
During the previous /close-session two similar files were created: one manual detailed closure log and one generated mirror. The naming relationship between them is not consistent. Do not rename either file now. Preserve as an open item for a future session-log naming convention review.

---

Delivered on: 2026-06-07
Delivered at: `Deliverables/20260607_Core_LC Triage Write-Plan/lc-triage-write-plan-v02.md`
