import { useEffect, useState, useCallback, useRef } from "react";
import { api } from "../api/client";

// ── Log formatting helpers ──

const _MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

/**
 * Format a Date or ISO string as "DD Mon YYYY HH:MM" (24-hour).
 * @param {Date|string} ts
 * @returns {string}
 */
function fmtTimestamp(ts) {
  const d = ts instanceof Date ? ts : new Date(ts);
  const day = String(d.getDate()).padStart(2, "0");
  const mon = _MONTHS[d.getMonth()];
  const year = d.getFullYear();
  const h = String(d.getHours()).padStart(2, "0");
  const m = String(d.getMinutes()).padStart(2, "0");
  return `${day} ${mon} ${year} ${h}:${m}`;
}

/**
 * Format a datetime-local string like "2026-07-12T10:00" as "12 Jul 2026 10:00".
 * Returns "(no date)" when value is falsy.
 * @param {string|null|undefined} value
 * @returns {string}
 */
function fmtEventDatetime(value) {
  if (!value) return "(no date)";
  const [datePart, timePart = "00:00"] = value.split("T");
  const [year, mon, day] = datePart.split("-");
  return `${day} ${_MONTHS[parseInt(mon, 10) - 1]} ${year} ${timePart.slice(0, 5)}`;
}

/**
 * Build a log entry string with timestamp FIRST.
 * Task:  "DD Mon YYYY HH:MM  Task [name] created"
 * Event: "DD Mon YYYY HH:MM  Event [name] — [datetime] added to calendar"
 * @param {string} type - "Task" or "Event"
 * @param {string|null|undefined} name
 * @param {string|null|undefined} eventDatetime
 * @param {Date|string} ts
 * @returns {string}
 */
function buildLogEntry(type, name, eventDatetime, ts) {
  const displayName = name || "(untitled)";
  const prefix = fmtTimestamp(ts);
  if (type === "Event") {
    return `${prefix}  Event ${displayName} — ${fmtEventDatetime(eventDatetime)} added to calendar`;
  }
  return `${prefix}  Task ${displayName} created`;
}

// ── Parked (S3 review — defer to later) ──
// MEDIUM: InboxRow clickable div needs role="button", tabIndex={0}, onKeyDown for keyboard nav
// MEDIUM: No focus-visible ring on InboxRow — keyboard users cannot see focus
// LOW:    Chevron SVG needs aria-hidden="true"

// ── Badge helpers ──

function ClassificationBadge({ value }) {
  if (!value) return null;
  const isAction = value === "Action";
  return (
    <span
      className={`inline-block px-2 py-0.5 rounded text-xs font-medium ${
        isAction
          ? "bg-amber-900 text-amber-200"
          : "bg-blue-900 text-blue-200"
      }`}
    >
      {value}
    </span>
  );
}

function TriageStatusBadge({ value }) {
  const styles = {
    pending: "bg-slate-700 text-slate-300",
    approved: "bg-green-900 text-green-200",
    declined: "bg-slate-600 text-slate-400",
    triage_error: "bg-red-900 text-red-300",
  };
  const label = {
    pending: "Pending",
    approved: "Approved",
    declined: "Declined",
    triage_error: "Error",
  };
  const cls = styles[value] || "bg-slate-700 text-slate-400";
  return (
    <span className={`inline-block px-2 py-0.5 rounded text-xs font-medium ${cls}`}>
      {label[value] || value}
    </span>
  );
}

// ── Sender parsing ──

function parseSenderName(sender) {
  if (!sender) return "";
  const match = sender.match(/^([^<]+?)\s*</);
  if (match) {
    const name = match[1].trim().replace(/^["']|["']$/g, "");
    if (name) return name;
  }
  return sender;
}

// ── ActionRowV3 — Slice 3 editable action row ──

/**
 * Props:
 *   action          — action object from API: { id, type, name, event_datetime, status, ... }
 *   editName        — current value in the name input (controlled)
 *   editDatetime    — current value in the datetime input (controlled, Event rows only)
 *   onNameChange    — (value: string) => void
 *   onDatetimeChange — (value: string) => void
 *   onApprove       — () => void
 *   onDecline       — () => void
 *   shouldFocus     — boolean: auto-focus the name field on mount when true
 *   onFocusHandled  — () => void: called after auto-focus fires so parent can clear the flag
 */
function ActionRowV3({
  action,
  editName,
  editDatetime,
  onNameChange,
  onDatetimeChange,
  onApprove,
  onDecline,
  shouldFocus,
  onFocusHandled,
}) {
  const isResolved = action.status !== "pending";
  const isApproved = action.status === "approved";
  const isDeclined = action.status === "declined";

  // Auto-focus name field when this is a newly added row
  const nameInputRef = useRef(null);
  useEffect(() => {
    if (shouldFocus && nameInputRef.current) {
      nameInputRef.current.focus();
      onFocusHandled?.();
    }
  }, [shouldFocus, onFocusHandled]);

  return (
    <div
      className={`rounded px-3 py-2 text-sm border ${
        isDeclined
          ? "bg-slate-800 border-slate-700 opacity-50"
          : "bg-slate-900 border-slate-700"
      }`}
    >
      <div className="flex items-start gap-2">
        <span className="text-xs text-slate-500 uppercase mt-2 w-10 shrink-0 font-medium">
          {action.type}
        </span>
        <div className="flex-1 min-w-0 space-y-1.5">
          {isResolved ? (
            // Resolved state: static text (not a disabled input)
            <>
              <p className="text-slate-300 text-sm px-2 py-1">
                {editName || "(untitled)"}
              </p>
              {action.type === "Event" && (
                <p className="text-slate-400 text-xs px-2 py-1">
                  {editDatetime ? fmtEventDatetime(editDatetime) : "(no date)"}
                </p>
              )}
            </>
          ) : (
            // Pending state: editable inputs
            <>
              <input
                ref={nameInputRef}
                type="text"
                value={editName}
                onChange={(e) => onNameChange(e.target.value)}
                placeholder="Enter name..."
                aria-label="Action name"
                className="w-full bg-slate-800 text-slate-200 text-sm px-2 py-1 rounded border border-slate-700 placeholder-slate-600 focus:outline-none focus:border-slate-500"
              />
              {action.type === "Event" && (
                <input
                  type="datetime-local"
                  value={editDatetime ? editDatetime.slice(0, 16) : ""}
                  onChange={(e) => onDatetimeChange(e.target.value)}
                  aria-label="Event datetime"
                  className="w-full bg-slate-800 text-slate-200 text-sm px-2 py-1 rounded border border-slate-700 focus:outline-none focus:border-slate-500"
                />
              )}
            </>
          )}
        </div>
        <div className="flex items-center gap-2 shrink-0 mt-1">
          {!isResolved ? (
            <>
              <button
                onClick={onApprove}
                className="text-xs text-green-400 hover:text-green-300 transition-colors"
                aria-label="Approve action"
              >
                Approve
              </button>
              <button
                onClick={onDecline}
                className="text-xs text-slate-500 hover:text-slate-400 transition-colors"
                aria-label="Decline action"
              >
                Decline
              </button>
            </>
          ) : (
            <span
              className={`text-xs font-medium ${
                isApproved ? "text-green-400" : "text-slate-500"
              }`}
            >
              {isApproved ? "Approved" : "Declined"}
            </span>
          )}
        </div>
      </div>
    </div>
  );
}

// ── ActionsPanel — fetches and manages actions for one email ──

/**
 * Mounts when the accordion opens. Fetches actions and execution log in parallel.
 * Unmounts (and resets) when accordion closes.
 */
function ActionsPanel({ emailId }) {
  const [actions, setActions] = useState(null); // null = loading
  const [loadError, setLoadError] = useState(null);

  // Log state — separate from actions
  const [logEntries, setLogEntries] = useState([]); // array of formatted strings
  const [logStatus, setLogStatus] = useState("loading"); // 'loading' | 'loaded' | 'error'

  // Controlled edit state per action: { [actionId]: { name, event_datetime } }
  const [edits, setEdits] = useState({});

  // Auto-focus: id of the action row that should receive focus
  const [pendingFocusId, setPendingFocusId] = useState(null);

  // Load actions and log in parallel on mount (accordion open)
  useEffect(() => {
    let cancelled = false;

    // Fetch actions
    api
      .get(`/api/email-management/emails/${emailId}/actions`)
      .then((d) => {
        if (cancelled) return;
        setActions(d.actions);
        const initial = {};
        d.actions.forEach((a) => {
          initial[a.id] = {
            name: a.name || "",
            event_datetime: a.event_datetime || "",
          };
        });
        setEdits(initial);
      })
      .catch((e) => {
        if (!cancelled) setLoadError(e.message);
      });

    // Fetch execution log
    api
      .get(`/api/email-management/emails/${emailId}/log`)
      .then((d) => {
        if (cancelled) return;
        const formatted = d.entries.map((e) =>
          buildLogEntry(e.action_type, e.name, e.event_datetime, e.executed_at)
        );
        setLogEntries(formatted);
        setLogStatus("loaded");
      })
      .catch(() => {
        if (!cancelled) setLogStatus("error");
      });

    return () => {
      cancelled = true;
    };
  }, [emailId]);

  const updateEdit = useCallback((actionId, field, value) => {
    setEdits((prev) => ({
      ...prev,
      [actionId]: { ...(prev[actionId] || {}), [field]: value },
    }));
  }, []);

  const handleApprove = useCallback(
    async (action) => {
      const editedName = edits[action.id]?.name ?? action.name ?? "";
      const editedDatetime =
        edits[action.id]?.event_datetime ?? action.event_datetime ?? null;

      try {
        const patchBody = { status: "approved", name: editedName };
        if (action.type === "Event") {
          patchBody.event_datetime = editedDatetime || undefined;
        }
        const updated = await api.patch(
          `/api/email-management/actions/${action.id}`,
          patchBody
        );
        setActions((prev) =>
          prev.map((a) => (a.id === action.id ? updated : a))
        );

        // Build log entry with timestamp first and prepend (newest at top)
        const entry = buildLogEntry(action.type, editedName, editedDatetime, new Date());
        setLogEntries((prev) => [entry, ...prev]);
        setLogStatus("loaded");
      } catch (e) {
        console.error("Approve failed:", e);
      }
    },
    [edits]
  );

  const handleDecline = useCallback(async (action) => {
    try {
      const updated = await api.patch(
        `/api/email-management/actions/${action.id}`,
        { status: "declined" }
      );
      setActions((prev) =>
        prev.map((a) => (a.id === action.id ? updated : a))
      );
      // No log entry on decline
    } catch (e) {
      console.error("Decline failed:", e);
    }
  }, []);

  const handleAddTask = useCallback(async () => {
    try {
      const newAction = await api.post(
        `/api/email-management/emails/${emailId}/actions`,
        { type: "Task", name: null }
      );
      setActions((prev) => [...prev, newAction]);
      setEdits((prev) => ({
        ...prev,
        [newAction.id]: { name: "", event_datetime: "" },
      }));
      setPendingFocusId(newAction.id);
    } catch (e) {
      console.error("Add task failed:", e);
    }
  }, [emailId]);

  const handleAddEvent = useCallback(async () => {
    try {
      const newAction = await api.post(
        `/api/email-management/emails/${emailId}/actions`,
        { type: "Event", name: null }
      );
      setActions((prev) => [...prev, newAction]);
      setEdits((prev) => ({
        ...prev,
        [newAction.id]: { name: "", event_datetime: "" },
      }));
      setPendingFocusId(newAction.id);
    } catch (e) {
      console.error("Add event failed:", e);
    }
  }, [emailId]);

  if (loadError) {
    return (
      <p className="text-red-400 text-xs mt-2">
        Failed to load actions: {loadError}
      </p>
    );
  }
  if (actions === null) {
    return <p className="text-slate-500 text-xs mt-2">Loading actions...</p>;
  }

  return (
    <div className="space-y-2 mt-2">
      {actions.map((action) => (
        <ActionRowV3
          key={action.id}
          action={action}
          editName={edits[action.id]?.name ?? action.name ?? ""}
          editDatetime={
            edits[action.id]?.event_datetime ?? action.event_datetime ?? ""
          }
          onNameChange={(v) => updateEdit(action.id, "name", v)}
          onDatetimeChange={(v) => updateEdit(action.id, "event_datetime", v)}
          onApprove={() => handleApprove(action)}
          onDecline={() => handleDecline(action)}
          shouldFocus={pendingFocusId === action.id}
          onFocusHandled={() => setPendingFocusId(null)}
        />
      ))}

      {/* Manual add controls — always visible, no cancel path */}
      <div className="flex gap-2 pt-1">
        <button
          onClick={handleAddTask}
          className="text-xs text-slate-400 hover:text-slate-200 border border-slate-700 rounded px-2 py-1 transition-colors"
        >
          + Task
        </button>
        <button
          onClick={handleAddEvent}
          className="text-xs text-slate-400 hover:text-slate-200 border border-slate-700 rounded px-2 py-1 transition-colors"
        >
          + Event
        </button>
      </div>

      {/* Execution log — loading state */}
      {logStatus === "loading" && (
        <div className="mt-3 pt-3 border-t border-slate-700">
          <p className="text-slate-500 text-xs">Loading log...</p>
        </div>
      )}

      {/* Execution log — error state */}
      {logStatus === "error" && (
        <div className="mt-3 pt-3 border-t border-slate-700">
          <p className="text-slate-500 text-xs">Execution log unavailable.</p>
        </div>
      )}

      {/* Execution log — loaded, only shown when entries exist */}
      {logStatus === "loaded" && logEntries.length > 0 && (
        <div
          className="mt-3 pt-3 border-t border-slate-700"
          aria-live="polite"
          aria-label="Execution log"
        >
          <p className="text-slate-500 text-xs font-medium mb-2">
            Execution log
          </p>
          <div className="space-y-1">
            {logEntries.map((entry, i) => (
              <p key={i} className="text-slate-400 text-xs font-mono">
                {entry}
              </p>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

// ── Inbox row (accordion) ──

function InboxRow({ email, isOpen, onToggle }) {
  const senderName = parseSenderName(email.sender);

  const receivedAt = email.received_at
    ? new Date(email.received_at).toLocaleString("nl-NL", {
        day: "2-digit",
        month: "short",
        hour: "2-digit",
        minute: "2-digit",
      })
    : "";

  return (
    <div>
      <div
        className="flex items-center gap-3 px-4 py-3 hover:bg-slate-700 transition-colors cursor-pointer select-none"
        onClick={() => onToggle(email.id)}
      >
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-1.5">
            <span className="text-slate-200 text-sm font-medium truncate">
              {senderName}
            </span>
            {email.gmail_url && (
              <a
                href={email.gmail_url}
                target="_blank"
                rel="noopener noreferrer"
                className="shrink-0 text-slate-500 hover:text-slate-300 transition-colors"
                aria-label="Open in Gmail"
                onClick={(e) => e.stopPropagation()}
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="12"
                  height="12"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                  <polyline points="15 3 21 3 21 9" />
                  <line x1="10" y1="14" x2="21" y2="3" />
                </svg>
              </a>
            )}
          </div>
          <div className="flex items-baseline justify-between gap-4 mt-0.5">
            <p className="text-slate-400 text-xs truncate">
              {email.subject || "(no subject)"}
            </p>
            <span className="text-slate-600 text-xs shrink-0 whitespace-nowrap">
              {receivedAt}
            </span>
          </div>
        </div>
        <svg
          className={`shrink-0 text-slate-500 transition-transform duration-200 ${
            isOpen ? "rotate-180" : ""
          }`}
          xmlns="http://www.w3.org/2000/svg"
          width="14"
          height="14"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <polyline points="6 9 12 15 18 9" />
        </svg>
      </div>
      {isOpen && (
        <div className="mx-4 mb-3 border border-slate-700 rounded bg-slate-900 px-4 py-3">
          <ActionsPanel emailId={email.id} />
        </div>
      )}
    </div>
  );
}

// ── Main page ──

export default function EmailTriage() {
  const [emails, setEmails] = useState(null);
  const [loading, setLoading] = useState(true);
  const [runLoading, setRunLoading] = useState(false);
  const [error, setError] = useState(null);
  const [runResult, setRunResult] = useState(null);
  const [openEmailId, setOpenEmailId] = useState(null);

  // Exclusive accordion: opening a row collapses any other open row.
  const handleToggle = useCallback((id) => {
    setOpenEmailId((prev) => (prev === id ? null : id));
  }, []);

  const loadEmails = useCallback(() => {
    return api
      .get("/api/email-management/emails")
      .then((d) => setEmails(d.emails))
      .catch((e) => setError(e.message));
  }, []);

  useEffect(() => {
    loadEmails().finally(() => setLoading(false));
  }, [loadEmails]);

  const handleRunTriage = async () => {
    setRunLoading(true);
    setRunResult(null);
    setError(null);
    try {
      const result = await api.post("/api/email-management/run", {});
      setRunResult(result);
      await loadEmails();
    } catch (e) {
      setError(e.message);
    } finally {
      setRunLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 p-6">
      <header className="flex items-center gap-4 mb-8">
        <button
          onClick={() => {
            window.location.href = "/dashboard";
          }}
          className="text-sm text-slate-400 hover:text-slate-200 transition-colors"
        >
          &larr; Back
        </button>
        <h1 className="text-xl font-semibold text-slate-100">Email Triage</h1>
      </header>

      <main className="max-w-2xl mx-auto">
        <div className="flex items-center gap-4 mb-6">
          <button
            onClick={handleRunTriage}
            disabled={runLoading}
            className="px-4 py-2 text-sm rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-100 disabled:opacity-50 transition-colors font-medium"
          >
            {runLoading ? "Running..." : "Run Triage"}
          </button>
          {runResult && (
            <span className="text-slate-400 text-xs">
              Processed: {runResult.processed} | Skipped: {runResult.skipped} |
              Errors: {runResult.errors}
            </span>
          )}
        </div>

        {error && (
          <div className="mb-4 p-3 rounded-lg bg-red-900 border border-red-700 text-red-200 text-sm">
            {error}
          </div>
        )}

        {loading && <p className="text-slate-500 text-sm">Loading...</p>}

        {!loading && emails && emails.length === 0 && !error && (
          <div className="text-center py-16">
            <p className="text-slate-500 text-sm">
              No emails yet. Click Run Triage to start.
            </p>
          </div>
        )}

        {emails && emails.length > 0 && (
          <div className="bg-slate-800 rounded-lg overflow-hidden divide-y divide-slate-700">
            {emails.map((email) => (
              <InboxRow
                key={email.id}
                email={email}
                isOpen={openEmailId === email.id}
                onToggle={handleToggle}
              />
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
