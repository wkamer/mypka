# GL-007 — Integration Naming Convention

## Rationale

Consistent naming across integrations reduces cognitive load: any agent or engineer can open an integration folder and immediately know what each file does without reading it. Vague names (`helper.py`, `utils.py`) hide intent; specific names (`connection.py`, `product_handler.py`) make intent explicit. This convention enforces that pattern across all integrations in `Team Knowledge/Core/Integrations/`.

---

## Standard Structure

Every integration lives in its own subfolder under `Team Knowledge/Core/Integrations/`:

```
integrations/
└── <integration_name>/
    ├── .env.example
    ├── README.md
    ├── connection.py
    └── <singular>_handler.py
```

Additional handler files are allowed when an integration covers multiple distinct object types (e.g. `order_handler.py` and `product_handler.py`). Each handler covers one object type.

---

## connection.py

**Purpose:** manages the technical connection to the external API.

Belongs in `connection.py`:
- Environment reading (`_read_env()`)
- Token acquisition and caching (`_get_token()`, `_fetch_token_via_credentials()`, `_token_cache`)
- Session or client initialization that is shared across all handlers
- Constants that are connection-scoped (store URL, API version, base URL)

Does not belong in `connection.py`:
- Business logic
- Object-specific methods (products, orders, ads)

---

## Handler Naming Rules

### Singular by default

The handler filename is singular: name it after the primary object type the handler operates on.

| Object type | Handler filename |
|---|---|
| Product | `product_handler.py` |
| Order | `order_handler.py` |
| Page | `page_handler.py` |
| Customer | `customer_handler.py` |

### Plural only when the capability itself is plural

Use plural only when the external API or feature is officially named in plural form.

| Capability | Handler filename | Reason |
|---|---|---|
| Meta Ads (Ad Library) | `ad_library_handler.py` | "Meta Ads" / "Ad Library" is the official product name |
| Shopify (all capabilities) | `shopify_handler.py` | Store-wide handler; singular by convention |

When in doubt: singular.

### One class per handler

Each handler file contains one primary class. The class name mirrors the handler name in PascalCase:
- `product_handler.py` → `class ProductHandler`
- `shopify_handler.py` → `class ShopifyClient`
- `ad_library_handler.py` → `class MetaAdLibrary`

---

## Forbidden Names

The following filenames are not allowed anywhere in the `integrations/` tree:

| Forbidden | Reason |
|---|---|
| `helper.py` | Vague — does not communicate what it helps with |
| `utils.py` | Vague — could mean anything |
| `misc.py` | Vague — explicitly "miscellaneous" is not a design |
| `api.py` | Too generic when used as a catch-all |
| `client.py` | Acceptable only as an alias; prefer `connection.py` for the connection layer |

---

## Examples

### Meta integration

```
integrations/
└── meta/
    ├── .env.example
    ├── README.md
    ├── connection.py          ← _read_env(), rate limiter, _api_get(), _paginate()
    ├── ad_library_handler.py  ← MetaAdLibrary class (Ad Library is the official product name)
    └── mypka-meta-bridge.py   ← existing service; not subject to this convention
```

### Shopify integration

```
integrations/
└── shopify/
    ├── .env.example
    ├── README.md
    ├── connection.py      ← _read_env(), _fetch_token_via_credentials(), _get_token(), _token_cache
    └── shopify_handler.py ← ShopifyClient class + all methods + smoke test block
```

---

## Security Rules

- **`.env` must never be committed to Git.** Add `.env` to `.gitignore` at repository root.
- **`.env.example` is always committed.** It documents required variables with empty values.
- `.env.example` format:

```
SHOPIFY_CLIENT_ID=
SHOPIFY_CLIENT_SECRET=
```

```
META_APP_ID=
META_APP_SECRET=
META_ACCESS_TOKEN=
META_AD_ACCOUNT_ID=
META_API_VERSION=
```

- Secrets are never hardcoded in any `.py` file — not even as fallback defaults.
- Token caches live in-process only (never written to disk).
