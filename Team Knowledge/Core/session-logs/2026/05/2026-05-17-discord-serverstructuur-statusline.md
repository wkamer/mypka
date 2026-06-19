# Discord serverstructuur & Claude Code statusline

**Datum:** 2026-05-17
**Topics:** discord · infra · claude-code
**DB id:** 60

## Samenvatting

Discord server K'mer Base volledig ingericht: categorie-volgorde gefixet via API, Voice Channels verwijderd, en DM-ondersteuning toegevoegd aan de mypka-discord-bridge. De ai-bridge context header is uitgebreid zodat Claude proactief Discord channel IDs en bot token kan vinden. Daarnaast is de Claude Code statusline geconfigureerd via een extern script met progress bars, token gebruik, percentages en reset-tijden voor zowel het 5h blok als de 7d weekly limit, met kleurcodering (groen/oranje/rood).

## Beslissingen

- Discord bot houdt Admin rol tijdens inrichting; myPKA Bot krijgt later minimale rechten
- Statusline als extern script (`~/.claude/hooks/statusline.sh`) i.p.v. inline one-liner

## Acties

- Discord categories/channels aangemaakt en geordend via Discord API
- DM support ingebouwd in `mypka-discord-bridge.py`
- `/home/admin/.claude/hooks/statusline.sh` aangemaakt
- `/home/admin/.claude/settings.json` bijgewerkt met statusLine verwijzing naar script

## Open items

- myPKA Bot rol minimale rechten instellen (na voltooiing inrichting)
- Sienna: feedback Discord snelheid vanuit dagelijks gebruik
- Telegram n8n workflow: `source: "telegram"` toevoegen
- Geldstroom Regie DB: duplicate tasks cleanup
