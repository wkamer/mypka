# Integrations

myPKA's kant van de verbinding met externe en lokale systemen. Een integratie folder bevat alles wat nodig is om myPKA met een systeem te laten werken: credentials, helpers, handlers, config.

Waar het systeem draait — lokaal (`/opt/`) of in de cloud — maakt niet uit. Dropbox is een systeem (extern). n8n is een systeem (lokaal op de Pi). Beide krijgen een integratie folder hier.

Interne myPKA daemons en watchers die geen verbinding met een systeem maken → `Team Knowledge/Core/Services/`.

**Owner:** Kai — The Infrastructure & Integration Architect

---

## Structure

```
Integrations/
  README.md               this file
  .gitignore              blocks secrets from git
  google/
    token.json            OAuth 2.0 refresh token (NOT in git)
    client_secret.json    OAuth 2.0 client credentials (NOT in git)
    scopes.md             active scopes and notes
  todoist/
    config.md             auth, rate limits, project IDs reference
  n8n/
    .env.template         n8n core service variables (keys only)
    bridges/
      larry-bridge.env.template
      mypka-ai-bridge.env.template
      mypka-discord-bridge.env.template
      mypka-meta-bridge.env.template
  discord/
    config.md             bot config, permissions, rate limits
  meta/
    config.md             Meta Marketing API, scopes, token management
  shopify/
    config.md             Admin API scopes, rate limits, write rules
  dropbox/
    config.md             OAuth2 token management, sync flow
    sync_handler.sh       copies Recorded Audio from Dropbox → Team Inbox, deletes source
    setup_token.sh        replaces rclone token from /tmp/dropbox_token.txt
```

---

## Rebuild from scratch (< 2 hours)

Follow these steps in order after a full system restore.

### Step 2b — Restore Dropbox rclone token (5 min)

1. Retrieve "Dropbox / rclone token" JSON from Bitwarden and save to `/tmp/dropbox_token.txt`
2. Run: `bash "Team Knowledge/Core/Integrations/dropbox/Scripts/setup_token.sh"`

### Step 1 — Retrieve secrets from Bitwarden (15 min)

Open Bitwarden and locate each item referenced in the `.env.template` files below. You will need:

- "n8n / Postgres" (user, password, db name)
- "n8n / Encryption Key"
- "n8n / Network" (host, editor base URL, webhook URL)
- "n8n / API Key"
- "Discord Bot" (token, channel IDs, owner ID)
- "Larry Bridge / Token"
- "AI Bridge / Token"
- "Meta / App" (app ID, app secret)
- "Meta / Access Token"
- "Meta / Ad Account"
- "Todoist / API Token"
- "Shopify / Admin API Token"

### Step 2 — Restore Google OAuth credentials (10 min)

1. Copy `token.json` from your offsite backup (Backblaze B2 or Google Drive) to `Integrations/google/token.json`
2. Copy `client_secret.json` from your offsite backup to `Integrations/google/client_secret.json`
3. If token.json is lost: delete the file and run any script that calls `google_helper.py` — it will open a browser OAuth flow to re-authenticate

### Step 3 — Populate n8n .env (10 min)

```bash
cp /opt/myPKA/Integrations/n8n/.env.template /opt/n8n/.env
# Fill in each variable using values from Bitwarden
nano /opt/n8n/.env
```

### Step 4 — Populate bridge .env files (15 min)

```bash
cp /opt/myPKA/Integrations/n8n/bridges/larry-bridge.env.template /opt/n8n/larry-bridge.env
cp /opt/myPKA/Integrations/n8n/bridges/mypka-ai-bridge.env.template /opt/n8n/mypka-ai-bridge.env
cp /opt/myPKA/Integrations/n8n/bridges/mypka-discord-bridge.env.template /opt/n8n/mypka-discord-bridge.env
cp /opt/myPKA/Integrations/n8n/bridges/mypka-meta-bridge.env.template /opt/n8n/mypka-meta-bridge.env
# Fill in each file using values from Bitwarden
```

### Step 5 — Start services (10 min)

```bash
cd /opt/n8n
docker compose up -d

# Restart bridges
sudo systemctl restart larry-bridge
sudo systemctl restart mypka-ai-bridge
sudo systemctl restart mypka-discord-bridge
```

### Step 6 — Verify (15 min)

- Open n8n editor URL and confirm login works
- Check Uptime Kuma — all services should go green within 2 minutes
- Send a test message via Discord and confirm the bridge responds
- Run a test script using `google_helper.py` and confirm it returns data without an auth error

### Step 7 — Restore n8n workflows (10 min)

If n8n workflows were lost (volume not restored):

```bash
# Import from backup export files in your offsite backup
# In n8n UI: Settings > Import Workflows
```

---

## Security notes

- `token.json` and `client_secret.json` are excluded from git via `.gitignore`
- All `.env` files (with values) are excluded from git — only `.env.template` files are committed
- All secrets live in Bitwarden — never in this repo
- Rotate tokens annually; immediately on suspected compromise

---

## Owned by

Kai — The Infrastructure & Integration Architect
`Team/Kai - The Infrastructure & Integration Architect/AGENT.md`
