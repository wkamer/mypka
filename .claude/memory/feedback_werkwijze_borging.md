---
name: feedback-werkwijze-borging
description: "Always record working methods in a GL file, not just in memory — so all agents follow them"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4b3957ab-21c0-4acd-9770-55a5b389fa48
---

When a working method, convention, or format is established: always record it in a GL file in `Team Knowledge/Core/Guidelines/`, not just in memory.

**Why:** Memory is Claude's personal context. Agents read their own AGENT.md and the GL files — not Claude's memory. A working method that only exists in memory will not be followed by other agents. The owner then has to mention it repeatedly.

**How to apply:**
1. Determine whether the rule applies to multiple agents or situations
2. If so: create a GL file (GL-008, GL-009, etc.) in `Team Knowledge/Core/Guidelines/`
3. Add to `gl-index.md`
4. Memory may contain a pointer, but the content lives in the GL

Applies to: formats, workflows, naming conventions, recording conventions, communication standards.
