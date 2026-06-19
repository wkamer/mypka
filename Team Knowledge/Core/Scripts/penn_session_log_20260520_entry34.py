"""
Penn session log — journal entry 34 — 2026-05-20
"""
import sqlite3
import sys
sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Scripts')

try:
    from db_helper import team_db
    db_path = team_db
except ImportError:
    db_path = '/opt/myPKA/Team Knowledge/team-knowledge.db'

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Check what columns exist
cols = [c[1] for c in conn.execute('PRAGMA table_info(session_logs)').fetchall()]
print("Columns:", cols)

summary = (
    "Penn verwerkte de vierde journaalentry van 2026-05-20 over de scheiding. "
    "Walter reageert op Wendy's bericht (10:19) waarin ze mediation afwees en zei dat ze hem hoort. "
    "Walter maakt een scherp onderscheid: Wendy framt duidelijkheid over het ouderschapsplan als zijn behoefte; "
    "voor Walter is het een noodzaak — twee kinderen, verantwoordelijkheid moet vastliggen. "
    "Hij kiest er bewust voor zijn reactie nog niet te sturen. "
    "Entry 34 gelinkt aan entries 31, 32, 33 en P-Scheiding. "
    "Reflecties: bewust onderscheid behoefte/noodzaak, patroon doorbreken door niet direct te sturen."
)

insert_fields = {
    'session_date': '2026-05-20',
    'agent_slug': 'penn',
    'session_title': 'Journal entry 34 — Wendy: behoefte vs noodzaak',
    'summary': summary,
    'topics': 'scheiding,wendy,ouderschapsplan,noodzaak',
    'decisions': 'Walter stuurt zijn reactie nog niet; kiest bewust voor bezinning over taal.',
    'actions_taken': 'Journal entry 34 aangemaakt en gelogd in personal.db (id=34).',
    'open_items': 'Hoe formuleert Walter het onderscheid behoefte/noodzaak zonder nieuwe discussie over taal?',
}

# Only insert fields that exist in the table
row = {k: v for k, v in insert_fields.items() if k in cols}
placeholders = ', '.join(['?' for _ in row])
keys = ', '.join(row.keys())
cur.execute(f'INSERT INTO session_logs ({keys}) VALUES ({placeholders})', list(row.values()))
conn.commit()
new_id = cur.lastrowid
print(f'Inserted session_log id: {new_id}')
conn.close()
