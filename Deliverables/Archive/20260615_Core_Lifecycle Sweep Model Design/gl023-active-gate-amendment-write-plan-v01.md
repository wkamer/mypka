# Write Plan — GL-023 Active Gate Amendment

**Document type:** Write plan — governance artifact
**Status:** Pending Owner authorization
**Session:** 2026-06-15
**Author:** Larry (Team Orchestrator)
**Trigger:** Owner observation — GL-023 was only applied on demand, not proactively
**Governing rule:** Governance Deliverable File-First Rule (CLAUDE.md) + GL-021 + GL-023

---

## 1. Objective

Amend the GL-023 section in CLAUDE.md to convert it from a documented rule into an
active pre-execution gate. Larry must proactively surface all five GL-023 elements
before any write plan is presented for Owner authorization AND before any authorized
write plan is executed.

---

## 2. GL-023 Applied to This Build

**Interview:** Amend CLAUDE.md GL-023 section. For Larry and all governed builds.
Out of scope: five steps unchanged, no other CLAUDE.md section touched, no DB changes.

**Spec:** Add `**Active gate — proactive enforcement:**` paragraph after the existing
Violation trigger in the GL-023 section. No other lines modified.

**Verify plan:** Read CLAUDE.md post-edit. Confirm Active gate paragraph present.
Confirm five-step list and Violation trigger unchanged. Confirm no other section modified.

**Tool check:** Read tool pre- and post-edit. String search for `Active gate —
proactive enforcement`. Line count diff limited to GL-023 section.

**Murphy scan:** Edit tool matches wrong substring and overwrites adjacent section.
Rollback: pre-edit exact text is in conversation context; re-apply Edit with original
old_string to restore.

---

## 3. Target

| Field | Value |
|---|---|
| File | `/opt/myPKA/CLAUDE.md` |
| Section | `### Pre-Build Protocol — Mandatory (GL-023)` |
| Action | Add one paragraph after the existing Violation trigger |
| New file | No |
| New D-folder | No |
| DB changes | None |

---

## 4. Exact Amendment

### 4.1 Current text at end of GL-023 section (to be preserved verbatim)

```
**Violation trigger:** If any build starts without completing all five steps — stop,
complete the missing steps, note the deviation in the session log.
```

### 4.2 Text to be appended immediately after the Violation trigger

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

## 5. File Verification Criteria

| # | Criterion | Pass condition |
|---|---|---|
| V-1 | Active gate paragraph present | `Active gate — proactive enforcement:` in CLAUDE.md GL-023 section |
| V-2 | Five-step list unchanged | Steps 1 through 5 verbatim identical to pre-edit |
| V-3 | Violation trigger unchanged | `Violation trigger:` text verbatim identical to pre-edit |
| V-4 | No other section modified | All text outside the GL-023 section byte-identical to pre-edit |

All 4 criteria must pass. Any failure = stop, restore from pre-edit text, report to Owner.

---

## 6. Explicit Exclusions

| Exclusion |
|---|
| No changes to any section of CLAUDE.md other than the GL-023 block |
| No new GL, SOP, or AGENT.md files |
| No DB writes of any kind |
| No new D-folder |
| No schema changes |
| No cleanup, archiving, or lifecycle state changes |

---

## 7. Execution Sequence (post-authorization)

1. Read CLAUDE.md to confirm pre-edit GL-023 section text
2. Apply Edit: append Active gate paragraph after Violation trigger
3. Verify V-1 through V-4
4. Report to Owner: confirmation of amendment, verification results

---

*Write plan persisted: 2026-06-15*
*Awaiting Owner verification and authorization before any execution.*
