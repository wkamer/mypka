---
name: todoist-api-endpoint
description: Todoist API is on v1 — always use https://api.todoist.com/api/v1/ (not the old /rest/v2/ which returns 410)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4b3957ab-21c0-4acd-9770-55a5b389fa48
---

Todoist REST API has been migrated to v1. Always use:

- Tasks: `https://api.todoist.com/api/v1/tasks`
- Projects: `https://api.todoist.com/api/v1/projects`
- Sections: `https://api.todoist.com/api/v1/sections`

The old `/rest/v2/` endpoints return HTTP 410 Gone. Never try these again.

Token via `todoist_helper.py` from `/opt/myPKA/Team Knowledge/Core/Integrations/todoist/`.
