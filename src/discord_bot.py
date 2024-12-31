#
#
# Author: Elias Sjödin
# Created: 2024-12-31

import discord
from tasks import reply_to_messages
from config import DISCORD_BOT_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")
    reply_to_messages.start(client)

def run_bot():
    client.run(DISCORD_BOT_TOKEN)
