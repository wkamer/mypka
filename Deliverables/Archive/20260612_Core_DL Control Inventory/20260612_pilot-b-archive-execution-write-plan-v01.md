# Pilot B Archive Execution Write Plan — v01

**Date:** 2026-06-12
**Author:** Governance Assistant
**Status:** Awaiting Owner authorization
**Containment folder:** `Deliverables/20260612_Core_DL Control Inventory/`
**Execution Persistence Rule:** This write plan is required before Owner authorization.
A persisted execution report is required immediately after execution completes.

---

## 1. Current Assumption Verification

**Task brief assumption:** active D-folder count before Pilot B = 38

**Verification result:**

| Source | Count | Notes |
|---|---|---|
| `ls Deliverables/ \| grep -v Archive` | 40 | Includes INDEX.md and README.md — not D-folders |
| D-folders only (40 minus 2 files) | **38** | Matches assumption |
| `deliverable_lifecycle WHERE state_gl017 != 'archived'` | **38** | DB confirms |
| Pilot A execution report | 43 - 5 = 38 | Arithmetic confirms |

**Result:** Assumption confirmed. Active D-folder count before Pilot B = 38.
**Stop condition NOT triggered.** Planning proceeds.

---

## 2. Proposed Pilot B Folder List (5 folders)

All 5 selected from the `ready_for_archive` classification in the operating model
(`20260612_d-folder-operating-model-and-current-inventory-v01.md`).
No routing target. No domain knowledge content. No live governance references.

### Folder 1

| Field | Value |
|---|---|
| Folder name | `20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal` |
| Lifecycle id | 47 |
| Current state_gl017 | `pending_lifecycle_decision` |
| Current owner_decision | NULL |

**Why safe:** DLH Phase A discovery and proposal artifact. Phase B and Phase C both executed. Phase A is fully superseded. No live action items.

**Why no routing:** Pure process artifact. No domain knowledge requiring permanent storage.

**Why not registered_but_unclear:** Classified as `ready_for_archive` in operating model v01 (DLH Phase A/B group, item 3).

**Owner decision needed:** Yes — batch confirm via this write plan approval.

---

### Folder 2

| Field | Value |
|---|---|
| Folder name | `20260608_Core_Retention Assessment P2 P5 UMC` |
| Lifecycle id | 62 |
| Current state_gl017 | `active` |
| Current owner_decision | NULL |

**Why safe:** UMC Archive Eligibility chain assessment. Retention decision already made and executed. Chain closed.

**Why no routing:** Assessment artifact. No permanent domain knowledge content.

**Why not registered_but_unclear:** Classified as `ready_for_archive` in operating model v01 (UMC chain, item 10).

**Owner decision needed:** Yes — batch confirm via this write plan approval.

---

### Folder 3

| Field | Value |
|---|---|
| Folder name | `20260608_Core_UMC Archive Eligibility Chain Process Review` |
| Lifecycle id | 64 |
| Current state_gl017 | `active` |
| Current owner_decision | NULL |

**Why safe:** Paired process review artifact for the UMC Archive Eligibility chain. Chain complete. No dependency.

**Why no routing:** Process review artifact. No domain knowledge requiring routing.

**Why not registered_but_unclear:** Classified as `ready_for_archive` in operating model v01 (UMC chain, item 8).

**Owner decision needed:** Yes — batch confirm via this write plan approval.

---

### Folder 4

| Field | Value |
|---|---|
| Folder name | `20260608_Core_R1-R5 Prioritization Assessment` |
| Lifecycle id | 65 |
| Current state_gl017 | `active` |
| Current owner_decision | NULL |

**Why safe:** R1-R5 prioritization exercise is complete. No open items. No live dependency.

**Why no routing:** Assessment artifact. No permanent domain knowledge content.

**Why not registered_but_unclear:** Classified as `ready_for_archive` in operating model v01 (UMC chain, item 12).

**Owner decision needed:** Yes — batch confirm via this write plan approval.

---

### Folder 5

| Field | Value |
|---|---|
| Folder name | `20260608_Core_Phase 1 Proposal R1 R5 v01` |
| Lifecycle id | 66 |
| Current state_gl017 | `active` |
| Current owner_decision | NULL |

**Why safe:** v01 is explicitly superseded by v02 (`20260608_Core_Phase 1 Proposal R1 R5 v02`, id 68). v01 has no independent live value.

**Why no routing:** Proposal artifact superseded by v02. v02 remains active for its own disposition.

**Why not registered_but_unclear:** Classified as `ready_for_archive` in operating model v01 (UMC chain, item 13).

**Owner decision needed:** Yes — batch confirm via this write plan approval.

---

### Excluded from Pilot B — Rationale

| Folder | Reason for exclusion |
|---|---|
| `20260608_Core_Write Proposal GL-013 Additions P2 P5` (id 63) | Unresolved Owner decision: GL-013 additions confirmed implemented? This question is open per operating model v01 section 6, item 2. Excluded until confirmed. |
| `20260608_Core_GL-013 Reconciliation Analysis` (id 67) | Related to GL-013 chain. Same unresolved question applies. Excluded. |
| `20260608_Core_Phase 1 Proposal R1 R5 v02` (id 68) | Note: "confirm accepted." Status ambiguous. Excluded until Owner confirms. |
| `20260608_Core_UMC Archive Eligibility Analysis 20260530` (id 60) | Kept for next batch. UMC chain partial archive is acceptable; v01-v02 relationship (id 60 and id 64) can be handled separately. No exclusion-forcing reason, deferred by choice to keep batch focused. |
| `20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen` (id 61) | Deferred to next batch. No exclusion-forcing reason. Batch size limit reached. |
| All `registered_but_unclear` folders (16) | Excluded per selection rule. Frozen until Owner explicitly reviews each item. |
| All `owner_decision_needed` folders (11) | Excluded per selection rule. Require substantive Owner decision (route, park, or archive). |
| Domain knowledge folders items 17-21 | Excluded per task constraint: no Owner approval yet for this group. |
| `active_work` folders (2) | Excluded: containment folder (self-referential) and Graduation Candidate (explicitly retained). |

---

## 3. Preflight Checks

Run these checks immediately before each archive action. Do not proceed past a failed check.

### 3.1 Source folder exists in active Deliverables

For each folder in Pilot B, confirm physical presence:

```bash
ls "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal/"
ls "/opt/myPKA/Deliverables/20260608_Core_Retention Assessment P2 P5 UMC/"
ls "/opt/myPKA/Deliverables/20260608_Core_UMC Archive Eligibility Chain Process Review/"
ls "/opt/myPKA/Deliverables/20260608_Core_R1-R5 Prioritization Assessment/"
ls "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v01/"
```

Expected: each command returns file listing without error.
If any returns "No such file or directory": STOP. Report missing folder. Do not proceed.

### 3.2 Archive target does not already exist

```bash
ls "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_Retention Assessment P2 P5 UMC" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_UMC Archive Eligibility Chain Process Review" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_R1-R5 Prioritization Assessment" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_Phase 1 Proposal R1 R5 v01" 2>&1
```

Expected: each returns "No such file or directory."
If any returns a file listing: STOP. Collision detected. Report to Owner before continuing.

### 3.3 Lifecycle record exists and matches

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
ids = [47, 62, 64, 65, 66]
for id_ in ids:
    row = conn.execute(
        "SELECT id, artifact_name, state_gl017 FROM deliverable_lifecycle WHERE id = ?",
        (id_,)
    ).fetchone()
    print(f"{id_}: {row}")
conn.close()
```

Expected: each id returns exactly one row.
If any id returns None: STOP. Missing lifecycle record. Report before continuing.

### 3.4 No live SOP, GL, or CLAUDE.md references

Run a grep across all system files for each folder name before moving:

```bash
grep -r "Deliverable Lifecycle Hardening Discovery and Proposal" \
  /opt/myPKA/Team\ Knowledge/Core/Guidelines/ \
  /opt/myPKA/Team\ Knowledge/Core/SOPs/ \
  /opt/myPKA/CLAUDE.md 2>/dev/null

grep -r "Retention Assessment P2 P5 UMC" \
  /opt/myPKA/Team\ Knowledge/Core/Guidelines/ \
  /opt/myPKA/Team\ Knowledge/Core/SOPs/ \
  /opt/myPKA/CLAUDE.md 2>/dev/null

grep -r "UMC Archive Eligibility Chain Process Review" \
  /opt/myPKA/Team\ Knowledge/Core/Guidelines/ \
  /opt/myPKA/Team\ Knowledge/Core/SOPs/ \
  /opt/myPKA/CLAUDE.md 2>/dev/null

grep -r "R1-R5 Prioritization Assessment" \
  /opt/myPKA/Team\ Knowledge/Core/Guidelines/ \
  /opt/myPKA/Team\ Knowledge/Core/SOPs/ \
  /opt/myPKA/CLAUDE.md 2>/dev/null

grep -r "Phase 1 Proposal R1 R5 v01" \
  /opt/myPKA/Team\ Knowledge/Core/Guidelines/ \
  /opt/myPKA/Team\ Knowledge/Core/SOPs/ \
  /opt/myPKA/CLAUDE.md 2>/dev/null
```

Expected: no output (no references).
If any grep returns a match: STOP. Live reference found. Do not archive that folder. Report to Owner.

### 3.5 No open team_task references

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
keywords = [
    "Hardening Discovery",
    "Retention Assessment P2",
    "Eligibility Chain Process Review",
    "R1-R5 Prioritization",
    "Phase 1 Proposal R1 R5 v01"
]
for kw in keywords:
    rows = conn.execute(
        "SELECT id, title, status FROM team_tasks WHERE title LIKE ? AND status != 'completed'",
        (f'%{kw}%',)
    ).fetchall()
    print(f"'{kw}': {rows}")
conn.close()
```

Expected: each keyword returns empty list.
If any returns open tasks: STOP. Unresolved task dependency. Report before continuing.

### 3.6 Folder contents do not contain unresolved action/decision signals

Before moving each folder, confirm no open items inside the folder:

Scan each folder's files for the following patterns:
- `TODO`, `ACTION REQUIRED`, `OPEN:`, `DECISION NEEDED`, `PENDING:`

```bash
grep -ri "TODO\|ACTION REQUIRED\|OPEN:\|DECISION NEEDED\|PENDING:" \
  "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal/" 2>/dev/null

grep -ri "TODO\|ACTION REQUIRED\|OPEN:\|DECISION NEEDED\|PENDING:" \
  "/opt/myPKA/Deliverables/20260608_Core_Retention Assessment P2 P5 UMC/" 2>/dev/null

grep -ri "TODO\|ACTION REQUIRED\|OPEN:\|DECISION NEEDED\|PENDING:" \
  "/opt/myPKA/Deliverables/20260608_Core_UMC Archive Eligibility Chain Process Review/" 2>/dev/null

grep -ri "TODO\|ACTION REQUIRED\|OPEN:\|DECISION NEEDED\|PENDING:" \
  "/opt/myPKA/Deliverables/20260608_Core_R1-R5 Prioritization Assessment/" 2>/dev/null

grep -ri "TODO\|ACTION REQUIRED\|OPEN:\|DECISION NEEDED\|PENDING:" \
  "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v01/" 2>/dev/null
```

Expected: no output, or hits that are historical references in closed content (evaluate case by case).
If any hit looks like a live open item: STOP. Report to Owner.

### 3.7 Archive folder is writable

```bash
touch "/opt/myPKA/Deliverables/Archive/.writecheck" && \
  rm "/opt/myPKA/Deliverables/Archive/.writecheck" && \
  echo "Archive writable" || echo "Archive NOT writable — stop"
```

Expected: "Archive writable."
If not: STOP. Do not proceed until write permission is resolved.

---

## 4. Exact Physical Archive Actions

Execute one folder at a time. Run the post-step check after each move.
Stop immediately on any failure — do not continue to the next folder.

**Archive target base path:** `/opt/myPKA/Deliverables/Archive/`

### Step 1 — Folder 1 (id 47)

```bash
mv "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal" \
   "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal"
```

**Post-step check:**

```bash
# Source is gone:
ls "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal" 2>&1
# Archive target exists:
ls "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal/"
```

Expected: source returns "No such file or directory"; archive target lists files.
If either fails: STOP. Report before continuing.

---

### Step 2 — Folder 2 (id 62)

```bash
mv "/opt/myPKA/Deliverables/20260608_Core_Retention Assessment P2 P5 UMC" \
   "/opt/myPKA/Deliverables/Archive/20260608_Core_Retention Assessment P2 P5 UMC"
```

**Post-step check:**

```bash
ls "/opt/myPKA/Deliverables/20260608_Core_Retention Assessment P2 P5 UMC" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_Retention Assessment P2 P5 UMC/"
```

Expected: same pattern as Step 1. If either fails: STOP.

---

### Step 3 — Folder 3 (id 64)

```bash
mv "/opt/myPKA/Deliverables/20260608_Core_UMC Archive Eligibility Chain Process Review" \
   "/opt/myPKA/Deliverables/Archive/20260608_Core_UMC Archive Eligibility Chain Process Review"
```

**Post-step check:**

```bash
ls "/opt/myPKA/Deliverables/20260608_Core_UMC Archive Eligibility Chain Process Review" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_UMC Archive Eligibility Chain Process Review/"
```

Expected: same pattern as Step 1. If either fails: STOP.

---

### Step 4 — Folder 4 (id 65)

```bash
mv "/opt/myPKA/Deliverables/20260608_Core_R1-R5 Prioritization Assessment" \
   "/opt/myPKA/Deliverables/Archive/20260608_Core_R1-R5 Prioritization Assessment"
```

**Post-step check:**

```bash
ls "/opt/myPKA/Deliverables/20260608_Core_R1-R5 Prioritization Assessment" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_R1-R5 Prioritization Assessment/"
```

Expected: same pattern as Step 1. If either fails: STOP.

---

### Step 5 — Folder 5 (id 66)

```bash
mv "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v01" \
   "/opt/myPKA/Deliverables/Archive/20260608_Core_Phase 1 Proposal R1 R5 v01"
```

**Post-step check:**

```bash
ls "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v01" 2>&1
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_Phase 1 Proposal R1 R5 v01/"
```

Expected: same pattern as Step 1. If either fails: STOP.

---

## 5. Exact Lifecycle DB Update Plan

Execute after all 5 physical moves complete and post-step checks pass.
All 5 updates inside one transaction.

```python
import sqlite3
from datetime import datetime

conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')

try:
    conn.execute("BEGIN TRANSACTION")

    approved_ids = [47, 62, 64, 65, 66]
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    for id_ in approved_ids:
        result = conn.execute(
            """UPDATE deliverable_lifecycle
               SET state_gl017 = 'archived',
                   owner_decision = 'archive',
                   updated_at = ?
               WHERE id = ?""",
            (now, id_)
        )
        affected = result.rowcount
        if affected != 1:
            raise Exception(
                f"ROLLBACK TRIGGER: id {id_} affected {affected} rows (expected exactly 1)"
            )
        print(f"id {id_}: updated ({affected} row)")

    conn.execute("COMMIT")
    print("Transaction committed.")

except Exception as e:
    conn.execute("ROLLBACK")
    print(f"ROLLED BACK: {e}")
    raise

finally:
    conn.close()
```

**Rules:**
- Each id must affect exactly 1 row. If any id returns 0 or more than 1: ROLLBACK immediately.
- Commit only after all 5 ids update correctly.
- If rollback triggered: STOP. Report exact error. Do not proceed to verification.

---

## 6. Verification Steps

Run after physical moves and DB updates complete.

### 6.1 Approved folders present in Archive

```bash
ls "/opt/myPKA/Deliverables/Archive/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal/"
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_Retention Assessment P2 P5 UMC/"
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_UMC Archive Eligibility Chain Process Review/"
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_R1-R5 Prioritization Assessment/"
ls "/opt/myPKA/Deliverables/Archive/20260608_Core_Phase 1 Proposal R1 R5 v01/"
```

Expected: all 5 return file listings.

### 6.2 Approved folders absent from active Deliverables

```bash
ls "/opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal" 2>&1
ls "/opt/myPKA/Deliverables/20260608_Core_Retention Assessment P2 P5 UMC" 2>&1
ls "/opt/myPKA/Deliverables/20260608_Core_UMC Archive Eligibility Chain Process Review" 2>&1
ls "/opt/myPKA/Deliverables/20260608_Core_R1-R5 Prioritization Assessment" 2>&1
ls "/opt/myPKA/Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v01" 2>&1
```

Expected: all 5 return "No such file or directory."

### 6.3 Active D-folder count decreased by exactly 5

```python
import sqlite3
conn = sqlite3.connect('/opt/myPKA/Team Knowledge/team-knowledge.db')
count = conn.execute(
    "SELECT COUNT(*) FROM deliverable_lifecycle WHERE state_gl017 != 'archived'"
).fetchone()[0]
print(f"Non-archived in DB: {count}")
conn.close()
```

Expected: 33 (38 before Pilot B minus 5 archived).
If not 33: STOP. Report discrepancy.

### 6.4 No new folders created

```bash
ls /opt/myPKA/Deliverables/ | grep -v '^Archive$' | wc -l
```

Expected: 35 total entries (33 D-folders + INDEX.md + README.md).
Note: the containment folder `20260612_Core_DL Control Inventory` is one of the 33.

### 6.5 Non-actions confirmed

Verify the following did NOT happen during execution:
- No routing performed to any live system file
- No dashboard work started
- No Learning Candidate triage performed
- No Batch 2 started
- No sweep performed
- No lifecycle records updated outside approved ids 47, 62, 64, 65, 66
- No new D-folders created
- No `registered_but_unclear` folders touched
- No `owner_decision_needed` folders touched
- No domain knowledge folders (items 17-21) touched

---

## 7. Persisted Execution Report Requirement

After execution, immediately write a persisted execution report inside the containment folder.

**Required path:**
`Deliverables/20260612_Core_DL Control Inventory/20260612_pilot-b-archive-execution-report-v01.md`

**Chat-only execution result is not sufficient.** This is a hard requirement per the Execution Persistence Rule (CLAUDE.md, live since 2026-06-12).

**Report must include:**
- Folders archived (names and lifecycle ids)
- Lifecycle records updated
- Active D-folder count before and after
- Stop conditions triggered (or none)
- Unintended actions (or none)
- Non-actions confirmed
- Execution report path (self-reference)

---

## 8. Stop Conditions

Stop immediately and report to Owner if any of the following occur:

| # | Stop condition |
|---|---|
| SC-1 | Active D-folder count before Pilot B does not equal 38 |
| SC-2 | Any source folder is absent from active Deliverables at preflight |
| SC-3 | Any archive target already exists in Archive |
| SC-4 | Any lifecycle record is missing or returns no row for an approved id |
| SC-5 | Any grep returns a live SOP, GL, or CLAUDE.md reference to an approved folder |
| SC-6 | Any open team_task references an approved folder |
| SC-7 | Any folder content contains a live open item signal |
| SC-8 | Archive folder is not writable |
| SC-9 | Any physical move fails or post-step check fails |
| SC-10 | DB update for any id affects 0 or more than 1 row (triggers rollback) |
| SC-11 | DB rollback triggered for any reason |
| SC-12 | Active D-folder count after execution is not exactly 33 |
| SC-13 | Any lifecycle record outside approved ids 47, 62, 64, 65, 66 was updated |
| SC-14 | Any `registered_but_unclear` or `owner_decision_needed` folder was touched |
| SC-15 | Execution report not written (Execution Persistence Rule violation) |

**On any stop condition:** halt all further execution, report exact condition and state to Owner,
await explicit instruction before continuing.

---

## 9. Final Report Format (Execution Report Template)

The execution report written to `20260612_pilot-b-archive-execution-report-v01.md` must follow this format:

```
# Pilot B Archive Execution Report — v01

**Date:** 2026-06-12
**Status:** [Complete / Partial — state which SC triggered]

## Execution Result
[Pilot B — Execution complete / Pilot B — Stopped at SC-X]

## Folders Archived ([N])
| Folder | Lifecycle id |
|---|---|
| [folder name] | [id] |
...

## Lifecycle Records Updated ([N])
ids [list] -> state_gl017=archived, owner_decision=archive

## D-Folder Count
| | Count |
|---|---|
| Active D-folder count before Pilot B | 38 |
| Active D-folder count after Pilot B | [33 or actual] |

## Stop Conditions
[None triggered / SC-X triggered: description]

## Unintended Actions
[None / description]

## Non-Actions Confirmed
- No routing performed
- No dashboard work
- No Learning Candidate triage
- No Batch 2
- No sweep
- No records updated outside approved ids
- No new folders created
- No registered_but_unclear folders touched
- No owner_decision_needed folders touched
- No domain knowledge folders touched

## Execution Report Path
Deliverables/20260612_Core_DL Control Inventory/20260612_pilot-b-archive-execution-report-v01.md
```

---

## Associated Write-List

No associated write-list exists for this execution. Therefore no write-list batch-stop rules apply.
Batch-stop rules are defined in Section 8 of this write plan only.

---

Delivered on: 2026-06-12
Delivered at: `Deliverables/20260612_Core_DL Control Inventory/20260612_pilot-b-archive-execution-write-plan-v01.md`
