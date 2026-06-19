#!/bin/bash
# Watches /opt/myPKA/Team Inbox/ for directly placed files and notifies n8n Team workflow via webhook.
# Source is always "Direct" — integrations that copy files into Team Inbox send their own notifications.
# Skips: Recorded Audio/ (handled by Dropbox integration), hidden files, rclone partial files.

INBOX="/opt/myPKA/Team Inbox/"
NOTIFY="/opt/myPKA/Team Knowledge/Core/Integrations/discord/notify_team_inbox.sh"

inotifywait -m -r -e create --format '%w%f' "$INBOX" | while read -r filepath; do
    filename=$(basename "$filepath")

    # Skip hidden files (markers) and rclone partial files
    [[ "$filename" == .* ]] && continue
    [[ "$filename" == *.partial ]] && continue

    # Skip subfolders managed by integrations
    [[ "$filepath" == *"/Recorded Audio/"* ]] && continue

    bash "$NOTIFY" "Direct" "$filepath"
done
