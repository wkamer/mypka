# Discord Integration

## What it is

Discord is used as the primary notification and communication channel for the myPKA ecosystem. The bot relays alerts, accepts Team Inbox messages, and bridges owner communications.

## Authentication

- **Method:** Bot token
- **Bitwarden item:** "Discord Bot"
- **Token location:** `DISCORD_BOT_TOKEN` environment variable in `mypka-discord-bridge.env`

## Permissions / Intents

- Read messages in configured channels
- Send messages
- Message history access
- Team Inbox channel write access

Apply least-privilege: only add intents the bridge actively uses.

## Key configuration values

| Variable | Description | Bitwarden item |
|---|---|---|
| `DISCORD_BOT_TOKEN` | Bot authentication token | "Discord Bot" |
| `DISCORD_OWNER_ID` | Owner's Discord user ID | "Discord Bot / Channel IDs" |

## Kanalen — K'mer Base server

Naamconventie: `DISCORD_CHANNEL_<CATEGORIE>_<NAAM>` — altijd categorie erbij zodat kanalen met dezelfde naam uniek zijn.

| Variable | Categorie | Channel naam | Channel ID |
|---|---|---|---|
| `DISCORD_CHANNEL_PERSONAL_GENERAL` | Personal | general | `1505520574024388691` |
| `DISCORD_CHANNEL_TEAM_NOTIFICATIONS` | Team | 🔔┃notifications | `1505993795244789760` |
| `DISCORD_CHANNEL_TEAM_INBOX` | Team | 📥┃inbox | `1505992336616849568` |
| `DISCORD_CHANNEL_KAMER_ECOMMERCE_GENERAL` | Kamer E-commerce | general | `1505520639824367656` |

Gebruik altijd de benoemde variabele, nooit een hardcoded ID. Bij een nieuw kanaal: voeg het hier én in `.env` toe voor je het gebruikt.

## Rate limits

- 50 requests per second (global)
- Per-channel: 5 messages per 5 seconds
- On 429: use the `retry_after` value from the response body

## Used by

`mypka-discord-bridge.py` at `Team Knowledge/Core/Integrations/discord/mypka-discord-bridge.py`

## Service

Managed by systemd: `mypka-discord-bridge.service`

- Script: `/opt/myPKA/Team Knowledge/Core/Integrations/discord/mypka-discord-bridge.py`
- EnvironmentFile: `/opt/myPKA/Team Knowledge/Core/Integrations/discord/.env`
- Python: `/opt/n8n/venv/bin/python`
