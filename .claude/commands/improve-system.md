---
description: Audit all permanent system layers, surface what is stale or missing, propose changes for owner confirmation. Owner-triggered only — not part of daily close.
allowed-tools: Bash Read Write Edit
---

# /improve-system

Scans 5 system layers in order. Produces a structured report in chat. Does not execute fixes — surfaces and proposes. Owner confirms per item.

---

## Layer 1 — AGENT.md files

Path: `/opt/myPKA/Team/*/AGENT.md` (16 files)

Check each file for:
- References to removed systems: UMC, memory_manager, `/opt/mypka-memory/`, pgvector, LCL, GL-017, SOP-019, GL-022
- Missing "Never Does" section
- Missing changelog entry or changelog entry older than 90 days

```bash
grep -rl "memory_manager\|mypka-memory\|pgvector\|UMC\|LCL\|GL-017\|SOP-019\|GL-022" /opt/myPKA/Team/*/AGENT.md 2>/dev/null
```

For each file with a hit: note which dead reference was found.

For "Never Does" section: scan each AGENT.md for the literal string `Never Does`. Flag any file missing it.

For changelog age: scan each AGENT.md for the last date in a `## Changelog` or `### Changelog` section. If absent or older than 90 days from today, flag it.

**Feedback propagation check:**
Scan `~/.claude/projects/-opt-myPKA/memory/feedback_*.md` for rules that should be in a specialist's AGENT.md but are not yet there. For each feedback file: read the rule, identify which specialist it applies to (if domain-specific), check whether the rule or its equivalent already appears in that specialist's AGENT.md. Flag any rule that is missing from the relevant AGENT.md and propose adding it.

```bash
ls ~/.claude/projects/-opt-myPKA/memory/feedback_*.md
```

---

## Layer 2 — CLAUDE.md

Path: `/opt/myPKA/CLAUDE.md`

Read the file directly. Check for:
- References to removed systems: UMC, memory_manager, LCL, governance overhead
- Session rhythm steps that describe a system no longer in use
- Hard stops or routing rules that reference team members not present in `/opt/myPKA/Team/`

Cross-reference: list actual folders in `/opt/myPKA/Team/` and compare to the team roster table in CLAUDE.md.

```bash
grep -n "memory_manager\|mypka-memory\|pgvector\|UMC\|LCL" /opt/myPKA/CLAUDE.md
ls /opt/myPKA/Team/
```

---

## Layer 3 — SOPs and GLs

Paths:
- `/opt/myPKA/Team Knowledge/SOPs/`
- `/opt/myPKA/Team Knowledge/Core/Guidelines/`

Check active files (not in Archive/) for:
- References to archived system files: SOP-007, SOP-016, SOP-019, GL-013, GL-015, GL-016, GL-017, GL-018, GL-019, GL-022
- References to `/opt/mypka-memory/venv/bin/python` (the venv is gone)

```bash
grep -rn "mypka-memory\|SOP-007\|SOP-016\|SOP-019\|GL-013\|GL-015\|GL-016\|GL-017\|GL-018\|GL-019\|GL-022" \
    "/opt/myPKA/Team Knowledge/SOPs/" \
    "/opt/myPKA/Team Knowledge/Core/Guidelines/" \
    2>/dev/null | grep -v "/Archive/"
```

Note each hit: filename + line number + matched pattern.

---

## Layer 4 — active-context.md

Path: `/opt/myPKA/Team Knowledge/Core/active-context.md`

Read the file. Then check:
- Projects listed: verify each exists in `/opt/myPKA/PKM/My Life/Projects/`
- Goals listed: verify each exists (not archived) in `/opt/myPKA/PKM/My Life/Goals/`

```bash
ls "/opt/myPKA/PKM/My Life/Projects/"
ls "/opt/myPKA/PKM/My Life/Goals/"
```

Flag any entry in active-context.md that does not match a live folder. Stale factual entries can be cleaned directly (no confirmation needed for factual cleanup).

---

## Layer 5 — Config and hooks

Paths:
- `/opt/myPKA/.claude/settings.json`
- `/opt/myPKA/.claude/commands/` (all skill files)

Check for:
- References to `/opt/mypka-memory/venv/bin/python`
- References to UMC, memory_manager, memory_config

```bash
grep -rn "mypka-memory\|memory_manager\|memory_config\|UMC" \
    /opt/myPKA/.claude/settings.json \
    /opt/myPKA/.claude/commands/ \
    2>/dev/null
```

Note each hit: file + line number + matched pattern.

---

## Output format

After all 5 layers are scanned, produce this report in chat:

```
## /improve-system — [YYYY-MM-DD]

### Layer 1 — AGENT.md (16 files)
[finding per specialist, or "No gaps found"]

### Layer 2 — CLAUDE.md
["Current" or finding per section]

### Layer 3 — SOPs and GLs
[finding per file, or "No gaps found"]

### Layer 4 — active-context.md
["Current" or stale entries found]

### Layer 5 — Config and hooks
["All paths valid" or broken references found]

---
## Proposed actions
[numbered list — each: what, which file, who executes]

Confirm per number. A yes on item 1 does not cover item 2.
```

---

## Routing per finding type

| Finding | Route |
|---|---|
| AGENT.md references dead system | Nolan updates |
| Feedback rule missing from AGENT.md | Nolan updates after confirmation |
| CLAUDE.md drift | Larry self-edits after confirmation |
| SOP/GL dead reference | Larry proposes, edits after confirmation |
| active-context.md stale entry | Larry edits directly, no confirmation needed for factual cleanup |
| Skill file dead path | Kai fixes |

---

## What this skill is NOT

- Not a replacement for /close-session
- Not automated — owner-triggered only
- It does not execute fixes itself — it surfaces and proposes
