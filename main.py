import discord
from discord import client
from discord.ext import commands

from music_cog import music_cog
from help_cog import help_cog

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot ready")
    await bot.add_cog(help_cog(client))
    await bot.add_cog(music_cog(client))

bot.run("MTA3Mjk4MTM2MTI3MjU1MzU3Mg.GSeKsC.Vw5ksL2qi2n4KPKfbyrAQMBClxX8A-bmhvAS4I")
