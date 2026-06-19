"""
Usage: python todoist_rename_section.py <section_id> <new_name>
Renames a Todoist section by ID.
"""
import urllib.request, json, sys
import sys as _sys, os as _os; _sys.path.insert(0, _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))); from todoist_helper import get_token

TOKEN = get_token()
HDRS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

if len(sys.argv) < 3:
    print("Usage: todoist_rename_section.py <section_id> <new_name>")
    sys.exit(1)

section_id = sys.argv[1]
new_name = sys.argv[2]

req = urllib.request.Request(
    f"https://api.todoist.com/api/v1/sections/{section_id}",
    data=json.dumps({"name": new_name}).encode(),
    headers=HDRS,
    method="POST"
)
with urllib.request.urlopen(req, timeout=10) as r:
    result = json.loads(r.read())
    print(f"renamed: {result['name']} (id={result['id']})")
