# GL-010 — Session Logs: Purpose and Discipline

**Applies to:** all agents, all sessions
**Last updated:** 2026-06-03

---

## Why Session-Logs exist

An AI team without Session-Logs has amnesia. Every session restarts cold. The same context gets re-explained, the same decisions get re-made, the same mistake recurs across specialists who were not in the room when the lesson was learned.

An AI team with Session-Logs compounds. By month three, the `session-logs/` folder holds sixty entries. Patterns become visible. The static three start getting revised because the temporal one accumulated. The team gets better over time, not just larger.

**Static knowledge tells the team what to do. Session-Logs tell the team what it did. Without the second, the first never gets revised.**

---

## The four layers

| Layer | What it holds | Where |
|---|---|---|
| SOPs | How to do repeatable work | `Team Knowledge/Core/SOPs/` |
| Workstreams | How recurring orchestrations run | `Team Knowledge/Core/Workstreams/` |
| Guidelines | Static reference rules | `Team Knowledge/Core/Guidelines/` |
| **Session-Logs** | **What the team did and decided** | `Team Knowledge/Core/session-logs/YYYY/MM/` |

The first three are static. Session-Logs are temporal. They are what causes the first three to get updated.

---

## Discipline

- Every substantive session gets a session log — no exceptions.
- The markdown mirror is written alongside the DB entry — both are required.
- Recurring patterns surfaced in session logs become candidates for SOP or Guideline updates.
- A session log without a summary is incomplete. A summary without decisions is shallow.
- The `/close-session` skill automates this. Running it is not optional.
