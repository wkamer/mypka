---
description: Goal-first daily planning — 8 steps, PPM then BPM. Top-down: Goals → Projects → Tasks. One question at a time.
allowed-tools: Bash Read Edit mcp__plugin_context-mode_context-mode__ctx_batch_execute mcp__plugin_context-mode_context-mode__ctx_execute mcp__plugin_context-mode_context-mode__ctx_search
---

# /start-daily-planning

Execute directly. No preamble — just start.

**Target date:** parameter `tomorrow` → tomorrow | parameter `today` → today | no parameter → time-based: before 18:00 = today, from 18:00 = tomorrow. Never ask.

Report: `Start Daily Planning`

**Flow:** Complete PPM (Steps 1–4) fully, then BPM (Steps 5–8).
**One question at a time.** Show result → wait for input → next step. Never auto-chain.
**"Continue" is always valid** — no changes, move directly to the next step.

**Architecture:** all data processing and formatting happens in Python scripts. Claude runs the script, captures the full stdout, and places it **verbatim as its own text** in the response — never as tool output. Bash tool output is not visible to the owner; only Claude's text renders as markdown.

```
SCRIPTS="/opt/myPKA/Team Knowledge/Core/Integrations/todoist/Scripts"
TARGET=$([ $(date +%H) -ge 18 ] && date -d tomorrow +%Y-%m-%d || date +%Y-%m-%d)
```

---

## Step 0 — Fetch data

```bash
python3 "/opt/myPKA/Team Knowledge/Core/Integrations/todoist/Scripts/dp_fetch.py"
```

Caches: `/tmp/dp_completed.json`, `/tmp/dp_open.json`, `/tmp/dp_projects.json`.
Reuse in Step 5 — no new API call.

---

## Step 1 — Review (PPM)

**Input:** /tmp/dp_completed.json + /tmp/dp_open.json + /tmp/dp_projects.json

```bash
python3 "/opt/myPKA/Team Knowledge/Core/Integrations/todoist/Scripts/dp_step1.py" \
  --domain ppm --target $TARGET
```

**Output:** 3 sections × 3 tiers. Show full output. Wait for answer.

**Processing:**

| Action | Effect |
|---|---|
| Keep | No change |
| Backlog | Remove due date + remove planning labels + remove `committed` label |
| Reschedule | Set new due date + remove `committed` label |
| Postpone | Shift due date to target + add `postponed` label (never remove) + remove `committed` label |
| Complete | Close task + remove `committed` label |
| Delete | Delete task + remove `committed` label |

**Rule:** all actions except Keep remove the `committed` label. A new commit comes exclusively via Step 3 (Plan).

STOP. Wait for answer.

---

## Step 2 — Goals / Project Alignment (PPM)

**Input:** /tmp/dp_projects.json + local goal.md and project.md files

```bash
python3 "/opt/myPKA/Team Knowledge/Core/Integrations/todoist/Scripts/dp_step2.py" \
  --domain ppm --target $TARGET
```

**Output:** Goals / Projects - Event-driven / Projects - Other tables.
**Side-effect:** writes /tmp/dp_goals.json (goal statuses for Step 3).

Show full output. Wait for answer.

Processing:
- Goal with movement → include as priority in Step 3
- Blocker given → update `Waiting on:` in goal.md
- Project without Type → classify first, then continue
- "None" / "Continue" → move to Step 3

STOP. Wait for answer.

---

## Step 3 — Plan (PPM)

**Input:** /tmp/dp_goals.json + /tmp/dp_projects.json + fresh API fetch (cached to /tmp/dp_plan.json)

```bash
python3 "/opt/myPKA/Team Knowledge/Core/Integrations/todoist/Scripts/dp_step3.py" \
  --domain ppm --target $TARGET
```

**Output:** 4 blocks — Highlight of the Day / Support Tasks / Buffer Tasks / Available to Plan.
Show full output.

If there is no Highlight (N=0): propose one task from the highest-priority available goal — add as `highlight` + due = target, then re-run `dp_step3.py --no-fetch`.

**Actions at the bottom of the overview:**
> **Actions: Backlog / Promote / Demote / Reschedule / Commit**

STOP. Wait for answer.

After each action: run Todoist API update, then run `dp_step3.py --no-fetch` to show updated overview.

**Iron label rule:** the `postponed` label is **never** removed — not by any action. On every label update: first fetch current labels, retain `postponed` if present, only adjust planning labels (`highlight`, `support`, `committed`).

**Promote / Demote — always one level:**

Hierarchy: Available to Plan ↔ Buffer Task ↔ Support Task ↔ Highlight of the Day (ceiling, no promote possible)

| Action | From → To | Effect |
|---|---|---|
| Backlog [#] | Buffer Task → Available to Plan | remove due date + remove `highlight`/`support`/`committed`; keep `postponed` |
| Promote [#] | Available to Plan → Buffer Task | due = target |
| Promote [#] | Buffer Task → Support Task | add `support` label + due = target |
| Promote [#] | Support Task → Highlight of the Day | add `highlight` label + due = target; remove previous `highlight` label first |
| Promote [#] | Highlight of the Day → ❌ | not possible — ceiling |
| Demote [#] | Highlight of the Day → Support Task | `highlight` → `support` label |
| Demote [#] | Support Task → Buffer Task | remove `support` label; keep due = target |
| Demote [#] | Buffer Task → Available to Plan | remove due date |
| Demote [#] | Available to Plan → ❌ | not possible — outside planning |
| Reschedule [#] [date] | Buffer Task / Available to Plan → Available to Plan | Set new future due date (> target); task appears in Av to Plan with new date |
| Commit | — | 1. Fetch current labels per task. 2. Add `committed` (keep `postponed`); set due = target on all buffer tasks (no planning label, due ≤ target). 3. Run `dp_step3.py` (fresh fetch). 4. Go to Step 4 |

**Capacity indicator — show after each section title with max:**
- `⭐ Highlight of the Day (X/1)` — X = number of tasks with `highlight` label
- `Support Tasks (X/3)` — X = number of tasks with `support` label
- Exceeded (X > max) → show ❗ — report "[N] too many, demote first"

---

## Step 4 — Commitment (PPM)

**Input:** /tmp/dp_plan.json + /tmp/dp_projects.json

```bash
python3 "/opt/myPKA/Team Knowledge/Core/Integrations/todoist/Scripts/dp_step3.py" \
  --domain ppm --target $TARGET --no-fetch --step 4 --subtitle Commitment
```

Show final PPM plan (Highlight + Support + Buffer). Hide Available to Plan.

> "Do you want to change anything?"

STOP. Wait for answer.

- Change wanted → back to Step 3 PPM
- Confirmed → start Step 5 (BPM)

---

## Step 5 — Review (BPM)

**Input:** reuse /tmp/dp_completed.json + /tmp/dp_open.json (no new fetch)

```bash
python3 "/opt/myPKA/Team Knowledge/Core/Integrations/todoist/Scripts/dp_step1.py" \
  --domain bpm --target $TARGET
```

STOP. Wait for answer.

---

## Step 6 — Goals / Project Alignment (BPM)

```bash
python3 "/opt/myPKA/Team Knowledge/Core/Integrations/todoist/Scripts/dp_step2.py" \
  --domain bpm --target $TARGET
```

STOP. Wait for answer.

---

## Step 7 — Plan (BPM)

```bash
python3 "/opt/myPKA/Team Knowledge/Core/Integrations/todoist/Scripts/dp_step3.py" \
  --domain bpm --target $TARGET
```

STOP per action. Wait for answer.

---

## Step 8 — Commitment (BPM + closing)

Show combined final plan PPM + BPM (Highlight + Support + Buffer per domain).

> "Do you want to change anything?"

STOP. Wait for answer.

- Change wanted → back to Step 7 BPM
- Confirmed → closing

**Closing:**
> "Plan is set. Tomorrow you start with ⭐ [PPM Highlight]."

---

## Data fetch strategy

| Step | Script | API call |
|---|---|---|
| Step 0 | dp_fetch.py | ✓ completed + open + projects |
| Step 1 PPM | dp_step1.py --domain ppm | none |
| Step 2 PPM | dp_step2.py --domain ppm | lazy per goal (parallel) |
| Step 3 PPM | dp_step3.py --domain ppm | ✓ fresh open tasks → dp_plan.json |
| Step 5 BPM | dp_step1.py --domain bpm | none (reuse cache) |
| Step 6 BPM | dp_step2.py --domain bpm | lazy per goal (parallel) |
| Step 7 BPM | dp_step3.py --domain bpm | none (--no-fetch, reuse dp_plan.json) |

Never fetch the same data twice.

---

## Behavioral rules

- **Never auto-chain** — every step waits for owner response before the next starts
- **"Continue" always valid** — no changes, move directly to next step
- **Run scripts, don't think** — Claude does not generate tables itself; always run the script
- **Output always as own text** — place stdout of each script verbatim in Claude's text; no preamble, no "here is the output", first character of the response = first character of the script output
- **After Promote/Demote** — update Todoist first, then `--no-fetch` re-render
- **PPM before BPM** — Step 4 fully closed before Step 5 starts
- **SSOT project type = `project.md`** — never Todoist
- **AI facilitates, owner decides** — propose, never impose
