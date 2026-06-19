#!/usr/bin/env python3
"""
myPKA AI Bridge — HTTP gateway between external tools (n8n, Discord, etc.) and Claude Code CLI.
POST /ask  →  claude -p <message>  →  JSON response
Maintains conversation history per chat_id (last 10 exchanges, 30 min TTL).
"""
import json
import os
import subprocess
import threading
import time
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

WORKING_DIR = "/opt/myPKA"
PORT = int(os.environ.get("BRIDGE_PORT", "8765"))
TOKEN = os.environ.get("BRIDGE_TOKEN", "")
TIMEOUT = int(os.environ.get("BRIDGE_TIMEOUT", "180"))
HISTORY_TTL = 1800
HISTORY_MAX = 10

_history = {}
_history_lock = threading.Lock()


def _get_history(chat_id):
    with _history_lock:
        entry = _history.get(chat_id)
        if not entry:
            return []
        if time.time() - entry["updated"] > HISTORY_TTL:
            del _history[chat_id]
            return []
        return entry["turns"]

def _save_turn(chat_id, user_msg, assistant_msg):
    with _history_lock:
        entry = _history.setdefault(chat_id, {"updated": 0, "turns": []})
        entry["turns"].append({"user": user_msg, "assistant": assistant_msg})
        entry["turns"] = entry["turns"][-HISTORY_MAX:]
        entry["updated"] = time.time()

def _context_header(source: str) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    return (
        f"[Context]\n"
        f"Source: {source}\n"
        f"Date/time: {now}\n"
        f"You have full access to myPKA — files, databases, scripts, and tools. "
        f"Query them proactively when the question requires current data (tasks, goals, session logs, finances, etc.).\n"
        f"Discord integration: bot token and channel IDs are in /opt/n8n/mypka-discord-bridge.env. "
        f"Script: /opt/n8n/mypka-discord-bridge.py. "
        f"Guild ID: 1505365972473741423. "
        f"Personal #general: 1505520574024388691. "
        f"Kamer E-commerce #general: 1505520639824367656. "
        f"Use the Discord API (api.discord.com/api/v10) with the bot token to send messages or manage the server when asked.\n"
        f"This is a chat interface: keep responses concise and direct. "
        f"No lengthy preamble. Answer the question, then stop.\n"
    )

def _build_prompt(chat_id, message, source="chat"):
    header = _context_header(source)
    turns = _get_history(chat_id)
    if not turns:
        return f"{header}\n[Message]\n{message}"
    history_text = "\n".join(
        f"User: {t['user']}\nAssistant: {t['assistant']}" for t in turns
    )
    return f"{header}\n[Conversation history]\n{history_text}\n\n[New message]\nUser: {message}"


class Handler(BaseHTTPRequestHandler):
    def _auth(self):
        if not TOKEN:
            return True
        auth = self.headers.get("Authorization", "")
        return auth == f"Bearer {TOKEN}"

    def _respond(self, status, body):
        data = json.dumps(body, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(data))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if urlparse(self.path).path == "/health":
            self._respond(200, {"status": "ok"})
        else:
            self._respond(404, {"error": "not found"})

    def do_POST(self):
        if not self._auth():
            self._respond(401, {"error": "unauthorized"})
            return

        path = urlparse(self.path).path

        if path == "/ask":
            length = int(self.headers.get("Content-Length", 0))
            try:
                body = json.loads(self.rfile.read(length))
            except Exception:
                self._respond(400, {"error": "invalid JSON"})
                return

            message = (body.get("message") or "").strip()
            chat_id = str(body.get("chat_id") or "default")
            source = str(body.get("source") or "chat")
            if not message:
                self._respond(400, {"error": "message required"})
                return

            prompt = _build_prompt(chat_id, message, source)

            try:
                result = subprocess.run(
                    ["claude", "-p", prompt, "--dangerously-skip-permissions"],
                    cwd=WORKING_DIR,
                    capture_output=True,
                    text=True,
                    timeout=TIMEOUT,
                    env={**os.environ, "HOME": "/home/admin"},
                )
                if result.returncode == 0:
                    response = result.stdout.strip()
                    _save_turn(chat_id, message, response)
                    self._respond(200, {"response": response})
                else:
                    self._respond(500, {
                        "error": result.stderr.strip() or "claude exited non-zero",
                        "response": result.stdout.strip(),
                    })
            except subprocess.TimeoutExpired:
                self._respond(504, {"error": f"timeout after {TIMEOUT}s"})
            except Exception as e:
                self._respond(500, {"error": str(e)})

        else:
            self._respond(404, {"error": "unknown endpoint"})

    def log_message(self, fmt, *args):
        print(f"[mypka-ai-bridge] {self.address_string()} {fmt % args}")


class ThreadedServer(HTTPServer):
    def process_request(self, request, client_address):
        t = threading.Thread(target=self._handle, args=(request, client_address))
        t.daemon = True
        t.start()

    def _handle(self, request, client_address):
        self.finish_request(request, client_address)


if __name__ == "__main__":
    server = ThreadedServer(("0.0.0.0", PORT), Handler)
    print(f"[mypka-ai-bridge] listening on port {PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
