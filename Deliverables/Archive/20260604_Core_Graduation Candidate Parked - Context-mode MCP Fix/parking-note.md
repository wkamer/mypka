# Graduation Candidate — Parked

**Status:** Parked — not approved for triage, not approved for implementation
**Date parked:** 2026-06-04
**Parked by:** Owner Walter Kamer
**Session origin:** Memory Domain Routing Triage + GL-015 Proposal + Context-mode fix (session_log id 146)

---

## Candidate

**Name:** Context-mode MCP fix procedure

**Suggested destination:** SOP — for example `SOP-016_Context-mode MCP fix after upgrade.md`

**Reason for candidacy:**
After each context-mode upgrade, the MCP server registration in `~/.claude.json` must be manually updated to point to the new version path. The pattern is reproducible and predictable: v1.0.162 introduced a change where the plugin skips `settings.json` MCP registration ("plugin hooks.json is sufficient"), but Claude Code v2.1.159 only exposes MCP tools from persistent user-scope servers — not from dynamic plugin config. Multiple agents may encounter broken ctx\_* tools after any future upgrade.

**Fix pattern (for reference only — not an approved SOP):**
```bash
claude mcp remove plugin_context-mode_context-mode -s user
claude mcp add plugin_context-mode_context-mode --scope user -- /usr/bin/node \
  /home/admin/.claude/plugins/cache/context-mode/context-mode/<VERSION>/start.mjs
```
Server name must be `plugin_context-mode_context-mode` to match the hook matchers in `hooks/hooks.json`.

---

## Owner Decision

Owner Walter Kamer has reviewed this candidate and decided to park it for later.

- Do not triage
- Do not create SOP-016
- Do not create a formal proposal
- Do not create or update any backlog item
- Auto-creation remains forbidden

---

## Reactivation

When the Owner is ready to act on this candidate, reference this file and confirm:
"Approve triage of graduation candidate: Context-mode MCP fix procedure."

Larry then initiates the SOP creation flow per SOP-003 / Nolan handoff.

---

*Delivered on: 2026-06-04*
*Delivered at: Deliverables/20260604_Core_Graduation Candidate Parked - Context-mode MCP Fix/parking-note.md*
