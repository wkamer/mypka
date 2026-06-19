# Close-Session Workflow Enforcement — Governance Amendment Proposal v01

**Date:** 2026-06-15
**Author:** Larry
**Status:** Proposal — pending Owner authorization
**Target:** CLAUDE.md / close-session skill instruction

---

## 1. Problem Statement

Claude sessions are not consistently closed through the governed `/close-session` workflow. Instead, sessions are sometimes closed with ad hoc manual summaries or minimal write plans outside the workflow. This produces recurring failures:

- Missing required fields (e.g., `session_date` absent from session_log INSERT)
- Wrong `write_summary()` signature — missing or reordered parameters
- Inconsistent post-execution verification
- Unclear distinction between proposed writes and executed writes
- Weak carry-forward discipline — open items not captured, constraints not repeated

Each occurrence requires a correction cycle that consumes Owner attention and session capacity. The correction is currently applied per-session rather than embedded as a system behavior.

---

## 2. Required Behavior

Whenever a session closes — whether triggered by the Owner ("close this session", "log this session") or by Claude recognizing session-end conditions — Claude must:

1. Invoke the governed `/close-session` skill, not produce an ad hoc summary.
2. Produce a write plan containing all minimum required elements (see Section 4).
3. Present the write plan to the Owner and wait for explicit authorization before executing any write.
4. Execute only the authorized writes.
5. Report results immediately after execution (see Section 4, item 8).

---

## 3. Trigger Condition

**Trigger:** Any of the following signals that the session should close:

- Owner says: "close this session", "log this session", "please close", or equivalent
- Owner invokes `/close-session` explicitly
- Routine step requires session closure (end-of-day routine, afternoon routine, morning routine close)
- Claude determines the session has reached a natural end point and proposes closure

**In all cases:** Claude uses the governed close-session workflow. Ad hoc manual summaries are not permitted as a substitute, regardless of session length or content volume.

---

## 4. Minimum Required Close-Session Elements

Every close-session write plan must include all of the following. Omitting any element is a protocol violation.

### 4.1 session_log INSERT

Required fields — no exceptions:

| Field | Requirement |
|---|---|
| `session_date` | Always explicit. Format: `YYYY-MM-DD`. Never omitted. |
| `session_title` | Descriptive, English |
| `topics` | 2–4 comma-separated tags, English |
| `summary` | 3–5 sentences, English |
| `decisions` | All decisions taken in the session |
| `actions_taken` | All actions executed |
| `delegations` | All delegations issued, or "None" |
| `open_items` | All unresolved threads and carry-forward constraints |

### 4.2 Markdown mirror

- Path pattern: `Team Knowledge/Core/session-logs/YYYY/MM/YYYYMMDD_<slug>.md`
- The exact target path must be stated in the write plan before execution.
- Content mirrors the session_log row.

### 4.3 UMC summary

Exact call signature — no deviations:

```python
mm.write_summary(
    full_content="...",   # full session narrative
    summary="...",         # 1–2 sentence summary
    description="...",     # "Close-session summary: <title>, <date>"
    domain="core",         # or relevant domain
    source_type="knowledge"
)
```

All five parameters must be named explicitly. Positional-only calls are not permitted.

### 4.4 Scope exclusions in write plan

The write plan must explicitly list what is not authorized. Minimum required exclusions to state:

- no new D-folder
- no routing
- no Learning Candidate writes
- no Deliverable Lifecycle sweep
- no GL/SOP/CLAUDE.md edits (unless separately authorized)
- no dashboard work
- no team_task changes
- no archive execution
- no folder moves
- no lifecycle DB updates beyond close-session writes

### 4.5 Post-execution report

After execution, Claude reports exactly:

- session_log id (integer returned by INSERT)
- Markdown mirror path (exact)
- UMC summary id (integer returned by write_summary)
- Deviations (explicit "none" if clean)

---

## 5. Authorization Rule

Close-session writes are proposed first. Execution does not start until the Owner explicitly authorizes.

- A prior general "yes" or "go ahead" in the session does not constitute authorization for close-session writes.
- Authorization must reference the write plan (by content or path) and confirm all three writes.
- If the Owner authorizes only a subset, Claude executes only that subset and notes the exclusion in the deviation report.

This rule applies regardless of session length or apparent simplicity of the closure.

---

## 6. Recommended Landing Location

Two locations, applied together:

### 6.1 CLAUDE.md — Hard Rules section

Add a new rule block: **Close-Session Enforcement Rule**. Content: trigger condition (Section 3), minimum required elements (Section 4 summary), authorization rule (Section 5). This makes it binding for Larry and all specialists who read CLAUDE.md.

### 6.2 Close-session skill instruction (`/close-session`)

Update the skill's internal checklist to enumerate all minimum elements from Section 4. The skill should self-check before presenting the write plan: if any element is missing, complete it before presenting to the Owner.

Applying both locations ensures enforcement whether Claude is operating from CLAUDE.md context or from an invoked skill.

---

## 7. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| CLAUDE.md edit introduces unintended side effects | Low | Medium | Amendment proposal reviewed before execution; minimal targeted addition |
| Skill update breaks existing close-session behavior | Low | High | Additive change only; no removal of existing steps |
| Rule is too prescriptive and slows routine closures | Low | Low | Elements are already required — this makes them explicit, not new |
| Future compaction drops CLAUDE.md rule from context | Medium | Medium | Skill serves as redundant enforcement point |
| Ad hoc closures continue despite rule | Low | Low | Rule creates a named violation trigger — corrections become faster |

---

## 8. Smallest Safe Implementation Plan

Three steps, in sequence. Each requires separate Owner authorization.

**Step 1 — CLAUDE.md amendment**
Add a "Close-Session Enforcement Rule" block to the Hard Rules section of CLAUDE.md.
- No structural changes to existing rules.
- Additive only.
- Estimated scope: 20–30 lines.

**Step 2 — Close-session skill update**
Update the `/close-session` skill instruction with the minimum elements checklist from Section 4.
- Additive update to the skill's existing workflow.
- No removal of existing steps.

**Step 3 — Verification**
In the next session that invokes `/close-session`: verify all required elements are present in the write plan before Owner authorization is requested. Report any deviation.

Steps 1 and 2 may be authorized and executed in the same session if Owner chooses. Step 3 is automatically triggered by the next session close.

---

## 9. Scope Exclusions

This proposal does not authorize:

- No new D-folder
- No routing
- No Learning Candidate writes
- No Deliverable Lifecycle sweep
- No dashboard work
- No team_task changes
- No direct CLAUDE.md edit (Step 1 above is separately authorized)
- No GL/SOP edits beyond the two target locations named in Section 6

---

*Delivered on: 2026-06-15*
*Delivered at: Deliverables/20260612_Core_DL Control Inventory/20260615_close-session-workflow-enforcement-proposal-v01.md*
