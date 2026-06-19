# Session Log — 2026-06-17

**Slug:** gl021-updated-language-rule-en-only
**Agent:** Larry
**Domain:** Team / Core

## What happened

GL-021 updated with two structural changes:
1. Skill files (`.claude/commands/`) explicitly named as file system writes in Section 4.2 — propose before writing applies without exception; approach approval does not constitute content write authorization.
2. All UMC references removed from Sections 4.1, 6.5, 7, 8 (6 edits total — one additional reference surfaced during verification and cleaned immediately).

Language rule hardened: system files always EN, no exceptions. Console output always EN. Owner input EN or NL accepted. Updated in CLAUDE.md, Larry AGENT.md, and memory.

## Decisions

- Language is a hard rule — no Dutch in system files or console output
- Skill files require the same write authorization as any other file write
- Approach approval ("option B", "go ahead") does not constitute write authorization for specific content

## Actions taken

- GL-021: 6 surgical edits (last reviewed date, Section 4.1, 4.2, 6.5, 7, 8)
- CLAUDE.md: language convention updated
- Larry AGENT.md: language section rewritten
- active-context.md: Dutch prose replaced with English
- Memory: feedback_language_hard_rule.md saved

## Open items

*(none)*
