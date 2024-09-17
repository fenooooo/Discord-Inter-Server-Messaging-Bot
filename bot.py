
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX", "!")
CHANNEL_IDS = os.getenv("CHANNEL_IDS").split(",")

# Set up the bot
bot = commands.Bot(command_prefix=PREFIX)

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {{bot.user}}")

# Command to send a message to all linked channels
@bot.command(name='sendmsg', help="Send a message to linked channels on other servers.")
async def send_message(ctx, *, message):
    if str(ctx.channel.id) in CHANNEL_IDS:
        for channel_id in CHANNEL_IDS:
            channel = bot.get_channel(int(channel_id))
            if channel:
                await channel.send(f"Message from {ctx.guild.name}: {message}")
        await ctx.send("Message sent to all linked servers.")
    else:
        await ctx.send("This channel is not authorized to send inter-server messages.")

bot.run(TOKEN)
