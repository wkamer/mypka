---
description: Sluit de Morning Routine af — borgt session log en Miracle Roadmap stand naar personal.db. Geen bevestiging nodig.
allowed-tools: Bash Read Write Edit
---

# /close-morning-routine

Voer direct uit zonder bevestiging te vragen. Borgt alles wat tijdens de Morning Routine is gedaan.

---

## Stap 1 — Borg session log

Stel de summary samen: Brain Zen items (taken aangemaakt), Miracle Roadmap stand (les X van norm Y).

INSERT in `PKM/personal.db` → `session_logs`:

```python
import sqlite3
from datetime import date

conn = sqlite3.connect('/opt/myPKA/PKM/personal.db')
c = conn.cursor()
c.execute('''INSERT OR IGNORE INTO session_logs
    (session_date, session_title, topics, summary, agent_slug)
    VALUES (?, ?, ?, ?, ?)''', (
    str(date.today()), 'Morning Routine', 'routine, morning',
    '<samenvatting>', 'larry'
))
conn.commit()
print('OK, id:', c.lastrowid)
conn.close()
```

Als er al een Morning Routine log voor vandaag bestaat: overslaan.

---

## Stap 2 — Borg Miracle Roadmap stand

UPDATE `PKM/personal.db` → `daily_growth` voor vandaag:
- Zet `miracle_roadmap_les` = de les waarop de owner staat (uit de Morning Routine)
- Als de rij nog niet bestaat: INSERT met datum van vandaag

---

## Stap 3 — Sweep Brain Zen items

Controleer of alle Brain Zen items uit deze sessie als taak in Todoist staan of als Calendar event zijn aangemaakt. Zo niet: alsnog aanmaken zonder te vragen.

---

## Afsluiting

Toon een korte ✓-lijst van wat daadwerkelijk is weggeschreven, bijvoorbeeld:
- ✓ session_logs → personal.db (id X)
- ✓ daily_growth.notes (Miracle Roadmap les X/norm Y) → personal.db
- ✓ Brain Zen sweep: [X taken in Todoist, Y events in Calendar]

Dan:

> ✅ **Morning Routine afgesloten.**
> Type `/compact` om de context te comprimeren voor de volgende sessie.

Daarna: geen verdere output. Sessie is klaar.
