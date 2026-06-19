---
name: verify-before-reporting
description: "Always verify that a built service, URL, or feature actually works before reporting it as done"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 110a1cf2-606e-4541-a2e9-cf80179ac2ef
---

After any build task involving a running service, URL, or interactive feature: verify it yourself before reporting completion. Start the services, hit the endpoint, confirm the result. Never just relay what an agent says it built.

**Why:** Twice reported a dashboard URL as working without checking — services were not running. Owner had to correct this both times.

**How to apply:** After Kai (or any agent) builds something that runs as a service or is accessible via URL:
1. Start the service(s)
2. Test the endpoint or open the URL
3. Confirm the expected behavior (e.g. login works, redirect works)
Only then report it as done.
