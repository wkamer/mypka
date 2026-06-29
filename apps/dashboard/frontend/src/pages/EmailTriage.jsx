import { useEffect, useState, useCallback } from 'react';
import { Link } from 'react-router-dom';
import { emailTriageApi } from '../api/emailTriage';
import { InboxRow } from '../components/EmailTriage';
import { ProcessedRow } from '../components/EmailTriage/ProcessedRow';

export default function EmailTriage() {
  const [pendingEmails, setPendingEmails] = useState([]);
  const [processedEmails, setProcessedEmails] = useState([]);
  const [disposeErrors, setDisposeErrors] = useState({});
  const [loading, setLoading] = useState(true);
  const [runLoading, setRunLoading] = useState(false);
  const [error, setError] = useState(null);
  const [runResult, setRunResult] = useState(null);
  const [openEmailId, setOpenEmailId] = useState(null);
  const [emailSessions, setEmailSessions] = useState({});

  const updateEmailSession = useCallback((emailId, updater) => {
    setEmailSessions((prev) => {
      const current = prev[emailId] || { actions: [], edits: {}, logEntries: [] };
      return {
        ...prev,
        [emailId]: updater(current),
      };
    });
  }, []);

  const handleToggle = useCallback((id) => {
    setOpenEmailId((prev) => (prev === id ? null : id));
  }, []);

  const loadEmails = useCallback(() => {
    return emailTriageApi
      .getEmails()
      .then((d) => {
        setPendingEmails(d.emails.filter((e) => e.status === "pending"));
        setProcessedEmails(
          d.emails
            .filter((e) => e.status === "processed")
            .sort((a, b) => new Date(b.processed_at || 0) - new Date(a.processed_at || 0))
        );
      })
      .catch((e) => setError(e.message));
  }, []);

  useEffect(() => {
    loadEmails().finally(() => setLoading(false));
  }, [loadEmails]);

  const handleDispose = useCallback(
    async (emailId, disposition) => {
      const email = pendingEmails.find((e) => e.id === emailId);
      if (!email) return;

      // Optimistic move
      setPendingEmails((prev) => prev.filter((e) => e.id !== emailId));
      setProcessedEmails((prev) => [{ ...email, status: "processed" }, ...prev]);
      setDisposeErrors((prev) => ({ ...prev, [emailId]: null }));

      try {
        await emailTriageApi.disposeEmail(emailId, disposition);
      } catch (e) {
        // Rollback
        setProcessedEmails((prev) => prev.filter((e) => e.id !== emailId));
        setPendingEmails((prev) =>
          [...prev, email].sort((a, b) => new Date(b.received_at) - new Date(a.received_at))
        );
        setOpenEmailId(null);
        setDisposeErrors((prev) => ({ ...prev, [emailId]: e.message }));
        // Remove the disposition log entry (first entry, prepended before the call)
        updateEmailSession(emailId, (prev) => ({
          ...prev,
          logEntries: (prev.logEntries || []).slice(1),
        }));
      }
    },
    [pendingEmails, updateEmailSession]
  );

  const handleRunTriage = async () => {
    setRunLoading(true);
    setRunResult(null);
    setError(null);
    try {
      const result = await emailTriageApi.runTriage();
      setRunResult(result);
      await loadEmails();
    } catch (e) {
      setError("Triage failed. Check your connection and try again.");
    } finally {
      setRunLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 p-6">
      <header className="flex items-center gap-4 mb-8">
        <Link
          to="/dashboard"
          className="text-sm text-slate-400 hover:text-slate-200 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-slate-400 rounded"
        >
          &larr; Back
        </Link>
        <h1 className="text-xl font-semibold text-slate-100">Email Triage</h1>
      </header>

      <main className="max-w-2xl mx-auto">
        <div className="flex items-center gap-4 mb-6">
          <button
            onClick={handleRunTriage}
            disabled={runLoading}
            aria-busy={runLoading}
            className="inline-flex items-center gap-2 px-4 py-2 text-sm rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-100 disabled:opacity-50 disabled:cursor-not-allowed transition-colors font-medium focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400"
          >
            {runLoading && (
              <svg
                aria-hidden="true"
                className="w-3.5 h-3.5 animate-spin text-slate-300"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
                />
              </svg>
            )}
            {runLoading ? "Running..." : "Run Triage"}
          </button>
          <span
            role="status"
            aria-live="polite"
            aria-atomic="true"
            className="text-slate-400 text-xs"
          >
            {runLoading && "Running triage..."}
            {!runLoading && !error && runResult && runResult.processed > 0 &&
              `${runResult.processed} email${runResult.processed === 1 ? "" : "s"} processed${runResult.errors > 0 ? `, ${runResult.errors} error${runResult.errors === 1 ? "" : "s"}` : ""}`}
            {!runLoading && !error && runResult && runResult.processed === 0 &&
              "No new emails found"}
          </span>
        </div>

        {error && (
          <div className="mb-4 p-3 rounded-lg bg-red-900 border border-red-700 text-red-200 text-sm">
            {error}
          </div>
        )}

        {loading && <p className="text-slate-500 text-sm">Loading...</p>}

        {/* Empty state */}
        {!loading && pendingEmails.length === 0 && processedEmails.length === 0 && !error && (
          <div className="text-center py-16">
            <p className="text-slate-500 text-sm">No emails yet. Click Run Triage to start.</p>
          </div>
        )}

        {/* Pending section */}
        {!loading && pendingEmails.length > 0 && (
          <div className="mb-6">
            <p className="text-xs font-medium text-slate-400 uppercase tracking-wide mb-2">
              Pending · {pendingEmails.length}
            </p>
            <div className="bg-slate-800 rounded-lg overflow-hidden divide-y divide-slate-700">
              {pendingEmails.map((email) => (
                <InboxRow
                  key={email.id}
                  email={email}
                  isOpen={openEmailId === email.id}
                  onToggle={handleToggle}
                  emailSession={emailSessions[email.id]}
                  updateEmailSession={updateEmailSession}
                  onDispose={(disposition) => handleDispose(email.id, disposition)}
                  disposeError={disposeErrors[email.id] || null}
                />
              ))}
            </div>
          </div>
        )}

        {/* Processed section */}
        {processedEmails.length > 0 && (
          <div>
            <p className="text-xs font-medium text-slate-400 uppercase tracking-wide mb-2">
              Processed{" "}
              <span aria-live="polite" aria-atomic="true">
                · {processedEmails.length}
              </span>
            </p>
            <div className="bg-slate-800 rounded-lg overflow-hidden divide-y divide-slate-700">
              {processedEmails.map((email) => (
                <ProcessedRow
                  key={email.id}
                  email={email}
                  isOpen={openEmailId === email.id}
                  onToggle={handleToggle}
                  emailSession={emailSessions[email.id]}
                />
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
