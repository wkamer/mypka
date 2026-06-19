---
name: feedback_script_output_verbatim
description: "Never introduce or describe script stdout — show it directly as own text, no preamble"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e1b074ce-75a2-4a0a-94fe-eb29c96aa0ec
---

Script output always placed directly as own text. Never introduce with "Here is the output of the script", "I have run the script", or similar phrases.

**Why:** The owner does not see the bash tool output. Claude's text IS the output. An introduction is noise and breaks the illusion that Claude itself is executing the planning.

**How to apply:** Run the script → place the full stdout directly in the response, without a single introductory sentence. First character of the response is the first character of the script output.
