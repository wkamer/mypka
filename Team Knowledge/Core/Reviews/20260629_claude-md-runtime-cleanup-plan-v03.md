# CLAUDE.md Runtime Cleanup Plan — v03

**Date:** 2026-06-29
**Author:** Larry
**Status:** Review — pending Owner approval to execute
**Trigger:** team_task 113 (CLAUDE.md cleanup, carry-forward from SOP Canonical Location Migration, session_log 269)
**Supersedes:** v02 (`20260629_claude-md-runtime-cleanup-plan-v02.md`)
**Iris review:** Completed in chat, 2026-06-29 — see Section 9
**Discovery checks:** `20260629_claude-md-runtime-cleanup-discovery-checks-v01.md` — see Section 10

---

## 1. Proposed Runtime-Only CLAUDE.md Structure

The new CLAUDE.md has eight sections. Nothing else.

```
# Larry — Team Orchestrator

## Identity
## Team
## 3 Hard Stops
## Key Routing Rules
## Briefing Template
## Session Rhythm
## Conventions
## CLAUDE.md Hygiene Rule
```

Estimated size reduction: ~60% by line count.
The file becomes a routing-and-protection instrument only.
All memory, history, reference data, and procedural detail moves out.

---

## 2. Items to Keep in CLAUDE.md

Keep means: survives in the new file, possibly compressed.

| Item | Current section | Keep as |
|------|----------------|---------|
| Iron Rule (Larry never executes domain work) | Identity | Keep — 2 lines max |
| Owner principle (progress over perfection) | Identity | Keep — 1 line |
| Domain question prohibition | Identity | Keep — 1 line |
| 3 Hard Stops table (Wendy / financial / irreversible technical) | 3 Hard Stops | Keep verbatim — table only, no explanatory text |
| Hard stop blocking rule | 3 Hard Stops | Keep — 1 sentence |
| New initiative routing rule | Key Routing Rules | Keep — compressed |
| Personal domain routing (Sienna / Penn) | Key Routing Rules | Keep — 1 line each |
| Build routing decisions (Devon / Kai / Finn / Sasha) | Key Routing Rules | Keep — bullet list only |
| Quinn two-question activation gate | Key Routing Rules | Keep — questions + rule only |
| Codex enforcement line (every Devon/Kai brief) | Key Routing Rules | Keep verbatim |
| Briefing Template six-field format | Briefing Template | Keep verbatim |
| Briefing Template validation rule (6 fields required) | Briefing Template | Keep — 1 sentence |
| Session start protocol (2 steps) | Session Rhythm | Keep — bullets only |
| Session close protocol (4 steps) | Session Rhythm | Keep — bullets only |
| Session-close write authorization rule | Session Rhythm | Keep — 1 sentence |
| Sienna failure path | Session Rhythm | Keep — 1 sentence |
| Language hard rule (EN system, EN/NL owner) | Conventions | Keep — 1 line |
| Tone (short sentences, no em dashes) | Conventions | Keep — 1 line |
| SSOT rule (one fact, one file) | Conventions | Keep — 1 line |
| Propose-before-write rule | Conventions | Keep — 1 line |
| Complete-all-identified-fixes rule | Conventions | Keep — 1 line |
| Code review multi-model rule | Conventions | Keep — 1 line |
| Weekly Friday sweep | Conventions | Keep — 1 line |
| Daily planning 3-day no-movement rule | Conventions | Keep — 1 line |
| Larry's three duties | Conventions | Keep — 1 line |
| CLAUDE.md Hygiene Rule | New section | Add verbatim — see Section 5 |
| Decision Boundary quick-test questions | New section | Add verbatim — see Section 6 |

**Iris note:** Decision Boundary quick-test questions (Section 6) must survive the rewrite alongside the Hygiene Rule prose. They are the actionable gate, not decorative.

---

## 3. Items to Move Out — with Exact Proposed Destination

| Item | Current section | Proposed destination | Notes |
|------|----------------|---------------------|-------|
| Team table (20 specialists, AGENT.md paths) | Team | `Team/agent-index.md` | agent-index.md becomes SSOT; CLAUDE.md keeps one-liner + reference |
| Hiring rule (Pax → Nolan sequence) | Team | `Team/Larry - The Orchestrator/AGENT.md` | Not a per-session routing rule; it is a procedure |
| Where Things Live path table | Where Things Live | Remove; `GL-004_Canonical paths.md` is SSOT | CLAUDE.md keeps: "Paths → [[GL-004_Canonical paths]]." |
| Deliverable rule (active = Deliverables/, done = Archive/) | Where Things Live | Append to GL-004 under Deliverables section | Currently duplicated |
| Task Systems — Todoist project IDs | Task Systems | New file: `Team Knowledge/Core/Guidelines/GL-025_todoist-projects.md` | Not routing logic; reference data |
| Task Systems — team_tasks explanation | Task Systems | `Team/Larry - The Orchestrator/AGENT.md` | Procedural context, not a per-session gate |
| Project Creation 5-step process | Project Creation | New SOP: `Team Knowledge/SOPs/SOP-019_project-creation.md` | Already procedural in nature; wrong file. CLAUDE.md retains one-line pointer after removal: "Project creation → [[SOP-019_project-creation]]" |
| Naming Conventions table | Naming Conventions | **Conditional — see Check 7 in Section 8:** either append to `Team Knowledge/Core/Guidelines/GL-001_File naming conventions.md`, or create new `Team Knowledge/Core/Guidelines/GL-026_naming-conventions.md` | GL-001 must be inspected before deciding. If GL-001 already covers entity-type naming conventions (P-, T-, KE-, G-, SOP-, GL- prefixes), append. If GL-001 covers only file-level naming, create GL-026. |
| Quinn activation "Current state (2026-06-29)" snapshot | Key Routing Rules | `Team Knowledge/Core/active-context.md` | Dated state snapshot; decays; wrong SSOT |
| Execution relay pattern (harness detail) | Briefing Template | `Team/Larry - The Orchestrator/AGENT.md` | Implementation detail, not a routing rule |
| "Think before briefing" paragraph | Briefing Template | `Team/Larry - The Orchestrator/AGENT.md` | Procedure, not a gate |
| Build routing explanatory paragraphs | Key Routing Rules | `Team/Devon - The Senior Full-Stack Developer/AGENT.md` + `Team/Kai - The Infrastructure & Integration Architect/AGENT.md` | Justifications for boundaries already set |
| Learning Rule (full text) | Learning Rule | `Team/Larry - The Orchestrator/AGENT.md` | Session-close procedure; not a routing gate |
| Conventions — "Language" detail beyond 1-line rule | Conventions | GL or `Team/Larry - The Orchestrator/AGENT.md` | Keep the rule; move the prose |

---

## 4. Items to Delete as Historical Noise

| Item | Current section | Reason |
|------|----------------|--------|
| Full Changelog section (6 entries) | Changelog | Git history is the record. Each removal commit must reference team_task 113 and "Iris review 2026-06-29" in the commit message. **Check 5 governs the pre-condition for this deletion.** |
| Incident reference: "G6 rejection on Email Management Slice 3 proved the gap" | Key Routing Rules | Incident narrative; not a routing rule |
| "Current state (2026-06-29): No pattern-level design system exists" | Key Routing Rules | Dated snapshot; decays; duplicated in active-context |
| Repeated "Larry never does himself" domain list | Key Routing Rules | Already fully covered by Iron Rule in Identity |
| Changelog entries embedded in Key Routing Rules (each Quinn rule change) | Key Routing Rules | Historical justification; not a runtime instruction |

---

## 5. Proposed CLAUDE.md Runtime Hygiene Rule

Add verbatim as a new final section in CLAUDE.md:

---

> **CLAUDE.md Hygiene Rule**
>
> CLAUDE.md may only contain rules Larry needs in every session to route, stop, delegate, or protect the Owner.
>
> Do not add: changelog entries, historical explanations, one-time decisions, project-specific procedures, long SOP steps, incident narratives, dated state snapshots, learning notes, or implementation details.
>
> When unsure, Larry must propose the correct destination first: CLAUDE.md, AGENT.md, SOP, GL, active-context, review deliverable, or session log.
>
> CLAUDE.md is the startmotor, not the memory.

---

## 6. Decision Boundary — Future Content in CLAUDE.md

A new rule or piece of content belongs in CLAUDE.md **only if all three are true:**

1. **Per-session scope** — Larry needs it at the start of every session, not occasionally.
2. **Routing or protection function** — It tells Larry who to route to, when to stop, or what to protect.
3. **No better SSOT exists** — It is not already captured in GL-004, an AGENT.md, a SOP, or active-context.

If any condition is false, route to the correct destination and reference it if needed.

Quick test questions:
- Is this a hard stop? → CLAUDE.md.
- Is this a routing decision Larry applies every session? → CLAUDE.md.
- Is this a procedure with steps? → SOP.
- Is this a named convention or path? → GL.
- Is this state that will change? → active-context.
- Is this an agent's working knowledge? → That agent's AGENT.md.
- Is this history or justification? → Session log or git commit message.

**Iris note:** These quick-test questions must survive the rewrite verbatim. They are the actionable operationalization of the Hygiene Rule.

---

## 7. Exact Files That Would Change If Owner Approves

| # | File | Change type | Description |
|---|------|------------|-------------|
| 1 | `CLAUDE.md` | Major rewrite | Remove Sections 3, 4, 9, 10, 11; compress Sections 2, 6, 8, 13; add Hygiene Rule + Decision Boundary sections; add Project Creation one-line pointer |
| 2 | `Team/agent-index.md` | Verify + complete if needed | Must list all 20 specialists before team table is removed in Step 11 |
| 3 | `Team Knowledge/Core/Guidelines/GL-004_Canonical paths.md` | Append | Add Deliverable rule (currently only in CLAUDE.md) |
| 4 | `Team Knowledge/Core/Guidelines/GL-025_todoist-projects.md` | New file | Todoist project IDs + team_tasks explanation |
| 5 | `Team Knowledge/Core/Guidelines/GL-001_File naming conventions.md` OR `GL-026_naming-conventions.md` | Append OR new file | Naming conventions table — GL-001 inspection (Check 7) determines which |
| 6 | `Team Knowledge/SOPs/SOP-019_project-creation.md` | New file | Project creation 5-step process |
| 7 | `Team/Larry - The Orchestrator/AGENT.md` | Append | Execution relay pattern, hiring rule, learning rule, task systems explanation, build routing context |
| 8 | `Team/Devon - The Senior Full-Stack Developer/AGENT.md` | Append | Build routing boundary justification |
| 9 | `Team/Kai - The Infrastructure & Integration Architect/AGENT.md` | Append | Kai/Devon boundary justification |
| 10 | `Team Knowledge/Core/active-context.md` | Update | Move Quinn "Current state" snapshot here; confirm alignment with existing entry |

**File count by branch:**
- If naming conventions append to GL-001 (file 5 = append): **2 new files, 8 updated files.**
- If GL-026 is created (file 5 = new file): **3 new files, 7 updated files.**
- Total affected files: **10 in either branch.**

**Sienna AGENT.md: explicitly excluded from this scope — see Section 11.**

---

## 8. Verification Checks and Execution Sequence

Checks are numbered 1-8 sequentially. Execution order is strict. No step may begin before its predecessor is complete. Each step is a separate git commit.

### Pre-execution checks (before Step 1)

**Check 1 — Routing completeness audit:** Read CLAUDE.md in full. Confirm every routing decision appears in Section 2 (keep) or Section 3 (destination named). No routing rule may be unaccounted for.

**Check 2 — Hard Stops audit:** Confirm all three Hard Stops are in Section 2 with "keep verbatim." No Hard Stop may be in Section 4 (delete) or Section 3 (move).

**Check 3 — agent-index.md audit:** Run `ls Team/` and compare against CLAUDE.md team table. Record whether agent-index.md is complete or needs completion. If completion is needed and is within Section 7 (file 2), execution may continue — Step 10 is the planned correction step. This check does not block execution start; it confirms whether Step 10 will have work to do. The CLAUDE.md rewrite (Step 11) may not proceed until agent-index.md is verified complete.

**Check 4 — GL-004 path coverage:** Read GL-004. Confirm every path in CLAUDE.md "Where Things Live" is present in GL-004. Any gap must be filled as part of the GL-004 append (file 3, Step 2) before CLAUDE.md section is removed.

**Check 5 — Changelog authorization audit:** Read current CLAUDE.md Changelog section. For each entry referencing an Iris audit event or Owner confirmation, verify the corresponding session log records that authorization. If any authorization event exists only in the CLAUDE.md Changelog, execution pauses. Larry reports the exact missing authorization event, the proposed session log target, and the required expanded authorization. No session log write is allowed under this cleanup authorization unless Owner explicitly approves that expanded scope.

**Check 6 — SOP-index.md reserved entries:** Read `Team Knowledge/SOPs/SOP-index.md`. Confirm SOP-019 is not reserved or assigned as a draft entry. If SOP-019 is taken, execution pauses. Larry reports the conflict and proposes the next free sequential number for Owner confirmation before proceeding.

**Check 7 — GL-001 inspection (naming conventions decision):** Read `Team Knowledge/Core/Guidelines/GL-001_File naming conventions.md`. If GL-001 covers entity-type naming conventions (P-, T-, KE-, G-, SOP-, GL- prefixes and formats), append the CLAUDE.md naming table there (file 5 = GL-001 append branch). If GL-001 covers only file-level naming (case, separators, extension), create GL-026 as a separate file (file 5 = GL-026 branch). Record the decision before Step 4 executes.

**Check 8 — Larry AGENT.md path:** Run `ls "Team/Larry - The Orchestrator/"` to confirm AGENT.md exists at that exact path. If not found, execution pauses. Larry reports the path discrepancy and waits for Owner confirmation before any append.

### Execution sequence (after all pre-execution checks pass)

**Step 1:** Add Hygiene Rule + Decision Boundary section to CLAUDE.md.
Git commit: `feat(CLAUDE.md): add Hygiene Rule and Decision Boundary — team_task 113, Iris review 2026-06-29`

**Step 2:** Append Deliverable rule to GL-004. Git commit.

**Step 3:** Create GL-025_todoist-projects.md. Git commit.

**Step 4:** Create GL-026 or append to GL-001 (per Check 7 decision). Git commit.

**Step 5:** Create SOP-019_project-creation.md. Git commit.

**Step 6:** Append to Larry AGENT.md (execution relay pattern, hiring rule, learning rule, task systems, build routing context). Git commit.

**Step 7:** Append to Devon AGENT.md (build routing boundary justification). Git commit.

**Step 8:** Append to Kai AGENT.md (Kai/Devon boundary justification). Git commit.

**Step 9:** Update active-context.md (Quinn state snapshot). Git commit.

**Step 10 — Complete and verify agent-index.md if needed:** If Check 3 recorded a gap, complete agent-index.md now. Verify all 20 specialists are listed. Git commit if changes were made.

**Step 11:** Rewrite CLAUDE.md (all removals, compressions, one-line Project Creation pointer added). Confirm agent-index.md is complete before this step begins.
Git commit: `refactor(CLAUDE.md): runtime-only rewrite — team_task 113, Iris review 2026-06-29`

**Hard rules:**
- Step 11 may not execute until Steps 1-10 are complete and confirmed.
- Steps 7 and 8 (Devon and Kai AGENT.md appends) must complete before Step 11.
- Check 5, 6, 7, and 8 pause execution if a conflict is found. They do not allow self-resolution under this cleanup authorization.

---

## 9. Iris Review Resolution

Iris review was received in chat, 2026-06-29.

| # | Iris answer | Resolution in v03 |
|---|-------------|------------------|
| 1 | Changelog removal is safe. Commit messages must reference team_task 113 and Iris review date. Verify session logs capture any authorization events first. | Check 5 governs this. If any authorization event is missing from session logs, execution pauses and Owner decides on expanded scope. No self-resolution permitted. |
| 2 | Sequence is correct. Two risks: (a) Check 8 (Todoist grep) must run before Owner approval; (b) Devon and Kai AGENT.md appends missing from verification sequence. | Check 8 (Todoist grep) completed in discovery report. Devon and Kai appends are Steps 7 and 8, sequenced before Step 11. |
| 3 | CLAUDE.md placement for Hygiene Rule is sufficient. No GL file needed. Decision Boundary quick-test questions must survive the rewrite. | Quick-test questions added explicitly to Section 2 keep list. Note added in Section 6. |
| 4 | Single authorization covers closed set in Section 7, contingent on Check 8 returning no out-of-scope agents. | Authorization boundary stated in Section 12. Check 8 result incorporated in Section 10. |

| # | Iris flag | Resolution in v03 |
|---|-----------|------------------|
| A | Devon and Kai AGENT.md paths wrong (`Team Knowledge/` instead of `Team/`) | Corrected in Sections 3, 7, and 8. |
| B | GL-005 and GL-006 numbers taken; SOP-026 not sequential | GL-025 and GL-026 used. SOP-019 used. Checks 6 and 7 added. |
| C | No CLAUDE.md pointer after Project Creation removal | One-line pointer "Project creation → [[SOP-019_project-creation]]" specified in Section 3 and Section 7 file 1. |
| D | Larry AGENT.md path unverified | Check 8 added. |

---

## 10. Pre-Execution Discovery Resolution

Discovery checks run: `20260629_claude-md-runtime-cleanup-discovery-checks-v01.md`

| Check | Discovery result | v03 resolution |
|-------|-----------------|---------------|
| GL-005 free? | FAIL — GL-005 taken (AI Engineering OS) | Renumbered to GL-025. |
| GL-006 free? | FAIL — GL-006 taken (Notification Format) | Renumbered to GL-026 conditional on Check 7 (GL-001 inspection). |
| SOP-026 free? | CONDITIONAL FAIL — free but not sequential; next sequential is SOP-019 | Renumbered to SOP-019. |
| Check 8 — out-of-scope agents? | PASS — no agent depends on CLAUDE.md for Todoist IDs | Scope remains closed. |
| Sienna hardcoded ID | PRE-EXISTING NOTE — Sienna AGENT.md:256 has personal project ID (6cFcm2MpmHvc2F3H) | Pre-existing SSOT note. Not created by this cleanup. Owner decision recorded in Section 11. |

---

## 11. Owner Decisions Recorded

**Decision 1 — Sienna AGENT.md scope:**
Owner accepts the pre-existing Sienna Todoist ID split (AGENT.md:256 has `6cFcm2MpmHvc2F3H` hardcoded). Sienna AGENT.md is excluded from this execution scope. No update to Sienna in this cleanup. If SSOT resolution is desired, it becomes a separate carry-forward item after this cleanup closes.

**Decision 2 — Authorization boundary:**
Stated in Section 12.

---

## 12. Authorization Boundary

Owner approval of v03 authorizes **only the following:**

- All writes listed in Section 7 (files 1-10), in the execution sequence defined in Section 8.
- No Sienna AGENT.md change.
- No additional files beyond Section 7 unless execution pauses and Owner explicitly approves expanded scope.

**On pre-execution check gaps:**
- If a pre-execution check reveals a gap that is already covered by a planned step in Section 7, execution continues. The check records the gap; the planned step resolves it. This applies to Check 3 (agent-index.md completion is handled by Step 10).
- If a pre-execution check reveals a gap that is outside Section 7, execution pauses. Larry reports the finding. Owner confirms expanded scope or correction before execution resumes. This applies to Checks 5, 6, 7 (conflict branch), and 8 (missing path).

This authorization does not cover any future CLAUDE.md edits beyond this cleanup. Each future change goes through the Hygiene Rule gate (Section 5) and the Decision Boundary (Section 6) independently.

---

*Review v03. Execution authorized upon Owner confirmation.*
