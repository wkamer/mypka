"""
Usage: python update_task.py <db> <task_id> <field>=<value> [field2=value2 ...]
  db:      core | personal | business
  task_id: ID of the task to update
  fields:  any combination of:
             title=<text>
             assignee=<slug|none>
             priority=<1-4>
             status=<open|completed>
             tags=<comma-separated>
             due_date=<YYYY-MM-DD>

Examples:
  python update_task.py personal 3 priority=1 assignee=sienna
  python update_task.py business 7 status=open tags=urgent,review
  python update_task.py core 2 title="New title here"
"""
import sqlite3, sys

DBS = {
    "core":       "C:/Users/wkame/myPKA/Team Knowledge/team-knowledge.db",
    "personal":   "C:/Users/wkame/myPKA/PKM/personal.db",
    "business":   "C:/Users/wkame/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db",
    "geldstroom": "C:/Users/wkame/myPKA/Team Knowledge/Geldstroom Regie/geldstroom-regie.db",
}

ALLOWED_FIELDS = {"title", "assignee", "priority", "status", "tags", "due_date"}

if len(sys.argv) < 4:
    print("Usage: update_task.py <db> <task_id> <field>=<value> [...]"); sys.exit(1)

db_key  = sys.argv[1].lower()
task_id = sys.argv[2]
updates = sys.argv[3:]

if db_key not in DBS:
    print(f"Unknown db '{db_key}'. Use: core | personal | business | geldstroom"); sys.exit(1)

fields, values = [], []
for update in updates:
    if "=" not in update:
        print(f"Invalid format '{update}' — use field=value"); sys.exit(1)
    field, value = update.split("=", 1)
    if field not in ALLOWED_FIELDS:
        print(f"Unknown field '{field}'. Allowed: {', '.join(sorted(ALLOWED_FIELDS))}"); sys.exit(1)
    fields.append(f"{field}=?")
    values.append(None if value.lower() == "none" else value)

values.append(task_id)
sql = f"UPDATE team_tasks SET {', '.join(fields)} WHERE id=?"

conn = sqlite3.connect(DBS[db_key])
c = conn.cursor()
c.execute(sql, values)
conn.commit()
if c.rowcount:
    print(f"Updated task #{task_id} in {db_key}: {', '.join(updates)}")
else:
    print(f"No task found with id={task_id} in {db_key}")
conn.close()
