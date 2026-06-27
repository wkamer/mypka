#!/bin/bash
# backup_sqlite_dbs.sh — Daily crash-safe backup for the 4 myPKA SQLite databases.
#
# Schedule : 02:30 daily via crontab (before rclone sync at */5 and before memory-db dump at 03:00)
# Method   : python3 sqlite3.connect().backup() — equivalent to sqlite3 ".backup" command;
#             crash-safe, works without sqlite3 CLI binary.
# Target   : /home/admin/backups/sqlite/YYYYMMDD/<db-name>.db
# Retention: 7 date-sets (older ones removed automatically)
#
# Databases backed up:
#   personal.db         /opt/myPKA/PKM/personal.db
#   team-knowledge.db   /opt/myPKA/Team Knowledge/team-knowledge.db
#   kamer-ecommerce.db  /opt/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db
#   geldstroom-regie.db /opt/myPKA/Team Knowledge/Geldstroom Regie/geldstroom-regie.db

set -euo pipefail

BACKUP_ROOT="/home/admin/backups/sqlite"
DATESTAMP=$(date +%Y%m%d)
BACKUP_DIR="${BACKUP_ROOT}/${DATESTAMP}"
LOG_FILE="/opt/myPKA/Team Knowledge/Core/Scripts/backup_sqlite_dbs.log"
RETAIN_DAYS=7

mkdir -p "$BACKUP_DIR"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting SQLite backups to $BACKUP_DIR" | tee -a "$LOG_FILE"

# ---------------------------------------------------------------------------
# Perform backups via Python sqlite3 module (crash-safe, no CLI dependency)
# ---------------------------------------------------------------------------
python3 - <<'PYTHON'
import sqlite3, os, sys

log_file = "/opt/myPKA/Team Knowledge/Core/Scripts/backup_sqlite_dbs.log"
datestamp = os.environ.get("DATESTAMP", __import__("datetime").date.today().strftime("%Y%m%d"))
backup_dir = f"/home/admin/backups/sqlite/{datestamp}"

databases = [
    ("/opt/myPKA/PKM/personal.db",                                                    "personal.db"),
    ("/opt/myPKA/Team Knowledge/team-knowledge.db",                                   "team-knowledge.db"),
    ("/opt/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db",                "kamer-ecommerce.db"),
    ("/opt/myPKA/Team Knowledge/Geldstroom Regie/geldstroom-regie.db",                "geldstroom-regie.db"),
    ("/opt/myPKA/apps/dashboard/email-management.db",                                   "email-management.db"),
]

def log(msg):
    from datetime import datetime
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line)
    with open(log_file, "a") as fh:
        fh.write(line + "\n")

all_ok = True
for src_path, dest_name in databases:
    dest_path = os.path.join(backup_dir, dest_name)
    try:
        src = sqlite3.connect(src_path)
        dst = sqlite3.connect(dest_path)
        src.backup(dst)
        dst.close()
        src.close()
        size = os.path.getsize(dest_path)
        log(f"OK  {dest_name}  ({size // 1024} KB) -> {dest_path}")
    except Exception as e:
        log(f"FAIL {dest_name}: {e}")
        all_ok = False

sys.exit(0 if all_ok else 1)
PYTHON

# ---------------------------------------------------------------------------
# Retention: remove date-sets older than RETAIN_DAYS
# ---------------------------------------------------------------------------
REMOVED=$(find "$BACKUP_ROOT" -maxdepth 1 -type d -name '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]' -mtime +"$RETAIN_DAYS" -print)
if [[ -n "$REMOVED" ]]; then
    find "$BACKUP_ROOT" -maxdepth 1 -type d -name '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]' -mtime +"$RETAIN_DAYS" -exec rm -rf {} +
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Removed old sets:" | tee -a "$LOG_FILE"
    echo "$REMOVED" | tee -a "$LOG_FILE"
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] SQLite backup complete." | tee -a "$LOG_FILE"
