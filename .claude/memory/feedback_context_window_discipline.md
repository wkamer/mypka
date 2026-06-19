---
name: feedback_context_window_discipline
description: Run /compact after each completed task block — never let a session grow past 2-3 major items without compacting
metadata: 
  node_type: memory
  type: feedback
  originSessionId: aeb9a06c-7ada-4660-8382-a9a0d915db19
---

Run `/compact` after each completed major task block (each B-item, each deliverable). Never let an audit session accumulate more than 2-3 items before compacting.

**Why:** Session hit 1M context limit on 2026-06-03 during AI team audit work (B-021A + B-005A + B-030 + B-030A + B-030B + B-021B in one session). `/compact` failed with "Usage credits required for 1M context" error. Owner explicitly said: "Ik wil dit echt voorkomen in de toekomst!"

**How to apply:** After each B-item or major deliverable is confirmed complete, run `/compact` before starting the next item. Suggest this to the owner at natural breakpoints in audit sessions.
