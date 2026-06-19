"""
todoist_helper.py — Todoist API token loader.

Token wordt gelezen uit Integrations/todoist/.env.
Nooit hardcoden in scripts.

Gebruik:
    from todoist_helper import get_token
    TOKEN = get_token()
"""
import os

_ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')


def _read_env(path: str) -> dict:
    result = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, _, value = line.partition('=')
                result[key.strip()] = value.strip()
    return result


def get_token() -> str:
    try:
        env = _read_env(_ENV_FILE)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Todoist .env niet gevonden op {_ENV_FILE}\n"
            "Zet TODOIST_API_TOKEN= in Integrations/todoist/.env"
        )
    token = env.get('TODOIST_API_TOKEN', '')
    if not token:
        raise ValueError(f"TODOIST_API_TOKEN niet gevonden in {_ENV_FILE}")
    return token
