import discord
from discord.ext import commands
import json
from random import randint

urlLennyFace = "https://i.kym-cdn.com/entries/icons/original/000/011/764/LennyFace.jpg"

class botUseless(commands.Cog):

    def __init__(self, annoyo):
        self.annoyo = annoyo

#///////////////////// command /////////////////////
    @commands.command()
    async def useless(self, ctx):
        arsedMeter = randint(0, 1)
        embed = discord.Embed (
            titel = "Useless command",
            colour = discord.Colour.red()
        )
        embed.set_thumbnail(url = urlLennyFace)
        if arsedMeter == 1:
            randomUseless = json.loads(open("json/useless.json").read())
            website = randomUseless["sites"][randint(0, len(randomUseless["sites"]) - 1)]
            embed.description = website
            await ctx.send(embed = embed)
        elif arsedMeter == 0:
            embed.description = "Can't be bothered right now, ask me later again!"
            await ctx.send(embed = embed)

def setup(annoyo):
    annoyo.add_cog(botUseless(annoyo))