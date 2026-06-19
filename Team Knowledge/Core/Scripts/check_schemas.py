import sqlite3

conn = sqlite3.connect("C:/Users/wkame/myPKA/PKM/personal.db")
cur = conn.cursor()
cur.execute("PRAGMA table_info(session_logs)")
print("personal session_logs:", [r[1] for r in cur.fetchall()])
conn.close()

conn = sqlite3.connect("C:/Users/wkame/myPKA/Team Knowledge/team-knowledge.db")
cur = conn.cursor()
cur.execute("PRAGMA table_info(agent_learnings)")
print("agent_learnings:", [r[1] for r in cur.fetchall()])
cur.execute("PRAGMA table_info(delegation_outcomes)")
print("delegation_outcomes:", [r[1] for r in cur.fetchall()])
cur.execute("PRAGMA table_info(team_log)")
print("team_log:", [r[1] for r in cur.fetchall()])
conn.close()
