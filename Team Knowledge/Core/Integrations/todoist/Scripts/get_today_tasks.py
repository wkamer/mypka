import urllib.request, json
from datetime import date
import sys as _sys, os as _os; _sys.path.insert(0, _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))); from todoist_helper import get_token

TOKEN = get_token()
today = str(date.today())
PROJECTS = {
    "Personal": "6cFcm2MpmHvc2F3H",
    "Kamer E-commerce": "6fC99W283Jw2cjV2",
    "Geldstroom Regie": "6gfFMpHcMCQvPQpc",
}

for label, pid in PROJECTS.items():
    url = f"https://api.todoist.com/api/v1/tasks?project_id={pid}&limit=100"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        tasks = data.get("results", data) if isinstance(data, dict) else data
        for t in tasks:
            due = t.get("due") or {}
            due_date = (due.get("date", "") or "")[:10]
            if due_date and due_date <= today:
                labels = t.get("labels", [])
                hl = "highlight" if "highlight" in labels else ""
                print(f"{label}|{t['id']}|{t['content']}|{due_date}|{hl}")
    except Exception as e:
        print(f"ERROR {label}: {e}")
