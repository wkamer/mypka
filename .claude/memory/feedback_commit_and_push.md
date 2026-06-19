---
name: commit-and-push
description: "After every successful change, always commit AND push immediately"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 110a1cf2-606e-4541-a2e9-cf80179ac2ef
---

Commit and push only after the owner confirms the feature works in the real environment. Do not commit on Larry's technical verification alone.

**Why:** Owner's confirmation is the acceptance gate. Larry's curl tests are a sanity check, not approval.

**How to apply:** Sequence is always — Kai builds → Larry verifies technically → Owner tests → Owner confirms → commit and push. One clean commit per completed feature, not per intermediate fix.
