#!/bin/bash
# SessionStart hook — injects recent UMC summary pointers into session context.

/opt/mypka-memory/venv/bin/python - <<'EOF'
import sys, os
sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
try:
    from memory_config import get_dsn
    os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
    from memory_manager import get_manager
    mm = get_manager()
    output = mm.get_summary_pointers(limit=3)
    if output and output.strip():
        print(output)
except Exception:
    sys.exit(0)
EOF
