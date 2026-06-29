# GL-004 — Canonical Paths

**Geldig voor:** gehele myPKA vault en alle agents
**Laatste update:** 2026-05-19

---

## Principe

Alle paden in dit bestand zijn de enige juiste paden. Agents, SOPs en skills verwijzen naar dit bestand via `[[GL-004_Canonical paths]]`. Ze dupliceren geen paden. Bij twijfel wint dit bestand altijd.

---

## Vault root

```
C:\Users\wkame\myPKA\
```

Alle paden hieronder zijn relatief aan de vault root.

---

## Team structuur

| Doel | Pad |
|---|---|
| Agent-bestanden | `Team/` |
| Agent-index | `Team/agent-index.md` |
| Team Knowledge (alle domeinen) | `Team Knowledge/` |
| SOPs | `Team Knowledge/SOPs/` |
| Guidelines | `Team Knowledge/Core/Guidelines/` |
| Workstreams | `Team Knowledge/Core/Workstreams/` |
| Scripts | `Team Knowledge/Core/Scripts/` |
| Session logs (markdown mirrors) | `Team Knowledge/Core/session-logs/YYYY/MM/` |
| Team inbox (alle domeinen, flat) | `Team Inbox/` |
| Team inbox archief | `Team Inbox/Archive/` |

**Regel:** `Team Inbox/` heeft geen domeinsubmappen. Alle inputs landen flat in de root.

**Workstream routing:** Core Workstreams (`Team Knowledge/Core/Workstreams/`) hold cross-domain agent orchestrations managed by Larry or Marcus. Domain Workstreams (`Team Knowledge/<Domain>/Workstreams/`) hold domain-specific operational flows managed by domain specialists.

**Scaffold-afwijking (bewust):** De scaffold gebruikt een platte structuur: `Team Knowledge/SOPs/`, `Team Knowledge/Guidelines/` etc. direct onder `Team Knowledge/`. SOPs volgen nu de scaffold-structuur. Guidelines gebruiken nog de `Core/` tussenlaag: `Team Knowledge/Core/Guidelines/`. Agents gebruiken altijd de paden uit dit bestand — nooit terugvallen op de scaffold-structuur.

---

## Integrations

| Doel | Pad |
|---|---|
| Integrations root | `Team Knowledge/Core/Integrations/` |
| Bootstrap README | `Team Knowledge/Core/Integrations/README.md` |
| Google OAuth token | `Team Knowledge/Core/Integrations/google/token.json` |
| Google client secret | `Team Knowledge/Core/Integrations/google/client_secret.json` |
| Google scopes documentatie | `Team Knowledge/Core/Integrations/google/scopes.md` |
| Todoist credentials | `Team Knowledge/Core/Integrations/todoist/.env` |
| n8n .env template | `Team Knowledge/Core/Integrations/n8n/.env.template` |
| n8n bridge templates | `Team Knowledge/Core/Integrations/n8n/bridges/` |
| Discord config | `Team Knowledge/Core/Integrations/discord/config.md` |
| Meta config | `Team Knowledge/Core/Integrations/meta/config.md` |
| Shopify credentials | `Team Knowledge/Core/Integrations/shopify/.env` |
| ADRs | `Team Knowledge/Core/Integrations/ADRs/` |
| Service catalog | `Team Knowledge/Core/Integrations/service-catalog.md` |

**Regel:** Elke integratie heeft een `.env` bestand met live credentials (nooit in git). Templates (sleutelnamen zonder waarden) staan als `.env.template` naast het `.env` bestand. Scripts lezen credentials altijd uit deze `.env` bestanden — nooit uit `~/.claude/settings.json` of hardcoded.

---

## Templates

| Doel | Pad |
|---|---|
| Templates root | `Team Knowledge/Templates/` |
| Templates index | `Team Knowledge/Templates/INDEX.md` |

Agents start from the corresponding template when creating any entity. See `[[Team Knowledge/Templates/INDEX.md]]` for the full list.

---

## Databases

| Database | Pad |
|---|---|
| Persoonlijk | `PKM/personal.db` |
| Kamer E-commerce | `Team Knowledge/Kamer E-commerce/kamer e-commerce.db` |
| Geldstroom Regie | `Team Knowledge/Geldstroom Regie/geldstroom-regie.db` |
| Core / Infrastructure | `Team Knowledge/team-knowledge.db` |

---

## Persoonlijk domein (PKM)

| Doel | Pad |
|---|---|
| PKM root | `PKM/` |
| Journal (canonical) | `PKM/Journal/YYYY/MM/` |
| Journal bestandsnaam | `YYYYMMDD_onderwerp 1, onderwerp 2.md` |
| Images | `PKM/Images/YYYY/MM/` |
| Documents root | `PKM/Documents/` |
| Documents — Key Elements | `PKM/Documents/Key Elements/KE-Naam/` |
| Documents — Projects | `PKM/Documents/Projects/` |
| Documents — Habits | `PKM/Documents/Habits/` |
| Documents — Ideas | `PKM/Documents/Ideas/` |
| CRM People | `PKM/CRM/People/` |
| CRM Organizations | `PKM/CRM/Organizations/` |
| My Life root | `PKM/My Life/` |
| Goals | `PKM/My Life/Goals/G-Titel/` |
| Projects | `PKM/My Life/Projects/P-Naam/` |
| Topics | `PKM/My Life/Topics/T-Naam.md` |
| Key Elements | `PKM/My Life/Key Elements/KE-Naam.md` |
| Habits | `PKM/My Life/Habits/H-Naam.md` |
| Ideas | `PKM/My Life/Ideas/` |
| SOPs (persoonlijk) | `PKM/SOPs/` |

---

## Business domeinen

| Domein | BKM root | Projects | Key Elements | Topics | Ideas |
|---|---|---|---|---|---|
| Kamer E-commerce | `Team Knowledge/Kamer E-commerce/` | `Team Knowledge/Kamer E-commerce/Projects/` | `Team Knowledge/Kamer E-commerce/Key Elements/` | `Team Knowledge/Kamer E-commerce/Topics/` | — |
| Geldstroom Regie | `Team Knowledge/Geldstroom Regie/` | `Team Knowledge/Geldstroom Regie/Projects/` | `Team Knowledge/Geldstroom Regie/Key Elements/` | `Team Knowledge/Geldstroom Regie/Topics/` | `Team Knowledge/Geldstroom Regie/Ideas/` |

---

## Deliverables

Flat structuur — geen domeinsubmappen.

```
Deliverables/YYYYMMDD_Domain_beschrijving/
Deliverables/Archive/
```

Voorbeelden:
- `Deliverables/20260516_Personal_ouderschapsplan/`
- `Deliverables/20260516_Kamer E-commerce_product launch/`
- `Deliverables/20260516_Geldstroom Regie_one-pager/`

**Regel:** domein staat in de mapnaam, nooit als submap.

**Deliverable lifecycle:** Active = in `Deliverables/`. Done = in `Deliverables/Archive/`. The folder name is the record. No database registration required.

---

## Pad-wijziging protocol

Wanneer een pad in dit bestand wijzigt:

1. Pas dit bestand aan (GL-004) — dit is stap 1, altijd
2. Grep de vault op het oude pad: alle `.md`-bestanden in `Team/`, `Team Knowledge/`, `PKM/My Life/`, `CLAUDE.md`
3. Pas elke treffer aan naar het nieuwe pad
4. Bevestig aan de owner welke bestanden zijn bijgewerkt
5. Controleer of de fysieke mapstructuur overeenkomt (`ls` op de relevante locatie)

Larry voert dit protocol uit. Geen agent wijzigt een pad zonder dit protocol te volgen.

---

## Changelog

- 2026-06-03 (Larry, B-005A): Added Workstream routing rule (Core vs Domain distinction). Added this Changelog section. Approved by Owner Walter Kamer.
