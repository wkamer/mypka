# Deliverable Lifecycle — Owner Usability Assessment

**Date:** 2026-06-08
**Prepared by:** Larry
**Status:** Read-only assessment — no implementation, no amendments, no migrations
**Scope:** Owner-facing usability of the Deliverable Lifecycle as currently implemented

---

## 1. Current State Snapshot

| Metric | Value |
|---|---|
| Active deliverable folders | 45 |
| Archived deliverable folders | 19 |
| Folders created on 2026-06-07 alone | 30+ |
| Folders with a visible lifecycle state | 0 |
| Navigational index or dashboard | None |
| Workstream grouping mechanism | None |
| Owner decision visibility at folder level | None |
| README.md content | Minimal; stale naming convention |

---

## 2. Assessment by Area

### 2.1 Deliverable Folder Discoverability

**Rating: Poor**

The Deliverables folder is a flat list of 45+ folders sorted by date prefix. Finding a specific deliverable requires scrolling the full list and reading each name. There is no grouping, no filter, no search surface beyond the file system.

The naming convention `YYYYMMDD_Domain_Description` provides a date and domain signal, but:

- 30+ folders share the same date prefix (2026-06-07)
- Most active folders share the same domain (Core)
- The description is the only differentiator, and descriptions are inconsistently abbreviated (LC, DL, DLH, SOP-019)

The Owner cannot scan the folder list and quickly locate a specific deliverable without prior context.

---

### 2.2 Deliverable Inventory Visibility

**Rating: None**

There is no inventory mechanism. No index file. No dashboard. No generated report. The Owner has no instrument to view the full set of deliverables in a structured, filtered, or summarized form.

The only available view is `ls /opt/myPKA/Deliverables/` — a raw folder list.

---

### 2.3 Active vs Completed vs Archived Work Identification

**Rating: Not possible from folder layer**

Per GL-017 principle P13, lifecycle state is recorded in execution reports, not written into source files. This is correct governance design. The consequence is that there is no visible indicator on any deliverable folder that distinguishes:

- Active deliverables (Accepted as Done, pending lifecycle decision)
- Archived deliverables (moved to `Archive/`)
- Parked or Deferred deliverables
- Superseded deliverables

A deliverable sitting in the active folder may be:
- Awaiting an Owner lifecycle decision
- Pending a specialist action
- Fully processed and ready to archive
- Superseded by a newer version

The Owner cannot determine any of this without opening the deliverable and cross-referencing team_tasks and execution reports.

The archive is the only structural state signal — the `Archive/` subfolder. Everything outside it is undifferentiated.

---

### 2.4 Owner Decision Visibility

**Rating: Zero at deliverable layer**

Pending Owner decisions are tracked in `team_tasks` (team-knowledge.db). They are surfaced during session starts via the daily planning routine. They are not surfaced at the Deliverables layer.

There are currently open tasks directly tied to deliverable decisions:

| Task ID | Title | Status |
|---|---|---|
| 87 | Determine artifact_type migration sequence | open |
| 81 | Batch 3 write-list — deferred pending Q1 and Q2 | open |
| 80 | Write lc-triage-write-plan-v02.md | open |
| 77 | Graduation candidate 1 — GL amendment | open |
| 75 | Deliverable Folder and Versioning Rule | open |

If the Owner navigates to `Deliverables/`, none of this is visible. The Owner must know to check team_tasks separately.

---

### 2.5 Relationship Between Deliverables in the Same Workstream

**Rating: Invisible**

Many deliverables belong to the same workstream (Deliverable Lifecycle Hardening, LC Lifecycle Phase 1, SOP-019). From the folder list, this relationship is only partially visible through shared name fragments — and only to a reader who already knows the workstream context.

Examples: there are at minimum 15 folders related to the Deliverable Lifecycle Hardening initiative. They are interleaved with unrelated folders and cannot be grouped, filtered, or navigated as a set.

There is no parent-child relationship, no workstream tag in the folder name, and no cross-reference index that links them.

---

### 2.6 Deliverable Lifecycle Navigation

**Rating: Requires external context**

To understand the lifecycle state of any deliverable, the Owner must:

1. Identify the deliverable folder
2. Open the folder and locate the main file
3. Locate the relevant execution report (which may be a separate folder)
4. Cross-reference team_tasks for pending decisions
5. Cross-reference session logs for decisions made in prior sessions

This is a 3-5 step manual lookup for a single deliverable. With 45 active folders and multiple active workstreams, this is not viable as routine operation.

---

### 2.7 Deliverable Cleanup and Archive Usability

**Rating: Procedurally defined; operationally difficult**

SOP-017 defines formal archiving procedure (EX-6). The procedure is correct. The operational problem is upstream: the Owner cannot determine which deliverables are candidates for archiving without first reconstructing lifecycle state.

The current cleanup workflow is:
1. Identify archivable deliverables (requires state knowledge — not surfaced)
2. Prepare a formal proposal (requires knowing all cross-references — requires reading multiple files)
3. Get Owner approval
4. Execute the archive move

Step 1 alone requires substantial manual effort. As the folder count grows, the friction compounds.

---

### 2.8 Governance vs Owner Usability Optimization

**Finding: The current system is optimized for governance correctness, not Owner usability**

This is not a design flaw. It is a deliberate trade-off.

The Deliverable Lifecycle governance (GL-017, SOP-017, GL-016, SOP-016) was designed to ensure:
- State transitions require explicit decisions
- No state is implicitly assumed
- All governance records are auditable
- Knowledge extracted from deliverables lands in canonical locations

This is correct. The governance design should not be changed.

The usability gap is a separate layer problem. The governance layer produces correct records. The usability layer should surface those records to the Owner in a navigable form. That layer does not currently exist.

The symptom: the Owner can no longer efficiently answer basic operational questions without manual inspection of many files.

---

### 2.9 Is a Dashboard, Index, or Workstream View Warranted?

**Finding: Yes — volume has crossed the manual navigation threshold**

The threshold was crossed at approximately 15-20 active folders. At 45 active folders with multiple concurrent workstreams, manual navigation is no longer a viable operating mode.

A summary mechanism is warranted. The mechanism should:

- Be generated from existing data (not require manual maintenance)
- Surface: active deliverables, workstream grouping, pending Owner decisions, archive candidates
- Not add governance overhead
- Not require new governance instruments to maintain

---

### 2.10 Solution Mechanism

**Finding: A reporting/indexing layer is the right mechanism — not additional governance**

The usability problem is a visibility problem, not a governance problem. Adding governance rules to address it would make the governance system heavier without solving the underlying visibility gap.

The correct mechanism is a lightweight reporting layer that reads what already exists (team_tasks, folder structure, naming conventions) and surfaces it in an Owner-readable form.

---

## 3. Solution Options

### Option A — Auto-Generated Deliverable Index (Markdown report)

A script reads the Deliverables folder structure and team_tasks, groups deliverables by workstream code, flags pending Owner decisions, and writes a `Deliverables/INDEX.md`.

The index is generated on session start or on demand. Larry runs it as part of the session start sweep.

**Pros:** Always current. No manual maintenance. Surfaces pending decisions automatically.
**Cons:** Requires workstream grouping signal in folder name or database. Currently missing.
**Effort:** Medium — requires workstream tag in database or naming convention.

---

### Option B — Deliverable Registry (database table)

A `deliverables_registry` table in team-knowledge.db tracks: folder path, workstream, lifecycle state, Owner decision pending, last updated.

Every deliverable creation and lifecycle transition writes a row. The registry drives the index and the session start report.

**Pros:** Queryable. Single truth source for state. Enables Owner decision reports, archive candidate reports.
**Cons:** Requires consistent write discipline at deliverable creation and lifecycle transition points.
**Effort:** Medium-high — database schema, write discipline enforcement, agent briefing updates.

---

### Option C — Workstream Code in Folder Name

Add a short workstream code as the fourth segment of the folder name:
`YYYYMMDD_Domain_WorkstreamCode_Description`

Example: `20260607_Core_DLH_LC-9 Closure Report`

All DLH deliverables sort together. File system view becomes a workstream view.

**Pros:** No tooling required. Immediate discoverability improvement. Works with any file browser.
**Cons:** Does not solve status visibility or Owner decision surfacing. Requires naming convention amendment. Retroactive alignment needed (already partially addressed in Task 86 context).
**Effort:** Low — naming convention amendment only.

---

### Option D — Combination: Workstream Code + Auto-Generated Index

Adopt Option C for folder naming AND Option A for reporting.

The workstream code in the folder name enables the auto-index to group deliverables correctly without a database. The auto-index surfaces pending decisions, active workstreams, and archive candidates.

**Pros:** Best coverage across all identified gaps. Naming is self-documenting; index is always current.
**Cons:** Requires both naming convention amendment (already in scope via Task 86) and script development.
**Effort:** Medium total — naming convention already being addressed, script is new work.

---

### Option E — Deliverable Registry + Auto-Generated Index + Workstream Code

Full combination: all three mechanisms.

Registry provides queryable state truth. Workstream code provides file-system discoverability. Auto-index surfaces the registry view as a readable report.

**Pros:** Most complete solution. Enables future automation (auto-archive proposals, decision reminders).
**Cons:** Highest implementation effort. Risks over-engineering for current scale.
**Effort:** High.

---

## 4. Recommendation

**Recommended option: Option D — Workstream Code + Auto-Generated Index**

Reasoning:

- Workstream code in folder names is already partially in scope (Task 86 addressed naming standards). It is the lowest-friction improvement with the highest discoverability gain.
- The auto-generated INDEX.md gives the Owner a single entry point without manual maintenance burden.
- No new governance instruments are required. The mechanism is a reporting layer, not a governance layer.
- Option E (full registry) is viable as a Phase 2 if the index proves insufficient, but it is not warranted now.

**What this does not solve:**

The pending Owner decisions (tasks 75, 77, 80, 81, 87) are a separate matter. They are tracked in team_tasks and should continue to be surfaced at session start. The index can surface a "pending decisions" section derived from team_tasks as a secondary output.

---

## 5. Recommended Next Step

Define and approve the Deliverable Dashboard specification:

1. Workstream code convention — naming rule extension (integrates with Task 86 outcome and GL-001/GL-004 amendments already proposed)
2. INDEX.md format specification — sections, grouping logic, pending decision surfacing
3. Script specification for auto-generation
4. Session start integration — where and how the index is regenerated

This is a Phase C of Deliverable Lifecycle Hardening. Scope is bounded: naming extension + one script + one markdown template. No governance amendments required beyond the naming convention already in motion.

---

Delivered on: 2026-06-08
Delivered at: Deliverables/20260608_Core_DL Usability Assessment Owner Perspective/dl-usability-assessment-owner-perspective.md
