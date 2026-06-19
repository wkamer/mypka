# Deliverable Lifecycle — Visibility Architecture Assessment

**Date:** 2026-06-08
**Prepared by:** Larry
**Prerequisite:** Approved by Owner — Deliverable Lifecycle Owner Usability Assessment (2026-06-08)
**Status:** Read-only assessment — no implementation, no amendments, no migrations
**Scope:** Architecture comparison of three visibility mechanisms for Owner-facing navigation,
status reporting, pending decisions, archive candidates, and workstream grouping

---

## 1. Pre-Conditions — What Already Exists

This assessment is grounded in observed system state, not hypothetical design.

### 1.1 The registry table already exists

The `deliverable_lifecycle` table in `team-knowledge.db` is populated with 48 rows. It has
the following schema:

| Field | Purpose |
|---|---|
| id | Row identifier |
| artifact_name | Folder name (key) |
| artifact_type | Classification: proposal, status_report, triage_document, etc. |
| state | Current lifecycle state |
| proposed_destination | Processing destination per SOP-017 |
| destination_domain | Routing domain per GL-015 |
| processing_notes | Free-text notes |
| superseded_by | Reference to superseding artifact |
| source_session | Session of origin |
| agent | Agent who registered the row |
| registered_at | Registration timestamp |
| state_changed_at | Last state transition timestamp |
| processed_at | Processing completion timestamp |
| owner_decision | Owner decision value |
| owner_decision_at | Decision timestamp |

A bootstrap script (`deliverable_lifecycle_bootstrap.py`) auto-classifies and registers
deliverable folders into this table. The script is idempotent.

### 1.2 Current registry population

| Metric | Value |
|---|---|
| Total rows | 48 |
| Folders on disk (active) | 46 |
| Registry coverage gap (on disk, not registered) | 2 folders |
| Registry ghost rows (in registry, folder in Archive/) | 4 rows |
| Rows with owner_decision recorded | 4 (8%) |
| Rows with owner_decision = None | 44 (92%) |

State distribution:

| State value | Count |
|---|---|
| ready | 38 |
| active | 5 |
| archived | 4 |
| superseded | 1 |

### 1.3 Critical gap: state vocabulary mismatch

The current registry uses its own state vocabulary (`ready`, `active`, `archived`,
`superseded`) that does NOT align with GL-017's canonical state model.

GL-017 post-acceptance primary states:

| GL-017 state | Definition |
|---|---|
| Accepted as Done | Owner accepted; lifecycle decision required |
| Superseded | Replaced by newer accepted version |
| Archived | Moved to Archive folder; formal procedure complete |
| Parked | Acknowledged but not actioned |
| Deferred | Valid but postponed |

The registry's `ready` and `active` states have no GL-017 equivalent. They are bootstrap
classifications, not governance states. 38 of 48 rows carry a state that does not exist
in the governing framework.

### 1.4 Task 87 is open

Task 87 ("Determine artifact_type migration sequence relative to naming standardization") is
open and directly addresses the artifact_type taxonomy. The state vocabulary misalignment
is related scope. Neither has been resolved.

### 1.5 What the registry does NOT currently track

- Workstream code or workstream grouping (no field exists)
- Pending Owner decisions (owner_decision field exists but is empty on 44 rows)
- Whether a deliverable is an archive candidate
- Whether a folder has been moved to Archive (4 ghost rows show this is not being maintained)

---

## 2. Option A — Folder Structure + Reporting Layer

### Description

The file system is the single source of truth. Existence is determined by folder presence.
Archive status is determined by location in `Archive/`. A reporting script reads the folder
list, team_tasks (for pending decisions), and session logs (for context), then generates
`Deliverables/INDEX.md` on session start.

The registry (`deliverable_lifecycle`) remains as a processing aid used during SOP-017
lifecycle execution, but does not drive the Owner-facing visibility layer.

### What this solves

- Workstream grouping (from workstream code in folder name, already in motion via Task 86)
- Pending Owner decisions (from team_tasks query)
- Active vs archived distinction (folder location)
- Single entry point for Owner navigation (INDEX.md)

### What this does not solve

- Lifecycle state visibility (Accepted as Done / Parked / Deferred not inferable from folder name)
- Artifact type visibility (proposal vs closure report vs execution report not visible without opening)
- Superseded deliverables (no folder-level signal)
- Relationship between workstream deliverables beyond name prefix matching

### Migration impact

None. No existing records to migrate. No schema changes. No governance amendments.
The bootstrap script and existing registry remain unchanged in their current role.

### Governance impact

None. GL-017 P13 (state in execution reports, not source files) is fully respected.
No new write obligations for any agent. SOP-017 is unchanged.

The INDEX.md is generated output, not a governance record. It does not require its own
lifecycle processing.

### Automation impact

Low. One script reads two sources (folder list + team_tasks). Output is a single markdown
file. Session start hook triggers generation. Script has no write obligations beyond
INDEX.md itself.

Risk: the reporting layer infers workstream from folder names. If naming is inconsistent
(e.g., "DLH", "DL Hardening", "Deliverable Lifecycle Hardening"), grouping breaks. The
script must be tolerant of naming variation.

### Owner usability impact

Moderate improvement. The Owner gets:
- Workstream-grouped folder list
- Pending decisions surfaced inline
- Active vs archived distinction

The Owner does NOT get:
- State per deliverable (which is Accepted as Done, which is Parked, which is Superseded)
- Artifact type per deliverable
- Whether a deliverable has been lifecycle-processed

### Summary assessment

Option A is the lowest cost path. It delivers meaningful usability improvement with no
governance or migration overhead. Its ceiling is determined by what can be inferred from
folder names and team_tasks — and that ceiling is below what the Owner needs as volume
continues to grow.

---

## 3. Option B — Deliverable Registry as Canonical Visibility Layer

### Description

The `deliverable_lifecycle` table becomes the authoritative source for Owner-facing state,
workstream, pending decisions, archive candidates, and artifact classification. The folder
structure remains the physical storage layer, but all meaningful metadata lives in the
registry. Reports are generated from registry queries. The folder list is secondary.

### What this solves

Everything identified in the usability assessment:
- Lifecycle state visibility (explicit GL-017-aligned state per row)
- Workstream grouping (explicit workstream field)
- Artifact type per deliverable
- Pending Owner decisions (explicit field, maintained)
- Archive candidates (queryable: state = Accepted as Done + no recent activity)
- Superseded deliverables (explicit state + superseded_by field)

### Pre-conditions for Option B to be viable

1. State vocabulary must be aligned to GL-017 (migrate 48 rows; 38 `ready` rows need
   classification; `active` needs mapping; `archived` aligns; `superseded` aligns)
2. Write discipline must be enforced at deliverable creation (not only during lifecycle
   processing). Every new folder must produce a registry row at the moment of creation.
3. Archive sync must be enforced. When a folder moves to `Archive/`, the registry row must
   be updated in the same action.
4. A workstream field must be added to the schema.
5. An owner_decision field must be maintained, not defaulted to None.
6. Governance instruments must be updated: GL-017 and SOP-017 must require registry writes
   as mandatory steps.

None of these pre-conditions are currently met.

### Migration impact

Significant. The following must happen before Option B is operable:

| Action | Complexity | Risk |
|---|---|---|
| Align state vocabulary (48 rows) | Medium | Low if done carefully |
| Classify 38 `ready` rows into GL-017 states | Medium-High | Requires per-row judgment |
| Add workstream field to schema | Low | None |
| Register 2 missing folders | Low | None |
| Reconcile 4 ghost rows (archived folders) | Low | None |
| Amend GL-017 to require registry writes | Medium | Governance scope increase |
| Amend SOP-017 Phase 6 to include registry write | Medium | Procedural change for all agents |
| Enforce creation-time registration (all agents) | High | Discipline failure = invisible deliverables |

Total migration scope: multi-session effort involving Kai (schema change, script updates),
Larry (governance amendments via SOP-015), and all deliverable-producing agents (write
discipline enforcement).

### Governance impact

Material. Making the registry canonical requires amendments to:
- GL-017: new principle — registry is the canonical metadata layer
- SOP-017 Phase 6: registry write added as mandatory step in state recording
- All agent AGENT.md files that produce deliverables: creation-time registration required

The governance investment is justified if the registry becomes durable and well-maintained.
The governance investment is wasted if write discipline degrades — the registry becomes
a stale index that provides false confidence to the Owner.

### Automation impact

High value if maintained, high risk if not. A well-maintained registry enables:
- On-demand Owner dashboard (query by state, workstream, pending decision)
- Archive candidate surfacing (automated query: Accepted as Done + age threshold)
- Pending decision reminders (session start query: owner_decision = None + state = active)
- Workstream progress view (all registry rows for workstream code X)

The automation ceiling is much higher than Option A. But automation built on a registry
that degrades due to missing writes will mislead the Owner more than no automation at all.

### Owner usability impact

Highest ceiling of the three options. When the registry is maintained:
- The Owner can ask "what is the state of deliverable X" and get a direct answer
- The Owner can see all pending decisions in one query
- The Owner can see all archive candidates in one query
- Workstream progress is explicit, not inferred

When the registry is not maintained (gaps accumulate):
- The Owner sees a misleading view — some deliverables visible, others invisible
- False confidence is worse than acknowledged uncertainty

### Summary assessment

Option B offers the highest Owner usability ceiling. The path to get there is expensive and
requires sustained write discipline across all agents. The current registry state
(48 rows, 38 in non-GL-017 states, 44 with no owner decision, 6-row coverage gap) shows
that full registry discipline has not been achieved. Option B is the right destination but
is not the right immediate step.

---

## 4. Option C — Hybrid Approach

### Description

The folder structure is the SSOT for physical existence. The registry is the SSOT for
metadata (workstream, artifact type, state, pending decisions). The reporting layer reads
both and generates INDEX.md. Neither layer can contradict the other: if a folder exists
on disk, it is real; if the registry says it is in a state, that state is correct.

The key design decision in Option C: the registry does NOT need to be 100% populated to be
useful. A folder with no registry row is visible via the folder scan and reported as
"unregistered." A folder with a registry row gets its metadata shown. The INDEX.md degrades
gracefully.

### What this solves

Same as Option B when registry is populated. Degrades gracefully when registry is incomplete.
- Workstream grouping: explicit from registry (or inferred from name if unregistered)
- Lifecycle state: explicit from registry (or "unregistered" if missing)
- Pending decisions: from registry owner_decision field + team_tasks cross-reference
- Archive candidates: from registry state + folder location
- Artifact type: from registry artifact_type field

### The specific design

**Layer 1 — Folder structure:** canonical for existence and location.
- A folder on disk = a deliverable exists, regardless of registry state.
- A folder in `Archive/` = physically archived, regardless of registry state.

**Layer 2 — Registry:** canonical for metadata.
- Workstream code (new field)
- Artifact type (existing field, aligning to GL-017 vocabulary per Task 87)
- Lifecycle state (aligned to GL-017 per migration)
- Owner decision pending (boolean derived from owner_decision field)
- Authoritative marker (new boolean field)

**Layer 3 — Reporting script:** generates INDEX.md from both layers.
- For every folder on disk: lookup registry row. Show metadata if found; mark as unregistered if not.
- Group by workstream code.
- Surface pending decisions section.
- Surface archive candidates section.

### Registration discipline

Option C requires registration at creation time — but lighter than Option B. The requirement
is: create the folder, create the registry row with artifact_type and workstream. State can
remain unset until lifecycle processing happens. This is lower friction than requiring a
full GL-017 state at creation.

### Migration impact

Moderate. Less than Option B because:
- 38 `ready` rows do not need immediate GL-017 state classification — they can be reported
  as "pending lifecycle decision" until SOP-017 processing happens
- The workstream field needs to be added (schema change)
- Creation-time registration needs to become operational discipline (CLAUDE.md addition for
  Larry; no full SOP-017 amendment required immediately)
- Ghost rows (4 archived folders) and missing rows (2 folders) need reconciliation

The migration is bounded and can be done incrementally. It does not block the reporting
layer from being useful immediately.

### Governance impact

Minimal. No GL-017 amendment required immediately. The registry is an operational metadata
layer, not a governance layer. GL-017 P13 (state in execution reports) remains intact —
the registry reflects state derived from execution reports, it does not replace them.

One addition to Larry's CLAUDE.md: create registry row when creating deliverable folder.
This is operational discipline, not a governance rule change.

Future path to full Option B: if write discipline proves consistent over time, GL-017 can
be amended to formally designate the registry as canonical. That is a future governance
decision, not a precondition for Option C.

### Automation impact

High. The reporting script reads two sources (registry + folder scan) and produces one
output (INDEX.md). Graceful degradation means the script is always safe to run — it never
misleads, it only provides less information when registry coverage is incomplete.

Additional automation that becomes possible:
- Archive candidate report (state = Accepted as Done + age > threshold)
- Pending decision report (owner_decision = None + state in active states)
- Workstream progress view (all rows for workstream code X)
- Session start briefing: "X deliverables pending lifecycle decision, Y decisions pending
  Owner input"

### Owner usability impact

High, with graceful degradation. The Owner gets:
- Workstream-grouped view (from registry or name inference)
- Lifecycle state per deliverable where registry is populated
- Clear signal for unregistered deliverables (they appear as "pending registration")
- Pending Owner decisions surfaced
- Archive candidates surfaced

The Owner is never misled. An unregistered deliverable is labeled as such, not hidden.

### Summary assessment

Option C is the pragmatic path. It leverages what already exists (the registry, the
bootstrap script, the schema) without requiring governance amendments or full write
discipline enforcement before becoming useful. It degrades gracefully when registry
coverage is incomplete. It creates a natural migration path toward Option B as write
discipline matures.

---

## 5. Comparative Summary

| Dimension | Option A | Option B | Option C |
|---|---|---|---|
| State vocabulary alignment needed | No | Yes — all 48 rows | Yes — create GL-017 mapping |
| Schema change needed | No | Yes — workstream field | Yes — workstream field |
| Governance amendment needed | No | Yes — GL-017, SOP-017 | No (for now) |
| Write discipline required | None | Strict at creation + every transition | At creation only |
| Coverage gap handling | Folder scan is always complete | Gaps make layer unreliable | Graceful degradation |
| Migration effort | None | Multi-session, multi-agent | Bounded, incremental |
| Owner usability ceiling | Moderate | Highest | High |
| Owner usability floor | Moderate (folder scan always works) | Low (gaps mislead) | High (folder scan fallback) |
| Automation potential | Moderate | Highest | High |
| Risk of misleading the Owner | Low | High (if write discipline fails) | Low |
| Reversibility | Always reversible | Commits to registry as canonical | Reversible at each step |

---

## 6. Recommendation

**Recommended architecture: Option C — Hybrid**

The recommendation rests on three observations:

**First:** The registry already exists but is not in a state that can reliably serve as a
canonical visibility layer. Making it canonical now would commit the system to a discipline
that has not been validated at scale. The 92% `owner_decision = None` rate and the 4-folder
coverage gap are signals that write discipline at the registry layer is not yet consistent.

**Second:** Option C delivers the same Owner usability improvement as Option B for daily
navigation, without the governance amendments and migration overhead. The difference between
B and C is not visible to the Owner until edge cases arise — and edge cases are handled
gracefully in C (unregistered = labeled, not hidden) versus dangerously in B (unregistered
= invisible).

**Third:** Option C is the natural migration path to Option B. If registration at creation
becomes consistently practiced, and the state vocabulary is aligned as part of Task 87 scope,
Option B becomes reachable without a separate governance initiative. The decision to formally
designate the registry as canonical can be made once the write discipline has been validated.

Option A is not recommended because its ceiling is too low. As the deliverable volume grows,
name-inference-based grouping will produce false groupings and miss relationships. Explicit
workstream tagging in the registry is strictly superior.

---

## 7. Recommended Next Step

Define the Hybrid Implementation Specification (Phase C of DL Hardening):

1. Schema addition: add `workstream_code` field to `deliverable_lifecycle` (Kai)
2. State vocabulary alignment: map existing `ready`/`active` rows to GL-017 states or a
   defined interim state (e.g., `pending_lifecycle_decision`) — this integrates with Task 87
3. Larry operational discipline: register row at deliverable creation (CLAUDE.md addition,
   not a governance amendment)
4. Reporting script specification: folder scan + registry lookup + workstream grouping +
   pending decision surfacing + INDEX.md output
5. Session start integration: regenerate INDEX.md on session start

This specification is bounded scope. It does not require governance amendments, does not
block on migration completion, and produces Owner usability improvement on first deployment.

---

Delivered on: 2026-06-08
Delivered at: Deliverables/20260608_Core_DL Visibility Architecture Assessment/dl-visibility-architecture-assessment.md
