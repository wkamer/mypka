export function TriageStatusBadge({ value }) {
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
