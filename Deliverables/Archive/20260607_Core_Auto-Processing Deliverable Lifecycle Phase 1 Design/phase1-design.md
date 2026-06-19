# Phase 1 Design: Auto-Processing / Deliverable Lifecycle

**Status:** Design — awaiting Owner write authorization to implement
**Date:** 2026-06-07
**Author:** Larry (Team Orchestrator)
**Predecessor:** discovery-scope-proposal.md (2026-06-07, Owner authorized: yes)
**Phase 1 scope:** Detection and classification only. No extraction, no archiving, no state transitions during this phase.

---

## What Phase 1 Builds

Four components:

1. `deliverable_lifecycle` table in `team-knowledge.db`
2. Classification rules (Python dict): artifact type → default state and proposed destination
3. Bootstrap script: one-time scan of `Deliverables/` to register existing artifacts
4. /close-session sweep extension: surface unprocessed artifacts older than 7 days

Nothing else. No extraction pipelines. No archiving automation. No personal routine processing.

---

## Component 1: Database Table

**Location:** `team-knowledge.db` (team-level scope, spans all domains)

```sql
CREATE TABLE IF NOT EXISTS deliverable_lifecycle (
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
    registered_at       TEXT NOT NULL DEFAULT (datetime('now')),
    state_changed_at    TEXT,
    processed_at        TEXT,
    owner_decision      TEXT,
    owner_decision_at   TEXT
);
```

**Field definitions:**

| Field | Values / Notes |
|---|---|
| artifact_name | Folder name under `Deliverables/` — this is the unique identifier |
| artifact_type | From taxonomy below |
| state | draft / ready / active / processing / processed / superseded / archived |
| proposed_destination | Human-readable destination string, may list multiple |
| destination_domain | personal / core / kamer-ecommerce / geldstroom-regie |
| processing_notes | Specific extraction instructions for the processing agent |
| superseded_by | artifact_name of the replacement artifact (nullable) |
| source_session | Session slug that produced this artifact (nullable) |
| agent | Specialist responsible for processing (nullable, set at assignment) |
| registered_at | Timestamp of registration |
| state_changed_at | Timestamp of last state change |
| processed_at | Timestamp when processing completed (nullable) |
| owner_decision | confirmed / deferred / rejected (nullable until Owner responds) |
| owner_decision_at | Timestamp of Owner decision (nullable) |

**State transition rules:**

```
ready         → active         (Owner confirms: this file itself is the reference, no extraction needed)
ready         → processing     (Owner confirms: extract to destination, agent assigned)
ready         → archived       (Owner confirms: no knowledge value, archive directly)
ready         → deferred       (Owner defers: stays ready, resurfaces next sweep)
processing    → processed      (Agent completes extraction, Larry confirms)
active        → superseded     (Newer artifact registered for same topic)
superseded    → archived       (Owner confirms cleanup)
processed     → archived       (After extraction verified, source archived as reference)
```

Every transition is logged with `state_changed_at` and `owner_decision_at`.

---

## Component 2: Classification Rules

**Embedded in bootstrap script and sweep as a Python dict.**

```python
CLASSIFICATION_RULES = {
    "proposal": {
        "default_state": "ready",
        "proposed_destination": "BKM: GL or SOP update (if approved) or Reference only (if superseded)",
        "destination_domain": "core",
        "auto_archive_eligible": False,
        "notes": "Proposals that were approved become active; rejected proposals go to archived"
    },
    "execution_report": {
        "default_state": "ready",
        "proposed_destination": "BKM: project/workstream notes + agent_learnings",
        "destination_domain": "core",
        "auto_archive_eligible": False,
        "notes": "Extract decisions and deviations; archive source after extraction"
    },
    "status_report": {
        "default_state": "ready",
        "proposed_destination": "Archived directly (no extraction if all-green)",
        "destination_domain": "core",
        "auto_archive_eligible": True,
        "notes": "Only extract if report contains decisions or escalations"
    },
    "closure_report": {
        "default_state": "ready",
        "proposed_destination": "BKM: project notes + decision record + agent_learnings",
        "destination_domain": "core",
        "auto_archive_eligible": False,
        "notes": "Most valuable artifact type; always extract before archiving"
    },
    "audit_report": {
        "default_state": "active",
        "proposed_destination": "BKM: team-knowledge.db patterns + agent_learnings (when acted on)",
        "destination_domain": "core",
        "auto_archive_eligible": False,
        "notes": "Audit reports stay active until acted on or superseded"
    },
    "decision_record": {
        "default_state": "active",
        "proposed_destination": "BKM: team-knowledge.db decisions table",
        "destination_domain": "core",
        "auto_archive_eligible": False,
        "notes": "Decision records remain active; archive only when superseded"
    },
    "research_brief": {
        "default_state": "ready",
        "proposed_destination": "BKM: domain database or AGENT.md of relevant specialist",
        "destination_domain": "core",
        "auto_archive_eligible": False,
        "notes": "Extract to the specialist it was written for"
    },
    "domain_knowledge_update": {
        "default_state": "ready",
        "proposed_destination": "BKM: AGENT.md + GL/SOP if applicable",
        "destination_domain": "core",
        "auto_archive_eligible": False,
        "notes": "Verify GL/SOP/AGENT.md reflects content before archiving"
    },
    "triage_document": {
        "default_state": "ready",
        "proposed_destination": "Reference only (link from relevant project or GL)",
        "destination_domain": "core",
        "auto_archive_eligible": False,
        "notes": "Usually superseded by a design or implementation record"
    }
}
```

**Classification by artifact name pattern (for bootstrap):**

The bootstrap script classifies existing artifacts by folder name keywords. Pattern priority: first match wins.

| Keyword pattern | Assigned type |
|---|---|
| contains "Closure Record" | closure_report |
| contains "Smoke Test" | status_report |
| contains "Implementation Readiness" | status_report |
| contains "Audit" | audit_report |
| contains "Triage" | triage_document |
| contains "Discovery" or "Scope Proposal" | proposal |
| contains "Design" (without "Scope") | proposal |
| contains "Amendment" | domain_knowledge_update |
| contains "Write-List" | proposal |
| contains "Research" | research_brief |
| contains "architectuur" | triage_document |
| contains "Blueprint" or "Schema" or "Routine" | domain_knowledge_update |
| contains "One-pager" | domain_knowledge_update |
| no match | proposal (fallback, flagged for manual review) |

**Domain routing by folder name:**

| Keyword | destination_domain |
|---|---|
| "Personal" | personal |
| "Kamer E-commerce" | kamer-ecommerce |
| "Geldstroom Regie" | geldstroom-regie |
| "Core" or no keyword | core |

---

## Component 3: Bootstrap Script

**Location:** `Team Knowledge/Core/Scripts/deliverable_lifecycle_bootstrap.py`

**Purpose:** One-time registration of all existing `Deliverables/` artifacts (excluding `Archive/`).

**Behavior:**

1. Scan `Deliverables/` for all subfolders (one level deep, exclude `Archive/`)
2. For each subfolder: apply classification rules to determine `artifact_type`, `destination_domain`, `proposed_destination`
3. Set `state` using `default_state` from classification rules
4. INSERT INTO `deliverable_lifecycle` — skip if `artifact_name` already exists (idempotent)
5. Print a summary table: how many registered, how many skipped, how many need manual review (fallback classification)
6. Write no state changes, no processing actions

**Output format (stdout):**

```
Deliverable Lifecycle Bootstrap — 2026-06-07

Registered: 18
Skipped (already exists): 0
Needs manual review: 2

Manual review needed:
  - 20260530_Personal_Blueprint weekschema en oefeningen  (fallback: proposal)
  - 20260530_Personal_Health Monitoring Schema            (fallback: proposal)

Run complete. No state changes written.
```

**Parameters:** `--db-path` (optional override for team-knowledge.db path)

**Idempotency:** Safe to run multiple times. Existing rows are never overwritten.

---

## Component 4: /close-session Sweep Extension

**Integration point:** Appended to the existing /close-session sweep step, after the team_tasks sweep.

**Trigger:** State = 'ready' AND registered_at < (datetime('now') - 7 days), OR state = 'ready' AND owner_decision = 'deferred'

**Query:**

```sql
SELECT artifact_name, artifact_type, proposed_destination, destination_domain,
       CAST((julianday('now') - julianday(registered_at)) AS INTEGER) AS days_open,
       owner_decision
FROM deliverable_lifecycle
WHERE state = 'ready'
  AND (
      registered_at < datetime('now', '-7 days')
      OR owner_decision = 'deferred'
  )
ORDER BY days_open DESC;
```

**Output shown to Owner (example):**

```
Deliverable Lifecycle Sweep: 3 items awaiting processing

| # | Artifact | Type | Proposed action | Days open |
|---|---|---|---|---|
| 1 | 20260520_Core_UMC architectuurschets | Triage | Reference only (link from GL) | 18 |
| 2 | 20260530_Personal_Blueprint weekschema | Domain knowledge | Extract to PKM: KE-Health | 8 |
| 3 | 20260603_Core_B-021C Closure Record | Closure report | Extract to project notes + agent_learnings | 4 |

Per item: bevestig / uitstellen / afwijzen / correctie
```

**What happens after Owner responds:**

- **Bevestig (confirm):** `owner_decision = 'confirmed'`, `owner_decision_at = now()`. State does NOT change yet. A `team_tasks` row is created assigning the processing work to the relevant specialist. State transitions to 'processing' only when the specialist begins.
- **Uitstellen (defer):** `owner_decision = 'deferred'`, `owner_decision_at = now()`. Item resurfaces in the next sweep.
- **Afwijzen (reject):** `owner_decision = 'rejected'`, state → 'archived'. No processing.
- **Correctie:** Owner provides a corrected proposed_destination or artifact_type. Row updated, state stays 'ready'.

**Write authorization per item:** Each Owner response (confirm / defer / reject) is a separate authorization. The sweep output is a proposal. No writes happen until the Owner responds.

---

## Files to Create During Implementation

| File | Action |
|---|---|
| `team-knowledge.db` | ALTER: add `deliverable_lifecycle` table |
| `Team Knowledge/Core/Scripts/deliverable_lifecycle_bootstrap.py` | CREATE |
| `/close-session skill` | EXTEND: append sweep query and output block |

No GL, SOP, WS, or AGENT.md files are created in Phase 1. Those belong to Phase 2 when processing destinations are actually used.

---

## What Phase 1 Does Not Do

Explicit non-scope for this phase:

- No extraction of insights into PKM or BKM
- No file moves or archiving
- No auto-SOP or GL updates
- No UMC indexing of deliverables
- No deletion of any artifact
- No processing pipelines
- No personal routine processing
- No Phase 2 design

---

## Phase 1 Success Criterion

At the end of every /close-session: the Owner sees a list of unprocessed deliverables with proposed actions. No deliverable older than 14 days goes unnoticed. The Owner can act on each item in under 30 seconds.

---

## Owner Authorization Request

This document is the complete Phase 1 design. It is execution-ready.

To proceed to implementation, the Owner must authorize:

1. Creating `deliverable_lifecycle` table in `team-knowledge.db`
2. Creating `deliverable_lifecycle_bootstrap.py` in `Team Knowledge/Core/Scripts/`
3. Extending the /close-session skill with the sweep query and output block

The Owner can respond with:

- **Ja** to authorize all three implementation writes
- **Nee** to stop here
- **Correctie** to adjust the design before implementation

---

*Delivered on: 2026-06-07*
*Delivered at: /opt/myPKA/Deliverables/20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design/phase1-design.md*
