import urllib.request, json

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZDAzZTRhMy03ZThiLTQ1MjQtOGE2OC0zMDUzNjk1ZjQ5YzMiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwianRpIjoiZjQwM2E3YTYtMjdjOS00NzUzLWIxZTctMWVkMmY1MzBjYWYzIiwiaWF0IjoxNzc4OTcwOTA1fQ.d5QRgQiTMKMd_G7Jk6uM5WcLuu4yPWNot8SQE9m7tvU"
BASE_URL = "http://localhost:5678/api/v1"
DISCORD_BOT_TOKEN = "MTUwNTM2Mjk2MTAwOTc0MTk1NA.G84JiG.gbFxz7XZJ1af1m2uSZhyWlTKuzraLECOZQwQF0"
DISCORD_CHANNEL_TEAM_NOTIFICATIONS = "1505993795244789760"

HEADERS = {
    "X-N8N-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

def create_workflow(payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(f"{BASE_URL}/workflows", data=data, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def activate_workflow(workflow_id):
    req = urllib.request.Request(f"{BASE_URL}/workflows/{workflow_id}/activate", data=b'', headers=HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

# --- Skeleton: Manual Trigger alleen (niet actief) ---
def skeleton(name):
    return {
        "name": name,
        "nodes": [
            {
                "id": "manual-1",
                "name": "Manual Trigger",
                "type": "n8n-nodes-base.manualTrigger",
                "typeVersion": 1,
                "position": [240, 300],
                "parameters": {}
            }
        ],
        "connections": {},
        "settings": {"executionOrder": "v1"}
    }

# --- Team workflow: Team Inbox → Discord ---
team_workflow = {
    "name": "Team",
    "nodes": [
        {
            "id": "file-trigger-1",
            "name": "Team Inbox — Nieuw bestand",
            "type": "n8n-nodes-base.localFileTrigger",
            "typeVersion": 1,
            "position": [240, 300],
            "parameters": {
                "path": "/opt/myPKA/Team Inbox/",
                "events": ["add"],
                "recursive": False,
                "options": {}
            }
        },
        {
            "id": "discord-post-1",
            "name": "Discord — Team Inbox melding",
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4,
            "position": [500, 300],
            "parameters": {
                "method": "POST",
                "url": f"https://discord.com/api/v10/channels/{DISCORD_CHANNEL_TEAM_NOTIFICATIONS}/messages",
                "sendHeaders": True,
                "headerParameters": {
                    "parameters": [
                        {"name": "Authorization", "value": f"Bot {DISCORD_BOT_TOKEN}"}
                    ]
                },
                "sendBody": True,
                "specifyBody": "json",
                "jsonBody": "={\"content\": \"📥 **Nieuw item in Team Inbox**\\n`{{ $json.name }}`\"}",
                "options": {}
            }
        }
    ],
    "connections": {
        "Team Inbox — Nieuw bestand": {
            "main": [[{"node": "Discord — Team Inbox melding", "type": "main", "index": 0}]]
        }
    },
    "settings": {"executionOrder": "v1"}
}

results = {}

print("Aanmaken workflows...")

for name, payload in [
    ("Team", team_workflow),
    ("Personal", skeleton("Personal")),
    ("Kamer E-commerce", skeleton("Kamer E-commerce")),
    ("Geldstroom Regie", skeleton("Geldstroom Regie")),
]:
    result = create_workflow(payload)
    wf_id = result["id"]
    results[name] = wf_id
    print(f"  CREATED  {wf_id} | {name}")

# Activeer alleen de Team workflow
print("\nActiveren Team workflow...")
activate_workflow(results["Team"])
print(f"  ACTIVE   {results['Team']} | Team")

print("\nResultaat:")
for name, wf_id in results.items():
    status = "actief" if name == "Team" else "skelet (inactief)"
    print(f"  {wf_id} | {name} | {status}")
