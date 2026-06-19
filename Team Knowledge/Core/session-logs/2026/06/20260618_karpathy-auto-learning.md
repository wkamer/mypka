# Implement Karpathy-style auto-learning for team agents

| Field | Value |
|---|---|
| Date | 2026-06-18 |
| Agent | Larry |
| Domain | Team |
| DB id | 238 |

## What happened

Analyzed the current auto-learning implementation and identified three disconnected systems, none of them active. Compared against the Karpathy method and implemented a minimal solution: 16 notes.md files created (one per specialist), Task Discipline updated in 15 AGENT.md files to read notes.md before tasks and append after corrections. Journals removed from the active protocol — templates kept as silent fallback. /improve-system updated with feedback propagation check.

## Decisions

- notes.md is the single active learning loop
- Journal steps removed from Task Discipline as dead weight — templates kept as silent fallback

## Actions taken

- 2 commits: 1ba1ac0 (notes.md + Task Discipline), 31f6e42 (journal steps stripped)
- 16 notes.md files created (one per specialist)
- 15 AGENT.md Task Discipline sections updated
- /improve-system updated with feedback propagation check

## Open items

None
