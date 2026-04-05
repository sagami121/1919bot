import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

scheduler = AsyncIOScheduler()

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user}")
    
    scheduler.add_job(send_1919, CronTrigger(hour=19, minute=19))
    scheduler.start()

async def send_1919():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("1919")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "1919" in message.content:
        await message.channel.send("1919")

    await bot.process_commands(message)

bot.run(TOKEN)