---
name: persistent-data-in-db
description: Persistent data must always be stored in the DB — never only in JS memory or React state
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0af27ef4-4e17-40ac-b98a-4b40e0e05ff1
---

Any data that must survive a page refresh or component remount must be persisted to the database. In-memory state (React state, module-level JS objects) is session-only and is not acceptable for persistent data.

**Why:** A Codex fix lifted execution log and action states to React state, which fixed accordion collapse/reopen within a session but failed on page refresh. The DB already stored the data — the frontend just wasn't reading it back. Lifted JS state is never a substitute for reading from the DB.

**How to apply:** When speccing or implementing any stateful UI behavior, ask: does this data need to survive a refresh? If yes, it must be written to the DB and read back on mount. Never accept in-memory session state as the persistence layer for user-facing data.
