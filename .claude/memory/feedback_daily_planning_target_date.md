---
name: feedback_daily_planning_target_date
description: Target date for daily planning without parameter is time-based — before 18:00 today, from 18:00 tomorrow
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 79275194-5713-4ed8-b1d1-637bb7a16708
---

When starting `/start-daily-planning-v3` without a parameter: target date is time-based.

- **Before 18:00** → target = today (mid-day review or correction)
- **From 18:00** → target = tomorrow (evening planning for the next day)

**Why:** After 18:00 the day is operationally done — wrapping up tasks no longer fits. Planning is then by definition for tomorrow.

**How to apply:** Determine the target date based on local time at the start of the skill. Parameters `morgen` and `vandaag` always override this. Never ask.
