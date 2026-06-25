# System fix: feedback rules synced to all AGENT.md files

**Date:** 2026-06-25
**Agent:** Larry
**Domain:** Team
**Log ID:** 251

---

## What happened

Walter signalled that proposals were low quality and too many corrections were needed. Larry diagnosed three structural causes:

1. Feedback corrections were captured in project memory but never synced to AGENT.md files
2. Subagents start fresh from their AGENT.md and do not read project memory — so the same mistakes repeated
3. Agents were generating output from pattern rather than reading the actual current state of files

## Decisions

- Larry owns the feedback-to-AGENT.md loop. No owner request needed.
- Feedback sync is a mandatory session close step (step 4) from this point forward.

## Actions taken

- CLAUDE.md updated: session close step 4 (feedback sync), Learning Rule strengthened, weekly Friday scan added
- Nolan briefed and executed: 15 AGENT.md files updated with Learned Rules section
  - Universal rules (8) added to all 15 specialists: agent signature, no dashes, language hard rule, no own interpretations, plan before execute, memory is a pointer, Kamer E-commerce full name, workflow archiving in GL
  - Sienna: 11 agent-specific rules (email, daily planning, inbox, Walter initiates)
  - Kai: 9 agent-specific rules (Discord, check before stopping, commit immediately, integration structure, verify before reporting)
  - Penn: 4 agent-specific rules (WhatsApp archiving, reflections, sparring journals, mail links)
  - Marcus: 5 agent-specific rules (Brain Zen project check, domain routing, Todoist folder link, cleanup cycle G2, SSOT)
  - Lena: 1 agent-specific rule (health resources in KE-Health)
- Committed and pushed: commits d93eb32 (CLAUDE.md) and 6c763bb (15 AGENT.md files)

## Open items

None.
