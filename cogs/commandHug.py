import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from random import randint
import requests
import json

urlLennyFace = "https://i.kym-cdn.com/entries/icons/original/000/011/764/LennyFace.jpg"

class botHug(commands.Cog):

    def __init__(self, annoyo):
        self.annoyo = annoyo

#///////////////////// command /////////////////////
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def hug(self, ctx, member : discord.Member):
        arsedMeter = randint(0, 1)
        authorId = ctx.message.author.id
        memberId = member.id
        embed = discord.Embed (
            titel = "Hug gif",
            colour = discord.Colour.red()
        )
        url = "https://some-random-api.ml/animu/hug"
        r = requests.get(url = url)
        json = r.json()
        hugGif = json["link"]
        if arsedMeter == 1:
            embed.description = f"<@{authorId}> is hugging <@{memberId}>"
            embed.set_image(url = hugGif)
            await ctx.send(embed = embed)
        elif arsedMeter == 0:
            embed.description = f"You can't hug <@{memberId}> right now!"
            embed.set_image(url = urlLennyFace)
            await ctx.send(embed = embed)

#///////////////////// error handling /////////////////////
    @hug.error
    async def hug_error(self, ctx, error):
        embed = discord.Embed (
            titel = "Hugging failed",
            colour = discord.Colour.red()
        )
        embed.set_thumbnail(url = urlLennyFace)
        if isinstance(error, commands.MissingRequiredArgument):
            embed.description = "You are a dum dum, you need to hug someone, you can even hug yourself!"
            await ctx.send(embed = embed)
        elif isinstance(error, commands.CommandOnCooldown):
            embed.description = "You might try again in: {:.2f} seconds".format(error.retry_after)
            await ctx.send(embed = embed)

def setup(annoyo):
    annoyo.add_cog(botHug(annoyo))