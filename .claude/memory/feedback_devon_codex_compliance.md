---
name: devon-codex-compliance
description: Route code tasks to Devon — Devon reads + plans, then spawns Codex. Never bypass Devon by routing directly to codex:codex-rescue.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0af27ef4-4e17-40ac-b98a-4b40e0e05ff1
---

Route all build tasks to Devon. Devon reads the specs, plans the implementation, then spawns a codex:codex-rescue subagent for the actual code writing. Do not bypass Devon by routing directly to codex:codex-rescue — that breaks the intended specialist boundary.

**Why:** Devon is the senior developer who owns reading, planning, and implementation coordination. Codex handles the raw code writing inside Devon's session. Skipping Devon removes the planning layer and the specialist boundary.

**How to apply:** Brief Devon as normal. Include the mandatory Codex delegation line in every brief: "Delegate all code writing to a codex:codex-rescue subagent. Read and plan using Claude-side tools, then spawn Codex with --write for the implementation." If Devon fails to spawn Codex, flag it and strengthen enforcement in Devon's AGENT.md — the fix is there, not in routing around Devon.
