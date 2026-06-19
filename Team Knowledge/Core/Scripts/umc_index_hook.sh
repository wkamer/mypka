#!/bin/bash
# PostToolUse hook — UMC auto-index for PKM files
# Triggers on Write and Edit tool calls. If the written file is under PKM/,
# indexes it into memory_knowledge via MemoryManager.
# Always exits 0 — never blocks agent flow.

TOOL_DATA=$(cat)

TOOL_NAME=$(echo "$TOOL_DATA" | /opt/mypka-memory/venv/bin/python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    print(d.get('tool_name', ''))
except:
    print('')
" 2>/dev/null)

# Only act on Write or Edit
if [[ "$TOOL_NAME" != "Write" && "$TOOL_NAME" != "Edit" ]]; then
    exit 0
fi

FILE_PATH=$(echo "$TOOL_DATA" | /opt/mypka-memory/venv/bin/python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    print(d.get('tool_input', {}).get('file_path', ''))
except:
    print('')
" 2>/dev/null)

# Only act on .md files inside PKM/
if [[ "$FILE_PATH" != *.md ]]; then
    exit 0
fi

if [[ "$FILE_PATH" != *"/PKM/"* && "$FILE_PATH" != /opt/myPKA/PKM/* ]]; then
    exit 0
fi

# Skip files larger than 50KB
if [ -f "$FILE_PATH" ]; then
    FILE_SIZE=$(stat -c%s "$FILE_PATH" 2>/dev/null || echo 0)
    if [ "$FILE_SIZE" -gt 51200 ]; then
        exit 0
    fi
else
    exit 0
fi

export UMC_INDEX_FILE_PATH="$FILE_PATH"

/opt/mypka-memory/venv/bin/python3 - <<'PYEOF' 2>/dev/null
import sys, os, re

sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
try:
    from memory_config import get_dsn
    os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
    from memory_manager import get_manager
    mm = get_manager()

    file_path = os.environ.get('UMC_INDEX_FILE_PATH', '')
    if not file_path:
        sys.exit(0)

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read().strip()

    if not content:
        sys.exit(0)

    # Relative path from MYPKA root
    rel_path = file_path.replace('/opt/myPKA/', '')

    # Determine source_type from path
    if '/CRM/WhatsApp/' in rel_path:
        source_type = 'whatsapp'
    elif '/Journal/' in rel_path:
        source_type = 'journal'
    elif '/CRM/People/' in rel_path or '/CRM/Organizations/' in rel_path:
        source_type = 'crm'
    elif '/My Life/Projects/' in rel_path:
        source_type = 'project'
    elif '/My Life/Topics/' in rel_path:
        source_type = 'topic'
    else:
        source_type = 'knowledge'

    # Determine domain
    if '/My Life/' in rel_path or '/CRM/' in rel_path or '/Journal/' in rel_path or '/Documents/' in rel_path:
        domain = 'personal'
    else:
        domain = 'core'

    # Extract date from filename if it starts with YYYYMMDD
    basename = os.path.basename(file_path)
    date_ref = None
    m = re.match(r'^(\d{4})(\d{2})(\d{2})', basename)
    if m:
        date_ref = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"

    mm.write_knowledge(domain, rel_path, content, chunk_index=0,
                       date_ref=date_ref, source_type=source_type)

except Exception:
    pass
PYEOF

exit 0
