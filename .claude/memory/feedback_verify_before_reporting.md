---
name: verify-before-reporting
description: "Always verify that a built service, URL, or feature actually works before reporting it as done"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 110a1cf2-606e-4541-a2e9-cf80179ac2ef
---

After every build task: verify the feature actually works before reporting done. Build is not proof. Commit is not proof.

**Why:** Reported "done" twice without verifying. The Karpathy principle applies to builds: build → verify behavior → then report. Reading files and running code does not equal a working feature.

**How to apply (Claude Code context):**
1. Start the service (or confirm it is running with updated code)
2. Test every new endpoint: auth check (401), happy path, edge case (404)
3. Confirm frontend routes exist in App.jsx and components render
4. Only then: commit, push, report done

**Larry routing note:** When Larry delegates to Kai, verification must be part of Kai's "done looks like" brief. Larry never reports done based on Kai's word alone — Kai must return a verification result.
