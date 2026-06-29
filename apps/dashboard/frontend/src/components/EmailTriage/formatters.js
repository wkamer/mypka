export const _MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

/**
 * Format a Date or ISO string as "DD Mon YYYY HH:MM" (24-hour).
 * @param {Date|string} ts
 * @returns {string}
 */
export function fmtTimestamp(ts) {
  const d = ts instanceof Date ? ts : new Date(ts);
  const day = String(d.getDate()).padStart(2, "0");
  const mon = _MONTHS[d.getMonth()];
  const year = d.getFullYear();
  const h = String(d.getHours()).padStart(2, "0");
  const m = String(d.getMinutes()).padStart(2, "0");
  return `${day} ${mon} ${year} ${h}:${m}`;
}

/**
 * Format a datetime-local string like "2026-07-12T10:00" as "12 Jul 2026 10:00".
 * Returns "(no date)" when value is falsy.
 * @param {string|null|undefined} value
 * @returns {string}
 */
export function fmtEventDatetime(value) {
  if (!value) return "(no date)";
  const [datePart, timePart = "00:00"] = value.split("T");
  const [year, mon, day] = datePart.split("-");
  return `${day} ${_MONTHS[parseInt(mon, 10) - 1]} ${year} ${timePart.slice(0, 5)}`;
}

/**
 * Build a log entry string with timestamp FIRST.
 * Task:  "DD Mon YYYY HH:MM  Task "[name]" created"
 * Event: "DD Mon YYYY HH:MM  Event "[name]" — [datetime] added to calendar"
 * @param {string} type - "Task" or "Event"
 * @param {string|null|undefined} name
 * @param {string|null|undefined} eventDatetime
 * @param {Date|string} ts
 * @returns {string}
 */
export function buildLogEntry(type, name, eventDatetime, ts) {
  const prefix = fmtTimestamp(ts);
  if (type === "Event") {
    const displayName = name || "(untitled)";
    return `${prefix}  Event "${displayName}" — ${fmtEventDatetime(eventDatetime)} added to calendar`;
  }
  const displayName = name || "(untitled)";
  return `${prefix}  Task "${displayName}" created`;
}

/**
 * Builds a disposition log entry string.
 * @param {"archive"|"delete"} disposition
 * @param {Date|string} ts
 * @returns {string} e.g. "29 Jun 2026 14:09  Email archived"
 */
export function buildDispositionLogEntry(disposition, ts) {
  const d = ts instanceof Date ? ts : new Date(ts);
  const dateStr = d.toLocaleDateString("en-GB", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
  const timeStr = d.toLocaleTimeString("en-GB", {
    hour: "2-digit",
    minute: "2-digit",
  });
  const label = disposition === "archive" ? "Email archived" : "Email deleted";
  return `${dateStr} ${timeStr}  ${label}`;
}

export function parseSenderName(sender) {
  if (!sender) return "";
  const match = sender.match(/^([^<]+?)\s*</);
  if (match) {
    const name = match[1].trim().replace(/^["']|["']$/g, "");
    if (name) return name;
  }
  return sender;
}
