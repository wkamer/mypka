import urllib.request, json
import sys as _sys, os as _os; _sys.path.insert(0, _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))); from todoist_helper import get_token

TOKEN = get_token()
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

# Tasks to move to backlog (remove due date)
TASKS = [
    ("6gV932Q69m3rMG9H", "Koop een ketonenmeter"),
    ("6gcMvGVm5PRCcv3j", "Doe les 90"),
]

for task_id, name in TASKS:
    # Check current state
    url = f"https://api.todoist.com/api/v1/tasks/{task_id}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    with urllib.request.urlopen(req, timeout=10) as r:
        t = json.loads(r.read())
    print(f"CURRENT {name}: due={t.get('due')}")

    # Remove due date using due_string
    data = json.dumps({"due_string": "no date"}).encode()
    req = urllib.request.Request(url, data=data, headers=HEADERS, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            result = json.loads(r.read())
        print(f"AFTER {name}: due={result.get('due')}")
    except Exception as e:
        print(f"ERROR {name}: {e}")
