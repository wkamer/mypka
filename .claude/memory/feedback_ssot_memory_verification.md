---
name: feedback-ssot-memory-verification
description: "Memory is a pointer, not a source — always read the actual file before answering"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: aaff4ea5-1ce8-4949-8ff3-897d0195333f
---

When memory contains a file path, always read the actual file before answering. Never answer directly from memory when an SSOT file exists.

**Why:** Memory had incorrect paths (`Kyara.md` instead of `Kamer, Kyara.md`) and birth dates that were never written to the CRM files. This caused outdated and incorrectly routed information to be given as answers.

**How to apply:** For every memory entry with a file path: read the file first. If the file does not exist or the path is wrong: correct memory and restore the SSOT before answering. Writing data to memory without also writing to SSOT is not permitted.
