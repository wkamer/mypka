# Write Plan — GL-023 Active Gate Amendment (v02)

**Document type:** Write plan — governance artifact
**Status:** Pending Owner authorization
**Session:** 2026-06-15
**Author:** Larry (Team Orchestrator)
**Supersedes:** gl023-active-gate-amendment-write-plan-v01.md (adds persisted execution report)
**Trigger:** Owner observation — GL-023 was only applied on demand, not proactively
**Governing rule:** Governance Deliverable File-First Rule (CLAUDE.md) + GL-021 + GL-023
**Execution Persistence Rule:** Persisted execution report required after any write that
changes files (CLAUDE.md qualifies).

---

## 1. Objective

Amend the GL-023 section in CLAUDE.md to add an active pre-execution gate. After
successful verification, persist an execution report in the existing session folder.

---

## 2. GL-023 Applied to This Build

**Interview:** Amend CLAUDE.md GL-023 section. For Larry and all governed builds.
Out of scope: five steps unchanged, no other CLAUDE.md section touched, no DB changes,
no new GL/SOP/AGENT.md, no new D-folder.

**Spec:** Add `**Active gate — proactive enforcement:**` paragraph after the existing
Violation trigger in the GL-023 section. Persist execution report after verification.
No other lines in CLAUDE.md modified.

**Verify plan:** Read CLAUDE.md post-edit. Confirm Active gate paragraph present.
Confirm five-step list and Violation trigger unchanged. Confirm no other section modified.

**Tool check:** Read tool pre- and post-edit. String search for `Active gate —
proactive enforcement`. Line count diff limited to GL-023 section.

**Murphy scan:** Edit tool matches wrong substring and overwrites adjacent section.
Rollback: pre-edit exact text is in conversation context; re-apply Edit with original
old_string to restore. Execution report is written only after verification passes —
it cannot create a false positive.

---

## 3. Outputs

| # | Output | Path | Condition |
|---|---|---|---|
| 1 | CLAUDE.md edit | `/opt/myPKA/CLAUDE.md` | Primary action |
| 2 | Execution report | `Deliverables/20260615_Core_Lifecycle Sweep Model Design/gl023-active-gate-amendment-execution-report-v01.md` | After V-1 through V-4 all pass |

No new D-folder. No DB writes. No GL/SOP/AGENT.md files.

---

## 4. Target — CLAUDE.md Edit

| Field | Value |
|---|---|
| File | `/opt/myPKA/CLAUDE.md` |
| Section | `### Pre-Build Protocol — Mandatory (GL-023)` |
| Action | Append one paragraph after the existing Violation trigger |

### 4.1 Current text at end of GL-023 section (preserved verbatim)

```
**Violation trigger:** If any build starts without completing all five steps — stop,
complete the missing steps, note the deviation in the session log.
```

### 4.2 Text to append immediately after the Violation trigger

```
**Active gate — proactive enforcement:** The five steps are not background checks. Before
presenting any write plan for Owner authorization, and again before executing any authorized
write plan, Larry must explicitly do one of:
(a) emit all five elements inline, confirming each applies to this build, or
(b) reference the persisted write plan by section name or number, showing which section
covers each of the five elements.
If neither (a) nor (b) is satisfied: stop. Do not request Owner authorization. Complete
the missing elements first.
```

### 4.3 Behavior change summary

| Before | After |
|---|---|
| GL-023 fires reactively if a build starts without the five steps | GL-023 fires proactively before presenting any write plan for authorization |
| Violation trigger catches failure after the fact | Active gate prevents the failure from occurring |
| Owner must prompt for GL-023 application | Larry surfaces GL-023 automatically on every governed build |

---

## 5. File Verification Criteria — CLAUDE.md Edit

| # | Criterion | Pass condition |
|---|---|---|
| V-1 | Active gate paragraph present | `Active gate — proactive enforcement:` in CLAUDE.md GL-023 section |
| V-2 | Five-step list unchanged | Steps 1 through 5 verbatim identical to pre-edit |
| V-3 | Violation trigger unchanged | `Violation trigger:` text verbatim identical to pre-edit |
| V-4 | No other section modified | All text outside the GL-023 block byte-identical to pre-edit |

All 4 criteria must pass before writing the execution report.
Any failure = stop, restore from pre-edit text, report to Owner. Do not write the
execution report.

---

## 6. Execution Report Content

To be written at:
`Deliverables/20260615_Core_Lifecycle Sweep Model Design/gl023-active-gate-amendment-execution-report-v01.md`

Must contain:
- **Exact changed section:** the full amended GL-023 block as it exists in CLAUDE.md
  post-edit (verbatim copy)
- **Verification V-1 through V-4:** pass/fail result for each criterion
- **Confirmation no other CLAUDE.md sections changed:** explicit statement with
  supporting evidence (e.g., byte count of unchanged regions)
- **Deviations:** any deviation from this write plan, or `None`
- **Rollback note:** the exact `old_string` that would restore the pre-edit state if
  needed

---

## 7. Explicit Exclusions

| Exclusion |
|---|
| No changes to any CLAUDE.md section other than the GL-023 block |
| No new GL, SOP, or AGENT.md files |
| No DB writes of any kind |
| No deliverable_lifecycle INSERT or UPDATE |
| No team_tasks update |
| No new D-folder |
| No schema changes |
| No cleanup, archiving, or lifecycle state changes |
| No governance amendments beyond the GL-023 Active gate paragraph |

---

## 8. Execution Sequence (post-authorization)

1. Read CLAUDE.md — capture pre-edit GL-023 section text exactly
2. Apply Edit — append Active gate paragraph after Violation trigger
3. Verify V-1 through V-4
4. If all pass: write execution report to existing session folder
5. Report to Owner: CLAUDE.md path, V-1 through V-4 results, execution report path

If any verification criterion fails at step 3: stop, restore pre-edit text via Edit,
report to Owner. Do not write the execution report.

---

*Write plan v02 persisted: 2026-06-15*
*Awaiting Owner verification and authorization before any execution.*
