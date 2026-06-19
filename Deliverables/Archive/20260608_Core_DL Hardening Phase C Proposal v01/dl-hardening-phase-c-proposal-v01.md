# DL Hardening — Phase C: Hybrid Visibility Layer Specification

**Version:** v01
**Date:** 2026-06-08
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner authorization
**Type:** Implementation specification — no implementation in this document

## Prerequisite Assessments (all approved)

| Document | Location |
|---|---|
| Owner Usability Assessment | `20260608_Core_DL Usability Assessment Owner Perspective` |
| Granularity Assessment | `20260608_Core_DL Granularity Assessment` |
| Visibility Architecture Assessment | `20260608_Core_DL Visibility Architecture Assessment` |
| Post-Granularity Usability Assessment | `20260608_Core_DL Post-Granularity Usability Assessment` |

## Context

**Phase A** implemented the deliverable_lifecycle registry and auto-registration for new
deliverables (2026-06-07).

**Phase B** implemented the Granularity Rules: GL-017 G1/G2/G3 criteria, SOP-017 Section 4a
output placement reference table, SOP-019 granularity gate, CLAUDE.md Granularity Gate
(2026-06-08). Phase B solved the folder proliferation problem. It did not solve Owner
visibility or navigation.

**Phase C** implements the visibility layer: the Owner-facing reporting layer, state
alignment, workstream grouping, and session-start briefing. Phase C is bounded scope — no
governance amendments beyond CLAUDE.md. It produces Owner usability improvement on first
deployment.

---

## 1. Scope

| Area | Included in Phase C |
|---|---|
| Task 86 — workstream code in folder naming | Integration only — Task 86 GL amendment is a parallel track; Phase C consumes its output |
| Task 87 — state vocabulary and artifact_type alignment | Full implementation in Phase C |
| deliverable_lifecycle registration discipline | CLAUDE.md addition only — Larry registers every new primary deliverable at creation |
| Schema addition (`workstream_code`) | Full implementation — Kai migration |
| Reporting script | Full implementation — Kai builds; folder scan + registry + INDEX.md |
| Pending decision visibility | Full implementation — surfaced in INDEX.md and at session start |
| Archive candidate visibility | Full implementation — surfaced in INDEX.md and at session start |
| Session-start visibility | Full implementation — INDEX.md auto-generated at session start |

---

## 2. Component Specifications

### 2.1 Task 86 Integration — Workstream Code Convention

**What Phase C does NOT do:** Implement the GL-001 and GL-004 naming convention amendments.
That is the Task 86 / GL Amendment Proposal v01 track (folder:
`20260608_Core_DLH GL-001 and GL-004 Amendment Proposal v01`). Owner authorization for
that proposal is separate from this proposal.

**What Phase C does:** Design the reporting script to consume workstream codes from the
`workstream_code` registry field. When a deliverable is registered, Larry populates
`workstream_code` if a workstream applies. The script groups INDEX.md output by this field.

**Graceful degradation:** The reporting script always runs safely even when Task 86 naming
amendments are not yet implemented. Deliverables without a `workstream_code` registry entry
appear in an "Ungrouped" section. No Owner-facing data is hidden. The grouping section
improves progressively as registration discipline builds.

**Dependency on Task 86:** Full workstream grouping value is only realized once:
a) the GL-001 workstream code convention is implemented, and
b) new deliverable folders use the convention, and
c) registration discipline captures the code at folder creation.

Phase C can be deployed before Task 86 implementation. Workstream grouping will be partial
until then.

---

### 2.2 Task 87 Integration — State Vocabulary and Artifact Type Alignment

**Problem:** The `deliverable_lifecycle` registry uses `ready` and `active` as state values.
GL-017 Section 3.2 defines the canonical post-acceptance states:

| GL-017 canonical state | Description |
|---|---|
| `active` | Deliverable is in-progress or awaiting a lifecycle decision |
| `parked` | Work suspended; Owner has not closed it |
| `deferred` | Decision pending; blocked on external condition |
| `accepted_as_done` | Owner has accepted the deliverable as complete |

**Migration rule for existing rows:**

| Current registry value | Proposed GL-017 mapping |
|---|---|
| `ready` | `pending_lifecycle_decision` (interim — not yet reviewed by SOP-017) |
| `active` | `active` (retain — already aligned) |

`pending_lifecycle_decision` is a defined interim state for deliverables that exist in the
registry but have not yet passed through SOP-017 lifecycle review. It is a signal to the
system, not an Owner-facing state. The reporting script maps it to "Awaiting lifecycle
review" in INDEX.md output.

**New interim state to add to the schema:**

```sql
ALTER TABLE deliverable_lifecycle
  ADD COLUMN IF NOT EXISTS state_gl017 TEXT;
```

Do not remove the existing `state` column immediately. The migration is additive: populate
`state_gl017` for all existing rows, run the reporting script against `state_gl017`, and
retire `state` in a subsequent cleanup pass after the reporting layer is stable.

**Artifact type vocabulary:**

The current taxonomy is incomplete. Proposed canonical `artifact_type` values:

| Value | When to use |
|---|---|
| `proposal` | Any proposal submitted for Owner accept/reject |
| `assessment` | Read-only analysis, architecture assessment, triage report |
| `execution_report` | Record of a completed execution batch |
| `write_list` | Pre-execution write plan (Iris-reviewed or not) |
| `verification_report` | Post-execution state check, session-start verification, smoke test |
| `closure_report` | Initiative or lifecycle closure record |
| `decision_record` | Named Owner decision on a specific question |
| `triage_document` | Multi-item classification or backlog triage |
| `research_brief` | Pax domain research brief |
| `domain_knowledge_update` | Update to a BKM, KE file, or team knowledge base |
| `working_artifact` | Intermediate or parking artifact with no standalone lifecycle value |

**Migration for existing artifact_type mismatches (from Phase B Triage analysis):**

| Current value | Affected rows | Correct type |
|---|---|---|
| `status_report` (execution reports) | LC Batch 1, LC Batch 2 execution reports | `execution_report` |
| `status_report` (verification reports) | LCL Session Start Verification, Post-SOP-019 Session Start Verification, Final Governance State Verification | `verification_report` |
| `proposal` (write-lists) | LC Batch 1 Write-List, LC Batch 2 Write-List, LC Triage Write-Plan | `write_list` |
| `triage_document` (assessments) | Architecture Triage Memory Domain Routing | `assessment` |

Kai executes the migration from the above mapping table. No Owner decision is required per
row — the mapping is deterministic from the Phase B Triage analysis.

---

### 2.3 Registration Discipline — CLAUDE.md Addition

**Current state:** Larry creates deliverable folders but does not consistently register them
in `deliverable_lifecycle` at creation time. Registration happens inconsistently, after the
fact, or not at all for deliverables created in fast-moving sessions.

**Proposed CLAUDE.md addition** (Larry operational section):

```
### Deliverable Registration — Mandatory

On every new primary deliverable folder creation (i.e., every folder that passes the
GL-017 Granularity Gate as G1): INSERT one row into `deliverable_lifecycle` in
`team-knowledge.db` before briefing any specialist or creating any content.

Fields to populate at creation:
- folder_name: exact folder name as created
- domain: Core / Personal / Kamer E-commerce / Geldstroom Regie
- artifact_type: from canonical vocabulary in Phase C specification
- state_gl017: 'active'
- workstream_code: if the deliverable belongs to a known workstream (e.g., DLH, LC, UMC),
  populate this field. Leave NULL if standalone.
- owner_decision: leave NULL at creation

If the INSERT fails: note the failure, proceed with folder creation, and add a team_tasks
row to register retroactively before session close.

Registration is not optional. An unregistered primary deliverable is a visibility gap.
```

This is a CLAUDE.md addition only. No governance amendment required.

---

### 2.4 Schema Addition — `workstream_code` Field

**Migration script** (Kai):

```sql
-- Add workstream_code field
ALTER TABLE deliverable_lifecycle
  ADD COLUMN IF NOT EXISTS workstream_code TEXT;

-- Add state_gl017 field (aligned to GL-017 Section 3.2)
ALTER TABLE deliverable_lifecycle
  ADD COLUMN IF NOT EXISTS state_gl017 TEXT;

-- Populate state_gl017 from existing state column
UPDATE deliverable_lifecycle
  SET state_gl017 = 'active'
  WHERE state = 'active';

UPDATE deliverable_lifecycle
  SET state_gl017 = 'pending_lifecycle_decision'
  WHERE state = 'ready' OR state IS NULL OR state = '';

-- Populate workstream_code for known workstream deliverables
-- (Kai infers from folder_name patterns; manual review for ambiguous cases)
UPDATE deliverable_lifecycle
  SET workstream_code = 'DLH'
  WHERE folder_name ILIKE '%Deliverable Lifecycle Hardening%'
     OR folder_name ILIKE '%DLH%'
     OR folder_name ILIKE '%DL Granularity%'
     OR folder_name ILIKE '%DL Hardening%'
     OR folder_name ILIKE '%DL Visibility%'
     OR folder_name ILIKE '%DL Usability%'
     OR folder_name ILIKE '%DL Post-Granularity%'
     OR folder_name ILIKE '%LC Lifecycle%'
     OR folder_name ILIKE '%LC Batch%'
     OR folder_name ILIKE '%LC Triage%'
     OR folder_name ILIKE '%LC-4%'
     OR folder_name ILIKE '%LC-5%'
     OR folder_name ILIKE '%LC-6%'
     OR folder_name ILIKE '%LC-7%'
     OR folder_name ILIKE '%LC-9%'
     OR folder_name ILIKE '%LC-10%'
     OR folder_name ILIKE '%LCL Session%'
     OR folder_name ILIKE '%Lifecycle Decision%'
     OR folder_name ILIKE '%Lifecycle Phase%'
     OR folder_name ILIKE '%SOP-017 Amendment%'
     OR folder_name ILIKE '%Auto-Processing Deliverable%'
     OR folder_name ILIKE '%Naming Artifact%';

UPDATE deliverable_lifecycle
  SET workstream_code = 'GG'
  WHERE folder_name ILIKE '%Governance Gatekeeper%'
     OR folder_name ILIKE '%SOP-019%'
     OR folder_name ILIKE '%Review Gate%';

UPDATE deliverable_lifecycle
  SET workstream_code = 'UMC'
  WHERE folder_name ILIKE '%Unified Memory%'
     OR folder_name ILIKE '%UMC%'
     OR folder_name ILIKE '%Memory Domain%';

UPDATE deliverable_lifecycle
  SET workstream_code = 'AUDIT'
  WHERE folder_name ILIKE '%AI Team Audit%'
     OR folder_name ILIKE '%B-021C%';
```

**Artifact_type migration** (separate script):

```sql
-- Fix execution reports mistyped as status_report
UPDATE deliverable_lifecycle
  SET artifact_type = 'execution_report'
  WHERE folder_name IN (
    '20260607_Core_LC Batch 1 Execution Report',
    '20260607_Core_LC Batch 2 Execution Report'
  );

-- Fix verification reports mistyped as status_report
UPDATE deliverable_lifecycle
  SET artifact_type = 'verification_report'
  WHERE folder_name IN (
    '20260607_Core_LCL Session Start Verification',
    '20260607_Core_Post-SOP-019 Session Start Verification',
    '20260607_Core_Final Governance State Verification'
  );

-- Fix write-lists mistyped as proposal
UPDATE deliverable_lifecycle
  SET artifact_type = 'write_list'
  WHERE folder_name IN (
    '20260607_Core_LC Batch 1 Write-List',
    '20260607_Core_LC Batch 2 Write-List',
    '20260607_Core_LC Triage Write-Plan',
    '20260606_Core_LC Lifecycle Phase 1 Write-List v05'
  );

-- Fix assessments mistyped as triage_document
UPDATE deliverable_lifecycle
  SET artifact_type = 'assessment'
  WHERE folder_name = '20260604_Core_Architecture Triage Memory Domain Routing';
```

---

### 2.5 Reporting Script Specification

**Script name:** `generate_deliverable_index.py`
**Location:** `Team Knowledge/Core/Scripts/generate_deliverable_index.py`
**Output:** `Deliverables/INDEX.md` (overwritten on each run)
**Executor:** Kai builds; Larry runs at session start

**Logic:**

```
1. Read all entries from deliverable_lifecycle WHERE state_gl017 != 'archived'
2. Scan Deliverables/ folder for all subfolders (excluding Archive/)
3. For each folder: match to registry row by folder_name
   - Match found: use registry data (state_gl017, workstream_code, artifact_type,
     owner_decision)
   - No match: label state as '[state unknown — not registered]'
4. Group by workstream_code:
   - Known workstream: group under workstream header
   - NULL workstream_code: group under "Standalone" section
   - Unregistered: group under "Unregistered (visibility gap)" section
5. For each deliverable, output one row:
   - Folder name (clickable link to folder)
   - State (from state_gl017, mapped to display label)
   - Artifact type
   - Owner decision pending flag (if owner_decision IS NULL and state_gl017 = 'active')
   - Archive candidate flag (if state_gl017 = 'accepted_as_done' and age > 14 days)
6. Append summary section:
   - Total active deliverables
   - Pending Owner decisions count
   - Archive candidates count
   - Unregistered folders count (visibility gap alert)
7. Write to Deliverables/INDEX.md
```

**State display labels** (in INDEX.md):

| state_gl017 value | Display label |
|---|---|
| `active` | Active |
| `parked` | Parked |
| `deferred` | Deferred |
| `accepted_as_done` | Done |
| `pending_lifecycle_decision` | Awaiting lifecycle review |
| `archived` | (excluded from INDEX.md) |
| NULL / unregistered | State unknown |

**Pending decision surfacing** — a deliverable shows "Decision pending" when:
- `owner_decision IS NULL`, AND
- `state_gl017` = `active` or `pending_lifecycle_decision`, AND
- `artifact_type` IN (`proposal`, `assessment`, `write_list`, `triage_document`)

**Archive candidate surfacing** — a deliverable shows "Archive candidate" when:
- `state_gl017` = `accepted_as_done`, AND
- `created_at` < NOW() - INTERVAL '14 days'

**Example INDEX.md output structure:**

```markdown
# Deliverables — Active Portfolio
_Generated: 2026-06-08 | 32 active | 4 pending decisions | 2 archive candidates | 0 unregistered_

---

## DLH — Deliverable Lifecycle Hardening

| Deliverable | State | Type | Flags |
|---|---|---|---|
| [DL Granularity Assessment](20260608_Core_DL Granularity Assessment/) | Done | assessment | Archive candidate |
| [DL Hardening Phase C Proposal v01](20260608_Core_DL Hardening Phase C Proposal v01/) | Active | proposal | Decision pending |
| ... | | | |

## GG — Governance Gatekeeper

...

## UMC — Unified Memory Core

...

## Standalone

...

## Unregistered (visibility gap)

_These folders exist in Deliverables/ but are not registered in deliverable_lifecycle._
_Larry: register before session close._

...

---

## Summary

- Pending Owner decisions: [list folder names]
- Archive candidates: [list folder names]
- Unregistered folders: [count and list]
```

---

### 2.6 Session-Start Integration

**Integration point:** The `start-morning-routine` skill and the `start-session` context.

**Proposed addition to session start (Larry operational):**

At every session start:
1. Run `generate_deliverable_index.py` (or call Kai to run it if the script is not yet
   accessible directly from the session context)
2. Surface the summary line: "X active deliverables | Y pending decisions | Z archive
   candidates | W unregistered"
3. If pending decisions > 0: list the deliverable names, one per line
4. If archive candidates > 0: list names and offer to process in batch
5. If unregistered > 0: alert and add a team_tasks row for registration

This does not require a hook. Larry executes this check as the first action after Team
Inbox check, before any other session work.

Long-term: Kai can wire this to the session-start hook (`PostToolUse` on session start)
so the INDEX.md is regenerated automatically. This is a Phase C enhancement, not a
prerequisite.

---

## 3. Implementation Sequence

Dependencies govern the sequence. The schema migration is the foundation; everything
else builds on it.

| Step | Action | Assignee | Depends on | Batch-stop trigger |
|---|---|---|---|---|
| C-1 | Schema migration: add `workstream_code` and `state_gl017` columns | Kai | Owner authorization | C-1 fails → stop all subsequent steps |
| C-2 | State vocabulary migration: populate `state_gl017` for all existing rows | Kai | C-1 | Any row with null `state_gl017` after migration → stop |
| C-3 | Workstream code migration: populate `workstream_code` for known workstreams | Kai | C-1 | Review flagged ambiguous rows before proceeding |
| C-4 | Artifact_type migration: correct mistyped rows | Kai | C-1 | Row count before and after must match; stop if mismatch |
| C-5 | CLAUDE.md registration discipline addition | Larry | C-1, C-2 | Larry confirms CLAUDE.md update before any new deliverable folders are created |
| C-6 | `generate_deliverable_index.py` script build | Kai | C-1, C-2, C-3 | Script must produce INDEX.md without error on first run |
| C-7 | INDEX.md first generation and Owner review | Larry | C-6 | If INDEX.md shows > 10 unregistered folders: stop and register before proceeding |
| C-8 | Session-start integration (Larry operational protocol) | Larry | C-7 | — |
| C-9 | Hook-based auto-generation (optional enhancement) | Kai | C-8, stable | Not a prerequisite; do not block Phase C completion on this |

**Task 86 parallel track:** GL-001/GL-004 amendment (naming convention) runs as a
separate authorization and implementation track. Phase C does not block on Task 86. Full
workstream grouping value is realized once Task 86 is implemented and new folders use the
convention.

---

## 4. Governance Impact

| Instrument | Change | Required? |
|---|---|---|
| GL-017 | No change | — |
| SOP-017 | No change | — |
| GL-016 | No change | — |
| SOP-019 | No change | — |
| GL-001 / GL-004 | No change in Phase C (Task 86 parallel track) | — |
| CLAUDE.md (Larry) | Addition: registration discipline rule (Section 2.3 above) | Yes — Owner authorization required |
| team-knowledge.db schema | Addition: two columns to `deliverable_lifecycle` | Yes — Kai migration |
| `generate_deliverable_index.py` | New script | Yes — Kai build |
| `Deliverables/INDEX.md` | New generated file | Yes — generated output; not a governance record |

Phase C does not require any governance amendments beyond the CLAUDE.md addition. The
INDEX.md is generated output, not a governance record, and does not require its own
lifecycle processing.

---

## 5. Post-Checks

After each step, confirm before proceeding:

| Step | Post-check |
|---|---|
| C-1 | `\d deliverable_lifecycle` shows `workstream_code` and `state_gl017` columns |
| C-2 | `SELECT COUNT(*) FROM deliverable_lifecycle WHERE state_gl017 IS NULL` = 0 |
| C-3 | `SELECT COUNT(*) FROM deliverable_lifecycle WHERE workstream_code IS NOT NULL` > 0 |
| C-4 | Row count before and after artifact_type migration is identical |
| C-5 | CLAUDE.md contains the exact registration discipline text |
| C-6 | Script runs without error; INDEX.md created in Deliverables/ |
| C-7 | INDEX.md accurately reflects active deliverable count; unregistered count < 5 |
| C-8 | Session-start protocol produces summary line with correct counts |

---

## 6. Batch-Stop Rules

**No associated write-list for this proposal.** No write-list batch-stop rules apply.
The implementation steps in Section 3 define their own batch-stop triggers per step.

Step C-1 is the critical gate: if the schema migration fails, all subsequent steps are
blocked. Do not proceed past C-1 until the schema is confirmed.

Step C-3 (workstream code migration) includes ambiguous rows that Kai must flag for
review before completing the migration. Kai does not auto-resolve ambiguous rows. Kai
surfaces them and waits for Owner or Larry confirmation.

Step C-7 (INDEX.md first generation) includes an unregistered-folder check. If the count
exceeds 10, Larry registers the missing deliverables before proceeding. This is a
quality gate, not a technical failure.

---

## 7. No-Action Scope (Out of Scope for Phase C)

The following items are explicitly excluded from Phase C:

- Task 75 (GL-001 deliverable folder and versioning rule amendment)
- Task 77 (English-language rule for governance deliverables, GL-014 amendment)
- Task 78 (correction versioning rule, SOP-015 amendment)
- Task 86 GL-001/GL-004 naming convention amendment (parallel track)
- Retroactive folder consolidation for pre-Phase B deliverables
- Full migration of the existing `state` column to `state_gl017` (the `state` column
  remains until the reporting layer is stable; retirement is a subsequent cleanup pass)
- Hook-based auto-generation of INDEX.md (C-9 is an optional enhancement)

---

## 8. Owner Decision Required

Authorization needed:

1. **Authorize Phase C implementation** — all steps C-1 through C-8 as specified above
2. **Authorize CLAUDE.md registration discipline addition** — exact text in Section 2.3
3. **Confirm Task 87 artifact_type migration** — mapping table in Section 2.2 is correct

Owner answers: yes, no, or correction per item.

---

Delivered on: 2026-06-08
Delivered at: `Deliverables/20260608_Core_DL Hardening Phase C Proposal v01/dl-hardening-phase-c-proposal-v01.md`
