import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { api } from "../api/client";

export default function KeyElementDetail() {
  const { slug } = useParams();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    api
      .get(`/api/key-elements/${slug}`)
      .then((d) => setData(d))
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false));
  }, [slug]);

  return (
    <div className="min-h-screen bg-slate-900 p-6">
      <header className="flex items-center gap-4 mb-8">
        <button
          onClick={() => { window.location.href = "/key-elements"; }}
          className="text-sm text-slate-400 hover:text-slate-200 transition-colors"
        >
          &larr; Back
        </button>
        <h1 className="text-xl font-semibold text-slate-100">
          {data ? data.name : "Key Element"}
        </h1>
      </header>

      <main className="max-w-2xl mx-auto">
        {loading && <p className="text-slate-500 text-sm">Loading...</p>}
        {error && <p className="text-red-400 text-sm">{error}</p>}
        {data && (
          <pre className="text-slate-300 text-sm font-sans whitespace-pre-wrap leading-relaxed">
            {data.content}
          </pre>
        )}
      </main>
    </div>
  );
}
