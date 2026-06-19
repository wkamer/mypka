# Meta Integration

## What it is

The Meta integration connects the myPKA ecosystem to the Meta Marketing API for ad account data (Kamer E-commerce domain). Used for campaign reporting and analytics.

## Authentication

- **Method:** Long-lived access token (OAuth 2.0)
- **Bitwarden item:** "Meta / Access Token"
- **Token location:** `META_ACCESS_TOKEN` environment variable in `mypka-meta-bridge.env`

## Credentials

| Variable | Description | Bitwarden item |
|---|---|---|
| `META_APP_ID` | App ID from Meta Developer Console | "Meta / App" |
| `META_APP_SECRET` | App secret | "Meta / App" |
| `META_ACCESS_TOKEN` | Long-lived user/system access token | "Meta / Access Token" |
| `META_AD_ACCOUNT_ID` | Ad account ID (format: `act_XXXXXXXXX`) | "Meta / Ad Account" |
| `META_API_VERSION` | API version (e.g. `v19.0`) | n/a |

## Permissions (scopes)

- `ads_read` — read ad account, campaign, ad set, and ad data
- `ads_management` — required for any write operations on ads

Apply least-privilege: use `ads_read` only unless write operations are explicitly needed.

## Token expiry

- Long-lived tokens expire in ~60 days
- Refresh before expiry via the token refresh endpoint
- System User tokens (via Business Manager) do not expire — preferred for automation

## Rate limits

- Marketing API: tiered by ad account spend tier
- Default: 200 calls per hour per app per token
- On 17 (`User Request Limit Reached`): back off and retry

## Used by

`mypka-meta-bridge.py` in `/opt/n8n/`
