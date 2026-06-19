# Spec: Larry Proactive Trigger Library and Pre-Action Gate

**Status:** Approved by Owner — 2026-06-16
**Implemented in:** CLAUDE.md (sections: Proactive Trigger Library, Pre-Action Gate, Richer Briefing Template)

---

## Problem Statement

myPKA has been structurally reactive. Larry activates specialists only when the owner asks. Larry does not intervene proactively at the right moment. Result: sensitive actions (communication to Wendy, new initiatives, financial commitments) are executed without specialist review because the owner did not know to ask.

Concrete trigger for this spec: the owner sent an emotional email to Wendy without Sienna reviewing the impact first. Larry should have recognized that moment and deployed Sienna proactively.

---

## Decision

myPKA becomes proactive. Larry recognizes patterns and acts without the owner having to ask.

Two mechanisms:

1. **Trigger Library** — explicit table of patterns that automatically activate a specialist
2. **Pre-Action Gate** — blocking rule that prevents Larry from executing sensitive actions before the right specialist has reviewed

Supporting mechanism:

3. **Richer Briefing Template** — every specialist brief now includes pattern signal and context, not just the task

---

## Scope

**In scope:**
- New "Proactive Trigger Library" section in CLAUDE.md
- New "Pre-Action Gate" section in CLAUDE.md
- New "Richer Briefing Template" section in CLAUDE.md

**Not in scope:**
- No new agents
- No database tables or schema changes
- No code or scripts
- No changes to existing GL or SOP files

---

## Design: Trigger Library

Larry scans every owner input against this table before acting.

| ID | Pattern | Signal | Auto-Action | Specialist | Minimum Brief Instruction |
|----|---------|--------|-------------|------------|--------------------------|
| T-01 | Communication toward Wendy | Any text, email, or message directed at Wendy | Hard block | Sienna | "Review on impact, tone, and timing. Is this constructive?" |
| T-02 | New initiative or project idea | Owner introduces anything not in the current plan | Priority Gate | Sienna → Marcus | See Sienna Priority Gate in CLAUDE.md. |
| T-03 | Emotional charge in input | Frustration, conflict, major personal decision | Journaling trigger | Penn | Direct to Penn, no confirmation needed. |
| T-04 | Day reflection or personal narrative | Owner shares day, feelings, or experiences | Journaling trigger | Penn | Direct to Penn, no confirmation needed. |
| T-05 | Financial commitment or expenditure | Any explicit commitment or expenditure | Hard block | Vera | "Assess cashflow impact and portfolio exposure." |
| T-06 | Health, exercise, or recovery | Owner asks about movement, nutrition, sleep, or recovery | Scope check | Lena | Route to Lena for coaching context before responding. |
| T-07 | Legal implication | Contract, liability, or compliance question | Alert | None | Stop and ask owner for direction. Do not proceed. |
| T-08 | Major technical or architectural decision | New integration, tool choice, or infrastructure | Pre-brief | Kai | "Review this decision before Larry executes." |
| T-09 | External communication on behalf of owner | Email or message to client, supplier, or partner | Soft block | Domain specialist | "Review for tone, completeness, and risk before sending." |

**Trigger scan rules:**
- Scan every owner input before acting — not after.
- Multiple patterns may match: the most restrictive pre-action gate wins.
- Library grows over time: when a new pattern repeats, add a row and propose it to the owner.

---

## Design: Pre-Action Gate

| Category | Definition | Gate Type | Specialist |
|----------|-----------|-----------|------------|
| G-1 Wendy communication | Any text, email, or message toward Wendy | Hard block | Sienna — mandatory |
| G-2 New initiative | Anything not in the current plan | Hard block | Sienna Priority Gate |
| G-3 External communication | Email or message to client, supplier, or partner | Soft block | Domain specialist advice |
| G-4 Financial commitment | Any explicit commitment or expenditure | Hard block | Vera — mandatory |
| G-5 Irreversible technical action | Delete, migration, production push | Hard block | Kai — mandatory |

**Hard block:** Larry stops completely and waits for specialist advice before taking any step.
**Soft block:** Larry may prepare but not execute until specialist advice is received.

**Gate sequence (hard block):**
1. Larry recognizes a blocked category in the requested action.
2. Larry does not act.
3. Larry briefs the specialist: task + trigger signal (T-XX or G-X) + context.
4. Specialist delivers advice — not a decision.
5. Larry presents the advice to the owner.
6. Owner gives direction.
7. GL-021 write authorization applies to all subsequent writes.

---

## Design: Richer Briefing Template

Every specialist brief contains four elements — in addition to the existing standing instruction ("Good is good enough. Do exactly what is asked."):

1. **Task** — what the owner asked
2. **Trigger** — which pattern activated and why (T-XX or G-X, or "no trigger")
3. **Context** — relevant background (prior decisions, owner patterns, active projects)
4. **Output format** — what Larry needs back (advice / review / execution / ...)

---

## GL-023 Record

- **Interview:** Owner provided full context in session brief. Two open points clarified: (a) trigger library in CLAUDE.md, not separate GL; (b) Wendy gate always hard, regardless of tone.
- **Spec:** This document.
- **Verify plan:** All nine trigger rows confirmed logically complete. Five gate categories confirmed non-overlapping. Sections reference existing mechanisms without duplicating them. CLAUDE.md read back after write.
- **Tool check:** grep over CLAUDE.md for existing mechanisms (Sienna Priority Gate, GL-021, Penn auto-journal) to confirm no duplication.
- **Murphy scan:** Risk: trigger library adds overhead on every input, making Larry feel bureaucratic. Mitigation: triggers are scoped to rare but significant moments, not routine inputs. Rollback: CLAUDE.md section delete, 60 seconds.

---

Delivered on: 2026-06-16
Delivered at: session — Proactive Larry Trigger Library and Pre-Action Gate
