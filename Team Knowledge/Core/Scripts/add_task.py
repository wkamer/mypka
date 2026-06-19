"""
Usage: python add_task.py <db> <title> <assignee> <priority> <source> [tags]
  db:       core | personal | business
  title:    task title (quote if contains spaces)
  assignee: specialist slug or "none"
  priority: 1=urgent 2=high 3=normal 4=low
  source:   delegation | sweep | manual
  tags:     optional comma-separated tags
"""
import sqlite3, sys

DBS = {
    "core":       "C:/Users/wkame/myPKA/Team Knowledge/team-knowledge.db",
    "personal":   "C:/Users/wkame/myPKA/PKM/personal.db",
    "business":   "C:/Users/wkame/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db",
    "geldstroom": "C:/Users/wkame/myPKA/Team Knowledge/Geldstroom Regie/geldstroom-regie.db",
}

if len(sys.argv) < 6:
    print("Usage: add_task.py <db> <title> <assignee> <priority> <source> [tags]"); sys.exit(1)

db_key   = sys.argv[1].lower()
title    = sys.argv[2]
assignee = None if sys.argv[3].lower() == "none" else sys.argv[3]
priority = int(sys.argv[4])
source   = sys.argv[5]
tags     = sys.argv[6] if len(sys.argv) > 6 else None

if db_key not in DBS:
    print(f"Unknown db '{db_key}'. Use: core | personal | business | geldstroom"); sys.exit(1)

conn = sqlite3.connect(DBS[db_key])
c = conn.cursor()
c.execute(
    "INSERT INTO team_tasks (title, assignee, priority, source, tags, status, created_at) VALUES (?,?,?,?,?,'open',datetime('now'))",
    (title, assignee, priority, source, tags)
)
conn.commit()
print(f"Added task #{c.lastrowid} in {db_key}: {title}")
conn.close()
