"""
Usage: python delete_task.py <db> <task_id> [task_id2 ...]
  db:      core | personal | business
  task_id: one or more task IDs to permanently delete
"""
import sqlite3, sys

DBS = {
    "core":     "C:/Users/wkame/myPKA/Team Knowledge/team-knowledge.db",
    "personal": "C:/Users/wkame/myPKA/PKM/personal.db",
    "business": "C:/Users/wkame/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db",
}

if len(sys.argv) < 3:
    print("Usage: delete_task.py <db> <task_id> [task_id2 ...]"); sys.exit(1)

db_key = sys.argv[1].lower()
if db_key not in DBS:
    print(f"Unknown db '{db_key}'. Use: core | personal | business"); sys.exit(1)

task_ids = sys.argv[2:]
placeholders = ",".join("?" * len(task_ids))

conn = sqlite3.connect(DBS[db_key])
c = conn.cursor()
c.execute(f"DELETE FROM team_tasks WHERE id IN ({placeholders})", task_ids)
conn.commit()
print(f"Deleted {c.rowcount} task(s): {', '.join(f'#{t}' for t in task_ids)}")
conn.close()
