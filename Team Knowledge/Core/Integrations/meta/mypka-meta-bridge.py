#!/usr/bin/env python3
"""
myPKA Meta Bridge — wraps the Meta Graph API for n8n and team use.
Exposes a simple HTTP API on localhost:BRIDGE_PORT.
"""
import os
import json
import asyncio
import aiohttp
from aiohttp import web

META_APP_ID        = os.environ["META_APP_ID"]
META_APP_SECRET    = os.environ["META_APP_SECRET"]
META_ACCESS_TOKEN  = os.environ["META_ACCESS_TOKEN"]
META_AD_ACCOUNT_ID = os.environ["META_AD_ACCOUNT_ID"]
META_API_VERSION   = os.environ.get("META_API_VERSION", "v21.0")
BRIDGE_PORT        = int(os.environ.get("BRIDGE_PORT", "8766"))

BASE_URL = f"https://graph.facebook.com/{META_API_VERSION}"


async def graph_get(session: aiohttp.ClientSession, path: str, params: dict = None) -> dict:
    p = {"access_token": META_ACCESS_TOKEN}
    if params:
        p.update(params)
    async with session.get(f"{BASE_URL}/{path}", params=p) as resp:
        return await resp.json()


async def graph_post(session: aiohttp.ClientSession, path: str, data: dict = None) -> dict:
    d = {"access_token": META_ACCESS_TOKEN}
    if data:
        d.update(data)
    async with session.post(f"{BASE_URL}/{path}", data=d) as resp:
        return await resp.json()


async def handle_health(request):
    return web.json_response({"status": "ok", "service": "mypka-meta-bridge"})


async def handle_account(request):
    account_id = META_AD_ACCOUNT_ID if META_AD_ACCOUNT_ID.startswith("act_") else f"act_{META_AD_ACCOUNT_ID}"
    async with aiohttp.ClientSession() as session:
        result = await graph_get(session, account_id, {
            "fields": "id,name,account_status,currency,timezone_name"
        })
    return web.json_response(result)


async def handle_request(request):
    try:
        body = await request.json()
    except Exception:
        return web.json_response({"error": "invalid JSON"}, status=400)

    method = body.get("method", "GET").upper()
    path   = body.get("path", "")
    params = body.get("params", {})

    if not path:
        return web.json_response({"error": "path is required"}, status=400)

    async with aiohttp.ClientSession() as session:
        if method == "GET":
            result = await graph_get(session, path, params)
        elif method == "POST":
            result = await graph_post(session, path, params)
        else:
            return web.json_response({"error": f"unsupported method: {method}"}, status=400)

    return web.json_response(result)


app = web.Application()
app.router.add_get("/health", handle_health)
app.router.add_get("/meta/account", handle_account)
app.router.add_post("/meta/request", handle_request)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=BRIDGE_PORT)
