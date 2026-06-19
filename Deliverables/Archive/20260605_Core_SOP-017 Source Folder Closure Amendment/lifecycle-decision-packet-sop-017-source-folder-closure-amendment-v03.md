# Lifecycle Decision Packet — SOP-017 Amendment: Source Folder Closure After Archive

**Document type:** Lifecycle Decision Packet (DP-6 preparation)
**Version:** v03 (supersedes v02)
**Prepared by:** Larry (Team Orchestrator)
**Date:** 2026-06-05
**Covers:** All deliverables in `Deliverables/20260605_Core_SOP-017 Source Folder Closure Amendment/`
**Status:** Proposal only. No lifecycle processing has occurred. No files have been archived, moved, or modified.

---

> **PROPOSAL ONLY.**
> Nothing in this document is implemented, active, or authoritative until the Owner explicitly approves it at DP-6. No files are moved, archived, or deleted by this document. No database writes occur. No indexes are updated. No governance files are modified. Lifecycle processing requires separate DP-6 Owner authorization.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v02 | 2026-06-05 | Initial lifecycle decision packet — 11 artifacts |
| v03 | 2026-06-05 | Corrected: added lifecycle decision packets v02 and v03 to archive scope; total artifact count updated from 11 to 13; v02 superseded by v03 |

---

## Context

The SOP-017 amendment flow for "Source Folder Closure After Archive" has completed through DP-5:

- SOP-017 amended and live (DP-4, confirmed)
- Implementation report accepted (DP-5, confirmed)
- Future graduation candidate recorded in DP-5 record
- Lifecycle processing not yet authorized (DP-6 required)

This packet proposes lifecycle decisions for all 13 deliverables in the source folder and provides the source folder closure plan required by the now-live SOP-017 Section 10 and EX-8.

**v02 correction note:** v02 of this packet listed 11 artifacts and proposed archiving those 11. It omitted both lifecycle decision packets from the archive scope. This would have left v02 and v03 behind in the source folder after the 11 archive moves, preventing the source folder from being confirmed empty and breaking the Source Folder Closure rule on its first use. v03 corrects this by including all 13 artifacts.

---

## Source Folder Contents (13 files)

| # | Filename | Type | Date created |
|---|---|---|---|
| 1 | `sop-017-amendment-source-folder-closure-v01.md` | Amendment proposal v01 | 2026-06-05 |
| 2 | `sop-017-amendment-source-folder-closure-v02.md` | Amendment proposal v02 (accepted, implemented) | 2026-06-05 |
| 3 | `review-context-packet-sop-017-source-folder-closure-amendment-v01.md` | Review context packet v01 | 2026-06-05 |
| 4 | `review-context-packet-sop-017-source-folder-closure-amendment-v02.md` | Review context packet v02 | 2026-06-05 |
| 5 | `review-context-packet-sop-017-source-folder-closure-amendment-v03.md` | Review context packet v03 (final, used for review gate) | 2026-06-05 |
| 6 | `review-gate-findings-sop-017-source-folder-closure-amendment-v01.md` | Review Gate findings v01 | 2026-06-05 |
| 7 | `review-gate-findings-sop-017-source-folder-closure-amendment-v02.md` | Review Gate findings v02 (accepted) | 2026-06-05 |
| 8 | `dp-3-owner-decision-sop-017-source-folder-closure-amendment-v02.md` | DP-3 Owner Decision Record | 2026-06-05 |
| 9 | `dp-4-owner-decision-sop-017-source-folder-closure-amendment-v02.md` | DP-4 Owner Decision Record | 2026-06-05 |
| 10 | `implementation-report-sop-017-source-folder-closure-amendment-v02.md` | Implementation report (accepted at DP-5) | 2026-06-05 |
| 11 | `dp-5-owner-decision-sop-017-source-folder-closure-amendment-v02.md` | DP-5 Owner Decision Record (contains future graduation candidate) | 2026-06-05 |
| 12 | `lifecycle-decision-packet-sop-017-source-folder-closure-amendment-v02.md` | Lifecycle decision packet v02 (superseded by v03) | 2026-06-05 |
| 13 | `lifecycle-decision-packet-sop-017-source-folder-closure-amendment-v03.md` | Lifecycle decision packet v03 (this document, accepted) | 2026-06-05 |

---

## Lifecycle Decision Proposals per Artifact

---

### Artifact 1 — `sop-017-amendment-source-folder-closure-v01.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Superseded — replaced by v02 |
| Authoritative governance artifact | No |
| Authoritative audit artifact | No — intermediate working artifact only |
| Should be archived | Yes |
| Reusable knowledge to extract | No |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R2 (Supersession), R10 (intermediate working artifact) |

**Recommendation:** Archive. v01 was superseded when v02 was accepted and implemented. No standalone authoritative value. No knowledge extraction required.

---

### Artifact 2 — `sop-017-amendment-source-folder-closure-v02.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Accepted as Done — the accepted and implemented amendment text |
| Authoritative governance artifact | Yes — canonical text of the amendment as implemented in SOP-017 |
| Authoritative audit artifact | Yes — the exact text that was approved and executed at DP-4 |
| Should be archived | Yes, with Authoritative marker assigned and recorded |
| Reusable knowledge to extract | Optional — governance reference value; Owner decides whether a separate R4 record is warranted |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — Authoritative marker assignment confirmation; formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R1 (Authoritative marker), R4 (Governance reference), R8 (Archive eligible) |

**Recommendation:** Assign Authoritative marker (record in execution report), then archive. The amendment text is preserved in SOP-017 itself; v02 is the authoritative source for the proposal-as-submitted record.

---

### Artifact 3 — `review-context-packet-sop-017-source-folder-closure-amendment-v01.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Superseded — replaced by v02 |
| Authoritative governance artifact | No |
| Authoritative audit artifact | No — intermediate working artifact |
| Should be archived | Yes |
| Reusable knowledge to extract | No |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R2 (Supersession), R10 (intermediate working artifact) |

**Recommendation:** Archive. v01 review context packet was superseded by v02. No standalone value.

---

### Artifact 4 — `review-context-packet-sop-017-source-folder-closure-amendment-v02.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Superseded — replaced by v03 |
| Authoritative governance artifact | No |
| Authoritative audit artifact | No — intermediate working artifact |
| Should be archived | Yes |
| Reusable knowledge to extract | No |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R2 (Supersession), R10 (intermediate working artifact) |

**Recommendation:** Archive. v02 review context packet was superseded by v03. No standalone value.

---

### Artifact 5 — `review-context-packet-sop-017-source-folder-closure-amendment-v03.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Accepted as Done — final review context used for the accepted Review Gate |
| Authoritative governance artifact | Yes — canonical review context for this amendment's Review Gate |
| Authoritative audit artifact | Yes — the packet used in the accepted Review Gate that produced the accepted v02 findings |
| Should be archived | Yes, with Authoritative marker assigned and recorded |
| Reusable knowledge to extract | Optional — review structure is documented in SOP-016; no separate extraction needed unless Owner requests it |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — Authoritative marker assignment confirmation; formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R1 (Authoritative marker), R4 (Governance reference), R8 (Archive eligible) |

**Recommendation:** Assign Authoritative marker (record in execution report), then archive. v03 is the authoritative review context record for this amendment flow.

---

### Artifact 6 — `review-gate-findings-sop-017-source-folder-closure-amendment-v01.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Superseded — replaced by v02 findings |
| Authoritative governance artifact | No |
| Authoritative audit artifact | No — superseded by v02 |
| Should be archived | Yes |
| Reusable knowledge to extract | No |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R2 (Supersession), R10 (intermediate working artifact) |

**Recommendation:** Archive. v01 findings were superseded when the v01 proposal was revised to v02 after the findings were applied.

---

### Artifact 7 — `review-gate-findings-sop-017-source-folder-closure-amendment-v02.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Accepted as Done — the accepted Review Gate findings for the accepted v02 proposal |
| Authoritative governance artifact | Yes — canonical review gate outcome for this amendment |
| Authoritative audit artifact | Yes — the accepted findings that drove the v02 corrections |
| Should be archived | Yes, with Authoritative marker assigned and recorded |
| Reusable knowledge to extract | Optional — review gate pattern may be relevant for R4 governance reference; Owner decides |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — Authoritative marker assignment confirmation; formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R1 (Authoritative marker), R4 (Governance reference), R8 (Archive eligible) |

**Recommendation:** Assign Authoritative marker (record in execution report), then archive. These findings are the governance record of the Review Gate outcome.

---

### Artifact 8 — `dp-3-owner-decision-sop-017-source-folder-closure-amendment-v02.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Accepted as Done — DP-3 Owner acceptance of the v02 proposal |
| Authoritative governance artifact | Yes — governance decision record |
| Authoritative audit artifact | Yes — Owner authorization point for the amendment proposal |
| Should be archived | Yes, with Authoritative marker assigned and recorded |
| Reusable knowledge to extract | No |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — Authoritative marker assignment confirmation; formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R1 (Authoritative marker), R4 (Governance reference), R8 (Archive eligible) |

**Recommendation:** Assign Authoritative marker (record in execution report), then archive. DP-3 record is a durable governance decision point.

---

### Artifact 9 — `dp-4-owner-decision-sop-017-source-folder-closure-amendment-v02.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Accepted as Done — DP-4 Owner implementation authorization |
| Authoritative governance artifact | Yes — the authorization that permitted SOP-017 to be modified |
| Authoritative audit artifact | Yes — highest-risk authorization point in this flow |
| Should be archived | Yes, with Authoritative marker assigned and recorded |
| Reusable knowledge to extract | No |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — Authoritative marker assignment confirmation; formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R1 (Authoritative marker), R4 (Governance reference), R8 (Archive eligible) |

**Recommendation:** Assign Authoritative marker (record in execution report), then archive. DP-4 is the canonical record of implementation authorization.

---

### Artifact 10 — `implementation-report-sop-017-source-folder-closure-amendment-v02.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Accepted as Done — accepted at DP-5 |
| Authoritative governance artifact | Yes — canonical record of what was changed in SOP-017 and all post-checks |
| Authoritative audit artifact | Yes — the definitive audit record for this amendment execution |
| Should be archived | Yes, with Authoritative marker assigned and recorded |
| Reusable knowledge to extract | Optional — the post-check structure and amendment application method could be a R4 governance reference; Owner decides |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — Authoritative marker assignment confirmation; formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R1 (Authoritative marker), R4 (Governance reference), R8 (Archive eligible) |

**Recommendation:** Assign Authoritative marker (record in execution report), then archive. This report is the single most important audit artifact in the flow.

---

### Artifact 11 — `dp-5-owner-decision-sop-017-source-folder-closure-amendment-v02.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Accepted as Done — DP-5 Owner acceptance of implementation report |
| Authoritative governance artifact | Yes — governance decision record; also contains the future graduation candidate |
| Authoritative audit artifact | Yes |
| Should be archived | Yes, with Authoritative marker assigned and recorded; see Future Graduation Candidate section below |
| Reusable knowledge to extract | Yes — future graduation candidate must be preserved before or during archive |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — Authoritative marker assignment confirmation; future graduation candidate preservation plan confirmation; formal archive proposal per EX-6 |
| Risk level | Medium — contains the future graduation candidate which must not be lost |
| Decision rules applied | R1 (Authoritative marker), R4 (Governance reference), R8 (Archive eligible) |

**Recommendation:** Assign Authoritative marker (record in execution report), then archive. Before archiving, confirm the future graduation candidate is preserved per the plan below. The archived DP-5 record remains the durable source; the lifecycle execution report serves as the forward-reference governance record for the candidate.

---

### Artifact 12 — `lifecycle-decision-packet-sop-017-source-folder-closure-amendment-v02.md`

| Field | Proposed value |
|---|---|
| Lifecycle status | Superseded — replaced by v03 (this document) |
| Authoritative governance artifact | No |
| Authoritative audit artifact | No — intermediate working artifact; v03 is the accepted version |
| Should be archived | Yes |
| Reusable knowledge to extract | No |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R2 (Supersession), R10 (intermediate working artifact) |

**Recommendation:** Archive. v02 was superseded when the Owner requested the correction that produced v03. v02 omitted itself and v03 from the archive scope; v03 corrects this. No standalone value beyond what v03 contains.

---

### Artifact 13 — `lifecycle-decision-packet-sop-017-source-folder-closure-amendment-v03.md` (this document)

| Field | Proposed value |
|---|---|
| Lifecycle status | Accepted as Done (upon DP-6 Owner authorization) |
| Authoritative governance artifact | Yes — the accepted lifecycle decision packet for this amendment flow |
| Authoritative audit artifact | Yes — the governance record of the proposed lifecycle decisions |
| Should be archived | Yes, with Authoritative marker assigned and recorded |
| Reusable knowledge to extract | Optional — the self-referential artifact inclusion pattern is a governance learning; Owner decides whether to record as R4 governance reference |
| Proposed destination | `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/` |
| Owner approval required | Yes — Authoritative marker assignment confirmation; formal archive proposal per EX-6 |
| Risk level | Low |
| Decision rules applied | R1 (Authoritative marker), R4 (Governance reference), R8 (Archive eligible) |

**Recommendation:** Assign Authoritative marker (record in execution report), then archive. This document is the accepted lifecycle decision packet. Including itself in the archive scope is intentional and necessary: after all 13 artifacts are archived, the source folder will be empty and can be deleted per the Source Folder Closure rule.

**Self-reference note:** It is structurally correct for a lifecycle decision packet to include itself in the archive scope. The packet is a governance artifact in the same source folder. Omitting it would leave it behind after all other artifacts are archived, breaking the Source Folder Closure rule. This is the same logic that required correcting v02.

---

## Future Graduation Candidate — Preservation Plan

**Candidate title:** Strict file-based governance artifact flow for auto-detection and auto-processing

**Source:** `dp-5-owner-decision-sop-017-source-folder-closure-amendment-v02.md` — Future Graduation Candidate section

### Status constraints (carry forward unchanged)

- The candidate is not approved for implementation.
- The candidate is not a backlog item unless Owner explicitly approves backlog creation later.
- The candidate should not be worked on during the current active governance flow.
- No auto-detection or auto-processing work may be started as part of this lifecycle execution.

### Preservation approach

When the lifecycle execution report is written (after DP-6 authorization), the following must occur:

1. The lifecycle execution report records the future graduation candidate under **Decision rules applied: R4 (Governance reference)** with the Indexed marker assigned.
2. The full candidate text (title, observation, candidate scope, specific process lessons, status) is reproduced verbatim in the execution report as a governance reference, not summarized.
3. The execution report serves as the forward-reference governance record for the candidate. When the DP-5 record is archived, the execution report provides the live durable pointer.
4. No separate file is created for the candidate at this time. The execution report is the preservation vehicle.

### What happens when DP-5 is archived

The DP-5 record is moved to `Deliverables/Archive/`. It remains retrievable. The lifecycle execution report in the separate execution folder (see Source Folder Closure Plan below) holds the Indexed marker and the forward reference. The candidate is not lost.

### Owner decision required

Before archiving the DP-5 record, the Owner must confirm: "The future graduation candidate is preserved in the lifecycle execution report. I accept the archive of the DP-5 record." This confirmation is a required sub-step of the DP-6 authorization for artifact 11.

---

## Source Folder Closure Plan

This section is required by SOP-017 Section 10 (Source Folder Closure) and EX-8, now live in the amended SOP-017.

### Lifecycle execution report location

The lifecycle execution report must be written to a separate deliverables folder outside the source folder:

**Required path:** `Deliverables/20260605_Core_SOP-017 Amendment Lifecycle Execution/`

**Rationale:** If the lifecycle execution report were placed inside the source folder, it would remain after all 13 artifacts are archived, preventing the source folder from being confirmed empty. Writing the execution report to a separate folder avoids this problem: after all 13 authorized archive moves complete, the source folder is checked and expected to be empty. The execution report exists outside the archive scope.

**This path must be confirmed by the Owner at DP-6 before any archive moves begin.**

### Step sequence after authorized archive moves complete

1. After all 13 authorized archive moves have been executed (artifacts 1 through 13 moved to `Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/`), the Maintainer checks the source folder using a hidden-file-aware method:

   ```
   ls -A "Deliverables/20260605_Core_SOP-017 Source Folder Closure Amendment/"
   ```

   Or the platform-equivalent command that surfaces hidden files (dotfiles, .DS_Store, etc.).

2. **If the source folder is empty** (no files returned, including hidden files): delete the source folder. Record in the lifecycle execution report: source folder path, confirmation that the folder was empty, confirmation that it was deleted (execution report fields 14 through 18 per SOP-017 Section 16).

3. **If the source folder is not empty**: do not delete. List all remaining files in the execution report. Surface the remaining files to the Owner with a brief description of each. Do not claim lifecycle cleanup complete until the Owner has made a decision about each remaining file.

4. Lifecycle cleanup may not be claimed Done until the source folder check has been performed, the result has been recorded in the execution report, and (if files remain) the Owner has made a decision about each remaining file.

---

## Summary of Proposed Archive Scope

All 13 artifacts are proposed for archiving to:
`Deliverables/Archive/20260605_Core_SOP-017 Source Folder Closure Amendment/`

| # | Filename | Authoritative marker | Archive |
|---|---|---|---|
| 1 | `sop-017-amendment-source-folder-closure-v01.md` | No | Yes |
| 2 | `sop-017-amendment-source-folder-closure-v02.md` | Yes | Yes |
| 3 | `review-context-packet-sop-017-source-folder-closure-amendment-v01.md` | No | Yes |
| 4 | `review-context-packet-sop-017-source-folder-closure-amendment-v02.md` | No | Yes |
| 5 | `review-context-packet-sop-017-source-folder-closure-amendment-v03.md` | Yes | Yes |
| 6 | `review-gate-findings-sop-017-source-folder-closure-amendment-v01.md` | No | Yes |
| 7 | `review-gate-findings-sop-017-source-folder-closure-amendment-v02.md` | Yes | Yes |
| 8 | `dp-3-owner-decision-sop-017-source-folder-closure-amendment-v02.md` | Yes | Yes |
| 9 | `dp-4-owner-decision-sop-017-source-folder-closure-amendment-v02.md` | Yes | Yes |
| 10 | `implementation-report-sop-017-source-folder-closure-amendment-v02.md` | Yes | Yes |
| 11 | `dp-5-owner-decision-sop-017-source-folder-closure-amendment-v02.md` | Yes | Yes (after future graduation candidate preservation confirmed) |
| 12 | `lifecycle-decision-packet-sop-017-source-folder-closure-amendment-v02.md` | No | Yes |
| 13 | `lifecycle-decision-packet-sop-017-source-folder-closure-amendment-v03.md` | Yes | Yes |

**Artifacts with Authoritative marker to assign before archiving:** 2, 5, 7, 8, 9, 10, 11, 13 (8 artifacts)

**All 13 artifacts require a formal archive proposal per EX-6 before any file is moved.**

**After all 13 archive moves complete:** source folder checked with `ls -A` or platform-equivalent. If empty, source folder deleted. If not empty, remaining files listed and surfaced to Owner.

---

## Owner Decision Required at DP-6

The Owner must confirm the following before lifecycle execution may begin:

| Item | Decision required |
|---|---|
| Archive all 13 artifacts as proposed | Yes / No / amend |
| Authoritative marker for artifacts 2, 5, 7, 8, 9, 10, 11, 13 | Confirm per artifact |
| Future graduation candidate preserved in execution report (R4, Indexed marker) | Confirm before artifact 11 is archived |
| Lifecycle execution report destination folder | Confirm `Deliverables/20260605_Core_SOP-017 Amendment Lifecycle Execution/` or specify alternative |
| Source folder closure check method | Confirm `ls -A` or specify platform-equivalent |
| Source folder deletion after confirmed empty | Confirm authorized |

No lifecycle execution may begin without explicit Owner DP-6 authorization covering all of the above items.

---

Delivered on: 2026-06-05
Delivered at: Deliverables/20260605_Core_SOP-017 Source Folder Closure Amendment/
