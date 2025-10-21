import discord
import yaml

from discord import Intents

discordIntents = Intents.default()
discordIntents.message_content = True
config = yaml.safe_load(open("config.yaml"))

class Middleman(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        print(f'Message from {message.author}: {message.content}')

client = Middleman(intents=discordIntents)
client.run(config.get('discord', {}).get("token", None))
