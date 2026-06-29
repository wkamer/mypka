import { parseSenderName } from './formatters';
import { ProcessedPanel } from './ProcessedPanel';

export function ProcessedRow({ email, isOpen, onToggle, emailSession }) {
  const senderName = parseSenderName(email.sender);

  const receivedAt = email.received_at
    ? new Date(email.received_at).toLocaleString("en-GB", {
        day: "2-digit",
        month: "short",
        hour: "2-digit",
        minute: "2-digit",
      })
    : "";

  return (
    <div>
      <div
        role="button"
        tabIndex={0}
        aria-expanded={isOpen}
        aria-controls={`email-panel-${email.id}`}
        className="flex items-center gap-3 px-4 py-3 hover:bg-slate-700 transition-colors cursor-pointer select-none focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-slate-400"
        onClick={() => onToggle(email.id)}
        onKeyDown={(e) => {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            onToggle(email.id);
          }
        }}
      >
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-1.5">
            <span className="text-slate-400 text-sm font-medium truncate">
              {senderName}
            </span>
            <span className="inline-flex items-center gap-1 text-xs rounded px-1.5 py-0.5 bg-slate-700 text-green-400 font-medium shrink-0">
              ✓ Processed
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
            <span className="text-slate-400 text-xs shrink-0 whitespace-nowrap">
              {receivedAt}
            </span>
          </div>
        </div>
        <svg
          aria-hidden="true"
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
        <div
          id={`email-panel-${email.id}`}
          className="mx-4 mb-3 border border-slate-700 rounded bg-slate-900 px-4 py-3"
        >
          {email.summary && (
            <div className="mb-3">
              <p className="text-xs font-medium text-slate-400 uppercase tracking-wide mb-1">
                Email Summary
              </p>
              <p className="text-slate-400 text-xs">{email.summary}</p>
            </div>
          )}
          <ProcessedPanel emailSession={emailSession} />
        </div>
      )}
    </div>
  );
}
