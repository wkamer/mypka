---
name: feedback_inbox_show_suggestions
description: When processing inbox always show proposed actions first and wait for confirmation — never execute directly
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f8a1778e-ddb9-49fd-9caa-fb7c4ad6f918
---

When processing the inbox, the owner always wants to see the proposed processing actions before anything is executed.

**Why:** The owner wants to maintain control over how inbox items are interpreted and routed.

**How to apply:** For every inbox processing round — whether it is 1 or 10 items — show per item:
- What the item is (transcript / text)
- Proposed action (type + details)
- Routing (who handles it, which system)

Wait for confirmation from the owner before executing. Never proceed automatically based on "obvious" actions.
