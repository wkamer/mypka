# Shopify Integration

## What it is

The Shopify integration connects the myPKA ecosystem to the Kamer E-commerce Shopify store. Used for order data, product management, and analytics flows.

## Files

| File | Purpose |
|---|---|
| `connection.py` | Token management: `_read_env()`, `_get_token()`, `_fetch_token_via_credentials()` |
| `shopify_handler.py` | `ShopifyClient` class — all read/write methods + smoke test |
| `.env` | Credentials (not in Git — see `.env.example`) |
| `.env.example` | Template with required variable names |

## Authentication

- **Method:** Admin API access token via client credentials grant (Custom App)
- **Bitwarden item:** "Shopify / Admin API Token"
- **Required variables:** `SHOPIFY_CLIENT_ID`, `SHOPIFY_CLIENT_SECRET` in `shopify/.env`

## Permissions (API scopes)

Grant only what is actively used. Current required scopes:

| Scope | Purpose |
|---|---|
| `read_orders` | Order reporting and analytics |
| `read_products` | Product data reads |
| `write_products` | Product updates (Sasha domain) |
| `read_customers` | Customer data for CRM sync |

Adding a scope requires creating a new app version and re-authenticating.

## Rate limits

- REST Admin API: 2 requests per second (leaky bucket, 40 burst)
- GraphQL Admin API: 50 cost points per second (query cost varies)
- On 429: respect `Retry-After` header; `_execute_with_retry()` handles this automatically

## Write operations

All Shopify write operations require owner approval before execution (CLAUDE.md Shopify rule). Always show: entity + command + before/after values, then wait for confirmation.

`dry_run=True` is the default on all write methods — never bypassed without explicit `dry_run=False`.

## Usage

```python
from shopify_handler import ShopifyClient
client = ShopifyClient()

# Read
products = client.products(first=10)
page = client.page(handle="faq")

# Write (dry_run=True default — safe)
client.update_page(page_id="123", body_html="<p>Nieuw</p>")           # shows plan, does NOT execute
client.update_page(page_id="123", body_html="<p>Nieuw</p>", dry_run=False)  # executes after confirmation
```

## Smoke test

```bash
cd /opt/myPKA && /opt/n8n/venv/bin/python3 "Team Knowledge/Core/Integrations/shopify/shopify_handler.py"
```

## Used by

Sasha (Shopify domain specialist) via scripts in `Team Knowledge/Core/Scripts/`
