# Meta Integration

## What it is

The Meta integration connects the myPKA ecosystem to the Meta Marketing API and Meta Ad Library API. Used for product intelligence research (Remy) and campaign analytics (Kamer E-commerce domain).

## Files

| File | Purpose |
|---|---|
| `connection.py` | `_read_env()`, `_RateLimiter`, `_api_get()`, `_paginate()` — shared transport layer |
| `ad_library_handler.py` | `MetaAdLibrary` class — Ad Library search, filtering, enrichment, weekly report |
| `mypka-meta-bridge.py` | Systemd service bridge — do not modify (symlinked to `/opt/mypka-meta-bridge.py`) |
| `.env` | Credentials (not in Git — see `.env.example`) |
| `.env.example` | Template with required variable names |

## Authentication

- **Method:** Long-lived access token (OAuth 2.0)
- **Bitwarden item:** "Meta / Access Token"
- **Token location:** `META_ACCESS_TOKEN` in `meta/.env`

## Credentials

| Variable | Description | Bitwarden item |
|---|---|---|
| `META_APP_ID` | App ID from Meta Developer Console | "Meta / App" |
| `META_APP_SECRET` | App secret | "Meta / App" |
| `META_ACCESS_TOKEN` | Long-lived user/system access token | "Meta / Access Token" |
| `META_AD_ACCOUNT_ID` | Ad account ID (format: `act_XXXXXXXXX`) | "Meta / Ad Account" |
| `META_API_VERSION` | API version (e.g. `v21.0`) | n/a |

## Permissions (scopes)

- `ads_read` — required for Ad Library access, ad account, campaign, ad set, and ad data
- `ads_management` — required for any write operations on ads

Apply least-privilege: use `ads_read` only unless write operations are explicitly needed.

## Token expiry

- Long-lived tokens expire in ~60 days
- Refresh before expiry via the token refresh endpoint
- System User tokens (via Business Manager) do not expire — preferred for automation

## Rate limits

- Ad Library API: 200 calls per hour per app per token (conservative)
- `connection.py` rate limiter enforces ~18 second intervals automatically
- On 429 or 613: exponential backoff with up to 5 retries

## Usage

```python
from ad_library_handler import MetaAdLibrary
lib = MetaAdLibrary()

# Search active ads by keyword
ads = lib.search_ads(["oversized blazer", "linen set"])

# EU data (richer via DSA legislation)
ads_eu = lib.search_ads_eu(["summer dress"])

# Filter on minimum 14 days active (scaling proof)
scaling = lib.ads_active_since(ads, days=14)

# Extract product signals
signals = lib.extract_products(scaling)

# Full weekly research session
lib.weekly_research_report(
    keywords_list=["oversized blazer", "linen co-ord", "summer maxi dress"],
    output_path="/tmp/weekly_research.md"
)
```

## Smoke test

```bash
cd /opt/myPKA && /opt/n8n/venv/bin/python3 "Team Knowledge/Core/Integrations/meta/ad_library_handler.py"
```

## Used by

- Remy (Product Intelligence) via `ad_library_handler.py`
- `mypka-meta-bridge.py` systemd service (do not modify)
