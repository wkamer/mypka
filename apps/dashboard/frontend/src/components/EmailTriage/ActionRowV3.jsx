import { useRef, useEffect } from 'react';
import { fmtEventDatetime } from './formatters';

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
export function ActionRowV3({
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
  const displayName =
    editName ||
    "(untitled)";
  const hasDisplayName = Boolean(editName);
  const hasDisplayDatetime = Boolean(editDatetime);

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
        <span className="text-xs text-slate-400 uppercase mt-2 w-10 shrink-0 font-medium">
          {action.type}
        </span>
        <div className="flex-1 min-w-0 space-y-1.5">
          {isResolved ? (
            // Resolved state: static text (not a disabled input)
            <>
              <p
                className={`text-sm px-2 py-1 ${
                  hasDisplayName ? "text-slate-300" : "text-slate-500 italic"
                }`}
              >
                {displayName}
              </p>
              {action.type === "Event" && (
                <p
                  className={`text-sm px-2 py-1 ${
                    hasDisplayDatetime ? "text-slate-400" : "text-slate-500 italic"
                  }`}
                >
                  {fmtEventDatetime(editDatetime)}
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
                className="w-full bg-slate-800 text-slate-200 text-sm px-2 py-1 rounded border border-slate-700 placeholder-slate-600 focus:outline-none focus:border-slate-500 focus-visible:ring-2 focus-visible:ring-slate-400 focus-visible:ring-offset-0"
              />
              {action.type === "Event" && (
                <input
                  type="datetime-local"
                  value={editDatetime ? editDatetime.slice(0, 16) : ""}
                  onChange={(e) => onDatetimeChange(e.target.value)}
                  aria-label="Event datetime"
                  className="w-full bg-slate-800 text-slate-200 text-sm px-2 py-1 rounded border border-slate-700 focus:outline-none focus:border-slate-500 focus-visible:ring-2 focus-visible:ring-slate-400 focus-visible:ring-offset-0"
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
                className="text-xs text-green-400 hover:text-green-300 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-slate-900 focus-visible:ring-green-400 rounded"
                aria-label="Approve action"
              >
                Approve
              </button>
              <button
                onClick={onDecline}
                className="text-xs text-slate-400 hover:text-slate-300 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400 rounded"
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
