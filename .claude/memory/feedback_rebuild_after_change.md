---
name: rebuild-after-change
description: "After every frontend code change, rebuild the app and verify it works in the browser before reporting done"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0af27ef4-4e17-40ac-b98a-4b40e0e05ff1
---

Tests green is not the same as working in the browser. If the app serves from a compiled bundle (dist/), source changes are invisible until rebuilt. Owner cannot test if the build is stale.

**Why:** Multiple times fixes were reported as done based on test results, but the browser still showed old behavior because the frontend bundle was not rebuilt.

**How to apply:** After every frontend code change: (1) rebuild the frontend, (2) verify the specific behavior in the running app, (3) only then report done. Never report done based on tests alone for browser-rendered code.
