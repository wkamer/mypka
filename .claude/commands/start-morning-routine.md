---
description: Start de dagelijkse Morning Routine — Brain Zen, Miracle Roadmap, inbox en sessie context. Goal check en Highlight → /start-daily-planning.
allowed-tools: Bash Read Write Edit mcp__todoist__get_tasks_list mcp__todoist__update_tasks mcp__todoist__get_tasks mcp__todoist__create_tasks
---

# /start-morning-routine

Begeleid de owner door de Morning Routine. Stap voor stap, wacht op input waar gevraagd. KISS.

Toon eerst dit overzicht:

> **Morning Routine**
> 1. 🧠 Brain Zen — hoofd leegmaken
> 2. 🗺️ Miracle Roadmap — voortgang bijhouden
> 3. 📥 Sessie context — laatste log + inboxen + open taken
> 4. 📅 Planning check — highlight bevestigen of alsnog plannen voor vandaag

Dan direct beginnen met Stap 0.

---

## Stap 0 — Consistentiecheck vorige routine

Query `PKM/personal.db` → `session_logs`:
```sql
SELECT id, summary FROM session_logs
WHERE session_date = date('now', '-1 day') AND session_title = 'End-of-Day Routine'
LIMIT 1;
```

**Gevonden:** kort benoemen — "Gisteren netjes afgesloten." Ga door naar Stap 1.

**Niet gevonden:** reflecteer kort en open:
- Benoem dat de End-of-Day Routine gisteren niet is afgesloten.
- Vraag: "Wat hield je gisteren tegen — geen tijd, vergeten, of voelde het niet zinvol?"
- Wacht op antwoord. Log het antwoord als `open_items` in een korte `session_logs` rij met `session_title = 'End-of-Day Routine — gemist'`, `session_date = gisteren`, en `summary = antwoord van de owner`.
- Ga daarna gewoon door met de Morning Routine. Geen oordeel, geen herhaling.

---

## Stap 1 — Brain Zen

Vraag: "Wat zit er in je hoofd? Dump het hier."

Wacht op input. Voor elke taak die erin zit:
1. Schat in: **Speedy** (<15 min) of **Task** (15 min – 3 uur)
2. Toon voorstel: "→ [taaknaam] — Speedy / Task (reden)"
3. Wacht op bevestiging van de owner (ja / corrigeer)
4. Maak aan in Todoist `👤 PERSONAL`. Bij Speedy: voeg label `speedy` toe.

Zeg daarna: "Hoofd leeg."

---

## Stap 1b — Miracle Roadmap voortgang

Bereken de norm van vandaag: **84 + aantal dagen sinds 10 mei 2026**.

Vraag: "Miracle Roadmap — norm vandaag: les [X]. Op welke les sta je?"

Wacht op antwoord. Toon kort: "Stand: les [Y] van norm [X]. [Achterstand / Op schema / Voor]."

Geen discussie. Gewoon registreren en door.

---

## Stap 2 — Sessie context en open taken

Haal recente context op uit `PKM/personal.db`:

```python
import sqlite3

conn = sqlite3.connect('/opt/myPKA/PKM/personal.db')
c = conn.cursor()
c.execute('''SELECT session_date, session_title, summary
             FROM session_logs
             ORDER BY session_date DESC, id DESC
             LIMIT 3''')
for row in c.fetchall():
    print(f"{row[0]} — {row[1]}: {(row[2] or '')[:120]}")
conn.close()
```

Check alle inboxen:
- `Team Inbox/Personal/` — nieuwe bestanden?
- `Team Inbox/Kamer E-commerce/` — nieuwe bestanden?
- `Team Inbox/Geldstroom Regie/` — nieuwe bestanden?
- Todoist Inbox — losse items om te routeren

Open `team_tasks` in `PKM/personal.db` — wat loopt er nog?

Rapporteer in max 5 regels. Geen uitgebreide analyse. Laad nooit volledige session logs — gebruik expand_summary(id) alleen als de owner specifiek vraagt naar een eerdere sessie.

---

## Stap 3 — Daily Planning check

Check of er een taak bestaat met label `highlight` en Due Date vandaag in Todoist.

**Highlight gevonden:** benoem hem kort — "⭐ [taaknaam] is je Highlight van vandaag." Vraag: "Klopt deze planning nog, of is er reden om bij te stellen?"

**Geen highlight:** benoem dat er geen geldige planning staat voor vandaag. Voer `/start-daily-planning` uit voor vandaag. Gebruik dezelfde stappen maar met datum van vandaag in plaats van morgen.

---

## Afsluiting

Zeg: "Type `/close-morning-routine` om de Morning Routine af te sluiten en alles weg te schrijven."
