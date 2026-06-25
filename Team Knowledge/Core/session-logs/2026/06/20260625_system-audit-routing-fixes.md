# Session Log — 2026-06-25

**Title:** System audit + routing fixes — Devon, Kai boundary, Learned Rules
**Agent:** Larry
**Domain:** Team
**Topics:** system-audit, routing, learned-rules, team-structure
**DB id:** 253

---

## What happened

Iris conducted a deep system audit at the owner's request, triggered by repeated routing errors (Larry delegating to wrong specialist, executing domain work himself). The audit revealed 5 critical issues, 6 structural gaps, and 8 drift items. Root cause: Devon was onboarded on 2026-06-25 but Larry's own AGENT.md and CLAUDE.md routing rules were not updated to reflect the Kai/Devon split.

All Prio 1, 2, and 3 fixes were applied in the same session. team-knowledge.db was diagnosed by Kai as fully operational — Iris had tested the wrong path using a CLI not installed on this host.

---

## Decisions

- Kai scope: integrations and infrastructure only. Not general coding.
- Devon scope: product feature builds, frontend/backend, UI wiring.
- Larry's domain Bash is forbidden. Only structural Bash allowed (mkdir, ls, find, git status/log).
- GL archive documented in gl-index.md.

---

## Actions taken

- Iris system audit executed (full audit summary presented to owner)
- CLAUDE.md: Iron Rule updated, Kai row corrected, Devon added to team table and routing rule, changelog added
- Larry AGENT.md: 11 Learned Rules added, Bash boundary hardened, Delegation Step 6 updated for Devon, outgoing routing updated
- Nolan AGENT.md: 4 rules added (propose before writing, draft only when asked, team hiring confirmation, system names in English)
- Iris AGENT.md: 2 rules added (propose before writing, draft only when asked)
- gl-index.md: Archive section added with 8 archived GLs and archive reasons
- active-context.md: last session translated to English
- team-knowledge.db: stale 0-byte file at wrong path removed by Kai

---

## Open items

- Advisory board beslissing — echte mensen vs. AI challenger-laag (owner decision, no deadline set)
- Email inbox viewer — standalone app, Devon, not started (team_task id: 106)
