import os

os.chdir("/Users/dtgs/Documents/run_equity_stocks/")
import discord
from discord.ext import commands
from discord.ext.commands import bot

client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(intents=discord.Intents.default(), command_prefix="!")


@client.event
async def on_ready():
    channel = client.get_channel(1156142819388432488)
    print("Connected!")
    await channel.send(file=discord.File("crossover_table.png"))
    exit()
    return "done!"


client.run("your discord token")
