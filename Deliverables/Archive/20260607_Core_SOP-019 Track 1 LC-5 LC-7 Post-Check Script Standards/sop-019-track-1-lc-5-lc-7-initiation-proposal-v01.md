# SOP-019 Track 1 — Initiation Proposal v01
## LC-5 + LC-7: Post-Check Script Standards — GL-005 Amendment

**Status:** Read-only initiation proposal. No live system files modified. No database rows updated.
**Date:** 2026-06-07
**Author:** Larry (orchestrator)
**Governance track:** SOP-019 Track 1
**Source task:** team_tasks id=82
**Requires:** Iris review → Owner authorization → write execution

---

## 1. Source Records

### LC-5 (learning_candidates id=5)

| Field | Value |
|---|---|
| Title | Verification script fragility in governance post-checks |
| Status | triaged |
| Category | CAT-3 |
| Level | 2 |
| Learning scope | governance |
| Triage routing | graduation_candidate |
| Flagged by | Iris |
| Flagged at | 2026-06-07 09:54:58 |

**Description (verbatim):**
During LC Batch 1, Iris first identified a W-3 post-check fragility caused by full-file string matching instead of targeted GL-022 line matching. During execution, W-2 then produced false negatives because the post-check searched for single-quoted lifecycle values while the GL-022 markdown used backtick notation. Both issues show the same governance verification risk: post-checks must target the relevant scope and match the actual document format to avoid false FAIL results and Owner confusion.

**Two concrete failure modes in LC-5:**
- **LC-5a (scope):** Full-file string matching instead of targeted section/line matching. Risk: false FAIL on unrelated content.
- **LC-5b (notation):** Post-check searches for `'triaged'` while the target document renders `` `triaged` ``. Risk: silent False negative — check passes, error undetected.

---

### LC-7 (learning_candidates id=7)

| Field | Value |
|---|---|
| Title | Post-check regex assumes branch order in resolve_lc — silent False negatives if order differs |
| Status | triaged |
| Category | CAT-3 |
| Level | 2 |
| Learning scope | tooling |
| Triage routing | graduation_candidate |
| Flagged by | Iris |
| Flagged at | 2026-06-07 10:49:02 |

**Description (verbatim):**
During Batch 2 write-list v04 review, Iris flagged that the post-check regex for the reject branch uses a pattern that assumes reject precedes escalate in the function body. If the branch order differs in the written file, the reject branch checks report False negatives silently, meaning a malformed reject path passes post-check undetected. Post-check scripts must not assume code structure order; use explicit named-group matching or extract the target function text before applying branch checks.

**One concrete failure mode in LC-7:**
- **LC-7a (structure):** Regex depends on branch order inside a function body. Risk: silent False negative when the written file places branches in a different order than the post-check assumes.

---

### team_tasks id=82

| Field | Value |
|---|---|
| id | 82 |
| Title | Initiate SOP-019 Track 1: GL amendment for post-check script standards (LC-5 + LC-7) |
| Assignee | larry |
| Priority | 2 |
| Status | open |
| Tags | lc-lifecycle, governance, sop-019 |
| Created | 2026-06-07 11:15:32 |

---

## 2. Proposed Destination

**File:** `Team Knowledge/Core/Guidelines/GL-005_AI Engineering Operating System.md`

**Rationale:**
GL-005 is the canonical engineering standard for the full AI team. It already governs the validation step (Step 4), the Definition of Done, and Diagnostic Discipline. Post-check script standards belong here because:
- Post-checks are a form of validation (Step 4 scope).
- LC-5 and LC-7 both produce engineering quality failures — not governance procedure gaps. The failure mode is a badly written verification script, not a missing SOP step.
- GL-005 is read by every technical agent as their engineering operating standard.

**Alternative considered and rejected:** A new standalone GL file for post-check standards. Rejected because post-checks are a sub-topic of validation, not a standalone domain. GL-005 already has the natural home.

**Insertion point:** A new section `## Post-Check Script Standards` inserted after `## Diagnostic discipline` and before `## Production safety`.

---

## 3. Proposed Exact Amendment

The following section is proposed for insertion into GL-005 after the `## Diagnostic discipline` section:

---

```markdown
## Post-Check Script Standards

Post-check scripts verify that a write action produced the expected outcome. These rules apply to every post-check script written or reviewed by any agent.

### Scope targeting

A post-check must target the specific section or lines relevant to the change — not the full file.

- Full-file string matching is not permitted as a post-check method.
- Each check must be scoped to the smallest relevant unit: a section, a named block, a defined line range.
- Rationale: full-file matching produces false FAIL results when unrelated content elsewhere in the file contains overlapping strings. (Source: LC-5a)

### Format matching

A post-check must match the exact notation used in the target document.

- Before writing regex or string checks: confirm whether the target document uses single quotes, backtick notation, bold markers, or plain text for the expected value.
- A check that searches for `'triaged'` will produce silent False negatives if the document renders `` `triaged` ``.
- Rationale: notation mismatch produces silent false negatives — the check passes, the error is undetected. (Source: LC-5b)

### Code structure independence

A post-check must not assume the order of branches, conditions, or blocks in a function body.

- Do not write regex that depends on one branch appearing before another (e.g. reject before escalate).
- Instead: extract the target function or block text first, then apply checks within that extracted scope.
- Use explicit named-group matching where branch identity matters.
- Rationale: branch order may differ between a write plan and the written file; an order-dependent regex produces silent False negatives without any FAIL signal. (Source: LC-7a)
```

---

## 4. Write Plan (not yet authorized)

The following write actions will be executed after Iris review and Owner authorization. No action below is permitted before that sequence completes.

| Step | Action | Target | Reversible |
|---|---|---|---|
| W-1 | Read GL-005 current content (verify exact insertion point) | GL-005 | N/A (read-only) |
| W-2 | Insert new section after `## Diagnostic discipline` | GL-005 | Yes (delete inserted block) |
| W-3 | Append changelog entry to GL-005 | GL-005 | Yes (remove last changelog line) |
| W-4 | Update team_tasks id=82 status to `completed` | team-knowledge.db | No (SQL UPDATE) |
| W-5 | Update learning_candidates id=5 status to `processed` | team-knowledge.db | No (SQL UPDATE) |
| W-6 | Update learning_candidates id=7 status to `processed` | team-knowledge.db | No (SQL UPDATE) |

**Batch-stop rule:**
This proposal has no associated write-list. Therefore no write-list batch-stop rules apply. The following batch-stop rule is defined for this execution:

> If W-2 (section insertion) produces a post-check FAIL — the inserted section is not found or is malformed — stop immediately. Do not proceed to W-3, W-4, W-5, or W-6. Report the failure to the Owner before any further action.

---

## 5. Iris Review Requirements

Before Owner authorization, Iris must review this proposal and produce a written review artifact.

**Iris review scope:**
1. Verify the proposed amendment fully addresses all three identified failure modes: LC-5a (scope), LC-5b (notation), LC-7a (structure).
2. Verify the proposed text contains no contradictions with existing GL-005 sections (Step 4 Validation, Definition of Done, Diagnostic Discipline).
3. Verify the insertion point is correct and does not break GL-005 document flow.
4. Verify the batch-stop rule is sufficient for the write plan.
5. Verify the changelog entry wording is appropriate.
6. Flag any gaps, ambiguities, or risks not addressed by the proposed amendment.
7. Confirm or adjust the proposed amendment text — exact wording only, no scope expansion.

**Iris review output artifact:**
`Deliverables/20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards/iris-review-report-track-1-lc-5-lc-7-v01.md`

---

## 6. Owner Authorization Requirements

After Iris review is complete and the review artifact is written:

- Larry presents the Iris review findings and any proposed adjustments to the Owner.
- The Owner authorizes or rejects the write plan.
- Authorization must be explicit: the Owner must say yes to the specific write plan shown.
- A prior yes for another write event does not cover this write event.
- If Iris proposes adjustments: Larry presents the adjusted amendment text as a revised proposal. Owner authorization covers the adjusted version, not the original.
- Write execution begins only after explicit Owner authorization.

---

## 7. Post-Check Requirements

After write execution (W-2 and W-3), the following post-checks must pass before declaring success:

| Check | Method | Expected result |
|---|---|---|
| PC-1 | Read GL-005 and locate `## Post-Check Script Standards` heading | Section found at correct position (after Diagnostic Discipline, before Production Safety) |
| PC-2 | Read GL-005 and confirm all three subsections present: `### Scope targeting`, `### Format matching`, `### Code structure independence` | All three subsection headings found |
| PC-3 | Read GL-005 and confirm changelog entry present with date 2026-06-07 and LC-5 + LC-7 reference | Entry found as last line in Changelog |
| PC-4 | Query team_tasks id=82 — confirm status = `completed` | status = completed |
| PC-5 | Query learning_candidates id=5 — confirm status = `processed` | status = processed |
| PC-6 | Query learning_candidates id=7 — confirm status = `processed` | status = processed |

Post-checks PC-1 through PC-3 apply the standards from LC-5 and LC-7 themselves:
- PC-1 and PC-2 are scoped to the inserted block, not full-file string matching (LC-5a compliance).
- PC-2 searches for the exact markdown heading notation used in the inserted text (LC-5b compliance).
- PC-3 extracts only the Changelog section before checking, not the full file (LC-5a + LC-7a compliance).

---

## 8. Proposed Changelog Entry for GL-005

```
- 2026-06-07 (Larry, SOP-019 Track 1): Post-Check Script Standards section added. Covers scope targeting, format matching, and code structure independence. Sources: LC-5 (post-check scope and notation fragility) and LC-7 (branch-order-dependent regex). Approved by Owner Walter Kamer.
```

---

## 9. Confirmation of Read-Only Status

This proposal document is the only file created in this initiation step.

| System | Action taken | Modification |
|---|---|---|
| GL-005 | Read (for amendment planning) | None |
| GL-004 | Read (for path verification) | None |
| team-knowledge.db / learning_candidates | Read (id=5, id=7) | None |
| team-knowledge.db / team_tasks | Read (id=82) | None |
| CLAUDE.md | Not touched | None |
| SOP files | Not touched | None |
| AGENT.md files | Not touched | None |
| LC-8 | Not touched | None |

No live system files were modified. No database rows were updated.

---

## 10. Ready for Iris Review

This proposal is ready for Iris review.

**Exact next prompt for Iris review:**

> You are Iris, governance reviewer for the myPKA AI team. Review the following initiation proposal before Owner authorization.
>
> **Review artifact to produce:**
> `Deliverables/20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards/iris-review-report-track-1-lc-5-lc-7-v01.md`
>
> **Proposal to review:**
> `Deliverables/20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards/sop-019-track-1-lc-5-lc-7-initiation-proposal-v01.md`
>
> **Review scope (address each point explicitly):**
> 1. Does the proposed amendment fully address all three failure modes: LC-5a (scope targeting), LC-5b (notation matching), LC-7a (code structure independence)?
> 2. Does the proposed text contradict or duplicate any existing GL-005 section (Step 4 Validation, Definition of Done, Diagnostic Discipline)?
> 3. Is the insertion point (after Diagnostic Discipline, before Production Safety) correct for document flow?
> 4. Is the batch-stop rule sufficient for the write plan?
> 5. Are the post-check requirements (PC-1 through PC-6) correctly specified and do they themselves comply with the standards they are meant to enforce?
> 6. Is the proposed amendment text execution-ready as written, or does it require adjustment?
>
> **Output format:** Written review artifact at the path above. For each review point: PASS / FAIL / ADVISORY with brief explanation. If any point is FAIL or ADVISORY: propose the exact corrected text. Conclude with: APPROVED FOR OWNER AUTHORIZATION or REQUIRES REVISION BEFORE OWNER AUTHORIZATION.
>
> **Scope restriction:** Read-only review of the proposal and GL-005. Do not modify GL-005, CLAUDE.md, any SOP file, any AGENT.md, or any database row during this review.

---

Delivered on: 2026-06-07
Delivered at: Track 1 initiation — pre-Iris, pre-Owner-authorization phase
