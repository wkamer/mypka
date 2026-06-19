#!/bin/bash
# Adds or replaces the Dropbox rclone token from /tmp/dropbox_token.txt.
# Usage: bash setup_token.sh

TOKEN_FILE=/tmp/dropbox_token.txt
RCLONE_CONF=/home/admin/.config/rclone/rclone.conf

if [ ! -f "$TOKEN_FILE" ]; then
    echo "Error: $TOKEN_FILE not found"
    exit 1
fi

TOKEN_JSON=$(python3 -c "
import json, re
content = open('$TOKEN_FILE').read()
match = re.search(r'\{.*?\}', content, re.DOTALL)
if match:
    json.loads(match.group(0))
    print(match.group(0))
else:
    raise ValueError('No valid JSON found in token file')
")

if [ $? -ne 0 ]; then
    echo "Error: could not extract valid JSON from $TOKEN_FILE"
    exit 1
fi

# Remove existing dropbox section if present
python3 -c "
import re
conf = open('$RCLONE_CONF').read()
conf = re.sub(r'\n\[dropbox\][^\[]*', '', conf)
open('$RCLONE_CONF', 'w').write(conf)
"

# Add new section
cat >> "$RCLONE_CONF" << EOF

[dropbox]
type = dropbox
token = $TOKEN_JSON
EOF

echo "Dropbox token updated. Testing connection..."
rclone lsd dropbox: && echo "Connection OK" || echo "Connection FAILED — check token"
