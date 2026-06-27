---
name: feedback-code-review-multi-model
description: Code reviews should use multiple non-context subagents with different models — varied weights catch different issues
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bd21968e-1947-43bb-a633-40605b1ea4cf
---

For code review after a build: use multiple forked subagents with different models (not context-mode agents). Varied model weights cause them to focus on different areas and triage issues differently. Pattern: combo of older coding models + a self-review pass. Each catches things the others miss.

**Why:** Walter explicitly flagged this. Single-model review misses issues that other model weights would catch.

**How to apply:** After any Devon (or other agent) build completes, run at minimum 2-3 review subagents with different models (e.g. sonnet + haiku + opus or similar). Use non-context agents so they come in fresh. Do not rely on a single review pass.
