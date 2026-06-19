# Deliverable Lifecycle Hardening — Discovery and Proposal

**Date:** 2026-06-07
**Author:** Larry, Team Orchestrator
**Status:** Proposal — awaiting Owner review
**Scope:** Read-only discovery; no files modified; no database writes; no folder moves

---

## 1. Current State Summary

### Folder counts

| Location | Count |
|---|---|
| Active (non-Archive) folders in `Deliverables/` | 38 |
| Archived folders in `Deliverables/Archive/` | 21 |
| Total folders | 59 |
| Registered in `deliverable_lifecycle` DB | 21 rows |
| Active folders with DB registration | 17 |
| Active folders WITHOUT DB registration | 21 |
| DB rows with state "ready" | 16 |
| DB rows with state "archived" | 4 |
| DB rows with state "active" | 1 |
| DB rows with `owner_decision` set | 1 (approved, archived) |
| DB rows with `owner_decision = NULL` | 20 |
| Deliverables that have reached "processed" state | 0 |

### Open lifecycle-related team_tasks

| id | title | assignee |
|---|---|---|
| 75 | Deliverable Folder and Versioning Rule — define and implement for governance flows | larry |
| 77 | Graduation candidate 1: add English-language rule for governance deliverables to GL | larry |
| 78 | Graduation candidate 2: add versioning rule for governance proposal corrections to SOP-015 or GL | larry |
| 80 | Write lc-triage-write-plan-v02.md — fix post-check scope and print bug | larry |
| 81 | Batch 3 write-list — deferred pending Q1 and Q2 answers | larry |

---

## 2. Problem Statement

The `Deliverables/` folder is functioning as an uncontrolled staging area. The lifecycle
infrastructure exists (GL-017, SOP-017, `deliverable_lifecycle` table) and has been implemented,
but it is not being applied consistently in practice.

**Specific problems identified:**

**P-1: 55% of active folders are unregistered.**
21 of 38 active folders have no entry in `deliverable_lifecycle`. All 21 are from today's
SOP-019 session work. They were created as part of governance execution but never registered.
This means the lifecycle DB is already behind the folder state, one day after the DB was set up.

**P-2: No deliverable has been processed.**
16 registered deliverables are in state "ready" with `owner_decision = NULL`. This includes
items dating from 2026-05-13 (4 weeks ago). The processing pipeline exists but has never run
from "ready" through to "processed" with confirmed knowledge extraction.

**P-3: No registration trigger at creation time.**
There is no mechanism that ensures a new deliverable folder is registered in the DB when it
is created. Registration depends on manual triage sessions, which fall behind during active
governance work.

**P-4: No versioning rule in effect.**
Multiple governance deliverable series have v01/v02/v03/v04 files scattered across
folders (e.g., `lc-batch2-write-list-v04.md`, `iris-review-lc-batch2-write-list-v04.md`).
There is no rule defining what "authoritative version" means within a folder, nor any rule
preventing the creation of a second folder for a revised version of the same deliverable.
Task 75 captures this as an open item.

**P-5: No "stale" detection.**
No alert fires when an item sits in "ready" state past a threshold. Items can accumulate
indefinitely without visibility.

**P-6: Graduation candidates are open but not progressing.**
Tasks 77 and 78 define two governance amendments (English-language rule, versioning rule)
that are directly relevant to deliverable lifecycle hardening. They have no execution plan yet.

**P-7: The Batch 1 proposal for backlog processing is itself unregistered.**
The proposal document `20260607_Core_Deliverable Lifecycle Backlog Processing Batch 1 Proposal`
sits in the active folder unregistered, which is an example of the registration gap
(P-1) applying to the tool meant to fix the backlog.

---

## 3. Existing Lifecycle Rules Found

### GL-017 — Deliverable Lifecycle, Knowledge Processing, and Archiving

**Status: Active.** Implemented 2026-06-04.

Defines:
- Lifecycle stages: Draft, Ready, Active/Authoritative, Processing, Processed, Superseded, Archived
- Lifecycle markers: Authoritative, Processed, Indexed, Knowledge Extracted, Reference Preserved
- 5 core principles (SSOT, owner confirmation, markers-are-additive, no-retroactive-changes,
  lifecycle-recording)
- Relationship to SOP-017, GL-016, SOP-016, GL-004

**Gap:** GL-017 defines the model but does not define the registration trigger — it assumes
deliverables will be registered. No rule says when and how registration happens.

### SOP-017 — Deliverable Lifecycle, Knowledge Processing, and Archiving Procedure

**Status: Active.** Implemented 2026-06-04.

Defines:
- 6-phase decision workflow (Prerequisite Verification, Rule Application, Cross-Domain Check,
  Owner Proposal, Execution, State Recording)
- Processing Destination Catalog (10 destinations: PKM, BKM, archive, reference, etc.)
- Decision rules R1 through R10
- Domain flows: Personal, Business, Governance
- Archive handling (superseded, source folder closure, mandatory empty-folder check)
- Authoritative Source handling
- Safeguards checklist (13 items)
- Execution report requirements (16 fields)
- Worked examples (5 examples covering proposals, execution reports, closure reports, BKM, PKM)

**Gap:** SOP-017 defines how to process a deliverable once identified for processing. It does
not define when processing must start, how long an item may remain in "ready" state, or who
triggers the SOP-017 workflow. There is no scheduled sweep or mandatory processing trigger.

### GL-016 — Review Gate for Governance-Relevant Deliverables

**Status: Active.** Implemented 2026-06-04/05.

Defines the review gate requirement for all governance deliverables before they enter the
lifecycle. All proposal types, execution reports, closure reports, status reports, system-file
changes, and database changes require a review gate.

**Gap:** GL-016 governs entry into the governance pipeline. It does not govern what happens
to a deliverable after the review gate passes. The handoff from "review-gate-passed" to
"registered-in-lifecycle" is not defined.

### SOP-016 — Review Gate Procedure

**Status: Active.**

Implements GL-016. Defines three operating modes, review package format, 13 checks, Owner
decision options, and hard stop conditions.

**Gap:** Same as GL-016 — SOP-016 does not define lifecycle registration as a post-gate step.

---

## 4. Lifecycle State Model Assessment

The existing model in GL-017 is sound. The seven states and five markers are well-defined.
The problem is not the model — it is that the model has no enforcement path.

| State | Model definition | Actual usage |
|---|---|---|
| Draft | Being prepared | Not tracked in DB |
| Ready | Complete, awaiting processing decision | 16 items stuck here with no decisions |
| Active / Authoritative | Current SSOT, no extraction needed | 1 item (not clear which) |
| Processing | Extraction in progress | 0 items |
| Processed | Extraction complete, archived as reference | 0 items |
| Superseded | Replaced by newer deliverable | 0 items — but v-numbered files imply superseded items exist, untracked |
| Archived | Filed for reference only | 4 items (only 1 with owner_decision set) |

**Critical gap:** The pipeline has never completed a full cycle. No deliverable has moved
from Ready to Processed. The lifecycle DB is a registration ledger, not a working system.

**Secondary gap:** "Superseded" is undefined in practice. Multiple version files exist
within deliverable folders with no DB markers.

---

## 5. Database and Table Assessment

### Table: `deliverable_lifecycle`

**Schema:**
`id`, `artifact_name`, `artifact_type`, `state`, `proposed_destination`,
`destination_domain`, `processing_notes`, `superseded_by`, `source_session`, `agent`,
`registered_at`, `state_changed_at`, `processed_at`, `owner_decision`, `owner_decision_at`

**Assessment: Schema is sufficient for the current model.**

Missing columns that would strengthen the model:
- No `stale_threshold_days` or `last_reviewed_at` — makes stale detection impossible
- No `folder_path` column — artifact_name is the folder name, which works, but an explicit
  path would be safer if folders are ever renamed
- No `registration_trigger` column — cannot audit how an item got registered (manual triage,
  session sweep, etc.)
- No `processing_batch` column — when processing in batches, there is no way to query
  "which items are in Batch 2" from the DB alone; it has to be maintained in a separate file

**Immediate concern:** `created_at` column does not exist on this table (confirmed by error
when queried). The query tool defaults to `registered_at`. This is fine for current use, but
any tooling or script that queries `created_at` will fail silently.

### Table coverage vs folder reality

21 of 38 active folders are unregistered. The DB is 55% behind the actual state.
The Archive folder has 21 subdirectories; only 4 are in the DB as "archived."
This means 17 archived items were moved manually without lifecycle registration — they
predate the lifecycle system or were archived outside the SOP-017 workflow.

---

## 6. Risk Analysis

| Risk | Severity | Likelihood |
|---|---|---|
| Processing a deliverable that should be kept as authoritative source | High | Medium — if batch processing runs without per-item review |
| Archiving a superseded version while the replacement is not yet confirmed | High | Medium — affects knowledge integrity |
| Growing unregistered backlog erodes DB value over time | Medium | High — already at 55% gap after 1 session |
| "Ready" items never processed — knowledge locked in flat files | Medium | High — 0 items processed in 3 days since setup |
| Duplicate knowledge: same insight extracted into multiple destinations | Low | Medium — no dedup check in SOP-017 |
| Folder move breaks links if no pre-move link audit | High | Low for now — links are not yet widespread |
| Processing items before open Graduation Candidates (77, 78) are resolved causes rework | Medium | Medium — versioning rule affects how superseded is defined |

---

## 7. Proposed Target Lifecycle

```
[Creation] → Registration (required, at creation time or at close-session sweep)
    ↓
[Ready] → Owner-approved processing decision (batch proposal)
    ↓
[Processing] → SOP-017 workflow executed (BKM/PKM extraction or archive-direct)
    ↓
[Processed] → Execution report filed, state recorded
    ↓
[Archived] — folder moved to Archive/; source folder closed (per SOP-017 EX-8)
```

**Supporting controls:**
- `/close-session` sweep: checks active Deliverables folders and flags unregistered items
- Stale alert: any item in "ready" for more than 7 days surfaced at weekly sweep
- Versioning rule (task 75): defines what counts as one deliverable vs. a new deliverable
- Language rule (task 77): governance deliverables use English filenames
- No deliverable moves state without Owner confirmation (existing GL-017 rule, unchanged)

---

## 8. Proposed Cleanup Strategy

### Phase A — Registration cleanup (DB writes only, no file moves)

Register the 21 unregistered active folders into `deliverable_lifecycle`.
For each item: assign `artifact_type`, `state = ready`, `proposed_destination` (preliminary),
`destination_domain`, `source_session`, `agent = larry`.

This is the lowest-risk first step. It is entirely DB-side. No files touched.

**Item classification for registration:**

| Folder | Suggested type | Domain |
|---|---|---|
| 20260607_Core_LC Batch 1 Write-List | proposal | core |
| 20260607_Core_LC Batch 1 Execution Report | status_report | core |
| 20260607_Core_LC Batch 2 Write-List | proposal | core |
| 20260607_Core_LC Batch 2 Execution Report | status_report | core |
| 20260607_Core_LC Triage Write-Plan | proposal | core |
| 20260607_Core_LC Naming Alignment Impact Assessment | triage_document | core |
| 20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion | closure_report | core |
| 20260607_Core_LC-5-6-7 Processed to Closed Assessment | status_report | core |
| 20260607_Core_LC-9 Closure Report | closure_report | core |
| 20260607_Core_LCL Session Start Verification | status_report | core |
| 20260607_Core_Learning Candidate Flag Triage Proposal | proposal | core |
| 20260607_Core_Post-SOP-019 Session Start Verification | status_report | core |
| 20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4 | proposal | core |
| 20260607_Core_SOP-019 LC-6 Execution Briefing Rule | proposal | core |
| 20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards | status_report | core |
| 20260607_Core_Final Governance State Verification | status_report | core |
| 20260607_Core_DL Phase 1 Retroactive Iris Review | triage_document | core |
| 20260607_Core_DL Smoke Test Recovery Report | status_report | core |
| 20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal | proposal | core |
| 20260607_Core_Deliverable Lifecycle Backlog Processing Batch 1 Proposal | proposal | core |
| 20260607_Core_team-tasks-id-76-assessment | triage_document | core |

### Phase B — Triage of stale "ready" items (Owner decisions required)

Present the 16 "ready" items without owner_decision to the Owner with proposed actions:
- Archive directly (status reports, scan results with no extractable knowledge)
- Process into BKM/PKM (domain knowledge updates, research briefs, closure reports)
- Keep as reference / keep active (triage documents, architectuurschets)
- Mark as superseded (where a newer version exists)

Each decision is explicit and Owner-confirmed before any action runs.

### Phase C — Execute Batch 1 approved processing

Process the items approved in Phase B using SOP-017. Start with the 3 simplest items
(direct archive, no extraction). Generate one execution report per batch.

### Phase D — Governance hardening

1. Resolve task 75: write the Versioning Rule as a GL amendment (which GL TBD)
2. Resolve task 77: write the English-language rule for governance deliverables as GL amendment
3. Resolve task 78: write the versioning rule for proposal corrections as SOP-015 amendment
4. Add registration trigger to `/close-session` sweep: any unregistered folder in `Deliverables/`
   (excluding `Archive/`) that is older than 24h generates a sweep row with `state = draft`
5. Add stale alert: weekly sweep surfaces all items in "ready" older than 7 days

### Phase E — Automation (optional, after D is confirmed)

Build a classification helper that suggests `artifact_type` and `proposed_destination`
for new folders based on naming patterns. This is advisory only; Owner always confirms.

---

## 9. Proposed Governance Hardening Steps

In priority order:

1. **Add registration trigger to `/close-session`.**
   Currently `/close-session` sweeps unresolved team_tasks. It does not check
   `Deliverables/` for unregistered folders. Adding this check would have caught
   the 21 unregistered folders at the end of today's session.

2. **Write the Versioning Rule (task 75).**
   Define: within a deliverable folder, v-numbered files are versions of the same
   deliverable. A new folder is created only when the topic or scope changes, not
   when a correction is made. This prevents the proliferation of near-duplicate folders.

3. **Write the English-language rule for governance deliverables (task 77).**
   All governance deliverable filenames and folder names to be in English.

4. **Add stale detection to the Weekly Sweep Rule.**
   The existing CLAUDE.md Weekly Sweep Rule covers `team_tasks` older than 7 days.
   It should also surface `deliverable_lifecycle` rows in "ready" state older than 7 days.

5. **Process the 16 ready items (Phases B and C above).**
   Completing the first full lifecycle cycle proves the model works end-to-end.

6. **Add `last_reviewed_at` column to `deliverable_lifecycle`.**
   Enables stale detection without requiring a full table scan of team_tasks.

---

## 10. Recommended First Bounded Implementation Step

**Phase A: Register the 21 unregistered folders.**

Rationale:
- DB writes only — no file moves, no folder renames, no archive actions
- Fully reversible: rows can be deleted if a classification is wrong
- Immediately brings the DB back in sync with the folder state
- Creates the accurate baseline needed for all subsequent cleanup decisions
- Does not require Owner pre-approval of individual processing decisions —
  just classification into the DB with `state = ready` and a proposed destination

**Success criterion:** `deliverable_lifecycle` table has 42 rows (21 existing + 21 new).
All 38 active folders appear in the DB. Archive-only items confirmed absent from active list.

**What this step does NOT do:**
- Does not move, rename, or delete any folder
- Does not extract knowledge into PKM or BKM
- Does not close or process any item
- Does not modify any SOP, GL, or CLAUDE.md

**After Phase A:** Owner reviews the registered table. For any misclassified rows,
Owner corrects before Phase B begins.

---

## 11. Exact Next Prompt for Owner Review

Paste this prompt exactly to start Phase A execution:

```
Register the 21 unregistered active deliverable folders into the deliverable_lifecycle
database table. This is Phase A of the Deliverable Lifecycle Hardening plan approved by
the Owner on 2026-06-07.

Use the classification table from the discovery deliverable at:
Deliverables/20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal/deliverable-lifecycle-hardening-discovery-v01.md
Section 8, Phase A.

For each of the 21 folders: INSERT one row into deliverable_lifecycle with:
- artifact_name = folder name (exact)
- artifact_type = as per classification table
- state = 'ready'
- proposed_destination = 'Pending triage — see Phase B'
- destination_domain = 'core' (all 21 are Core domain)
- processing_notes = NULL
- superseded_by = NULL
- source_session = '2026-06-07-sop019-lc-chain'
- agent = 'larry'
- registered_at = datetime('now')
- state_changed_at = NULL
- processed_at = NULL
- owner_decision = NULL
- owner_decision_at = NULL

After inserting all 21 rows: verify by querying total row count and listing all new rows.
Report the result to the Owner.

Batch-stop rule: if any INSERT fails or produces an error, stop immediately and report
the failure before proceeding to the next row.

No file writes. No file moves. No archive actions. DB writes only.
```

---

Delivered on: 2026-06-07
Delivered at: Larry, Team Orchestrator
