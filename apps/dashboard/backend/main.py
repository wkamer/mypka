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


@app.post("/api/logout")
def logout(response: Response):
    response.delete_cookie(key=COOKIE_NAME, samesite="lax")
    return {"ok": True}
