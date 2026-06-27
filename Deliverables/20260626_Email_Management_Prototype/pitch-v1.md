# Pitch — Email Management
**Author:** Phoebe
**Date:** 2026-06-27
**Status:** Awaiting owner approval

---

## Problem

The owner processes email reactively in Gmail, with no single place to see what needs action, approve suggested tasks, and disposition each email in one pass.

---

## Appetite

5 owner review rounds (slices). If scope threatens to exceed 5 slices, cut — do not extend.

---

## Breadboard

```
Email Management Page
  [Run Triage]  -->  Email Management Page (pending list refreshed with real data)

Pending List
  [email row: sender, Action or Information badge, Gmail link, subject, date]
                -->  Accordion — expanded

Accordion — expanded
  [Email Summary — AI-generated text, read-only]
  [Actions section — visible for ALL classifications, Action and Information]
    [Task action row: type label "Task" + editable name field (pre-filled with AI suggestion)]
    [Event action row: type label "Event"
                       + editable name field (pre-filled with AI suggestion)
                       + editable date/time field (pre-filled with AI-extracted date/time — always visible so AI extraction is transparent to the owner)]
      [Approve]  -->  task or event executed immediately in SSOT
                      + action row: Approved state (submits edited name and date/time, buttons hidden, badge shown)
                      + Execution Log: entry appended immediately with timestamp (date + time)
      [Decline]  -->  action row: Declined state (buttons hidden, muted label)
  [+ Task]   -->  new empty Task row added (editable name field + Approve/Decline)
               available for Action AND Information emails
  [+ Event]  -->  new empty Event row added (editable name field + date/time selector + Approve/Decline)
               available for Action AND Information emails
  [Execution Log — read-only, cumulative]
    Appears after first Approve. Each entry includes timestamp (date + time).
    Task approved:  "Task [name] created"
    Event approved: "Event [name] — [datetime] added to calendar"
    Disposition:    "Email archived" or "Email deleted" — always the final entry
  [Archive]      -->  blocked until all action rows are Approved or Declined
                      then: email row receives "Processed" label immediately
                      + appends disposition log entry + Gmail archive (SSOT) + moves to Processed
  [Delete]       -->  blocked until all action rows are Approved or Declined
                      then: email row receives "Processed" label immediately
                      + appends disposition log entry + Gmail delete (SSOT) + moves to Processed
  [row header click] --> Accordion — collapsed

Processed List
  Ordering: most recently processed email at top. New items prepend, not append.
  [email row — muted styling, shows "Processed" label]
                -->  Accordion — read-only (summary + execution log visible, no actions)
  Execution log in processed accordion always shows the disposition entry as final line.
  If no Approvals occurred before disposition, the log is only visible here — not shown in pending.
```

---

## Fat Marker Sketch

```
+--------------------------------------------+
|  Email Management              [Run Triage] |
+--------------------------------------------+
|  PENDING · 2                                |
| +------------------------------------------+
| | Jan de Vries  [Action] [↗]               |
| | Factuur april 2026              15 jun   |
| +------------------------------------------+
| | Remko Kamer   [Info]   [↗]               |  <-- EXPANDED
| | +-----------------------------------------+
| | | Email Summary                           |
| | | Remko vraagt om een datum voor het      |
| | | broederweekend. Geen actie vereist.     |
| | |-----------------------------------------|
| | | Actions                                 |
| | | Task  [Stuur datum door aan Remko_____] |
| | |            [Approve]  [Decline]         |
| | | Event [Broederweekend inplannen_______] |
| | |            [Approve]  [Decline]         |
| | |              [+ Task]  [+ Event]        |
| | |-----------------------------------------|
| | | Log                                     |
| | | ✓ Task "Stuur datum door" created       |
| | |-----------------------------------------|
| | |                  [Archive]  [Delete]    |
| | +-----------------------------------------+
| +------------------------------------------+
|                                             |
|  PROCESSED · 1                              |
| +------------------------------------------+
| | noreply@ing.nl  [✓ Processed]  [↗]       |
| | ING afschrift                   14 jun   |
| +------------------------------------------+
```

Notes (not spec — Devon resolves these):
- One accordion open at a time
- Processed rows are visually muted (color treatment Devon's call)
- Badge shows exactly two values: "Action" or "Information" (sketch uses [Info] as abbreviation — Devon uses full label)
- Gmail link opens in new tab, does not trigger accordion toggle

---

## Slices

Each slice is end-to-end and owner-verifiable in under 15 minutes.

**Slice 1 — Email list (static)**
Pending section renders with hardcoded rows. Two-line layout: sender + Action or Information badge + Gmail link on line 1, subject + date on line 2. No accordion. No API. Owner confirms the row structure looks right.

**Slice 2 — Accordion with Email Summary**
Click any pending row opens an inline accordion. Accordion shows the Email Summary field (hardcoded text). Click again collapses. Only one accordion open at a time. Owner confirms the expand/collapse behavior and summary field placement.

**Slice 3 — Actions panel and execution log** *(heaviest slice)*
Accordion shows Actions section below Email Summary for all emails regardless of classification. Action types are Task and Event only. Task rows show: type label + editable name field pre-filled with AI suggestion. Event rows show: type label + editable name field pre-filled with AI suggestion + editable date/time field pre-filled with the AI-extracted date/time. The date/time field is always visible on Event rows; this makes the AI extraction transparent to the owner. The owner can edit both the name and the date/time before approving. Approving a Task collapses the buttons to an Approved badge and appends "Task [name] created" with timestamp to the log. Approving an Event collapses the buttons and appends "Event [name] — [datetime] added to calendar" with timestamp. Declining updates the row to a muted/declined state with no log entry. Two manual buttons, [+ Task] and [+ Event], are always visible at the bottom-right of the Actions block for all email classifications. Clicking [+ Task] adds an empty Task row (name field + Approve/Decline). Clicking [+ Event] adds an empty Event row (name field + date/time selector + Approve/Decline). The log is cumulative. Owner confirms: editable name and date/time work on Event rows, edited values appear in log, manual +Event includes date/time selector, manual rows log correctly.

**Slice 4 — Disposition and Processed section**
Accordion has Archive and Delete buttons. Both buttons are disabled until all action rows in that email have been resolved (Approved or Declined). Once all rows are resolved, the buttons activate. Clicking either button immediately adds a "Processed" label to the email row, appends a final log entry ("Email archived" or "Email deleted" with timestamp) to the execution log, moves the email row to the top of the Processed section, and decrements the Pending count. The UI response is otherwise identical. The difference is what happens in the SSOT: Archive triggers a Gmail archive action, Delete triggers a Gmail delete action. Neither button removes the row from the list entirely. Processed section shows muted rows with a visible "Processed" label/badge. The processed accordion shows the Email Summary and the execution log (including the disposition entry as final line). If the owner dispositioned without approving any actions, the execution log is only visible in the processed accordion. It was not shown in the pending panel. Owner confirms the full triage pass: open accordion, review summary, approve/decline actions, Archive or Delete activates, email gets Processed label, row moves to Processed section.

**Slice 5 — Run Triage (live)**
Run Triage button calls the triage API. The pending list refreshes with real emails and AI-generated content (Email Summary and Actions populated from API response). Loading state shown while triage runs. Owner confirms the live flow end-to-end.

---

## Rabbit Holes

**AI summary latency.** Run Triage calls an external AI service. If the response is slow (5+ seconds), the owner sees nothing happening. Devon must decide upfront: optimistic UI, skeleton loading, or a status indicator. Not deciding this before Slice 5 will cause rework.

**Actions schema partially resolved.** Action types are now defined: Task and Event only. The type list is closed. What remains unconfirmed before Slice 3 begins: the full API response schema — field names, data types, and how the AI returns the action description and type. Kai must confirm the schema before Devon builds the Actions panel, otherwise Devon builds against a stub he will have to undo.

**Accordion exclusive toggle.** Only one row may be open at a time. This is a small state management detail that is easy to get wrong when multiple rows are open and a new one is clicked. Worth noting explicitly so Sloane writes a scenario for it.

---

## No-gos

These are explicitly out of scope for this iteration.

- Reply or compose email from within the tile
- Bulk selection or bulk actions (select all, archive all)
- Email search or filtering
- Email threading or conversation view
- Custom category labels beyond what the AI returns
- Notification badge or unread count on the dashboard tile
- Pagination or infinite scroll (hardcoded list is sufficient for Slices 1 through 4)
- Accessibility audit (WCAG compliance is a future gate)

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-27 ~09:00 | Initial pitch — Phoebe |
| 2026-06-27 ~10:30 | Four spec updates added by owner: (1) + Task / + Event available for all classifications, not only Action emails; (2) every log entry carries a date + time timestamp; (3) Archive/Delete always appends a final disposition log entry — visible in processed accordion only if no prior approvals; (4) Archive/Delete buttons disabled until all action rows are Approved or Declined. |
| 2026-06-27 ~11:30 | Four more spec updates added by owner: (1) After archive/delete, email row immediately receives "processed" label; (2) Event action rows always show an AI-extracted date/time field (makes AI extraction visible to owner); (3) Event action date/time field is editable; (4) manually added Event rows (+Event) include an empty date/time selector. |
| 2026-06-27 ~14:00 | Two spec additions by Phoebe: (1) Processed list ordering: most recently processed email prepends to top of Processed section, new items always at top; (2) Execution log language set to English throughout: "Task [name] created", "Event [name] — [datetime] added to calendar", "Email archived", "Email deleted". Cleo prose reviewed and rewritten: em dashes removed, Dutch log strings replaced. |
