import { parseSenderName } from './formatters';
import { ActionsPanel } from './ActionsPanel';

export function InboxRow({ email, isOpen, onToggle, emailSession, updateEmailSession }) {
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
          <ActionsPanel
            emailId={email.id}
            emailSession={emailSession}
            updateEmailSession={updateEmailSession}
          />
        </div>
      )}
    </div>
  );
}
