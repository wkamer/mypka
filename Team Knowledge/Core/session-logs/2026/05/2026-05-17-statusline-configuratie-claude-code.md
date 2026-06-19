# Statusline configuratie Claude Code

**Datum:** 2026-05-17
**Agent:** Larry
**DB id:** 63
**Topics:** infrastructure, claude-code, statusline, debugging

## Samenvatting

Sessie gericht op het instellen van een custom statusline in de Claude Code console met token verbruik en weekly limit. Script aangemaakt op `~/.claude/statusline-command.sh` en gekoppeld via `settings.json`. Ontdekt dat `jq` niet geinstalleerd is op de Raspberry Pi; script herschreven met Python als parser. Docs geraadpleegd om de correcte config-structuur te bevestigen. Claude Code herstart nodig om de config te activeren; `rate_limits` veld alleen beschikbaar voor Pro/Max subscribers.

## Beslissingen

- Script gebruikt Python ipv jq voor JSON parsing
- Statusline toont: `tokens: X.Xk | week: X%`
- Config staat in user settings (`~/.claude/settings.json`)

## Acties

- `statusline-command.sh` aangemaakt en meerdere keren herschreven
- `settings.json` bijgewerkt met `statusLine` config
- Claude Code docs geraadpleegd voor juiste configuratie

## Delegaties

Geen.

## Open items

- Bevestigen dat statusline zichtbaar is na herstart
- Controleren of `rate_limits` beschikbaar is (Pro/Max vereist)
