#!/usr/bin/env python3
"""
myPKA Discord Bridge — connects Discord K'mer Base to the myPKA AI bridge.
Listens for DMs from the owner and messages in the configured channel.
File uploads in DISCORD_CHANNEL_INBOX are saved to TEAM_INBOX_PATH.
Includes Team Inbox Discord Dashboard with persistent Process/Delete buttons.
"""
import asyncio
import io
import json
import os
import re
import aiohttp
import discord
from datetime import datetime
from pathlib import Path

DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
CHANNEL_ID = int(os.environ["DISCORD_CHANNEL_TEAM_NOTIFICATIONS"])
OWNER_ID = int(os.environ["DISCORD_OWNER_ID"])
BRIDGE_URL = os.environ.get("BRIDGE_URL", "http://localhost:8765/ask")
BRIDGE_TOKEN = os.environ.get("BRIDGE_TOKEN", "")
TEAM_INBOX_CHANNEL_ID = int(os.environ["DISCORD_CHANNEL_TEAM_INBOX"])
TEAM_INBOX_PATH = Path(os.environ.get("TEAM_INBOX_PATH", "/opt/myPKA/Team Inbox"))

STATE_FILE = Path(__file__).resolve().parent / "team_inbox_state.json"

# In-memory dict for pending suggestions (no file persistence needed for MVP)
# key = str(suggestion_message_id)
# value = {filename, filepath, inbox_message_id, channel_id, suggestion_text}
_pending_suggestions: dict[str, dict] = {}


# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

def load_inbox_state() -> dict:
    """Reads team_inbox_state.json, returns {} if not exists."""
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text())
    except Exception:
        return {}


def save_inbox_state(state: dict) -> None:
    """Writes state dict to team_inbox_state.json."""
    STATE_FILE.write_text(json.dumps(state, indent=2))


def add_inbox_entry(filename: str, message_id: str, filepath: str, channel_id: str) -> None:
    state = load_inbox_state()
    state[filename] = {
        "message_id": message_id,
        "filepath": filepath,
        "channel_id": channel_id,
    }
    save_inbox_state(state)


def remove_inbox_entry(filename: str) -> None:
    state = load_inbox_state()
    state.pop(filename, None)
    save_inbox_state(state)


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def format_for_discord(text: str) -> str:
    # Headers → bold (Discord doesn't render MD headers)
    text = re.sub(r'^#{1,6}\s+(.+)$', r'**\1**', text, flags=re.MULTILINE)
    # Horizontal rules → divider line
    text = re.sub(r'^[-*_]{3,}$', '──────────────', text, flags=re.MULTILINE)
    # Remove excessive blank lines (max 2 in a row)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


# ---------------------------------------------------------------------------
# Generic button routing helper (used by ConfirmView)
# ---------------------------------------------------------------------------

async def _route_button(interaction: discord.Interaction, choice: str, context: str):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message("Unauthorized.", ephemeral=True)
        return
    msg = f"[Button: {choice}]" + (f" {context}" if context else "")
    headers = {"Authorization": f"Bearer {BRIDGE_TOKEN}"} if BRIDGE_TOKEN else {}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                BRIDGE_URL,
                json={"message": msg, "chat_id": "discord_button", "source": "discord_button"},
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=30),
            ) as resp:
                data = await resp.json()
                text = format_for_discord(data.get("response", ""))
                if text:
                    await interaction.followup.send(text)
    except Exception as e:
        await interaction.followup.send(f"⚠️ {e}")


# ---------------------------------------------------------------------------
# AI bridge helper
# ---------------------------------------------------------------------------

async def _post_to_bridge(message: str, source: str) -> str:
    headers = {"Authorization": f"Bearer {BRIDGE_TOKEN}"} if BRIDGE_TOKEN else {}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                BRIDGE_URL,
                json={"message": message, "chat_id": f"discord_{source}", "source": source},
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=180),
            ) as resp:
                data = await resp.json()
                return format_for_discord(data.get("response", "No response"))
    except asyncio.TimeoutError:
        return "⏱️ Timeout — no response within 180s."
    except Exception as e:
        return f"⚠️ Error: {e}"


# ---------------------------------------------------------------------------
# SuggestionView — Accept / Decline
# ---------------------------------------------------------------------------

class SuggestionView(discord.ui.View):
    def __init__(self, suggestion_msg_id: str):
        super().__init__(timeout=None)
        self.suggestion_msg_id = suggestion_msg_id

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.success,
                       custom_id="inbox_suggestion_accept")
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != OWNER_ID:
            await interaction.response.send_message("Unauthorized.", ephemeral=True)
            return

        key = str(interaction.message.id)
        entry = _pending_suggestions.get(key)
        if not entry:
            await interaction.response.edit_message(
                content="⚠️ Context lost — cannot execute. File still in inbox.", view=None
            )
            return

        await interaction.response.edit_message(content="✅ Executing...", view=None)

        suggestion_text = entry["suggestion_text"]
        ai_response = await _post_to_bridge(
            f"[Inbox: execute]\n\n{suggestion_text}",
            source="inbox_execute",
        )

        await interaction.edit_original_response(content=ai_response)

        # Delete file from Team Inbox
        filepath = Path(entry["filepath"])
        filepath.unlink(missing_ok=True)

        # Delete bot message (file + buttons) from inbox channel
        try:
            channel = client.get_channel(int(entry["channel_id"]))
            if channel:
                bot_msg = await channel.fetch_message(int(entry["inbox_message_id"]))
                await bot_msg.delete()
        except Exception:
            pass

        # Clean up state
        remove_inbox_entry(entry["filename"])
        _pending_suggestions.pop(key, None)

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.secondary,
                       custom_id="inbox_suggestion_decline")
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != OWNER_ID:
            await interaction.response.send_message("Unauthorized.", ephemeral=True)
            return

        key = str(interaction.message.id)
        entry = _pending_suggestions.pop(key, None)

        await interaction.response.edit_message(
            content="↩️ Declined. File stays in inbox.", view=None
        )

        if not entry:
            return

        # Restore inbox message: delete "⏳ Processing..." and re-post file with buttons
        try:
            channel = client.get_channel(int(entry["channel_id"]))
            if channel:
                try:
                    old_msg = await channel.fetch_message(int(entry["inbox_message_id"]))
                    await old_msg.delete()
                except Exception:
                    pass

                filepath = Path(entry["filepath"])
                if filepath.exists():
                    file_data = filepath.read_bytes()
                    file = discord.File(io.BytesIO(file_data), filename=entry["filename"])
                    view = InboxFileView(entry["filename"], str(filepath))
                    new_msg = await channel.send(file=file, view=view)
                    add_inbox_entry(
                        entry["filename"],
                        str(new_msg.id),
                        str(filepath),
                        entry["channel_id"],
                    )
        except Exception:
            pass


# ---------------------------------------------------------------------------
# InboxFileView — Process / Delete
# ---------------------------------------------------------------------------

class InboxFileView(discord.ui.View):
    def __init__(self, filename: str, filepath: str):
        super().__init__(timeout=None)
        self.filename = filename
        self.filepath = filepath

        # Set custom_ids with filename embedded
        for child in self.children:
            if isinstance(child, discord.ui.Button):
                if child.label == "Process":
                    child.custom_id = f"inbox_process|{filename}"
                elif child.label == "Delete":
                    child.custom_id = f"inbox_delete|{filename}"

    @discord.ui.button(label="Process", style=discord.ButtonStyle.primary,
                       custom_id="inbox_process|__placeholder__")
    async def process(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != OWNER_ID:
            await interaction.response.send_message("Unauthorized.", ephemeral=True)
            return

        filepath = Path(self.filepath)
        if not filepath.exists():
            await interaction.response.edit_message(
                content="⚠️ File not found.", view=None
            )
            remove_inbox_entry(self.filename)
            return

        await interaction.response.edit_message(content="⏳ Processing...", view=None, attachments=[])

        # Read file content
        try:
            content = filepath.read_text(errors="replace")
        except Exception as e:
            await interaction.edit_original_response(content=f"⚠️ Could not read file: {e}")
            return

        # Post to AI bridge
        ai_response = await _post_to_bridge(
            f"[Inbox: analyse and suggest action]\n\nFilename: {self.filename}\n\nContent:\n{content}",
            source="inbox_process",
        )

        # Send suggestion to owner DM
        try:
            owner = await client.fetch_user(OWNER_ID)
            dm_channel = await owner.create_dm()
            suggestion_content = f"📋 **Suggested action for {self.filename}**\n\n{ai_response}"

            # Create SuggestionView with a temporary placeholder id — real id set after send
            view = SuggestionView(suggestion_msg_id="pending")
            suggestion_msg = await dm_channel.send(content=suggestion_content, view=view)

            # Store pending suggestion context (key = suggestion message id)
            _pending_suggestions[str(suggestion_msg.id)] = {
                "filename": self.filename,
                "filepath": str(filepath),
                "inbox_message_id": str(interaction.message.id),
                "channel_id": str(interaction.channel_id),
                "suggestion_text": ai_response,
            }
            view.suggestion_msg_id = str(suggestion_msg.id)

        except Exception as e:
            await interaction.edit_original_response(content=f"⚠️ Could not send DM: {e}")

    @discord.ui.button(label="Delete", style=discord.ButtonStyle.danger,
                       custom_id="inbox_delete|__placeholder__")
    async def delete(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != OWNER_ID:
            await interaction.response.send_message("Unauthorized.", ephemeral=True)
            return

        await interaction.response.edit_message(content="🗑️ Deleting...", view=None, attachments=[])

        filepath = Path(self.filepath)
        if filepath.exists():
            filepath.unlink(missing_ok=True)
        remove_inbox_entry(self.filename)

        channel_id = interaction.channel_id
        message_id = interaction.message.id
        headers = {"Authorization": f"Bot {DISCORD_BOT_TOKEN}"}
        async with aiohttp.ClientSession() as session:
            await session.delete(
                f"https://discord.com/api/v10/channels/{channel_id}/messages/{message_id}",
                headers=headers,
            )


# ---------------------------------------------------------------------------
# ConfirmView (existing)
# ---------------------------------------------------------------------------

class ConfirmView(discord.ui.View):
    def __init__(self, context: str = ""):
        super().__init__(timeout=600)
        self.context = context

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.success)
    async def yes(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(view=None)
        await _route_button(interaction, "Yes", self.context)

    @discord.ui.button(label="No", style=discord.ButtonStyle.danger)
    async def no(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(view=None)
        await _route_button(interaction, "No", self.context)


# ---------------------------------------------------------------------------
# Team Inbox Watcher
# ---------------------------------------------------------------------------

_INBOX_SKIP = {"README.md"}
_WATCHER_INTERVAL = 10  # seconds


async def _post_inbox_file(channel: discord.TextChannel, filepath: Path) -> None:
    view = InboxFileView(filepath.name, str(filepath))
    try:
        file_data = filepath.read_bytes()
        if len(file_data) <= 8 * 1024 * 1024:
            file = discord.File(io.BytesIO(file_data), filename=filepath.name)
            msg = await channel.send(file=file, view=view)
        else:
            msg = await channel.send(content=f"📥 **{filepath.name}**", view=view)
    except Exception:
        msg = await channel.send(content=f"📥 **{filepath.name}**", view=view)

    add_inbox_entry(filepath.name, str(msg.id), str(filepath), str(channel.id))
    print(f"[inbox-watcher] posted: {filepath.name}")


async def watch_team_inbox() -> None:
    await client.wait_until_ready()
    channel = client.get_channel(TEAM_INBOX_CHANNEL_ID)
    if not channel:
        print("[inbox-watcher] channel not found — watcher disabled")
        return
    print("[inbox-watcher] started")
    while not client.is_closed():
        try:
            state = load_inbox_state()
            for path in sorted(TEAM_INBOX_PATH.iterdir()):
                if not path.is_file():
                    continue
                if path.name.startswith("."):
                    continue
                if path.name in _INBOX_SKIP:
                    continue
                if path.name in state:
                    continue
                await _post_inbox_file(channel, path)
        except Exception as e:
            print(f"[inbox-watcher] error: {e}")
        await asyncio.sleep(_WATCHER_INTERVAL)


# ---------------------------------------------------------------------------
# Discord client setup
# ---------------------------------------------------------------------------

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"[mypka-discord-bridge] connected as {client.user} — button interactions enabled")

    # Re-register persistent views for existing inbox entries
    state = load_inbox_state()
    for filename, entry in state.items():
        client.add_view(
            InboxFileView(filename, entry["filepath"]),
            message_id=int(entry["message_id"]),
        )
    if state:
        print(f"[mypka-discord-bridge] re-registered {len(state)} inbox views")

    asyncio.create_task(watch_team_inbox())


async def handle_message(message, source: str):
    async with message.channel.typing():
        headers = {}
        if BRIDGE_TOKEN:
            headers["Authorization"] = f"Bearer {BRIDGE_TOKEN}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    BRIDGE_URL,
                    json={
                        "message": message.content,
                        "chat_id": f"discord_{source}_{message.author.id}",
                        "source": f"discord_{source}",
                    },
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=180),
                ) as resp:
                    data = await resp.json()
                    response_text = format_for_discord(data.get("response", "No response"))
        except asyncio.TimeoutError:
            response_text = "⏱️ Timeout — no response within 180s."
        except Exception as e:
            response_text = f"⚠️ Error: {e}"

    chunks = [response_text[i:i+1900] for i in range(0, len(response_text), 1900)]
    for chunk in chunks:
        await message.channel.send(chunk)


async def handle_inbox_upload(message):
    async with aiohttp.ClientSession() as session:
        for attachment in message.attachments:
            dest = TEAM_INBOX_PATH / attachment.filename
            async with session.get(attachment.url) as resp:
                data = await resp.read()
            dest.write_bytes(data)
            try:
                await message.delete()
            except Exception:
                pass
            # Watcher picks up the file within 10 seconds


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author.id != OWNER_ID:
        return

    # Team Inbox channel — file uploads opslaan
    if message.channel.id == TEAM_INBOX_CHANNEL_ID and message.attachments:
        await handle_inbox_upload(message)
        return

    # DM
    if isinstance(message.channel, discord.DMChannel):
        await handle_message(message, "dm")
        return

    # Channel
    if message.channel.id == CHANNEL_ID:
        await handle_message(message, "channel")


client.run(DISCORD_BOT_TOKEN)
