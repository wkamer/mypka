from pathlib import Path

from fastapi import FastAPI, Cookie, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from auth import create_token, decode_token, verify_credentials

app = FastAPI(title="PKA Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://raspberrypi.local:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

COOKIE_NAME = "pka_token"


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/api/login")
def login(body: LoginRequest, response: Response):
    if not verify_credentials(body.username, body.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(body.username)
    response.set_cookie(
        key=COOKIE_NAME,
        value=token,
        httponly=True,
        samesite="lax",
        secure=True,
        max_age=60 * 60 * 24 * 7,  # 7 days
    )
    return {"ok": True}


@app.get("/api/me")
def me(pka_token: str = Cookie(default=None)):
    if pka_token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")

    username = decode_token(pka_token)
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return {"username": username}


@app.get("/api/projects")
def projects(pka_token: str = Cookie(default=None)):
    if pka_token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    if decode_token(pka_token) is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    personal_path = Path("/opt/myPKA/PKM/My Life/Projects/project-index.md")
    ke_path = Path("/opt/myPKA/Team Knowledge/Kamer E-commerce/Projects/project-index.md")
    gr_path = Path("/opt/myPKA/Team Knowledge/Geldstroom Regie/Projects/project-index.md")

    def parse_personal(path: Path) -> list[str]:
        if not path.exists():
            return []
        result = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            cols = [c.strip() for c in line.split("|")]
            # cols[0] is empty (before first |), cols[1] = Project, cols[4] = Status
            if len(cols) < 5:
                continue
            name = cols[1]
            status = cols[4]
            if not name or name.replace("-", "") == "" or name == "Project":
                continue
            if not status or status.replace("-", "") == "" or status == "Status":
                continue
            if status != "Gearchiveerd":
                result.append(name)
        return result

    def parse_business(path: Path) -> list[str]:
        if not path.exists():
            return []
        result = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            cols = [c.strip() for c in line.split("|")]
            # cols[1] = Name, cols[4] = Status
            if len(cols) < 5:
                continue
            name = cols[1]
            status = cols[4]
            if not name or name.replace("-", "") == "" or name == "Name":
                continue
            if not status or status.replace("-", "") == "" or status == "Status":
                continue
            if status != "Gearchiveerd":
                result.append(name)
        return result

    personal = parse_personal(personal_path)
    business = parse_business(ke_path) + parse_business(gr_path)

    return {"personal": personal, "business": business}


@app.post("/api/logout")
def logout(response: Response):
    response.delete_cookie(key=COOKIE_NAME, samesite="lax", secure=True)
    return {"ok": True}
