import discord
from discord.ext import commands

urlLennyFace = "https://i.kym-cdn.com/entries/icons/original/000/011/764/LennyFace.jpg"

class botEvents(commands.Cog):

    def __init__(self, annoyo):
        self.annoyo = annoyo





def setup(annoyo):
    annoyo.add_cog(botEvents(annoyo))