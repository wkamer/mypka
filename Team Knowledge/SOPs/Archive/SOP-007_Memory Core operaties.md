# SOP-007: Memory Core operaties

**Eigenaar:** Kai — Infrastructure & Integration Architect
**Service:** memory-db (PostgreSQL 16 + pgvector)
**Locatie:** `/opt/myPKA/Team Knowledge/Core/Integrations/memory-db/`
**Aangemaakt:** 2026-05-20

---

## 1. Eerste opstart (go-live)

### Stap 1 — .env aanmaken

```bash
cd "/opt/myPKA/Team Knowledge/Core/Integrations/memory-db"
cp .env.template .env
nano .env   # vul MEMORY_DB_USER, MEMORY_DB_PASSWORD, MEMORY_DB_NAME, MEMORY_DB_DSN in
```

Wachtwoord-eisen: minimaal 20 tekens, alfanumeriek + symbolen. Sla op in Bitwarden.

### Stap 2 — Port conflict check

n8n-postgres luistert op poort 5432 (intern, niet gepubliceerd op host). memory-db hoeft geen host-port te publiceren tenzij je er direct vanaf de host verbinding mee wilt maken. Voor scripts op de host: voeg een port-mapping toe aan docker-compose.yml:

```yaml
ports:
  - "5433:5432"
```

Daarna DSN in .env aanpassen: `postgresql://user:pass@localhost:5433/mypka_memory`

### Stap 3 — Container starten

```bash
cd "/opt/myPKA/Team Knowledge/Core/Integrations/memory-db"
docker compose --env-file .env up -d
```

### Stap 4 — Initialisatie verifiëren

```bash
docker logs memory-db 2>&1 | tail -20
# Verwacht: "database system is ready to accept connections"

docker exec memory-db psql -U $MEMORY_DB_USER -d $MEMORY_DB_NAME -c "\dt"
# Verwacht: tool_logs en memory_summaries
```

### Stap 5 — Python dependencies installeren

```bash
/opt/n8n/venv/bin/pip install psycopg2-binary pgvector sentence-transformers
# Of in de project venv:
pip install psycopg2-binary pgvector sentence-transformers
```

### Stap 6 — Client testen

```bash
export MEMORY_DB_DSN="postgresql://user:pass@localhost:5433/mypka_memory"
python3 - <<'EOF'
from memory_client import log_tool_output
row_id = log_tool_output(
    session_id="test-session",
    agent_slug="kai",
    tool_name="smoke-test",
    tool_args={"test": True},
    output="Smoke test output",
)
print(f"Inserted row id: {row_id}")
EOF
```

Verwacht: `Inserted row id: 1`

---

## 2. Dagelijkse operaties

### Container status controleren

```bash
docker ps --filter name=memory-db
docker stats memory-db --no-stream
```

### Logs bekijken

```bash
docker logs memory-db --tail 50
```

### Verbinding testen

```bash
docker exec memory-db psql -U $MEMORY_DB_USER -d $MEMORY_DB_NAME -c "SELECT count(*) FROM tool_logs;"
```

---

## 3. Stoppen en herstarten

```bash
# Graceful stop
docker compose -f "/opt/myPKA/Team Knowledge/Core/Integrations/memory-db/docker-compose.yml" stop memory-db

# Herstart
docker compose -f "/opt/myPKA/Team Knowledge/Core/Integrations/memory-db/docker-compose.yml" start memory-db

# Volledige recreate (na config-wijziging)
docker compose --env-file .env up -d --force-recreate memory-db
```

---

## 4. Backup

### Manuele backup

```bash
BACKUP_DIR="/opt/myPKA/backups/memory-db"
mkdir -p "$BACKUP_DIR"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

docker exec memory-db pg_dump \
  -U $MEMORY_DB_USER \
  -d $MEMORY_DB_NAME \
  --format=custom \
  > "$BACKUP_DIR/memory_db_$TIMESTAMP.dump"
```

### Restore from backup

```bash
docker exec -i memory-db pg_restore \
  -U $MEMORY_DB_USER \
  -d $MEMORY_DB_NAME \
  --clean \
  < /path/to/memory_db_TIMESTAMP.dump
```

### Verificatie na restore

```bash
docker exec memory-db psql -U $MEMORY_DB_USER -d $MEMORY_DB_NAME \
  -c "SELECT count(*) FROM tool_logs; SELECT count(*) FROM memory_summaries;"
```

---

## 5. Problemen oplossen

### Symptoom: Container start niet op

**Diagnose:**
```bash
docker logs memory-db 2>&1 | head -50
```

Veelvoorkomende oorzaken:
- `.env` niet ingevuld of niet aanwezig
- Port 5433 al in gebruik: `ss -tlnp | grep 5433`
- Volume corrupt: zie sectie 6

### Symptoom: `MEMORY_DB_DSN is not set`

De omgevingsvariabele is niet beschikbaar in de shell die het script uitvoert.

```bash
export MEMORY_DB_DSN="postgresql://user:pass@localhost:5433/mypka_memory"
```

Of voeg toe aan `/etc/environment` of de venv activate-script.

### Symptoom: `pgvector extension not found`

De init.sql heeft niet gedraaid. Dit kan als het volume al bestond voor de eerste start.

```bash
docker exec memory-db psql -U $MEMORY_DB_USER -d $MEMORY_DB_NAME \
  -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

### Symptoom: Embedding duurt erg lang (eerste run)

Normaal gedrag. `all-MiniLM-L6-v2` (~90 MB) wordt gedownload en geladen bij eerste gebruik. Daarna gecached in geheugen.

### Symptoom: `sentence-transformers not installed`

Valt terug op opslaan zonder embedding (embedding = NULL). Installeer:

```bash
pip install sentence-transformers
```

---

## 6. Volume herstel na crash

Als het data-volume corrupt is:

```bash
# Stop container
docker compose stop memory-db

# Verwijder corrupt volume (DATA VERLIES — alleen als backup beschikbaar is)
docker volume rm memory_db_data

# Herbouw en herstel
docker compose --env-file .env up -d memory-db
# Wacht op healthy status
docker restore (zie sectie 4)
```

---

## 7. Schema-uitbreiding (Fase 2+)

Alle schema-wijzigingen via migration scripts in `memory-db/migrations/`:

```bash
docker exec -i memory-db psql -U $MEMORY_DB_USER -d $MEMORY_DB_NAME < migrations/V002_add_column.sql
```

Nooit schema direct aanpassen op draaiende container zonder migratiescript.

---

## Referenties

- Architectuurbeslissing: `[[GL-013_Memory Core Architecture]]`
- ADR: `[[ADR-002_Memory-Core-pgvector]]`
- Docker Compose: `Team Knowledge/Core/Integrations/memory-db/docker-compose.yml`
- Client: `Team Knowledge/Core/Scripts/memory_client.py`
