---
name: feedback_plan_before_execute
description: Always present the plan first and wait for confirmation before building or executing anything — never just start
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d84693ed-3179-4fea-bc12-20ebe6460e64
---

Never execute directly without first presenting the plan and receiving confirmation from the owner.

**Why:** The owner wants to maintain control over what is being built. Building ahead without permission feels like overstepping, even when the intention is good.

**How to apply:** For every build or execution task, first show a concrete plan (what will be done, in which steps, with what result) and explicitly wait for "yes, proceed" before making the first tool call. This also applies to scripts, API calls, n8n workflows, and file writes.

**Extended — verify before fixing (Karpathy principle):** Diagnosis must be verified before proposing a fix. Stating "the problem is X" and immediately jumping to a solution skips the proof step. Correct sequence: Diagnose → Verify (prove X is actually the cause) → Propose → Confirm → Execute. This applies especially when diagnosing missing wiring, routing gaps, or behavioral triggers — check all possible paths before concluding one is missing.
