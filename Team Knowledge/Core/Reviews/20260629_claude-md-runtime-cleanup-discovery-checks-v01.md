# CLAUDE.md Runtime Cleanup — Pre-Execution Discovery Checks

**Date:** 2026-06-29
**Author:** Larry
**Scope:** Discovery only — no writes authorized
**Parent plan:** `20260629_claude-md-runtime-cleanup-plan-v01.md`
**Iris review:** `20260629_claude-md-runtime-cleanup-plan-v01.md` Section 9

---

## Commands Run

```bash
# Flag B — GL numbering
ls "Team Knowledge/Core/Guidelines/"

# Flag B — SOP numbering
ls "Team Knowledge/SOPs/"

# Check 8 — Todoist IDs in AGENT.md files
grep -rn "6cFcm2MpmHvc2F3H|6c8XR7HXhgMWMWwj|6fC99W283Jw2cjV2|6gfFMpGVh5WJHPCx|6gfFMpHcMCQvPQpc|6gfFMpmXQ3RCGgMC" /opt/myPKA/Team/ --include="AGENT.md"
```

---

## Raw Results

### Guidelines directory

```
Archive
GL-001_File naming conventions.md
GL-002_Frontmatter conventions.md
GL-003_Email setup.md
GL-004_Canonical paths.md
GL-005_AI Engineering Operating System.md
GL-006_Notification Format.md
GL-007_Integration naming convention.md
GL-008_WhatsApp conversatie borging.md
GL-009_CRM people link consistency.md
GL-010_Session logs purpose and discipline.md
GL-011_Project documentation conventions.md
GL-012_ChatGPT prompt ICOR module-verwerking.md
GL-014_AI Team Governance.md
GL-021_Owner Interaction Rule and Write Authorization Boundary.md
GL-023_Pre-Build Protocol.md
GL-024_delivery-pipeline.md
gl-index.md
```

Highest assigned GL number: **GL-024**
Next free sequential numbers: **GL-025, GL-026**

### SOPs directory

```
Archive
SOP-001_Disaster recovery.md
SOP-002_How to do deep online research.md
SOP-003_How to hire a new team member.md
SOP-005_Task management.md
SOP-006_Project management.md
SOP-008_Read own journal before task.md
SOP-009_Write journal entry after task.md
SOP-012_Daily Planning v3 flow.md
SOP-013_365academy bestanden hernoemen.md
SOP-014_Claude Code session context hygiene.md
SOP-015_System File Change Proposal Procedure.md
SOP-017_vertical-slice-gherkin.md
SOP-018_tdd-build.md
SOP-index.md
```

Highest assigned SOP number: **SOP-018**
Next free sequential number: **SOP-019**

### Check 8 — Todoist ID grep results

```
/opt/myPKA/Team/Sienna - The Personal Assistant/AGENT.md:256:
  - Todoist personal project: `👤 PERSONAL` (id: 6cFcm2MpmHvc2F3H)
```

One match. One file. One ID.

---

## Flag B — GL Numbering

**Result: FAIL**

| Number | Status | Reason |
|--------|--------|--------|
| GL-005 | TAKEN | `GL-005_AI Engineering Operating System.md` |
| GL-006 | TAKEN | `GL-006_Notification Format.md` |

The cleanup plan (v01 Section 7) assigns GL-005 and GL-006 to the two new GL files. Both numbers are already in use. These must be renumbered before any GL file is created.

**Correct numbers:**
- Todoist projects reference: **GL-025**
- Naming conventions: **GL-026**

**Additional observation:** GL-001 is titled "File naming conventions." The CLAUDE.md naming conventions table (P-Projectnaam, T-Onderwerp, KE-Naam, G-Titel, etc.) may overlap with or complement GL-001 rather than warrant an entirely new GL file. Before creating GL-026, check GL-001 to determine whether the CLAUDE.md naming table should append to GL-001 or become GL-026. This is a scope clarification question, not a blocker.

---

## Flag B — SOP Numbering

**Result: CONDITIONAL FAIL**

| Number | Status | Reason |
|--------|--------|--------|
| SOP-026 | FREE | Not present in directory |

SOP-026 is technically free. However, the highest existing SOP is SOP-018. Assigning SOP-026 skips 7 numbers without justification. The correct next sequential number is **SOP-019**.

Using SOP-026 would create a false gap in the SOP index and violate the naming discipline that sequential numbering implies.

**Correct number:** SOP-019 (verify SOP-index.md for any reserved or draft entries not yet written to disk).

---

## Check 8 — Todoist IDs in AGENT.md Files

**Result: PASS with one pre-existing SSOT note**

**Finding:** One AGENT.md file contains a hardcoded Todoist project ID:

- File: `Team/Sienna - The Personal Assistant/AGENT.md` (line 256)
- ID: `6cFcm2MpmHvc2F3H` (personal project `👤 PERSONAL`)
- Context: Sienna's operational working knowledge, written directly into her AGENT.md

**Assessment:**

Sienna does not read this ID from CLAUDE.md at runtime. The ID is embedded in her own AGENT.md. Removing Todoist IDs from CLAUDE.md will not break Sienna.

No other AGENT.md file contains any of the six Todoist project IDs currently in CLAUDE.md.

**Pre-existing SSOT concern (not created by this cleanup):**
If GL-025 is created as the Todoist project reference GL, there will be two locations for the personal project ID: GL-025 and Sienna's AGENT.md. This is a pre-existing split that predates this cleanup. The cleanup plan does not worsen it. However, when GL-025 is created, Owner should decide whether Sienna's AGENT.md should be updated to reference GL-025 instead, or whether each agent retaining its own operational IDs is acceptable.

This is a scope question for the Owner, not a blocker. Sienna's AGENT.md is currently outside Section 7. If the Owner wants SSOT resolution, she would be added.

**Scope impact:** None. Execution scope remains closed.

---

## Summary

| Check | Result | Blocking? |
|-------|--------|-----------|
| GL-005 free | FAIL — number taken | Yes — plan needs renumbering |
| GL-006 free | FAIL — number taken | Yes — plan needs renumbering |
| SOP-026 free | CONDITIONAL FAIL — free but not sequential | Yes — plan needs renumbering |
| Check 8 scope | PASS — no agent depends on CLAUDE.md for IDs | No |
| Check 8 SSOT | PRE-EXISTING NOTE — Sienna has one ID hardcoded | Scope question only |

---

## Recommendation

**PAUSE for plan revision — proceed to v02.**

The execution scope is otherwise closed. No out-of-scope agents were found. The blocking issues are numbering corrections only.

**Required corrections for v02:**

1. GL-005 → rename to **GL-025** (Todoist projects reference)
2. GL-006 → rename to **GL-026** (naming conventions) — pending Owner decision on GL-001 overlap
3. SOP-026 → rename to **SOP-019** (project creation)
4. Correct two file paths in Section 7 (Iris Flag A from governance review: Devon and Kai AGENT.md paths)
5. Add post-removal pointer for Project Creation in CLAUDE.md rewrite spec (Iris Flag C)
6. Verify Larry AGENT.md path before execution (Iris Flag D)
7. Owner decision: include Sienna AGENT.md in scope for SSOT resolution, or accept pre-existing split

v02 is a numbering and path correction to the existing plan. It does not require re-running these discovery checks. v02 authorizes execution if Owner confirms.

---

*Discovery only. No writes executed. No files modified.*
