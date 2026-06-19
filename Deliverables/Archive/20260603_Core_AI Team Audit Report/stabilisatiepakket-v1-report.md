# Stabilisatiepakket v1 Report

**Datum:** 2026-06-03
**Uitgevoerd door:** Larry (B-002, B-004), Kai (B-001, B-008 plan), Nolan (B-003)
**Basis:** Walter's akkoord Stabilisatiepakket v1

---

## 1. Wat is uitgevoerd?

| Item | Status | Uitvoerder |
|---|---|---|
| B-001 Database backup activeren | ✓ Uitgevoerd | Kai |
| B-002 GL nummering conflict oplossen | ✓ Uitgevoerd | Larry |
| B-003 Finn routing corrigeren | ✓ Uitgevoerd | Nolan |
| B-004 Governance concept opstellen | ✓ Concept gereed | Larry |
| B-008 agent_slug migratiePlan | ✓ Plan gereed | Kai |

---

## 2. Welke bestanden zijn aangepast?

**B-001 — Nieuwe scriptbestanden:**
- `Team Knowledge/Core/Integrations/memory-db/backup_memory_db.sh` (nieuw)
- `Team Knowledge/Core/Scripts/backup_sqlite_dbs.sh` (nieuw)
- `Team Knowledge/Core/Integrations/n8n/backup_n8n.sh` (nieuw)

**B-002 — Hernoemd:**
- `GL-002_ChatGPT prompt ICOR module-verwerking.md` → `GL-012_ChatGPT prompt ICOR module-verwerking.md`
- `GL-010_Memory Core Architecture.md` → `GL-013_Memory Core Architecture.md`

**B-002 — Bijgewerkt (interne verwijzingen):**
- `Team Knowledge/Core/Guidelines/gl-index.md` — volledig bijgewerkt met correcte nummering + omschrijvingen
- `Team Knowledge/Core/SOPs/SOP-007_Memory Core operaties.md` — verwijzing GL-010 → GL-013
- `Team Knowledge/Core/Integrations/service-catalog.md` — verwijzing GL-010 → GL-013

**B-003 — Bijgewerkt:**
- `Team/Finn - The WordPress Specialist/AGENT.md` — routing-regel gecorrigeerd + changelog toegevoegd

**B-004 — Nieuw (concept):**
- `Deliverables/20260603_Core_AI Team Audit Report/GL-014-concept-AI-Team-Governance.md`

**B-008 — Nieuw (plan):**
- `Deliverables/20260603_Core_AI Team Audit Report/B-008-agent-slug-migration-plan.md`

---

## 3. Welke technische wijzigingen zijn gedaan?

**B-001 — Cron-entries toegevoegd (3):**
```
30 2 * * *  backup_sqlite_dbs.sh       — SQLite backup alle 4 databases
45 2 * * *  backup_n8n.sh              — n8n-postgres pg_dump
0  3 * * *  backup_memory_db.sh        — memory-db pg_dump
```

**Geen database schema-wijzigingen uitgevoerd.**
**Geen bestanden verwijderd.**

---

## 4. Welke backups zijn actief?

| Backup | Script | Frequentie | Doel | Bewaren |
|---|---|---|---|---|
| SQLite (4 databases) | `backup_sqlite_dbs.sh` | Dagelijks 02:30 | `/home/admin/backups/sqlite/YYYYMMDD/` | 7 sets |
| n8n-postgres | `backup_n8n.sh` | Dagelijks 02:45 | `/home/admin/backups/n8n/` | 7 dumps |
| memory-db pg_dump | `backup_memory_db.sh` | Dagelijks 03:00 | `/home/admin/backups/memory-db/` | 7 dumps |
| Lokale rsync snapshot | `local-backup.sh` (bestaand) | Dagelijks 02:00 | `/home/admin/backups/myPKA/YYYYMMDD/` | 30 sets |
| Google Drive sync | `sync.sh` (bestaand) | Elke 5 min | gdrive:myPKA | Permanent |

**Smoke tests uitgevoerd door Kai:** alle 3 nieuwe scripts succesvol gerund. Dumps aangemaakt en controleerbaar.

---

## 5. Welke checks zijn uitgevoerd?

- GL-map na hernoemen gecontroleerd: nummering uniek, geen dubbelen meer
- Interne verwijzingen naar oude GL-nummers opgezocht en bijgewerkt (2 bestanden)
- Finn AGENT.md gecheckt: routing-schending verwijderd, changelog aanwezig
- Backup smoke tests door Kai: pg_dump memory-db (4.9M), SQLite 4x, n8n-postgres (34M)
- GL-index bijgewerkt met alle 13 GLs (correct genummerd)

---

## 6. Welke risico's blijven open?

| Risico | Status | Toelichting |
|---|---|---|
| Bridges als onbeheerde processen | Open (B-006) | Discord-bridge en ai-bridge nog geen Docker — niet in scope Fase 1 |
| n8n volume backup | Actief (script) | Script aangemaakt maar volume backup via `pg_dump` — geen volume snapshot. Volledig herstel vereist ook workflow re-import. |
| agent_slug migratie | Plan gereed | SQL plan klaar, wacht op Walter's akkoord voor uitvoering |
| Workstreams ontbreken | Open (B-005) | Niet in scope Fase 1 |
| Leerloop niet battle-tested | Open (B-015) | Niet in scope Fase 1 |
| rclone token niet zelfcontained | Open | Laag risico, niet in scope |
| Integratie SOPs (9 van 11) | Open (B-012) | Niet in scope Fase 1 |

**Security note:** Kai heeft 3 cron-entries toegevoegd. Dit was binnen de scope van B-001 (database backup activeren). De entries zijn alleen backup-scripts — geen data-wijziging, geen externe API-calls.

---

## 7. Welke onderdelen wachten nog op Walter's akkoord?

| Item | Wat wacht | Document |
|---|---|---|
| B-008 agent_slug | SQL uitvoeren | `B-008-agent-slug-migration-plan.md` |
| B-004 Governance | Document authoritative maken (GL-014) | `GL-014-concept-AI-Team-Governance.md` |
| B-005 Workstreams | Start Fase 2 | Audit rapport §8 |
| Fase 2 overall | Rollen aanscherpen (B-017 t/m B-020) | Audit rapport §11 |

---

## 8. Aanbevolen volgende stap

**Onmiddellijk (geen nieuwe approval nodig):**
- Verifieer de backup-scripts door morgen de `/home/admin/backups/` map te controleren

**Volgende approval-ronde:**
1. **B-008 akkoord:** agent_slug migratie uitvoeren (laag risico, plan is gereed)
2. **GL-014 akkoord:** governance concept authoritative maken
3. **Fase 2 akkoord:** AGENT.md kwaliteitsverbeteringen (B-017 t/m B-020)

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/stabilisatiepakket-v1-report.md`*
