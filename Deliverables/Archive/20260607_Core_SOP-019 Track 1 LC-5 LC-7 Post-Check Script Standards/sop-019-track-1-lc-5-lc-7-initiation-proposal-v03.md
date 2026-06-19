# SOP-019 Track 1 — Initiation Proposal v03
## LC-5 + LC-7: Post-Check Script Standards — GL-005 Amendment

**Status:** Read-only initiation proposal. No live system files modified. No database rows updated.
**Date:** 2026-06-07
**Author:** Larry (orchestrator)
**Governance track:** SOP-019 Track 1
**Source task:** team_tasks id=82
**Requires:** Owner authorization → write execution

---

## Revision History

**v03 supersedes v02.**

Reason: Iris review (iris-review-report-track-1-lc-5-lc-7-v01.md) returned REQUIRES REVISION BEFORE OWNER AUTHORIZATION with two advisory issues:

1. W-3 changelog failure was not covered by a batch-stop rule. If the changelog append failed after W-2 succeeded, the executor would proceed to mark all database records as processed — producing an undocumented GL-005 amendment with a misleading completion audit trail.
2. PC-1 through PC-3 method cells were underspecified and could lead an executor to perform full-file searches (violating LC-5a), incomplete position verification (PC-1), or non-final-entry confirmation (PC-3). The compliance intent was documented only in a footnote below the table, not in the method cells themselves.

Corrections in v03: batch-stop rule for W-3 added (Section 4); PC-1, PC-2, and PC-3 method cells replaced with scoped, unambiguous specifications (Section 7).

The GL-005 amendment text (Section 3) is unchanged. Iris confirmed it is execution-ready. The proposed changelog entry (Section 8) is unchanged. Iris confirmed it is governance-safe.

**v02 superseded v01.**
Reason: v01 included the Owner's personal name in the proposed GL-005 changelog entry.

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

The following write actions will be executed after Owner authorization. No action below is permitted before that authorization.

| Step | Action | Target | Reversible |
|---|---|---|---|
| W-1 | Read GL-005 current content (verify exact insertion point) | GL-005 | N/A (read-only) |
| W-2 | Insert new section after `## Diagnostic discipline` | GL-005 | Yes (delete inserted block) |
| W-3 | Append changelog entry to GL-005 | GL-005 | Yes (remove last changelog line) |
| W-4 | Update team_tasks id=82 status to `completed` | team-knowledge.db | No (SQL UPDATE) |
| W-5 | Update learning_candidates id=5 status to `processed` | team-knowledge.db | No (SQL UPDATE) |
| W-6 | Update learning_candidates id=7 status to `processed` | team-knowledge.db | No (SQL UPDATE) |

**Batch-stop rules:**
This proposal has no associated write-list. Therefore no write-list batch-stop rules apply. The following batch-stop rules are defined for this execution:

> If W-2 (section insertion) produces a post-check FAIL — the inserted section is not found or is malformed — stop immediately. Do not proceed to W-3, W-4, W-5, or W-6. Report the failure to the Owner before any further action.

> If W-3 (changelog append) produces a post-check FAIL — the changelog entry is not found as the final entry in the Changelog section — stop immediately. Do not proceed to W-4, W-5, or W-6. Report the failure to the Owner before any further action.

---

## 5. Iris Review Requirements

**Iris review is complete.**

Iris reviewed proposal v02 and produced:
`Deliverables/20260607_Core_SOP-019 Track 1 LC-5 LC-7 Post-Check Script Standards/iris-review-report-track-1-lc-5-lc-7-v01.md`

All advisory items from that review have been incorporated in v03 exactly as specified. No second Iris review is required before Owner authorization.

Iris review findings summary:
- Point 1 (failure mode coverage): PASS
- Point 2 (no contradiction or duplication): PASS
- Point 3 (insertion point): PASS
- Point 4 (batch-stop rule): ADVISORY — resolved in v03
- Point 5 (post-check methods): ADVISORY — resolved in v03
- Point 6 (amendment execution-readiness): PASS
- Point 7 (changelog governance safety): PASS

---

## 6. Owner Authorization Requirements

This proposal is ready for Owner authorization.

- The Owner authorizes or rejects the write plan.
- Authorization must be explicit: the Owner must say yes to the specific write plan shown.
- A prior yes for another write event does not cover this write event.
- Write execution begins only after explicit Owner authorization.

---

## 7. Post-Check Requirements

After write execution (W-2 and W-3), the following post-checks must pass before declaring success:

| Check | Method | Expected result |
|---|---|---|
| PC-1 | Extract the ordered list of `##`-level headings from GL-005. Confirm that `## Post-Check Script Standards` appears immediately after `## Diagnostic discipline` and immediately before `## Production safety` in that ordered list. | Section found at correct position: after Diagnostic Discipline, before Production Safety |
| PC-2 | Extract the `## Post-Check Script Standards` block from GL-005 (from that heading up to the next `##`-level heading). Within that extracted block only, confirm all three subsection headings are present: `### Scope targeting`, `### Format matching`, `### Code structure independence`. | All three subsection headings found within the extracted block |
| PC-3 | Extract the `## Changelog` section from GL-005 (from that heading to end of file). Within that extracted block only, identify the final non-empty line. Confirm it contains `2026-06-07` and references both `LC-5` and `LC-7`. | Final changelog entry contains date and both LC references |
| PC-4 | Query team_tasks id=82 — confirm status = `completed` | status = completed |
| PC-5 | Query learning_candidates id=5 — confirm status = `processed` | status = processed |
| PC-6 | Query learning_candidates id=7 — confirm status = `processed` | status = processed |

Post-check compliance with LC-5 and LC-7 standards:
- PC-1 verifies position via heading order extraction, not heading presence alone. No full-file string matching. (LC-5a compliant)
- PC-2 is scoped to the extracted `## Post-Check Script Standards` block, not the full file. Searches for exact markdown heading notation as used in the inserted text. (LC-5a and LC-5b compliant)
- PC-3 is scoped to the extracted `## Changelog` block, not the full file. Verifies the final non-empty line, not any occurrence of the date string. (LC-5a compliant; no branch-order assumption, LC-7a compliant)
- PC-4 through PC-6 are direct field queries with exact values. No pattern matching, no scope concerns.

---

## 8. Proposed Changelog Entry for GL-005

```
- 2026-06-07 (Larry, SOP-019 Track 1): Post-Check Script Standards section added. Covers scope targeting, format matching, and code structure independence. Sources: LC-5 (post-check scope and notation fragility) and LC-7 (branch-order-dependent regex). Approved by Owner.
```

---

## 9. Confirmation of Read-Only Status

Proposal v01, v02, and v03 are the only files created in this initiation step. The Iris review artifact was written during the review phase.

| System | Action taken | Modification |
|---|---|---|
| GL-005 | Read (for amendment planning and Iris review) | None |
| GL-004 | Read (for path verification) | None |
| team-knowledge.db / learning_candidates | Read (id=5, id=7) | None |
| team-knowledge.db / team_tasks | Read (id=82) | None |
| CLAUDE.md | Not touched | None |
| SOP files | Not touched | None |
| AGENT.md files | Not touched | None |
| LC-8 | Not touched | None |

No live system files were modified. No database rows were updated.

---

## 10. Ready for Owner Authorization

Iris review is complete. All advisory items resolved. This proposal is ready for Owner authorization.

**What the Owner is authorizing:**

The Owner is authorizing execution of the write plan as specified in Section 4 of this document (v03). Specifically:

- W-2: Insert the `## Post-Check Script Standards` section into GL-005 after `## Diagnostic discipline`
- W-3: Append the changelog entry from Section 8 to GL-005
- W-4: Mark team_tasks id=82 as `completed`
- W-5: Mark learning_candidates id=5 as `processed`
- W-6: Mark learning_candidates id=7 as `processed`

Batch-stop rules apply as defined in Section 4. Post-checks as defined in Section 7 must pass before declaring success.

---

Delivered on: 2026-06-07
Delivered at: Track 1 initiation — Iris review complete, awaiting Owner authorization
