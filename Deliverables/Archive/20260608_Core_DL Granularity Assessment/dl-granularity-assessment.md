# Deliverable Lifecycle — Granularity Assessment

**Date:** 2026-06-08
**Prepared by:** Larry
**Prerequisite:** Approved by Owner — DL Visibility Architecture Assessment (2026-06-08),
Option C (Hybrid) accepted as provisional preferred direction
**Status:** Read-only assessment — no implementation, no amendments, no migrations
**Scope:** Determine what types of outputs warrant their own deliverable lifecycle folder,
and whether current deliverable proliferation is caused by incorrect granularity rather
than — or in addition to — missing visibility tooling

---

## 1. The Central Question

The previous assessments identified 46 active deliverable folders as a navigation problem.
Two candidate explanations exist:

**Explanation A:** The folders are all correctly scoped. The system lacks visibility tooling
to navigate them. Fix: build the tooling.

**Explanation B:** Some folders should never have been folders. They are process artifacts
that belong inside an existing deliverable. Fix: define and apply a granularity rule.

**Finding: Both explanations are true. They are not mutually exclusive.**

The evidence for B is concrete and measurable. Approximately 17 of 46 active folders
contain outputs that should have been files within their parent deliverable. The June 7
spike of 30+ folders in a single day was driven primarily by this pattern.

Fixing granularity reduces the folder count directly. Fixing visibility tooling makes the
remaining folders navigable. Both are needed. Granularity is the simpler fix and delivers
immediate benefit without any tooling change.

---

## 2. Observed Folder Patterns

The 46 active deliverable folders fall into five observable patterns based on their
contents and purpose.

### Pattern 1: Multi-file initiative deliverable (correctly scoped)

Multiple files inside one folder: primary document, version iterations, Iris review
report(s), and/or execution report. The folder represents a complete unit of work
with an internal lifecycle.

Examples:
- `20260607_Core_SOP-019 LC-6 Execution Briefing Rule` — 5 files:
  initiation proposal v01/v02/v03 + Iris review + execution report
- `20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards` — 5 files:
  initiation proposal v01/v02/v03 + Iris review + execution report
- `20260607_Core_LC Naming Alignment Impact Assessment` — 5 files:
  impact assessment v02–v05 + v01
- `20260604_Core_Review Gate Protocol Triage` — 7 files:
  triage report + GL proposal v01/v02 + SOP proposal v01/v02 + implementation report
- `20260604_Core_Deliverable Lifecycle Knowledge Processing Triage` — 6 files:
  implementation report + GL proposal v01/v02 + SOP proposal v01/v02

**Verdict:** These are correctly scoped. They are multi-file workstream deliverables
with internal version control. The folder model (Task 85, Model A) was designed for this.

---

### Pattern 2: Standalone substantive output (correctly scoped)

Single markdown file containing a substantive knowledge product: a research brief,
a domain knowledge document, a personal plan, a diagnostic report. The output has
standalone reference value independent of any governance workflow.

Examples:
- `20260513_Geldstroom Regie_One-pager methodiek` — business methodology document
- `20260519_Kamer E-commerce_Remy Research Week 21` — research report
- `20260530_Personal_Blueprint weekschema en oefeningen` — personal plan
- `20260531_Personal_Health Monitoring Schema` — health reference
- `20260603_Core_B-021C Closure Record` — initiative closure record

**Verdict:** Correctly scoped. These are substantive outputs the Owner or team would
look up by name. Their lifecycle is independently meaningful.

---

### Pattern 3: Execution report as standalone folder (incorrectly scoped)

A single execution report file in its own folder. The execution report describes what
happened when another deliverable was implemented. Its sole purpose is to confirm
that a specific write action was authorized and completed.

Examples:
- `20260607_Core_LC Batch 1 Execution Report` — 1 file: confirms Batch 1 writes executed
- `20260607_Core_LC Batch 2 Execution Report` — 2 files: confirms Batch 2 writes executed
- `20260605_Core_SOP-017 Amendment Lifecycle Execution` — 1 file: confirms SOP-017
  amendment was implemented

These execution reports are audit trails for a parent action. They contain no
knowledge that would be independently looked up. The `LC Batch 1 Execution Report`
confirms that the `LC Batch 1 Write-List` was executed. Functionally, it is
an appendix to the write-list, not a standalone artifact.

**Verdict:** Incorrectly scoped. These should be files within the deliverable folder
they describe, not standalone folders.

---

### Pattern 4: Write-list / pre-execution planning tool as standalone folder (incorrectly scoped)

A write-list or scoping document that exists to authorize and structure a specific set
of write actions. It is a process instrument used during execution, not a standalone
knowledge product.

Examples:
- `20260607_Core_LC Batch 1 Write-List` — 1 file: write-list for 3 write actions
- `20260606_Core_LC Lifecycle Phase 1 Write-List v05` — 1 file: write-list for
  Phase 1 implementation

Write-lists are produced to satisfy the governance requirement (CAT-3 flow) that
actions be pre-authorized in a structured document. They are not outputs the Owner
would look up after execution is complete. Once the execution report confirms the
writes were executed, the write-list's standalone value is zero.

Note: `20260607_Core_LC Batch 2 Write-List` is an exception — it contains 5 files
including Iris reviews and version iterations. It evolved into a multi-version
reviewed document and is correctly scoped as Pattern 1.

**Verdict:** Incorrectly scoped (except when the write-list itself underwent iterative
review and became a Pattern 1 artifact).

---

### Pattern 5: In-process verification and state-check output (incorrectly scoped)

A single report produced to verify the system state at a specific moment in a workflow.
It answers "is the governance state correct at this point?" — a process control
question, not a knowledge question.

Examples:
- `20260607_Core_Final Governance State Verification` — end-of-session state table
- `20260607_Core_Post-SOP-019 Session Start Verification` — pre-work state check
- `20260607_Core_LCL Session Start Verification` — session start verification
- `20260607_Core_LC-5-6-7 Processed to Closed Assessment` — state transition check
- `20260607_Core_team-tasks-id-76-assessment` — assessment of a single team_task
- `20260607_Core_DL Smoke Test Recovery Report` — incident report for a write error

These outputs were produced because the governance flow required a moment-in-time
state record before proceeding. They are internal process documentation. The
`Final Governance State Verification` is a table of LC states at session end — this
belongs in the session log, not in a deliverable folder.

**Verdict:** Incorrectly scoped. These should be sections within a session log, sections
within the parent process deliverable, or files within the deliverable they serve.

---

### Pattern 6: Single-step process proposal without follow-through (borderline)

A single-file proposal produced for one step in a larger governance flow, where the
proposal was not independently reviewed by Iris and did not generate a separate
execution report.

Examples:
- `20260607_Core_Auto-Processing Deliverable Lifecycle Discovery` — 1 file: discovery
  proposal for the auto-processing initiative
- `20260607_Core_Auto-Processing Deliverable Lifecycle Phase 1 Design` — 1 file:
  design proposal for Phase 1
- `20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal` — 1 file: test plan
- `20260607_Core_SOP-019 Initiation Proposal Learning Candidate 4` — 1 file:
  initiation proposal for one track
- `20260607_Core_LC-4 SOP-019 Amendment Retrospective Completion` — 1 file:
  retrospective assessment for LC-4
- `20260604_Core_Graduation Candidate Parked - Context-mode MCP Fix` — 1 file:
  parking note

These outputs served one decision point in a larger flow. The `Discovery` and `Phase 1
Design` proposals are phases of the auto-processing initiative — they could have been
files within a single `Auto-Processing Initiative` folder.

**Verdict:** Borderline. The current system produces one folder per process step within
a larger initiative. This is the core driver of the June 7 spike. The correct model:
one folder per initiative, with phase proposals as files within it.

---

## 3. Quantified Impact

| Pattern | Description | Count | Verdict |
|---|---|---|---|
| 1 | Multi-file initiative deliverable | ~11 | Correctly scoped |
| 2 | Standalone substantive output | ~8 | Correctly scoped |
| 3 | Execution report as standalone folder | ~3 | Incorrectly scoped |
| 4 | Write-list as standalone folder | ~2 | Incorrectly scoped |
| 5 | In-process verification / state check | ~6 | Incorrectly scoped |
| 6 | Single-step proposal (borderline) | ~6 | Borderline — case-by-case |
| — | Empty folder | 1 | Structural gap |

Patterns 3, 4, 5 total: approximately 11 incorrectly scoped folders.
Pattern 6 borderline: approximately 6 folders, of which most are incorrectly scoped.

Estimated reducible folder count: **14–17 of the 46 active folders** should not be
standalone lifecycle artifacts under a correct granularity rule.

If the granularity rule had existed on June 7, the day's folder creation would have
been approximately 16 instead of 30+.

---

## 4. The Root Cause

The governance framework (SOP-019, SOP-017, and the CAT-3 authorization flow) mandates
outputs at each procedural step. Every mandate produces an output. The framework does
not define whether a mandated output is a standalone deliverable folder or a file within
an existing folder.

In the absence of a granularity rule, the default behavior is: every output gets its
own folder. This is the correct behavior for Pattern 1 and Pattern 2 outputs — and
the incorrect behavior for everything else.

The proliferation is not random. It follows the governance procedure structure exactly.
Each LC had an initiation proposal. Each initiation proposal had an Iris review. Each
Iris review had an execution report. If each of those is a folder, one LC generates
3–4 folders. Five LCs = 15–20 folders. That is what happened on June 7.

The fix is not to reduce governance output. The fix is to define where each output
type lands relative to its parent deliverable.

---

## 5. Proposed Granularity Test

A deliverable warrants its own lifecycle folder when it satisfies at least one of:

| Criterion | Description |
|---|---|
| Standalone reference value | The Owner or a specialist would look up this output by name, independently of any parent process |
| Independent approval event | The Owner made an isolated accept/reject decision on this specific output, not as a step within a larger flow |
| Persistent citation function | Other deliverables, SOPs, or GLs reference this output by folder name |
| Substantive knowledge product | The output contains knowledge extracted into the knowledge base under its own identity |

An output remains a file within an existing deliverable when it satisfies one of:

| Criterion | Description |
|---|---|
| Version iteration | The same output in a later version (v01 → v02 → v03) |
| Supporting review | An Iris review, pre-review checklist, or review report for the primary output |
| Execution confirmation | A record that a specific write action was authorized and completed |
| Pre-execution planning tool | A write-list, scoping document, or authorization packet for a defined set of writes |
| Process state check | A verification table or state report produced to confirm conditions at a workflow step |
| Phase output within an initiative | A discovery, design, or scoping output serving one phase of a larger workstream — unless that phase was independently approved by the Owner as a standalone deliverable |

---

## 6. Governance Impact

This granularity distinction does not exist in any current governance instrument.
GL-017 defines what a deliverable is (Section 2: scope) but does not define what
distinguishes a primary deliverable from a supporting artifact within one.

SOP-017 requires execution reports but does not specify whether execution reports
are standalone deliverable folders or files within the deliverable they describe.

SOP-019 requires initiation proposals and execution reports per track but does not
specify their folder placement.

**What governance change is needed:**

One addition to GL-017: a section defining the granularity test — specifically,
what qualifies as a primary deliverable folder versus a supporting artifact file.
This is an additive amendment, not a change to existing principles.

One addition to SOP-017: clarify that execution reports are files within the
deliverable they describe (unless the execution report itself is a substantive
governance record warranting independent lifecycle tracking).

One addition to SOP-019: clarify that initiation proposals and execution reports
for a track are files within the track's primary deliverable folder.

These amendments are bounded and non-conflicting with existing principles.

---

## 7. Lifecycle Impact

**On existing folders:** No migration required. The 14–17 incorrectly scoped folders
already exist and are registered in the `deliverable_lifecycle` table. Retroactive
migration would create more churn than value. They remain as-is.

**On new deliverables:** The granularity rule, once defined, applies to all new
output production. The folder creation reduction takes effect immediately on the
next governance procedure execution.

**On the registry:** The granularity rule reduces the number of registry rows that
need to be created per governance procedure. Currently, one SOP-019 track generates
3–5 registry rows. Under the corrected rule, it generates 1 row (the primary track
deliverable folder) with supporting files inside.

**On SOP-017 lifecycle processing:** Execution reports that are correctly scoped as
files within a parent folder do not require their own lifecycle processing. The parent
deliverable's lifecycle processing covers them. This reduces the SOP-017 trigger
surface significantly.

---

## 8. Owner Usability Impact

**Folder count reduction:** Immediate and significant. Approximately 14–17 fewer
folders on day one of rule application. The June 7 spike pattern (30+ folders for
one governance initiative) becomes approximately 15 folders for the same scope.

**Findability improvement:** Initiative work is consolidated. Instead of 10 folders
spread across an initiative's lifecycle, the Owner sees 1–2 folders per initiative
with all supporting files inside. The SOP-019 LC-6 track is visible as one folder
with its complete history inside, not as 3–4 folders that must be mentally assembled.

**Prerequisite for the INDEX.md:** The Option C hybrid reporting layer (from the
Visibility Architecture Assessment) becomes more effective when each folder represents
a genuine unit of work. An INDEX.md built on correctly scoped folders gives an accurate
workstream view. An INDEX.md built on over-granular folders produces noise.

**The combined effect:** Granularity correction + visibility tooling delivers a
multiplicative improvement. Granularity correction alone reduces folder count to
navigable scale. Visibility tooling makes the reduced count actively navigable.
Either alone is partial. Both together solve the Owner usability problem.

---

## 9. Relationship to Option C (Hybrid Architecture)

The granularity assessment changes the Option C implementation scope:

**Before this assessment:** Option C required a workstream code in folder names to
group related folders. The reporting layer would aggregate 5–10 folders per workstream.

**After this assessment:** If granularity is corrected, many of those 5–10 folders
become files within 1–2 folders. The workstream grouping problem is partially solved
by the folder structure itself, not only by the reporting layer.

**Implication:** The Option C specification should address granularity first. The
workstream code convention and reporting layer are still needed — but they operate on
a leaner, more correctly scoped folder set. The combination is more robust.

---

## 10. Recommendation

**Finding:** Current deliverable proliferation is caused by both incorrect granularity
AND missing visibility tooling. Granularity is the larger driver of the June 7 spike
and is the simpler fix.

**Recommended action sequence:**

1. Define and add the granularity test to GL-017 (additive amendment — no existing
   principles changed). This is the first governance gate before any implementation.

2. Apply the corrected granularity rule to all new output production going forward.
   No retroactive migration.

3. Proceed with Option C (Hybrid) implementation on the leaner, correctly scoped
   folder set.

**What this assessment does NOT recommend:**

- Removing any existing folders (they remain as-is under their current lifecycle state)
- Reducing the governance output requirements of SOP-019, SOP-017, or the CAT-3 flow
- Skipping the granularity fix and proceeding directly to Option C tooling

The granularity fix is a precondition for Option C to deliver its full benefit. Building
the INDEX.md and reporting layer on an over-granular folder set solves the symptom
without addressing the cause.

---

Delivered on: 2026-06-08
Delivered at: Deliverables/20260608_Core_DL Granularity Assessment/dl-granularity-assessment.md
