# Team renames, LiteLLM setup, connection fix

**Date:** 2026-05-02
**Session ID:** 15 (team-knowledge.db)
**Topics:** team-structure, litellm, ollama, infrastructure

## Summary

Session covered four work streams: fixed Ollama PATH in Git Bash (.bashrc) and pulled qwen3:8b as the local free model. Renamed all 7 team member role titles to the "The [X] Agent" convention across folders, CLAUDE.md headers, index files, and journal-agent.md. Attempted LiteLLM proxy setup to route Nolan to free Ollama and complex agents to Anthropic; SessionStart hook and litellm-config.yaml were written. Setting ANTHROPIC_BASE_URL in settings.json caused complete API loss — diagnosed and fixed by removing the env var, restoring direct Anthropic connectivity.

## Decisions

- Team role naming convention standardized to "The [X] Agent" for all 7 specialists
- LiteLLM routes: claude-haiku-4-5-20251001 → ollama/qwen3:8b (free); claude-sonnet/opus → Anthropic passthrough
- ANTHROPIC_BASE_URL must NOT be set in Claude Code settings.json unless LiteLLM is guaranteed running before Claude Code starts
- SessionStart hook retained to start LiteLLM in background; direct Anthropic routing preserved for Claude Code itself

## Actions Taken

- Added Ollama + LiteLLM Scripts directories to ~/.bashrc
- Pulled qwen3:8b model via Ollama
- Renamed 7 team folders to new naming convention
- Updated 7 CLAUDE.md headers
- Updated Core/Team/agent-index.md (all 7 rows)
- Updated Personal/Team/team-index.md (Sienna + Penn rows)
- Updated root CLAUDE.md Sienna path reference
- Updated .claude/agents/journal-agent.md title + location
- Wrote Core/Scripts/litellm-config.yaml
- Wrote Core/Scripts/ensure-litellm.ps1
- Wrote Core/Scripts/start-litellm.ps1
- Installed litellm[proxy] via pip
- Fixed .claude/settings.json: removed ANTHROPIC_BASE_URL, kept SessionStart hook

## Delegations

None (structural admin session)

## Open Items

- Set ANTHROPIC_API_KEY as Windows user env var to enable LiteLLM → Anthropic passthrough
- Consider Windows Task Scheduler to start LiteLLM at login for guaranteed availability

---

Delivered on: 2026-05-02
Delivered at: Core/Knowledge/session-logs/2026-05-02-team-renames-litellm-connection-fix.md
