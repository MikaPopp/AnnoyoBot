import discord
from discord.ext import commands
import os

token = "token here"

annoyo = commands.Bot(command_prefix = "!")

@annoyo.command()
@commands.has_any_role("Admin", "Owner")
async def load(ctx, extension):
    annoyo.load_extension(f"cogs.{extension}")
    print("loaded cog")

@annoyo.command()
@commands.has_any_role("Admin", "Owner")
async def unload(ctx, extension):
    annoyo.unload_extension(f"cogs.{extension}")
    print("unloaded cogs")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        annoyo.load_extension(f"cogs.{filename[:-3]}")
        
annoyo.run(token)