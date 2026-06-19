---
name: feedback_daily_planning_interaction
description: "Daily planning must proceed step by step — do not fetch everything and dump it all at once, interaction must come from the owner"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 79275194-5713-4ed8-b1d1-637bb7a16708
---

The v3 daily planning fetches everything in one round (goals, tasks, completed tasks, projects) and then presents a wall of tables plus multiple questions at once. This takes ~6 minutes and is unworkable.

**Why:** The owner wants to move through the planning carefully, quickly, and step by step. The interaction must come from him — he responds, then the next step follows. Not the other way around.

**How to apply:**
- Phase data fetching: only fetch what is needed for the current step, not everything upfront
- Show Phase 1 (goal scan) as soon as it is ready → wait for blocker answer → then Phase 2
- Skip empty phases without waiting ("no overdue, skip")
- Never ask more than one question per turn
- Handle PPM and BPM sequentially, not in parallel
- Fetch completed tasks only when a goal is potentially stagnant (lazy)
- Speed over completeness: a fast, usable planning beats a perfect slow one
