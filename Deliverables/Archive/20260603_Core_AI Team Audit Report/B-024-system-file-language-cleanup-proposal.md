# B-024 System File Language Cleanup Proposal

**Datum:** 2026-06-03
**Opgesteld door:** Larry
**Status:** Concept — wacht op Owner's explicit approval
**Governance:** volledig conform GL-014 AI Team Governance v1.1
**Geen wijzigingen uitgevoerd**

---

## 1. Executive Summary

Fase 2 AGENT.md Quality Improvements introduced Dutch content into 6 of 7 system files — primarily in `## Knowledge Currency` sections, Larry's `## Samenwerking` section, and all 7 changelog entries. The Dutch content is functional and correct, but violates the Owner-clarified rule that all system files must be written in English.

The scope of this cleanup is limited and precise: translate Fase 2-added Dutch content to English without altering any functional meaning. All Never Does sections (added in Fase 2) are already in English and require no changes.

---

## 2. Why this cleanup is needed

| Reason | Detail |
|---|---|
| System-file language rule | All system files must be in English — clarified by Owner after Fase 2 implementation |
| Agent context loading | Agents load their AGENT.md as active instructions — Dutch instructions risk misinterpretation or inconsistency |
| Consistency | Other AGENT.md sections and recent governance documents (GL-014) use English |
| Future-proofing | New agents, new hires and system audits expect English system content |

---

## 3. Files inspected

| File | Fase 2 additions | Dutch content found |
|---|---|---|
| Marcus AGENT.md | Never Does, Knowledge Currency | Knowledge Currency: Yes |
| Sienna AGENT.md | Never Does, Knowledge Currency | Knowledge Currency: Yes |
| Penn AGENT.md | Never Does (2 items), Knowledge Currency | Knowledge Currency: Yes |
| Pax AGENT.md | Never Does | Never Does: No — Changelog: Yes |
| Nolan AGENT.md | Never Does | Never Does: Partial (1 term) — Changelog: Yes |
| Larry AGENT.md | Samenwerking | Entirely: Yes |
| Bo AGENT.md | Domain Knowledge, Never Does, Knowledge Currency | Knowledge Currency: Yes |

---

## 4. Dutch system-file content found

### Larry — Samenwerking (B-019)
Full section in Dutch. Headings, labels, and all bullet content.

### Marcus, Sienna, Penn, Bo — Knowledge Currency (B-018/B-020)
All four Knowledge Currency sections use the same Dutch template:
- `**Verversingsfrequentie:**`
- Table headers: `| Wat | Snelheid | Signaal |`
- Table values in Dutch
- `**Update-protocol:**` in Dutch

### All 7 — Changelog entries (B-017/B-018/B-019/B-020)
All 7 changelog entries contain Dutch descriptions:
- "Never Does en Knowledge Currency toegevoegd."
- "Never Does aangevuld (2 items) en Knowledge Currency toegevoegd."
- "Samenwerking-sectie toegevoegd."
- "Domain Knowledge, Never Does en Knowledge Currency toegevoegd."
- "Never Does toegevoegd."

### Nolan — Never Does (partial)
One item contains a Dutch section name used as a system term:
> `- Never writes a specialist without a Samenwerking sectie — this is a hard structural requirement`

**Assessment:** "Samenwerking sectie" functions as a proper noun / section identifier. Recommend translating to "Collaboration section" for full English compliance, but this is a judgment call (see §10).

---

## 5. Proposed replacements per file

### Larry — Samenwerking

**Path:** `Team/Larry - The Orchestrator/AGENT.md`
**Type:** Active system content — Owner approval required

| Current | Proposed |
|---|---|
| `## Samenwerking` | `## Collaboration` |
| `**Inkomend** — Larry ontvangt van:` | `**Incoming** — Larry receives from:` |
| `**Uitgaand** — Larry signaleert naar:` | `**Outgoing** — Larry signals to:` |
| `**Interrupt Trigger — Larry spreekt uit wanneer:**` | `**Interrupt Trigger — Larry speaks up when:**` |

**Full proposed replacement for all bullet content:**

```markdown
## Collaboration

**Incoming** — Larry receives from:
- **Owner**: every request, question, observation — Larry is the sole entry point from the Owner to the team
- **Sienna**: Priority Gate confirmation (Owner is deliberate) → Larry routes to Marcus for ICOR classification
- **Sienna**: business-relevant signals from the personal domain
- **Marcus**: weekly health check results, escalation of blockers, deadlines at risk
- **All specialists**: feedback on delegations — Larry receives, synthesizes and reports back to the Owner

**Outgoing** — Larry signals to:
- **Pax**: research briefs for new hires, knowledge refresh, domain questions
- **Nolan**: hiring assignment once the Pax brief is available
- **Sienna**: Priority Gate trigger for every new Owner initiative
- **Marcus**: project delegations, planning, ICOR classification assignment
- **Penn**: personal narratives and reflections routed directly
- **Kai**: code, scripts, integrations, architecture
- **Domain specialist**: every task that falls within an existing domain

**Interrupt Trigger — Larry speaks up when:**
- A specialist performs domain execution that Larry initiated without proper delegation
- A new Owner initiative moves to execution without a Priority Gate check via Sienna
- A specialist returns with work that does not cover the assignment — Larry redirects, not the Owner
- The weekly sweep shows a task open for more than 14 days without movement
- A SSOT violation or structural drift is discovered at session close
```

**Risk:** Low. Translation only, no functional change.

---

### Marcus — Knowledge Currency

**Path:** `Team/Marcus - The Project Manager/AGENT.md`
**Type:** Active system content — Owner approval required

**Proposed replacement:**

```markdown
## Knowledge Currency

**Refresh frequency:** semi-annually for PM methodologies, immediately upon system changes.

| What | Rate | Signal |
|---|---|---|
| Todoist API (endpoints, fields) | On platform update | API call returns 410 Gone or unexpected behavior |
| PKM conventions (GL-001, GL-004, GL-011) | On system change | New GL files, path changes in GL-004 |
| Team composition (who exists, what they do) | Continuously | New specialist hired or role changed |
| PPM/BPM framework (ICOR classifications) | Semi-annually | Larry introduces new classification criteria |
| Goal structure (active goals, goal periods) | Each planning cycle | Owner adjusts goals in daily planning |

**Update protocol:** Larry briefs Pax → Pax delivers delta report → Nolan applies in this AGENT.md after Owner approval.
```

**Risk:** Low.

---

### Sienna — Knowledge Currency

**Path:** `Team/Sienna - The Personal Assistant/AGENT.md`
**Type:** Active system content — Owner approval required

**Proposed replacement:**

```markdown
## Knowledge Currency

**Refresh frequency:** monthly for personal context, immediately upon API changes.

| What | Rate | Signal |
|---|---|---|
| Owner's personal projects and goals | Continuously | New planning cycle, new initiative via Priority Gate |
| Gmail API (endpoints, draft structure) | On platform update | send_email.py returns error |
| Todoist API (endpoints, project IDs) | On platform update | Task creation fails, project ID not found |
| Owner's growth themes and behavioral patterns | Each journal period | Penn signals new pattern, Owner names new growth area |
| CRM record Owner (relationships, context) | Continuously | New person introduced, relationship changed |

**Update protocol:** Larry briefs Pax for API deltas → Nolan applies. Personal context: Sienna actively reads Penn's recent journal entries and the current growth context in Owner's KE files.
```

**Risk:** Low.

---

### Penn — Knowledge Currency

**Path:** `Team/Penn - The Journal Writer/AGENT.md`
**Type:** Active system content — Owner approval required

**Proposed replacement:**

```markdown
## Knowledge Currency

**Refresh frequency:** semi-annually for journaling methodologies, immediately upon PKM structural changes.

| What | Rate | Signal |
|---|---|---|
| Owner's bucket definition (Bucket Detection) | Semi-annually | Owner introduces new life area, bucket no longer fits |
| PKM structure (folders, Topics, KE files) | On system change | Cross-link target no longer exists, new pattern in GL-004 |
| Active goals and projects (cross-link targets) | Each planning cycle | Goal completed, new project started |
| CRM record (people, relationships) | Continuously | New person introduced via People Detection |
| Writing and processing techniques | Annually | Fundamentals are stable |

**Update protocol:** Larry briefs Pax for methodology updates → Nolan applies. PKM structure: Penn reads GL-004 when uncertain about paths and the topic index for new cross-links.
```

**Risk:** Low.

---

### Bo — Knowledge Currency

**Path:** `Team/Bo - The Market Validator/AGENT.md`
**Type:** Active system content — Owner approval required

**Proposed replacement:**

```markdown
## Knowledge Currency

**Refresh frequency:** semi-annually for validation methodologies, immediately upon market, platform or venture changes.

| What | Rate | Signal |
|---|---|---|
| Validation frameworks | Semi-annually | New validation method or better benchmark available |
| Venture context | On venture change | Owner changes proposition, target audience, pricing model or business model |
| Market sizing methodology | Annually | New market data or segment definition needed |
| Pricing and WTP methodology | Semi-annually | Pricing strategy changes or WTP signals contradict each other |
| Competitive landscape | Per validation assignment | New competitor, substitute or status quo alternative discovered |
| E-commerce and product validation benchmarks | Semi-annually | Conversion benchmarks, CPC, CPA or pre-order signals shift |

**Update protocol:** Larry briefs Pax for methodology or market updates → Pax delivers delta report → Nolan applies in Bo's AGENT.md after Owner approval.
```

**Risk:** Low.

---

### All 7 files — Changelog entries

**Type:** Historical system record — see §6 for recommendation.

| File | Current entry | Proposed replacement |
|---|---|---|
| Marcus | "Never Does en Knowledge Currency toegevoegd." | "Never Does and Knowledge Currency added." |
| Sienna | "Never Does en Knowledge Currency toegevoegd." | "Never Does and Knowledge Currency added." |
| Penn | "Never Does aangevuld (2 items) en Knowledge Currency toegevoegd." | "Never Does supplemented (2 items) and Knowledge Currency added." |
| Pax | "Never Does toegevoegd." | "Never Does added." |
| Nolan | "Never Does toegevoegd." | "Never Does added." |
| Larry | "Samenwerking-sectie toegevoegd." | "Collaboration section added." |
| Bo | "Domain Knowledge, Never Does en Knowledge Currency toegevoegd." | "Domain Knowledge, Never Does and Knowledge Currency added." |

---

### Nolan — Never Does item (partial)

**Current:** `- Never writes a specialist without a Samenwerking sectie — this is a hard structural requirement`

**Proposed:** `- Never writes a specialist without a Collaboration section — this is a hard structural requirement`

**Note:** "Samenwerking" functions as a section name across the team's AGENT.md files. If Owner decides to keep "Samenwerking" as the canonical section name (a deliberate Dutch proper noun), this item stays as-is. If the section is renamed to "Collaboration" in Larry's AGENT.md, this item should follow. See §10.

---

## 6. Historical changelog entries: leave or update?

**Recommendation: Update.**

Rationale: The changelog entries from Fase 2 (dated 2026-06-03) are recent and describe system changes. They are part of the AGENT.md system file, not standalone historical documents. Translating the description text (not the date, agent name, or approval statement) aligns them with the language rule without altering their audit meaning.

The date, agent attribution, backlog ID and "Approved by Owner" statement remain unchanged. Only the Dutch description words are translated.

**Exception:** The historical entry in GL-014 (`Goedgekeurd door Walter`) is already preserved per the GL-014 B-022 decision. That precedent does not apply here — these changelog entries are in AGENT.md system files, not in a governance document.

---

## 7. Impact on Fase 2 functionality

None. This is a translation-only cleanup. All functional improvements from Fase 2 are preserved:

| Fase 2 improvement | Status after B-024 |
|---|---|
| Never Does sections (all agents) | Unchanged — already in English |
| Bo's Domain Knowledge | Unchanged — already in English |
| Bo's Never Does | Unchanged — already in English |
| Knowledge Currency sections (functional logic) | Preserved — only Dutch labels translated |
| Larry's Collaboration section (functional routing) | Preserved — Dutch headings translated, routing logic unchanged |
| Penn's Never Does additions | Unchanged — already in English |

---

## 8. Risks and mitigations

| Risk | Level | Mitigation |
|---|---|---|
| Mistranslation alters functional meaning | Low | Exact proposed text provided — review before approve |
| "Samenwerking" as proper noun vs translated term | Low | Decision point §10 — Owner decides |
| Sienna/Penn have pre-existing Dutch Samenwerking sections (outside Fase 2 scope) | Out of scope | These are noted here; cleanup is a separate future proposal if desired |
| Pax has pre-existing Dutch in Hiring Research section (outside Fase 2 scope) | Out of scope | Noted; separate future proposal |
| Nolan has pre-existing Dutch in Domain Knowledge section (outside Fase 2 scope) | Out of scope | Noted; separate future proposal |

---

## 9. B-025 recommendation: formalize language rule in GL-014

**Recommendation: Do B-025 before or together with B-024.**

Rationale: If B-024 is executed without a formalized rule in GL-014, the language requirement exists only as an Owner instruction in conversation — not as an authoritative governance rule. Future Nolan implementations or system additions may re-introduce Dutch without knowing the rule exists.

**Proposed addition to GL-014 §1 Approval-gates (or as a new §10 Language Rule):**

```markdown
## 10. System file language rule

All system files must be written in English. System files include: AGENT.md files, SOPs, Guidelines, Workstreams, CLAUDE.md, changelog entries, logs, governance documents, AI-team templates, and integration documentation.

Only user-facing content may be written in Dutch. User-facing content includes: Todoist task names, journal entries, and direct Owner communication.
```

**Sequencing options:**

| Option | Sequence | Pros | Cons |
|---|---|---|---|
| A | B-025 first, then B-024 | Rule is authoritative before cleanup | One extra approval round |
| B | B-025 and B-024 simultaneously | One approval round, rule and cleanup land together | Slightly more complex single approval |
| C | B-024 first, then B-025 | Cleanup done quickly | Rule not formally established until after |

**Advice:** Option B — simultaneous. Both are low-risk, both are small, and landing them together creates an atomic state: rule + compliance at the same moment.

---

## 10. Decision points for Owner

| Decision | Advice | Options |
|---|---|---|
| Approve B-024 execution | Yes — low risk, language compliance | a) Full approval b) Approval excluding changelog entries c) Defer |
| Update changelog entries | Yes — they are in system files | a) Yes, translate descriptions b) Leave as historical record |
| "Samenwerking" → "Collaboration" as canonical section name | Translate for consistency | a) Rename to Collaboration everywhere b) Keep Samenwerking as proper noun |
| B-025 timing | Simultaneous with B-024 | a) Before b) Simultaneous c) After |
| Scope of future cleanup (pre-existing Dutch in Pax, Nolan, Sienna, Penn Samenwerking sections) | Separate proposal | a) Include in B-024 b) Separate B-026 c) Leave |

---

## 11. Confirmation that nothing was changed

- No AGENT.md files were modified
- No SOPs were modified
- No Guidelines were modified
- No Workstreams were created or modified
- CLAUDE.md was not modified
- No databases were modified
- No integration configurations were modified
- No files were deleted
- No historical deliverables were rewritten
- This document is a read-only proposal in the Deliverables folder only

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-024-system-file-language-cleanup-proposal.md`*
