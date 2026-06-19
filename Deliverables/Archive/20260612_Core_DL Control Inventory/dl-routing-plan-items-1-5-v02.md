# DL Routing Plan — Items 1–5 (Approved Knowledge Items) — v02

**Date:** 2026-06-12
**Status:** Plan only — not yet authorized for execution

---

## Revision note

This is corrected version v02. It supersedes the earlier routing plan version (`dl-routing-plan-items-1-5.md`).
**Reason:** Owner-requested corrections after review.

**Correction summary:**
- a. Item 2 changed from subfolder target to single markdown file.
- b. Global preflight added.
- c. Sequential execution only.
- d. No new folders of any kind.
- e. Agent handoff removed.

---

## Scope constraint

No execution. No archive. No Batch 2. No new folders of any kind. No extra review files. No deliverable lifecycle sweep. No database writes.

---

## Global preflight rule (applies to every item)

Before any write action:

1. Source file must exist at the stated path.
2. Target parent folder must already exist — do not create it.
3. Target file must not already exist — unless Owner has explicitly approved overwrite.
4. For items with a post-copy link action (Items 1, 3, 4, 5): verify the link target file exists and contains the required Resources section. If the link target file is missing or the Resources section is absent, stop before copying the item.
5. If any check fails: stop, report which check failed and for which item, and do not proceed to the next item.

No item proceeds without all checks passing.

---

## Execution order

Sequential only. No parallel execution.

```
Item 1 → Item 2 → Item 3 → Item 4 → Item 5
```

Each item completes (preflight + write + post-copy) before the next begins.

---

## Item 1 — GR One-pager methodiek

**Source:** `Deliverables/20260513_Geldstroom Regie_One-pager methodiek/one-pager-structuur.md`
**Target:** `Team Knowledge/Geldstroom Regie/Documents/20260513_One-pager structuur.md`

**Preflight:**
- Source `Deliverables/20260513_Geldstroom Regie_One-pager methodiek/one-pager-structuur.md` must exist.
- Target parent `Team Knowledge/Geldstroom Regie/Documents/` must already exist.
- Target file `20260513_One-pager structuur.md` must not already exist.
- Link target `Team Knowledge/Geldstroom Regie/Key Elements/KE-Methode.md` must exist and must contain a Resources section. If missing or Resources section absent: stop before copying this item.

**Action:** Copy source file to target path.
**Post-copy:** Add wikilink `[[20260513_One-pager structuur]]` to `KE-Methode.md` Resources section.
**Batch-stop:** If preflight fails on any check, stop and report to Owner before writing.

---

## Item 2 — Kamer E-commerce Remy Research Week 21

**Source:** `Deliverables/20260519_Kamer E-commerce_Remy Research Week 21/report.md`
**Target:** `Team Knowledge/Kamer E-commerce/Research/20260519_Remy Research Week 21.md`

**Preflight:**
- Source `Deliverables/20260519_Kamer E-commerce_Remy Research Week 21/report.md` must exist.
- Target parent `Team Knowledge/Kamer E-commerce/Research/` must already exist.
- Target file `20260519_Remy Research Week 21.md` must not already exist.

**Action:** Copy source file to target path as a single markdown file. No subfolder created.
**Post-copy:** None.
**Batch-stop:** Global preflight only. No post-copy link action.

---

## Item 3 — Personal Blueprint weekschema en oefeningen

**Source:** `Deliverables/20260530_Personal_Blueprint weekschema en oefeningen/blueprint-starter-plan.md`
**Target:** `PKM/My Life/Key Elements/20260530_Health_Blueprint Starter Plan.md`

**Preflight:**
- Source `Deliverables/20260530_Personal_Blueprint weekschema en oefeningen/blueprint-starter-plan.md` must exist.
- Target parent `PKM/My Life/Key Elements/` must already exist.
- Target file `20260530_Health_Blueprint Starter Plan.md` must not already exist.
- Link target `PKM/My Life/Key Elements/KE-Health.md` must exist and must contain a Resources section. If missing or Resources section absent: stop before copying this item. Do not proceed to Item 4.

**Action:** Copy source file to target path.
**Post-copy:** Add wikilink `[[20260530_Health_Blueprint Starter Plan]]` to `KE-Health.md` Resources section.
**Batch-stop:** If post-copy write to KE-Health.md fails, stop and report to Owner. Do not proceed to Item 4.

---

## Item 4 — Personal Health Monitoring Schema

**Source:** `Deliverables/20260531_Personal_Health Monitoring Schema/health-monitoring-schema.md`
**Target:** `PKM/My Life/Key Elements/20260531_Health_Health Monitoring Schema.md`

**Preflight:**
- Source `Deliverables/20260531_Personal_Health Monitoring Schema/health-monitoring-schema.md` must exist.
- Target parent `PKM/My Life/Key Elements/` must already exist.
- Target file `20260531_Health_Health Monitoring Schema.md` must not already exist.
- Link target `PKM/My Life/Key Elements/KE-Health.md` must exist and must contain a Resources section. If missing or Resources section absent: stop before copying this item. Do not proceed to Item 5.
- Item 3 post-copy write to KE-Health.md must have succeeded before this item begins.

**Action:** Copy source file to target path.
**Post-copy:** Add wikilink `[[20260531_Health_Health Monitoring Schema]]` to `KE-Health.md` Resources section.
**Batch-stop:** If Item 3 post-copy failed, stop before this item. If post-copy write to KE-Health.md fails, stop and report to Owner. Do not proceed to Item 5.

---

## Item 5 — Personal Morning Mobility Routine

**Source:** `Deliverables/20260531_Personal_Morning Mobility Routine/morning-mobility-routine.md`
**Target:** `PKM/My Life/Key Elements/20260531_Health_Morning Mobility Routine.md`

**Preflight:**
- Source `Deliverables/20260531_Personal_Morning Mobility Routine/morning-mobility-routine.md` must exist.
- Target parent `PKM/My Life/Key Elements/` must already exist.
- Target file `20260531_Health_Morning Mobility Routine.md` must not already exist.
- Link target `PKM/My Life/Key Elements/KE-Health.md` must exist and must contain a Resources section. If missing or Resources section absent: stop before copying this item.
- Item 4 post-copy write to KE-Health.md must have succeeded before this item begins.

**Action:** Copy source file to target path.
**Post-copy:** Add wikilink `[[20260531_Health_Morning Mobility Routine]]` to `KE-Health.md` Resources section.
**Batch-stop:** If Item 4 post-copy failed, stop before this item.

---

## Containment boundary

This routing operation produces exactly:

- 5 copied files at their target paths
- 4 wikilink additions (Items 1, 3, 4, 5) to existing files
- No new folders
- No new Deliverable folders
- No agent deliverables
- No extra review files
- No new indexes. Only the explicitly listed wikilink additions to existing knowledge files are allowed.
- No archive actions
- No Batch 2 actions
- No database writes

Any action outside this list requires separate Owner authorization.

---

*G2 artifact — stays inside 20260612_Core_DL Control Inventory*
*Written by Larry — 2026-06-12*
