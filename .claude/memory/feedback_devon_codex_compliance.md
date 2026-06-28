---
name: devon-codex-compliance
description: Devon repeatedly fails to spawn Codex — Larry should route code tasks directly to codex:codex-rescue instead of briefing Devon
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0af27ef4-4e17-40ac-b98a-4b40e0e05ff1
---

Devon does not reliably spawn Codex subagents even when the brief explicitly requires it. This has happened multiple times (commit ca60ade fixes this pattern, but the issue recurs). Bypassing Devon is NOT the fix — Codex invocation belongs inside Devon's role.

**Why:** Devon's AGENT.md has the Codex-first rule documented in multiple places (top section, Never Does, Critical rules, Learned Rules), but Devon ignores it in practice despite explicit instructions in the brief.

**How to apply:** The fix is in Devon's AGENT.md — the Codex-first step must be made even more impossible to skip. Whenever Devon fails to use Codex, flag it and strengthen the enforcement in Devon's AGENT.md. Do not bypass Devon by routing directly to Codex — that breaks the intended specialist boundary.
