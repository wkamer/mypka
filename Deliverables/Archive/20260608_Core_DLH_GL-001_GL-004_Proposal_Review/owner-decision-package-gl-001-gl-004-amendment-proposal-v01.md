# Owner Decision Package: GL-001 and GL-004 Amendment Proposal v01

**Review verdict:** Accept with corrections
**Source proposal:** Deliverables/20260608_Core_DLH GL-001 and GL-004 Amendment Proposal v01/gl-amendment-proposal-v01.md
**Review report:** Deliverables/20260608_Core_DLH_GL-001_GL-004_Proposal_Review/review-report-gl-001-gl-004-amendment-proposal-v01.md
**Date:** 2026-06-08

---

## 1. Verdict Summary

The proposal correctly implements the Task 85 and Task 86 decisions and is compatible with
all governance instruments reviewed (GL-016, GL-017, SOP-016, SOP-017, SOP-019).

Two mandatory corrections must be applied before implementation. One advisory item requires
an Owner decision before the corrected proposal (v02) can be written.

The proposal cannot be implemented as-is.

---

## 2. Mandatory Corrections (block implementation until resolved)

### C-1: Update the existing File Names by Type table row

**Problem:** GL-001 already has a row in the File Names by Type table defining deliverable
folder naming as `YYYYMMDD_Domain_description/`. The proposal adds a new section defining
`YYYYMMDD_Domain_[WorkstreamCode ]ArtifactDescription/` without updating the existing row.
After implementation, GL-001 would have two conflicting definitions. SSOT violation.

**Required fix in v02:** W-1 adds a 4th change — update the File Names by Type table row:

Old row:
```
| Deliverable | `YYYYMMDD_Domain_description/` | `20260509_Kamer E-commerce_US store audit/` |
```

New row:
```
| Deliverable | `YYYYMMDD_Domain_[WorkstreamCode ]ArtifactDescription/` | `20260607_Core_DLH Discovery and Proposal/` |
```

The post-check plan must gain a corresponding check verifying this row was updated.

---

### C-2: Reformat "Text to insert (exact)" block to avoid nested markdown fences

**Problem:** Section 3.1 wraps the GL-001 insertion text in a triple-backtick code fence.
The insertion text itself contains triple-backtick fences (for the format string examples).
Markdown parsers close the outer fence at the first inner fence, producing a corrupted
rendering. An implementor reading rendered markdown receives incomplete and malformed "exact
text."

**Required fix in v02:** Section 3.1 must use a fence-safe representation for the outer
wrapper. Recommended approach: present the "Text to insert" as plain markdown prose sections
with a clear boundary marker (e.g., `<!-- BEGIN INSERT -->` and `<!-- END INSERT -->`
HTML comment markers, or 4-space indented blocks for the outer wrapper), not as a
triple-backtick code fence containing other triple-backtick code fences.

---

## 3. Advisory Item (Owner decision required before v02 is written)

### F-3: "Silent overwrite is not permitted" — keep in GL-001 or remove?

**Problem:** The GL-001 Versioning section contains "Silent overwrite is not permitted.
Corrections to governance deliverables must produce a new versioned file. See SOP-015."
This is a procedural prohibition. GL-001 is a naming guideline. Task 78 was created to add
this prohibition to SOP-015.

**Three options:**

| Option | Description | Implication |
|---|---|---|
| A — Keep as-is | Prohibition stays in GL-001, also appears in SOP-015 when Task 78 is done | Two instruments carry the same rule; GL-001 is the earlier statement |
| B — Remove from GL-001 | Remove the prohibition; keep only naming/format rules (syntax, Correction Note format, same-folder rule) | Clean GL-001 scope; prohibition lives in SOP-015 only after Task 78 |
| C — Qualify scope in GL-001 | Add scope qualifier: "Corrections to governance deliverables (proposals, reports, closure records, write-lists) must produce a new versioned file" | Prohibition stays but its scope is defined within GL-001 |

**Owner decision:** Select A, B, or C before Larry writes v02.

---

## 4. Mode 3 Limitation Notice

This review was conducted as Mode 3 (Single-System Fallback) because Larry is both the
producer and reviewer of this proposal. Per SOP-016 Section 4, SOP or GL proposals reviewed
by the same agent that produced them should use Mode 2 (second specialist as reviewer) or
Mode 1 (external reviewer).

**Owner option:** Request an independent review by a second specialist before authorizing
implementation. This eliminates the role overlap limitation. If independent review is not
required, proceed with the current review findings.

---

## 5. Exact Owner Responses

### If accepting with corrections and proceeding to v02

Select a response:

**Response A (Accept — keep "silent overwrite" in GL-001):**
> "Review accepted. Proceed with corrections C-1 and C-2. For F-3: keep the prohibition in GL-001 as-is (Option A). Produce GL-001 and GL-004 Amendment Proposal v02."

**Response B (Accept — remove "silent overwrite" from GL-001):**
> "Review accepted. Proceed with corrections C-1 and C-2. For F-3: remove the prohibition from GL-001 (Option B). Produce GL-001 and GL-004 Amendment Proposal v02."

**Response C (Accept — qualify scope in GL-001):**
> "Review accepted. Proceed with corrections C-1 and C-2. For F-3: add the scope qualifier (Option C). Produce GL-001 and GL-004 Amendment Proposal v02."

**Response D (Accept — request independent second review first):**
> "Review accepted but I want an independent second review before v02. Assign a second specialist."

### If rejecting the proposal

> "Reject GL-001 and GL-004 Amendment Proposal v01. [State reason]. Do not proceed to v02 until further instruction."

---

## 6. Recommended Next Step

Owner selects one of the Accept responses above (A, B, or C), resolving the F-3 decision.

Larry produces GL-001 and GL-004 Amendment Proposal v02 incorporating C-1 and C-2.

v02 returns for a new review gate (the corrected exact text and SSOT fix must be verified
before implementation is authorized). If the Owner is satisfied with v02 and no further
review gaps are found, implementation may proceed.

Estimated scope of v02 changes:
- Add W-1 4th change (table row update)
- Add corresponding post-check for table row
- Reformat Section 3.1 to avoid nested fences
- Apply F-3 decision to Versioning section

---

*Delivered on: 2026-06-08*
*Delivered at: Deliverables/20260608_Core_DLH_GL-001_GL-004_Proposal_Review/owner-decision-package-gl-001-gl-004-amendment-proposal-v01.md*
