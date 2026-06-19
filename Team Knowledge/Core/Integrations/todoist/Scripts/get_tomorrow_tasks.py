import urllib.request, json
import sys as _sys, os as _os; _sys.path.insert(0, _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))); from todoist_helper import get_token

TOKEN = get_token()
tomorrow = "2026-05-18"

url = "https://api.todoist.com/api/v1/projects?limit=100"
req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
with urllib.request.urlopen(req, timeout=10) as r:
    data = json.loads(r.read())
projects = data.get("results", data) if isinstance(data, dict) else data

proj_map = {p["id"]: p["name"] for p in projects}

for p in projects:
    url = f"https://api.todoist.com/api/v1/tasks?project_id={p['id']}&limit=100"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        tasks = data.get("results", data) if isinstance(data, dict) else data
        for t in tasks:
            due = t.get("due") or {}
            due_date = (due.get("date", "") or "")[:10]
            if due_date == tomorrow:
                labels = t.get("labels", [])
                hl = "⭐" if "highlight" in labels else "  "
                print(f"{hl}|{p['name']}|{t['id']}|{t['content']}")
    except Exception as e:
        print(f"ERROR {p['name']}: {e}")
