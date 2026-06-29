export function ClassificationBadge({ value }) {
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
