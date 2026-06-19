---
name: feedback_brain_zen_project_check
description: During Brain Zen always fetch existing Todoist projects first before assigning — never blindly route to 👤 PERSONAL
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1a2ae651-58e5-405e-9c48-f70bf16cf386
---

When creating tasks from Brain Zen: first fetch existing projects and check whether a task belongs to an existing project. Only then assign a project.

**Why:** A holiday task was created in 👤 PERSONAL while P-Zomervakantie 2026 already existed. That is an SSOT violation.

**How to apply:** For each Brain Zen task: fetch `/api/v1/projects`, check for a logical match on name/subject, propose the project to the owner before creating.
