#!/bin/bash
# backup_n8n.sh — Daily pg_dump backup for the n8n-postgres container.
#
# Schedule : 02:45 daily via crontab
# Target   : /home/admin/backups/n8n/YYYYMMDD_n8n-postgres.sql
# Retention: 7 dumps
#
# Method   : docker exec on n8n-postgres container using its own env vars.
#             Safe to run while n8n is live — PostgreSQL handles concurrent reads.
#             The existing /opt/n8n/backup-n8n.sh continues to run at 03:00 as-is;
#             this script is the myPKA-managed backup targeting /home/admin/backups/.

set -euo pipefail

BACKUP_DIR="/home/admin/backups/n8n"
TIMESTAMP=$(date +%Y%m%d)
BACKUP_FILE="${BACKUP_DIR}/${TIMESTAMP}_n8n-postgres.sql"
LOG_FILE="/opt/myPKA/Team Knowledge/Core/Integrations/n8n/logs/backup_n8n.log"
RETAIN_DAYS=7

mkdir -p "$BACKUP_DIR"
mkdir -p "$(dirname "$LOG_FILE")"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting n8n-postgres backup" | tee -a "$LOG_FILE"

# Verify container is running before attempting backup
if ! docker ps --format '{{.Names}}' | grep -q '^n8n-postgres$'; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: n8n-postgres container is not running — skipping backup" | tee -a "$LOG_FILE"
    exit 1
fi

# pg_dump via docker exec — credentials from container environment
docker exec n8n-postgres \
    sh -c 'PGPASSWORD="$POSTGRES_PASSWORD" pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB" --format=plain' \
    > "$BACKUP_FILE"

DUMP_SIZE=$(du -sh "$BACKUP_FILE" | cut -f1)
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Backup created: $BACKUP_FILE ($DUMP_SIZE)" | tee -a "$LOG_FILE"

# Retention: remove dumps older than RETAIN_DAYS
REMOVED=$(find "$BACKUP_DIR" -maxdepth 1 -type f -name '*_n8n-postgres.sql' -mtime +"$RETAIN_DAYS" -print)
if [[ -n "$REMOVED" ]]; then
    find "$BACKUP_DIR" -maxdepth 1 -type f -name '*_n8n-postgres.sql' -mtime +"$RETAIN_DAYS" -delete
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Removed old dumps:" | tee -a "$LOG_FILE"
    echo "$REMOVED" | tee -a "$LOG_FILE"
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Done." | tee -a "$LOG_FILE"
