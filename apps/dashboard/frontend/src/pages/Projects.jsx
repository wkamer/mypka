import { useEffect, useState } from "react";
import { api } from "../api/client";

export default function Projects() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    api
      .get("/api/projects")
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
        <h1 className="text-xl font-semibold text-slate-100">My Projects</h1>
      </header>

      <main className="max-w-2xl mx-auto">
        {loading && (
          <p className="text-slate-500 text-sm">Loading...</p>
        )}

        {error && (
          <p className="text-red-400 text-sm">{error}</p>
        )}

        {data && (
          <div className="space-y-8">
            <section>
              <h2 className="text-slate-400 text-xs uppercase tracking-wider font-medium mb-3">
                Personal
              </h2>
              {data.personal.length === 0 ? (
                <p className="text-slate-500 text-sm">No active projects</p>
              ) : (
                <ul className="space-y-2">
                  {data.personal.map((name) => (
                    <li
                      key={name}
                      className="bg-slate-800 rounded-lg px-4 py-3 text-slate-100 text-sm"
                    >
                      {name}
                    </li>
                  ))}
                </ul>
              )}
            </section>

            <section>
              <h2 className="text-slate-400 text-xs uppercase tracking-wider font-medium mb-3">
                Business
              </h2>
              {data.business.length === 0 ? (
                <p className="text-slate-500 text-sm">No active projects</p>
              ) : (
                <ul className="space-y-2">
                  {data.business.map((name) => (
                    <li
                      key={name}
                      className="bg-slate-800 rounded-lg px-4 py-3 text-slate-100 text-sm"
                    >
                      {name}
                    </li>
                  ))}
                </ul>
              )}
            </section>
          </div>
        )}
      </main>
    </div>
  );
}
