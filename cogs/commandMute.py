import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from random import randint
import asyncio
import requests

urlLennyFace = "https://i.kym-cdn.com/entries/icons/original/000/011/764/LennyFace.jpg"
guildId = 378219558248644608

class botMute(commands.Cog):

    def __init__(self, annoyo):
        self.annoyo = annoyo

#///////////////////// command /////////////////////
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def mute(self, ctx, member : discord.Member):
        guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
        roleMute = discord.utils.get(guild.roles, name = "muted")
        rolePending = discord.utils.get(guild.roles, name = "pending")
        author = ctx.message.author
        decision = randint(1, 100)
        arsedMeter = randint(0, 1)
        embed = discord.Embed (
            titel = "Kick command",
            colour = discord.Colour.red()
        )
        embed.set_thumbnail(url = urlLennyFace)
        if member != author:
            if arsedMeter == 1:
                if 1 <= decision <= 99:
                    member = author
                    embed.description = "Sucks to be you, you can get your roles back in 24 hours!"     
                    for x in range(1000):
                        try:
                            await member.remove_roles(member.top_role)
                        except:
                            break
                    await member.add_roles(roleMute) 
                    await member.send(embed = embed) 
                    await asyncio.sleep(86400)
                    await member.remove_roles(roleMute)
                    await member.add_roles(rolePending)              
                elif decision == 100:
                    embed.description = f"Wow {author} got you muted & deafened, you might want to get revenge in 24 hours!"
                    for x in range(1000):
                        try:
                            await member.remove_roles(member.top_role)
                        except:
                            break
                    await member.add_roles(roleMute)
                    await member.send(embed = embed)  
                    await asyncio.sleep(86400)
                    await member.remove_roles(roleMute)
                    await member.add_roles(rolePending)
            elif arsedMeter == 0:
                embed.description = "Can't be bothered right now, ask me later again!"
                await ctx.send(embed = embed)
        elif member == author:
            embed.description = "That's how you get 100% probability, but you wouldn't want to mute & deafen yourself!"
            await ctx.send(embed = embed)   

#///////////////////// error handling /////////////////////
    @mute.error
    async def mute_error(self, ctx, error):
        embed = discord.Embed (
            titel = "Support's on the way!",
            colour = discord.Colour.red()
        )
        embed.set_thumbnail(url = urlLennyFace)
        if isinstance(error, commands.MissingRequiredArgument):
            embed.description = "You know you can target someone, so do it!"
            await ctx.send(embed = embed)
        elif isinstance(error, commands.CommandOnCooldown):
            embed.description = "You might try again in: {:.2f} seconds".format(error.retry_after)
            await ctx.send(embed = embed)

def setup(annoyo):
    annoyo.add_cog(botMute(annoyo))