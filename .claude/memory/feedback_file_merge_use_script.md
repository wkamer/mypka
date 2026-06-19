---
name: feedback_file_merge_use_script
description: "For bulk file operations (template filling, merging, batch rename), always use a Python script — never spawn an agent with Read/Write loops"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: aeb9a06c-7ada-4660-8382-a9a0d915db19
---

For bulk file operations where the logic is fixed and data is already in files (template filling, merging content into a template, batch processing), always use a Python script run via Bash — never spawn an agent that calls Read/Write in a loop.

**Why:** An agent calling Read 60 times + Write 20 times took 41 minutes for a task a Python script completes in under 10 seconds. Agent overhead (context, tokens, tool call latency) makes it the wrong tool for mechanical file operations.

**How to apply:** When the task is "read N files, fill template, write N files" — write a Python script and run it via Bash. Reserve agents for tasks requiring judgment, research, or multi-step reasoning that cannot be expressed as a simple script.
