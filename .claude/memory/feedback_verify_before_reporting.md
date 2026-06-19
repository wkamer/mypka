---
name: verify-before-reporting
description: "Always verify that a built service, URL, or feature actually works before reporting it as done"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 110a1cf2-606e-4541-a2e9-cf80179ac2ef
---

Technical verification after a build is Kai's responsibility, not Larry's. Larry synthesizes Kai's verification report for the owner — never runs curl, API tests, or service checks himself.

**Why:** Larry violated the Iron Rule by running technical verification himself. Verification is domain execution — it belongs to Kai.

**How to apply:** Kai's brief must always include a verification step as part of "done looks like." Larry receives Kai's report and synthesizes it for the owner. Owner confirms in real environment. Larry routes confirmation back to Kai to commit and push.
