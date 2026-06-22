import { useEffect, useState } from "react";
import { api } from "../api/client";

export default function KeyElements() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    api
      .get("/api/key-elements")
      .then((d) => setData(d))
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="min-h-screen bg-slate-900 p-6">
      <header className="flex items-center gap-4 mb-8">
        <button
          onClick={() => { window.location.href = "/dashboard"; }}
          className="text-sm text-slate-400 hover:text-slate-200 transition-colors"
        >
          &larr; Back
        </button>
        <h1 className="text-xl font-semibold text-slate-100">Key Elements</h1>
      </header>

      <main className="max-w-2xl mx-auto">
        {loading && <p className="text-slate-500 text-sm">Loading...</p>}
        {error && <p className="text-red-400 text-sm">{error}</p>}
        {data && (
          <ul className="space-y-2">
            {data.items.map((ke) => (
              <li key={ke.slug}>
                <button
                  onClick={() => { window.location.href = `/key-elements/${ke.slug}`; }}
                  className="w-full text-left bg-slate-800 hover:bg-slate-700 rounded-lg px-4 py-3 text-slate-100 text-sm transition-colors flex items-center justify-between"
                >
                  <span>{ke.name}</span>
                  <span className="text-slate-500 text-xs">&rarr;</span>
                </button>
              </li>
            ))}
          </ul>
        )}
      </main>
    </div>
  );
}
