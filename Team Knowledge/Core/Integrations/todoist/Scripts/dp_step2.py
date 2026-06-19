#!/usr/bin/env python3
"""dp_step2.py — Step 2 Goals/Project Alignment: render goals and projects as markdown.
Writes /tmp/dp_goals.json for use by dp_step3.py.
"""
import sys, os, json, re, argparse, urllib.request
from datetime import date, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from todoist_helper import get_token
from dp_config import (
    TODOIST_API, get_domain_ids, fmt_deadline, NL_MONTHS,
    get_goals_dirs, get_projects_dirs,
)

TOKEN = get_token()
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def fetch_recent_completions(project_id: str, since: str) -> int:
    url = f"{TODOIST_API}/tasks/completed?project_id={project_id}&since={since}&limit=1"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        items = data if isinstance(data, list) else data.get('results', data.get('items', []))
        return len(items)
    except Exception:
        return 0


def parse_goal(path: str) -> dict:
    """Parse a goal.md file into a dict of key fields."""
    result = {'path': path, 'name': '', 'deadline': '', 'waiting_on': '',
              'status_field': '', 'project_link': ''}
    try:
        with open(path) as f:
            content = f.read()
    except Exception:
        return result
    result['name'] = os.path.basename(os.path.dirname(path))
    for key, field in [('deadline', 'Deadline'), ('waiting_on', 'Waiting on'),
                       ('status_field', 'Status'), ('project_link', 'Project')]:
        m = re.search(rf'\*\*{field}:\*\*[ \t]*([^\n]*)', content)
        val = m.group(1).strip() if m else ''
        # Strip wiki-link brackets
        val = re.sub(r'\[\[([^\]]+)\]\]', r'\1', val)
        result[key] = val
    return result


def parse_project(path: str) -> dict:
    result = {'path': path, 'name': '', 'type': '', 'goal': '', 'event': '',
              'deadline': '', 'status': ''}
    try:
        with open(path) as f:
            content = f.read()
    except Exception:
        return result
    result['name'] = os.path.basename(os.path.dirname(path))
    for key, field in [('type', 'Type'), ('goal', 'Goal'), ('event', 'Event'),
                       ('deadline', 'Deadline'), ('status', 'Status')]:
        m = re.search(rf'\*\*{field}:\*\*\s*([^\n]*)', content)
        val = m.group(1).strip() if m else ''
        val = re.sub(r'\[\[([^\]]+)\]\]', r'\1', val)
        result[key] = val
    return result


def determine_goal_status(goal: dict, project_id: str | None, today: date, three_ago: str) -> str:
    if goal['waiting_on']:
        return '⏳'
    if project_id is None:
        return '🔴'
    count = fetch_recent_completions(project_id, three_ago)
    if count == 0:
        return '🔴'
    deadline = goal.get('deadline', '').strip()
    if deadline:
        try:
            dl = date.fromisoformat(deadline)
            return '🟡' if (dl - today).days <= 14 else '🟢'
        except ValueError:
            pass
    return '🟡'


def build_name_to_id(projects: list) -> dict:
    result = {}
    for p in projects:
        name = p.get('name', '')
        result[name] = p['id']
        clean = name.lstrip('👤💼 ').strip()
        result[clean] = p['id']
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain', default='ppm', choices=['ppm', 'bpm'])
    parser.add_argument('--target', default=str(date.today()))
    args = parser.parse_args()
    today = date.fromisoformat(args.target)
    three_ago = (today - timedelta(days=3)).strftime('%Y-%m-%dT00:00:00Z')

    with open('/tmp/dp_projects.json') as f:
        raw = json.load(f)
    projects = raw if isinstance(raw, list) else raw.get('results', [])
    name_to_id = build_name_to_id(projects)

    goals_dirs = get_goals_dirs(args.domain)
    projects_dirs = get_projects_dirs(args.domain)

    # Collect project names in scope (for goal cross-domain filtering)
    domain_project_names = set()
    for projects_dir in projects_dirs:
        if os.path.isdir(projects_dir):
            for entry in os.scandir(projects_dir):
                if entry.is_dir() and entry.name != 'Archive':
                    domain_project_names.add(entry.name)

    # Load all goals across all goals dirs
    goal_records = []
    for goals_dir in goals_dirs:
        if not os.path.isdir(goals_dir):
            continue
        for entry in sorted(os.scandir(goals_dir), key=lambda e: e.name):
            gpath = os.path.join(entry.path, 'goal.md')
            if entry.is_dir() and os.path.exists(gpath):
                g = parse_goal(gpath)
                proj_name = g['project_link']
                if proj_name and proj_name not in domain_project_names:
                    continue
                prefix = '👤 ' if args.domain == 'ppm' else '💼 '
                g['project_id'] = (name_to_id.get(proj_name)
                                   or name_to_id.get(f'{prefix}{proj_name}'))
                goal_records.append(g)

    # Determine statuses in parallel (skip ⏳ goals — no API needed)
    def resolve(g):
        if g['waiting_on']:
            return g['name'], '⏳'
        return g['name'], determine_goal_status(g, g.get('project_id'), today, three_ago)

    statuses = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        futures = {ex.submit(resolve, g): g for g in goal_records}
        for fut in as_completed(futures):
            name, status = fut.result()
            statuses[name] = status

    for g in goal_records:
        g['status'] = statuses.get(g['name'], '🔴')

    # Load all projects across all projects dirs
    project_records = []
    for projects_dir in projects_dirs:
        if not os.path.isdir(projects_dir):
            continue
        for entry in sorted(os.scandir(projects_dir), key=lambda e: e.name):
            ppath = os.path.join(entry.path, 'project.md')
            if entry.is_dir() and os.path.exists(ppath) and entry.name != 'Archive':
                p = parse_project(ppath)
                prefix = '👤 ' if args.domain == 'ppm' else '💼 '
                p['todoist_id'] = (name_to_id.get(p['name'])
                                   or name_to_id.get(f'{prefix}{p["name"]}'))
                project_records.append(p)

    # Sort goals: deadline first (nearest), then by status order
    STATUS_ORDER = {'🔴': 0, '🟡': 1, '🟢': 2, '⏳': 3}

    def sort_key(g):
        dl = g.get('deadline', '').strip()
        try:
            days = (date.fromisoformat(dl) - today).days if dl else 9999
        except ValueError:
            days = 9999
        return (0 if days < 9999 else 1, days, STATUS_ORDER.get(g['status'], 9))

    goal_records.sort(key=sort_key)

    step_num = 2 if args.domain == 'ppm' else 6
    domain_label = args.domain.upper()
    lines = [f"## [Step {step_num}] Daily Planning - Goals & Projects Alignment ({domain_label})", '', '---', '', '**Goals**', '']

    # Map goal name → project record
    goal_to_proj = {}
    for p in project_records:
        g_link = p.get('goal', '')
        if g_link:
            goal_to_proj[g_link] = p

    STATUS_LABELS = {'🔴': '🔴 Stagnant', '🟡': '🟡 Active', '🟢': '🟢 On track', '⏳': '⏳ Waiting'}

    counter = 1
    goal_status_cache = {}
    lines += ['| # | Goal | Project | Status | Deadline | Description |',
              '|---|---|---|---|---|---|']
    for g in goal_records:
        proj_rec = goal_to_proj.get(g['name'])
        proj_name = proj_rec['name'] if proj_rec else '—'
        status = g['status']
        status_label = STATUS_LABELS.get(status, status)
        deadline = fmt_deadline(g['deadline'], today)
        desc = g['waiting_on'] if status == '⏳' else '—'
        lines.append(f"| {counter} | {g['name']} | {proj_name} | {status_label} | {deadline} | {desc} |")
        proj_id = g.get('project_id')
        if proj_id:
            goal_status_cache[proj_id] = status
        counter += 1

    lines.append('')

    # Event-driven projects — determine status via recent completions
    event_projs = [p for p in project_records if p.get('type', '').lower() == 'event-driven']

    def resolve_proj_status(p):
        pid = p.get('todoist_id')
        if not pid:
            return p['name'], '🔴'
        count = fetch_recent_completions(pid, three_ago)
        if count == 0:
            return p['name'], '🔴'
        event_str = p.get('event', '')
        # Extract date from event field (format: "Omschrijving — DD maand YYYY" or ISO)
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', event_str)
        if not date_match:
            # Try "17 juni 2026" pattern
            nl_map = {v: k for k, v in {1:'jan',2:'feb',3:'mrt',4:'apr',5:'mei',6:'jun',
                                         7:'jul',8:'aug',9:'sep',10:'okt',11:'nov',12:'dec'}.items()}
            dm = re.search(r'(\d{1,2})\s+(\w+)\s+(\d{4})', event_str)
            if dm:
                mn = nl_map.get(dm.group(2).lower()[:3])
                if mn:
                    date_match_str = f"{dm.group(3)}-{mn:02d}-{int(dm.group(1)):02d}"
                    try:
                        ev_date = date.fromisoformat(date_match_str)
                        return p['name'], '🟡' if (ev_date - today).days <= 14 else '🟢'
                    except ValueError:
                        pass
            return p['name'], '🟡'
        try:
            ev_date = date.fromisoformat(date_match.group(1))
            return p['name'], '🟡' if (ev_date - today).days <= 14 else '🟢'
        except ValueError:
            return p['name'], '🟡'

    proj_statuses = {}
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = {ex.submit(resolve_proj_status, p): p for p in event_projs}
        for fut in as_completed(futures):
            name, status = fut.result()
            proj_statuses[name] = status

    lines += ['**Projects - Event-driven**', '']
    if event_projs:
        lines += ['| # | Project | Event | Status | Deadline | Description |',
                  '|---|---|---|---|---|---|']
        for p in event_projs:
            status = proj_statuses.get(p['name'], '🔴')
            status_label = STATUS_LABELS.get(status, status)
            event = p.get('event', '—')
            # Parse event date for deadline display
            event_date_str = ''
            dm = re.search(r'(\d{1,2})\s+(\w+)\s+(\d{4})', event)
            nl_map = {v: k for k, v in {1:'jan',2:'feb',3:'mrt',4:'apr',5:'mei',6:'jun',
                                         7:'jul',8:'aug',9:'sep',10:'okt',11:'nov',12:'dec'}.items()}
            if dm:
                mn = nl_map.get(dm.group(2).lower()[:3])
                if mn:
                    event_date_str = f"{dm.group(3)}-{mn:02d}-{int(dm.group(1)):02d}"
            deadline = fmt_deadline(event_date_str, today)
            lines.append(f"| {counter} | {p['name']} | {event} | {status_label} | {deadline} | — |")
            counter += 1
    else:
        lines.append('*(none)*')
    lines.append('')

    # Projects - Other (no type or unknown)
    other_projs = [p for p in project_records
                   if p.get('type', '').lower() not in ('goal-driven', 'event-driven')]
    lines += ['**Projects - Other**', '']
    if other_projs:
        lines += ['| # | Project | Description |', '|---|---|---|']
        for p in other_projs:
            lines.append(f"| {counter} | ⚠️ {p['name']} | Onbekend type — classificeer eerst |")
            counter += 1
    else:
        lines.append('*(none)*')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('Which goal / project gets movement?')

    print('\n'.join(lines))

    # Write goal status cache for dp_step3.py
    with open('/tmp/dp_goals.json', 'w') as f:
        json.dump(goal_status_cache, f)


if __name__ == '__main__':
    main()
