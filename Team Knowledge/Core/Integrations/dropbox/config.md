# Dropbox Integration

## What it is

Dropbox is used as a transfer layer for voice memos from the iPhone to the myPKA Team Inbox. The iPhone Shortcuts app saves recorded audio to `Dropbox/Recorded Audio/`. A sync script on the Pi copies those files to `Team Inbox/Recorded Audio/` and deletes them from Dropbox.

## Authentication

- **Method:** OAuth2 via rclone
- **Remote name:** `dropbox`
- **Token location:** `~/.config/rclone/rclone.conf` — section `[dropbox]`
- **Bitwarden item:** "Dropbox / rclone token"

## Re-authenticate

If the token expires or is revoked:

1. On your local machine: `rclone authorize "dropbox" > ~/dropbox_token.txt`
2. Open `~/dropbox_token.txt`, copy the complete JSON (from `{` to `}`)
3. SCP to Pi: `scp ~/dropbox_token.txt admin@raspberrypi.local:/tmp/dropbox_token.txt`
4. On Pi: run `Team Knowledge/Core/Integrations/dropbox/Scripts/setup_token.sh`

## Sync flow

| Step | What happens |
|---|---|
| iPhone Shortcut records audio | File saved to `Dropbox/Recorded Audio/` |
| Cron job runs (every 5 min) | `sync_voice_inbox.sh` copies to `Team Inbox/Recorded Audio/` |
| After successful copy | File deleted from Dropbox |
| team-inbox-watcher | Picks up new file, triggers n8n webhook |

## Paths

| Location | Path |
|---|---|
| Dropbox source | `dropbox:/Recorded Audio/` |
| Pi destination | `/opt/myPKA/Team Inbox/Recorded Audio/` |
| Sync handler | `Team Knowledge/Core/Integrations/dropbox/sync_handler.sh` |
| Log | `Team Knowledge/Core/Integrations/dropbox/logs/dropbox-recorded-audio-sync.log` |
| rclone config | `Team Knowledge/Core/Integrations/dropbox/rclone.conf` |

## Used by

Larry (routing), Sienna (Team Inbox processing)
