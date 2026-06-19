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
        <p className="text-slate-500 text-sm">
          Dashboard content coming in the next iteration.
        </p>
      </main>
    </div>
  );
}
