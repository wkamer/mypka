---
name: feedback_discord_channel_naming
description: "Discord channel names always use \"┃\" (box drawing vertical, U+2503) as separator between icon and name"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d84693ed-3179-4fea-bc12-20ebe6460e64
---

Always use `┃` (box drawing heavy vertical, U+2503) as separator in Discord channel names — never `|` (pipe), because Discord converts that to a dash.

**Why:** The pipe character is automatically converted to a dash by Discord, which breaks the formatting.

**How to apply:** For every Discord channel that is created or proposed: `🔔 ┃ channel-name` instead of `🔔 | channel-name`.
