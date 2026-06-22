import { useEffect, useState } from "react";
import {
  BrowserRouter,
  Navigate,
  Route,
  Routes,
  useNavigate,
} from "react-router-dom";
import { api } from "./api/client";
import Dashboard from "./pages/Dashboard";
import KeyElementDetail from "./pages/KeyElementDetail";
import KeyElements from "./pages/KeyElements";
import Login from "./pages/Login";
import Projects from "./pages/Projects";
import "./index.css";

function AuthGate() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api
      .me()
      .then((data) => setUser(data.username))
      .catch(() => setUser(null))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-900 flex items-center justify-center">
        <span className="text-slate-500 text-sm">Loading...</span>
      </div>
    );
  }

  return (
    <Routes>
      <Route
        path="/login"
        element={user ? <Navigate to="/dashboard" replace /> : <Login />}
      />
      <Route
        path="/dashboard"
        element={
          user ? (
            <Dashboard user={user} />
          ) : (
            <Navigate to="/login" replace />
          )
        }
      />
      <Route
        path="/projects"
        element={user ? <Projects /> : <Navigate to="/login" replace />}
      />
      <Route
        path="/key-elements"
        element={user ? <KeyElements /> : <Navigate to="/login" replace />}
      />
      <Route
        path="/key-elements/:slug"
        element={user ? <KeyElementDetail /> : <Navigate to="/login" replace />}
      />
      <Route
        path="*"
        element={<Navigate to={user ? "/dashboard" : "/login"} replace />}
      />
    </Routes>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <AuthGate />
    </BrowserRouter>
  );
}
