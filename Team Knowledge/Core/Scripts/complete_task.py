"""
Usage: python complete_task.py <db> <id> [id2 id3 ...]

db aliases: core | personal | business | geldstroom
Or pass a full path to the .db file.
"""
import sqlite3, sys
from datetime import datetime

DB_ALIASES = {
    "core":       "C:/Users/wkame/myPKA/Team Knowledge/team-knowledge.db",
    "personal":   "C:/Users/wkame/myPKA/PKM/personal.db",
    "business":   "C:/Users/wkame/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db",
    "geldstroom": "C:/Users/wkame/myPKA/Team Knowledge/Geldstroom Regie/geldstroom-regie.db",
}

if len(sys.argv) < 3:
    print("Usage: complete_task.py <db> <id> [id2 id3 ...]")
    sys.exit(1)

db = DB_ALIASES.get(sys.argv[1].lower(), sys.argv[1])
ids = [int(x) for x in sys.argv[2:]]

conn = sqlite3.connect(db)
cur = conn.cursor()
for task_id in ids:
    cur.execute(
        "UPDATE team_tasks SET status='completed', completed_at=datetime('now') WHERE id=?",
        (task_id,)
    )
    print(f"Task {task_id}: {'completed' if cur.rowcount else 'not found'}")
conn.commit()
conn.close()
