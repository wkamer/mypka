# Deliverable Lifecycle Naming and Artifact Standardization — Implementation Proposal v01

**Status:** Proposal only — no implementation
**Version:** v01
**Date:** 2026-06-07
**Author:** larry
**Backlog items:** Task 75, Task 77, Task 78
**Requires approval by:** Owner Walter Kamer — see Approval Gate

---

## 1. Exact Implementation Scope

This proposal covers four tightly coupled changes that must be implemented as a unit.
They share a single purpose: establishing a complete, unambiguous naming and artifact
standard for all myPKA AI team deliverables.

### Scope item 1 — Deliverable folder and file naming standard (Task 75)

**What:** Add two new sections to GL-001 (File Naming Conventions):
- Deliverable folder naming rules (confirms and codifies the `YYYYMMDD_Domain_Description` pattern)
- Deliverable file naming rules (introduces the amended standard: `<YYYYMMDD>-<artifact-type-slug>-<description-slug>-v<NN>.md`)
- Versioning syntax (`v01/v02/v03`, zero-padded, no semver, starts at `v01`)
- Same-folder vs. new-folder rules
- Correction Note requirement

**Target file:** `Team Knowledge/Core/Guidelines/GL-001_File naming conventions.md`
**What GL-001 currently lacks:** No coverage of Deliverables folder naming, no deliverable file naming pattern, no versioning syntax. The current GL-001 covers Projects (P-), Topics (T-), Key Elements (KE-), Goals (G-), SOPs, GLs, Wikilinks — but nothing about the Deliverables folder.

### Scope item 2 — English-language rule for governance deliverable content (Task 77)

**What:** Add a new section to GL-014 (AI Team Governance) establishing that all persisted
governance deliverables — proposals, execution reports, closure reports, triage reports,
write-lists, decision records, verification reports, assessments, SOPs, GLs, session logs,
AGENT.md files — must be written fully in English. Mixed Dutch/English is permitted only
when quoting Owner input verbatim or citing an existing Dutch-language source text.

**Target file:** `Team Knowledge/Core/Guidelines/GL-014_AI Team Governance.md`
**Why GL-014 and not GL-001:** GL-001 governs naming (filenames, folder names). GL-014
governs how the team operates. The English-language rule governs deliverable content,
which is an operational governance principle, not a naming convention. GL-014 is the
correct home.
**CLAUDE.md:** No amendment needed. CLAUDE.md already says "read GL-001 before any create
or rename operation." After this implementation, GL-001 will carry the naming standard and
GL-014 will carry the language standard. No redundant entry in CLAUDE.md is required.
**AGENT.md:** No amendment needed for any specialist. The GLs are the authoritative source;
agents reference GLs, not their own AGENT.md for naming conventions.

### Scope item 3 — Correction versioning rule (Task 78)

**What:** Amend SOP-015 (Proposal Iteration Protocol for System File Changes) to make the
new-version-on-correction rule explicit as a standalone rule, not only implied by Step 3.

SOP-015 Step 3 already says "Write a new versioned file — do not overwrite or edit the
prior version file." The gap is that this rule is buried inside the step sequence and
applies only to proposals explicitly governed by SOP-015. There is no general rule
covering all governance artifacts (execution reports, closure reports, write-lists, etc.)
that are not SOP-015 proposals. The amendment adds an Explicit Rule section to SOP-015
that covers the full artifact scope.

**Target file:** `Team Knowledge/Core/SOPs/SOP-015_Proposal Iteration Protocol for System File Changes.md`
**Amendment type:** Add one new section: `## Explicit Rules — Versioning and Correction Handling`
covering all governance artifacts, not only proposals under SOP-015 iteration.

### Scope item 4 — Artifact type taxonomy and normalization (Decision C)

**Part A — SOP-017 amendment:**
Add a formal Artifact Type Taxonomy as a new Section 5a in SOP-017 (Deliverable Lifecycle
Knowledge Processing and Archiving Procedure). Section 5 (Processing Destination Catalog)
references artifact types informally. Section 5a will define the canonical enum of valid
`artifact_type` values, their file-slug equivalents, and their definitions.

**Target file:** `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md`
**What SOP-017 currently lacks:** No enumeration of valid artifact_type values. The
`deliverable_lifecycle` DB table accepts free-text `artifact_type`, which has led to six
non-standard values in active use.

**Part B — DB migration script:**
A Python script normalizes the 17 affected rows in `deliverable_lifecycle` (team-knowledge.db).
The script runs inside a BEGIN TRANSACTION / COMMIT block and produces a pre-migration snapshot.

**Target:** `team-knowledge.db` — table `deliverable_lifecycle`, column `artifact_type`
**Script location (after write):** `Team Knowledge/Core/Scripts/normalize_artifact_types.py`

---

## 2. Recommended Governance Landing Locations

| Change | Target instrument | Instrument type | Reason |
|---|---|---|---|
| Deliverable folder naming | GL-001 | Guideline | GL-001 is the naming authority for the entire vault |
| Deliverable file naming | GL-001 | Guideline | Same — no other instrument covers file naming conventions |
| Versioning syntax (`v01/v02`) | GL-001 | Guideline | Naming convention; belongs with the file naming rules |
| Same-folder vs. new-folder rule | GL-001 | Guideline | Structural naming decision; belongs with folder naming |
| Correction Note requirement | GL-001 | Guideline | Naming and versioning consequence; belongs with versioning rules |
| English-language rule for content | GL-014 | Guideline | Operational governance principle; GL-014 governs team operating standards |
| Correction versioning — broad scope | SOP-015 | SOP | SOP-015 owns the versioning and iteration protocol for all governance artifacts |
| Artifact type taxonomy definition | SOP-017 | SOP | SOP-017 owns the deliverable processing procedure; taxonomy belongs near Section 5 |
| Artifact type DB normalization | Script + DB | Infrastructure | Execution-only; no GL or SOP needed beyond the SOP-017 taxonomy definition |

**Not required:**
- CLAUDE.md amendment: existing rule "read GL-001 before any create or rename operation" is sufficient. No new behavioral rule is needed.
- AGENT.md amendments: zero specialist AGENT.md files need to change. Naming and language rules live in GLs, which all agents reference directly.

---

## 3. Proposed Write-List Structure

Implementation is split into two batches. Each batch has its own write-list, Iris review, and
Owner authorization. Batch B must not start before Batch A is complete and post-checked.

---

### Batch A — GL and SOP text amendments (no DB changes)

**Batch A scope:** W-A1 through W-A3. File writes only. No database changes. Reversible.

**W-A1 — GL-001 amendment (Task 75)**

Target: `Team Knowledge/Core/Guidelines/GL-001_File naming conventions.md`

Pre-check:
- Confirm GL-001 does not already contain a "Deliverables" section (collision check)
- Confirm GL-001 does not already define a versioning syntax (collision check)
- Record line count of current file

Changes:
- Add new section `## Deliverables Folder Naming` after the existing `## File Names by Type` section
- Add new section `## Deliverables File Naming` immediately after
- Add new section `## Versioning` immediately after
- Add Changelog entry

Batch-stop rule: If the pre-check finds an existing Deliverables or versioning section, halt W-A1 and surface the collision to the Owner before proceeding.

---

**W-A2 — GL-014 amendment (Task 77)**

Target: `Team Knowledge/Core/Guidelines/GL-014_AI Team Governance.md`

Pre-check:
- Confirm GL-014 does not already contain a language or English-content rule (collision check)
- Confirm Section 5 (Changelog-protocol) is the last numbered section (determines insert position)

Changes:
- Add new section `## 6. Language standards` after Section 5 (Changelog-protocol)
- Add Changelog entry

Batch-stop rule: If pre-check finds an existing language rule that conflicts with the proposed rule, halt and surface to Owner.

---

**W-A3 — SOP-015 amendment (Task 78)**

Target: `Team Knowledge/Core/SOPs/SOP-015_Proposal Iteration Protocol for System File Changes.md`

Pre-check:
- Confirm SOP-015 does not already have an Explicit Rules section
- Confirm Step 3 text is still present and unchanged ("Write a new versioned file — do not overwrite or edit the prior version file")

Changes:
- Add new section `## Explicit Rules — Versioning and Correction Handling` at the end of the document, before the Changelog
- Add Changelog entry

Batch-stop rule: If pre-check finds a conflicting explicit rule already present, halt and surface to Owner.

Batch-stop across W-A1 through W-A3: If any single write in Batch A fails its pre-check, the entire Batch A halts. Writes W-A2 and W-A3 do not execute if W-A1's pre-check failed, and W-A3 does not execute if W-A2's pre-check failed.

---

### Batch B — SOP-017 amendment and DB migration

**Batch B scope:** W-B1 and W-B2. Batch B must not start before Batch A post-check passes.

**W-B1 — SOP-017 amendment — artifact type taxonomy**

Target: `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md`

Pre-check:
- Confirm Section 5 (Processing Destination Catalog) exists and is intact
- Confirm no Section 5a already exists
- Confirm no existing artifact_type enumeration is present in SOP-017

Changes:
- Insert new section `## 5a. Artifact Type Taxonomy` immediately after Section 5
- Add Changelog entry

Batch-stop rule: If pre-check finds an existing Section 5a or conflicting taxonomy, halt and surface to Owner. W-B2 does not execute if W-B1's pre-check fails.

---

**W-B2 — DB migration — normalize artifact_type values**

Target: `team-knowledge.db` — table `deliverable_lifecycle`, column `artifact_type`

Pre-check (run before any UPDATE):
```sql
SELECT artifact_type, COUNT(*), GROUP_CONCAT(id)
FROM deliverable_lifecycle
GROUP BY artifact_type ORDER BY artifact_type;
```
Expected pre-migration distribution:
- closure_report: 3 (IDs 9, 32, 34)
- decision_record: 1 (ID 14)
- domain_knowledge_update: 5 (IDs 2, 6, 7, 8, 16)
- proposal: 12 (IDs 17, 18, 19, 26, 28, 30, 36, 38, 39, 44, 45, 47)
- research_brief: 1 (ID 3)
- status_report: 12 (IDs 1, 15, 20, 21, 27, 29, 33, 35, 37, 40, 41, 43)
- triage_document: 9 (IDs 4, 5, 10, 11, 12, 13, 31, 42, 46)

If the pre-check does not match this distribution exactly, halt the entire Batch B migration and surface the discrepancy to the Owner.

Migration steps (all inside a single transaction):
```sql
BEGIN TRANSACTION;

-- Step 1: triage_document → triage_report (9 rows)
UPDATE deliverable_lifecycle
SET artifact_type = 'triage_report'
WHERE artifact_type = 'triage_document';

-- Step 2: proposal (write-lists) → write_list (2 rows: IDs 26, 28)
UPDATE deliverable_lifecycle
SET artifact_type = 'write_list'
WHERE id IN (26, 28);

-- Step 3: status_report (execution reports) → execution_report (2 rows: IDs 27, 29)
UPDATE deliverable_lifecycle
SET artifact_type = 'execution_report'
WHERE id IN (27, 29);

-- Step 4: status_report (verifications) → verification_report (3 rows: IDs 35, 37, 41)
UPDATE deliverable_lifecycle
SET artifact_type = 'verification_report'
WHERE id IN (35, 37, 41);

-- Step 5: status_report (assessments) → assessment (1 row: ID 33)
UPDATE deliverable_lifecycle
SET artifact_type = 'assessment'
WHERE id IN (33);

COMMIT;
```

Post-migration verification (run immediately after COMMIT):
```sql
SELECT artifact_type, COUNT(*), GROUP_CONCAT(id)
FROM deliverable_lifecycle
GROUP BY artifact_type ORDER BY artifact_type;
```

Expected post-migration distribution:
- assessment: 1 (ID 33)
- closure_report: 3 (IDs 9, 32, 34)
- decision_record: 1 (ID 14)
- domain_knowledge_update: 5 (IDs 2, 6, 7, 8, 16)
- execution_report: 2 (IDs 27, 29)
- proposal: 10 (IDs 17, 18, 19, 30, 36, 38, 39, 44, 45, 47)
- research_brief: 1 (ID 3)
- status_report: 6 (IDs 1, 15, 20, 21, 40, 43)
- triage_report: 9 (IDs 4, 5, 10, 11, 12, 13, 31, 42, 46)
- verification_report: 3 (IDs 35, 37, 41)
- write_list: 2 (IDs 26, 28)

Total row count must remain 43 before and after. Any deviation triggers immediate ROLLBACK.

---

## 4. Proposed Artifact Type Migration Plan

### Full migration table

| ID | Current artifact_type | Proposed artifact_type | Artifact name | Rationale |
|---|---|---|---|---|
| 4 | triage_document | triage_report | UMC architectuurschets | Consistent with new taxonomy |
| 5 | triage_document | triage_report | UMC diagnose en aanbevelingen | Consistent with new taxonomy |
| 10 | triage_document | triage_report | Architecture Triage Memory Domain Routing | Consistent with new taxonomy |
| 11 | triage_document | triage_report | Deliverable Lifecycle Knowledge Processing Triage | Consistent with new taxonomy |
| 12 | triage_document | triage_report | Graduation Candidate Parked - Context-mode MCP Fix | Consistent with new taxonomy |
| 13 | triage_document | triage_report | Review Gate Protocol Triage | Consistent with new taxonomy |
| 31 | triage_document | triage_report | LC Naming Alignment Impact Assessment | Consistent with new taxonomy |
| 42 | triage_document | triage_report | DL Phase 1 Retroactive Iris Review | Consistent with new taxonomy |
| 46 | triage_document | triage_report | team-tasks-id-76-assessment | Consistent with new taxonomy |
| 26 | proposal | write_list | LC Batch 1 Write-List | A write-list is not a proposal; mislabeled at registration |
| 28 | proposal | write_list | LC Batch 2 Write-List | A write-list is not a proposal; mislabeled at registration |
| 27 | status_report | execution_report | LC Batch 1 Execution Report | An execution report is a distinct artifact type; mislabeled at registration |
| 29 | status_report | execution_report | LC Batch 2 Execution Report | An execution report is a distinct artifact type; mislabeled at registration |
| 35 | status_report | verification_report | LCL Session Start Verification | A verification report is a distinct artifact type; mislabeled at registration |
| 37 | status_report | verification_report | Post-SOP-019 Session Start Verification | A verification report is a distinct artifact type; mislabeled at registration |
| 41 | status_report | verification_report | Final Governance State Verification | A verification report is a distinct artifact type; mislabeled at registration |
| 33 | status_report | assessment | LC-5-6-7 Processed to Closed Assessment | An assessment is a distinct artifact type; mislabeled at registration |

**Unchanged rows (26 rows):**
All rows not in the table above retain their current artifact_type. No change to IDs:
1, 2, 3, 6, 7, 8, 9, 14, 15, 16, 17, 18, 19, 20, 21, 30, 32, 34, 36, 38, 39, 40, 43, 44, 45, 47.

### New artifact_type values introduced by this migration

| New value | DB representation | File slug | Definition |
|---|---|---|---|
| triage_report | triage_report | triage-report | Analysis and classification output requiring Owner decision; replaces triage_document |
| write_list | write_list | write-list | Ordered list of write actions for a specific execution; always paired with an execution_report |
| execution_report | execution_report | execution-report | Post-execution record of what was done, against which write-list, with what outcome |
| verification_report | verification_report | verification-report | Point-in-time state check; session-start, post-execution, smoke test |
| assessment | assessment | assessment | Impact analysis, risk analysis, audit output, naming assessment |

### Artifact types retained unchanged

| Value | File slug | Definition |
|---|---|---|
| proposal | proposal | Any artifact awaiting Owner approval before execution |
| closure_report | closure-report | End-of-project, end-of-task, or end-of-LC closure |
| decision_record | decision-record | Record of Owner decision on a governance question |
| domain_knowledge_update | knowledge-output | Domain knowledge artifact for BKM or PKM extraction |
| research_brief | research-brief | Research output from Pax or domain specialist |
| status_report | status-report | General status update; use only when no specific type fits |

---

## 5. Risks and Rollback Plan

### Risk R-1: GL-001 collision

**Risk:** GL-001 already contains a Deliverables or versioning section that conflicts with the proposed additions.

**Likelihood:** Low. GL-001 scan confirms no Deliverables section currently exists. The
existing sections are: General Rule, File Names by Type, ALL CAPS, Numbering (SOP/GL/WS),
Wikilinks, Changelog. No versioning syntax section exists.

**Mitigation:** Pre-check W-A1 detects the collision before any write.

**Rollback:** If the pre-check fires, no write has occurred. No rollback needed — the write
was blocked. Surface collision content to Owner for resolution before re-authorizing.

---

### Risk R-2: SOP-015 Step 3 conflict

**Risk:** The new explicit rules section in SOP-015 contradicts or weakens the existing
Step 3 wording, creating two versions of the same rule that agents interpret differently.

**Likelihood:** Low. Step 3 says "Write a new versioned file — do not overwrite or edit
the prior version file." The new explicit rules section broadens this to all governance
artifacts, not contracts it. A broader scope rule cannot logically contradict a narrower
implementation of the same principle.

**Mitigation:** Pre-check W-A3 verifies Step 3 is intact. The new section references Step 3
explicitly, making the relationship unambiguous.

**Rollback:** GL-001 and GL-014 writes (W-A1, W-A2) can be manually reverted by restoring
the file content from the proposal document (which contains the exact before/after text per
SOP-015 standards). The proposal file is the rollback source.

---

### Risk R-3: SOP-017 Section 5 / Section 5a numbering conflict

**Risk:** An existing SOP-017 amendment has already added a Section 5a that is unknown to
this proposal.

**Likelihood:** Low. SOP-017 was last amended 2026-06-05. The most recent amendment (EX-8)
added to Section 14. Section 5 is unchanged per the amendment records.

**Mitigation:** Pre-check W-B1 reads and verifies the current Section 5 and confirms no
Section 5a exists.

**Rollback:** SOP-017 file can be manually restored from the pre-write content recorded in
the execution report (SOP-015 Step 7 requirement — execution report includes before/after
for every write).

---

### Risk R-4: DB migration — partial update or row count mismatch

**Risk:** A bug in the migration script updates fewer rows than expected, leaving the DB in
an inconsistent state (some rows with `triage_document`, others with `triage_report`).

**Likelihood:** Low. The migration uses explicit ID lists for targeted rows and a
type-name filter for the triage_document → triage_report rename. The transaction
wrapper ensures atomicity.

**Mitigation:**
- Pre-migration: `cp 'team-knowledge.db' 'team-knowledge.db.pre-202606-migration'` — backup before any transaction opens
- All five UPDATE statements run inside a single BEGIN TRANSACTION / COMMIT block
- Post-migration count check must match the expected distribution exactly before COMMIT is confirmed

**Rollback:**
- If the post-migration count check fails: ROLLBACK is issued inside the same transaction block (not yet committed)
- If ROLLBACK fails for any reason: restore from `team-knowledge.db.pre-202606-migration` — this is a full file restore, not a targeted undo

---

### Risk R-5: SOP-017 amendment makes existing lifecycle execution reports non-compliant

**Risk:** The new artifact type taxonomy in SOP-017 Section 5a defines types that execution
reports already produced (today and prior sessions) did not use. Those reports reference the
old types. This does not invalidate the reports retroactively.

**Likelihood:** Certain — all existing reports used the old types. This is expected and
acceptable. The taxonomy defines forward-going behavior.

**Mitigation:** Section 5a must include a migration note: "Artifact_type values in rows
registered before 2026-06-07 may use pre-taxonomy type names. Those rows are normalized
per the W-B2 migration. No retroactive changes to execution reports are required."

**Rollback:** Not applicable. This is an acknowledged forward-only rule.

---

## 6. Post-Check Plan

### Batch A post-checks

**PC-A1: GL-001 content verification**
- Read GL-001 in full
- Confirm presence of: `## Deliverables Folder Naming`, `## Deliverables File Naming`, `## Versioning`
- Confirm the new sections contain the exact text from the approved write-list
- Confirm the Changelog entry is present with correct date, agent, and backlog reference
- Confirm no existing GL-001 section was modified (line count of unchanged sections)

**PC-A2: GL-014 content verification**
- Read GL-014 in full
- Confirm presence of `## 6. Language standards`
- Confirm the section text matches the approved write-list exactly
- Confirm Sections 1 through 5 are unchanged
- Confirm Changelog entry is present

**PC-A3: SOP-015 content verification**
- Read SOP-015 in full
- Confirm presence of `## Explicit Rules — Versioning and Correction Handling`
- Confirm Step 3 is unchanged ("Write a new versioned file — do not overwrite or edit the prior version file")
- Confirm no other SOP-015 section was modified
- Confirm Changelog entry is present

### Batch B post-checks

**PC-B1: SOP-017 Section 5a verification**
- Read SOP-017 Sections 5 and 5a
- Confirm Section 5 (Processing Destination Catalog) is unchanged
- Confirm Section 5a contains the complete artifact type taxonomy table
- Confirm Changelog entry is present

**PC-B2: DB migration verification**
```sql
-- Row count
SELECT COUNT(*) FROM deliverable_lifecycle;  -- must be 43

-- Type distribution
SELECT artifact_type, COUNT(*), GROUP_CONCAT(id)
FROM deliverable_lifecycle
GROUP BY artifact_type ORDER BY artifact_type;

-- Verify no triage_document rows remain
SELECT COUNT(*) FROM deliverable_lifecycle
WHERE artifact_type = 'triage_document';  -- must be 0

-- Verify specific reclassified rows
SELECT id, artifact_type FROM deliverable_lifecycle
WHERE id IN (26,27,28,29,33,35,37,41)
ORDER BY id;
-- Expected: 26=write_list, 27=execution_report, 28=write_list,
--           29=execution_report, 33=assessment, 35=verification_report,
--           37=verification_report, 41=verification_report
```

**PC-B3: Pre-migration backup verification**
- Confirm `team-knowledge.db.pre-202606-migration` exists in `Team Knowledge/`
- Confirm its file size is non-zero
- This file is retained until at least one full subsequent session confirms the migrated DB is stable

---

## 7. One Batch or Multiple Batches

**Recommendation: Two batches.**

**Batch A** (GL-001, GL-014, SOP-015 amendments) and **Batch B** (SOP-017 amendment, DB
migration) must execute in order, with Batch A post-check passing before Batch B begins.

**Rationale:**

| Criterion | Batch A | Batch B |
|---|---|---|
| Write type | File writes only | File write + live DB mutation |
| Reversibility | Manual file restore from proposal | DB backup restore (full file) |
| Dependencies | None — all three writes are independent of each other | Depends on Batch A completing: SOP-017 Section 5a must exist before DB migration runs so the taxonomy is documented when the DB values change |
| Risk level | Low | Medium (DB mutation) |
| Blocking | Does not block Batch 1 of Phase B | Does not block Phase B Batch 1 |

**Single-batch argument (rejected):** Combining all five writes into one batch makes the
execution report simpler and reduces the number of Owner authorization steps. However, if
the DB migration requires a ROLLBACK, having already written GL-001, GL-014, and SOP-015
would leave the governance files inconsistent with the DB state. Two batches preserve
isolation.

**Each batch requires:** a write-list document, one Iris review, one Owner authorization,
one execution, one execution report, one post-check.

---

## 8. Exact Owner Authorization Package

The following is a complete statement of what Owner authorization covers for each step.

### Phase 1 — This proposal authorization (current step)

Owner authorizes:
1. This implementation proposal (v01) as the approved basis for the write-lists that follow
2. The two-batch structure (Batch A then Batch B)
3. The governance landing locations (GL-001 for naming, GL-014 for language, SOP-015 for correction versioning, SOP-017 for taxonomy, DB for migration)
4. The artifact_type migration plan — all 17 rows as specified in Section 4
5. Task 77 and Task 78 batched into the same implementation sequence (Decision B confirmed)
6. LC-10 is not in scope for this proposal (Decision D confirmed)

This authorization does NOT cover:
- The content of any GL or SOP amendment text (that is reviewed in Batch A write-list)
- The DB migration script (that is reviewed in Batch B write-list)
- Any file write to GL-001, GL-014, SOP-015, or SOP-017
- Any DB UPDATE statement

### Phase 2 — Batch A write-list authorization

Owner will receive: a write-list document containing the exact before/after text for each
of the three GL/SOP amendments. Iris review is completed before the write-list is presented.

Owner authorizes (at that time):
- The exact amendment text for GL-001
- The exact amendment text for GL-014
- The exact amendment text for SOP-015
- Batch-stop rules as stated in Section 3

### Phase 3 — Batch B write-list authorization

Owner will receive: a write-list document containing the exact SOP-017 Section 5a text
and the exact DB migration script. Iris review is completed before the write-list is presented.
Batch A post-check confirmation is included in the Batch B write-list preamble.

Owner authorizes (at that time):
- The exact SOP-017 Section 5a text
- The exact migration script (readable SQL + Python)
- The DB backup step
- Batch-stop rules as stated in Section 3

---

## 9. Exact Next Prompt for Implementation Authorization

The following prompt authorizes Phase 1 (this proposal) and triggers Batch A write-list
production. It is execution-ready and requires no modification.

---

**Prompt to authorize Phase 1 and start Batch A write-list:**

> You are Larry, Team Orchestrator.
>
> Owner authorizes implementation proposal v01 for Deliverable Lifecycle Naming and Artifact
> Standardization, located at:
> `Deliverables/20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal/20260607-proposal-naming-artifact-standardization-v01.md`
>
> Authorization covers:
> - Two-batch structure (Batch A then Batch B)
> - Governance landing locations as specified in Section 2
> - Artifact type migration plan as specified in Section 4
> - Task 77 and Task 78 batched into the same sequence
>
> Task:
> Produce the Batch A write-list for Owner review. The write-list must contain exact
> before/after text for W-A1 (GL-001), W-A2 (GL-014), and W-A3 (SOP-015). Read each
> target file before writing any amendment text. Apply batch-stop rules as specified in
> Section 3 of the proposal. Submit for Iris review before presenting to Owner.
>
> Do not execute any writes. Do not modify any files. Produce the write-list document only.

---

**Note on Iris review:** Per SOP-016 and GL-016, governance-relevant write-lists require an
Iris review before Owner authorization. The Batch A write-list will be submitted to Iris
immediately after production, and the Iris-reviewed version will be presented to the Owner
for authorization before any write is executed.

---

## Approval Gate

No implementation may happen until Owner Walter Kamer explicitly approves this proposal v01.

Approval of this proposal authorizes the two-batch structure and governance landing
locations only. It does not authorize any file write, any DB change, or any GL/SOP
amendment text. Those require separate write-list authorizations in Phase 2 (Batch A)
and Phase 3 (Batch B).

Approval of a prior or future version of this proposal does not carry forward to v01.

---

**Delivered on:** 2026-06-07
**Delivered at:** /opt/myPKA/Deliverables/20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal/
