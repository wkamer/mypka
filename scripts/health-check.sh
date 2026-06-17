#!/usr/bin/env bash

DB="/opt/myPKA/Team Knowledge/team-knowledge.db"
EXPECTED_TABLES=("session_logs" "team_tasks" "team_log" "agent_learnings")
DISK_THRESHOLD=80
EXIT=0

pass() { echo "PASS  $1"; }
fail() { echo "FAIL  $1"; EXIT=1; }

# Check 1: DB reachable + expected tables present
check_db() {
    if [ ! -f "$DB" ]; then
        fail "DB not found: $DB"
        return
    fi
    missing=()
    for table in "${EXPECTED_TABLES[@]}"; do
        result=$(python3 - "$DB" "$table" <<'EOF'
import sqlite3, sys
conn = sqlite3.connect(sys.argv[1])
row = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (sys.argv[2],)).fetchone()
print("yes" if row else "no")
EOF
)
        [ "$result" != "yes" ] && missing+=("$table")
    done
    if [ ${#missing[@]} -eq 0 ]; then
        pass "team-knowledge.db reachable, all expected tables present"
    else
        fail "team-knowledge.db missing tables: ${missing[*]}"
    fi
}

# Check 2: Root disk usage under 80%
check_disk() {
    usage=$(df / | awk 'NR==2 {gsub(/%/,"",$5); print $5}')
    if [ "$usage" -lt "$DISK_THRESHOLD" ]; then
        pass "Disk usage ${usage}% (threshold: ${DISK_THRESHOLD}%)"
    else
        fail "Disk usage ${usage}% exceeds ${DISK_THRESHOLD}% threshold"
    fi
}

# Check 3: Docker running (required by n8n, Postgres, Ollama)
check_docker_running() {
    docker_state=$(systemctl is-active docker 2>&1)
    docker_status=$?
    if [ "$docker_status" -eq 0 ]; then
        pass "Docker running (expected)"
    elif [ "$docker_state" = "inactive" ] || [ "$docker_state" = "failed" ]; then
        fail "Docker not running (n8n, Postgres, Ollama depend on it)"
    else
        fail "Unable to determine Docker state: $docker_state"
    fi
}

check_db
check_disk
check_docker_running

exit $EXIT
