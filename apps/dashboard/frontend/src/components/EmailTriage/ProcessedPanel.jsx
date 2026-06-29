export function ProcessedPanel({ emailSession }) {
  const logEntries = emailSession?.logEntries || [];
  const displayEntries = [...logEntries].reverse(); // oldest first, disposition last

  if (displayEntries.length === 0) {
    return (
      <p className="text-slate-500 text-xs mt-2">No actions recorded.</p>
    );
  }

  return (
    <div className="mt-2" aria-label="Execution log">
      <p className="text-slate-400 text-xs font-medium mb-2">Execution log</p>
      <ul className="space-y-1">
        {displayEntries.map((entry, i) => (
          <li key={i} className="text-slate-400 text-xs font-mono">
            {entry}
          </li>
        ))}
      </ul>
    </div>
  );
}
