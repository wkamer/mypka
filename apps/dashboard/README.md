# PKA Dashboard

Local dashboard for the myPKA ecosystem. FastAPI backend + React/Vite/Tailwind frontend.

## Requirements

- Python 3.11+
- Node 18+

---

## Backend

### Install

```bash
cd backend
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```

### Configure credentials

Edit `backend/.env`:

```
APP_USERNAME=admin
PASSWORD_HASH=<bcrypt hash — see below>
JWT_SECRET=<random 64-char hex>
```

### Generate a password hash

```bash
python3 -c "
import bcrypt, getpass
pw = getpass.getpass('Password: ').encode()
print(bcrypt.hashpw(pw, bcrypt.gensalt()).decode())
"
```

Paste the output as `PASSWORD_HASH` in `.env`.

### Generate a JWT secret

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

### Run

```bash
cd backend
venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

API available at `http://localhost:8000`.

---

## Frontend

### Install

```bash
cd frontend
npm install
```

### Run (development)

```bash
npm run dev
```

Frontend available at `http://localhost:5173`.

---

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/login` | Validate credentials, set httpOnly cookie |
| GET | `/api/me` | Return current user (requires cookie) |
| POST | `/api/logout` | Clear auth cookie |

---

## Default credentials

Username: `admin`  
Password: `admin`

Change the password hash in `backend/.env` before exposing on the network.
