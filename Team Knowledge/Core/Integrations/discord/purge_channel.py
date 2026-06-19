#!/usr/bin/env python3
"""Purge all messages from a Discord channel. Handles messages older than 14 days."""
import argparse
import asyncio
import os
import sys
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

import discord

def parse_args():
    parser = argparse.ArgumentParser(description="Purge all messages from a Discord channel.")
    parser.add_argument("--channel", required=True, help="Channel ID to purge")
    return parser.parse_args()

async def purge(token: str, channel_id: int) -> int:
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    count = 0

    @client.event
    async def on_ready():
        nonlocal count
        channel = client.get_channel(channel_id)
        if channel is None:
            print(f"ERROR: channel {channel_id} not found", file=sys.stderr)
            await client.close()
            return
        recent = await channel.purge(limit=None)
        count += len(recent)
        async for message in channel.history(limit=None):
            await message.delete()
            count += 1
            await asyncio.sleep(0.5)
        await client.close()

    await client.start(token)
    return count

def main():
    args = parse_args()
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        print("ERROR: DISCORD_BOT_TOKEN not set", file=sys.stderr)
        sys.exit(1)
    deleted = asyncio.run(purge(token, int(args.channel)))
    print(f"Purged {deleted} messages from channel {args.channel}")

if __name__ == "__main__":
    main()
