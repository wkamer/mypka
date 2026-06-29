import { useEffect, useState, useCallback } from 'react';
import { Link } from 'react-router-dom';
import { emailTriageApi } from '../api/emailTriage';
import { InboxRow } from '../components/EmailTriage';

export default function EmailTriage() {
  const [emails, setEmails] = useState(null);
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

  // Exclusive accordion: opening a row collapses any other open row.
  const handleToggle = useCallback((id) => {
    setOpenEmailId((prev) => (prev === id ? null : id));
  }, []);

  const loadEmails = useCallback(() => {
    return emailTriageApi
      .getEmails()
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
      const result = await emailTriageApi.runTriage();
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
                emailSession={emailSessions[email.id]}
                updateEmailSession={updateEmailSession}
              />
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
