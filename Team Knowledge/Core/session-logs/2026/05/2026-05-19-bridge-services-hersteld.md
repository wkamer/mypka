# 2026-05-19 — Bridge services hersteld na integratie-migratie

**session_log_id:** 71
**Agent:** Larry
**Topics:** infrastructure, systemd, bridges, integrations

---

## Samenvatting

Na de migratie van bridge-scripts naar `Team Knowledge/Core/Integrations/` bleken alle drie bridge-services (meta, ai, discord) kapot: de service files verwezen nog naar de oude `/opt/n8n/` locaties. Root cause: systemd kan geen spaties in `EnvironmentFile`-paden aan, ook niet met backslash-escaping. Fix: symlinks aangemaakt op paden zonder spaties (`/etc/mypka-*.env`, `/opt/mypka-*.py`) en service files bijgewerkt. Shell script geschreven voor herhaalbare uitvoering.

---

## Beslissingen

- Vaste fix-strategie voor systemd + paden met spaties: symlink op `/etc/` en `/opt/` niveau, service file verwijst naar symlink.

---

## Acties

- Symlinks aangemaakt voor meta, ai en discord bridge (.env + script)
- Alle drie service files herschreven naar nieuwe paden
- `/tmp/fix_bridges.sh` geschreven voor herhaalbare uitvoering
- Alle drie bridges actief en running bevestigd

## Delegaties

Geen.

---

## Open items

- **Owner actie:** Shopify Custom App aanmaken en `shpat_` token plaatsen in `Team Knowledge/Core/Integrations/shopify/.env` als `SHOPIFY_ADMIN_TOKEN=shpat_...`
