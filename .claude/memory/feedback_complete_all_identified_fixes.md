---
name: complete-all-identified-fixes
description: "When multiple fixes are identified in one process, execute all of them in the same action — not just the one the owner explicitly named"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e52be7a3-4aad-4afa-b870-f751dfbb3113
---

When a set of issues is identified and the owner confirms one fix, execute ALL identified fixes in that same action unless the owner explicitly says to skip the others.

**Why:** In the GL-024 / Cleo session (2026-06-27), Larry identified three issues: (1) GL-024 wrong, (2) CLAUDE.md missing Cleo, (3) stale Sloane reference. Owner said "pas GL-024 aan." Larry only fixed GL-024 and left CLAUDE.md incomplete. Owner had to follow up.

**How to apply:** When proposing multiple fixes and the owner confirms, treat the confirmation as covering all identified fixes unless explicitly scoped otherwise. Do not wait for a second confirmation per fix.
