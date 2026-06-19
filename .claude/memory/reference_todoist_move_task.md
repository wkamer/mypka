---
name: reference_todoist_move_task
description: "Todoist API v1 — move task to another project via POST /api/v1/tasks/{id}/move"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1a2ae651-58e5-405e-9c48-f70bf16cf386
---

Move task to another project + section:

```
POST https://api.todoist.com/api/v1/tasks/{task_id}/move
Body: {"project_id": "<id>", "section_id": "<id>"}
```

PATCH and POST on `/tasks/{id}` do not work for `project_id` (400 / 405).
Sync v9 is deprecated (410).
The `/move` endpoint is the correct route.
