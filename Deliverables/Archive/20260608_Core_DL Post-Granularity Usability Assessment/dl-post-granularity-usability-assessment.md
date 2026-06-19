# Deliverable Lifecycle — Post-Granularity Usability Assessment

**Date:** 2026-06-08
**Prepared by:** Larry
**Status:** Read-only assessment — no implementation, no amendments, no migrations
**Scope:** Assessment of remaining Owner usability gaps in the Deliverable Lifecycle system
after implementation of the Granularity Rules (GL-017 amendment, SOP-017 Section 4a,
SOP-019 amendment, CLAUDE.md Granularity Gate).

**Prerequisite assessments:**
- Deliverable Lifecycle — Owner Usability Assessment (2026-06-08) `20260608_Core_DL Usability Assessment Owner Perspective`
- Deliverable Lifecycle — Granularity Assessment (2026-06-08) `20260608_Core_DL Granularity Assessment`
- Deliverable Lifecycle — Visibility Architecture Assessment (2026-06-08) `20260608_Core_DL Visibility Architecture Assessment`

---

## 1. What the Granularity Rules Implemented

The following instruments were amended and are now active:

- **GL-017 Section 2:** Added G1/G2/G3 granularity criteria and the output-type placement reference table
- **SOP-017 Section 4a:** Added the operational output-type placement reference table
- **SOP-019:** Added granularity gate step before any new folder creation in governance tracks
- **CLAUDE.md (Larry):** Added mandatory Granularity Gate with violation trigger

**What the implementation established:**

| Area | What changed |
|---|---|
| Folder creation discipline | Every folder creation now requires an affirmative G1 answer. Default is G2 (file inside existing folder). |
| Supporting artifact placement | Execution reports, write-lists, verification reports, state checks, incident reports, correction notes, and phase documents now go inside existing folders, not in their own folders. |
| Initiative consolidation | A governance track that previously produced 5–10 folders now produces 1–2 folders with all supporting files inside. |
| Folder count | Estimated reduction: 14–17 fewer active folders on day one. The June 7 spike (30+ folders for one initiative) becomes approximately 15 folders for the same scope. |
| Reporting layer prerequisite | Each remaining folder now represents a genuine unit of work. INDEX.md generation becomes meaningful. |

---

## 2. Assessment by Usability Area

### 2.1 Deliverable Discovery

**Before granularity rules:** 46+ active folders in a flat list. Browsing `ls Deliverables/` was the only discovery mechanism. No grouping, no search, no index.

**After granularity rules:** ~32 active folders in a flat list. Browsing `ls Deliverables/` is still the only discovery mechanism.

**What changed:** Folder count reduced. Signal-to-noise improved.

**What did not change:** No INDEX.md. No search mechanism. No grouped view. Discovery still requires scrolling a flat folder list and mentally parsing `YYYYMMDD_Domain_Description` names.

**Gap status:** Unsolved. Reduced in severity.

---

### 2.2 Deliverable Navigation

**Before granularity rules:** No single entry point. No INDEX.md. No workstream code in folder names. Related folders must be mentally assembled.

**After granularity rules:** Same. The Granularity Gate consolidates within-initiative supporting artifacts but adds no navigation layer.

**What changed:** Intra-initiative navigation improved (supporting files now inside parent folders rather than scattered as siblings). Cross-initiative navigation is unchanged.

**What did not change:** No INDEX.md. No workstream code in folder names (Task 86 is open). No path from "I need the Phase 1 write-list for LC track" to finding it without scanning.

**Gap status:** Unsolved. Intra-initiative navigation partially improved as a side effect of consolidation.

---

### 2.3 Active Work Visibility

**Before granularity rules:** Lifecycle state (Active / Parked / Deferred / Accepted as Done) not visible from folder name or location. GL-017 Section 3 defines states; states are recorded only in execution reports.

**After granularity rules:** Same. The Granularity Gate does not add any state signal to folder names or the folder structure.

**What changed:** Nothing for state visibility.

**What did not change:** To determine whether a deliverable is active, parked, or done, the Owner or agent must open the folder and read the execution report. There is no folder-level or structure-level state signal.

**Gap status:** Unsolved.

---

### 2.4 Pending Decision Visibility

**Before granularity rules:** No automated mechanism to surface deliverables awaiting Owner decision. team_tasks tracks delegations but no session-start query flags pending decisions at the deliverable level.

**After granularity rules:** Same. The Granularity Gate is a creation-time rule only.

**What changed:** Nothing for pending decision visibility.

**What did not change:** No session-start surfacing of "X deliverables need Owner decision." No query that surfaces which deliverables have `owner_decision = None` in the registry. The 92% `owner_decision = None` rate in the registry (identified in the Visibility Architecture Assessment) remains.

**Gap status:** Unsolved.

---

### 2.5 Workstream Visibility

**Before granularity rules:** No workstream code in folder names. 5–10 folders per initiative, spread across the Deliverables folder, must be mentally assembled by the Owner.

**After granularity rules:** Reduced to 1–2 folders per initiative (consolidation). No workstream code added. Still no grouping signal.

**What changed:** The folder count per initiative dropped significantly. Mental assembly effort reduced proportionally. Task 86 (workstream code in folder names) remains open.

**What did not change:** No explicit grouping signal in folder names. Identifying all folders belonging to "DL Hardening" or "SOP-019 LC track" still requires reading and mentally parsing all folder names.

**Gap status:** Partially improved (fewer fragments). Not solved (no grouping signal).

---

### 2.6 Archive Visibility

**Before granularity rules:** Active vs archived distinction inferable from folder location (Deliverables/ vs Deliverables/Archive/). No mechanism to surface archive candidates (Accepted as Done + eligible for archiving).

**After granularity rules:** Same. The Granularity Gate does not affect archive logic.

**What changed:** Nothing for archive visibility.

**What did not change:** No archive candidate report. No automatic surfacing of deliverables that should be archived. The Archive/ folder exists and is used, but candidates are not surfaced proactively.

**Gap status:** Partially solved by existing SOP-017 archiving rules. Archive candidate surfacing remains unsolved.

---

### 2.7 Deliverable Lifecycle Reporting

**Before granularity rules:** No INDEX.md. No session-start briefing. Registry (`deliverable_lifecycle`) exists with state vocabulary mismatch (`ready`/`active` vs GL-017 states) and 4-folder coverage gap.

**After granularity rules:** Same. The Granularity Gate does not add any reporting output.

**What changed:** The cleaner folder set makes future reporting more accurate. The INDEX.md reporting layer, when built, will reflect genuine units of work rather than process artifacts. This is a prerequisite improvement, not a reporting capability.

**What did not change:** No INDEX.md exists. No session-start briefing. No reporting script. Registry state vocabulary remains misaligned. No Owner-facing summary of deliverable portfolio state.

**Gap status:** Unsolved. Prerequisite (clean folder structure) is now met.

---

## 3. Solved vs Unsolved Matrix

| Usability area | Solved by Granularity Rules? | Remaining gap | Priority |
|---|---|---|---|
| Folder count / noise | Yes — fully solved | None | — |
| Agent folder creation discipline | Yes — fully solved | None | — |
| Supporting artifact placement | Yes — fully solved | None | — |
| Initiative consolidation | Yes — solved for future work | Retroactive consolidation not done | Low |
| Deliverable discovery | Partially — reduced count | No INDEX.md, no search | High |
| Deliverable navigation | No | No INDEX.md, no entry point, Task 86 open | High |
| Active work visibility | No | State invisible from structure | High |
| Pending decision visibility | No | No surfacing mechanism | High |
| Workstream visibility | Partially — fewer fragments | No grouping signal (Task 86 open) | High |
| Archive visibility | No | No archive candidate surfacing | Medium |
| Deliverable Lifecycle reporting | No (prerequisite met) | No INDEX.md, no script, registry misaligned | High |

---

## 4. Findings

**Finding 1 — Granularity Rules solved the supply-side problem.**

Before implementation, the system had no rule governing whether a process output became a folder or a file. The result was uncontrolled folder proliferation. The Granularity Rules eliminate this: every future folder creation is gate-checked against G1 criteria. The creation-time problem is solved.

**Finding 2 — The demand-side problem is entirely unsolved.**

The Owner cannot navigate, discover, or understand the deliverable portfolio from its structure alone. Folder count reduction improved the browsing experience, but the Owner still has no:
- Single entry point (no INDEX.md)
- Workstream grouping signal (Task 86 open)
- State signal (Active / Parked / Done invisible)
- Pending decision surfacing
- Archive candidate surfacing
- Lifecycle reporting at session start

**Finding 3 — The prerequisite is now met for the visibility layer.**

The Visibility Architecture Assessment recommended Option C (Hybrid): folder scan + registry + workstream grouping + INDEX.md. That architecture required correct folder granularity to produce a meaningful INDEX.md. That prerequisite is now satisfied. The Granularity Rules were a necessary first step. They are not sufficient on their own.

**Finding 4 — Task 86 and Task 87 remain open and are on the critical path.**

Task 86 (workstream code in folder names) enables the reporting layer to group deliverables by initiative without relying on name-inference heuristics. Task 87 (state vocabulary alignment) enables the registry to surface accurate lifecycle state. Both are prerequisites for the INDEX.md to be meaningful rather than a flat list with unknown-state entries.

**Finding 5 — The registry write discipline problem persists.**

The 92% `owner_decision = None` rate in the registry and the 4-folder coverage gap (identified in the Visibility Architecture Assessment) are not affected by the Granularity Rules. The registry cannot serve as a visibility layer until population discipline is enforced at deliverable creation time.

---

## 5. Recommended Next Step

Authorize Phase C of DL Hardening: define the Hybrid Implementation Specification.

The Visibility Architecture Assessment already specified this step in full. No additional research is required. The granularity prerequisite is now complete.

**Phase C scope (from Visibility Architecture Assessment Section 7):**

1. Schema addition: add `workstream_code` field to `deliverable_lifecycle` (Kai)
2. State vocabulary alignment: map existing `ready`/`active` rows to GL-017 states or interim state `pending_lifecycle_decision` (integrates with Task 87) (Kai)
3. Larry registration discipline: add row to `deliverable_lifecycle` at deliverable creation (CLAUDE.md addition, not a governance amendment)
4. Reporting script: folder scan + registry lookup + workstream grouping + pending decision surfacing + INDEX.md output (Kai)
5. Session start integration: auto-regenerate INDEX.md on session start (Kai + update to start-morning-routine skill or equivalent)

**This specification is bounded scope.** It does not require governance amendments beyond CLAUDE.md. It does not block on full migration completion. It delivers Owner usability improvement on first deployment.

**Sequencing constraint:** Task 86 (naming convention) should be resolved before or in parallel with Phase C step 4 (reporting script), so the script can use workstream codes for grouping rather than name-inference.

---

Delivered on: 2026-06-08
Delivered at: `Deliverables/20260608_Core_DL Post-Granularity Usability Assessment/dl-post-granularity-usability-assessment.md`
