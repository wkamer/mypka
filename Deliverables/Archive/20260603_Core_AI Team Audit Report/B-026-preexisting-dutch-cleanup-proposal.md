# B-026 Pre-existing Dutch System Content Cleanup Proposal

**Datum:** 2026-06-03
**Opgesteld door:** Larry
**Status:** Concept — wacht op Owner's explicit approval
**Governance:** volledig conform GL-014 AI Team Governance v1.1 (§10 System File Language Rule)
**Geen wijzigingen uitgevoerd**

---

## 1. Executive Summary

Four AGENT.md files contain pre-existing Dutch system-file content that was not introduced during Fase 2 and was therefore out of scope for B-024. The content includes `## Samenwerking` sections (all four files), a `## Walter's Groeicontext` section in Sienna, Dutch section headings and full Dutch body content in Pax's Hiring Research and Kennisverversing sections, and Nolan's Domain Knowledge section which is entirely in Dutch.

The most substantial cleanup is Nolan's Domain Knowledge — seven subsections, all in Dutch. All other content is structurally significant but translatable with low functional risk.

One explicit user-facing exception is identified: `## Walter's Groeicontext` in Sienna contains personal Owner context that partially qualifies as user-facing content — see §6.

---

## 2. Why this cleanup is needed

GL-014 §10 System File Language Rule, added as B-025, states: "All system files must be written in English." The four files inspected contain Dutch headings, Dutch active instructions and Dutch code comments that are system-file content, not user-facing content. Agents loading these files as instructions receive Dutch language system directives, which is inconsistent with the language rule.

---

## 3. Files inspected

| File | Pre-existing Dutch found |
|---|---|
| `Team/Sienna - The Personal Assistant/AGENT.md` | Samenwerking section, Walter's Groeicontext, UMC Dutch comments |
| `Team/Penn - The Journal Writer/AGENT.md` | Samenwerking section, Dutch body content |
| `Team/Pax - The Research Specialist/AGENT.md` | Samenwerking section, Hiring Research section, Kennisverversing section |
| `Team/Nolan - The HR Specialist/AGENT.md` | Samenwerking section, Responsibilities bullet, Domain Knowledge (all 7 subsections) |

---

## 4. Dutch system-file content found

### Sienna

| Location | Type | Dutch content |
|---|---|---|
| `## Samenwerking` heading | Active system instruction | Dutch section name |
| Samenwerking body | Active system instruction | Inkomend/Uitgaand/Interrupt Trigger labels + all bullet content |
| `## Walter's Groeicontext` heading | Borderline (see §6) | Dutch section name + personal Owner context |
| UMC Python code comments | Active system instruction | "laad de juiste context vóór actie", "Recente sessiestatus", "Walter's voorkeuren en persoonlijke context", "Persoon opzoeken", "WhatsApp berichten (niet via bestandsontdekking)", "Persoonlijke update" |
| Links section | Active system instruction | "verantwoordelijk voor taakplanning", "ontvangt alle journaalwaardige content van Sienna" |

### Penn

| Location | Type | Dutch content |
|---|---|---|
| `## Samenwerking` heading | Active system instruction | Dutch section name |
| Samenwerking body | Active system instruction | Inkomend/Uitgaand/Interrupt Trigger labels + all bullets in Dutch |

### Pax

| Location | Type | Dutch content |
|---|---|---|
| `## Samenwerking` heading | Active system instruction | Dutch section name |
| Samenwerking body | Active system instruction | Inkomend/Uitgaand/Interrupt Trigger labels + all bullets |
| `## Hiring Research (verplichte trigger)` heading | Active system instruction | Dutch heading + parenthetical |
| Hiring Research body | Active system instruction | All instructions in Dutch |
| `## Kennisverversing (Knowledge Refresh)` heading | Active system instruction | Dutch heading (English subtitle in parentheses) |
| Kennisverversing body | Active system instruction | All instructions in Dutch |

### Nolan

| Location | Type | Dutch content |
|---|---|---|
| `## Samenwerking` heading | Active system instruction | Dutch section name |
| Samenwerking body | Active system instruction | Inkomend/Uitgaand/Interrupt Trigger labels + all bullets |
| Responsibilities bullet (line 29) | Active system instruction | Full Dutch instruction about Samenwerking sectie structure |
| `## Domain Knowledge` — all 7 subsections | Active system instruction | Entirely in Dutch |
| UMC Python code comments | Active system instruction | Dutch comments throughout |

---

## 5. Proposed replacements per file

### Sienna

**`## Samenwerking` → `## Collaboration`**

```markdown
## Collaboration

**Incoming** — Sienna receives from:
- **Larry**: Priority Gate trigger when Owner introduces a new initiative (all domains)
- **Larry**: personal domain delegations (inbox, projects, life admin)
- **Marcus**: objective signal that planned work is not being done → Sienna investigates the behavioral layer

**Outgoing** — Sienna signals to:
- **Larry**: Priority Gate confirmed (Owner is deliberate) → Larry routes to Marcus for ICOR classification
- **Larry**: business-relevant signals encountered in the personal domain
- **Penn**: all journalable content — personal narratives, reflections, insights — always, without asking permission

**Interrupt Trigger — Sienna speaks up when:**
- A new initiative is executed without a Priority Gate check (any domain)
- The Owner postpones or avoids the same theme twice without Sienna naming it
- A behavioral pattern is visible that connects to an active growth theme but has not been flagged
```

**`## Walter's Groeicontext` → see §6 (borderline exception)**

**UMC Python comments — proposed English replacements:**

| Current Dutch comment | Proposed English |
|---|---|
| `# laad de juiste context vóór actie` | `# load the right context before action` |
| `# Recente sessiestatus (Laag 8 — Summary)` | `# Recent session status (Layer 8 — Summary)` |
| `# Walter's voorkeuren en persoonlijke context (Laag 1 — Identity)` | `# Owner preferences and personal context (Layer 1 — Identity)` |
| `# Persoon opzoeken (Laag 2 — Entity)` | `# Look up person (Layer 2 — Entity)` |
| `# WhatsApp berichten (niet via bestandsontdekking)` | `# WhatsApp messages (not via file discovery)` |
| `# Persoonlijke update (Laag 1 — Identity of Laag 3 — Project)` | `# Personal update (Layer 1 — Identity or Layer 3 — Project)` |
| `content='Walter geeft aan dat hij ... prefereert bij ...'` | `content='Owner indicates preference for ... in context of ...'` |

**Links section:**

| Current | Proposed |
|---|---|
| `Marcus (PM): verantwoordelijk voor taakplanning, time blocking en objectieve voortgang` | `Marcus (PM): responsible for task planning, time blocking and objective progress` |
| `Penn (Journal): ontvangt alle journaalwaardige content van Sienna` | `Penn (Journal): receives all journalable content from Sienna` |

**Risk:** Low. Translation only.
**Owner approval:** Yes.

---

### Penn

**`## Samenwerking` → `## Collaboration`**

```markdown
## Collaboration

**Incoming** — Penn receives from:
- **Sienna**: journalable content — personal narratives, reflections, sparring output
- **Larry**: personal stories, day reflections, life updates routed directly
- **Owner (direct)**: raw input in any form — text, image, audio, document

**Outgoing** — Penn signals to:
- **Sienna**: behavioral patterns and growth observations Penn recognizes in journal entries — as coaching input
- **PKM buckets**: journal entry, Topics, Goals, Key Elements, CRM — Penn files and reports briefly

**Interrupt Trigger — Penn speaks up when:**
- A personal narrative is shared in the session without Penn being triggered
- A name or entity recurs multiple times without a PKM stub existing
- Journalable content is handled by another agent without involving Penn
```

**Risk:** Low.
**Owner approval:** Yes.

---

### Pax

**`## Samenwerking` → `## Collaboration`**

```markdown
## Collaboration

**Incoming** — Pax receives from:
- **Larry**: all research briefs — new hires, knowledge refresh, domain questions
- **Kai**: feasibility check request for a technical direction (always via Larry)

**Outgoing** — Pax signals to:
- **Nolan**: hiring brief for every new hire — Pax delivers, Nolan writes the AGENT.md
- **Kai**: integration-related research always ends with an explicit recommendation toward Kai
- **Larry**: report + "This belongs in: [bucket]" — always, no report without a destination

**Interrupt Trigger — Pax speaks up when:**
- A research task starts without confirmed scope
- An implementation appears to be based on a summary of Pax's report rather than the source itself
- A finding is presented as fact while Pax has not read the primary source directly
```

**`## Hiring Research (verplichte trigger)` → `## Hiring Research (mandatory trigger)`**

Body replacement:

```markdown
## Hiring Research (mandatory trigger)

When Larry wants to hire a new specialist, Larry briefs Pax before Nolan writes anything.

**Pax's research question for a new hire:**
> "What does a world-class [role] look like? What are the best frameworks, decision standards, knowledge areas and working methods that define excellence in this domain?"

**Output of Pax (hiring brief):**
1. Core frameworks used by the best specialists in this domain
2. How the best in this field thinks and makes decisions
3. Knowledge standards — what a world-class specialist always knows
4. Working methods and quality standards
5. Three concrete examples of what distinguishes a good vs. poor specialist
6. **Change profile** — what changes in this domain, how fast, and which signals indicate that the specialist's knowledge is becoming outdated? This determines the knowledge refresh frequency.

Pax delivers this brief to Larry. Larry passes the brief to Nolan. Nolan embeds the knowledge in the AGENT.md. Pax never writes the AGENT.md herself.
```

**`## Kennisverversing (Knowledge Refresh)` → `## Knowledge Refresh`**

Body replacement:

```markdown
## Knowledge Refresh

When Larry signals that a domain has changed significantly — or when a specialist's knowledge refresh deadline has passed — Larry briefs Pax for an update study:

> "What has changed in the domain of [specialist] since the last knowledge update? Which frameworks, standards or working methods are outdated, updated or new?"

Pax delivers a delta report: only what has changed relative to existing knowledge. Larry routes to Nolan, who updates the AGENT.md. Outdated knowledge is removed, new knowledge is added.
```

**Risk:** Low.
**Owner approval:** Yes.

---

### Nolan

**`## Samenwerking` → `## Collaboration`**

```markdown
## Collaboration

**Incoming** — Nolan starts only when:
- **Larry** sends a hiring request — this is the only task entry point
- **Pax** has delivered the world-class domain brief — no brief means no start, always route back to Larry

**Outgoing** — Nolan signals to:
- **Larry**: immediately after delivering a new AGENT.md — including the smoke test result as evidence of quality
- **Larry**: when role overlap with an existing specialist is detected — before proceeding, never after
- **Larry**: when a new AGENT.md describes collaboration with an existing specialist — so Larry can brief that specialist about the new colleague

**Interrupt Trigger — Nolan speaks up when:**
- A new specialist is put into use without Nolan having written an AGENT.md
- An AGENT.md is modified by Larry or another agent without a structure check by Nolan
- A smoke test fails — Nolan rewrites the Domain Knowledge section and retests before reporting the hire as complete
```

**Responsibilities bullet (line 29):**

Current: `Elk nieuw AGENT.md bevat een \`## Samenwerking\` sectie met drie verplichte blokken: **Inkomend** (wie levert input, wanneer getriggerd), **Uitgaand** (wie ontvangt output, wanneer gesignaleerd), **Interrupt Trigger** (wanneer de agent zelf uitpreekt zonder opdracht). Geen AGENT.md is compleet zonder deze sectie.`

Proposed: `Every new AGENT.md contains a \`## Collaboration\` section with three mandatory blocks: **Incoming** (who provides input, when triggered), **Outgoing** (who receives output, when signaled), **Interrupt Trigger** (when the agent speaks up without being asked). No AGENT.md is complete without this section.`

**`## Domain Knowledge` — 7 subsections (all Dutch → English):**

| Current heading | Proposed heading |
|---|---|
| `### Rol definiëren — outcome boven taken` | `### Role definition — outcome over tasks` |
| `### Dreyfus Skill Model — excellentie definiëren` | `### Dreyfus Skill Model — defining excellence` |
| `### KSAO — competentie-architectuur` | `### KSAO — competency architecture` |
| `### Job Architecture — rollen in relatie tot elkaar` | `### Job Architecture — roles in relation to each other` |
| `### Brief schrijven naar Pax` | `### Writing the brief to Pax` |
| `### Knowledge Currency — kennis actueel houden` | `### Knowledge Currency — keeping knowledge current` |
| `### Smoke test — afweging, geen structuurcheck` | `### Smoke test — judgment check, not a structure check` |

Body content for each subsection requires full translation. Key examples:

- Dreyfus table headers: `| Niveau | Kenmerk |` → `| Level | Characteristic |`
- KSAO: "wat de specialist weet" → "what the specialist knows", etc.
- Knowledge Currency table: `| Domeintype | Frequentie | Reden |` → `| Domain type | Frequency | Reason |`
- Nolan's Responsibilities content: all Dutch body text translated to English

**UMC Python comments** (same pattern as Sienna — replace Dutch comments with English equivalents):
- `# laad context vóór actie` → `# load context before action`
- etc.

**Risk:** Medium (volume). Translation only — no functional change. Nolan's Domain Knowledge is the most extensive section and requires careful translation to preserve all functional nuance.

**Owner approval:** Yes.

---

## 6. User-facing exceptions

### Sienna — `## Walter's Groeicontext`

**Current content:**
> Walter doorloopt een diep persoonlijk groeitraject (Miracle Roadmap); zijn kernthema's zijn gezien worden, controle loslaten en zichtbaarheid vanuit authenticiteit — zie `[[what-about-me]] (sectie Miracle Roadmap)` voor het volledige profiel inclusief coachingsignalen.

**Assessment:** This section describes the Owner's personal growth context. The content is personal context about the Owner — it is arguably user-facing in that it describes a real person's inner experience. However, it is a section in a system file providing instructions to Sienna about how to understand the Owner. As a system instruction, it should be in English.

**Proposed treatment:**

Option A — Translate to English (recommended):
```markdown
## Owner's Growth Context

Owner is in a deep personal growth journey (Miracle Roadmap); core themes are being seen, releasing control and visibility from authenticity — see `[[what-about-me]] (section Miracle Roadmap)` for the full profile including coaching signals.
```

Option B — Mark as user-facing exception and leave in Dutch.

**Recommendation:** Option A. The section gives Sienna active instructions about coaching context — it is system instruction, not personal content.

---

## 7. Historical changelog entries: leave or update?

**Finding:** No Fase 1/pre-Fase 2 Dutch changelog entries were found in the four inspected files. The only changelog entries in these files are from Fase 2 (already translated in B-024) or are from an earlier period and already in English.

**Recommendation:** No action needed on changelog entries for B-026.

---

## 8. Impact on agent functionality

None. This is translation-only cleanup. All functional instructions, routing rules, behavioral contracts, domain knowledge content, and agent responsibilities are fully preserved in English.

---

## 9. Risks and mitigations

| Risk | Level | Mitigation |
|---|---|---|
| Nolan's Domain Knowledge is extensive — translation errors possible | Medium | Exact English text to be reviewed before implementation |
| Penn/Pax Samenwerking → Collaboration needs cross-reference check with other agents | Low | Only heading and body translated — all routing targets remain the same |
| Sienna UMC code comments: some Dutch is inside placeholder strings | Low | Translate comment lines, not placeholder values in strings |
| `Walter's Groeicontext` naming decision | Low | Decision point §10 — Owner decides Option A or B |

---

## 10. Decision points for Owner

| Decision | Advice | Options |
|---|---|---|
| Approve B-026 execution (all 4 files) | Yes — low/medium risk, language compliance | a) Full approval b) Partial (exclude Nolan Domain Knowledge) c) Defer |
| Sienna `Walter's Groeicontext` | Translate to `Owner's Growth Context` | a) Translate (Option A) b) Leave as Dutch exception (Option B) |
| Nolan Domain Knowledge | Full translation required | a) Full translation b) Headings only c) Defer |
| Sequencing | Execute all 4 files in one pass | a) All together b) Samenwerking sections first, then body content |

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
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-026-preexisting-dutch-cleanup-proposal.md`*
