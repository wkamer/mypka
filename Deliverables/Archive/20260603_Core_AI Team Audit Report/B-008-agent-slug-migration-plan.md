# B-008 — agent_slug Migration Plan

**Date:** 2026-06-03
**Author:** Kai
**Scope:** Add missing `agent_slug` column to `session_logs` in personal.db and kamer-ecommerce.db

---

## 1. Current Situation

| Database | Path | session_logs rows | agent_slug column |
|---|---|---|---|
| personal.db | `/opt/myPKA/PKM/personal.db` | 55 | MISSING |
| kamer-ecommerce.db | `/opt/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db` | 9 | MISSING |
| team-knowledge.db | `/opt/myPKA/Team Knowledge/team-knowledge.db` | — | PRESENT (already migrated) |
| geldstroom-regie.db | `/opt/myPKA/Team Knowledge/Geldstroom Regie/geldstroom-regie.db` | — | PRESENT (already migrated) |

Column definition in databases that have it (reference, from team-knowledge.db):

```sql
agent_slug TEXT
```

No NOT NULL constraint, no default value — nullable, added via ALTER TABLE.

---

## 2. Exact SQL per Database

### personal.db

```sql
-- Step 1: verify current state (run first, confirm before proceeding)
SELECT name FROM pragma_table_info('session_logs') WHERE name = 'agent_slug';
-- Expected output: 0 rows (column absent)

-- Step 2: add column
ALTER TABLE session_logs ADD COLUMN agent_slug TEXT;

-- Step 3: verify
SELECT name FROM pragma_table_info('session_logs') WHERE name = 'agent_slug';
-- Expected output: 1 row — agent_slug
```

### kamer-ecommerce.db

```sql
-- Step 1: verify current state
SELECT name FROM pragma_table_info('session_logs') WHERE name = 'agent_slug';
-- Expected output: 0 rows

-- Step 2: add column
ALTER TABLE session_logs ADD COLUMN agent_slug TEXT;

-- Step 3: verify
SELECT name FROM pragma_table_info('session_logs') WHERE name = 'agent_slug';
-- Expected output: 1 row — agent_slug
```

### Python execution block (use /opt/mypka-memory/venv/bin/python)

```python
import sqlite3

migrations = [
    ("/opt/myPKA/PKM/personal.db",                                                "personal.db"),
    ("/opt/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db",            "kamer-ecommerce.db"),
]

for path, name in migrations:
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    # Pre-check: column must not exist yet
    cur.execute("SELECT name FROM pragma_table_info('session_logs') WHERE name='agent_slug'")
    if cur.fetchone():
        print(f"{name}: agent_slug already exists — skipping")
        conn.close()
        continue

    cur.execute("ALTER TABLE session_logs ADD COLUMN agent_slug TEXT")
    conn.commit()

    # Post-check
    cur.execute("SELECT name FROM pragma_table_info('session_logs') WHERE name='agent_slug'")
    result = cur.fetchone()
    print(f"{name}: {'OK — agent_slug added' if result else 'FAIL — column not found after ALTER'}")
    conn.close()
```

---

## 3. Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| ALTER TABLE locks the database briefly | Low | Low | SQLite ALTER TABLE on a nullable column with no default is near-instant; no table rebuild required |
| Existing rows get NULL for agent_slug | Certain | Acceptable | Correct behavior — historical rows have no agent context; fill on next write |
| Wrong database path used | Low | Medium | Use the Python block above — paths hardcoded from schema audit |
| Migration runs twice | Low | None | Pre-check in Python block prevents double-execution |
| Backup missing at time of migration | Low | High | See section 4 |

SQLite ALTER TABLE adding a nullable column without a default does NOT rebuild the table in SQLite 3.37+. Risk of data loss is minimal. Still: backup first.

---

## 4. Backup Check

Before executing, verify that a backup from today or the previous day exists:

```bash
ls -la /home/admin/backups/sqlite/
# Must show a YYYYMMDD/ folder for today or yesterday

ls /home/admin/backups/sqlite/$(date +%Y%m%d)/
# Must contain:
#   personal.db
#   kamer-ecommerce.db
```

If the SQLite backup cron (02:30 daily, added by B-001) has not run yet on the day of migration: run the backup script manually first:

```bash
/bin/bash "/opt/myPKA/Team Knowledge/Core/Scripts/backup_sqlite_dbs.sh"
```

The backup from the rclone local-backup (02:00 daily via `/home/admin/.config/rclone/local-backup.sh`) also covers these files via rsync of `/opt/myPKA/`. Check:

```bash
ls /home/admin/backups/myPKA/$(date +%Y%m%d)/PKM/personal.db
ls "/home/admin/backups/myPKA/$(date +%Y%m%d)/Team Knowledge/Kamer E-commerce/kamer e-commerce.db"
```

Either source is sufficient. Do not proceed without a verified backup.

---

## 5. Rollback Plan

SQLite does not support `ALTER TABLE DROP COLUMN` in versions below 3.35, and even in 3.35+ it requires a full table rebuild.

The rollback strategy is: restore from backup. Not a schema reversal.

```bash
# Rollback personal.db
cp /home/admin/backups/sqlite/YYYYMMDD/personal.db \
   /opt/myPKA/PKM/personal.db

# Rollback kamer-ecommerce.db
cp "/home/admin/backups/sqlite/YYYYMMDD/kamer-ecommerce.db" \
   "/opt/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db"
```

Replace YYYYMMDD with the actual backup date. Stop any active agent sessions before restoring.

---

## 6. Test Steps

1. **Pre-migration verification**
   Run the Step 1 queries above. Confirm 0 rows returned (column absent). If 1 row returned, migration already done — stop.

2. **Backup verification**
   Confirm backup exists as described in section 4.

3. **Execute migration**
   Run the Python block from section 2. Read the output — both databases must print "OK — agent_slug added".

4. **Post-migration schema check**
   ```python
   import sqlite3
   for path, name in [
       ("/opt/myPKA/PKM/personal.db", "personal"),
       ("/opt/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db", "kamer-ecommerce"),
   ]:
       conn = sqlite3.connect(path)
       cur = conn.cursor()
       cur.execute("PRAGMA table_info(session_logs)")
       cols = [row[1] for row in cur.fetchall()]
       print(f"{name}: {cols}")
       assert "agent_slug" in cols, f"FAIL: agent_slug missing in {name}"
       conn.close()
   print("All OK")
   ```

5. **Write test**
   Insert a test row with agent_slug populated, confirm it persists, then delete:
   ```python
   import sqlite3, datetime
   conn = sqlite3.connect("/opt/myPKA/PKM/personal.db")
   cur = conn.cursor()
   cur.execute(
       "INSERT INTO session_logs (session_date, session_title, agent_slug) VALUES (?, ?, ?)",
       (datetime.date.today().isoformat(), "B-008 migration test", "kai")
   )
   conn.commit()
   cur.execute("SELECT id, session_title, agent_slug FROM session_logs ORDER BY id DESC LIMIT 1")
   print(cur.fetchone())
   # Verify output shows ("B-008 migration test", "kai")
   cur.execute("DELETE FROM session_logs WHERE session_title = 'B-008 migration test'")
   conn.commit()
   conn.close()
   ```

6. **Existing data integrity check**
   Confirm existing rows are untouched:
   ```python
   import sqlite3
   conn = sqlite3.connect("/opt/myPKA/PKM/personal.db")
   cur = conn.cursor()
   cur.execute("SELECT COUNT(*) FROM session_logs")
   print(cur.fetchone())  # Must still be 55
   cur.execute("SELECT COUNT(*) FROM session_logs WHERE agent_slug IS NOT NULL")
   print(cur.fetchone())  # Must be 0 (all historical rows have NULL — correct)
   conn.close()
   ```

---

Delivered on: 2026-06-03
Delivered at: Kai — B-008 migration plan
