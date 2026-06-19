# Team Inbox Watcher Integration

## What it is

Watches `/opt/myPKA/Team Inbox/` recursively for new files and sends a notification to the n8n Team Inbox webhook. n8n forwards the notification to Discord.

## Source detection

Priority order (first match wins):

| Condition | Source label |
|---|---|
| File path contains `/Recorded Audio/` | iPhone |
| Marker file `.source_discord_<filename>` present in same dir | Discord |
| _(none)_ | Direct |

The marker file is created by the originating integration before the file lands. The watcher deletes it after reading. Path-based detection (iPhone) takes priority and requires no marker — any file synced into `Team Inbox/Recorded Audio/` is always treated as iPhone.

## Notification format

GL-006: Source · Subject · Status · Message

## Dependencies

- `inotifywait` (inotify-tools)
- n8n webhook: `http://localhost:5678/webhook/team-inbox`
- Runs as systemd service: `team-inbox-watcher`

## Logs

```bash
journalctl -u team-inbox-watcher -f
```

## Service management

```bash
sudo systemctl restart team-inbox-watcher
sudo systemctl status team-inbox-watcher
```

## Crontab / service file

Systemd service — `/etc/systemd/system/team-inbox-watcher.service`
Points to: `Team Knowledge/Core/Services/team-inbox-watcher/team_inbox_watcher.sh`
