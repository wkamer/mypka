#!/usr/bin/env python3
"""dp_status.py — Day status: committed plan (label-based) + live completion check."""
import sys, os, json, argparse, urllib.request
from datetime import date, datetime, timezone, timedelta

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from todoist_helper import get_token
from dp_config import TODOIST_API, get_domain_ids, filter_tasks, NL_MONTHS

TOKEN = get_token()
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

PLANNING_LABELS = {'highlight', 'support', 'committed'}


def fmt_do_date(due_date: str) -> str:
    if not due_date:
        return '—'
    try:
        d = date.fromisoformat(due_date)
        return f"{d.day} {NL_MONTHS[d.month]}"
    except ValueError:
        return due_date


def fetch_completed_ids() -> set:
    since = (datetime.now(timezone.utc) - timedelta(days=1)).replace(
        hour=22, minute=0, second=0, microsecond=0
    ).strftime('%Y-%m-%dT%H:%M:%SZ')
    req = urllib.request.Request(
        f"{TODOIST_API}/tasks/completed?since={since}&limit=200",
        headers=HEADERS
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read())
    tasks = data if isinstance(data, list) else data.get('results', data.get('items', []))
    return {str(t.get('task_id') or t.get('id', '')) for t in tasks}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain', default='ppm', choices=['ppm', 'bpm'])
    parser.add_argument('--target', default=str(date.today()))
    args = parser.parse_args()
    target = args.target

    if not os.path.exists('/tmp/dp_plan.json'):
        print("⚠️ Geen plan gevonden — voer eerst Step 3 uit.")
        return

    with open('/tmp/dp_projects.json') as f:
        raw = json.load(f)
    projects = raw if isinstance(raw, list) else raw.get('results', [])
    domain_ids = get_domain_ids(projects, args.domain)
    proj_names = domain_ids

    with open('/tmp/dp_plan.json') as f:
        raw_tasks = json.load(f)
    tasks = raw_tasks if isinstance(raw_tasks, list) else raw_tasks.get('results', [])
    domain_tasks = filter_tasks(tasks, set(domain_ids.keys()))

    completed_ids = fetch_completed_ids()

    highlight, support, buffer_tasks = [], [], []
    for t in domain_tasks:
        labels = set(t.get('labels', []))
        if not labels & PLANNING_LABELS:
            continue
        due = t.get('due') or {}
        due_date = (due.get('date', '') or '')[:10]
        if due_date != target:
            continue
        if 'highlight' in labels:
            highlight.append(t)
        elif 'support' in labels:
            support.append(t)
        else:
            buffer_tasks.append(t)

    def done(t) -> str:
        return '✅' if str(t.get('id', '')) in completed_ids else '—'

    def pfx(t) -> str:
        labels = t.get('labels', [])
        if 'highlight' in labels: return '⭐ '
        if 'speedy' in labels: return '⚡ '
        return ''

    def sfx(t) -> str:
        return ' ↩' if 'postponed' in t.get('labels', []) else ''

    HDR = '| # | Taak | Project | Do Date | |'
    SEP = '|---|---|---|---|---|'
    NONE = '| — | *(none)* | — | — | — |'

    lines = []
    counter = [1]

    def row(t):
        n = counter[0]; counter[0] += 1
        content = t.get('content', '')
        pid = t.get('project_id', '')
        proj = proj_names.get(pid, '—')
        due = t.get('due') or {}
        due_date = (due.get('date', '') or '')[:10]
        return f"| {n} | {pfx(t)}{content}{sfx(t)} | {proj} | {fmt_do_date(due_date)} | {done(t)} |"

    all_committed = highlight + support + buffer_tasks
    if not all_committed:
        print(f"⚠️ Geen committed taken gevonden voor {fmt_do_date(target)} — is Step 4 al afgerond?")
        return

    total = len(all_committed)
    n_done = sum(1 for t in all_committed if str(t.get('id', '')) in completed_ids)

    lines.append(f"**Dagstatus — {fmt_do_date(target)} ({n_done}/{total} afgerond)**")
    lines.append('')

    lines.append('⭐ Highlight of the Day')
    lines.append('')
    lines.append(HDR)
    lines.append(SEP)
    for t in highlight: lines.append(row(t))
    if not highlight: lines.append(NONE)
    lines.append('')

    lines.append('Support Tasks')
    lines.append('')
    lines.append(HDR)
    lines.append(SEP)
    for t in support: lines.append(row(t))
    if not support: lines.append(NONE)
    lines.append('')

    lines.append('Buffer Tasks')
    lines.append('')
    lines.append(HDR)
    lines.append(SEP)
    for t in buffer_tasks: lines.append(row(t))
    if not buffer_tasks: lines.append(NONE)

    print('\n'.join(lines))


if __name__ == '__main__':
    main()
