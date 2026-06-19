#!/opt/n8n/venv/bin/python3
"""
connection.py — Shopify technische verbinding

Verantwoordelijk voor:
- .env lezen (_read_env)
- Token ophalen via client credentials grant (_fetch_token_via_credentials)
- Token cache beheren (_get_token, _token_cache)
- Store-constanten (STORE, API_VERSION)

Geïmporteerd door shopify_handler.py. Nooit direct aanroepen.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.error

# --- Constanten -----------------------------------------------------------------

STORE = "ynmuzt-xm.myshopify.com"
API_VERSION = "2025-01"  # Shopify stabiele versie — update bij Shopify major releases

_ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')

# In-memory token cache (geldig per proces, maximaal 24u)
_token_cache: dict = {"token": None, "expires_at": 0}


# --- Env helper -----------------------------------------------------------------

def _read_env(path: str) -> dict:
    result = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, _, value = line.partition('=')
                    result[key.strip()] = value.strip()
    except FileNotFoundError:
        pass
    return result


# --- Token management -----------------------------------------------------------

def _fetch_token_via_credentials(client_id: str, client_secret: str) -> tuple:
    """Haalt een access token op via client credentials grant. Retourneert (token, expires_at)."""
    url = f"https://{STORE}/admin/oauth/access_token"
    payload = json.dumps({
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }).encode()
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
            token = data["access_token"]
            expires_in = data.get("expires_in", 86399)
            expires_at = int(time.time()) + expires_in - 300  # 5 min veiligheidsmarge
            return token, expires_at
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        raise RuntimeError(f"Token ophalen mislukt ({e.code}): {body}")


def _get_token() -> str:
    """Retourneert een geldig access token. Ververst automatisch bij verlopen."""
    global _token_cache

    env = _read_env(_ENV_FILE)

    # Gecachte token nog geldig
    if _token_cache["token"] and time.time() < _token_cache["expires_at"]:
        return _token_cache["token"]

    client_id = env.get("SHOPIFY_CLIENT_ID", "").strip()
    client_secret = env.get("SHOPIFY_CLIENT_SECRET", "").strip()

    if not client_id or not client_secret:
        print(f"ERROR: SHOPIFY_CLIENT_ID en/of SHOPIFY_CLIENT_SECRET niet gevonden in {_ENV_FILE}")
        print("Zet beide waarden in Integrations/shopify/.env")
        sys.exit(1)

    token, expires_at = _fetch_token_via_credentials(client_id, client_secret)
    _token_cache["token"] = token
    _token_cache["expires_at"] = expires_at
    return token
