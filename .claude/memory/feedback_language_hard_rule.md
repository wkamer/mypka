---
name: feedback-language-hard-rule
description: "Language is a hard rule — system files and console output always EN, owner input EN or NL"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 39da2b1e-fcf1-4063-a687-feff575ff055
---

System files always EN — no exceptions. This includes DB records, .md files, AGENT.md, skills, active-context.md, SOPs, GLs, session logs.

Console output always EN.

Owner input: EN or NL — both accepted.

**Why:** Dutch was leaking into system files (active-context.md had Dutch prose). The owner called this out as a hard rule violation, not a preference.

**How to apply:** Before writing any system file, check that all prose is in English. Goal and project names (proper names) stay as-is. Journal content stays in the owner's language.
