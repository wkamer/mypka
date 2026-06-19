# Deliverable Lifecycle Hardening — Phase B Addendum: Naming, Versioning, and File-Type Standardization

**Date:** 2026-06-07
**Author:** Larry
**Phase:** B Addendum — Naming and Versioning Triage
**Status:** Awaiting Owner Confirmation
**Companion document:** phase-b-triage-report-v01.md

---

## 1. Purpose

This addendum to the Phase B triage report establishes proposed standards for:

- Canonical Deliverables folder naming syntax
- Canonical deliverable file naming syntax
- Standard deliverable types and their file-suffix mapping
- Standard `artifact_type` values for `deliverable_lifecycle`
- Versioning syntax
- Same-folder version rules vs. new-folder rules
- Corrected versions vs. superseded versions
- Naming connections for specific report types
- Ownership routing (tasks 75, 77, 78, LC-10, or new candidate)
- Whether naming standardization must precede Batch 1 execution

This is a proposal only. No files are renamed, no GLs are updated, no DB values are changed
as part of this document.

---

## 2. Current State: The Naming Problem

### 2.1 Folder naming

The existing folder convention from CLAUDE.md is:

```
YYYYMMDD_Domain_Description
```

Examples from the active Deliverables folder:
```
20260513_Geldstroom Regie_One-pager methodiek
20260607_Core_LC Batch 2 Write-List
20260607_Core_Deliverable Lifecycle Hardening Phase B Triage
```

This pattern is structurally sound and consistently applied. The domain separator and
date prefix work. Issues are narrow:
- Descriptions use spaces (correct per CLAUDE.md) but casing is inconsistent (Title Case
  vs. all-caps abbreviations vs. mixed)
- Some descriptions contain Dutch words (e.g., "One-pager methodiek") — conflicts with the
  English system-names rule (task 77 scope)
- No type indicator in the folder name — a folder named "LC Batch 2 Write-List" gives the
  type, but "B-021C Closure Record" embeds the type differently. There is no enforced pattern
  for where the type word sits in the description.

### 2.2 File naming

The file naming landscape is the primary problem. A scan of all active deliverable folders
reveals six distinct patterns in concurrent use:

| Pattern | Example | Problem |
|---|---|---|
| Bare descriptive, no version | `report.md`, `rapport.md`, `closure-record.md` | No version, Dutch, no type |
| Date-embedded with version | `audit-status-report-2026-06-04-v02.md` | Date redundant (already in folder name) |
| Topic-type-version | `deliverable-lifecycle-gl-proposal-v01.md` | Best existing pattern |
| Semver style | `proposal-v0.1.md`, `proposal-v0.4.md` | Non-standard; mixes with v01 style |
| Versionless alongside versioned | `lc-batch2-write-list.md` + `-v03.md` + `-v04.md` | Ambiguous authoritative copy |
| Version gaps with no v01 | `-v02.md`, `-v03.md`, `-v04.md`, `-v05.md` with no v01 | History is incomplete |

None of these patterns are the result of a deliberate standard. They are accumulation artifacts
from multiple agents producing output without a shared file-naming rule.

### 2.3 artifact_type values currently in use

From `deliverable_lifecycle` (team-knowledge.db):

| Value | Count |
|---|---|
| domain_knowledge_update | 5 |
| research_brief | 1 |
| triage_document | 9 |
| closure_report | 3 |
| proposal | 12 |
| status_report | 9 |
| decision_record | 1 |

Missing from the DB but present in actual deliverable content:
- execution_report (LC Batch 1 and Batch 2 execution reports are typed as `status_report`)
- write_list (write-lists are typed as `proposal`, which is inaccurate)
- assessment (impact assessments and audit reports have no dedicated type)
- verification_report (session-start and post-execution verifications are typed as `status_report`)
- working_artifact (parking notes, intermediate analysis files have no dedicated type)

---

## 3. Proposed Canonical Folder Naming Syntax

**No change to the existing pattern.** The CLAUDE.md convention is correct:

```
YYYYMMDD_Domain_Description
```

Rules to clarify and enforce:

| Element | Rule |
|---|---|
| YYYYMMDD | Date the deliverable folder was created (not the work date, not the approval date) |
| Domain | Exactly one of: `Core`, `Personal`, `Kamer E-commerce`, `Geldstroom Regie` |
| Description | Title Case; English only (task 77 rule); spaces permitted; no underscores within description; no version number in folder name |
| Type indicator | Not required in folder name — type lives in the file name and the DB `artifact_type` field |
| Separator | Single underscore between date, domain, and description. No underscores within domain or description |

**Corrected examples:**
```
20260513_Geldstroom Regie_One-pager Methodology    ← English, Title Case
20260519_Kamer E-commerce_Remy Research Week 21    ← already correct
20260607_Core_LC Batch 2 Write-List                ← already correct
```

**Explicitly not permitted:**
```
20260513_GR_One-pager methodiek    ← domain abbreviation; Dutch description
20260607_core_lc-batch2-write-list ← lowercase; underscores in description
20260607_Core_LC_Batch_2_v01       ← version in folder name; underscores in description
```

---

## 4. Proposed Canonical File Naming Syntax

### 4.1 Standard pattern

```
<topic-slug>-<artifact-type-slug>-v<NN>.md
```

Where:

| Element | Rule |
|---|---|
| topic-slug | Kebab-case. Short noun phrase derived from the folder description. Omit the domain and date (already in folder). English only. |
| artifact-type-slug | One of the standard slugs from Section 5. Always present. |
| vNN | Zero-padded two-digit version number. Always starts at `v01`. |
| Extension | `.md` always. No `.txt`, no `.docx`. |

**Examples:**
```
lc-batch2-write-list-v01.md
deliverable-lifecycle-gl-proposal-v01.md
review-gate-protocol-sop-proposal-v02.md
b021c-closure-report-v01.md
umc-architecture-assessment-v01.md
lena-brief-health-domain-knowledge-output-v01.md
```

### 4.2 Single-file folders

A deliverable folder that contains exactly one artifact and has no iteration history (simple
one-off content output, not a governance artifact) may use a versionless primary file if
and only if:
- The artifact type is `knowledge_output`, `research_brief`, or `working_artifact`
- The folder will never go through a review cycle
- The Owner has not designated it as an authoritative governance reference

All governance artifacts (proposals, execution reports, write-lists, closure reports,
decision records, verification reports, assessments, triage reports) must carry a version
number. There is no exception.

### 4.3 What is not permitted

```
report.md              ← no topic, no type, no version
rapport.md             ← Dutch
closure-record.md      ← no version
proposal-v0.1.md       ← semver style
audit-status-report-2026-06-04.md  ← date embedded (redundant with folder name)
```

### 4.4 The authoritative copy problem

Several folders currently contain both a versionless file and multiple versioned copies
(e.g., `lc-batch2-write-list.md` + `lc-batch2-write-list-v03.md` + `-v04.md`). This
creates ambiguity about which file is authoritative.

**Rule:** The highest-numbered versioned file is always the current working version.
There is no separate "authoritative copy" or "final" file alongside the versioned series.
When an artifact reaches final approved state, that is recorded in `deliverable_lifecycle`
via the `Authoritative` lifecycle marker — not by creating a separate unversioned copy.

Existing versionless files alongside versioned series are legacy artifacts and should be
resolved during Batch 3 (archive after check) per the main triage report.

---

## 5. Standard Artifact Types

### 5.1 Standard type table

| File type slug | DB artifact_type | GL-017 category | Description |
|---|---|---|---|
| `proposal` | `proposal` | Proposals | Any artifact awaiting Owner approval before execution; GL/SOP change proposals, architecture proposals, design proposals |
| `write-list` | `write_list` | Working artifacts | Ordered list of write actions for a specific execution; always paired with an execution report |
| `execution-report` | `execution_report` | Execution reports | Post-execution confirmation of what was done, against which write-list, with what outcome |
| `closure-report` | `closure_report` | Closure reports | End of a project, task, LC item, or governance flow; includes decisions, learnings, open items |
| `triage-report` | `triage_report` | Triage reports | Analysis and classification output awaiting Owner decision; replaces the ambiguous `triage_document` |
| `assessment` | `assessment` | Working artifacts | Impact analysis, risk analysis, audit output, naming impact assessment |
| `decision-record` | `decision_record` | Decision packets | Record of Owner decision on a governance question; standalone or embedded in closure report |
| `verification-report` | `verification_report` | Status reports | Point-in-time state verification; post-execution check, session-start snapshot, smoke test result |
| `status-report` | `status_report` | Status reports | General status update not fitting a more specific type; use sparingly |
| `knowledge-output` | `domain_knowledge_update` | Domain knowledge | Domain knowledge artifact for BKM or PKM extraction; research output not classified as a brief |
| `research-brief` | `research_brief` | Domain knowledge | Research brief from Pax or domain specialist; structured for specialist ingestion |
| `working-artifact` | `working_artifact` | Working artifacts | Supporting material, intermediate output, parking notes; not governed by full lifecycle |

### 5.2 Migration notes for existing artifact_type values

| Current DB value | Proposed migration |
|---|---|
| `triage_document` | Rename to `triage_report` — 9 rows affected in current backlog |
| `status_report` used for execution reports | Reclassify to `execution_report` — affects IDs 27, 29, 33, 35, 37, 40, 41, 43 |
| `status_report` used for verifications | Reclassify to `verification_report` — affects IDs 35, 37, 41 |
| `proposal` used for write-lists | Reclassify to `write_list` — affects IDs 26, 28 |

This migration is a DB update only. No file moves. Proposed as Phase C work, not Batch 1.

### 5.3 Specific naming for common document pairs

Write-lists and their execution reports are always produced as a pair. Naming must make
the pairing explicit:

```
lc-batch1-write-list-v01.md           → DB: write_list
lc-batch1-execution-report-v01.md     → DB: execution_report
```

Proposals and their Iris reviews are always paired. Naming must reflect the subject:

```
gl-017-proposal-v01.md                → GL-017 proposal, version 1
gl-017-proposal-v02.md                → corrected version after review
iris-review-gl-017-proposal-v02.md    → Iris review of v02
```

Review reports reference their subject artifact in the topic slug:

```
iris-review-<subject-slug>-v<NN>.md
```

---

## 6. Versioning Rules

### 6.1 Version numbering syntax

```
v01, v02, v03 ... v99
```

- Zero-padded two digits only.
- Starts at `v01` always. There is no `v00` or `v0`.
- Semver (`v0.1`, `v1.0`, `v2.3`) is not permitted.
- Version suffix is part of the filename, not the folder name.
- Version numbers do not carry semantic meaning (major/minor/patch). Every iteration is
  simply the next number.

### 6.2 When a new version stays inside the same deliverable folder

A new version file is created in the same folder when:

1. **Iterative correction:** A factual error, scope correction, or review-cycle edit is made
   to an artifact still in progress. Example: `gl-017-proposal-v01.md` → review finds error
   → `gl-017-proposal-v02.md` in the same folder.

2. **Review cycle iteration:** SOP-015 Proposal Iteration Protocol requires a new version
   per review round. The proposal and all its iteration versions belong in the same folder.

3. **Companion document update:** An Iris review references `gl-017-proposal-v02.md`. If a
   new Iris review is run on `v03`, the new review file (`iris-review-gl-017-proposal-v03.md`)
   belongs in the same folder as all other artifacts for that proposal.

4. **Minor execution update:** An execution report contains a factual correction (wrong count,
   wrong DB id) discovered immediately after creation. Create `execution-report-v02.md` in the
   same folder.

**Rule:** Same deliverable subject + same governance flow = same folder.

### 6.3 When a new deliverable folder must be created

A new deliverable folder is created when:

1. **New phase of work:** A new governance phase begins based on a prior deliverable. Example:
   Phase A discovery → Phase B triage → these are separate folders because they are separate
   decision points, not iterations of the same artifact.

2. **Artifact type changes:** A proposal becomes an execution report. These are structurally
   different artifacts with different lifecycle states. New folder.

3. **Scope change after Owner rejection:** Owner rejects a proposal and requests a fundamentally
   different approach. A corrected minor version stays in the same folder. A new approach
   requiring a fresh proposal starts a new folder.

4. **New work session for a distinct artifact:** A new closure report, a new assessment,
   a new brief — if it is a new artifact rather than an iteration of an existing one, it gets
   a new folder.

5. **New date + new artifact:** When the same type of artifact is produced in a new session
   (e.g., a new write-list for a different batch), the new date and new purpose mean a new folder.

**Decision heuristic:** If the existing folder's date is the same and the artifact is a
direct iteration of what is already there, stay in the same folder. If the artifact represents
a new decision point, a new phase, or a structurally different output, create a new folder.

### 6.4 Corrected version vs. superseded version

These are fundamentally different concepts and must not be conflated.

**Corrected version** — same artifact, fixed content:
- An error or scope gap is found in an existing version.
- A new version file is created in the same folder (v02, v03, etc.).
- The prior version is retained — it is never deleted.
- The new version includes a `## Correction Note` section at the top, stating what changed
  and why. This section is mandatory.
- The `deliverable_lifecycle` DB entry is not changed — the folder, not the file, is the
  registered unit.
- Example: `lc-batch2-write-list-v04.md` corrects an error in `lc-batch2-write-list-v03.md`.
  Both files exist in the folder. v04 has a Correction Note.

**Superseded version** — earlier artifact replaced by a different artifact:
- A later deliverable in a different folder makes this deliverable obsolete.
- The superseded deliverable's folder is not touched.
- In `deliverable_lifecycle`, set `superseded_by` to the new artifact name.
- The `state` may be changed to `archived` (Batch 1 or Batch 2 action).
- No Correction Note is added to the original files — they are historical.
- Example: `20260604_Core_Deliverable Lifecycle Knowledge Processing Triage` is superseded
  by the current Phase B work. The Phase B folder is not the same folder. The old folder
  gets `superseded_by='20260607_Core_Deliverable Lifecycle Hardening Phase B Triage'`.

**Summary table:**

| | Corrected version | Superseded version |
|---|---|---|
| Same folder? | Yes | No — different folder |
| Old files kept? | Yes | Yes — folder not touched |
| New file created? | Yes — next version number | No — new folder is the replacement |
| Correction Note required? | Yes | No |
| DB change? | None (folder is the unit) | `superseded_by` + state change |
| Use case | Review cycle, error fix | Phase transition, approach change |

---

## 7. Naming Connections for Specific Document Types

### 7.1 Proposals

```
<subject-slug>-proposal-v<NN>.md
```

A proposal is any artifact presented to the Owner for approval before execution. This
includes GL proposals, SOP proposals, architecture proposals, and briefing proposals.

The `subject-slug` identifies what the proposal is for:
```
gl-017-proposal-v01.md             ← proposal to create GL-017
sop-015-amendment-proposal-v01.md  ← proposal to amend SOP-015
auto-processing-design-proposal-v01.md
```

### 7.2 Review reports (Iris reviews)

```
iris-review-<subject-slug>-v<NN>.md
```

The version number matches the subject artifact version being reviewed. If the proposal
is at v03 when reviewed, the review file is `iris-review-...-v03.md`. This makes the
pairing unambiguous.

```
iris-review-lc-batch2-write-list-v04.md
iris-review-gl-017-proposal-v02.md
```

### 7.3 Execution reports

```
<subject-slug>-execution-report-v<NN>.md
```

The subject slug references the write-list being executed:
```
lc-batch1-execution-report-v01.md
gl-017-execution-report-v01.md
```

Execution reports start at v01 and are only incremented for factual corrections, not for
subsequent executions. A subsequent execution of a different batch gets its own folder.

### 7.4 Closure reports

```
<subject-slug>-closure-report-v<NN>.md
```

The subject slug references what is being closed (project, task, LC):
```
b021c-closure-report-v01.md
lc-9-closure-report-v01.md
p-tricolarae-closure-report-v01.md
```

### 7.5 Verification reports

```
<subject-slug>-verification-report-v<NN>.md
```

Used for: post-execution checks, session-start state verification, smoke tests.
```
lc-phase1-verification-report-v01.md
session-start-governance-verification-report-v01.md
```

### 7.6 Assessments

```
<subject-slug>-assessment-v<NN>.md
```

Used for: impact assessments, audit outputs, risk analyses, naming impact analysis.
```
lc-naming-alignment-assessment-v01.md
umc-architecture-assessment-v01.md
task-76-assessment-v01.md
```

### 7.7 Decision records

```
<subject-slug>-decision-record-v<NN>.md
```

A standalone Owner decision on a governance question. When a decision record is embedded
inside a closure report, the separate file is not required. Use a standalone file when
the decision is significant enough to be referenced independently.
```
gl-017-sop-017-decision-record-v01.md
lifecycle-phase-b-decision-record-v01.md
```

### 7.8 Write-lists

```
<subject-slug>-write-list-v<NN>.md
```

Write-lists are versioned because they go through review cycles before execution. The
approved version is the one that gets executed. Each revision is a new version file.
```
lc-batch1-write-list-v01.md
lc-batch2-write-list-v04.md   ← four iterations before execution
```

---

## 8. Ownership Routing

### 8.1 Task 75 — Deliverable Folder and Versioning Rule

**Scope:** Task 75 ("Deliverable Folder and Versioning Rule — define and implement for
governance flows") directly owns the implementation of what this addendum proposes. The
task notes explicitly reference: versioned files (v1/v2), final summary, implementation
report, verification report, decision record, exception record.

**Decision:** This addendum is the triage and proposal phase that feeds Task 75.
Task 75 owns the implementation: identify the correct GL home, draft the exact amendment
text, run Iris review, get Owner authorization, execute the write. This addendum does not
close Task 75 — it provides the analysis that enables Task 75 to proceed.

### 8.2 Task 77 — English-language rule

**Scope:** Task 77 ("add English-language rule for governance deliverables") directly
intersects with file naming. Several current file names are Dutch (`rapport.md`,
`one-pager-structuur.md`). The naming standard proposed here requires English — but the
English-language rule in a GL must exist before the naming standard can reference it.

**Decision:** Task 77 is a prerequisite for the GL amendment that will codify the naming
standard. Task 77 should be executed before or simultaneously with the GL update for Task 75.
The two tasks may be batched into a single GL amendment proposal.

### 8.3 Task 78 — Versioning rule for corrections

**Scope:** Task 78 ("add versioning rule for governance proposal corrections to SOP-015
or appropriate GL") is directly addressed by Section 6.4 of this addendum. The rule
"corrections create a new version file; silent overwrite is not permitted" is specified here.

**Decision:** Section 6.4 (corrected vs. superseded version) is the content that Task 78
needs to formalize into a GL or SOP-015 amendment. Task 78 should consume Section 6.4 as
its source text during the proposal drafting phase.

### 8.4 LC-10 — Missing outcome artifact

**Scope:** LC-10 ("Option execution omitted required persisted outcome artifact when Owner
selected shorthand option") is about a different failure mode: an artifact was not created
at all, not that it was named incorrectly. However, LC-10 and the naming standard are
interdependent. If the naming standard is not in place, agents creating required artifacts
under the LC-10 resolution mechanism will create inconsistently named files.

**Decision:** LC-10 is independent of naming standardization but depends on it for clean
execution. LC-10's resolution mechanism (which defines when an artifact is "required")
should reference the naming standard as the format specification for required artifacts.
LC-10 does not own the naming standard; it consumes it.

### 8.5 New Learning Candidate

A new Learning Candidate is not recommended. The gap is already covered:
- Task 75 owns the folder/versioning rule implementation
- Task 77 owns the English-language rule
- Task 78 owns the correction-versioning rule
- LC-10 covers the missing-artifact failure mode

Adding a new LC would create overlap and split accountability. The three open tasks and
one captured LC are sufficient vehicles for the full scope of naming standardization.

### 8.6 Ownership summary

| Topic | Owner | Status |
|---|---|---|
| Folder naming syntax | Task 75 | Proposed here; Task 75 implements |
| File naming syntax | Task 75 | Proposed here; Task 75 implements |
| English-only file names | Task 77 | Prerequisite for naming GL; implement first |
| Correction versioning rule | Task 78 | Section 6.4 is the source text for Task 78 |
| artifact_type DB migration | Task 75 | Section 5.2 migration is part of Task 75 scope |
| Missing artifact obligation | LC-10 | Independent; consumes naming standard |
| No new LC needed | — | Coverage is complete across existing tasks |

---

## 9. Batch 1 Dependency Assessment

**Conclusion: Naming standardization is NOT a prerequisite for Batch 1 execution.**

Batch 1 consists of 19 items all going to `state='archived'` in `deliverable_lifecycle`.
The only writes are DB state changes. No new files are created. No existing files are
renamed. No knowledge is extracted to PKM or BKM. Folder naming is not touched.

Naming standardization becomes relevant at these future steps:

| Phase | Naming dependency |
|---|---|
| Batch 1 — archive direct | None. DB state change only. |
| Batch 2 — mark active | None. DB state change only. |
| Batch 3 — archive after check | Low. No new files. Minor if versionless legacy files are resolved. |
| Batch 4 — BKM extraction | Yes. New files written to GL, SOP, or agent_learnings. Should follow naming standard. |
| Batch 5 — PKM extraction | Yes. New files written to KE-Health.md or similar. Should follow naming standard. |
| Phase C — auto-processing | Yes. Auto-registration creates new folders and files at runtime. Standard must be in place before Phase C. |

**Recommended execution sequence:**

```
Step 1: Batch 1 (archive direct) — immediate, no naming dependency
Step 2: Batch 2 (mark active) — immediate, no naming dependency
Step 3: Task 77 execution — English rule into GL (prerequisite for Task 75 GL amendment)
Step 4: Task 78 + Task 75 execution — naming/versioning standard into GL
Step 5: Batch 3 (archive after check) — can proceed with or without naming standard
Step 6: Batch 4 + Batch 5 (extraction) — naming standard should be in place
Step 7: Phase C (auto-processing) — naming standard is a hard prerequisite
```

Batch 1 and Batch 2 can execute now without waiting for this addendum to be actioned.
The naming standard work (Tasks 75, 77, 78) can run in parallel with Batches 1 and 2.

---

## 10. Proposed Owner Decisions

This addendum requires no Owner decision for Batch 1 authorization. The decisions below
are for the naming standardization work.

**Decision A — Accept the proposed naming standards as the basis for Task 75 execution.**
Owner approves the proposals in Sections 3, 4, 5, and 6 as the authoritative input for
the GL amendment that Task 75 will produce.

**Decision B — Batch tasks 77 and 78 into a single GL amendment proposal.**
Tasks 77 (English-language rule) and 78 (correction-versioning rule) share the same
GL home (likely a new GL or amendment to GL-017). Batching them is more efficient than
two separate Iris review cycles.

**Decision C — Confirm artifact_type DB migration is in scope for Task 75.**
The DB cleanup in Section 5.2 (renaming `triage_document` → `triage_report`, reclassifying
mistyped `status_report` rows, adding `write_list` type) is confirmed as part of Task 75
implementation, not a separate task.

**Decision D — Confirm LC-10 consumes the naming standard but does not block it.**
LC-10 resolution proceeds independently. Its output artifact naming will follow the standard
once the standard is in place. LC-10 does not block naming standardization and naming
standardization does not block LC-10.

---

**Delivered on:** 2026-06-07
**Delivered at:** /opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Hardening Phase B Triage/
