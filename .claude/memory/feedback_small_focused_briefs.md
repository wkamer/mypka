---
name: small-focused-briefs
description: "Owner wants fast iteration — keep specialist briefs small and focused, never bundle multiple tasks into one brief"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0af27ef4-4e17-40ac-b98a-4b40e0e05ff1
---

Owner wants to iterate quickly. Large combined briefs (multiple fixes in one) slow down the cycle because Codex writes all fixes sequentially inside one session — wall-clock time is the sum of all fixes, not the longest one.

**Why:** Explicitly stated: "snel en gericht is pre, ik wil snel itereren." Observed: 3 fixes bundled into one Devon brief caused a 17-minute build. Same 3 fixes as parallel Devon briefs would take ~6 minutes (longest single fix).

**How to apply:** One brief = one task. When multiple independent fixes are needed, spawn separate Devon briefs in parallel — each spawns its own Codex, they run concurrently. Total time approaches the longest single fix. Only bundle when fixes are truly sequential (one depends on the other).
