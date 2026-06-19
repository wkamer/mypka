# AI Team Audit Report
**Datum:** 2026-06-03
**Uitgevoerd door:** Larry (orchestratie + SSOT/governance), Nolan (AGENT.md kwaliteit), Kai (technisch), Marcus (workflow + planning)
**Status:** Concept — wacht op Walter's review en akkoord
**Versie:** v0.1

---

## 1. Executive Summary

Het myPKA AI-team bestaat uit 15 goed gedocumenteerde specialisten met duidelijke rollen en een functionerende orchestratielaag. De kerninfrastructuur werkt. De fundamenten zijn gelegd voor een zelflerend team (session logs, agent journals, graduation candidates, task discipline).

Vier kritieke problemen vereisen prioritaire aandacht:

1. **Geen actieve database backup** — geen enkele cron voor pg_dump of SQLite backup is actief. Productieverlies bij hardware failure.
2. **Geen Workstreams** — de Workstreams-map bestaat niet terwijl CLAUDE.md ernaar verwijst en 10 terugkerende multi-agent processen kwalificeren.
3. **GL-nummering conflict** — GL-002 en GL-010 bestaan elk dubbel. Agents weten niet welke authoritative is.
4. **Finn's routing bypasses Larry** — Finn stuurt scope-vragen naar Vera i.p.v. Larry, wat de Iron Rule schendt.

De leerinfrastructuur is structureel aanwezig maar nog niet battle-tested: agent journals zijn leeg, `linked_journal_entries` is nooit gebruikt, graduation candidates zijn nog niet opgepakt.

---

## 2. Huidige situatie

### Agents
15 specialisten, volledig gedocumenteerd in `Team/agent-index.md`. Subagent shims aanwezig in `.claude/agents/`. Alle AGENT.md bestanden bevatten Task Discipline sectie (toegevoegd 2026-06-03).

### SOPs
9 aanwezig: SOP-001 (DR), SOP-002 (Research), SOP-003 (Hiring), SOP-005 (Tasks), SOP-006 (Projects), SOP-007 (Memory), SOP-008 (Read journal), SOP-009 (Write journal), SOP-012 (Daily Planning), SOP-013 (365 Academy). Gaps: SOP-004, SOP-010, SOP-011 ontbreken; Routines, Governance en meerdere integraties hebben geen SOP.

### Guidelines
11 bestanden, maar GL-002 en GL-010 bestaan elk dubbel — numbering conflict. Geen gl-index met authoritatieve nummering.

### Workstreams
**Geen.** De map `/opt/myPKA/Team Knowledge/Core/Workstreams/` bestaat niet. CLAUDE.md verwijst er naar als bestaande laag.

### Leerinfrastructuur
- 121 session logs (4 met NULL titel)
- 39 agent_learnings rijen in team-db, 7 in personal-db
- `delegation_outcomes` tabel: 0 rijen (nooit gevuld)
- Agent journals: mappen aangemaakt, templates aanwezig, 0 echte entries
- `linked_journal_entries`: kolom aanwezig in alle team_tasks tabellen, nooit gebruikt
- Graduation candidates: stap toegevoegd aan close-session (2026-06-03), nooit uitgevoerd

### Integraties
Actief: memory-db, rclone (one-way sync), dropbox (cron), whisper (cron), n8n, cloudflared, discord-bridge, ai-bridge, Ollama.
SOP/Runbook aanwezig: memory-db (SOP-007), whisper (runbook). 9 van 11 integraties zonder SOP.

### Logging
Session logs: aanwezig maar 4 NULL titels. `agent_learnings`: gevuld maar niet systematisch. `team_log`: sporadisch. `delegation_outcomes`: leeg. Audit trail voor AGENT.md wijzigingen: geen.

### Governance
Geen formeel governance-document. Regels staan verspreid over CLAUDE.md, Larry AGENT.md en memory. Geen approval-tracking voor kritieke wijzigingen.

---

## 3. Belangrijkste risico's

| Risico | Categorie | Classificatie | Beschrijving |
|---|---|---|---|
| Geen actieve database backup | Technisch | **Hoog** | pg_dump cron ontbreekt; SQLite backup niet crash-safe; n8n volume onbeschermd |
| Finn bypasses Larry routing | Rolconflict / Governance | **Hoog** | Finn stuurt scope-vragen naar Vera i.p.v. Larry — schending Iron Rule |
| GL-002 en GL-010 dubbel | SSOT | **Hoog** | Agents weten niet welke GL authoritative is; conflicterende conventies |
| Geen Workstreams | Ontbrekende structuur | **Hoog** | 10 terugkerende multi-agent processen ongeborgd; CLAUDE.md verwijst naar non-existent laag |
| Geen governance-document | Governance | **Hoog** | Geen formele borging van approval-gates; regels in CLAUDE.md maar niet als aparte authoritative bron |
| Bridges als onbeheerde processen | Technisch | **Medium** | Discord-bridge en ai-bridge als losse python3, geen Docker, geen auto-restart |
| n8n zonder backup | Technisch | **Medium** | Alle n8n credentials en workflows verloren bij volume-verlies |
| agent_slug schema-inconsistentie | Technisch | **Medium** | Halverwege migratie — personal.db en kamer-ecommerce.db missen kolom |
| Leerloop niet battle-tested | Ongecontroleerde zelflerendheid | **Medium** | Journals leeg, linked_journal_entries nooit gebruikt, graduation nooit uitgevoerd |
| Routines alleen als skills | Ontbrekende SOPs | **Medium** | Morning/Afternoon/End-of-Day Routine geen SOP-borging; skills kunnen veranderen zonder procedurele basis |
| Delegation_outcomes nooit gevuld | Logging | **Medium** | Tabel bestaat, 0 rijen in personal.db; geen audit trail voor delegaties |
| Knowledge Currency niet geactiveerd | Audit trail | **Laag** | Aanwezig in AGENT.md's maar Larry monitort niet actief of ververstermijnen verlopen zijn |
| Larry mist Samenwerking-sectie | SSOT | **Laag** | Larry schrijft Samenwerking verplicht voor anderen maar heeft hem zelf niet |
| Bo is dunste AGENT.md | Kwaliteit | **Laag** | Knowledge Currency, Task Discipline en UMC ontbreken bij Bo |

---

## 4. Gap Analysis

| Onderdeel | Huidige situatie | Gewenste situatie | Gap | Prioriteit |
|---|---|---|---|---|
| Database backup | Geen actieve cron | pg_dump + SQLite backup dagelijks actief | Cron aanmaken, testen, monitoren | **Hoog** |
| Workstreams | Map bestaat niet, 0 bestanden | 8-10 WS bestanden voor terugkerende multi-agent processen | Volledige laag aanmaken | **Hoog** |
| GL nummering | GL-002 en GL-010 dubbel | Unieke nummering, gl-index authoritative | Hernoem/archiveer dubbele bestanden, update index | **Hoog** |
| Governance-document | Verspreid over CLAUDE.md + memory | Eén GL of SOP met approval-gates, escalation rules, audit trail | GL-012 of SOP-010 aanmaken | **Hoog** |
| Finn routing | Scope-vragen naar Vera | Alle scope-vragen via Larry | Finn AGENT.md corrigeren | **Hoog** |
| Routines als SOP | Skills only | SOP-010/011 voor Morning/End-of-Day Routine | SOPs aanmaken | **Medium** |
| Leerloop activeren | Structuren aanwezig, nooit gebruikt | Agent journals met echte entries, graduation opgepakt | Eerste echte journals schrijven, graduation review inrichten | **Medium** |
| delegation_outcomes | Tabel leeg | Gevuld bij elke delegatie | SOP-005 updaten; Larry invullen bij elke delegatie | **Medium** |
| agent_slug migratie | Halverwege | Consistent in alle 4 databases | ALTER TABLE op personal.db en kamer-ecommerce.db | **Medium** |
| Bridges in Docker | Losse processen | Docker Compose met restart, health check | docker-compose.yml schrijven | **Medium** |
| n8n backup | Geen | Dagelijkse volume backup | local-backup.sh uitbreiden | **Medium** |
| Integratie SOPs | 2 van 11 | Alle kritieke integraties gedocumenteerd | Runbooks voor n8n, cloudflared, dropbox | **Medium** |
| "Never Does" secties | 5 agents missen het | Alle agents hebben expliciete grenzen | AGENT.md updates voor Marcus, Sienna, Penn, Pax, Nolan | **Laag** |
| Knowledge Currency | 4 agents missen het | Alle agents hebben KC sectie | AGENT.md updates voor Marcus, Sienna, Penn, Bo | **Laag** |
| Larry Samenwerking-sectie | Ontbreekt | Aanwezig zoals bij andere agents | Larry AGENT.md updaten | **Laag** |
| Bo AGENT.md versterken | Dun | Task Discipline + UMC aanwezig | Bo AGENT.md updaten | **Laag** |

---

## 5. Rollenmatrix

| Agent | Huidige rol | Eigenaarschap | Overlap met | Aanbevolen wijziging |
|---|---|---|---|---|
| Larry | Orchestrator, governance, SSOT | Session logs, team routing, weekly sweep | Marcus (taken), Nolan (AGENT.md) | Samenwerking-sectie toevoegen |
| Nolan | HR, talent acquisition, AGENT.md kwaliteit | Specialist onboarding, AGENT.md schrijven | Larry (admin) | Knowledge Currency sectie toevoegen |
| Pax | Deep research | Research output | Nolan (hiring brief) | Formele Never Does sectie toevoegen |
| Kai | Infrastructure + integraties | Technische laag, databases, scripts | Larry (admin) | Formele Never Does sectie |
| Penn | Journal writing, PKM capture | Journal entries, entiteiten | Sienna (persoonlijk domein routing) | Knowledge Currency toevoegen |
| Sienna | Personal assistant, inbox | Persoonlijke executie | Penn (journaal) | Knowledge Currency toevoegen |
| Lena | Health coaching | Health habits en ritme | Marcus (routines) | — (sterk AGENT.md) |
| Marcus | Project + task management | Daily Planning, project lifecycle | Larry (Goal Commitment, team_tasks) | Goal-drempel afstemmen met Larry (3 vs 5 dagen) |
| Vera | Portfolio business manager | Venture richting | Finn (richting via Vera ipv Larry), Nova/Sasha/Zara/Remy (uitvoering) | Finn-routing corrigeren |
| Sasha | Shopify specialist | Tricolarae store | Nova (operations), Vera (strategie) | Never Does sectie |
| Nova | E-commerce operations | SOP-driven dagelijkse ops | Remy (product), Sasha (store) | Never Does sectie |
| Zara | Ads intelligence | Meta/TikTok campagnes | Nova (margins), Remy (products) | — (sterk AGENT.md) |
| Remy | Product intelligence | Product scoring en selectie | Nova, Sasha, Zara, Bo | Never Does sectie |
| Bo | Market validator | Go/no-go aanbevelingen | Vera (strategie), Zara (go-signaal) | AGENT.md versterken (KC, TD, UMC) |
| Finn | WordPress specialist | Geldstroom Regie site | Kai (integraties), Vera (richting) | **Routing fix: Vera → Larry bij scope-vragen** |

---

## 6. SOP-analyse

| SOP | Status | Probleem | Actie | Prioriteit |
|---|---|---|---|---|
| SOP-001 Disaster Recovery | Aanwezig | pg_dump cron in SOP beschreven maar niet actief | Kai: cron activeren | Hoog |
| SOP-002 Deep Research | Aanwezig | — | — | OK |
| SOP-003 Hiring | Aanwezig | — | — | OK |
| SOP-004 | Ontbreekt | Gat in nummering | Toewijzen of reserved markeren | Laag |
| SOP-005 Task Management | Aanwezig | Marcus niet bij naam als eigenaar; Larry/Marcus grens impliciet | Update: eigenaar expliciet benoemen | Medium |
| SOP-006 Project Management | Aanwezig | "Gepauzeerd" fase ontbreekt; health check niet geborgd; project-index paden incorrect | Update: fase toevoegen, paden corrigeren | Medium |
| SOP-007 Memory Core | Aanwezig | pg_dump backup beschreven maar cron niet actief | Kai: cron activeren | Hoog |
| SOP-008 Read journal | Aanwezig (nieuw) | Nooit in gebruik genomen | Activeren via eerste echte delegaties | Medium |
| SOP-009 Write journal | Aanwezig (nieuw) | Nooit in gebruik genomen | Activeren via eerste echte delegaties | Medium |
| SOP-010 | Ontbreekt | Morning Routine niet als SOP geborgd | Nieuw schrijven | Medium |
| SOP-011 | Ontbreekt | End-of-Day Routine niet als SOP geborgd | Nieuw schrijven | Medium |
| SOP-012 Daily Planning | Aanwezig | Goal Commitment Rule niet opgenomen; referentie naar feedback-regels ontbreekt | Update: Goal Commitment toevoegen | Laag |
| SOP-013 365 Academy | Aanwezig | — | — | OK |
| SOP-Governance | Ontbreekt | Geen SOP voor AI Team Governance (approval, audit trail, changelog) | Nieuw schrijven als SOP-010 of GL-012 | Hoog |

---

## 7. Guideline-analyse

| Guideline | Status | Conflict | Actie | Prioriteit |
|---|---|---|---|---|
| GL-001 File naming conventions | Aanwezig | — | — | OK |
| GL-002 ChatGPT prompt ICOR | Aanwezig | **Dubbel nummer** | Hernoemen naar GL-012 of archiveren | **Hoog** |
| GL-002 Frontmatter conventions | Aanwezig | **Dubbel nummer** | Dit is de authoritative GL-002 — behoudt nummer | **Hoog** |
| GL-003 Email setup | Aanwezig | — | — | OK |
| GL-004 Canonical paths | Aanwezig | — | — | OK |
| GL-005 AI Engineering OS | Aanwezig | — | — | OK |
| GL-006 Notification Format | Aanwezig | — | — | OK |
| GL-007 Integration naming | Aanwezig | — | — | OK |
| GL-008 WhatsApp borging | Aanwezig | — | — | OK |
| GL-009 CRM link consistency | Aanwezig | — | — | OK |
| GL-010 Memory Core Architecture | Aanwezig | **Dubbel nummer** | Hernoemen naar GL-013 | **Hoog** |
| GL-010 Session logs purpose | Aanwezig | **Dubbel nummer** | Dit is de authoritative GL-010 — behoudt nummer | **Hoog** |
| GL-011 Project documentation | Aanwezig | — | — | OK |
| gl-index.md | Aanwezig | Niet up-to-date met nieuwe GLs | Update toevoegen na nummering fix | Medium |

**Besluit nodig:** Wat gebeurt er met GL-002 ChatGPT prompt? Is deze nog relevant of te archiveren?

---

## 8. Workstream-voorstel

**Map aan te maken:** `Team Knowledge/Core/Workstreams/`

Voorgestelde Workstreams op basis van terugkerende patronen in session logs en skills:

| # | Workstream | Agents | Frequentie | Prioriteit |
|---|---|---|---|---|
| WS-001 | Daily Planning | Marcus, Larry | Dagelijks | **Hoog** |
| WS-002 | Morning Routine | Larry, Marcus, Sienna, Penn | Dagelijks | **Hoog** |
| WS-003 | End-of-Day Routine | Larry, Marcus, Penn | Dagelijks | **Hoog** |
| WS-004 | Close Session + Learning | Larry | Per sessie | **Hoog** |
| WS-005 | New Specialist Hiring | Larry, Pax, Nolan | Ad hoc | Medium |
| WS-006 | Priority Gate (nieuw initiatief) | Larry, Sienna, Marcus | Ad hoc | Medium |
| WS-007 | Weekly Project Health Check | Marcus, Larry | Wekelijks | Medium |
| WS-008 | Knowledge Refresh per specialist | Larry, Pax, Nolan | Bij trigger | Medium |
| WS-009 | Learning Loop + Graduation | Larry | Per sessie/week | Medium |
| WS-010 | Integration Change | Kai, Larry | Ad hoc | Laag |

---

## 9. Governance-model

### Wat zelfstandig is toegestaan
- Inventariseren, analyseren, signaleren
- Verbetervoorstellen maken
- Conceptdocumenten schrijven
- Implementation backlog opstellen
- Agent journals schrijven (eigen agent, na taak)
- Graduation candidates voorstellen

### Wat alleen na akkoord van Walter mag
- CLAUDE.md wijzigen
- AGENT.md bestanden wijzigen
- SOPs toevoegen of aanpassen
- Guidelines toevoegen of aanpassen
- Workstreams aanmaken of aanpassen
- Folderstructuur wijzigen
- Database schema-wijzigingen
- Integratieconfiguraties aanpassen
- Governance-regels wijzigen
- Kernprompts en memory-structuren wijzigen

### Wat nooit zonder expliciete opdracht mag
- Bestanden verwijderen
- Agents verwijderen of hernoemen
- Kernrollen overschrijven
- Bestaande SOPs vervangen zonder changelog
- Bestaande instructies stilletjes wijzigen
- Eigen gedragsregels automatisch aanpassen
- Walter's approval overslaan

### Eigenaarschap per type wijziging
| Type | Eigenaar audit | Eigenaar implementatie | Reviewer | Approval |
|---|---|---|---|---|
| AGENT.md | Nolan | Nolan | Larry | Walter |
| SOP | Larry | Domein-specialist | Larry | Walter |
| Guideline | Larry | Nolan/Kai/Marcus | Larry | Walter |
| Workstream | Marcus/Larry | Marcus | Larry | Walter |
| Database schema | Kai | Kai | Larry | Walter |
| Integraties | Kai | Kai | Larry | Walter |
| Governance | Larry | Larry | — | Walter |

### Audit trail (ontbreekt, moet worden geborgd)
Elke wijziging in AGENT.md, SOP, GL of WS na approval moet een changelog-entry bevatten:
- Datum
- Wat gewijzigd
- Waarom
- Wie verantwoordelijk
- Welke approval gegeven

**Aanbeveling:** `GL-012_AI Team Governance.md` aanmaken met bovenstaande regels als authoritative bron.

---

## 10. Learning Loop Model

De learning loop is structureel aanwezig maar nog niet in productie genomen.

**Huidig model (ontworpen):**

```
1. Feedback ontvangen (owner, task outcome, session)
         ↓
2. Feedback classificeren (agent_learnings / team_log)
         ↓
3. Patroon herkennen (Larry bij session close)
         ↓
4. Learning formuleren (agent journal entry via SOP-009)
         ↓
5. Learning loggen (linked_journal_entries in task)
         ↓
6. Graduation candidate maken (close-session Stap 5)
         ↓
7. Verbetering voorstellen aan Walter
         ↓
8. Walter approval
         ↓
9. SOP / GL / WS / AGENT.md aanpassen + changelog
         ↓
10. Volgende taak: priors laden via SOP-008
```

**Ontbrekende schakels:**
- Stap 4-5: `linked_journal_entries` is nooit gevuld — geen priors beschikbaar
- Stap 6: graduation is structureel aanwezig maar nooit uitgevoerd
- Stap 9: changelog-systeem bestaat niet
- Stap 10: `SOP-008 Read own journal` is nooit actief gebruikt

**Activering vereist:**
- Eerste echte agent journal entries schrijven (na eerste echte delegaties met outcome)
- Eerste graduation candidate review uitvoeren
- Changelog-systeem introduceren (minimaal: `## Changelog` sectie in elk SOP/GL/WS bestand)

---

## 11. Implementation Backlog

| ID | Verbetering | Type | Impact | Risico | Eigenaar | Approval nodig | Prioriteit |
|---|---|---|---|---|---|---|---|
| B-001 | Database backup activeren (pg_dump + SQLite cron) | Technisch | Hoog | Laag | Kai | Walter | **1 — Hoog** |
| B-002 | GL nummering conflict oplossen (GL-002 en GL-010 dubbel) | Structuur | Hoog | Laag | Larry | Walter | **1 — Hoog** |
| B-003 | Finn routing corrigeren (Vera → Larry) | AGENT.md | Hoog | Laag | Nolan | Walter | **1 — Hoog** |
| B-004 | GL-012 Governance document aanmaken | Governance | Hoog | Laag | Larry | Walter | **1 — Hoog** |
| B-005 | Workstreams map aanmaken + WS-001 t/m WS-004 schrijven | Workstream | Hoog | Medium | Marcus/Larry | Walter | **2 — Hoog** |
| B-006 | Bridges containeriseren (Docker Compose) | Technisch | Medium | Medium | Kai | Walter | **2 — Medium** |
| B-007 | n8n volume backup inrichten | Technisch | Medium | Laag | Kai | Walter | **2 — Medium** |
| B-008 | agent_slug migratie afronden (personal.db + ke.db) | Database | Medium | Laag | Kai | Walter | **2 — Medium** |
| B-009 | SOP-010 Morning Routine schrijven | SOP | Medium | Laag | Marcus | Walter | **2 — Medium** |
| B-010 | SOP-011 End-of-Day Routine schrijven | SOP | Medium | Laag | Marcus | Walter | **2 — Medium** |
| B-011 | delegation_outcomes vullen (SOP-005 updaten) | Logging | Medium | Laag | Larry | Walter | **2 — Medium** |
| B-012 | Integratie runbooks: n8n, cloudflared, dropbox | Documentatie | Medium | Laag | Kai | Walter | **3 — Medium** |
| B-013 | SOP-006 updaten: gepauzeerde fase + health check + paden | SOP | Medium | Laag | Marcus | Walter | **3 — Medium** |
| B-014 | Goal-inactiviteitsdrempel afstemmen Larry/Marcus (3 vs 5 dagen) | AGENT.md | Medium | Laag | Larry + Marcus | Walter | **3 — Medium** |
| B-015 | Eerste echte agent journals schrijven (learning loop activeren) | Learning | Medium | Laag | Alle agents | Nee | **3 — Medium** |
| B-016 | WS-005 t/m WS-010 schrijven | Workstream | Medium | Laag | Marcus/Larry | Walter | **3 — Medium** |
| B-017 | "Never Does" secties toevoegen (5 agents) | AGENT.md | Laag | Laag | Nolan | Walter | **4 — Laag** |
| B-018 | Knowledge Currency secties toevoegen (4 agents) | AGENT.md | Laag | Laag | Nolan | Walter | **4 — Laag** |
| B-019 | Larry Samenwerking-sectie toevoegen | AGENT.md | Laag | Laag | Nolan | Walter | **4 — Laag** |
| B-020 | Bo AGENT.md versterken (Task Discipline, UMC, KC) | AGENT.md | Laag | Laag | Nolan | Walter | **4 — Laag** |

---

## 12. Change Proposal

### CP-001 — Database backup activeren

**Wat:** Cron-entries aanmaken voor pg_dump (memory-db) en SQLite backup (4 databases) + n8n volume backup
**Waarom:** SOP-007 beschrijft het maar de cron ontbreekt. Bij Pi-crash is alles weg.
**Bestanden:** `/home/admin/.config/rclone/local-backup.sh`, crontab
**Risico:** Geen functioneel risico. Alleen nieuw toevoegen.
**Reviewer:** Kai
**Walter approval:** Ja (database schema en cron zijn kritieke infrastructuur)

---

### CP-002 — GL nummering conflict oplossen

**Wat:** `GL-002_ChatGPT prompt ICOR module-verwerking.md` hernoemen naar GL-012. `GL-010_Memory Core Architecture.md` hernoemen naar GL-013. gl-index updaten.
**Waarom:** Agents weten niet welke GL authoritative is. Conflicterende nummering.
**Bestanden:** 2 GL-bestanden, gl-index.md
**Risico:** Laag (hernoemen, geen inhoud wijzigen). Wikilinks die naar de oude nummers verwijzen moeten worden geüpdated.
**Reviewer:** Larry
**Walter approval:** Ja

---

### CP-003 — Finn routing corrigeren

**Wat:** Finn AGENT.md aanpassen: verwijder of corrigeer de zin "bij scope-onduidelijkheid vraagt Finn terug naar Vera". Vervangen door: scope-onduidelijkheid escaleren naar Larry.
**Waarom:** Directe schending van de Iron Rule — Larry is de enige taakingang.
**Bestanden:** `Team/Finn - The WordPress Specialist/AGENT.md`
**Risico:** Laag (gedragswijziging die de governance herstelt).
**Reviewer:** Nolan
**Walter approval:** Ja

---

### CP-004 — GL-012 AI Team Governance aanmaken

**Wat:** Nieuw GL-bestand met approval-gates, escalation rules, changelog-protocol, audit trail
**Waarom:** Governance-regels staan verspreid over CLAUDE.md en memory. Geen authoritative bron.
**Bestanden:** Nieuw `GL-012_AI Team Governance.md`, gl-index.md
**Risico:** Laag (additioneel document).
**Reviewer:** Larry
**Walter approval:** Ja

---

### CP-005 — Workstreams map + WS-001 t/m WS-004

**Wat:** Map aanmaken, WS-001 (Daily Planning), WS-002 (Morning Routine), WS-003 (End-of-Day Routine), WS-004 (Close Session + Learning) schrijven
**Waarom:** CLAUDE.md verwijst naar non-existent laag. 10 terugkerende processen zijn ongeborgd.
**Bestanden:** Nieuwe map + 4 nieuwe WS-bestanden
**Risico:** Medium (nieuwe structuurlaag introduceren)
**Reviewer:** Marcus + Larry
**Walter approval:** Ja

---

## 13. Aanbevolen implementatiefases

### Fase 1 — Stabiliseren (week 1)
Kritieke problemen zonder gedragsverandering oplossen:
- B-001: Database backup activeren (Kai)
- B-002: GL nummering conflict oplossen (Larry)
- B-003: Finn routing corrigeren (Nolan)
- B-004: GL-012 Governance document aanmaken (Larry)
- B-008: agent_slug migratie afronden (Kai)

### Fase 2 — Rollen aanscherpen (week 2)
- B-014: Goal-drempel afstemmen Larry/Marcus
- B-017: "Never Does" secties toevoegen (5 agents)
- B-018: Knowledge Currency secties toevoegen (4 agents)
- B-019: Larry Samenwerking-sectie
- B-020: Bo AGENT.md versterken

### Fase 3 — SOPs aanvullen (week 2-3)
- B-009: SOP-010 Morning Routine
- B-010: SOP-011 End-of-Day Routine
- B-013: SOP-006 updaten (gepauzeerde fase + paden)
- B-012: Integratie runbooks (n8n, cloudflared, dropbox)

### Fase 4 — Workstreams introduceren (week 3-4)
- B-005: WS-001 t/m WS-004 (Daily Planning, Routines, Close Session)
- B-016: WS-005 t/m WS-010

### Fase 5 — Learning Loop activeren (week 4-5)
- B-015: Eerste echte agent journals
- B-011: delegation_outcomes vullen
- Eerste graduation candidate review

### Fase 6 — Technische versterking (parallel)
- B-006: Bridges containeriseren
- B-007: n8n volume backup

### Fase 7 — Gecontroleerde implementatie + changelog
Elke wijziging na akkoord: changelog-entry, rapportage aan Larry, Walter informeren over wijziging.

---

## 14. Besluitpunten voor Walter

| Besluit | Advies team | Opties | Impact | Keuze Walter |
|---|---|---|---|---|
| Fase 1 fiatteren | Start direct — kritieke risico's | a) Ja, go | Backup + SSOT stabiel | |
| GL-002 ChatGPT prompt | Hernoemen naar GL-012 of archiveren | a) Hernoemen b) Archiveren | SSOT conflict opgelost | |
| Workstreams aanmaken | Ja — CLAUDE.md verwijst er al naar | a) Start met WS-001 t/m WS-004 b) Alle 10 tegelijk | Structuur compleet | |
| GL-012 Governance | Aanmaken als authoritative governance-bron | a) Als GL b) Als SOP | Approval-gates geborgd | |
| Finn routing | Corrigeren richting Larry | a) Corrigeer direct | Iron Rule hersteld | |
| Leerloop activeren | Ja, maar stap voor stap | a) Start na Fase 1 b) Start gelijktijdig | Team leert werkelijk | |
| Audit borgen als SOP | Ja — SOP-010 of GL-012 | a) SOP-010 AI Team Management b) GL-012 Governance | Herhaalbare audit | |
| Changelog-systeem | Introduceren als verplichte stap | a) Sectie in elk SOP/GL/WS b) Aparte changelog.md | Audit trail compleet | |

---

---

## 15. Owner Acceptance Records

This section records Owner-accepted closures for audit backlog items. Each entry is logged only after Owner Walter Kamer's explicit review and acceptance.

| Item | Description | Sub-items | Accepted on | Accepted by | Notes |
|---|---|---|---|---|---|
| B-021C | Secure Credential Recovery | B-021C-A (SOP update), B-021C-B (`.env` permissions) | 2026-06-03 | Walter Kamer | Execution correct and within scope. No secret exposure. No files outside SOP-001 modified. No service restart performed. team_log id=79. |

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/audit-report.md`*
*Geen wijzigingen uitgevoerd. Wacht op Walter's expliciete akkoord per Change Proposal.*
