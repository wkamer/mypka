---
description: Sluit de Afternoon Routine af — borgt session log, groei-signaal, delegaties en Goal beweging naar de juiste databases. Geen bevestiging nodig.
allowed-tools: Bash Read Write Edit
---

# /close-afternoon-routine

Voer direct uit zonder bevestiging te vragen. Borgt alles wat tijdens de Afternoon Routine is gedaan.

---

## Database Routing Rule

| Domein | Database |
|---|---|
| Persoonlijk leven, goals, habits | `PKM/personal.db` |
| Kamer E-commerce | `Team Knowledge/Kamer E-commerce/kamer e-commerce.db` |
| Geldstroom Regie | `Team Knowledge/Geldstroom Regie/geldstroom-regie.db` |
| Team operations, delegaties | `Team Knowledge/team-knowledge.db` |

---

## Stap 1 — Borg session log

INSERT in `PKM/personal.db` → `session_logs`:
- `session_date` = vandaag
- `session_title` = "Afternoon Routine"
- `topics` = "routine, afternoon"
- `summary` = Samenvatting van inbox verwerking (X items), delegaties (Y), Highlight status, Goal beweging per goal.
Als er al een Afternoon Routine log voor vandaag bestaat: overslaan.

---

## Stap 2 — Borg delegaties

Voor elke delegatie die tijdens de Afternoon Routine is uitgezet:
- INSERT `team_tasks` rij in de juiste database (routing rule hierboven)
- Velden: `title`, `assignee`, `priority=3`, `source="afternoon-routine"`

Sla over als geen delegaties.

---

## Stap 3 — Borg Goal beweging

UPDATE `PKM/personal.db` → `daily_growth` voor vandaag:
- Zet `afternoon_checkin` = groei-signaal antwoord van de owner
- Als de rij nog niet bestaat: INSERT met datum van vandaag

---

## Afsluiting

Toon een korte ✓-lijst van wat daadwerkelijk is weggeschreven, bijvoorbeeld:
- ✓ session_logs → personal.db (id X)
- ✓ daily_growth.afternoon_checkin → personal.db
- ✓ team_tasks → [database] (X delegaties)

Dan:

> ✅ **Afternoon Routine afgesloten.**
> Type `/compact` om de context te comprimeren voor de volgende sessie.

Daarna: geen verdere output. Sessie is klaar.
