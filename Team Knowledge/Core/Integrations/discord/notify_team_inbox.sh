#!/bin/bash
# SSOT for Team Inbox Discord notifications.
# Usage: notify_team_inbox.sh <source> <filepath>

WEBHOOK="http://localhost:5678/webhook/team-inbox"
SOURCE="$1"
FILEPATH="$2"

payload=$(python3 -c "
import json, sys
from datetime import datetime, timezone
source   = sys.argv[1]
location = sys.argv[2]
print(json.dumps({
    'discord_payload': {
        'embeds': [{
            'color': 5763719,
            'fields': [
                {'name': 'Source',  'value': source,             'inline': True},
                {'name': 'Status',  'value': 'Uploaded',         'inline': True},
                {'name': 'Subject', 'value': 'Team Inbox',       'inline': False},
                {'name': 'Message', 'value': f'location: {location}', 'inline': False}
            ],
            'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        }]
    }
}))
" "$SOURCE" "$FILEPATH")

curl -s -X POST "$WEBHOOK" \
    -H "Content-Type: application/json" \
    -d "$payload" \
    > /dev/null
