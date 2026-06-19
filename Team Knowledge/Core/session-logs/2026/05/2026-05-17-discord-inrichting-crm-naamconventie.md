# Discord inrichting & CRM naamconventie afronding

**Datum:** 2026-05-17
**Topics:** discord · integratie · CRM · infra
**DB id:** 59

## Samenvatting

Sessie startte met het afronden van de CRM naamconventie (Achternaam, Voornaam.md) en het hernoemen van ruben.md naar Voort, Ruben van der.md. Daarna is de Discord server K'mer Base volledig ingericht: categories Personal en Kamer E-commerce aangemaakt, kanaalstructuur opgeschoond en Voice/Text Channels verwijderd. De mypka-discord-bridge is uitgebreid met DM-ondersteuning zodat Walter direct met de bot kan DM'en. De ai-bridge context header is aangevuld met Discord configuratiedetails. Sessie sloot af met een reflectie op Progression over Perfection als persoonlijk groeiprincipe.

## Beslissingen

- CRM naamconventie vastgesteld: Achternaam, Voornaam.md, tussenvoegsels lowercase na voornaam
- Discord bot behoudt Admin rol tijdens inrichting; myPKA Bot rol krijgt later minimale rechten
- Discord responsesnelheid blijft zo — file system access via Claude Code is de kernwaarde
- Personal staat bovenaan in Discord server structuur

## Acties

- `Voort, Ruben van der.md` aangemaakt, `ruben.md` verwijderd, CRM INDEX bijgewerkt
- Discord categories Personal en Kamer E-commerce aangemaakt met elk #general via API
- Origineel #general, Text Channels, Voice Channels verwijderd via Discord API
- DM support ingebouwd in `mypka-discord-bridge.py`
- ai-bridge context header uitgebreid met Discord integratie info (channel IDs, guild ID, env locatie)
- `mypka-discord-bridge.env` geconfigureerd met nieuwe channel ID (Personal #general)

## Delegaties

- **Penn** — journaal persoonlijke reflectie (Progression over Perfection)

## Open items

- myPKA Bot rol instellen met minimale rechten (na voltooiing inrichting)
- Sienna: feedback Discord snelheid vanuit dagelijks gebruik
- Telegram n8n workflow: `source: "telegram"` toevoegen
- Geldstroom Regie DB: duplicate tasks cleanup
- Personal team task #22: root map hernoemen
