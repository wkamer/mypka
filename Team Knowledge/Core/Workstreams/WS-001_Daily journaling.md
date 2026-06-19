# WS-001 — Daily Journaling

**Domain:** Core (Personal)
**Trigger:** Owner delivers raw personal input directly, or Larry or Sienna routes a personal narrative, reflection, life update, or observation to Penn.
**Maintainer:** Larry
**Status:** Active

---

## Purpose

Turn raw personal input from Owner Walter Kamer into structured PKM entries. The journal is the Owner's personal memory backbone — every narrative, observation, reflection, or life update lands here and becomes cross-linked into the rest of the PKM wiki.

This Workstream ensures that input capture, filing, cross-linking and memory extraction happen in a consistent, auditable sequence regardless of which agent receives the input first.

---

## Agents

| Agent | Role in this Workstream |
|---|---|
| Larry | Receives Owner input; identifies journalable content; routes to Penn; performs Librarian pass at session close |
| Sienna | Identifies journalable content in personal domain sessions; routes to Penn |
| Penn | Processes all input; writes journal entries; cross-links; files entities; extracts UMC entities; writes session log |

---

## Inputs

- Raw text: personal narrative, reflection, day update, observation, or experience
- Image: screenshot, photo, business card
- Audio: voice note
- Document: PDF, scan

---

## Steps

### Step 1 — Route input to Penn

**Step lead:** Larry or Sienna (whichever receives the input first)
**Trigger:** Owner shares a personal narrative, day reflection, life update, observation, or experience — even mid-conversation on another topic.
**Action:** Route immediately to Penn. Do not process the input before routing. Do not ask permission to route.
**Passes to:** Step 2

---

### Step 2 — Write journal entry

**Step lead:** Penn
**Input:** Raw Owner input

For text input:
1. Write journal entry at `PKM/Journal/YYYY/MM/YYYYMMDD_subject 1, subject 2.md` — this is the only canonical location (see [[GL-004_Canonical paths]])
2. Write in the Owner's language (Dutch if Dutch, English if English)
3. Preserve the Owner's words and expressions; paraphrase only for structure
4. Remove repetitions; complete sentences; group related thoughts
5. Do not add opinions, interpretations or conclusions the Owner did not express
6. Create `YYYY/MM/` parent folders if they do not exist

For image input:
1. Save file to `PKM/Images/YYYY/MM/YYYYMMDD_description.ext`
2. Embed in journal entry: `![[Images/YYYY/MM/YYYYMMDD_description.ext]]`
3. If image shows a person: create or update `PKM/CRM/People/Achternaam, Voornaam.md`
4. If image shows an organization: create or update `PKM/CRM/Organizations/Naam.md`

For audio input:
1. Transcribe; if unable, write `[transcript pending]`
2. Process transcript as text input from step 2a above

For document input:
1. File to `PKM/Documents/` using `YYYYMMDD_Type_Persoon_Detail.ext`
2. Create stub in `PKM/Documents/` and link from journal entry

**Output:** Draft journal entry file
**Passes to:** Step 3

---

### Step 3 — People detection and bucket detection

**Step lead:** Penn

**People detection — for every name found:**
- New name: create stub at `PKM/CRM/People/Achternaam, Voornaam.md`; insert row in `personal.db` table `people` with `needs_review=true`
- Existing name: update `last_contact` in `personal.db` table `people`
- Every mention: insert row in `personal.db` table `contact_interactions` with `interaction_type='journal'`, `summary=one-line description`, `journal_id=inserted journal row id`
- Every mention: add wikilink to journal entry under `## Related to → Journal` in that person's CRM file. See [[GL-009_CRM people link consistency]].
- Gift idea or purchase wish → append to CRM stub as `Gift ideas: <item>`

**Bucket detection — map each signal to the right PKM location:**

| Signal | Destination |
|---|---|
| Interest / recurring subject | `PKM/My Life/Topics/T-Naam.md` |
| Time-bound effort | `PKM/My Life/Projects/P-Naam/` |
| Recurring rhythm or routine | `PKM/My Life/Habits/H-Naam.md` |
| Outcome or aspiration | `PKM/My Life/Goals/` |
| Stable life dimension | `PKM/My Life/Key Elements/KE-Naam.md` |
| Someday travel idea | `PKM/My Life/Ideas/I-Travel.md` |
| Someday experience idea | `PKM/My Life/Ideas/I-Experiences.md` |
| Someday purchase idea | `PKM/My Life/Ideas/I-Purchases.md` |
| Real-world document | `PKM/Documents/` |
| Image | `PKM/Images/YYYY/MM/` |

For Topics: add one-line entry under **What I am exploring right now** and append a dated line to **Mentions log** linking to the journal entry. If no matching topic exists, create `T-Naam.md` using the standard topic template.

Stub creation rule: if the entity has a name the Owner will refer to again, create the stub. When in doubt, create it.

**Output:** Journal entry with resolved wikilinks; PKM stubs created or updated
**Passes to:** Step 4

---

### Step 4 — Database insert

**Step lead:** Penn
**Action:**
1. Run schema check: verify actual column names in `journal` table — the date column is `entry_date`, not `date`. Never assume column names.
2. Insert one row into `PKM/personal.db` table `journal` (`entry_date`, `title`, `entry_type`, `summary`)

**Output:** DB row inserted
**Passes to:** Step 5

---

### Step 5 — UMC entity extraction

**Step lead:** Penn

**Interpreter:** `/opt/mypka-memory/venv/bin/python`

```python
import sys, os
sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
from memory_config import get_dsn
os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
from memory_manager import get_manager
mm = get_manager()

# Extract entities from journal entry (Layer 2 — Entity)
entities = mm.extract_and_store_entities(journal_entry_text)

# Store insight as conversation memory (Layer 6 — Conversation)
mm.icor_refine(
    layer='conversation',
    content='Insight: [pattern or observation from the entry].',
    agent='penn',
    topic='journal-insight',
    date_ref='YYYY-MM-DD'
)
```

If UMC is unreachable: skip and report "⚠️ UMC niet bereikbaar" to the Owner. Report entity count only if >0.

**Output:** Entities stored in UMC; conversation layer updated
**Passes to:** Step 6

---

### Step 6 — Close journal entry: learning reflections and KE-check

**Step lead:** Penn
**Action:**
1. Close the journal entry with 1–3 learning reflections: patterns observed, open questions, connections to goals/topics/people. These are Penn's observations, not the Owner's words.
2. Mandatory KE-check: verify whether the entry connects to an active Key Element in `PKM/My Life/Key Elements/` and add the connection if applicable.

**Output:** Journal entry complete with reflections and KE connection
**Passes to:** Step 7

---

### Step 7 — Session log

**Step lead:** Penn
**Action:** Write one row to `Team Knowledge/team-knowledge.db` table `session_logs` with `agent_slug="penn"`.

**Output:** Session log row written
**Passes to:** Step 8 (Larry — at session close)

---

### Step 8 — Librarian pass

**Step lead:** Larry
**Trigger:** Session close
**Action:**
1. Verify all `[[wikilinks]]` in the new journal entry resolve
2. Confirm images sit in `PKM/Images/YYYY/MM/`, not duplicated elsewhere
3. Confirm each new stub is listed in its section's index file where applicable
4. Flag any SSOT violations to Owner Walter Kamer

**Output:** Structural integrity confirmed or violations flagged to Owner

---

## Outputs

- Journal entry at `PKM/Journal/YYYY/MM/YYYYMMDD_subject 1, subject 2.md`
- Updated PKM stubs (CRM, Topics, Goals, Projects, Habits, Key Elements, Documents as applicable)
- `personal.db` rows: journal insert, people updates, contact_interactions
- UMC: entity and conversation layer updates
- `team-knowledge.db` session log row

---

## What this Workstream does not do

- Does not produce business workflows — business process inputs are routed to the relevant domain agent; Penn writes a short journal note linking to it
- Does not produce research reports — route to Pax
- Does not edit past journal entries — entries are append-only
- Does not replace Sienna's behavioral accountability role
- Does not add interpretations, opinions or conclusions the Owner did not express
- Does not skip any step — bucket detection and wikilink cross-linking run on every input without exception

---

## References

- [[GL-001_File naming conventions]] — filenames for journal entries, images, documents
- [[GL-004_Canonical paths]] — all canonical PKM folder paths
- [[GL-009_CRM people link consistency]] — CRM update rule on every person mention
- [[SOP-008_Read own journal before task]] — Penn reads prior task journal before processing
- [[SOP-009_Write journal entry after task]] — Penn's specialist journal for task-level learnings

---

## Changelog

- 2026-06-03 (Larry, B-005A): Created. Derived from Penn AGENT.md and Larry AGENT.md current state. Approved by Owner Walter Kamer.
