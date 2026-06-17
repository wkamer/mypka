---
description: Sluit de dag volledig af — session logs, delegaties, sweep, SOP check, DR check, deliverables archiveren, mirror naar markdown. Vervangt /close-the-day. Geen bevestiging nodig.
allowed-tools: Bash Read Write Edit mcp__todoist__get_tasks_list mcp__todoist__update_tasks mcp__todoist__close_tasks
---

# /close-end-of-day-routine

Voer direct uit zonder bevestiging te vragen. Borgt alles wat vandaag is gedaan.

---

## Database Routing Rule

| Domein | Database |
|---|---|
| Team operations, delegaties, learnings | `Team Knowledge/team-knowledge.db` |
| Persoonlijk leven, goals, habits | `PKM/personal.db` |
| Kamer E-commerce | `Team Knowledge/Kamer E-commerce/kamer e-commerce.db` |
| Geldstroom Regie | `Team Knowledge/Geldstroom Regie/geldstroom-regie.db` |

---

## Stap 1 — Session logs

Bepaal welke databases van toepassing zijn op basis van wat er vandaag is gedaan. INSERT één `session_logs` rij per relevante database:

| Veld | Toelichting |
|---|---|
| `session_date` | vandaag |
| `session_title` | korte beschrijvende titel |
| `topics` | 2–4 kommagescheiden tags |
| `summary` | 3–5 zinnen: wat gedaan, besluiten, opgeleverd |
| `decisions` | bullet lijst |
| `actions_taken` | bullet lijst |
| `delegations` | specialist + taak, of "Geen" |
| `open_items` | onopgeloste threads |
Sla bestaande logs voor vandaag over.

---

## Stap 2 — Delegaties borgen

Voor elke delegatie van vandaag, INSERT in `/opt/myPKA/Team Knowledge/team-knowledge.db`:
- `agent_learnings`: `agent_slug`, `what_worked`, `what_to_improve`, `session_log_id`
- `delegation_outcomes`: `to_agent`, `brief_summary`, `outcome`, `session_log_id`

Sla over als geen delegaties.

---

## Stap 3 — Team learning

Als er een nieuw patroon of team-niveau inzicht is: INSERT één `team_log` rij in `/opt/myPKA/Team Knowledge/team-knowledge.db`:
`entry_type = "learning"`, `content` = één zin.

Sla over als niets noemenswaardigs.

---

## Stap 3b — Borg sessie naar Unified Memory Core

Roep het verificatiescript aan via Bash voor elke session_log die zojuist is aangemaakt:

```bash
/opt/mypka-memory/venv/bin/python '/opt/myPKA/Team Knowledge/Core/Scripts/close_routine_verification.py' \
    --session-date <YYYY-MM-DD> \
    --session-title "<session_title>" \
    --summary "<samenvatting>" \
    --domain <personal|team|ke|gr> \
    --topics "<topics>" \
    --db <personal|team|ke|gr>
```

Lees de JSON output:
- `session_log.ok: true` → ✓ session_logs → [db] (id X)
- `session_log.skipped: true` → ✓ session_logs → al aanwezig (id X)
- `umc.ok: true` → ✓ UMC → memory_summaries (id X)
- Elk veld met `ok: false` → ⚠️ [stap]: [error] in de afsluitlijst

---

## Stap 3c — Context compactie via UMC

Na Stap 3b: als `umc.ok: true`, activeer context compactie:

```python
# Interpreter: /opt/mypka-memory/venv/bin/python
import sys, os
sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
from memory_config import get_dsn
os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
from memory_manager import get_manager
mm = get_manager()

session_id = "<YYYY-MM-DD>-end-of-day"
context_snapshot = "<samenvatting van de huidige sessie-inhoud: wat gedaan, besluiten, open items>"
compact_ref, summaries = mm.offload_to_summary(context_snapshot)
if summaries:
    print(f"[UMC compactie] Summary ID: {summaries[0]['id']} — {summaries[0]['description']}")
else:
    print("[UMC compactie] Context onder drempelwaarde — geen compactie nodig.")
```

Gebruik `compact_ref` als referentie in de rest van de sessie, niet de volledige snapshot.

---

## Stap 4 — Sweep open items

Voor elk onopgelost thread of follow-up: INSERT één `team_tasks` rij in de juiste database:
`title`, `assignee` (of NULL), `priority=3`, `source="sweep"`.

---

## Stap 5 — Mirror session logs

Mirror elke session log van vandaag naar:
`Team Knowledge/Core/session-logs/YYYY/MM/YYYYMMDD_<slug>.md`

Maak de map aan als die nog niet bestaat.

---

## Stap 6 — Archiveer reviewed Deliverables

Check `Deliverables/` op submappen die als reviewed zijn gemarkeerd. Verplaats naar `Deliverables/Archive/`.

---

## Stap 7 — SOP check

Als er vandaag een nieuw herhaalbaar proces is ontstaan: maak een SOP-bestand aan in de juiste domein-SOPs-map. Schrijf zonder te vragen.

---

## Stap 8 — Disaster Recovery check

Triggers (één is genoeg):
- Nieuw plugin, MCP server of CLI tool geïnstalleerd
- Nieuwe API key of credential toegevoegd
- settings.json of .mcp.json gewijzigd
- Nieuw slash command aangemaakt
- Nieuwe hook geconfigureerd

Zo ja: open `Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md`, update de relevante stap(pen) en de *Last updated* regel. Schrijf zonder te vragen.

Zo nee: stil overslaan.

---

## Afsluiting

Toon een korte ✓-lijst van wat er is weggeschreven (databases, bestanden, mirrors). Dan:

> ✅ **Dag afgesloten.**
> Type `/clear` om de context te wissen en de console open te houden.

Daarna: geen verdere output. Sessie is klaar.
