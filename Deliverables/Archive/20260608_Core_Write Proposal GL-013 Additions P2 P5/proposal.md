# Write Proposal — GL-013 Additions P2 and P5

**Prepared by:** Larry, Team Orchestrator  
**Date:** 2026-06-08  
**Authorized by retention assessment:** `Deliverables/20260608_Core_Retention Assessment P2 P5 UMC/assessment.md`  
**Target file:** `Team Knowledge/Core/Guidelines/GL-013_Memory Core Architecture.md`  
**Scope:** Two append-only additions to GL-013. No existing content modified or removed.

---

## Write Plan

| # | Action | Location | Trigger |
|---|---|---|---|
| W-1 | Append new section "Operationeel Model — Specialist UMC Writes" | After the existing `## Beheer` section | Owner: yes |
| W-2 | Append new section "Bekende Hiaten en Toekomstige Uitbreidingen" | After W-1 (end of file) | Owner: yes, same write action |

Both additions are appended to the end of the file. No existing lines are changed.

---

## W-1 — Exact Text to Append (P2)

```
---

## Operationeel Model — Specialist UMC Writes

Specialists worden aangeroepen binnen de sessie van Larry. Zij hebben geen eigen
sessiegrens en kunnen daarom niet autonoom `write_summary` aanroepen bij het afsluiten
van een taak.

**Werkwijze:**
- Bij het afronden van een substantiële taak schrijft een specialist één handoff-notitie
  naar de sessiecontext (bijv. "Sasha heeft Shopify-productsync afgerond").
- De close-session routine leest de handoff-notities en schrijft per actief domein in de
  sessie één samengestelde UMC-samenvatting, met de juiste `source_type` per domein.
  Zie [[GL-015_Memory Domain Routing Protocol]] §3 voor de canonieke domain- en
  source_type-waarden per specialist.

De `## UMC`-sectie is om deze reden niet aanwezig in individuele AGENT.md-bestanden.
De close-session routine is het enige schrijfpunt voor `memory_summaries` vanuit
specialist-werk.
```

---

## W-2 — Exact Text to Append (P5)

```
---

## Bekende Hiaten en Toekomstige Uitbreidingen

### UMC Activiteitsmonitoring

Er bestaat momenteel geen mechanisme om te detecteren of de UMC daadwerkelijk
schrijfacties ontvangt. Een domein kan stilvallen zonder dat dit zichtbaar is.

Vereiste: een wekelijkse geautomatiseerde controle die het aantal UMC-entries per domein
per week telt en een alert stuurt naar Discord of Team Inbox wanneer een domein 7 of meer
dagen geen nieuwe entries heeft ontvangen. Implementatie: Kai.
```

---

## Post-Write Verification

After writing: Larry reads back the final 40 lines of GL-013 and confirms both sections
are present and correctly formatted before reporting completion to the Owner.

---

## Effect on Archive Eligibility

After W-1 and W-2 are written and verified:

- P2 (Delegation Model) is captured in GL-013. No unique knowledge remains in the source deliverable for this item.
- P5 (Periodic Validation) is captured in GL-013. No unique knowledge remains in the source deliverable for this item.
- The source deliverable `20260530_Core_UMC diagnose en aanbevelingen` becomes safe to archive.

---

## Owner Decision Required

**Approve this write proposal: yes / no / correction.**

A "yes" authorizes Larry to execute W-1 and W-2 in a single write action and perform the post-write read-back.

No other actions are authorized by this approval.

---

Delivered on: 2026-06-08  
Delivered at: (session)
