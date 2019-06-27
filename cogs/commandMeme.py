import discord
from discord.ext import commands
import praw
import json
from random import randint

urlLennyFace = "https://i.kym-cdn.com/entries/icons/original/000/011/764/LennyFace.jpg"
settings = json.loads(open("json/settings.json").read())
reddit = praw.Reddit (client_id = settings["settings"]["clientId"],
                      client_secret = settings["settings"]["clientSecret"],
                      username = settings["settings"]["username"],
                      password = settings["settings"]["password"],
                      user_agent = settings["settings"]["userAgent"])


class botMeme(commands.Cog):

    def __init__(self, annoyo):
        self.annoyo = annoyo

#///////////////////// command /////////////////////
    @commands.command()
    async def meme(self, ctx):
        embed = discord.Embed (
            titel = "meme command",
            colour = discord.Colour.red()
        )
        arsedMeter = randint(0, 1)
        if arsedMeter == 1:
            memeSubmissions = reddit.subreddit(settings["settings"]["subreddit"]).new()
            postToPick = randint(1, 10)
            for i in range(0, postToPick):
                submission = next(x for x in memeSubmissions)
            embed.set_image(url = submission.url)
            await ctx.send(embed = embed)
        elif arsedMeter == 0:
            embed.description = "Can't be bothered right now, ask me later again!"
            embed.set_thumbnail(url = urlLennyFace)
            await ctx.send(embed = embed)

def setup(annoyo):
    annoyo.add_cog(botMeme(annoyo))