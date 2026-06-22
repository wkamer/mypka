import { useNavigate } from "react-router-dom";
import { api } from "../api/client";

export default function Dashboard({ user }) {
  const navigate = useNavigate();

  async function handleLogout() {
    await api.logout().catch(() => {});
    window.location.href = "/login";
  }

  return (
    <div className="min-h-screen bg-slate-900 p-6">
      <header className="flex items-center justify-between mb-8">
        <h1 className="text-xl font-semibold text-slate-100">PKA Dashboard</h1>
        <div className="flex items-center gap-3">
          <span className="text-sm text-slate-400">{user}</span>
          <button
            onClick={handleLogout}
            className="text-sm text-slate-400 hover:text-slate-200 transition-colors"
          >
            Sign out
          </button>
        </div>
      </header>

      <main className="max-w-4xl mx-auto">
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-4">
          <button
            onClick={() => { window.location.href = "/projects"; }}
            className="bg-slate-800 hover:bg-slate-700 rounded-lg p-6 flex flex-col items-center gap-3 text-slate-100 transition-colors"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="w-8 h-8 text-indigo-400"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              strokeWidth={1.5}
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M2.25 12.75V12A2.25 2.25 0 014.5 9.75h15A2.25 2.25 0 0121.75 12v.75m-8.69-6.44l-2.12-2.12a1.5 1.5 0 00-1.061-.44H4.5A2.25 2.25 0 002.25 6v12a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9a2.25 2.25 0 00-2.25-2.25h-5.379a1.5 1.5 0 01-1.06-.44z"
              />
            </svg>
            <span className="text-sm font-medium">My Projects</span>
          </button>

          <button
            onClick={() => { window.location.href = "/key-elements"; }}
            className="bg-slate-800 hover:bg-slate-700 rounded-lg p-6 flex flex-col items-center gap-3 text-slate-100 transition-colors"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="w-8 h-8 text-emerald-400"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              strokeWidth={1.5}
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M6.75 3h10.5M6.75 3a.75.75 0 00-.75.75v.75m11.25-.75a.75.75 0 01.75.75v.75M6.75 3v.75m10.5-.75v.75M3 8.25h18M3 8.25A2.25 2.25 0 015.25 6h13.5A2.25 2.25 0 0121 8.25M3 8.25v10.5A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V8.25M9 12h6m-6 3.75h6"
              />
            </svg>
            <span className="text-sm font-medium">Key Elements</span>
          </button>
        </div>
      </main>
    </div>
  );
}
