#!/usr/bin/env python3
"""dp_fetch.py — Step 0: fetch Todoist data and cache to /tmp/."""
import sys, os, json, urllib.request
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from todoist_helper import get_token
from dp_config import TODOIST_API

TOKEN = get_token()
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def fetch_list(url: str) -> list:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read())
    if isinstance(data, list):
        return data
    return data.get('results', data.get('items', []))


def main():
    # Since yesterday 22:00 UTC = local midnight NL (UTC+2)
    since = (datetime.now(timezone.utc) - timedelta(days=1)).replace(
        hour=22, minute=0, second=0, microsecond=0
    ).strftime('%Y-%m-%dT%H:%M:%SZ')

    completed = fetch_list(f"{TODOIST_API}/tasks/completed?since={since}&limit=200")
    with open('/tmp/dp_completed.json', 'w') as f:
        json.dump(completed, f)

    open_tasks = fetch_list(f"{TODOIST_API}/tasks?limit=200")
    with open('/tmp/dp_open.json', 'w') as f:
        json.dump(open_tasks, f)

    # Cache task_id → labels for completed task label lookup in Step 1
    label_cache = {str(t['id']): t.get('labels', []) for t in open_tasks}
    with open('/tmp/dp_task_labels.json', 'w') as f:
        json.dump(label_cache, f)

    req = urllib.request.Request(f"{TODOIST_API}/projects", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        raw = json.loads(r.read())
    projects = raw if isinstance(raw, list) else raw.get('results', [])
    with open('/tmp/dp_projects.json', 'w') as f:
        json.dump(projects, f)

    print(f"✓ {len(completed)} completed, {len(open_tasks)} open, {len(projects)} projects cached.")


if __name__ == '__main__':
    main()
