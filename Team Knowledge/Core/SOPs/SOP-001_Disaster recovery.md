# SOP: Disaster Recovery — Full System Restore

**Purpose:** Restore the complete AI team setup on any machine from scratch.
**Starting point:** Any device with internet access. The `myPKA` folder is the SSOT — everything derives from it.
**Time estimate:** 45–90 minutes depending on platform and download speed.

> Platform notes appear only where the command actually differs. Where there is no note, the command is identical on Windows, macOS, and Linux/Pi.

---

## What Lives in myPKA (Automatic)

`myPKA` syncs via Google Drive. Everything inside survives device changes without extra steps:

| What | Where |
|---|---|
| All CLAUDE.md / AGENT.md files | throughout myPKA |
| Databases | `PKM/personal.db`, `Team Knowledge/*.db` |
| Scripts (relative paths, any device) | `Team Knowledge/Core/Scripts/` |
| MCP config + Todoist API key | `.mcp.json` |
| API keys + WordPress credentials | `.env` |
| Claude permissions + MCP allowlist | `.claude/settings.local.json` |
| Claude memory (device-independent) | `.claude/memory/` |
| Google OAuth credentials file | `client_secret_*.json` (myPKA root) |
| All SOPs, Deliverables, Inbox files | throughout myPKA |

**What lives outside myPKA and must be set up per device:**
- `~/.claude/settings.json` — user-level settings (plugins, env vars)
- `token.json` — Google OAuth token (re-generated per device, stays in myPKA root)
- Memory symlink from `~/.claude/projects/<hash>/memory/` to `myPKA/.claude/memory/`

**SQLite write conflict rule:** Never open the same database on two devices simultaneously. If a second device becomes active, close the vault on the first.

---

## Step 1 — Get myPKA onto the device

myPKA lives on Google Drive. Choose the right client for the device:

**Google Drive desktop (Windows / macOS):** Install the Google Drive desktop app, sign in, wait for sync. myPKA appears at:
- Windows: `C:\Users\<username>\myPKA\`
- macOS: `/Users/<username>/myPKA/`

**rclone (Linux / Pi / any headless device):**
```bash
sudo apt install rclone fuse3    # Debian/Ubuntu/Pi OS
rclone config                    # add remote: name it "gdrive", type Google Drive, follow OAuth
mkdir -p ~/myPKA
rclone mount gdrive:myPKA ~/myPKA --vfs-cache-mode writes --daemon
```

Auto-mount at boot (systemd):
```bash
sudo tee /etc/systemd/system/rclone-gdrive.service > /dev/null << 'EOF'
[Unit]
Description=rclone Google Drive mount
After=network-online.target

[Service]
ExecStart=rclone mount gdrive:myPKA /home/pi/myPKA --vfs-cache-mode writes
ExecStop=/bin/fusermount -u /home/pi/myPKA
Restart=on-failure
User=pi

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl enable rclone-gdrive && sudo systemctl start rclone-gdrive
```

Replace `/home/pi` with your home directory if the username differs.

---

## Step 2 — Install Node.js and Python

```bash
# Debian / Ubuntu / Pi OS
sudo apt update && sudo apt upgrade -y
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install nodejs python3 python3-pip -y
```

```powershell
# Windows (winget)
winget install OpenJS.NodeJS
winget install Python.Python.3
```

```bash
# macOS (Homebrew)
brew install node python
```

Verify:
```
node --version
python3 --version
```

---

## Step 3 — Install Claude Code

```
npm install -g @anthropic-ai/claude-code
```

Sign in (opens browser or device-auth URL):
```
claude
```

Claude Code runs on your existing Pro/Max subscription. No extra API costs.

---

## Step 4 — Open myPKA and link memory

Navigate to myPKA and start Claude Code once, then exit:
```bash
cd ~/myPKA    # adjust path for your device
claude
# exit immediately with /exit or Ctrl+C
```

This creates the session folder at `~/.claude/projects/<path-hash>/`. Now link memory so it travels with myPKA:

**Linux / macOS / Pi:**
```bash
HASH_DIR=$(ls ~/.claude/projects/ | grep "myPKA" | head -1)
SESSION_MEMORY=~/.claude/projects/$HASH_DIR/memory
VAULT_MEMORY=~/myPKA/.claude/memory

rm -rf "$SESSION_MEMORY"
ln -s "$VAULT_MEMORY" "$SESSION_MEMORY"
echo "Linked: $SESSION_MEMORY -> $VAULT_MEMORY"
```

**Windows (PowerShell):**
```powershell
$hash = Get-ChildItem "$env:USERPROFILE\.claude\projects" | Where-Object { $_.Name -match "myPKA" } | Select-Object -ExpandProperty Name
$sessionMemory = "$env:USERPROFILE\.claude\projects\$hash\memory"
$vaultMemory = "$env:USERPROFILE\myPKA\.claude\memory"

Remove-Item $sessionMemory -Recurse -Force -ErrorAction SilentlyContinue
cmd /c mklink /J "$sessionMemory" "$vaultMemory"
Write-Host "Linked: $sessionMemory -> $vaultMemory"
```

After this step, memory is device-independent and persists in myPKA.

---

## Step 5 — User-level Claude settings

Create or restore `~/.claude/settings.json`. Minimum required content:

```json
{
  "env": {
    "TODOIST_API_TOKEN": "ec179b9939cca5bc7179accb57fd30fce8711c16"
  },
  "enabledPlugins": {
    "context-mode@context-mode": true,
    "shopify-plugin@shopify-ai-toolkit": true
  }
}
```

Windows additionally needs:
```json
  "env": {
    "TODOIST_API_TOKEN": "ec179b9939cca5bc7179accb57fd30fce8711c16",
    "CLAUDE_CODE_USE_POWERSHELL_TOOL": "true"
  }
```

---

## Step 6 — MCP Servers

`.mcp.json` is already in myPKA with the Todoist API key embedded.

Verify:
```
claude mcp list
```
Expected: Todoist connected.

---

## Step 7 — Google Authentication

Run once per device to generate `token.json`:
```bash
python3 "Team Knowledge/Core/Scripts/google_auth.py"
# Windows:
python "Team Knowledge/Core/Scripts/google_auth.py"
```

A browser opens for OAuth consent. On headless devices (Pi without desktop), the script prints a URL — open it on any browser, paste the code back. The `client_secret_*.json` file must be present in the myPKA root (it syncs via Google Drive). If missing, re-download from Google Cloud Console (project: myPKA, OAuth 2.0 Desktop App client).

Scopes: spreadsheets, gmail.modify, calendar, drive.

---

## Step 8 — Context-Mode Plugin

```
claude plugin marketplace add mksglu/context-mode
claude plugin install context-mode@context-mode
```

Restart Claude Code. Verify: `claude plugin list` shows context-mode enabled.

---

## Step 9 — Python Dependencies

```bash
# Linux / Pi OS (Debian-based):
sudo apt install python3-google-auth python3-google-auth-oauthlib python3-googleapi python3-google-api-core -y
# macOS:
pip3 install google-auth google-auth-oauthlib google-api-python-client
# Windows:
pip install google-auth google-auth-oauthlib google-api-python-client
```

`sqlite3` is built into Python — no install needed.

---

## Step 10 — Platform-specific: Windows

Install Shopify tooling (needed for Kamer E-commerce / Sasha):

```powershell
winget install Shopify.ShopifyCLI
winget install Ollama.Ollama
```

Install plugins:
```
claude plugins install shopify-plugin@shopify-ai-toolkit
claude plugins enable shopify-plugin@shopify-ai-toolkit
```

Authenticate Shopify:
```
shopify store auth --store ynmuzt-xm.myshopify.com --scopes read_products,write_products,read_inventory,write_inventory,read_locations,write_locations,read_orders,write_orders,read_order_edits,write_order_edits,read_fulfillments,write_fulfillments,read_assigned_fulfillment_orders,write_assigned_fulfillment_orders,read_merchant_managed_fulfillment_orders,write_merchant_managed_fulfillment_orders,read_draft_orders,write_draft_orders,read_returns,write_returns,read_customers,write_customers,read_discounts,write_discounts,read_price_rules,write_price_rules,read_shipping,write_shipping,read_content,write_content,read_online_store_pages,read_online_store_navigation,write_online_store_navigation,read_reports,read_gift_cards,write_gift_cards,read_themes,write_themes,read_translations,write_translations,read_markets,write_markets,read_metaobjects,write_metaobjects
```
Log in as `info@kamerecommerce.com`. Verify: `shopify store execute --store ynmuzt-xm.myshopify.com --query 'query { shop { name } }'` returns `"Tricolarae"`.

Pull local LLM for Pax:
```
ollama pull qwen3.5:9b
```

---

## Step 11 — Platform-specific: always-on server (Pi or Linux)

Install n8n as automation layer for Telegram, cron, and webhook triggers:

```bash
npm install -g n8n
```

Run as a systemd service:
```bash
sudo tee /etc/systemd/system/n8n.service > /dev/null << 'EOF'
[Unit]
Description=n8n workflow automation
After=network.target

[Service]
ExecStart=/usr/bin/n8n start
Restart=always
User=pi
Environment=N8N_PORT=5678

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl enable n8n && sudo systemctl start n8n
```

n8n UI at `http://<device-ip>:5678`.

Flows to configure:
- Telegram trigger (whitelist your user ID) → `claude` CLI → reply
- Gmail webhook → Larry processes mail
- Cron 07:00 → morning check

---

## Step 13 — Verify Everything

| Check | Command | Expected |
|---|---|---|
| Claude Code | `claude --version` | Version number |
| MCP | `claude mcp list` | Todoist connected |
| Memory link | `ls -la ~/.claude/projects/<hash>/memory` | Symlink or junction to myPKA/.claude/memory/ |
| Context-mode | `claude plugin list` | context-mode enabled |
| Google auth | `python3 "Team Knowledge/Core/Scripts/google_auth.py"` | "Authenticatie geslaagd" |
| Databases | `python3 "Team Knowledge/Core/Scripts/session_open.py"` | Open tasks listed |
| Shopify (Windows) | `shopify store execute --store ynmuzt-xm.myshopify.com --query 'query { shop { name } }'` | "Tricolarae" |
| n8n (server) | `http://<ip>:5678` | UI loads |

---

## Key Credentials Reference

| System | Credential | Where |
|---|---|---|
| Anthropic | Account login | claude.ai — Pro/Max subscription |
| Todoist | `ec179b9939cca5bc7179accb57fd30fce8711c16` | `.mcp.json` (syncs in myPKA) |
| OpenRouter | API key | `.env` (syncs in myPKA) |
| Google | OAuth2 Desktop App | Re-run `google_auth.py` per device |
| Shopify store | `ynmuzt-xm.myshopify.com` | `Team/Sasha - The Shopify Agent/AGENT.md` |
| Shopify login | `info@kamerecommerce.com` | OAuth via browser |
| WordPress (GR) | `GR_WP_USER` + `GR_WP_APP_PASSWORD` | `.env` (syncs in myPKA) |

---

## Geldstroom Regie — WordPress

Site: geldstroomregie.nl. Hosting: Vimmex.
Credentials in `.env`. If lost: create a new Application Password in WordPress Admin and update `.env`.
Maintenance plugin: "Maintenance" by WebFactory Ltd — active. Disable via wp-admin before launch.

---

## Backup Infrastructure (B-001)

The backup infrastructure below was introduced in B-001 (Stabilization Package v1). All backup jobs run as cron jobs on the always-on Pi server.

### Backup Scripts and Schedule

| Time | Script | Target | Retention |
|---|---|---|---|
| `0 2 * * *` | `/home/admin/.config/rclone/local-backup.sh` | `/home/admin/backups/myPKA/YYYYMMDD/` | 30 days |
| `30 2 * * *` | `Team Knowledge/Core/Scripts/backup_sqlite_dbs.sh` | `/home/admin/backups/sqlite/YYYYMMDD/` | 7 days |
| `45 2 * * *` | `Team Knowledge/Core/Integrations/n8n/backup_n8n.sh` | `/home/admin/backups/n8n/` | 7 days |

Google Drive sync (every 5 minutes, one-way):

| Time | Script | Target |
|---|---|---|
| `*/5 * * * *` | `/home/admin/.config/rclone/sync.sh` | `gdrive:myPKA` |

### Backup Types

**1. myPKA local rsync snapshot**
- Script: `/home/admin/.config/rclone/local-backup.sh`
- Source: `/opt/myPKA/`
- Target: `/home/admin/backups/myPKA/YYYYMMDD/`
- Retention: 30 days

**2. SQLite database backup**
- Script: `Team Knowledge/Core/Scripts/backup_sqlite_dbs.sh`
- Target: `/home/admin/backups/sqlite/YYYYMMDD/`
- Databases: `personal.db`, `team-knowledge.db`, `kamer-ecommerce.db`, `geldstroom-regie.db`
- Retention: 7 days

**3. n8n PostgreSQL backup**
- Script: `Team Knowledge/Core/Integrations/n8n/backup_n8n.sh`
- Target: `/home/admin/backups/n8n/YYYYMMDD_n8n-postgres.sql`
- What: daily `pg_dump` of the n8n-postgres database
- Retention: 7 days
- **Canonical B-001 managed backup: `/home/admin/backups/n8n/`**
- Pre-existing separate backup: `/opt/n8n/backup-n8n.sh` → `/opt/n8n/backups/` — pre-dates B-001, currently active. No decommissioning is approved.

### Rclone Re-Authentication

rclone may require re-authentication on new hardware or after token expiry. This requires device access and an OAuth flow (browser or device-auth URL). See Step 1 for the initial rclone setup procedure.

### Google Drive Remote Validation

The Google Drive remote contents (`gdrive:myPKA`) were **not validated** as part of the B-021 backup check. The rclone sync job is confirmed active in crontab, but end-to-end backup coverage is not confirmed until a separate remote validation check is performed.

---

## Changelog

- 2026-06-03 (Kai, B-021A): Added backup infrastructure documentation for B-001 backups. Documentation only. No scripts, backups, credentials or remote contents modified. Approved by Owner.
- 2026-06-03 (Larry, B-021C-A): Step 12c fully replaced — complete English credential recovery procedure with permission lock and pre-start verification. Backup Infrastructure placeholder replaced with cross-reference to Step 12c. Approved by Owner Walter Kamer.

---

*Last updated: 2026-06-03 — B-021A: backup infrastructure documentation added.*
