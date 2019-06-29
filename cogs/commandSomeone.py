import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import json
from random import randint

urlLennyFace = "https://i.kym-cdn.com/entries/icons/original/000/011/764/LennyFace.jpg"
settings = json.loads(open("json/settings.json").read())
guildId = settings["settings"]["guildId"]

class botSomeone(commands.Cog):

    def __init__(self, annoyo):
        self.annoyo = annoyo

#///////////////////// command /////////////////////
    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def someone(self, ctx):
        author = ctx.message.author
        guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
        memberList = guild.members
        randMember = memberList[randint(0, len(memberList) - 1)]
        while randMember.id == author.id or randMember.bot == True:
            randMember = memberList[randint(0, len(memberList) - 1)]
        await ctx.send(f"<@{randMember.id}>")

#///////////////////// error handling /////////////////////
    @someone.error
    async def someone_error(self, ctx, error):
        embed = discord.Embed (
            titel = "Support's on the way!",
            colour = discord.Colour.red()
        )
        embed.set_thumbnail(url = urlLennyFace)
        if isinstance(error, commands.CommandOnCooldown):
            embed.description = "You might try again in: {:.2f} seconds".format(error.retry_after)
            await ctx.send(embed = embed)

def setup(annoyo):
    annoyo.add_cog(botSomeone(annoyo))