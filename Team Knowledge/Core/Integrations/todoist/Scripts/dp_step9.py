#!/usr/bin/env python3
"""dp_step9.py — Step 9: Combined committed planning overview PPM + BPM."""
import sys, os, json, argparse
from datetime import date

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from dp_config import get_domain_ids, filter_tasks, NL_MONTHS


def fmt_do_date(due_date: str) -> str:
    if not due_date:
        return '—'
    try:
        d = date.fromisoformat(due_date)
        return f"{d.day} {NL_MONTHS[d.month]}"
    except ValueError:
        return due_date


def render_domain(domain: str, tasks: list, proj_names: dict, target: str, counter: list) -> list:
    HDR = ['| # | Taak | Project | Do Date |', '|---|---|---|---|']
    NONE_ROW = '| — | *(none)* | — | — |'

    domain_label = domain.upper()
    lines = [f"**{domain_label}**", '']

    highlight, support, buffer_tasks = [], [], []
    for t in tasks:
        labels = t.get('labels', [])
        due = (t.get('due') or {}).get('date', '') or ''
        due_date = due[:10]
        if 'highlight' in labels:
            highlight.append(t)
        elif 'support' in labels:
            support.append(t)
        elif due_date and due_date <= target:
            buffer_tasks.append(t)

    def row(t):
        n = counter[0]; counter[0] += 1
        labels = t.get('labels', [])
        content = t.get('content', '')
        proj = proj_names.get(t.get('project_id', ''), '—')
        pfx = '⭐ ' if 'highlight' in labels else ('⚡ ' if 'speedy' in labels else '')
        sfx = ' ↩' if 'postponed' in labels else ''
        due = (t.get('due') or {}).get('date', '') or ''
        return f"| {n} | {pfx}{content}{sfx} | {proj} | {fmt_do_date(due[:10])} |"

    n_hl = len(highlight)
    n_sup = len(support)
    hl_ind = f"({n_hl}/1)" + (' ❗' if n_hl > 1 else '')
    sup_ind = f"({n_sup}/3)" + (' ❗' if n_sup > 3 else '')

    lines += [f"⭐ Highlight of the Day {hl_ind}", '', *HDR]
    lines += [row(t) for t in highlight] if highlight else [NONE_ROW]
    lines.append('')

    lines += [f"Support Tasks {sup_ind}", '', *HDR]
    lines += [row(t) for t in support] if support else [NONE_ROW]
    lines.append('')

    lines += ['Buffer Tasks', '', *HDR]
    lines += [row(t) for t in buffer_tasks] if buffer_tasks else [NONE_ROW]
    lines.append('')

    return lines


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', default=str(date.today()))
    args = parser.parse_args()
    target = args.target

    with open('/tmp/dp_plan.json') as f:
        raw = json.load(f)
    all_tasks = raw if isinstance(raw, list) else raw.get('results', [])

    with open('/tmp/dp_projects.json') as f:
        raw = json.load(f)
    projects = raw if isinstance(raw, list) else raw.get('results', [])

    lines = ['## [Step 9] Daily Planning - Committed Planning (PPM & BPM)', '']
    counter = [1]

    for domain in ('ppm', 'bpm'):
        domain_ids = get_domain_ids(projects, domain)
        domain_tasks = filter_tasks(all_tasks, set(domain_ids.keys()))
        lines += render_domain(domain, domain_tasks, domain_ids, target, counter)
        lines += ['---', '']

    lines.append('Plan is set.')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
