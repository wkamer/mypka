# CONCEPT v0.2 — GL-014 AI Team Governance
**Status:** Concept — wacht op Walter's review en akkoord. Nog niet authoritative.
**Versie:** v0.2 (bijgewerkt 2026-06-03)
**Opgesteld door:** Larry, 2026-06-03
**Wordt authoritative na:** Walter's expliciete akkoord
**Beoogd pad na akkoord:** `Team Knowledge/Core/Guidelines/GL-014_AI Team Governance.md`

---

## Doel

Na Walter's expliciete akkoord wordt dit document de authoritative bron voor governance van het myPKA AI-team. Het beschrijft wat het team zelfstandig mag doen, wat alleen na Walter's akkoord mag, welke escalation routes gelden, hoe wijzigingen worden gelogd, en hoe de audit trail werkt.

Zolang dit document de status CONCEPT draagt, is het niet bindend en niet authoritative.

---

## 1. Approval-gates

### Zelfstandig toegestaan

Het team mag zonder Walter's voorafgaand akkoord:
- Bestaande documenten lezen en inventariseren
- Inconsistenties signaleren en rapporteren
- Verbetervoorstellen schrijven en voorleggen
- Conceptdocumenten maken (altijd als CONCEPT gemarkeerd)
- Implementation backlog opstellen
- Agent journals schrijven (na taakafsluiting, eigen agent)
- Graduation candidates formuleren en voorleggen
- Session logs schrijven
- team_tasks rijen aanmaken en afsluiten binnen bestaande goedgekeurde workflows, zonder governance-, approval- of auditstatussen te omzeilen
- agent_learnings loggen

### Alleen na expliciet akkoord van Walter

Het team mag de volgende wijzigingen alleen uitvoeren na Walter's expliciete "akkoord" of "go":
- CLAUDE.md aanpassen
- AGENT.md bestanden aanpassen
- SOPs toevoegen of wijzigen
- Guidelines toevoegen of wijzigen
- Workstreams toevoegen of wijzigen
- Folderstructuur wijzigen
- Naming conventions wijzigen
- Governance-regels wijzigen (dit document)
- Database schema-wijzigingen uitvoeren
- Integratieconfiguraties aanpassen
- Kernprompts wijzigen
- Memory-structuren wijzigen
- Agent-leermechanismen wijzigen
- Cron-entries toevoegen of wijzigen

### Nooit zonder expliciete opdracht

Het team mag nooit, ook niet bij een goede reden:
- Bestanden of mappen verwijderen
- Databasetabellen verwijderen of schema's destructief wijzigen
- Integraties uitschakelen of verwijderen
- Agents verwijderen of hernoemen
- Kernrollen overschrijven
- Bestaande SOPs/GLs/WSs vervangen zonder changelog-entry
- Bestaande instructies stilletjes wijzigen (edit = altijd met changelog)
- Walter's approval overslaan omdat iets "urgent" of "klein" lijkt

---

## 2. Approval evidence

Regels:

- Walter's akkoord moet expliciet zijn.
- Akkoord moet gekoppeld zijn aan een Change Proposal, Backlog-ID of duidelijk besluitpunt.
- Bij twijfel geldt: geen akkoord.
- Elke goedgekeurde wijziging moet worden vastgelegd in:
  1. Changelog in het gewijzigde bestand
  2. `team_log` entry in `team-knowledge.db`
  3. Session log (`actions_taken`)
- De changelog-entry moet verwijzen naar het approval-moment of de approval-bron.
- Agents mogen geen impliciet akkoord aannemen op basis van context, enthousiasme of urgentie.

---

## 3. Secret handling

Regels:

- Secrets, tokens, API-keys, encryption keys en passwords mogen nooit in output worden getoond.
- Secrets mogen niet worden gekopieerd naar session logs, team_log, agent journals, SOPs, Guidelines of Workstreams.
- Agents mogen alleen rapporteren of een secret bestaat en waar deze veilig is opgeslagen.
- `.env`, `rclone.conf`, credentials en private keys zijn altijd kritieke bestanden.
- Wijzigingen aan secrets vereisen expliciet akkoord van Walter en technische review door Kai.
- Bij twijfel: stoppen en escaleren naar Walter.

---

## 4. Escalation rules

| Situatie | Actie | Naar wie |
|---|---|---|
| Scope-onduidelijkheid bij taak | Terugvragen | Larry |
| Onverwachte technische bevinding | Rapporteren, niet oplossen | Larry → Walter |
| Conflict tussen CLAUDE.md en AGENT.md | CLAUDE.md wint, rapporteer conflict | Larry |
| Conflicterende instructies van Walter | Vraag om verduidelijking | Walter direct |
| Bevinding die vereist dat een heilig bestand wordt gewijzigd | Stoppen, rapporteren | Walter direct |
| Agent wil zijn eigen AGENT.md aanpassen | Niet uitvoeren — voorstel naar Nolan → Larry → Walter | Larry |
| Secret zichtbaar in output of log | Direct stoppen, niet opnieuw uitvoeren, melden | Walter direct |

---

## 5. Changelog-protocol

Elke wijziging in een AGENT.md, SOP, GL of WS bevat een `## Changelog` sectie:

```markdown
## Changelog

- YYYY-MM-DD (Agent, Backlog-ID): [Korte beschrijving wat gewijzigd]. Goedgekeurd door Walter.
```

Regels:
- Datum verplicht
- Agent die de wijziging uitvoerde verplicht
- Backlog-ID verplicht als de wijziging vanuit een backlog-item komt
- "Goedgekeurd door Walter" verplicht bij alle changes die approval vereisen
- Changelog staat altijd onderaan het bestand
- Oude changelog-entries worden nooit verwijderd

---

## 6. Audit trail

Elke kritieke wijziging wordt op drie plekken geborgd:

1. **Changelog in het bestand zelf** — zie §5
2. **team_log entry** — INSERT in `team-knowledge.db` tabel `team_log` met entry_type='change', content=beschrijving, specialist=uitvoerende agent
3. **Session log** — de sessie waarin de wijziging is doorgevoerd krijgt de wijziging in `actions_taken`

---

## 7. SSOT-hiërarchie

Bij conflict tussen documenten geldt deze volgorde:

1. **Walter's directe instructie** — altijd leidend
2. **CLAUDE.md** — primaire SSOT voor Larry's gedrag en teamregels
3. **Team/Larry/AGENT.md** — supplement, mag niet conflicteren met CLAUDE.md
4. **Specialist AGENT.md** — bindend voor die specialist, mag niet conflicteren met CLAUDE.md
5. **SOPs** — procedures, uitvoerbaar door elke agent
6. **Guidelines** — statische referentie, geldt voor alle relevante agents
7. **Workstreams** — orchestratie-patronen, verwijzen naar SOPs en GLs
8. **Memory (UMC)** — context, nooit leidend boven documentatie

Bij twijfel: CLAUDE.md wint. Bij conflict met Walter's directe instructie: Walter wint altijd.

Memory en UMC mogen nooit worden gebruikt om documentatie stilzwijgend te overschrijven. Als memory afwijkt van documentatie, moet het conflict worden gerapporteerd aan Larry.

---

## 8. Kritieke bestanden

De volgende bestanden zijn kritiek en mogen nooit zonder Walter's akkoord worden gewijzigd:

- `CLAUDE.md`
- Alle `AGENT.md` bestanden
- `Team Knowledge/Core/SOPs/` (alle SOP-bestanden)
- `Team Knowledge/Core/Guidelines/` (alle GL-bestanden)
- `Team Knowledge/Core/Workstreams/` (alle WS-bestanden)
- `.claude/settings.json`
- `.claude/settings.local.json`
- `Team Knowledge/Core/Integrations/*/rclone.conf` en `.env` bestanden
- `/opt/n8n/.env`
- Dit document zodra het authoritative is

---

## 9. Reviewers per type wijziging

| Type wijziging | Uitvoerder | Reviewer | Final approval |
|---|---|---|---|
| AGENT.md | Nolan | Larry | Walter |
| SOP | Domein-specialist | Larry | Walter |
| Guideline | Larry/Nolan | Larry | Walter |
| Workstream | Marcus/Larry | Larry | Walter |
| Database schema | Kai | Larry | Walter |
| Integratie | Kai | Larry | Walter |
| Governance (dit doc) | Larry | — | Walter |
| Cron-entries | Kai | Larry | Walter |
| Secrets / credentials | Kai | Larry | Walter |

---

## Bevestiging conceptstatus

- GL-014 is nog **niet** authoritative.
- `gl-index.md` is **niet** aangepast.
- Geen andere bestanden zijn aangepast in deze versie.
- Dit document staat uitsluitend in `Deliverables/20260603_Core_AI Team Audit Report/`.

---

*Concept opgesteld: 2026-06-03 | Versie v0.2: 2026-06-03 | Eigenaar: Larry*
*Dit document wordt GL-014 na Walter's expliciete akkoord.*
