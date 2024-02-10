# This example requires the 'message_content' intent.

from dotenv import load_dotenv
from discord.ext import commands

import os
import discord

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', description='A simple discord bot to help users develop good habits.', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='ping')
async def pong(ctx):
    await ctx.send('ping!')



bot.run(os.getenv('DISCORD_BOT_TOKEN'))