# Iris Review Report — SOP-019 Track 1
## LC-5 + LC-7: Post-Check Script Standards — GL-005 Amendment

**Reviewer:** Iris (governance reviewer)
**Review date:** 2026-06-07
**Proposal reviewed:** `sop-019-track-1-lc-5-lc-7-initiation-proposal-v02.md`
**GL-005 version read:** current on disk at time of review (last changelog entry: 2026-06-03, B-031B)
**Scope:** Read-only review. No system files modified. No database rows updated.

---

## Review Findings

### Point 1 — Failure mode coverage: LC-5a, LC-5b, LC-7a

**PASS**

All three failure modes are fully addressed by the proposed amendment.

**LC-5a (scope targeting):**
The `### Scope targeting` subsection states: "A post-check must target the specific section or lines relevant to the change — not the full file." It prohibits full-file string matching and requires scope to the smallest relevant unit (section, named block, defined line range). Rationale cites LC-5a. The failure mode — W-3 using full-file string matching instead of targeted GL-022 line matching — is directly addressed.

**LC-5b (notation matching):**
The `### Format matching` subsection states: "A post-check must match the exact notation used in the target document." It requires pre-check confirmation of the notation style (single quotes, backticks, bold, plain text) and provides a concrete example using the `'triaged'` vs `` `triaged` `` case from the source event. Rationale cites LC-5b. The failure mode — searching for single-quoted values when the document uses backtick notation — is directly addressed.

**LC-7a (code structure independence):**
The `### Code structure independence` subsection states: "A post-check must not assume the order of branches, conditions, or blocks in a function body." It prohibits order-dependent regex, requires extracting the target function block first, and mandates named-group matching for branch identity. Rationale cites LC-7a. The failure mode — reject branch regex silently failing when branch order differs — is directly addressed.

---

### Point 2 — No contradiction or duplication with existing GL-005 sections

**PASS**

Three existing sections examined:

**Step 4. Validation (GL-005 lines 89–96):** Covers what to validate during development (tests, linting, typing, formatting, runtime validation, API contract validation). The proposed section governs how to construct post-check verification scripts in a governance workflow. These are complementary: Step 4 is about development-phase validation targets; the new section is about post-write governance verification quality. No overlap in scope, no duplication of rules.

**Definition of Done (lines 158–169):** Lists completion criteria (tests pass, linting passes, documentation updated, etc.). The new section does not touch completion criteria and does not restate any DoD item. No contradiction.

**Diagnostic Discipline (lines 135–144):** Covers reactive investigation of unexpected system behavior. The new section covers proactive post-check script construction. These are thematically adjacent but functionally distinct. No contradiction.

---

### Point 3 — Insertion point: after Diagnostic Discipline, before Production Safety

**PASS**

GL-005 confirmed section order at lines 135–154:
- `## Diagnostic discipline` ends at line 144 (followed by `---` separator)
- `## Production safety` begins at line 148

The proposed insertion between these two sections is structurally correct. Both neighbors are standalone operational discipline sections, not part of the engineering flow steps. The new section follows the same standalone pattern and is thematically coherent with its neighbors: Diagnostic Discipline governs reactive investigation; Post-Check Script Standards govern proactive verification; Production Safety governs write execution caution. The progression is logical.

---

### Point 4 — Batch-stop rule sufficiency

**ADVISORY**

The current batch-stop rule covers W-2 failure only:

> "If W-2 (section insertion) produces a post-check FAIL — stop immediately. Do not proceed to W-3, W-4, W-5, or W-6."

**Gap identified:** No batch-stop rule covers W-3 failure. If W-2 passes (GL-005 receives the new section) but W-3 fails (changelog entry not appended or malformed), the execution would proceed to W-4, W-5, and W-6 — marking team_tasks id=82 and learning_candidates id=5 and id=7 as processed. The result: GL-005 contains an undocumented amendment, database records report completion, and there is no audit trail for when the change was approved and by whom. This is a partial-write state that would not surface automatically.

**Required correction — add the following to Section 4, Batch-stop rule block, immediately after the existing rule:**

```
> If W-3 (changelog append) produces a post-check FAIL — the changelog entry is not found as the final entry in the Changelog section — stop immediately. Do not proceed to W-4, W-5, or W-6. Report the failure to the Owner before any further action.
```

---

### Point 5 — Post-check requirements PC-1 through PC-6

**ADVISORY**

PC-4, PC-5, and PC-6 are correctly specified. Database queries with exact field and value targets. No issues.

PC-1, PC-2, and PC-3 have a shared problem: the compliance intent (scoped execution, matching exact notation) is documented in a separate paragraph below the table, but the **Method column** does not encode that intent. An executor who reads only the check table — which is the standard execution surface — would implement these as full-file operations, violating LC-5a. A post-check table for a section about post-check quality standards must itself be fully compliant within the table, not in a footnote.

Three specific gaps follow.

---

**PC-1 gap — position verification is underspecified**

Current method: "Read GL-005 and locate `## Post-Check Script Standards` heading"
Current expected result: "Section found at correct position (after Diagnostic Discipline, before Production Safety)"

The method only verifies presence, not position. An executor who finds the heading anywhere in the file (e.g., inserted at the end of the document) would call this PASS. The position requirement in the expected result column is not matched by the method.

**Required correction — replace PC-1 row Method cell with:**

```
Extract the ordered list of `##`-level headings from GL-005. Confirm that `## Post-Check Script Standards` appears immediately after `## Diagnostic discipline` and immediately before `## Production safety` in that ordered list.
```

---

**PC-2 gap — full-file search instead of scoped block search**

Current method: "Read GL-005 and confirm all three subsections present: `### Scope targeting`, `### Format matching`, `### Code structure independence`"

This is a full-file search. It violates LC-5a (scope targeting) and the note below the table acknowledges this should be scoped. The method column must specify the scope.

**Required correction — replace PC-2 row Method cell with:**

```
Extract the `## Post-Check Script Standards` block from GL-005 (from that heading up to the next `##`-level heading). Within that extracted block only, confirm all three subsection headings are present: `### Scope targeting`, `### Format matching`, `### Code structure independence`.
```

---

**PC-3 gap — full-file search instead of scoped Changelog search, and final-entry verification unspecified**

Current method: "Read GL-005 and confirm changelog entry present with date 2026-06-07 and LC-5 + LC-7 reference"

This is a full-file search. The string "2026-06-07" could appear anywhere in the file (e.g., in a future section heading or a comment). Additionally, the expected result requires the entry to be "the last line in Changelog" but the method does not specify how to verify this is the final entry.

**Required correction — replace PC-3 row Method cell with:**

```
Extract the `## Changelog` section from GL-005 (from that heading to end of file). Within that extracted block only, identify the final non-empty line. Confirm it contains '2026-06-07' and references both 'LC-5' and 'LC-7'.
```

---

### Point 6 — Amendment text execution-readiness

**PASS**

The proposed amendment block (Section 3, the markdown code block) is execution-ready.

- Section heading `## Post-Check Script Standards` is unambiguous and correctly formatted for GL-005.
- Three subsections are each self-contained with a declarative rule, specifics, and source-cited rationale.
- Language is consistent with GL-005's existing style and tone.
- No references to dynamic state, external systems, or context not available to an executor.
- No ambiguous terms requiring interpretation.
- Insertion instruction is clear: after `## Diagnostic discipline`, before `## Production safety`.

The use of source citations in parentheses at the end of rationale bullets (e.g., `(Source: LC-5a)`) is a new formatting pattern not present elsewhere in GL-005. This is informative and not stylistically disruptive. It may be removed in a future cleanup without functional effect, but it does not block execution.

---

### Point 7 — Changelog entry governance safety

**PASS**

Proposed changelog entry (Section 8):

```
- 2026-06-07 (Larry, SOP-019 Track 1): Post-Check Script Standards section added. Covers scope targeting, format matching, and code structure independence. Sources: LC-5 (post-check scope and notation fragility) and LC-7 (branch-order-dependent regex). Approved by Owner.
```

No personal name present. Uses role-based reference "Owner" only. Format is consistent with existing GL-005 changelog entries (date, agent identifier, description, approval). Content accurately describes the change being made.

**Observation (no action required):** The two existing GL-005 changelog entries (lines 196–197) contain `Approved by Owner Walter Kamer.` This is pre-existing content outside the scope of this amendment. The proposed entry correctly uses `Approved by Owner.` and is governance-safe.

---

## Summary

| Point | Verdict | Issue |
|---|---|---|
| 1 — Failure mode coverage | PASS | All three modes addressed |
| 2 — No contradiction or duplication | PASS | Complementary to existing sections |
| 3 — Insertion point | PASS | Correct position and flow |
| 4 — Batch-stop rule | ADVISORY | W-3 failure not covered |
| 5 — Post-check methods PC-1 to PC-6 | ADVISORY | PC-1 position unverified; PC-2/PC-3 method column underspecified |
| 6 — Amendment execution-readiness | PASS | Execution-ready as written |
| 7 — Changelog governance safety | PASS | No personal name; role-based reference only |

---

## Required Revisions

Before Owner authorization, Larry must produce v03 of the initiation proposal incorporating the following exact corrections:

**Correction 1 — Section 4, Batch-stop rule block:**
Add the following immediately after the existing W-2 batch-stop rule:

```
> If W-3 (changelog append) produces a post-check FAIL — the changelog entry is not found as the final entry in the Changelog section — stop immediately. Do not proceed to W-4, W-5, or W-6. Report the failure to the Owner before any further action.
```

**Correction 2 — Section 7, PC-1 Method cell:**
Replace with:
```
Extract the ordered list of `##`-level headings from GL-005. Confirm that `## Post-Check Script Standards` appears immediately after `## Diagnostic discipline` and immediately before `## Production safety` in that ordered list.
```

**Correction 3 — Section 7, PC-2 Method cell:**
Replace with:
```
Extract the `## Post-Check Script Standards` block from GL-005 (from that heading up to the next `##`-level heading). Within that extracted block only, confirm all three subsection headings are present: `### Scope targeting`, `### Format matching`, `### Code structure independence`.
```

**Correction 4 — Section 7, PC-3 Method cell:**
Replace with:
```
Extract the `## Changelog` section from GL-005 (from that heading to end of file). Within that extracted block only, identify the final non-empty line. Confirm it contains '2026-06-07' and references both 'LC-5' and 'LC-7'.
```

---

## Verdict

**REQUIRES REVISION BEFORE OWNER AUTHORIZATION**

The proposed GL-005 amendment text (Section 3) is approved as written. The advisories do not concern the amendment content itself — they concern the write plan and post-check specification in the proposal document.

The two advisory items must be corrected in v03 before the proposal is presented to the Owner for write authorization:

1. The missing W-3 batch-stop creates a genuine partial-write risk where GL-005 could receive an undocumented amendment while database records report completion.
2. The underspecified PC methods create a self-consistency failure: a proposal that introduces post-check quality standards must itself present post-check methods that comply with those standards. The current PC-1 through PC-3 method column would direct an executor to perform full-file searches — the exact failure pattern LC-5a prohibits.

Once v03 incorporates Corrections 1 through 4, the proposal may proceed to Owner authorization.

---

Delivered on: 2026-06-07
Delivered at: Iris review — pre-Owner-authorization phase
