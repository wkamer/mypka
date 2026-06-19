#!/opt/n8n/venv/bin/python3
"""
connection.py — Meta Graph API technische verbinding

Verantwoordelijk voor:
- .env lezen (_read_env)
- Rate limiting (_RateLimiter, _rate_limiter)
- HTTP GET met retry-logica (_api_get)
- Cursor-based paginering (_paginate)
- API-constanten (_API_BASE, _EU_COUNTRIES, rate limit config)

Geïmporteerd door ad_library_handler.py. Nooit direct aanroepen.
"""

import json
import time
import urllib.error
import urllib.parse
import urllib.request

# ---------------------------------------------------------------------------
# Constanten
# ---------------------------------------------------------------------------

_API_BASE = "https://graph.facebook.com"

# EU landen voor DSA-rijke data coverage
_EU_COUNTRIES = ["NL", "GB", "DE"]

# Rate limiting: Meta Ad Library API — conservatief 200 calls/uur
_RATE_LIMIT_CALLS_PER_HOUR = 200
_MIN_INTERVAL_SECONDS = 3600 / _RATE_LIMIT_CALLS_PER_HOUR  # ~18 seconden


# ---------------------------------------------------------------------------
# Env helper
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Rate limit tracker (in-process)
# ---------------------------------------------------------------------------

class _RateLimiter:
    """Eenvoudige token-bucket voor max 200 calls/uur."""

    def __init__(self, calls_per_hour: int = _RATE_LIMIT_CALLS_PER_HOUR):
        self._interval = 3600 / calls_per_hour
        self._last_call = 0.0

    def wait(self):
        now = time.time()
        elapsed = now - self._last_call
        if elapsed < self._interval:
            time.sleep(self._interval - elapsed)
        self._last_call = time.time()


_rate_limiter = _RateLimiter()


# ---------------------------------------------------------------------------
# HTTP helper met retry-logica
# ---------------------------------------------------------------------------

def _api_get(url: str, params: dict, max_retries: int = 5) -> dict:
    """
    GET-request naar Meta Graph API met exponential backoff.
    Retourneert de geparseerde JSON body.
    Gooit RuntimeError bij niet-herstelbare fouten.
    """
    _rate_limiter.wait()

    query_string = urllib.parse.urlencode(params, doseq=True)
    full_url = f"{url}?{query_string}"

    delay = 5
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(full_url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")

            # Rate limit (429) of Business Use Case rate limit (613)
            if e.code in (429, 613):
                print(f"  [rate-limit] HTTP {e.code} — wacht {delay}s (poging {attempt + 1}/{max_retries})")
                time.sleep(delay)
                delay = min(delay * 2, 120)
                continue

            # Scope-fout onderscheppen en duidelijk rapporteren
            if e.code == 400:
                try:
                    err_data = json.loads(body)
                    err_msg = err_data.get("error", {}).get("message", "")
                    err_code = err_data.get("error", {}).get("code", "")
                    if "ads_read" in err_msg or err_code in (200, 10):
                        raise RuntimeError(
                            f"Token heeft onvoldoende scope.\n"
                            f"Vereist: ads_read\n"
                            f"Meta fout: {err_msg}\n"
                            f"Oplossing: genereer een nieuw token via "
                            f"developers.facebook.com/tools/explorer met 'ads_read' permission."
                        )
                except (json.JSONDecodeError, KeyError):
                    pass
                raise RuntimeError(f"HTTP 400 van Meta API: {body[:500]}")

            raise RuntimeError(f"HTTP {e.code} van Meta API: {body[:500]}")

        except urllib.error.URLError as e:
            if attempt < max_retries - 1:
                print(f"  [network] URLError: {e.reason} — wacht {delay}s (poging {attempt + 1}/{max_retries})")
                time.sleep(delay)
                delay = min(delay * 2, 60)
                continue
            raise RuntimeError(f"Netwerk-fout na {max_retries} pogingen: {e.reason}")

    raise RuntimeError(f"API-call mislukt na {max_retries} pogingen (rate limit uitgeput).")


def _paginate(url: str, params: dict, limit: int) -> list:
    """
    Haalt resultaten op via cursor-based paginering totdat `limit` bereikt is.
    Retourneert gecombineerde lijst van alle `data`-elementen.
    """
    results = []
    current_url = url
    current_params = dict(params)

    while len(results) < limit:
        current_params["limit"] = min(limit - len(results), 50)  # max 50 per call
        response = _api_get(current_url, current_params)
        data = response.get("data", [])
        results.extend(data)

        # Cursor-based paginering
        paging = response.get("paging", {})
        next_url = paging.get("next")
        if not next_url or not data:
            break

        # Volgende pagina: URL is al compleet (inclusief query params van Meta)
        current_url = next_url.split("?")[0]
        current_params = dict(urllib.parse.parse_qs(next_url.split("?")[1]))
        # parse_qs geeft lijsten; flatten naar strings
        current_params = {k: v[0] if isinstance(v, list) else v for k, v in current_params.items()}

    return results[:limit]
