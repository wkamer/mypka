import { useEffect, useState, useCallback, useRef } from 'react';
import { emailTriageApi } from '../../api/emailTriage';
import { buildDispositionLogEntry, buildLogEntry } from './formatters';
import { ActionRowV3 } from './ActionRowV3';

/**
 * Mounts when the accordion opens. Fetches actions and reconstructs the execution log.
 * Unmounts (and resets) when accordion closes.
 */
export function mergeActionSnapshot(actions, action) {
  return actions.some((a) => a.id === action.id)
    ? actions.map((a) => (a.id === action.id ? { ...a, ...action } : a))
    : [...actions, action];
}

export function ActionsPanel({ emailId, emailSession, updateEmailSession, onDispose }) {
  const [actions, setActions] = useState(null); // null = loading
  const [loadError, setLoadError] = useState(null);

  // Execution log reconstructed from approved actions plus in-session approvals.
  const [logEntries, setLogEntries] = useState([]); // array of formatted strings
  const [, setLogStatus] = useState("loading");

  // Controlled edit state per action: { [actionId]: { name, event_datetime } }
  const [edits, setEdits] = useState({});
  const latestEditsRef = useRef({});

  // Auto-focus: id of the action row that should receive focus
  const [pendingFocusId, setPendingFocusId] = useState(null);

  const allResolved =
    actions !== null &&
    actions.every((a) => a.status === "approved" || a.status === "declined");

  // Load actions on mount (accordion open)
  useEffect(() => {
    let cancelled = false;

    emailTriageApi
      .getActions(emailId)
      .then((d) => {
        if (cancelled) return;
        const savedActions = emailSession?.actions || [];
        const savedById = new Map(savedActions.map((a) => [a.id, a]));
        const mergedActions = d.actions.map((a) => {
          const saved = savedById.get(a.id);
          if (!saved) return a;
          const resolvedInSession = saved.status && saved.status !== "pending";
          return resolvedInSession ? { ...a, ...saved } : { ...saved, ...a };
        });
        savedActions.forEach((saved) => {
          if (!mergedActions.some((a) => a.id === saved.id)) {
            mergedActions.push(saved);
          }
        });
        setActions(mergedActions);
        const initial = {};
        mergedActions.forEach((a) => {
          const sessionEdit = emailSession?.edits?.[a.id];
          initial[a.id] = {
            name: sessionEdit !== undefined ? sessionEdit.name : (a.name || ""),
            event_datetime:
              sessionEdit !== undefined
                ? sessionEdit.event_datetime
                : (a.event_datetime || ""),
          };
        });
        setEdits(initial);
        latestEditsRef.current = initial;

        const approvedActions = mergedActions
          .filter((a) => a.status === "approved" && a.approved_at)
          .sort((a, b) => new Date(b.approved_at) - new Date(a.approved_at));
        const backendLogEntries = approvedActions.map((a) =>
          buildLogEntry(a.type, a.name, a.event_datetime, a.approved_at)
        );
        const ssLog = emailSession?.logEntries || [];
        const merged = [...ssLog];
        backendLogEntries.forEach((e) => {
          if (!merged.includes(e)) merged.push(e);
        });
        setLogEntries(merged);
        setLogStatus("loaded");
      })
      .catch((e) => {
        if (!cancelled) setLoadError(e.message);
      });

    return () => {
      cancelled = true;
    };
  }, [emailId]);

  const updateEdit = useCallback((actionId, field, value) => {
    latestEditsRef.current = {
      ...latestEditsRef.current,
      [actionId]: {
        ...(latestEditsRef.current[actionId] || {}),
        [field]: value,
      },
    };
    setEdits((prev) => ({
      ...prev,
      [actionId]: { ...(prev[actionId] || {}), [field]: value },
    }));
    updateEmailSession(emailId, (prev) => ({
      ...prev,
      edits: {
        ...(prev.edits || {}),
        [actionId]: { ...(prev.edits?.[actionId] || {}), [field]: value },
      },
    }));
  }, [emailId, updateEmailSession]);

  const handleApprove = useCallback(
    async (action) => {
      const currentEdit =
        latestEditsRef.current[action.id] || edits[action.id] || {};
      const editedName = currentEdit.name ?? action.name ?? "";
      const editedDatetime =
        currentEdit.event_datetime ?? action.event_datetime ?? null;

      try {
        const patchBody = { status: "approved", name: editedName };
        if (action.type === "Event") {
          patchBody.event_datetime = editedDatetime || undefined;
        }
        const updated = await emailTriageApi.patchAction(action.id, patchBody);
        const updatedAction = updated || {};
        const resolvedAction = {
          ...action,
          ...updatedAction,
          status: "approved",
          name: editedName,
          event_datetime:
            action.type === "Event" ? editedDatetime || null : updatedAction.event_datetime,
        };
        setActions((prev) =>
          prev.map((a) => (a.id === action.id ? resolvedAction : a))
        );

        // Build log entry with timestamp first and prepend (newest at top)
        const entry = buildLogEntry(action.type, editedName, editedDatetime, new Date());
        setLogEntries((prev) => [entry, ...prev]);
        updateEmailSession(emailId, (prev) => ({
          ...prev,
          actions: mergeActionSnapshot(prev.actions || [], resolvedAction),
          edits: {
            ...(prev.edits || {}),
            [action.id]: {
              name: editedName,
              event_datetime: editedDatetime || "",
            },
          },
          logEntries: [entry, ...(prev.logEntries || [])],
        }));
      } catch (e) {
        console.error("Approve failed:", e);
      }
    },
    [edits, emailId, updateEmailSession]
  );

  const handleDecline = useCallback(async (action) => {
    try {
      const updated = await emailTriageApi.patchAction(action.id, { status: "declined" });
      const resolvedAction = { ...action, ...(updated || {}), status: "declined" };
      setActions((prev) =>
        prev.map((a) => (a.id === action.id ? resolvedAction : a))
      );
      updateEmailSession(emailId, (prev) => ({
        ...prev,
        actions: mergeActionSnapshot(prev.actions || [], resolvedAction),
      }));
      // No log entry on decline
    } catch (e) {
      console.error("Decline failed:", e);
    }
  }, [emailId, updateEmailSession]);

  const handleAddTask = useCallback(async () => {
    try {
      const newAction = await emailTriageApi.createAction(emailId, { type: "Task", name: null });
      latestEditsRef.current = {
        ...latestEditsRef.current,
        [newAction.id]: { name: "", event_datetime: "" },
      };
      setActions((prev) => [...prev, newAction]);
      setEdits((prev) => ({
        ...prev,
        [newAction.id]: { name: "", event_datetime: "" },
      }));
      updateEmailSession(emailId, (prev) => ({
        ...prev,
        actions: mergeActionSnapshot(prev.actions || [], newAction),
        edits: {
          ...(prev.edits || {}),
          [newAction.id]: { name: "", event_datetime: "" },
        },
      }));
      setPendingFocusId(newAction.id);
    } catch (e) {
      console.error("Add task failed:", e);
    }
  }, [emailId, updateEmailSession]);

  const handleAddEvent = useCallback(async () => {
    try {
      const newAction = await emailTriageApi.createAction(emailId, { type: "Event", name: null });
      latestEditsRef.current = {
        ...latestEditsRef.current,
        [newAction.id]: { name: "", event_datetime: "" },
      };
      setActions((prev) => [...prev, newAction]);
      setEdits((prev) => ({
        ...prev,
        [newAction.id]: { name: "", event_datetime: "" },
      }));
      updateEmailSession(emailId, (prev) => ({
        ...prev,
        actions: mergeActionSnapshot(prev.actions || [], newAction),
        edits: {
          ...(prev.edits || {}),
          [newAction.id]: { name: "", event_datetime: "" },
        },
      }));
      setPendingFocusId(newAction.id);
    } catch (e) {
      console.error("Add event failed:", e);
    }
  }, [emailId, updateEmailSession]);

  const handleArchive = useCallback(() => {
    const entry = buildDispositionLogEntry("archive", new Date());
    updateEmailSession(emailId, (prev) => ({
      ...prev,
      logEntries: [entry, ...(prev.logEntries || [])],
    }));
    onDispose?.("archive");
  }, [emailId, updateEmailSession, onDispose]);

  const handleDelete = useCallback(() => {
    const entry = buildDispositionLogEntry("delete", new Date());
    updateEmailSession(emailId, (prev) => ({
      ...prev,
      logEntries: [entry, ...(prev.logEntries || [])],
    }));
    onDispose?.("delete");
  }, [emailId, updateEmailSession, onDispose]);

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
      <p className="text-xs font-medium text-slate-400 uppercase tracking-wide mb-2">Actions</p>
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

      {/* Execution log — only shown when entries exist */}
      {logEntries.length > 0 && (
        <div
          className="mt-3 pt-3 border-t border-slate-700"
          aria-live="polite"
          aria-label="Execution log"
        >
          <p className="text-slate-400 text-xs font-medium mb-2">
            Execution log
          </p>
          <ul className="space-y-1">
            {logEntries.map((entry, i) => (
              <li key={i} className="text-slate-400 text-xs font-mono">
                {entry}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Disposition buttons — always rendered, disabled until all rows resolved */}
      <div className="flex justify-end gap-2 mt-3 pt-3 border-t border-slate-700">
        <button
          disabled={!allResolved}
          aria-label="Archive email"
          aria-disabled={!allResolved}
          onClick={handleArchive}
          className="px-3 py-1.5 text-xs rounded bg-slate-700 hover:bg-slate-600 text-slate-100 font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400 disabled:opacity-40 disabled:cursor-not-allowed"
        >
          Archive
        </button>
        <button
          disabled={!allResolved}
          aria-label="Delete email"
          aria-disabled={!allResolved}
          onClick={handleDelete}
          className="px-3 py-1.5 text-xs rounded bg-red-900 hover:bg-red-800 text-red-200 font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-slate-900 focus-visible:ring-red-400 disabled:opacity-40 disabled:cursor-not-allowed"
        >
          Delete
        </button>
      </div>
    </div>
  );
}
