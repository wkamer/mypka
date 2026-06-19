# improve-system execution + /clear reminder

**Date:** 2026-06-19
**Agent:** Larry
**Domain:** Team
**DB row:** team-knowledge.db session_logs id 246

---

## What happened

After the first close-session of the day, Walter asked why /improve-system had been skipped. Larry had classified the session as routine — incorrect, because Kai's AGENT.md had been structurally updated and a pattern-level gap in GL-023 enforcement had been identified. /improve-system was run.

Found 6 gaps across 5 system layers:

1. Sienna AGENT.md — missing `feedback_communicatie_verzender` rule (email sender name)
2. Lena AGENT.md — missing `feedback_health_resources_ke` rule (KE-Health vs Topic)
3. Penn AGENT.md — missing `feedback_whatsapp_borging` rule (full WhatsApp text including quoted messages)
4. Memory — `feedback_whatsapp_umc_lookup.md` referenced dead UMC system
5. SOP-013 — 5 references to `/opt/mypka-memory/venv/bin/python` (dead path)
6. SOP-001 — entire Step 12 (UMC rebuild) plus all mypka-memory references — dead system in DR SOP

All 6 fixed and committed.

Additionally: Walter asked whether /clear could be auto-triggered at close-session. Confirmed it cannot (client-side command). Added a reminder line to the close-session skill so every session close ends with the prompt to type /clear.

---

## Decisions

- /improve-system must not be skipped when AGENT.md rules change or structural gaps are identified — these always qualify as significant sessions.
- /clear reminder is now standard output at every close-session.

---

## Actions taken

- Sienna AGENT.md: Never Does rule added — email always by sender name, not organisation
- Lena AGENT.md: Never Does rule added — fitness/nutrition/sleep resources go to KE-Health.md
- Penn AGENT.md: Never Does rule added — always include quoted message in WhatsApp saves
- `feedback_whatsapp_umc_lookup.md` deleted from memory; MEMORY.md updated
- SOP-013: `/opt/mypka-memory/venv/bin/python` replaced with `python3` (all occurrences)
- SOP-001: Step 12 removed, verification rows removed, backup entry removed, credential section removed
- close-session.md: /clear reminder line added as final output

---

## Open items

None new. Cloudflare Zero Trust route for dashboard.kmerbase.com remains open from session 245.
