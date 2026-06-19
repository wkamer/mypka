# Iterative D-Folder Control — Pilot A Proposal — v01

**Date:** 2026-06-12
**Prepared by:** Larry, Team Orchestrator
**Type:** Pilot proposal — read-only
**Placement:** G2 — file inside `20260612_Core_DL Control Inventory/`

**Read-only declaration:** No archive, no routing, no lifecycle updates, no sweep,
no Batch 2, no Learning Candidate triage, no dashboard work, no folder creation,
no file creation beyond this proposal.

---

## 1. Baseline Note

**Source document:** `20260612_d-folder-operating-model-and-current-inventory-v01.md`

**Status of v01:** Accepted as read-only baseline snapshot only.
The operating model section in v01 is not final governance. It is a draft for
iterative refinement based on what works in practice — starting with Pilot A.

**Last confirmed active D-folder count (from v01):** 43

**Known staleness in v01:**

| Item | v01 state | Actual state |
|---|---|---|
| Items 17-21 (5 domain knowledge folders: GR, KE, Personal x3) | `owner_decision_needed` — routing pending | Routing Items 1-5 has been executed and closed. These items are no longer pending routing decisions. |
| Sub-batch A as proposed in v01 | 6 folders proposed | Violates v01's own stop rule: max 5 folders per batch. Proposal is invalid as written. |

**Corrected current count:** Not re-verified in this task. The last confirmed baseline is 43.
If the 5 routed domain knowledge folders (items 17-21) have since been archived, the actual
count may be lower. Owner to confirm if a fresh count is needed before Pilot A approval.

---

## 2. Pilot Principle

The purpose of Pilot A is to validate the archive process for D-folders on a small,
unambiguous set before scaling. The rule-set in v01 is refined only after Pilot A
produces confirmed results.

**Four steps — no shortcuts:**

1. **Propose** — present the pilot folder list with preflight checks (this document)
2. **Owner approves** — explicit confirmation before any action
3. **Execute** — archive only the approved folders, one at a time, preflight first
4. **Verify** — confirm filesystem state, lifecycle DB, and folder count after execution

**Operating rules for Pilot A:**

- Maximum 5 folders
- Process artifacts only — no folder requiring routing, no `registered_but_unclear` folder,
  no folder referenced by a live SOP, GL, or CLAUDE.md
- Owner approves the full list before execution starts
- Execution halts immediately on any stop condition (see Section 4)
- Lifecycle DB updates happen after physical archive, not before
- No batch-level authorization carries over to subsequent batches

---

## 3. Proposed Pilot A — 5 Folders

These five folders are the safest available process artifacts.
All are confirmed `ready_for_archive` in v01. None require routing. None are
`registered_but_unclear`. None are referenced by live governance documents.

| # | Folder | Lifecycle record | Current DB state |
|---|---|---|---|
| 1 | `20260612_Core_DL Batch 1 Archive Execution Plan` | Yes (id 70, type: working_artifact) | active |
| 2 | `20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal` | Yes (id 71, type: triage_document) | active |
| 3 | `20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal` | Yes (type: proposal) | pending |
| 4 | `20260607_Core_DL Smoke Test Recovery Report` | Yes | pending |
| 5 | `20260607_Core_Deliverable Lifecycle Hardening Phase B Triage` | Yes | pending |

---

## 4. Per-Folder Detail

### Folder 1 — `20260612_Core_DL Batch 1 Archive Execution Plan`

**Why it is safe:**
Batch 1 (LC chain archive) is complete. This folder contains the execution plan for that
batch. The underlying work is done. No live SOP or GL references this folder. Pure process
artifact from a closed action.

**Preflight checks required:**
- Confirm filesystem: folder exists in active `Deliverables/`
- Confirm lifecycle record id 70 is present and `state_gl017 = 'active'`
- Confirm no file inside the folder is referenced by any live SOP, GL, or CLAUDE.md
- Confirm Batch 1 execution is confirmed complete (no open items)

**Expected action if approved:** `mv` folder to `Deliverables/Archive/`. Update lifecycle
record: `state_gl017 = 'archived'`, `owner_decision = 'archive'`.

**Stop condition:** Halt if any preflight check fails. Halt if folder contents reveal an
open item or unresolved condition not visible from the folder name alone.

---

### Folder 2 — `20260612_Core_DL Post-Batch-1 Status Check and Batch 2 Proposal`

**Why it is safe:**
This folder was created to check status after Batch 1 and propose a Batch 2. The operating
model deliverable (v01) and this pilot proposal supersede it. The `Batch 2` proposal it
contains is not the execution path — iterative pilots replace it. DB note already flags
it as a GL-017 correction candidate.

**Preflight checks required:**
- Confirm filesystem: folder exists in active `Deliverables/`
- Confirm lifecycle record id 71 is present
- Confirm no file inside is referenced by any live SOP, GL, or CLAUDE.md
- Confirm the `dl-routing-plan-items-1-5-v02.md` inside the Control Inventory (not this folder)
  is the authoritative routing reference and this folder adds no unique content

**Expected action if approved:** `mv` folder to `Deliverables/Archive/`. Update lifecycle
record: `state_gl017 = 'archived'`, `owner_decision = 'archive'`.

**Stop condition:** Halt if folder contains any file that is the SSOT for a still-active
decision or open item.

---

### Folder 3 — `20260607_Core_Deliverable Lifecycle Phase 1 Smoke Test Proposal`

**Why it is safe:**
The DLH Phase 1 smoke test was executed. The recovery report (Folder 4) documents the
outcome. This proposal is a pre-execution planning artifact from a completed chain. Phase B
and Phase C both post-date it. No live governance rule references this proposal as authoritative.

**Preflight checks required:**
- Confirm lifecycle record is present and `state_gl017 = 'pending_lifecycle_decision'`
- Confirm smoke test execution is confirmed complete (recovery report exists and is complete)
- Confirm no SOP or GL references this folder as a live document
- Confirm no open item in any team_task points to this folder

**Expected action if approved:** `mv` folder to `Deliverables/Archive/`. Update lifecycle
record: `state_gl017 = 'archived'`, `owner_decision = 'archive'`.

**Stop condition:** Halt if smoke test outcome is disputed or if recovery is not confirmed complete.

---

### Folder 4 — `20260607_Core_DL Smoke Test Recovery Report`

**Why it is safe:**
The recovery report documents the outcome of the smoke test and the corrective actions taken.
All corrective actions from this report are complete (they informed Phase B and Phase C).
This is a historical record of a closed incident. Paired with Folder 3.

**Preflight checks required:**
- Confirm lifecycle record is present and `state_gl017 = 'pending_lifecycle_decision'`
- Confirm all corrective actions listed in the report are implemented
- Confirm no open team_task references this report as a source of a pending action
- Confirm Folder 3 preflight passed before proceeding to this folder

**Expected action if approved:** `mv` folder to `Deliverables/Archive/`. Update lifecycle
record: `state_gl017 = 'archived'`, `owner_decision = 'archive'`.

**Stop condition:** Halt if any corrective action in the report is not confirmed implemented.

---

### Folder 5 — `20260607_Core_Deliverable Lifecycle Hardening Phase B Triage`

**Why it is safe:**
Phase B of DLH is definitively complete. Phase C (proposal in active folder) supersedes it.
The Phase B triage produced outputs that informed Phase C design. Those outputs have been
absorbed. The folder is a closed phase artifact with no live dependency.

**Preflight checks required:**
- Confirm lifecycle record is present and `state_gl017 = 'pending_lifecycle_decision'`
- Confirm Phase C proposal exists in active `Deliverables/` (confirms Phase B is superseded)
- Confirm no SOP or GL references this Phase B triage as authoritative
- Confirm no open team_task references this folder

**Expected action if approved:** `mv` folder to `Deliverables/Archive/`. Update lifecycle
record: `state_gl017 = 'archived'`, `owner_decision = 'archive'`.

**Stop condition:** Halt if Phase C is confirmed complete and Phase C's own folder would be
a better candidate to archive instead (re-sequence the batch in that case).

---

**Excluded from Pilot A — and why:**

| Folder | Reason excluded |
|---|---|
| `20260607_Core_Deliverable Lifecycle Hardening Discovery and Proposal` | Initial discovery document; may have residual reference value as the chain origin. Reserve for second pilot. |
| `20260608_Core_*` UMC chain (8 folders) | Larger chain; GL-013 implementation not confirmed. Defer to a later batch after Pilot A verified. |
| Items 17-21 (domain knowledge folders) | Routing confirmed complete — but archive eligibility for these folders depends on Owner confirming routing is done and source folders can now close. Separate decision required. |

---

## 5. Verification Checklist

To be completed after Pilot A execution, if Owner approves. Not completed in this task.

| Check | Expected result | Verified |
|---|---|---|
| Folder 1 moved to Archive/ | Yes | — |
| Folder 2 moved to Archive/ | Yes | — |
| Folder 3 moved to Archive/ | Yes | — |
| Folder 4 moved to Archive/ | Yes | — |
| Folder 5 moved to Archive/ | Yes | — |
| Lifecycle records updated (5 rows) | state_gl017 = 'archived', owner_decision = 'archive' | — |
| No new folders created | 0 new folders | — |
| No routing performed | Confirmed | — |
| No dashboard work | Confirmed | — |
| No Learning Candidate triage | Confirmed | — |
| No Batch 2 execution | Confirmed | — |
| No unexpected files in active Deliverables/ | 0 unexpected | — |
| Active D-folder count after execution | 43 minus 5 = 38 (if baseline was 43); adjust if routing of items 17-21 already reduced count | — |

---

## 6. Why This Is Safer Than the Original 6-Folder Sub-batch A

| Dimension | v01 Sub-batch A | Pilot A (this document) |
|---|---|---|
| Folder count | 6 — violates the stop rule in v01 itself | 5 — within the stated max |
| Operating model status | Treated as execution-ready | Treated as draft; pilot validates before rules are finalized |
| Rule-set status | Applied as if final | Rule-set is refined after pilot results |
| Items 17-21 | Listed as included context | Correctly excluded — routing complete, separate archive decision needed |
| Discovery document | Included | Excluded — slightly higher ambiguity, deferred |
| Iteration model | Single batch | Preflight per folder, stop conditions explicit, verify before next batch |

---

## 7. Open Owner Decisions

Before Pilot A can be executed:

1. **Approve Pilot A folder list** (5 folders listed above)?
2. **Confirm current D-folder count** — if routing of items 17-21 was followed by archiving
   those 5 folders, the baseline is no longer 43. Fresh count needed before execution.
3. **Confirm Phase C status** — is `20260608_Core_DL Hardening Phase C Proposal v01` still
   active work? This affects sequencing for later batches, not Pilot A itself.

Items 17-21 routing decisions are confirmed closed. No decision needed on those.

---

Delivered on: 2026-06-12
Delivered at: `Deliverables/20260612_Core_DL Control Inventory/20260612_iterative-d-folder-control-pilot-a-v01.md`
