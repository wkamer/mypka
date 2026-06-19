import os
import sys
import uuid
import urllib.request
import urllib.parse
import json
import sys as _sys, os as _os; _sys.path.insert(0, _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))); from todoist_helper import get_token

# Usage: python archive_project.py <project_id>

def archive_project(project_id):
    token = get_token()
    if not token:
        sys.exit(1)

    payload = json.dumps({
        "commands": [
            {
                "type": "project_archive",
                "uuid": str(uuid.uuid4()),
                "args": {"id": project_id}
            }
        ]
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.todoist.com/api/v1/sync",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())

    status = result.get("sync_status", {}).get(list(result.get("sync_status", {}).keys())[0]) if result.get("sync_status") else result
    print(f"Archived project {project_id}: {status}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python archive_project.py <project_id>")
        sys.exit(1)
    archive_project(sys.argv[1])
