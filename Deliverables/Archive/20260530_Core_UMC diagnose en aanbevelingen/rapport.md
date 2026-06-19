# UMC Diagnosis Report — Unified Memory Core
**Prepared by:** Kai, Infrastructure & Integration Architect
**Date:** 2026-05-30

---

## 1. UMC Table Inventory

| Table | Rows | Latest entry | Status |
|---|---|---|---|
| `memory_summaries` | 164 | 2026-05-29 | Active — driven by close routines |
| `memory_knowledge` | 1876 | 2026-05-30 | Active — driven by knowledge_indexer |
| `memory_entities` | 95 | 2026-05-30 | Active — driven by Penn |
| `tool_logs` | 62 | 2026-05-30 | Active — driven by PostToolUse hook |
| `conversational_memory` | 28 | 2026-05-29 | Active — driven by daily-routines thread |

No table is empty or completely abandoned. However, depth and distribution vary significantly across tables and agents.

### memory_summaries breakdown

| Domain | Source type | Count | Period |
|---|---|---|---|
| personal | session_log | 47 | 2026-05-20 to 2026-05-29 |
| core | session_log | 77 | 2026-05-20 to 2026-05-20 |
| core | manual | 2 | 2026-05-20 |
| team | session_log | 18 | 2026-05-20 to 2026-05-28 |
| kamer-ecommerce | session_log | 9 | 2026-05-20 only |
| geldstroom-regie | session_log | 9 | 2026-05-20 only |
| gr | session_log | 2 | 2026-05-26 to 2026-05-27 |

Key observation: zero summaries carry agent-specific source_types such as `orchestration`, `infrastructure`, `hr`, `research`, `project_management`, `wordpress`, `market_validation`, `product_intelligence`, `ads_intelligence`, `operations`, `shopify`, `portfolio_management`, `journal`, or `personal_assistant`. All summaries use `session_log` — written exclusively by the close-session/close-routine scripts, not by the specialist agents themselves.

### tool_logs: only three agent slugs ever appeared

| Agent slug | Tools used |
|---|---|
| hook | Write, Edit, ctx_batch_execute, ctx_execute, Agent, WebFetch (automated via PostToolUse hook) |
| larry | get_tasks, read_file, smoke |
| call-001 | search_summaries |

No specialist agent (Penn, Sienna, Sasha, Remy, Finn, etc.) has ever logged a tool call directly under their own agent slug.

---

## 2. Agent Coverage Audit

All 14 AGENT.md files contain a `## UMC` section. The section is structurally complete in every file, covering:
- Interpreter path
- Session start: `get_summary_pointers` + domain-specific `search_knowledge`
- Large output handling (PostToolUse hook reference)
- Session close: `write_summary` with domain and source_type
- Fallback: "UMC niet bereikbaar" message

Penn has additional UMC content earlier in her file (the entity extraction block), and her UMC section also includes `search_entities`.

**Structural coverage: 14/14 (100%)**
**Actual execution coverage: 0/14 (0%)**

---

## 3. Expected vs Actual Usage

### What the spec requires (per CLAUDE.md)

| Trigger | Expected action | Who executes |
|---|---|---|
| Session start | `mm.get_summary_pointers(limit=3)` | Every agent |
| Session start | `mm.search_knowledge(query, domain=X)` | Every agent |
| After journal entry | `mm.extract_and_store_entities(text)` | Penn |
| Large in-code output | `mm.offload_if_large(...)` | Every agent |
| Session close | `mm.write_summary(domain=X, source_type=Y)` | Every agent |
| Session close | `mm.write_message(thread_id="daily-routines")` | close-session script |

### What actually happens

| Trigger | Actual execution |
|---|---|
| Session start | Not observed in any agent session. `get_summary_pointers` is never called by agents. |
| Knowledge search before reading | Not observed. Agents go directly to file reads. |
| After journal entry | Penn extracts entities — this works. 95 entities present, written on recent dates. |
| Large tool output offload | Works via the PostToolUse hook (automated, agent-agnostic). |
| Session close | The close-session skill calls `close_routine_verification.py`, which calls `write_summary`. This works when the routine is used. |

Penn's entity extraction is the only agent-driven UMC write that actually happens. The rest is handled by infrastructure (hooks, scripts) rather than by agents executing Python themselves.

---

## 4. Root Causes

### RC-1: write_summary is never called by specialists — only by close routines

The 14 AGENT.md files instruct specialists to call `mm.write_summary(...)` at session close. But specialists are not autonomous processes that run Python at the end of a session. They are invoked within a Larry session. When the session ends, the close-session skill calls `close_routine_verification.py`, which writes one summary per session — not one per specialist. The domain on that summary reflects the session topic (personal, team, ke, gr), not the specialist who did the work.

There is no mechanism that causes Sasha to write a summary with `source_type="shopify"` when she finishes a Shopify task. The instruction exists in her AGENT.md, but she has no session boundary of her own.

### RC-2: Domain naming is inconsistent

The close-session skill accepts `--domain ke` and `--domain gr` (short forms). `close_routine_verification.py` passes these directly to `mm.write_summary()`. The result: `memory_summaries` contains rows with domain `"ke"` and `"gr"` mixed with `"kamer-ecommerce"` and `"geldstroom-regie"`. Semantic search across these domains will miss entries depending on which name is used in the query. This split is visible in the data: `geldstroom-regie` has 9 entries (from backfill), `gr` has 2 (from recent close-session calls).

### RC-3: Session start UMC reads are not enforced

Every AGENT.md instructs agents to call `get_summary_pointers` before doing work. This is text-level instruction with no enforcement. In practice, agents proceed directly to file reads or tool calls. There is no hook that triggers a memory load at the start of a session, and agents do not invoke the Python code themselves. The context is therefore cold at every session start.

### RC-4: Penn's write_summary at session close is a dead letter

Penn's AGENT.md instructs her to call `mm.write_summary(..., domain="personal", source_type="journal")` at session close. This never happens, because Penn does not have a distinct session. She is invoked inside the main session. Her entity extraction (after journal entry) works because that instruction is specific and actionable inside her execution flow. The session-close summary is not.

### RC-5: No agent-attribution in summaries

All summaries written through `close_routine_verification.py` use `source_type="session_log"`. Even if a session was primarily Sasha executing Shopify work, the summary says `source_type=session_log, domain=ke`. There is no way to filter summaries by which specialist did the work. Semantic search returns results, but attribution is lost.

---

## 5. Recommendations

### Priority 1 — Fix domain naming inconsistency (immediate)

Standardize domain names across all entry points. The canonical set should be:
- `personal`
- `team`
- `kamer-ecommerce`
- `geldstroom-regie`
- `core`

Action: update `close_routine_verification.py` to map short forms `ke` -> `kamer-ecommerce` and `gr` -> `geldstroom-regie` before passing to `write_summary`. Also update the close-session skill to pass the full domain name, or let the script handle the mapping.

Backfill: update the 2 existing `gr` rows in `memory_summaries` to `geldstroom-regie`.

### Priority 2 — Replace the write_summary instruction in AGENT.md with a delegation to the close-session script

The current AGENT.md instruction (`mm.write_summary(...)`) asks specialists to do something they cannot do in practice. Replace it with a delegation model: when a specialist finishes a substantive task, she writes a one-line handoff note to the session context (e.g. "Sasha completed Shopify product sync — see close-session for borging"). The close-session skill then reads the handoff notes and writes one composite summary per domain active in the session, with the correct source_type.

This aligns execution with how the system actually works, rather than expecting specialists to manage their own session boundaries.

### Priority 3 — Add a SessionStart hook for UMC context loading

The session-start UMC read (`get_summary_pointers`) is currently a text instruction with zero enforcement. Add a SessionStart hook that automatically calls `get_summary_pointers(limit=3)` and injects the result as a compact context block at the start of every session. This makes the memory-first principle automatic rather than aspirational.

The hook can be minimal: call the Python script, output max 500 chars to stdout, exit 0. The Claude Code harness will include the output in the session preamble.

### Priority 4 — Add source_type attribution to specialist summaries

When close-session writes a summary, it should record which specialists were active and what their contribution was. Extend `close_routine_verification.py` with an optional `--agents` argument (comma-separated list). Each specialist listed gets its own `agent_learnings` row, and the main summary gets a structured tag. This enables future queries like "what has Sasha written about recently?"

### Priority 5 — Periodic validation cron

No one currently checks whether the UMC is actually receiving writes. Add a weekly cron that runs a simple validation: count entries per domain per week, compare to expected minimum based on session activity, and post a summary to Discord or the Team Inbox if any domain goes silent for 7+ days. This surfaces drift before it becomes a gap.

---

## Summary Assessment

The UMC infrastructure is solid and functional. PostgreSQL is running, all five tables exist, embeddings are being stored, and the PostToolUse hook correctly offloads large tool outputs. The knowledge_indexer has populated memory_knowledge with 1876 entries across all domains.

The core gap is behavioral: specialist agents are instructed to write to the UMC at session start and close, but they have no mechanism to execute that instruction autonomously. The only actual agent-driven UMC write is Penn's entity extraction, which works because it is embedded directly in her processing flow with a concrete code block.

The fix does not require rebuilding the UMC. It requires aligning the instructions with how agents actually operate: hooks for automated behavior, explicit script calls in routines for session-boundary actions, and removal of the "specialist calls Python at session close" fiction from all AGENT.md files.

---

Delivered on: 2026-05-30
Delivered at: 08:24
