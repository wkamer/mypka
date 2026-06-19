import urllib.request, json
import sys as _sys, os as _os; _sys.path.insert(0, _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))); from todoist_helper import get_token

TOKEN = get_token()
PROJECTS = {
    "Personal": "6cFcm2MpmHvc2F3H",
    "Personal-Projects": "6c8XR7HXhgMWMWwj",
}

for label, pid in PROJECTS.items():
    url = f"https://api.todoist.com/api/v1/tasks?project_id={pid}&limit=200"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        tasks = data.get("results", data) if isinstance(data, dict) else data
        for t in tasks:
            labels = t.get("labels", [])
            content = t["content"]
            if "highlight" in labels or "88" in content or "les" in content.lower() or "miracle" in content.lower():
                due = (t.get("due") or {})
                print(f"{label}|{t['id']}|{content}|{due.get('date','no date')}|{labels}")
    except Exception as e:
        print(f"ERROR {label}: {e}")
