# Larry Bridge — n8n ↔ Claude Code integratie

**Datum:** 2026-05-17
**Topics:** infrastructure, n8n, telegram, claude-code
**DB id:** 58

## Samenvatting

Volledige integratie opgezet tussen n8n (Docker) en myPKA via Larry Bridge, een Python HTTP gateway op poort 8765. De gateway voert `claude -p` aan als CLI-aanroep en retourneert het antwoord aan n8n. De Telegram flow in n8n is uitgebreid met een typing indicator, conversatiecontext per chat_id (10 exchanges, 30 min TTL), en een MD→HTML converter node zodat Telegram de responses netjes opmaakt. Cloudflare Access bypass en cloudflared IPv4-fix waren nodig om Telegram webhooks door te laten.

## Beslissingen

- Pro subscription via `claude -p` CLI (niet Anthropic API)
- In-memory conversation history in larry-bridge.py (geen externe store)
- MD→HTML conversie als Code node in n8n (niet in de bridge zelf)
- `N8N_APPEND_ATTRIBUTION: false` + `appendAttribution: false` per node voor footer-verwijdering

## Acties

- larry-bridge.py aangemaakt met `/ask` endpoint en conversation history
- larry-bridge.service systemd unit aangemaakt en geactiveerd
- docker-compose.yml uitgebreid met volume mount, extra_hosts en trust proxy
- Cloudflare Access bypass geconfigureerd voor `/webhook/` pad
- cloudflared config gewijzigd van localhost naar 127.0.0.1 (IPv4-fix)
- n8n Telegram flow aangemaakt: Trigger → Eigenaar check → Typing → Ask Larry → MD naar HTML → Stuur antwoord
- MD naar HTML Code node ingevoegd via n8n API (Python patch script)
- `parse_mode: HTML` ingesteld op Stuur antwoord node

## Delegaties

Geen.

## Open punten

- Footer nog te testen na huidige wijzigingen (`appendAttribution: false`)
- MD→HTML formatter in productie testen met echte markdown output van Larry
