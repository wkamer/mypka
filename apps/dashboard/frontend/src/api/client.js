const BASE = "";

async function request(method, path, body) {
  const options = {
    method,
    credentials: "include",
    headers: body ? { "Content-Type": "application/json" } : {},
  };
  if (body) options.body = JSON.stringify(body);

  const res = await fetch(`${BASE}${path}`, options);
  if (!res.ok) {
    const data = await res.json().catch(() => ({}));
    throw new Error(data.detail || "Request failed");
  }
  return res.json();
}

export const api = {
  login: (username, password) =>
    request("POST", "/api/login", { username, password }),
  me: () => request("GET", "/api/me"),
  logout: () => request("POST", "/api/logout"),
  get: (path) => request("GET", path),
};
