# 2026-05-19 — Integrations folder + credentials migratie

**session_log_id:** 70
**Agent:** Larry
**Topics:** integraties, credentials, infrastructure, shopify

---

## Samenvatting

Shopify Custom App permissions besproken (alle scopes aanzetten). Kai ontworpen en uitgevoerd: `Team Knowledge/Core/Integrations/` opgezet als canonical locatie voor alle integratie-configuratie en credentials. Google OAuth credentials verplaatst van myPKA root naar `Integrations/google/`. `todoist_helper.py` gebouwd; Todoist token verwijderd uit 16 scripts en uit `settings.json` -- token leeft nu in `Integrations/todoist/.env`. `shopify_helper.py` aangepast om uit `Integrations/shopify/.env` te lezen. GL-004 bijgewerkt met alle nieuwe paden en credential-regel. `settings.json` heeft geen credentials meer.

---

## Beslissingen

- `.env` per integratie-folder is de standaard voor alle credentials
- `~/.claude/settings.json` bevat geen credentials meer -- alleen Claude Code infrastructuur
- Shopify token komt in `Integrations/shopify/.env` zodra Custom App is aangemaakt

---

## Acties

- Kai: `Team Knowledge/Core/Integrations/` mapstructuur aangemaakt met templates en config.md per integratie
- Google OAuth credentials verplaatst van myPKA root naar `Integrations/google/`
- `todoist_helper.py` geschreven — leest token uit `Integrations/todoist/.env`
- 16 Todoist-scripts bulk-updated (hardcoded token vervangen door `get_token()`)
- `shopify_helper.py` bijgewerkt — leest uit `Integrations/shopify/.env`
- `google_helper.py` padupdate naar nieuwe locatie
- GL-004 bijgewerkt met alle nieuwe Integrations-paden en credential-regel

## Delegaties

- Kai gedelegeerd voor Integrations folder ontwerp en uitvoering

---

## Open items

- **Owner actie:** Shopify Custom App aanmaken in Shopify Admin en `shpat_` token plaatsen in `Team Knowledge/Core/Integrations/shopify/.env` als `SHOPIFY_ADMIN_TOKEN=shpat_...`
