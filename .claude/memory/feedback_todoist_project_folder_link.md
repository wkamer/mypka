---
name: feedback-todoist-project-folder-link
description: The 📂 folder reference in the Resources section of each Todoist project must be a clickable link to the network location on the owner's laptop.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9ee1fbf6-8402-49f6-9abd-4682dad011f1
---

The 📂 task in the Resources section of a Todoist project must be a clickable Markdown link, not plain text.

**Format:**
- Task content (title): `📂 P-Projectname` (plain text, not clickable)
- Task description: `[\\raspberrypi.local\myPKA\PKM\My Life\Projects\P-Projectname](file://raspberrypi.local/myPKA/PKM/My%20Life/Projects/P-Projectname)` (clickable Markdown link)

**Network path base (for now):** `\\raspberrypi.local\myPKA`
**URL base:** `file://raspberrypi.local/myPKA`
**Spaces in path:** URL-encode as `%20`

**Why:** The owner wants to navigate directly from Todoist to the project folder on his laptop. Plain text is not clickable.

**How to apply:** For every new project (personal, Kamer E-commerce, Geldstroom Regie) always create the 📂 Resources task as a Markdown link. Fix existing projects when they come up.

Related: [[feedback_personal_project_convention]]
