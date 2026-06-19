"""
Usage: python session_open.py
Prints undated Todoist tasks (owner action needed) and last session logs.
Team-internal tasks (team_tasks) are not shown — background bookkeeping only.
"""
import sqlite3, os, urllib.request, urllib.parse, json, sys
from datetime import datetime, timezone
import sys as _sys, os as _os; _sys.path.insert(0, _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))); from todoist_helper import get_token
sys.stdout.reconfigure(encoding="utf-8")

TODOIST_TOKEN = get_token()
PROJECTS = {
    "Personal": "6cFcm2MpmHvc2F3H",
    "Business": "6fC99W283Jw2cjV2",
}

DBS = {
    "Core":               "C:/Users/wkame/myPKA/Team Knowledge/team-knowledge.db",
    "Personal":           "C:/Users/wkame/myPKA/PKM/personal.db",
    "Kamer E-commerce":   "C:/Users/wkame/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db",
    "Geldstroom Regie":   "C:/Users/wkame/myPKA/Team Knowledge/Geldstroom Regie/geldstroom-regie.db",
}

def todoist_tasks(project_id):
    url = f"https://api.todoist.com/api/v1/tasks?project_id={project_id}&limit=100"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TODOIST_TOKEN}"})
    try:
        res = urllib.request.urlopen(req, timeout=10)
        data = json.loads(res.read())
        return data.get("results", data) if isinstance(data, dict) else data
    except Exception as e:
        print(f"  [Todoist error: {e}]")
        return []

print("=== TAKEN ZONDER DATUM (actie nodig) ===")
any_tasks = False
for label, project_id in PROJECTS.items():
    tasks = todoist_tasks(project_id)
    undated = [t for t in tasks if not t.get("due")]
    for t in undated:
        priority = 5 - t.get("priority", 1)  # Todoist: 4=P1, 1=P4 → display as 1-4
        print(f"TASK|{label}|{t['id']}|{t['content']}|{priority}")
        any_tasks = True
if not any_tasks:
    print("Geen taken zonder datum.")

print("\n=== LAST SESSION LOGS ===")
for label, path in DBS.items():
    if not os.path.exists(path):
        print(f"{label}: db not found"); continue
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='session_logs'")
    if not c.fetchone():
        print(f"SESSION|{label}|no session_logs table"); conn.close(); continue
    c.execute("SELECT session_date, session_title FROM session_logs ORDER BY rowid DESC LIMIT 1")
    row = c.fetchone()
    print(f"SESSION|{label}|{row[0]}|{row[1]}" if row else f"SESSION|{label}|no log yet")
    conn.close()
