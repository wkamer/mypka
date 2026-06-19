#!/bin/bash
# PostToolUse hook — triggers on Write tool calls
# Notifies when a new GL/SOP/WS document is created

TOOL_DATA=$(cat)
FILE_PATH=$(echo "$TOOL_DATA" | python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    print(d.get('tool_input', {}).get('file_path', ''))
except:
    print('')
" 2>/dev/null)

if echo "$FILE_PATH" | grep -qE "(Guidelines/GL-|SOPs/SOP-|Workstreams/WS-)"; then
    FILENAME=$(basename "$FILE_PATH")
    echo "NIEUW DOCUMENT AANGEMAAKT: $FILENAME — Lees het terug en bevestig de inhoud aan de owner voor de sessie sluit."
fi
