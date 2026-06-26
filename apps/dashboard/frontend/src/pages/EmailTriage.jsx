import { useEffect, useState, useCallback } from "react";
import { api } from "../api/client";

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

function ActionTypeBadge({ value }) {
  const styles = {
    todoist: "bg-red-900 text-red-200",
    calendar: "bg-indigo-900 text-indigo-200",
    archive: "bg-slate-600 text-slate-300",
  };
  return (
    <span
      className={`inline-block px-2 py-0.5 rounded text-xs font-medium ${
        styles[value] || "bg-slate-700 text-slate-400"
      }`}
    >
      {value}
    </span>
  );
}

function ActionStatusBadge({ value, externalId }) {
  const styles = {
    pending: "bg-slate-700 text-slate-300",
    executed: "bg-green-900 text-green-200",
    failed: "bg-red-900 text-red-300",
    declined: "bg-slate-600 text-slate-400",
  };
  const label = {
    pending: "Pending",
    executed: externalId ? `Executed (${externalId})` : "Executed",
    failed: "Failed",
    declined: "Declined",
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
  // "Display Name <addr@domain>" — extract display name
  const match = sender.match(/^([^<]+?)\s*</);
  if (match) {
    const name = match[1].trim().replace(/^["']|["']$/g, "");
    if (name) return name;
  }
  // fallback: return raw sender string (plain address or unknown format)
  return sender;
}

// ── Inbox row (S3: accordion) ──

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
          className={`shrink-0 text-slate-500 transition-transform duration-200 ${isOpen ? "rotate-180" : ""}`}
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
          {/* AC-10: detail panel — intentionally empty for MVP */}
        </div>
      )}
    </div>
  );
}

// ── Action row ──

function ActionRow({ action, onStatusChange }) {
  const [loading, setLoading] = useState(false);

  const handle = async (newStatus) => {
    setLoading(true);
    try {
      const updated = await api.patch(
        `/api/email-triage/actions/${action.id}`,
        { status: newStatus }
      );
      onStatusChange(updated);
    } catch (e) {
      console.error("Action update failed:", e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-start gap-3 bg-slate-900 rounded px-3 py-2 text-sm">
      <div className="mt-0.5">
        <ActionTypeBadge value={action.action_type} />
      </div>
      <div className="flex-1 min-w-0">
        <p className="text-slate-200 font-medium truncate">{action.suggested_title}</p>
        <p className="text-slate-500 text-xs mt-0.5 truncate">{action.description}</p>
      </div>
      <div className="flex items-center gap-2 shrink-0">
        {action.status === "pending" ? (
          <>
            <button
              onClick={() => handle("approved")}
              disabled={loading}
              className="text-xs text-green-400 hover:text-green-300 disabled:opacity-50 transition-colors"
            >
              Approve
            </button>
            <button
              onClick={() => handle("declined")}
              disabled={loading}
              className="text-xs text-slate-500 hover:text-slate-400 disabled:opacity-50 transition-colors"
            >
              Decline
            </button>
          </>
        ) : (
          <ActionStatusBadge value={action.status} externalId={action.external_id} />
        )}
      </div>
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

  const handleToggle = useCallback((id) => {
    setOpenEmailId((prev) => (prev === id ? null : id));
  }, []);

  const loadEmails = useCallback(() => {
    return api
      .get("/api/email-triage/emails")
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
      const result = await api.post("/api/email-triage/run", {});
      setRunResult(result);
      await loadEmails();
    } catch (e) {
      setError(e.message);
    } finally {
      setRunLoading(false);
    }
  };

  const handleEmailStatusChange = (updated) => {
    setEmails((prev) =>
      prev ? prev.map((e) => (e.id === updated.id ? { ...e, ...updated } : e)) : prev
    );
  };

  return (
    <div className="min-h-screen bg-slate-900 p-6">
      <header className="flex items-center gap-4 mb-8">
        <button
          onClick={() => { window.location.href = "/dashboard"; }}
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
              Processed: {runResult.processed} | Skipped: {runResult.skipped} | Errors:{" "}
              {runResult.errors}
            </span>
          )}
        </div>

        {error && (
          <div className="mb-4 p-3 rounded-lg bg-red-900 border border-red-700 text-red-200 text-sm">
            {error}
          </div>
        )}

        {loading && (
          <p className="text-slate-500 text-sm">Loading...</p>
        )}

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
