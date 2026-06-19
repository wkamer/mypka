# UMC auto-index hook voor PKM bestanden — 2026-05-25

**Session date:** 2026-05-25
**Topics:** umc, indexing, hooks, automation

## Summary

Gap geïdentificeerd: nieuwe PKM bestanden werden niet automatisch in de UMC geïndexeerd. umc_index_hook.sh gebouwd die Write en Edit tool calls op .md bestanden in PKM/ automatisch indexeert via MemoryManager. settings.json bijgewerkt met Write|Edit matcher als derde PostToolUse hook.
