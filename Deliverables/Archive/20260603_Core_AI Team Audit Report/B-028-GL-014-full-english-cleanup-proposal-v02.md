# B-028 GL-014 Full English Cleanup Proposal v0.2

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Concept — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.1
**No changes executed**
**Changes vs v0.1:** Header proposal corrected (`Owner:` → `Maintainer:`). Execution Checklist counts replaced with descriptive scope language.

---

## 1. Executive Summary

GL-014 AI Team Governance is the authoritative governance document for the team. It states in §10 that all system files must be written in English. However, GL-014 itself is largely written in Dutch — header metadata, section headings, approval-gate descriptions, escalation rules, changelog protocol, audit trail instructions and the SSOT hierarchy are all in Dutch.

This creates a governance inconsistency: the document that mandates English system files is itself not in English.

This proposal provides the full execution-ready English replacement for every Dutch section in GL-014, with specific handling for historical changelog entries. No functional meaning is altered.

---

## 2. Why this cleanup is needed

| Issue | Detail |
|---|---|
| Self-referential inconsistency | GL-014 §10 mandates English system files; GL-014 itself is Dutch |
| Agent instruction loading | Agents load GL-014 as governance reference — Dutch instructions risk inconsistency |
| Audit credibility | An audit report pointing to a Dutch governance document weakens the audit trail |
| Future maintainability | New sections should be written in English — existing Dutch creates a confusing baseline |

---

## 3. File inspected

`Team Knowledge/Core/Guidelines/GL-014_AI Team Governance.md`

---

## 4. Dutch system-file content found in GL-014

| Location | Dutch content | Type |
|---|---|---|
| Header: `**Versie:**` | Label text | Metadata |
| Header: `**Goedgekeurd door:**` | Label text | Metadata |
| Header: `**Datum akkoord:**` | Label text | Metadata |
| Header: `**Eigenaar:**` | Label text | Metadata |
| Header: `**Owner definitie:**` | Full sentence in Dutch | Active governance |
| `## Doel` | Section heading + full body | Active governance |
| `### Zelfstandig toegestaan` | Subheading + all bullet items | Active governance |
| `### Alleen na explicit Owner approval` | Mixed intro sentence in Dutch + all list items in Dutch | Active governance |
| `### Nooit zonder expliciete opdracht` | Subheading + all bullet items | Active governance |
| §2 `Regels:` + body | All body text in Dutch | Active governance |
| §3 `Regels:` + body | All body text in Dutch | Active governance |
| §4 Escalation table | Dutch column headers + Dutch table cell values | Active governance |
| §5 intro sentence | Dutch | Active governance |
| §5 Changelog template placeholder | `[Korte beschrijving wat gewijzigd]` | Active template |
| §5 `Regels:` + rules | Dutch rules (except one already in English) | Active governance |
| §6 body | Full body in Dutch | Active governance |
| `## 7. SSOT-hiërarchie` | Section heading + Dutch descriptions + Dutch body sentences | Active governance |
| `## 8. Kritieke bestanden` | Section heading + Dutch intro + Dutch list items | Active governance |
| `## 9. Reviewers per type wijziging` | Section heading + Dutch table headers + Dutch table values | Active governance |
| Changelog B-004 | Full Dutch description | Historical record |
| Changelog B-022 | Full Dutch description | Historical record |

---

## 5. Full proposed English replacement for GL-014 sections

### Header block

**Current:**
```
**Versie:** v1.1
**Goedgekeurd door:** Owner (Walter Kamer)
**Datum akkoord:** 2026-06-03
**Eigenaar:** Larry
**Owner definitie:** Owner = Walter Kamer. In alle procedures, governance-documenten en templates wordt de rolterm Owner gebruikt.
```

**Proposed:**
```
**Version:** v1.2
**Approved by:** Owner (Walter Kamer)
**Approval date:** 2026-06-03
**Maintainer:** Larry
**Owner definition:** Owner = Walter Kamer. In all procedures, governance documents and templates, the role term Owner is used.
```

**Note on Maintainer:** The label `**Owner:**` is replaced with `**Maintainer:**` to avoid conflict with the governance definition `Owner = Walter Kamer`. Larry maintains this document; Walter Kamer is the Owner.

---

### `## Doel` → `## Purpose`

**Current:**
```markdown
## Doel

Dit document is de authoritative bron voor governance van het myPKA AI-team. Het beschrijft wat het team zelfstandig mag doen, wat alleen na Owner approval mag, welke escalation routes gelden, hoe wijzigingen worden gelogd, en hoe de audit trail werkt.
```

**Proposed:**
```markdown
## Purpose

This document is the authoritative source for governance of the myPKA AI team. It describes what the team may do independently, what requires Owner approval, which escalation routes apply, how changes are logged, and how the audit trail works.
```

---

### `## 1. Approval-gates` — three subsections

**Current `### Zelfstandig toegestaan` → proposed `### Permitted independently`:**

```markdown
### Permitted independently

The team may without Owner's prior approval:
- Read and inventory existing documents
- Signal and report inconsistencies
- Write and submit improvement proposals
- Create concept documents (always marked as CONCEPT)
- Compile an implementation backlog
- Write agent journals (after task completion, own agent)
- Formulate and submit graduation candidates
- Write session logs
- Create and close team_tasks rows within existing approved workflows, without bypassing governance, approval or audit statuses
- Log agent_learnings
```

---

**Current `### Alleen na explicit Owner approval` → proposed `### Only after explicit Owner approval`:**

```markdown
### Only after explicit Owner approval

The team may execute the following changes only after Owner's explicit approval ("akkoord" or "go"):
- Modify CLAUDE.md
- Modify AGENT.md files
- Add or modify SOPs
- Add or modify Guidelines
- Add or modify Workstreams
- Modify folder structure
- Modify naming conventions
- Modify governance rules (this document)
- Execute database schema changes
- Modify integration configurations
- Modify core prompts
- Modify memory structures
- Modify agent learning mechanisms
- Add or modify cron entries
```

---

**Current `### Nooit zonder expliciete opdracht` → proposed `### Never without explicit instruction`:**

```markdown
### Never without explicit instruction

The team may never, even with a good reason:
- Delete files or folders
- Delete database tables or destructively modify schemas
- Disable or remove integrations
- Delete or rename agents
- Overwrite core roles
- Replace existing SOPs/GLs/WSs without a changelog entry
- Silently modify existing instructions (edit = always with changelog)
- Bypass Owner approval because something seems "urgent" or "small"
```

---

### `## 2. Approval evidence` — body

**Current:**
```markdown
Regels:

- Owner approval must be explicit.
- Akkoord moet gekoppeld zijn aan een Change Proposal, Backlog-ID of duidelijk besluitpunt.
- Bij twijfel geldt: geen akkoord.
- Elke goedgekeurde wijziging moet worden vastgelegd in:
  1. Changelog in het gewijzigde bestand
  2. `team_log` entry in `team-knowledge.db`
  3. Session log (`actions_taken`)
- De changelog-entry moet verwijzen naar het approval-moment of de approval-bron.
- Agents mogen geen impliciet akkoord aannemen op basis van context, enthousiasme of urgentie.
```

**Proposed:**
```markdown
Rules:

- Owner approval must be explicit.
- Approval must be linked to a Change Proposal, Backlog ID or clear decision point.
- When in doubt: no approval.
- Every approved change must be recorded in:
  1. Changelog in the modified file
  2. `team_log` entry in `team-knowledge.db`
  3. Session log (`actions_taken`)
- The changelog entry must refer to the approval moment or approval source.
- Agents may not assume implicit approval based on context, enthusiasm or urgency.
```

---

### `## 3. Secret handling` — body

**Current:**
```markdown
Regels:

- Secrets, tokens, API-keys, encryption keys en passwords mogen nooit in output worden getoond.
- Secrets mogen niet worden gekopieerd naar session logs, team_log, agent journals, SOPs, Guidelines of Workstreams.
- Agents mogen alleen rapporteren of een secret bestaat en waar deze veilig is opgeslagen.
- `.env`, `rclone.conf`, credentials en private keys zijn altijd kritieke bestanden.
- Wijzigingen aan secrets vereisen Owner's explicit approval en technische review door Kai.
- When in doubt: stop and escalate to Owner directly.
```

**Proposed:**
```markdown
Rules:

- Secrets, tokens, API keys, encryption keys and passwords may never be shown in output.
- Secrets may not be copied to session logs, team_log, agent journals, SOPs, Guidelines or Workstreams.
- Agents may only report whether a secret exists and where it is securely stored.
- `.env`, `rclone.conf`, credentials and private keys are always critical files.
- Changes to secrets require Owner's explicit approval and technical review by Kai.
- When in doubt: stop and escalate to Owner directly.
```

---

### `## 4. Escalation rules` — table

**Current:**
```markdown
| Situatie | Actie | Naar wie |
| Scope-onduidelijkheid bij taak | Terugvragen | Larry |
| Onverwachte technische bevinding | Rapporteren, niet oplossen | Larry → Owner |
| Conflict tussen CLAUDE.md en AGENT.md | CLAUDE.md wint, rapporteer conflict | Larry |
| Conflicting instructions from Owner | Vraag om verduidelijking | Owner directly |
| Bevinding die vereist dat een heilig bestand wordt gewijzigd | Stoppen, rapporteren | Owner directly |
| Agent wil zijn eigen AGENT.md aanpassen | Niet uitvoeren — voorstel naar Nolan → Larry → Owner | Larry |
| Secret zichtbaar in output of log | Direct stoppen, niet opnieuw uitvoeren, melden | Owner directly |
```

**Proposed:**
```markdown
| Situation | Action | Escalate to |
|---|---|---|
| Unclear scope on a task | Ask for clarification | Larry |
| Unexpected technical finding | Report, do not resolve | Larry → Owner |
| Conflict between CLAUDE.md and AGENT.md | CLAUDE.md wins, report conflict | Larry |
| Conflicting instructions from Owner | Ask for clarification | Owner directly |
| Finding requires modifying a critical file | Stop, report | Owner directly |
| Agent wants to modify their own AGENT.md | Do not execute — propose to Nolan → Larry → Owner | Larry |
| Secret visible in output or log | Stop immediately, do not re-execute, report | Owner directly |
```

---

### `## 5. Changelog-protocol` — intro + template + rules

**Current intro:**
`Elke wijziging in een AGENT.md, SOP, GL of WS bevat een \`## Changelog\` sectie:`

**Proposed:**
`Every change to an AGENT.md, SOP, GL or WS contains a \`## Changelog\` section:`

**Current template placeholder:**
`[Korte beschrijving wat gewijzigd]`

**Proposed:**
`[Short description of what was changed]`

**Current rules:**
```
- Datum verplicht
- Agent die de wijziging uitvoerde verplicht
- Backlog-ID verplicht als de wijziging vanuit een backlog-item komt
- "Approved by Owner" required for all changes that require approval
- Changelog staat altijd onderaan het bestand
- Oude changelog-entries worden nooit verwijderd
```

**Proposed:**
```
- Date required
- Agent who executed the change required
- Backlog ID required when the change originates from a backlog item
- "Approved by Owner" required for all changes that require approval
- Changelog is always at the bottom of the file
- Old changelog entries are never deleted
```

---

### `## 6. Audit trail` — body

**Current:**
```markdown
Elke kritieke wijziging wordt op drie plekken geborgd:

1. **Changelog in het bestand zelf** — zie §5
2. **team_log entry** — INSERT in `team-knowledge.db` tabel `team_log` met entry_type='change', content=beschrijving, specialist=uitvoerende agent
3. **Session log** — de sessie waarin de wijziging is doorgevoerd krijgt de wijziging in `actions_taken`
```

**Proposed:**
```markdown
Every critical change is recorded in three places:

1. **Changelog in the file itself** — see §5
2. **team_log entry** — INSERT into `team-knowledge.db` table `team_log` with entry_type='change', content=description, specialist=executing agent
3. **Session log** — the session in which the change was made records the change in `actions_taken`
```

---

### `## 7. SSOT-hiërarchie` → `## 7. SSOT Hierarchy`

**Current:**
```markdown
## 7. SSOT-hiërarchie

Bij conflict tussen documenten geldt deze volgorde:

1. **Owner's direct instruction** — always leading
2. **CLAUDE.md** — primaire SSOT voor Larry's gedrag en teamregels
3. **Team/Larry/AGENT.md** — supplement, mag niet conflicteren met CLAUDE.md
4. **Specialist AGENT.md** — bindend voor die specialist, mag niet conflicteren met CLAUDE.md
5. **SOPs** — procedures, uitvoerbaar door elke agent
6. **Guidelines** — statische referentie, geldt voor alle relevante agents
7. **Workstreams** — orchestratie-patronen, verwijzen naar SOPs en GLs
8. **Memory (UMC)** — context, nooit leidend boven documentatie

Bij twijfel: CLAUDE.md wint. Upon conflict with Owner's direct instruction: Owner wins always.

Memory en UMC mogen nooit worden gebruikt om documentatie stilzwijgend te overschrijven. Als memory afwijkt van documentatie, moet het conflict worden gerapporteerd aan Larry.
```

**Proposed:**
```markdown
## 7. SSOT Hierarchy

When documents conflict, this order of precedence applies:

1. **Owner's direct instruction** — always leading
2. **CLAUDE.md** — primary SSOT for Larry's behavior and team rules
3. **Team/Larry/AGENT.md** — supplement, may not conflict with CLAUDE.md
4. **Specialist AGENT.md** — binding for that specialist, may not conflict with CLAUDE.md
5. **SOPs** — procedures, executable by any agent
6. **Guidelines** — static reference, applies to all relevant agents
7. **Workstreams** — orchestration patterns, reference SOPs and GLs
8. **Memory (UMC)** — context, never authoritative over documentation

When in doubt: CLAUDE.md wins. Upon conflict with Owner's direct instruction: Owner wins always.

Memory and UMC may never be used to silently overwrite documentation. If memory deviates from documentation, the conflict must be reported to Larry.
```

---

### `## 8. Kritieke bestanden` → `## 8. Critical Files`

**Current:**
```markdown
## 8. Kritieke bestanden

De volgende bestanden zijn kritiek en mogen nooit zonder Owner approval worden gewijzigd:

- `CLAUDE.md`
- Alle `AGENT.md` bestanden
- `Team Knowledge/Core/SOPs/` (alle SOP-bestanden)
- `Team Knowledge/Core/Guidelines/` (alle GL-bestanden)
- `Team Knowledge/Core/Workstreams/` (alle WS-bestanden)
- `.claude/settings.json`
- `.claude/settings.local.json`
- `Team Knowledge/Core/Integrations/*/rclone.conf` en `.env` bestanden
- `/opt/n8n/.env`
- Dit document
```

**Proposed:**
```markdown
## 8. Critical Files

The following files are critical and may never be modified without Owner approval:

- `CLAUDE.md`
- All `AGENT.md` files
- `Team Knowledge/Core/SOPs/` (all SOP files)
- `Team Knowledge/Core/Guidelines/` (all GL files)
- `Team Knowledge/Core/Workstreams/` (all WS files)
- `.claude/settings.json`
- `.claude/settings.local.json`
- `Team Knowledge/Core/Integrations/*/rclone.conf` and `.env` files
- `/opt/n8n/.env`
- This document
```

---

### `## 9. Reviewers per type wijziging` → `## 9. Reviewers per Change Type`

**Current:**
```markdown
## 9. Reviewers per type wijziging

| Type wijziging | Uitvoerder | Reviewer | Final approval |
|---|---|---|---|
| AGENT.md | Nolan | Larry | Owner |
| SOP | Domein-specialist | Larry | Owner |
| Guideline | Larry/Nolan | Larry | Owner |
| Workstream | Marcus/Larry | Larry | Owner |
| Database schema | Kai | Larry | Owner |
| Integratie | Kai | Larry | Owner |
| Governance (dit doc) | Larry | — | Owner |
| Cron-entries | Kai | Larry | Owner |
| Secrets / credentials | Kai | Larry | Owner |
```

**Proposed:**
```markdown
## 9. Reviewers per Change Type

| Change type | Executor | Reviewer | Final approval |
|---|---|---|---|
| AGENT.md | Nolan | Larry | Owner |
| SOP | Domain specialist | Larry | Owner |
| Guideline | Larry/Nolan | Larry | Owner |
| Workstream | Marcus/Larry | Larry | Owner |
| Database schema | Kai | Larry | Owner |
| Integration | Kai | Larry | Owner |
| Governance (this document) | Larry | — | Owner |
| Cron entries | Kai | Larry | Owner |
| Secrets / credentials | Kai | Larry | Owner |
```

---

## 6. Metadata translation proposal

| Label | Current | Proposed |
|---|---|---|
| `**Versie:**` | Dutch | `**Version:**` |
| `**Goedgekeurd door:**` | Dutch | `**Approved by:**` |
| `**Datum akkoord:**` | Dutch | `**Approval date:**` |
| `**Eigenaar:**` | Dutch | `**Maintainer:**` (not `Owner:` — see note below) |
| `**Owner definitie:**` | Dutch sentence | English sentence |
| Version number | v1.1 | v1.2 |

**Note on Maintainer vs Owner:** The original label `**Eigenaar:** Larry` must not become `**Owner:** Larry`. The governance definition in this same document states `Owner = Walter Kamer`. Using `Owner` for Larry would create a direct conflict. The correct English label is `**Maintainer:** Larry`.

---

## 7. Changelog handling proposal

| Entry | Classification | Proposed action |
|---|---|---|
| B-004 | Historical record — predates language rule | Leave unchanged |
| B-022 | Historical record — predates language rule | Leave unchanged |
| B-025 | Already in English | No action |
| B-027 | Already in English | No action |
| New B-028 entry | New | Add: `2026-06-03 (Larry, B-028): GL-014 fully translated to English. No functional changes. Version updated to v1.2. Approved by Owner.` |

---

## 8. Historical records: leave or update?

| Item | Recommendation | Reason |
|---|---|---|
| Changelog entry B-004 | Leave unchanged | Historical record, predates language rule |
| Changelog entry B-022 | Leave unchanged | Historical record, predates language rule |
| Old session logs | Leave | Out of scope |
| Old team_log entries | Leave | Out of scope |

Owner may explicitly approve translating the B-004 and B-022 descriptions if desired. Default is to leave them.

---

## 9. Impact on governance functionality

None. Every section replacement preserves full functional meaning. All approval gates, escalation routes, secret handling rules, changelog protocol, audit trail model, SSOT hierarchy, critical files list, §10 language rule, B-025 and B-027 additions are preserved verbatim in meaning.

---

## 10. Risks and mitigations

| Risk | Level | Mitigation |
|---|---|---|
| Translation error alters functional meaning | Low | Full exact text provided in §5 — review before approving |
| `Maintainer` label unfamiliar | Low | Explained in §6 — avoids Owner conflict |
| Historical entries left in Dutch | Low | Intentional per GL-014 rule — Owner may override |

---

## 11. Execution Checklist

| Section | Action | Preserve |
|---|---|---|
| Header block | Translate all Dutch labels; use `Maintainer:` not `Owner:`; update version to v1.2 | Owner definition meaning |
| `## Doel` | Rename to `## Purpose`; translate body | Full meaning |
| `§1 Zelfstandig toegestaan` | Rename to `Permitted independently`; translate all permission items | All permissions |
| `§1 Alleen na…` | Rename to `Only after explicit Owner approval`; translate intro sentence and all restriction items | All restrictions |
| `§1 Nooit zonder…` | Rename to `Never without explicit instruction`; translate intro sentence and all prohibition items | All prohibitions |
| `§2 Approval evidence body` | Translate all Dutch rules | All rules intact |
| `§3 Secret handling body` | Translate all Dutch rules | All rules intact |
| `§4 Escalation table` | Translate column headers and all Dutch cell values | All table rows |
| `§5 intro sentence` | Translate | Meaning |
| `§5 template placeholder` | Translate | Template structure |
| `§5 Regels:` rules | Translate all Dutch rules | All rules |
| `§6 Audit trail body` | Translate intro sentence and Dutch inline content | All three recording locations |
| `§7 SSOT-hiërarchie` | Rename to `SSOT Hierarchy`; translate intro; translate all Dutch hierarchy descriptions; translate body sentences | Full hierarchy order and precedence |
| `§8 Kritieke bestanden` | Rename to `Critical Files`; translate intro; translate Dutch list items | All file paths |
| `§9 Reviewers per type wijziging` | Rename to `Reviewers per Change Type`; translate column headers and Dutch table cell values | All rows |
| `§10 System File Language Rule` | No change needed — already in English | Full section including B-025 and B-027 |
| B-028 changelog entry | Add new English entry | — |
| B-004, B-022 entries | Leave unchanged | Historical record |

---

## 12. Decision points for Owner

| Decision | Advice | Options |
|---|---|---|
| Approve B-028 execution | Yes — removes governance inconsistency | a) Full approval b) Defer |
| Translate B-004 changelog entry | Leave as historical record (default) | a) Leave unchanged b) Translate description |
| Translate B-022 changelog entry | Leave as historical record (default) | a) Leave unchanged b) Translate description |
| Version number | Update to v1.2 | a) v1.2 b) Keep v1.1 |

---

## 13. Confirmation that nothing was changed

- GL-014 was not modified
- No AGENT.md files were modified
- No SOPs were modified
- No Workstreams were created or modified
- CLAUDE.md was not modified
- No databases were modified
- No integration configurations were modified
- No files were deleted
- No historical deliverables were rewritten
- This document is a read-only proposal in the Deliverables folder only

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-028-GL-014-full-english-cleanup-proposal-v02.md`*
