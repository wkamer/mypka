# LC Batch 2 Write-List

**Date:** 2026-06-07
**Author:** Larry
**Status:** Pending Iris review — not yet authorized for execution
**Assessment basis:** [[lc-naming-alignment-impact-assessment-v05.md]]
**Dependency:** Batch 1 complete and verified (confirmed 2026-06-07)
**Governance route:** CAT-3 — Larry prepares → Iris review gate → Owner authorization → execute

---

## Scope and Dependencies

Batch 2 aligns the operational implementation (/close-session skill) to the model established in Batch 1. GL-021 was also listed in scope, but upon reading the actual file, the specific old LC status value text referenced in the impact assessment was found in GL-022 Section 7 (not GL-021), and was already corrected in Batch 1 W-2. See W-5 finding below.

| Write | Target | Type | Risk |
|---|---|---|---|
| W-4 | `.claude/commands/close-session.md` | Three targeted edits | Medium — active skill |
| W-5 | GL-021 | Finding: no change required | Low |

**Implementation order:** W-4 only (three edits within the same file, applied in document order). W-5 is a documented finding.

**Batch stop rule:** If any W-4 sub-edit fails or produces unexpected output, stop and report before continuing.

---

## W-4 — /close-session skill update

**Purpose:** Align the three LC-related sections of /close-session to the new schema: Step 1 LC scan (status values and column names), Step 1b write plan label, and Step 3b LC sweep (SQL, Python logic, decision verbs, and resolve_lc function).

**Location:** `/opt/myPKA/.claude/commands/close-session.md`

**Pre-check:**

```bash
python3 -c "
with open('/opt/myPKA/.claude/commands/close-session.md') as f:
    content = f.read()
checks = [
    ('Step 1 uses pending status',      \"status = 'pending'\" in content),
    ('Step 1 uses max_days_pending',    'max_days_pending' in content),
    ('Step 1b uses LC status updates',  'LC status updates' in content),
    ('Step 3b uses surfaced status',    \"status = 'surfaced'\" in content),
    ('Step 3b uses surfaced_at',        'surfaced_at' in content),
    ('resolve_lc has approve key',      \"'approve'\" in content),
    ('resolve_lc has promote key',      \"'promote'\" in content),
]
all_present = True
for label, result in checks:
    print(f'  {\"PASS\" if result else \"SKIP\"}: {label}')
    if not result: all_present = False
print('Pre-check complete' if all_present else 'WARNING: some expected old text not found — verify before proceeding')
"
```

---

### W-4a — Step 1 LC scan: status values, column name, print label

**Change — exact before/after:**

Old:
```python
cur.execute("""
    SELECT COUNT(*) FROM learning_candidates
    WHERE status = 'pending'
    AND CAST(julianday('now') - julianday(flagged_at) AS INTEGER) >= max_days_pending
""")
overdue = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM learning_candidates WHERE status = 'pending'")
total = cur.fetchone()[0]
conn.close()
print(f"LC pending: {total}, LC overdue: {overdue}")
```

New:
```python
cur.execute("""
    SELECT COUNT(*) FROM learning_candidates
    WHERE status = 'captured'
    AND CAST(julianday('now') - julianday(flagged_at) AS INTEGER) >= max_days_captured
""")
overdue = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM learning_candidates WHERE status = 'captured'")
total = cur.fetchone()[0]
conn.close()
print(f"Learning Candidates captured: {total}, Learning Candidates overdue_for_triage: {overdue}")
```

---

### W-4b — Step 1b write plan: LC row label

**Change — exact before/after:**

Old:
```
| LC status updates: [X overdue / none] | learning_candidates status → 'surfaced' in team-knowledge.db (if applicable) |
```

New:
```
| LC triage updates: [X overdue_for_triage / none] | learning_candidates status → 'triaged' in team-knowledge.db (if applicable) |
```

---

### W-4c — Step 3b full section replacement

**Change — full section before/after:**

Old (entire Step 3b section):
```markdown
## Step 3b — Learning Candidate sweep

If LC overdue count from Step 1 > 0, execute the surfacing UPDATE:

```python
# Interpreter: /opt/mypka-memory/venv/bin/python
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("""
    UPDATE learning_candidates
    SET status = 'surfaced', surfaced_at = datetime('now')
    WHERE status = 'pending'
    AND CAST(julianday('now') - julianday(flagged_at) AS INTEGER) >= max_days_pending
""")
updated = cur.rowcount
conn.commit()
cur.execute("""
    SELECT id, title, level, category, flagged_by,
           CAST(julianday('now') - julianday(flagged_at) AS INTEGER) AS days_pending
    FROM learning_candidates
    WHERE status = 'surfaced' AND date(surfaced_at) = date('now')
    ORDER BY flagged_at ASC
""")
rows = cur.fetchall()
conn.close()
print(f"LC surfaced: {updated}")
for r in rows:
    print(f"  LC-{r[0]} | {r[1]} | L{r[2]} | cat:{r[3]} | by {r[4]} | {r[5]}d pending")
` ` `

Show surfaced LCs to the Owner. For each one, wait for the Owner's decision: approve / reject / promote.

**Authorization rule:** The Owner's decision statement per LC ("approve LC-{id}", "reject LC-{id}",
"promote LC-{id}") is itself the authorization for the follow-up UPDATE per GL-022 Section 7.
No separate "yes" is required. Execute immediately after each Owner statement.

` ` `python
# Interpreter: /opt/mypka-memory/venv/bin/python
import sqlite3

def resolve_lc(lc_id, decision):
    resolutions = {
        'approve': ('approved', 'Owner approved — Level 2 behavior applied autonomously going forward.'),
        'reject':  ('rejected', 'Owner rejected — discarded.'),
        'promote': ('promoted', 'Owner approved escalation to Level 3 — SOP-019 initiated by Larry.'),
    }
    status, resolution = resolutions[decision]
    db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
    conn = sqlite3.connect(db)
    conn.execute(
        "UPDATE learning_candidates SET status=?, resolved_at=datetime('now'), resolution=? WHERE id=?",
        (status, resolution, lc_id)
    )
    conn.commit()
    conn.close()
    print(f"LC-{lc_id} → {status}")

# Replace id and decision per Owner statement — one call per LC:
# resolve_lc(1, 'approve')
# resolve_lc(2, 'reject')
# resolve_lc(3, 'promote')
` ` `

For `promote`: after executing the UPDATE, Larry immediately triggers SOP-019 for the promoted LC.

If LC overdue count = 0: skip silently.
```

New (entire Step 3b section):
```markdown
## Step 3b — Learning Candidate sweep

If LC overdue count from Step 1 > 0, execute the triage UPDATE:

```python
# Interpreter: /opt/mypka-memory/venv/bin/python
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("""
    UPDATE learning_candidates
    SET status = 'triaged', triaged_at = datetime('now')
    WHERE status = 'captured'
    AND CAST(julianday('now') - julianday(flagged_at) AS INTEGER) >= max_days_captured
""")
updated = cur.rowcount
conn.commit()
cur.execute("""
    SELECT id, title, level, category, flagged_by,
           CAST(julianday('now') - julianday(flagged_at) AS INTEGER) AS days_captured
    FROM learning_candidates
    WHERE status = 'triaged' AND date(triaged_at) = date('now')
    ORDER BY flagged_at ASC
""")
rows = cur.fetchall()
conn.close()
print(f"Learning Candidates triaged: {updated}")
for r in rows:
    print(f"  LC-{r[0]} | {r[1]} | L{r[2]} | cat:{r[3]} | by {r[4]} | {r[5]}d captured")
` ` `

Show triaged LCs to the Owner. For each one, wait for the Owner's decision: apply / reject / escalate.

**Authorization rule:** The Owner's decision statement per LC ("apply LC-{id}", "reject LC-{id}",
"escalate LC-{id}") is itself the authorization for the follow-up UPDATE per GL-022 Section 7.
No separate "yes" is required. Execute immediately after each Owner statement.

` ` `python
# Interpreter: /opt/mypka-memory/venv/bin/python
import sqlite3

def resolve_lc(lc_id, decision):
    db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT learning_scope FROM learning_candidates WHERE id=?", (lc_id,))
    row = cur.fetchone()
    scope = row[0] if row else None

    if decision == 'apply':
        outcome = 'agent_learning' if scope == 'agent' else 'team_learning'
        conn.execute(
            """UPDATE learning_candidates
               SET status='processed', processed_at=datetime('now'),
                   processed_outcome=?, resolved_at=datetime('now'),
                   resolution='Owner approved — behavior applied going forward.'
               WHERE id=?""",
            (outcome, lc_id)
        )
    elif decision == 'reject':
        conn.execute(
            """UPDATE learning_candidates
               SET status='closed', resolved_at=datetime('now'),
                   processed_outcome='rejected',
                   resolution='Owner rejected — discarded.'
               WHERE id=?""",
            (lc_id,)
        )
    elif decision == 'escalate':
        # triage_routing marks this LC for structural escalation.
        # Status stays 'triaged' — must not move to processed until SOP-019
        # completes and processed_outcome is known.
        conn.execute(
            """UPDATE learning_candidates
               SET triage_routing='graduation_candidate',
                   resolution='Owner approved escalation — SOP-019 initiated by Larry.'
               WHERE id=?""",
            (lc_id,)
        )
    conn.commit()
    conn.close()
    print(f"LC-{lc_id} → {decision}")

# Replace id and decision per Owner statement — one call per LC:
# resolve_lc(1, 'apply')
# resolve_lc(2, 'reject')
# resolve_lc(3, 'escalate')
` ` `

For `escalate`: after executing the UPDATE, Larry immediately triggers SOP-019 for the escalated LC. Status remains `triaged` — the LC stays open. Only after SOP-019 completes does Larry record the outcome: set `processed_outcome` to the specific result (`sop_update`, `guideline_update`, `agent_instruction_update`, `claude_instruction_update`, `backlog_item`, `rejected`, `deferred`, or `no_action`), then move status to `processed`, then to `closed`. The LC must not move to `processed` without a valid `processed_outcome`.

If LC overdue count = 0: skip silently.
```

---

**W-4 Post-check:**

```bash
python3 -c "
import re
with open('/opt/myPKA/.claude/commands/close-session.md') as f:
    content = f.read()

# General checks
checks = [
    ('Step 1 uses captured status',              \"status = 'captured'\" in content),
    ('Step 1 uses max_days_captured',            'max_days_captured' in content),
    ('Step 1 print uses overdue_for_triage',     'overdue_for_triage' in content),
    ('Step 1 print uses Learning Candidates',    'Learning Candidates captured' in content),
    ('Step 1b uses LC triage updates',           'LC triage updates' in content),
    ('Step 3b uses triaged status in UPDATE',    \"status = 'triaged'\" in content),
    ('Step 3b uses triaged_at',                  'triaged_at' in content),
    ('Step 3b uses days_captured',               'days_captured' in content),
    ('Step 3b print uses triaged',               'Learning Candidates triaged' in content),
    ('resolve_lc has apply key',                 \"'apply'\" in content),
    ('resolve_lc has escalate key',              \"'escalate'\" in content),
    ('resolve_lc has processed_outcome field',   'processed_outcome' in content),
    ('old pending NOT in Step 1 SQL',            \"status = 'pending'\" not in content),
    ('old surfaced NOT in Step 3b SQL',          \"status = 'surfaced'\" not in content),
    ('old approve key NOT in resolve_lc',        \"'approve':\" not in content),
    ('old promote key NOT in resolve_lc',        \"'promote':\" not in content),
]

# Targeted escalate branch checks
escalate_m = re.search(r\"elif decision == 'escalate':(.*?)(?=elif decision|# Replace id|conn\\.commit\\(\\))\", content, re.DOTALL)
if escalate_m:
    eb = escalate_m.group(1)
    checks += [
        (\"escalate sets triage_routing=graduation_candidate\", \"triage_routing='graduation_candidate'\" in eb),
        (\"escalate does NOT set status=processed\",            \"status='processed'\" not in eb),
        (\"escalate does NOT set processed_at\",               \"processed_at\" not in eb),
    ]
else:
    checks.append((\"escalate branch found in resolve_lc\", False))

all_pass = True
for label, result in checks:
    s = 'PASS' if result else 'FAIL'
    if not result: all_pass = False
    print(f'  {s}: {label}')
print('OVERALL: PASS' if all_pass else 'OVERALL: FAIL')
"
```

**W-4 Rollback:** Restore the three changed sections to their pre-Batch-2 state. The original text is preserved verbatim in this write-list under the "Old" sections above.

---

## W-5 — GL-021 update: finding

**Finding:** Upon reading the actual GL-021 file, the text "UPDATE status → 'surfaced'" and "UPDATE status → approved / rejected / promoted" referenced in impact assessment items 30–31 does not exist in GL-021. These strings were located in GL-022 Section 7 ("Post-implementation operational writes" table), which was corrected in Batch 1 W-2 Change 2f.

GL-021 Section 7 contains only general rules about pre-authorized writes (Rules 1–5), with no specific mention of LC status values. The LC-related implementation tracker entries in GL-021 (lines 156–158: LC-Iris-001, LC-Owner-001, LC-CloseSession-001) do not reference old status values and do not require updating.

**Action:** No change to GL-021 required in Batch 2. Impact assessment items 30–31 were incorrectly attributed. The intended correction was already applied as part of W-2 in Batch 1.

**W-5 status:** No write action. Finding documented.

---

## Summary: Write Plan for Owner Confirmation

When this write-list is authorized for execution:

| Write | Purpose |
|---|---|
| W-4a | /close-session Step 1 SQL: `pending` → `captured`, `max_days_pending` → `max_days_captured`, print label updated |
| W-4b | /close-session Step 1b: write plan row label updated |
| W-4c | /close-session Step 3b: SQL, Python, decision verbs, resolve_lc function fully aligned to new schema |
| W-5 | No change — finding documented |

---

## Governance Route

1. Larry prepares this write-list (complete)
2. **Iris performs review gate** — verdict, risk assessment, exact next prompt for Owner
3. Owner authorizes or rejects per SOP-019 CP-1 through CP-4
4. Execution proceeds only after Owner authorization

**Current status: awaiting Iris review.**

---

Delivered on: 2026-06-07
Delivered at: `Deliverables/20260607_Core_LC Batch 2 Write-List/lc-batch2-write-list.md`
