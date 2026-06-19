---
name: todoist-project-folder-link
description: "Todoist 📂 resource task — clean name in content, link as [Open](...) in description"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4b3957ab-21c0-4acd-9770-55a5b389fa48
---

Resources tasks in Todoist always structured as follows (the `* ` prefix removes the checkbox):

**📂 folder task:**
- **Content:** `* 📂 P-Name`
- **Description:** `[Open](file://raspberrypi.local/myPKA/<url-encoded path>/)`

**🎯 goal task (only for goal-driven projects):**
- **Content:** `* 🎯 G-Name`
- **Description:** path to the goal folder

**📅 event task (only for event-driven projects):**
- **Content:** `* 📅 Event: [description] — [date]`
- **Description:** (empty or extra context)

The `* ` prefix (asterisk + space) applies to ALL resource tasks. It removes the checkbox.
Spaces in the path always URL-encoded (`%20`). With encoding the link is clickable in the description field.

Path follows the domain (see GL-004):
- Personal: `PKM/My Life/Projects/P-Name/`
- Kamer E-commerce: `Team Knowledge/Kamer E-commerce/Projects/P-Name/`
- Geldstroom Regie: `Team Knowledge/Geldstroom Regie/Projects/P-Name/`
