# SOP Canonical Location Review — v01
Date: 2026-06-29
Scope: SOP folder structure and path references only. No files changed except this deliverable.
Iris review requested: Yes — see Section 10.

---

## 1. Existing SOP Folders Found

| Folder | Exists | Purpose |
|--------|--------|---------|
| `Team Knowledge/SOPs/` | No — does not exist | Proposed canonical home |
| `Team Knowledge/Core/SOPs/` | Yes | Current home for all team-wide SOPs |
| `Team Knowledge/Kamer E-commerce/SOPs/` | Yes | Domain-specific SOPs for Kamer E-commerce |
| `Team Knowledge/Geldstroom Regie/SOPs/` | Yes | Domain-specific SOPs for Geldstroom Regie |

The proposed canonical location does not exist. All live references point to `Team Knowledge/Core/SOPs/`.

---

## 2. Existing SOP Filenames and Numbering Per Folder

### Team Knowledge/Core/SOPs/

| File | Notes |
|------|-------|
| SOP-001_Disaster recovery.md | — |
| SOP-002_How to do deep online research.md | Number reserved — do not reuse |
| SOP-003_How to hire a new team member.md | — |
| SOP-005_Task management.md | SOP-004 absent (archived or never created) |
| SOP-006_Project management.md | — |
| SOP-008_Read own journal before task.md | SOP-007 absent |
| SOP-009_Write journal entry after task.md | — |
| SOP-012_Daily Planning v3 flow.md | SOP-010, SOP-011 absent |
| SOP-013_365academy bestanden hernoemen.md | — |
| SOP-014_Claude Code session context hygiene.md | — |
| SOP-015_System File Change Proposal Procedure.md | — |
| SOP-017_vertical-slice-gherkin.md | SOP-016 absent |
| SOP-018_tdd-build.md | — |
| SOP-index.md | Index file |
| Archive/ | Subfolder |

**Highest number in use:** SOP-018. Next available for a new SOP: **SOP-019**.

### Team Knowledge/Kamer E-commerce/SOPs/

| File |
|------|
| SOP-002_Product discovery naar live.md |
| SOP-003_Editorial image genereren via ChatGPT DALL-E.md |

### Team Knowledge/Geldstroom Regie/SOPs/

| File |
|------|
| SOP-001_Geldstroom Regie methodiek.md |
| SOP-002_Geldstroom Scan.md |
| SOP-003_Geldstroom Reset.md |
| SOP-004_Geldstroom Implementatie.md |

Domain SOPs use their own numbering sequences. These are not team-wide SOPs and are not in scope for migration.

---

## 3. All References Found to Team Knowledge/Core/SOPs/

**Live system files (not Archive):**

| File | Category |
|------|----------|
| `Team/Nolan - The HR Specialist/AGENT.md` | Agent |
| `Team/Iris - The Governance Gatekeeper/AGENT.md` | Agent |
| `Team/Devon - The Senior Full-Stack Developer/AGENT.md` | Agent |
| `Team/Sloane - The Delivery Lead/AGENT.md` | Agent |
| `Team/Pax - The Research Specialist/AGENT.md` | Agent |
| `Team Knowledge/Core/Guidelines/GL-004_Canonical paths.md` | Canonical reference |
| `Team Knowledge/Core/Guidelines/GL-014_AI Team Governance.md` | Governance |
| `Team Knowledge/Core/Guidelines/GL-010_Session logs purpose and discipline.md` | Guidelines |
| `Team Knowledge/Core/Documents/00_START_HERE_myPKA_Governance_and_Auto-Learning_Readiness.md` | Reference doc |
| `Team Knowledge/Core/Documents/Idea-to-Implementation Governance Pack Design Decisions and Amendment History.md` | Historical reference |
| `Team Knowledge/Core/Documents/Idea-to-Implementation Governance Pack Regression Test Reference.md` | Reference doc |
| `Team Knowledge/Core/SOPs/SOP-index.md` | Self-referential |
| `Team Knowledge/Core/SOPs/Archive/SOP-017_...md` | Archived SOP |
| `Team Knowledge/Core/session-logs/2026/06/20260603_...md` | Session log (historical) |
| `Team Knowledge/Core/CLAUDE-backup-20260617.md` | Backup (inactive) |
| `.claude/commands/improve-system.md` | Skill/command |
| `.claude/commands/close-end-of-day-routine.md` | Skill/command |

**Total live referencing files:** 17 (excluding Archive deliverables)

**CLAUDE.md:** Does not currently reference `Team Knowledge/Core/SOPs/` by path. The Where Things Live table refers only to `Team Knowledge/` generically.

---

## 4. All References Found to Team Knowledge/SOPs/

**Live files:** None.
**Archive deliverables only:** References found in archived documents — none authoritative.

The proposed canonical path has zero live references. There is no split-state today. All references are to `Team Knowledge/Core/SOPs/`.

---

## 5. Proposed Canonical Rule

`Team Knowledge/SOPs/` is the SSOT for all team-wide SOPs.

This means:
- New team-wide SOPs are created in `Team Knowledge/SOPs/`.
- Existing SOPs in `Team Knowledge/Core/SOPs/` migrate on a schedule to be determined.
- Domain-specific SOPs (`Kamer E-commerce/SOPs/`, `Geldstroom Regie/SOPs/`) stay in their domain folders and are not affected.
- `SOP-index.md` moves with the SOPs or is recreated at the new location.

---

## 6. Migration Options

### Option A — Declare canonical rule only, no physical changes

Update `CLAUDE.md` and `GL-004_Canonical paths.md` to state: new SOPs go to `Team Knowledge/SOPs/`. Leave existing SOPs in `Team Knowledge/Core/SOPs/` and leave all references unchanged.

**Risk:** Split state from day one. New SOPs land in `Team Knowledge/SOPs/`, existing ones stay in `Team Knowledge/Core/SOPs/`. Agents following the old canonical path miss new SOPs. Agents following the new canonical path miss existing ones. Increases over time.

**Verdict:** Not recommended. Creates immediate divergence.

---

### Option B — Declare canonical rule, create folder, defer physical migration

1. Update `CLAUDE.md` and `GL-004` to declare `Team Knowledge/SOPs/` as canonical.
2. Create the `Team Knowledge/SOPs/` folder (placeholder or with SOP-index stub).
3. Physical file moves and reference updates are a separate tracked action.

**Risk:** During the gap between step 2 and the physical migration, the canonical path exists but is empty. Any agent reading the index finds nothing. Moderate confusion risk. Acceptable if the migration is scoped and scheduled immediately.

**Verdict:** Viable if physical migration is the very next action in the same task.

---

### Option C — Full migration now

1. Create `Team Knowledge/SOPs/`.
2. Move all 13 SOP files + SOP-index + Archive subfolder from `Team Knowledge/Core/SOPs/` to `Team Knowledge/SOPs/`.
3. Update all 17 live referencing files.
4. Update `CLAUDE.md` Where Things Live table.
5. Remove or redirect the now-empty `Team Knowledge/Core/SOPs/` folder.

**Risk:** Wide blast radius — 17 files to update. High probability of missing at least one reference. Should be done by a single scoped agent action with a verification pass. Not suitable for this session given the current narrow scope.

**Verdict:** Correct eventual outcome. Too wide for this session.

---

## 7. Recommended Smallest Safe Next Step

**Recommended: Option B — scoped to two files, migration scoped immediately after.**

Step 1 (this session if owner approves): Update `CLAUDE.md` and `GL-004_Canonical paths.md` to declare `Team Knowledge/SOPs/` as canonical. Create the folder.

Step 2 (immediately after, same or next session): Physical migration — move all Core/SOPs files to SOPs/, update all 15 remaining referencing files in one Kai-scoped action.

Rationale: The canonical rule must be written before any new SOP is created (including the Project Creation SOP). Option B gets that rule in place with only 2 file edits. The physical migration is a separate action with a clear, auditable scope. This keeps the current session narrow.

---

## 8. Files That Would Need Changing If Owner Approves

### Step 1 — Declare canonical rule (2 files + 1 folder)

| Action | Target |
|--------|--------|
| Edit | `CLAUDE.md` — update Where Things Live table: add `Team-wide SOPs → Team Knowledge/SOPs/` |
| Edit | `Team Knowledge/Core/Guidelines/GL-004_Canonical paths.md` — update SOP canonical path |
| Create folder | `Team Knowledge/SOPs/` |

### Step 2 — Physical migration (separate action, 15 files + file moves)

| Action | Target |
|--------|--------|
| Move 13 SOP files + SOP-index + Archive/ | `Core/SOPs/` → `SOPs/` |
| Edit | 5 AGENT.md files (Nolan, Iris, Devon, Sloane, Pax) |
| Edit | GL-010, GL-014 |
| Edit | 3 Documents files (00_START_HERE, Governance Pack Design Decisions, Regression Test Reference) |
| Edit | `.claude/commands/improve-system.md` |
| Edit | `.claude/commands/close-end-of-day-routine.md` |
| Leave as-is | `CLAUDE-backup-20260617.md` (inactive backup) |
| Leave as-is | Session log from 20260603 (historical, no runtime effect) |

---

## 9. Things Not Touched in This Review

- No files were edited.
- No files were moved.
- No files were created except this review deliverable.
- No CLAUDE.md changes made.
- No AGENT.md files inspected beyond confirming they reference `Core/SOPs`.
- No SOP content read beyond titles and numbers.
- Domain SOPs (Kamer E-commerce, Geldstroom Regie) are out of scope for migration.
- No databases touched.
- No session close executed.
- No Project Creation SOP created or drafted.
- No governance redesign performed.

---

## 10. Iris Review Request

This review touches SOP structure, canonical path references in `GL-004`, CLAUDE.md references, and AGENT.md files. Iris review is required before execution.

**Routing to Iris in this session for four-element Owner-facing review.**

Iris brief:

```
Task: Review the SOP Canonical Location Review (20260629_sop-canonical-location-review-v01.md) before Owner decides on execution.
Trigger: no trigger
Context: Owner decision is to adopt Team Knowledge/SOPs/ as the canonical SSOT for team-wide SOPs, replacing the current Team Knowledge/Core/SOPs/. A review deliverable has been written. It covers: existing folder state, SOP inventory, reference map (17 live files), three migration options, and a recommended smallest safe next step (Option B). No files have been changed.
Output: Four-element Owner-facing review: (1) governance risk assessment, (2) structural correctness check, (3) decision recommendation (proceed / correct / hold), (4) any blocking concerns before Step 1 execution is authorized.
Done looks like: Iris produces one Owner-facing review block covering all four elements.
Minimum viable: Flag any risks the review missed. Confirm or correct the recommended option. Keep it short.
Good is good enough. Do not redesign the migration. Review what is written.
```
