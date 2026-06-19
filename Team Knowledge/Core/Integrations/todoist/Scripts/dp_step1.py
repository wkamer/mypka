#!/usr/bin/env python3
"""dp_step1.py — Step 1 Review: render planned/overdue/completed tasks as markdown."""
import sys, os, json, argparse
from datetime import date

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from dp_config import get_domain_ids, filter_tasks, RESOURCE_PREFIXES


def load(path: str) -> list:
    with open(path) as f:
        data = json.load(f)
    return data if isinstance(data, list) else data.get('results', data.get('items', []))


def bucket(tasks: list):
    hl, sup, buf = [], [], []
    for t in tasks:
        labels = t.get('labels', [])
        if 'highlight' in labels:
            hl.append(t)
        elif 'support' in labels:
            sup.append(t)
        else:
            buf.append(t)
    return hl, sup, buf


def render_tier(name: str, tasks: list, proj_names: dict, counter: list, is_hotd=False) -> list:
    star = '⭐ ' if is_hotd else ''
    lines = [f"{star}{name}"]
    if not tasks:
        lines.append('*(none)*')
        lines.append('')
        return lines
    lines += ['| # | Taak | Project |', '|---|---|---|']
    for t in tasks:
        n = counter[0]; counter[0] += 1
        labels = t.get('labels', [])
        content = t.get('content', '')
        proj = proj_names.get(t.get('project_id', ''), '—')
        pfx = '⭐ ' if 'highlight' in labels else ('⚡ ' if 'speedy' in labels else '')
        lines.append(f"| {n} | {pfx}{content} | {proj} |")
    lines.append('')
    return lines


def render_section(title: str, hl: list, sup: list, buf: list,
                   proj_names: dict, counter: list, actions: str | None) -> list:
    has_tasks = any([hl, sup, buf])
    lines = [f"**{title}**", '']
    lines += render_tier('Highlight of the Day', hl, proj_names, counter, is_hotd=True)
    lines += render_tier('Support Tasks', sup, proj_names, counter)
    lines += render_tier('Buffer Tasks', buf, proj_names, counter)
    if actions and has_tasks:
        lines.append(f"> **Actions: {actions}**")
        lines.append('')
    lines.append('---')
    lines.append('')
    return lines


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain', default='ppm', choices=['ppm', 'bpm'])
    parser.add_argument('--target', default=str(date.today()))
    args = parser.parse_args()
    target = args.target
    actual_today = str(date.today())

    with open('/tmp/dp_projects.json') as f:
        raw = json.load(f)
    projects = raw if isinstance(raw, list) else raw.get('results', [])

    domain_ids = get_domain_ids(projects, args.domain)
    proj_names = domain_ids

    completed_raw = load('/tmp/dp_completed.json')
    completed_ids = {str(t.get('task_id') or t.get('id', '')) for t in completed_raw}

    # Label cache: task_id → labels (completed API strips labels)
    label_cache = {}
    try:
        with open('/tmp/dp_task_labels.json') as f:
            label_cache = json.load(f)
    except Exception:
        pass

    open_tasks = filter_tasks(load('/tmp/dp_open.json'), set(domain_ids.keys()))

    overdue, today_open = [], []
    for t in open_tasks:
        due = t.get('due') or {}
        d = (due.get('date', '') or '')[:10]
        if not d:
            continue
        tid = str(t.get('id', ''))
        if d < actual_today:
            overdue.append(t)
        elif d == actual_today and tid not in completed_ids:
            today_open.append(t)

    today_completed = []
    for t in completed_raw:
        if t.get('project_id') not in domain_ids:
            continue
        if any(t.get('content', '').startswith(p) for p in RESOURCE_PREFIXES):
            continue
        tid = str(t.get('task_id') or t.get('id', ''))
        labels = t.get('labels') or label_cache.get(tid) or []
        if not labels:
            # Parse @labelname shortcuts from content as fallback
            import re as _re
            labels = _re.findall(r'@(\w+)', t.get('content', ''))
        if labels or not t.get('labels'):
            t = dict(t)
            t['labels'] = labels
            # Strip @label shortcuts from displayed content
            t['content'] = _re.sub(r'\s*@\w+', '', t['content']).strip()
        today_completed.append(t)

    step_num = 1 if args.domain == 'ppm' else 5
    domain_label = args.domain.upper()
    counter = [1]
    lines = [f"## [Step {step_num}] Daily Planning - Review ({domain_label})", '']

    hl, sup, buf = bucket(overdue)
    lines += render_section('Planned - Overdue', hl, sup, buf, proj_names, counter,
                            'Backlog / Reschedule / Complete / Delete')

    hl, sup, buf = bucket(today_open)
    lines += render_section('Planned Today - Open', hl, sup, buf, proj_names, counter,
                            'Keep / Backlog / Reschedule / Postpone / Complete / Delete')

    hl, sup, buf = bucket(today_completed)
    lines += render_section('Planned Today - Completed', hl, sup, buf, proj_names, counter,
                            actions=None)

    if any([overdue, today_open]):
        lines.append("What's your action for each task?")

    print('\n'.join(lines))


if __name__ == '__main__':
    main()
