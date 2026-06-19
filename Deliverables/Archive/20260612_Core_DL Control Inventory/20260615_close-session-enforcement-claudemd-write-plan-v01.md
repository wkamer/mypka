# Close-Session Enforcement — CLAUDE.md Write Plan v01

**Date:** 2026-06-15
**Author:** Larry
**Status:** Pending Owner authorization
**Source proposal:** `Deliverables/20260612_Core_DL Control Inventory/20260615_close-session-workflow-enforcement-proposal-v01.md`

---

## 0. Preflight / Batch-Stop Condition

Before editing CLAUDE.md, verify the old_string anchor occurs exactly once.

**Check:** search CLAUDE.md for the following exact string:

```
---

### SSOT Golden Rule
```

**Expected result:** exactly one occurrence.

**Batch-stop rules:**
- If the anchor is not found: stop immediately. Do not edit CLAUDE.md. Report to Owner.
- If the anchor is found more than once: stop immediately. Do not edit CLAUDE.md. Report to Owner.
- Only if exactly one occurrence is found: proceed with the edit.

---

## 1. Exact CLAUDE.md Insertion Point

File: `/opt/myPKA/CLAUDE.md`

Insert after line 293 — the `---` separator that closes the Pre-Build Protocol (GL-023) rule block — and directly before line 295: `### SSOT Golden Rule`.

The old_string anchor for the edit:

```
---

### SSOT Golden Rule
```

The new_string replaces this anchor with the new rule block followed by the original anchor text (the `---` and `### SSOT Golden Rule` header are preserved; the insert goes between them).

---

## 2. Exact Text to Insert

```markdown
### Close-Session Enforcement Rule — Mandatory

Whenever a session closes — triggered by the Owner or by Claude — Claude must invoke the governed /close-session skill. Ad hoc manual summaries are not a permitted substitute, regardless of session length.

**Minimum required write plan elements (all mandatory, no exceptions):**
- session_log INSERT with explicit `session_date = YYYY-MM-DD`
- Markdown mirror at `Team Knowledge/Core/session-logs/YYYY/MM/YYYYMMDD_<slug>.md`
- UMC summary using exact signature: `mm.write_summary(full_content, summary, description, domain, source_type)` — all five parameters named explicitly
- Scope exclusions stated explicitly in the write plan
- Post-execution report: session_log id, Markdown mirror path, UMC summary id, deviations

**Authorization rule:** Write plan is proposed first. No write is executed before Owner explicitly authorizes it. A prior general "yes" in the session does not authorize close-session writes.

**Trigger condition:** Owner says "close this session", "log this session", or equivalent; Owner invokes /close-session; or a routine close step is reached.

**Violation trigger:** If a session closes without a governed write plan and explicit Owner authorization — stop, complete the missing elements, note the deviation in the session log.

---

```

---

## 3. Additive-Only Confirmation

This change is additive only.

- No existing rule block is modified, reordered, or removed.
- No heading is renamed.
- No existing text is deleted.
- The new block is inserted between two existing blocks (Pre-Build Protocol and SSOT Golden Rule) without touching either.

---

## 4. Scope Exclusions

| Action | Status |
|---|---|
| CLAUDE.md additive insert (this write plan) | authorized after Owner confirmation |
| Close-session skill edit | not in scope |
| New D-folder | excluded |
| Routing | excluded |
| Learning Candidate writes | excluded |
| Deliverable Lifecycle sweep | excluded |
| Dashboard work | excluded |
| team_task changes | excluded |
| GL/SOP edits | excluded |
| Any other CLAUDE.md change | excluded |

---

## 5. Verification Steps After Edit

1. Read CLAUDE.md lines 290–310 and confirm:
   - `### Close-Session Enforcement Rule — Mandatory` is present
   - `### Pre-Build Protocol — Mandatory (GL-023)` is intact above it
   - `### SSOT Golden Rule` is intact below it
   - No existing text was altered
2. Confirm total line count increased by the expected number of inserted lines.
3. Report result in the execution report.

---

## 6. Required Execution Report Path

`Deliverables/20260612_Core_DL Control Inventory/20260615_close-session-enforcement-claudemd-execution-report-v01.md`

The execution report must confirm:
- lines inserted and verified
- pre-edit and post-edit anchor text
- deviations (or "none")

---

*Delivered on: 2026-06-15*
*Delivered at: Deliverables/20260612_Core_DL Control Inventory/20260615_close-session-enforcement-claudemd-write-plan-v01.md*
