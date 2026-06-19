#!/bin/bash
# PostToolUse hook — UMC auto-offload
# Reads tool output from stdin. If > 2000 chars: offloads via MemoryManager
# and writes a compact reference to stdout. Always exits 0 — never blocks agent flow.

TOOL_DATA=$(cat)

# Extract tool name from the hook payload
TOOL_NAME=$(echo "$TOOL_DATA" | /opt/mypka-memory/venv/bin/python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    print(d.get('tool_name', 'unknown'))
except:
    print('unknown')
" 2>/dev/null)

# Extract tool output from the hook payload
# Claude Code PostToolUse payload: {"tool_name": "...", "tool_input": {...}, "tool_response": {"type": "tool_result", "content": [{"type": "text", "text": "..."}]}}
TOOL_OUTPUT=$(echo "$TOOL_DATA" | /opt/mypka-memory/venv/bin/python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    r = d.get('tool_response', {})
    # Handle string response
    if isinstance(r, str):
        print(r)
    elif isinstance(r, dict):
        # Standard format: content is a list of content blocks
        content = r.get('content', '') or r.get('output', '') or r.get('result', '')
        if isinstance(content, list):
            parts = []
            for item in content:
                if isinstance(item, dict):
                    parts.append(item.get('text', ''))
                else:
                    parts.append(str(item))
            print('\n'.join(parts))
        else:
            print(str(content))
    else:
        print(str(r))
except Exception as e:
    print('')
" 2>/dev/null)

OUTPUT_LEN=${#TOOL_OUTPUT}

if [ "$OUTPUT_LEN" -gt 2000 ]; then
    # Offload via MemoryManager
    SESSION_ID=$(date +"%Y-%m-%d-hook")

    # Export env vars BEFORE the Python subprocess reads them
    export UMC_TOOL_NAME="$TOOL_NAME"
    export UMC_SESSION_ID="$SESSION_ID"
    export UMC_OUTPUT="$TOOL_OUTPUT"

    REF=$(/opt/mypka-memory/venv/bin/python3 - <<'PYEOF' 2>/dev/null
import sys, os

sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
try:
    from memory_config import get_dsn
    os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
    from memory_manager import get_manager
    mm = get_manager()

    tool_name = os.environ.get('UMC_TOOL_NAME', 'unknown')
    session_id = os.environ.get('UMC_SESSION_ID', 'unknown')
    output = os.environ.get('UMC_OUTPUT', '')

    ref = mm.write_tool_log(session_id, "hook", tool_name, {}, output)
    print(f"[UMC] Offloaded {len(output)} chars from '{tool_name}' → ref={ref}")
except Exception as e:
    print(f"[UMC] Offload skipped: {e}")
PYEOF
)

    if [ -n "$REF" ]; then
        echo "$REF"
    fi
fi

exit 0
