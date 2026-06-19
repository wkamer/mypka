# LC Lifecycle Phase 1 Write-List v05

**Datum:** 2026-06-06
**Status:** Governance deliverable — persisted. Implementation not yet authorized.
**Grondslag:** GL-020 Risk 5 mitigation. Scoping voorstel + Iris-review Accept (2026-06-06).
**Versie:** v05 — final phase 1 write list after Owner corrections and scope decisions.

---

## Scope Fase 1

| Nr | Write | Type | Volgorde |
|---|---|---|---|
| W-1 | `learning_candidates` tabel aanmaken | DDL — team-knowledge.db | 1 |
| W-2 | GL-022 document schrijven | Nieuw bestand (.md) | 2 |
| W-3 | gl-index.md updaten | Edit (.md) | 3 |
| W-4 | Iris AGENT.md — optionele LC Flag | Edit (.md) | 4 |
| W-5 | /close-session — scan + write plan + sweep | Edit (.md) | 5 |

**Batch-stop:** Als W-1 pre-check 'ABORTED' → stop. W-2 t/m W-5 niet uitvoeren.

**Buiten scope Fase 1:**
- Persoonlijke routines (Morning Routine, Afternoon Routine, End-of-Day Routine) — voor Owner's leven, planning, reflectie en energie. Geen systeemonderhoud.
- Toekomstige system-maintenance sweep-uitbreidingen — vereisen aparte Owner-autorisatie na Fase 1.

**Governance-classificatie alle writes:** CAT-3 Governance Input. Level 3. Elk vereist expliciete Owner-autorisatie, individueel of als batched confirmation per GL-021 Section 7.

---

## W-1 — DDL: `learning_candidates`

**Doel:** Fundament van het tracking-systeem. Geen LC kan worden geregistreerd zolang de tabel niet bestaat.

**Locatie:** `Team Knowledge/team-knowledge.db`

**Exacte DDL:**

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
);
```

**Pre-check + Execute-commando:**

```bash
/opt/mypka-memory/venv/bin/python3 -c "
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='learning_candidates'\")
if cur.fetchone():
    conn.close()
    print('ABORTED: learning_candidates already exists — FULL BATCH STOPPED.')
else:
    conn.execute('''CREATE TABLE learning_candidates (
        id               INTEGER PRIMARY KEY AUTOINCREMENT,
        title            TEXT NOT NULL,
        description      TEXT,
        level            INTEGER NOT NULL CHECK(level = 2),
        category         TEXT,
        flagged_by       TEXT NOT NULL,
        flagged_at       TEXT NOT NULL DEFAULT (datetime(\'now\')),
        session_id       INTEGER REFERENCES session_logs(id),
        status           TEXT NOT NULL DEFAULT \'pending\'
                             CHECK(status IN (\'pending\',\'surfaced\',\'approved\',\'rejected\',\'promoted\')),
        surfaced_at      TEXT,
        surfaced_session INTEGER REFERENCES session_logs(id),
        resolved_at      TEXT,
        resolution       TEXT,
        owner            TEXT NOT NULL DEFAULT \'larry\',
        max_days_pending INTEGER NOT NULL DEFAULT 3,
        created_at       TEXT NOT NULL DEFAULT (datetime(\'now\'))
    )''')
    conn.commit()
    conn.close()
    print('OK: learning_candidates created')
"
```

**Batch-stop regel:** Bij output 'ABORTED' — stop. Voer W-2 t/m W-5 niet uit. Meld aan Owner: "Pre-check W-1: learning_candidates bestaat al — implementatiebatch gestopt."

**Post-check** (alleen bij pre-check 'OK'; bij 'ABORTED' → rapporteer 'SKIPPED'):

```bash
/opt/mypka-memory/venv/bin/python3 -c "
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
cur = conn.cursor()
cur.execute(\"SELECT name, sql FROM sqlite_master WHERE type='table' AND name='learning_candidates'\")
row = cur.fetchone()
conn.close()
if not row: print('FAIL: table not found')
elif 'CHECK(level = 2)' in (row[1] or ''): print('PASS')
else: print('WARN: schema differs — verify manually')
"
```

**Rollback:** `DROP TABLE learning_candidates;`

---

## W-2 — GL-022 Learning Candidate Lifecycle

**Doel:** Autoritative definitie van de LC lifecycle. Alle commands en AGENT.md updates refereren naar dit document.

**Locatie:** `Team Knowledge/Core/Guidelines/GL-022_Learning Candidate Lifecycle.md`

**Volledig bestandsinhoud:**

```markdown
# GL-022 — Learning Candidate Lifecycle

**Last reviewed:** 2026-06-06
**Status:** Active

---

## Section 1 — Purpose and Scope

This guideline governs the full lifecycle of Learning Candidates (LCs): behavioral observations
flagged by team members as potentially useful beyond the current session. It implements the
mitigation defined in GL-020 Section 8 Risk 5 (Level 2 Candidate Decay).

Cross-references: [[GL-020_Intent Classification Taxonomy]] Section 5 and Section 8 Risk 5,
[[GL-021_Owner Interaction Rule and Write Authorization Boundary]] Section 7

---

## Section 2 — What Is a Learning Candidate?

A Learning Candidate exists when a team member encounters an observation during execution that:
1. Does not meet the Level 1 boundary criterion: a third party reading the team member's
   AGENT.md without session context could not have predicted this behavioral change, AND
2. Is not yet a confirmed structural change requiring SOP-019.

Level 1 learnings are autonomous — never registered as LCs.
Level 2 learnings are registered in `learning_candidates` and tracked per this guideline.
The `level` field is always 2. Level 3 learnings trigger SOP-019 immediately and are never
entered as new records in `learning_candidates`.

A Level 2 record may be escalated by Owner decision: status set to `promoted`, SOP-019
triggered by Larry. The `level` field remains 2 as origin documentation.

---

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

---

## Section 4 — Who Flags, Who Owns

Any team member may flag a Level 2 candidate. The flagging threshold is intentionally low.

**Standard flagging fields:**
1. `title` — one sentence
2. `description` — what was observed and why it qualifies as a candidate
3. `category` — GL-020 CAT that produced the observation (CAT-1 through CAT-6)

**Exception — Iris:** Iris flags with title and category only. The review output in which
the LC Flag appears serves as the implicit description. Larry records the description during
registration, drawing from the review context. Iris does not provide a separate description
field.

Ownership transfers immediately to Larry upon flagging.
Larry is the sole owner of all LCs after flagging.

---

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

---

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

---

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

---

## Section 8 — Roles

| Role | Responsibility |
|---|---|
| **Larry** | Sole owner after flagging. Registers (including description reconstruction for Iris-flagged LCs). Sweeps at /close-session. Surfaces to Owner. Updates status after Owner decision. |
| **Iris** | Flags with title + category only via optional LC Flag line. Review context is implicit description. Ownership transfers to Larry immediately. Does not register. |
| **Responsible team member** | Flags with three fields. No further action after flagging. Applies approved Level 2 behavior autonomously after Owner approval. |
| **Nolan** | Updates AGENT.md files when a promoted Level 3 LC produces structural changes. Receives brief from Larry after Owner approval. |
| **Kai** | Available for database implementation or maintenance when assigned. |

---

## Section 9 — Future Extension

Phase 1 sweep point is /close-session only.

A future governance-maintenance or system-maintenance flow may add additional LC sweep
points — for example, a weekly system-health command that surfaces aged candidates without
requiring a full /close-session. This extension:

- Is explicitly outside the scope of personal routines (Morning, Afternoon, End-of-Day)
- Requires separate Owner authorization before implementation
- Would be designed as a standalone governance command, not embedded in personal workflows
- Will reference this GL and extend Section 5 when authorized

No action is taken on this extension until the Owner explicitly initiates the design flow.

---

## Section 10 — Changelog

| Date | Change | By | Approval |
|---|---|---|---|
| 2026-06-06 | Initial creation. LC lifecycle, status states, ownership rule, surfacing rules (Phase 1: /close-session only), decay prevention, pre-authorization scope, roles, Future Extension note. Iris exception in Section 4: title + category only, review context as implicit description. Implements GL-020 Section 8 Risk 5 mitigation. Iris-reviewed and accepted. | Larry | Owner |
```

**Post-check:** `test -f "/opt/myPKA/Team Knowledge/Core/Guidelines/GL-022_Learning Candidate Lifecycle.md" && echo PASS || echo FAIL`

**Rollback:** Bestand verwijderen + W-3 rollback.

---

## W-3 — gl-index.md

**Doel:** GL-022 registreren in de authoritative index.

**Locatie:** `Team Knowledge/Core/Guidelines/gl-index.md`

**Tekst vóór:**

```
| GL-021 | [[GL-021_Owner Interaction Rule and Write Authorization Boundary]] | Owner answers only yes/no/correction; every write requires explicit Owner confirmation; Iris review vs Owner authorization distinction; pre-authorized CAT-1 writes; /close-session batched confirmation protocol |
```

**Tekst na:**

```
| GL-021 | [[GL-021_Owner Interaction Rule and Write Authorization Boundary]] | Owner answers only yes/no/correction; every write requires explicit Owner confirmation; Iris review vs Owner authorization distinction; pre-authorized CAT-1 writes; /close-session batched confirmation protocol |
| GL-022 | [[GL-022_Learning Candidate Lifecycle]] | LC lifecycle: status states, ownership rule, surfacing via /close-session (Phase 1), decay prevention, pre-authorization scope for operational LC writes |
```

**Post-check:** `grep -c "GL-022" "/opt/myPKA/Team Knowledge/Core/Guidelines/gl-index.md"` — verwacht: `1`

**Rollback:** GL-022-regel verwijderen uit gl-index.md.

---

## W-4 — Iris AGENT.md

**Doel:** Iris in staat stellen om LC's te markeren vanuit governance reviews via een optionele vijfde outputregel.

**Locatie:** `/opt/myPKA/Team/Iris - The Governance Gatekeeper/AGENT.md`

**Tekst vóór:**

```
In multi-phase governance flows (scoping → implementation, review → execution): the exact next prompt must explicitly name which phase the Owner is approving. Scoping approval and write authorization are always stated as two separate decisions. A prompt that conflates approving the proposal with authorizing the writes is incomplete and must be corrected before Iris presents it to the Owner.

**Example output shape:**
```

**Tekst na:**

```
In multi-phase governance flows (scoping → implementation, review → execution): the exact next prompt must explicitly name which phase the Owner is approving. Scoping approval and write authorization are always stated as two separate decisions. A prompt that conflates approving the proposal with authorizing the writes is incomplete and must be corrected before Iris presents it to the Owner.

**Optional — LC Flag (when applicable)**
When Iris's review identifies an observation that may qualify as a Learning Candidate per [[GL-022_Learning Candidate Lifecycle]] — an observation useful beyond the current session, not derivable from the responsible agent's current AGENT.md without session context — Iris appends one line after the four required elements:

`LC Flag: [one-sentence title] — [GL-020 category]`

This is the only permitted addition to the default output format. No explanation, no description. The review context itself serves as the implicit description. Ownership transfers to Larry immediately upon flagging. Iris does not register the LC.

**Example output shape:**
```

**Changelog-toevoeging (onderdeel van dezelfde write):**

```
| 2026-06-06 | LC-Iris-003 — optional LC Flag line added to Default Output Format per GL-022. Iris flags with title + category only; review context is implicit description; ownership to Larry immediately. | Larry | Owner |
```

**Post-check — twee afzonderlijke checks:**

```bash
grep -c "Optional — LC Flag" "/opt/myPKA/Team/Iris - The Governance Gatekeeper/AGENT.md"
# Verwacht: 1

grep -c "LC-Iris-003" "/opt/myPKA/Team/Iris - The Governance Gatekeeper/AGENT.md"
# Verwacht: 1
```

**Rollback:** Nieuwe paragraaf + changelog-entry verwijderen.

---

## W-5 — /close-session (drie wijzigingen)

**Doel:** LC-scan aan voorbereidingsfase toevoegen, write plan uitbreiden, Step 3b sweep toevoegen.

**Locatie:** `/opt/myPKA/.claude/commands/close-session.md`

---

### Wijziging 5a — Scan toevoegen aan Step 1

**Tekst vóór:**

```
If a session_log already exists for today with the same title: add a suffix to `session_title`, e.g., "(2)". The script detects duplicates automatically on exact title.
```

**Tekst na (exacte bestandsinhoud):**

````
If a session_log already exists for today with the same title: add a suffix to `session_title`, e.g., "(2)". The script detects duplicates automatically on exact title.

Also scan `learning_candidates` in `team-knowledge.db` for overdue rows and note the count:

```python
# Interpreter: /opt/mypka-memory/venv/bin/python
import sqlite3
db = '/opt/myPKA/Team Knowledge/team-knowledge.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
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

Use these counts in Step 1b.
````

---

### Wijziging 5b — Write plan tabel uitbreiden

**Tekst vóór:**

```
| Graduation candidates: [X proposed / none] | team_tasks row per candidate (if applicable) |
```

**Tekst na:**

```
| Graduation candidates: [X proposed / none] | team_tasks row per candidate (if applicable) |
| LC status updates: [X overdue / none] | learning_candidates status → 'surfaced' in team-knowledge.db (if applicable) |
```

---

### Wijziging 5c — Nieuwe Step 3b toevoegen

**Tekst vóór:**

```
## Step 4 — Team learning (optional)
```

**Tekst na (exacte bestandsinhoud):**

````
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
```

Show surfaced LCs to the Owner. For each one, wait for the Owner's decision: approve / reject / promote.

**Authorization rule:** The Owner's decision statement per LC ("approve LC-{id}", "reject LC-{id}",
"promote LC-{id}") is itself the authorization for the follow-up UPDATE per GL-022 Section 7.
No separate "yes" is required. Execute immediately after each Owner statement.

```python
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
```

For `promote`: after executing the UPDATE, Larry immediately triggers SOP-019 for the promoted LC.

If LC overdue count = 0: skip silently.

---

## Step 4 — Team learning (optional)
````

**Post-check:**

```bash
grep -c "Step 3b" /opt/myPKA/.claude/commands/close-session.md          # Verwacht: 1
grep -c "LC status updates" /opt/myPKA/.claude/commands/close-session.md # Verwacht: 1
```

**Rollback:** Drie tekstblokken terugdraaien naar originele tekst.

---

## Implementatievolgorde Fase 1

| Stap | Write | Afhankelijkheid |
|---|---|---|
| 1 | W-1 DDL tabel aanmaken | Geen — foundation |
| 2 | W-2 GL-022 schrijven | Geen — foundation |
| 3 | W-3 gl-index.md | Na W-2 |
| 4 | W-4 Iris AGENT.md | Na W-2 |
| 5 | W-5 /close-session | Na W-1 + W-2 |

W-3, W-4, W-5 zijn onderling onafhankelijk. Ze kunnen na W-1 en W-2 in één batched confirmation worden uitgevoerd.

---

Delivered on: 2026-06-06
Delivered at: Learning Candidate Lifecycle and Risk 5 Tracking governance flow — end of v05 write-list iteration.
