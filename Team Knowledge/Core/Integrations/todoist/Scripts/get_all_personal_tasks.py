import urllib.request, json
from datetime import date
import sys as _sys, os as _os; _sys.path.insert(0, _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))); from todoist_helper import get_token

TOKEN = get_token()
today = str(date.today())

# Get all projects first
url = "https://api.todoist.com/api/v1/projects?limit=100"
req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
with urllib.request.urlopen(req, timeout=10) as r:
    data = json.loads(r.read())
projects = data.get("results", data) if isinstance(data, dict) else data

print("=== ALL PROJECTS ===")
for p in projects:
    print(f"{p['id']}|{p['name']}")

print("\n=== HIGHLIGHT TASKS ===")
for p in projects:
    url = f"https://api.todoist.com/api/v1/tasks?project_id={p['id']}&limit=100"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        tasks = data.get("results", data) if isinstance(data, dict) else data
        for t in tasks:
            labels = t.get("labels", [])
            if "highlight" in labels:
                due = (t.get("due") or {})
                print(f"{p['name']}|{t['id']}|{t['content']}|{due.get('date','no date')}")
    except Exception as e:
        print(f"ERROR {p['name']}: {e}")
