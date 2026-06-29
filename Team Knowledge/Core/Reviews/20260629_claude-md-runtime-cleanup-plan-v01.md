# CLAUDE.md Runtime Cleanup Plan — v01

**Date:** 2026-06-29
**Author:** Larry
**Status:** Review only — no writes authorized
**Trigger:** team_task 113 (CLAUDE.md cleanup, carry-forward from SOP Canonical Location Migration, session_log 269)
**Iris review requested:** Yes — see Section 9

---

## 1. Proposed Runtime-Only CLAUDE.md Structure

The new CLAUDE.md has seven sections. Nothing else.

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

---

## 3. Items to Move Out — with Exact Proposed Destination

| Item | Current section | Proposed destination | Notes |
|------|----------------|---------------------|-------|
| Team table (20 specialists, AGENT.md paths) | Team | `Team/agent-index.md` | agent-index.md becomes SSOT; CLAUDE.md keeps one-liner + reference |
| Hiring rule (Pax → Nolan sequence) | Team | Larry's `Team/Larry - The Orchestrator/AGENT.md` | Not a per-session routing rule; it is a procedure |
| Where Things Live path table | Where Things Live | Remove; `GL-004_Canonical paths.md` is SSOT | CLAUDE.md keeps: "Paths → [[GL-004_Canonical paths]]." |
| Deliverable rule (active = Deliverables/, done = Archive/) | Where Things Live | Add to GL-004 under Deliverables section | Currently duplicated |
| Task Systems — Todoist project IDs | Task Systems | New file: `Team Knowledge/Core/Guidelines/GL-005_todoist-projects.md` | Not routing logic; reference data |
| Task Systems — team_tasks explanation | Task Systems | Larry's AGENT.md | Procedural context, not a per-session gate |
| Project Creation 5-step process | Project Creation | New SOP: `Team Knowledge/SOPs/SOP-026_project-creation.md` | Already procedural in nature; wrong file |
| Naming Conventions table | Naming Conventions | `Team Knowledge/Core/Guidelines/GL-005_naming-conventions.md` (new) or append to GL-004 | Reference data, not routing logic |
| Quinn activation "Current state (2026-06-29)" snapshot | Key Routing Rules | `Team Knowledge/Core/active-context.md` | Dated state snapshot; decays; wrong SSOT |
| Execution relay pattern (harness detail) | Briefing Template | Larry's AGENT.md | Implementation detail, not a routing rule |
| "Think before briefing" paragraph | Briefing Template | Larry's AGENT.md | Procedure, not a gate |
| Build routing explanatory paragraphs | Key Routing Rules | Devon AGENT.md + Kai AGENT.md | Justifications for boundaries already set |
| Learning Rule (full text) | Learning Rule | Larry's AGENT.md | Session-close procedure; not a routing gate |
| Conventions — "Language" detail beyond 1-line rule | Conventions | GL or Larry's AGENT.md | Keep the rule; move the prose |

---

## 4. Items to Delete as Historical Noise

| Item | Current section | Reason |
|------|----------------|--------|
| Full Changelog section (6 entries) | Changelog | Git history is the record; changelog in a runtime file is noise and will be stale |
| Incident reference: "G6 rejection on Email Management Slice 3 proved the gap" | Key Routing Rules | Incident narrative; not a routing rule; belongs in session log at most |
| "Current state (2026-06-29): No pattern-level design system exists" | Key Routing Rules | Dated snapshot; decays; duplicated in active-context |
| Repeated "Larry never does himself" domain list | Key Routing Rules | Already fully covered by Iron Rule in Identity |
| Changelog entries embedded in § Key Routing Rules (each Quinn rule change) | Key Routing Rules | Historical justification; not a runtime instruction |

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

---

## 7. Exact Files That Would Change If Owner Approves

| File | Change type | Description |
|------|------------|-------------|
| `CLAUDE.md` | Major rewrite | Remove Sections 3, 4, 9, 10, 11; compress Sections 2, 6, 8, 13; add Hygiene Rule section |
| `Team/agent-index.md` | Verify + complete | Must list all 20 specialists before team table is removed from CLAUDE.md |
| `Team Knowledge/Core/Guidelines/GL-004_Canonical paths.md` | Append | Add Deliverable rule (currently only in CLAUDE.md) |
| `Team Knowledge/Core/Guidelines/GL-005_todoist-projects.md` | New file | Todoist project IDs + team_tasks explanation |
| `Team Knowledge/Core/Guidelines/GL-006_naming-conventions.md` | New file | Naming conventions table |
| `Team Knowledge/SOPs/SOP-026_project-creation.md` | New file | Project creation 5-step process (verify SOP numbering first) |
| `Team/Larry - The Orchestrator/AGENT.md` | Append | Execution relay pattern, hiring rule, learning rule, task systems explanation, build routing context |
| `Team Knowledge/Devon - The Senior Full-Stack Developer/AGENT.md` | Append | Build routing boundary justification |
| `Team Knowledge/Kai - The Infrastructure & Integration Architect/AGENT.md` | Append | Kai/Devon boundary justification |
| `Team Knowledge/Core/active-context.md` | Update | Quinn "Current state" snapshot (already partially reflected; confirm alignment) |

**Total: 10 files. 3 new, 7 existing.**

---

## 8. Verification Checks

Before any write is executed:

1. **Routing completeness** — Every routing decision in current CLAUDE.md appears in the new version or is documented at its named destination. No routing rule may be lost.
2. **Hard Stops intact** — All three Hard Stops survive verbatim. Verify line-by-line after rewrite.
3. **agent-index.md exists and is complete** — All 20 specialists listed before team table removal. Run `ls Team/` to confirm.
4. **GL-004 path coverage** — Verify GL-004 covers all paths referenced in the current CLAUDE.md "Where Things Live" section. Any gap must be filled before removal.
5. **SOP-026 written before section removal** — Project Creation section in CLAUDE.md may not be deleted before SOP-026 exists and is linked.
6. **GL-005 and GL-006 written before section removal** — Todoist IDs and naming conventions must land before their CLAUDE.md sections are removed.
7. **Larry AGENT.md absorbs all moved items** — Verify each moved item is present in Larry's AGENT.md before it is deleted from CLAUDE.md.
8. **No agent depends on CLAUDE.md Todoist IDs** — Grep all AGENT.md files for Todoist project IDs. If any agent reads those IDs from CLAUDE.md (unlikely but must verify), update that agent to reference GL-005 instead.
9. **Hygiene Rule added before other sections removed** — Hygiene Rule section is the first write. It gates all subsequent removals.
10. **Git commit after each atomic step** — Each removal/addition is a separate commit. No bundled rewrites.

---

## 9. Iris Review Request

**To:** Iris — The Governance Gatekeeper
**From:** Larry
**Subject:** CLAUDE.md Runtime Cleanup — governance review before Owner decision

**Context:** CLAUDE.md is the root runtime instruction for every session. team_log 139 flagged that canonical declarations before migrations create bounded split-state gaps and require explicit closing triggers. This cleanup is that closing trigger.

**What I am asking Iris to review:**

1. **Scope safety** — Is it safe to remove the Changelog section from CLAUDE.md entirely? Git history is the record. Is there a governance reason to keep a changelog in the file itself?

2. **Sequencing gate** — The plan requires destination files to exist before source sections are removed. Is the proposed sequencing (Hygiene Rule first, then GL files, then SOP, then Larry AGENT.md, then CLAUDE.md rewrite) the correct order? Any sequencing risk?

3. **Hygiene Rule formalization** — The Hygiene Rule is proposed as a section inside CLAUDE.md. Should it also be formalized as a GL file so agents can reference it independently? Or is CLAUDE.md placement sufficient?

4. **Authorization scope** — Owner approval of this review authorizes all writes listed in Section 7 in the sequence from Section 8. Is that the correct authorization boundary, or should Owner confirm each file separately?

**Done looks like:** Iris returns four answers — one per numbered question. Owner then has full information to approve the smallest safe execution step.

---

*Review only. No writes authorized until Owner confirms.*
