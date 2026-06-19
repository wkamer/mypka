#!/usr/bin/env python3
"""dp_step3.py — Step 3 Plan: render 4-block plan view as markdown.
Fetches fresh open tasks → caches to /tmp/dp_plan.json.
Reads /tmp/dp_goals.json for goal-status filter.
"""
import sys, os, json, argparse, urllib.request
from datetime import date

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from todoist_helper import get_token
from dp_config import TODOIST_API, get_domain_ids, filter_tasks, get_projects_dirs, NL_MONTHS

TOKEN = get_token()
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

ACTIVE_STATUSES = {'🔴', '🟡'}  # goals whose tasks appear in Available to Plan


def fetch_open_tasks() -> list:
    req = urllib.request.Request(f"{TODOIST_API}/tasks?limit=200", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read())
    tasks = data if isinstance(data, list) else data.get('results', data.get('items', []))
    with open('/tmp/dp_plan.json', 'w') as f:
        json.dump(tasks, f)
    return tasks


def fmt_do_date(due_date: str) -> str:
    if not due_date:
        return '—'
    try:
        d = date.fromisoformat(due_date)
        return f"{d.day} {NL_MONTHS[d.month]}"
    except ValueError:
        return due_date


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain', default='ppm', choices=['ppm', 'bpm'])
    parser.add_argument('--target', default=str(date.today()))
    parser.add_argument('--no-fetch', action='store_true',
                        help='Use cached /tmp/dp_plan.json instead of fetching')
    parser.add_argument('--step', type=int, default=None,
                        help='Override step number in title')
    parser.add_argument('--subtitle', default=None,
                        help='Override subtitle (default: Plan)')
    args = parser.parse_args()
    today = args.target

    # Projects
    with open('/tmp/dp_projects.json') as f:
        raw = json.load(f)
    projects = raw if isinstance(raw, list) else raw.get('results', [])

    domain_ids = get_domain_ids(projects, args.domain)
    proj_names = domain_ids

    # Goal status cache (project_id → status)
    goal_statuses = {}
    if os.path.exists('/tmp/dp_goals.json'):
        with open('/tmp/dp_goals.json') as f:
            goal_statuses = json.load(f)

    # Build project_id → goal name mapping
    import re
    proj_to_goal = {}
    for projects_dir in get_projects_dirs(args.domain):
        if not os.path.isdir(projects_dir):
            continue
        for entry in os.scandir(projects_dir):
            ppath = os.path.join(entry.path, 'project.md')
            if entry.is_dir() and os.path.exists(ppath):
                try:
                    with open(ppath) as f:
                        content = f.read()
                    m = re.search(r'\*\*Goal:\*\*\s*([^\n]*)', content)
                    if m:
                        goal_name = re.sub(r'\[\[([^\]]+)\]\]', r'\1', m.group(1)).strip()
                        proj_name = entry.name
                        for pid, pname in proj_names.items():
                            if proj_name in pname or pname.endswith(proj_name):
                                proj_to_goal[pid] = goal_name
                                break
                except Exception:
                    pass

    # Fetch or load plan tasks
    if args.no_fetch and os.path.exists('/tmp/dp_plan.json'):
        with open('/tmp/dp_plan.json') as f:
            raw_tasks = json.load(f)
        tasks = raw_tasks if isinstance(raw_tasks, list) else raw_tasks.get('results', [])
    else:
        tasks = fetch_open_tasks()

    domain_tasks = filter_tasks(tasks, set(domain_ids.keys()))

    highlight, support, buffer_tasks, available = [], [], [], []

    for t in domain_tasks:
        labels = t.get('labels', [])
        due = t.get('due') or {}
        due_date = (due.get('date', '') or '')[:10]
        pid = t.get('project_id', '')

        if 'highlight' in labels and (not due_date or due_date <= today):
            highlight.append(t)
        elif 'support' in labels and (not due_date or due_date <= today):
            support.append(t)
        elif due_date and due_date <= today:
            buffer_tasks.append(t)
        else:
            # Available to Plan filter: goal-status driven
            goal_status = goal_statuses.get(pid)
            has_movement = bool(goal_status and '⚡' in goal_status)
            base_status = goal_status.replace('⚡', '').strip() if goal_status else None
            if has_movement or base_status in ACTIVE_STATUSES or goal_status is None:
                available.append(t)
            # ⏳ / 🟢 without movement → skip

    n_hl = len(highlight)
    n_sup = len(support)
    hl_indicator = f"({n_hl}/1)" + (' ❗' if n_hl > 1 else '')
    sup_indicator = f"({n_sup}/3)" + (' ❗' if n_sup > 3 else '')

    default_step = 3 if args.domain == 'ppm' else 7
    step_num = args.step if args.step is not None else default_step
    subtitle = args.subtitle if args.subtitle else 'Plan'
    domain_label = args.domain.upper()
    lines = [f"## [Step {step_num}] Daily Planning - {subtitle} ({domain_label})", '']
    counter = [1]  # continuous numbering across all blocks

    def row(t):
        n = counter[0]; counter[0] += 1
        labels = t.get('labels', [])
        content = t.get('content', '')
        pid = t.get('project_id', '')
        proj = proj_names.get(pid, '—')
        goal = proj_to_goal.get(pid, '—')
        pfx = '⭐ ' if 'highlight' in labels else ('⚡ ' if 'speedy' in labels else '')
        sfx = ' ↩' if 'postponed' in labels else ''
        due = t.get('due') or {}
        due_date = (due.get('date', '') or '')[:10]
        return f"| {n} | {pfx}{content}{sfx} | {proj} | {goal} | {fmt_do_date(due_date)} |"

    HDR = ['| # | Taak | Project | Goal | Do Date |', '|---|---|---|---|---|']
    NONE_ROW = '| — | *(none)* | — | — | — |'

    # Block 1: Highlight of the Day
    lines.append(f"⭐ Highlight of the Day {hl_indicator}")
    lines.append('')
    lines += HDR
    if highlight:
        for t in highlight:
            lines.append(row(t))
    else:
        lines.append(NONE_ROW)
    lines.append('')

    # Block 2: Support Tasks
    lines.append(f"Support Tasks {sup_indicator}")
    lines.append('')
    lines += HDR
    if support:
        for t in support:
            lines.append(row(t))
    else:
        lines.append(NONE_ROW)
    lines.append('')

    # Block 3: Buffer Tasks
    lines.append('Buffer Tasks')
    lines.append('')
    lines += HDR
    if buffer_tasks:
        for t in buffer_tasks:
            lines.append(row(t))
    else:
        lines.append(NONE_ROW)
    lines.append('')

    # Block 4: Available to Plan — no due date first, future due date at bottom
    available.sort(key=lambda t: (bool((t.get('due') or {}).get('date')),
                                  (t.get('due') or {}).get('date') or ''))
    lines.append('Available to Plan')
    lines.append('')
    lines += HDR
    if available:
        for t in available:
            lines.append(row(t))
    else:
        lines.append(NONE_ROW)
    lines.append('')

    lines.append('> **Actions: Backlog / Promote / Demote / Reschedule / Commit**')

    print('\n'.join(lines))


if __name__ == '__main__':
    main()
