import discord
from discord.ext import commands
from random import randint
import random

urlLennyFace = "https://i.kym-cdn.com/entries/icons/original/000/011/764/LennyFace.jpg"
urlWelp = "https://cdn.pixilart.com/photos/large/ac41d828090b245.jpg"

class botHelp(commands.Cog):

    def __init__(self, annoyo):
        self.annoyo = annoyo

#///////////////////// command /////////////////////
    @commands.command()
    async def help(self, ctx, command = None):
        fakeCommands = ["purge", "ban", "kick", "cookie", "profile", "danbooru", "pepo", "avatar", "coinflip", "votekick", "ship"]
        realCommands = ["mute", "useless", "pat", "hug", "meme", "someone"]
        embed = discord.Embed (
            titel = "Kick command",
            colour = discord.Colour.red()
        )
        embed.set_thumbnail(url = urlLennyFace)
        embed.set_image(url = urlWelp)
        if command == None:
            commandsPost = []
            for x in range(3):
                commandsPost.append(fakeCommands[randint(0, len(fakeCommands) - 1)])
            commandsPost.append(realCommands[randint(0, len(realCommands) - 1)])
            random.shuffle(commandsPost)
            embed.description = "Here are some commands, I don't post all of the commands I know at once. Oh and you might want to test them, since some of them might not work ¯\_(ツ)_/¯"
            embed.add_field(name = "Commands", value = f"{commandsPost[0]}, {commandsPost[1]}, {commandsPost[2]}, {commandsPost[3]}", inline = False)
            await ctx.send(embed = embed)
        elif command == "mute":
            embed.description = "Wow! I can do something with this. TL;DR: 99% you get muted & deafened and 1% your target will experience this."
            embed.add_field(name = "!mute [@user]", value = "oh btw this command has a 50/50 chance to work or not.", inline = False)
            await ctx.send(embed = embed)
        elif command == "useless":
            embed.description = "Wow! I can do something with this. TL;DR: you get a useless website!"
            embed.add_field(name = "!useless", value = "oh btw this command has a 50/50 chance to work or not.", inline = False)
            await ctx.send(embed = embed)
        elif command == "pat":
            embed.description = "This will be very easy!"
            embed.add_field(name = "!pat [@user]", value = "I mean it's you patting someone else.", inline = False)
            await ctx.send(embed = embed)
        elif command == "hug":
            embed.description = "If you love someone, hug him!"
            embed.add_field(name = "!hug [@user]", value = "If you are reading this, you can also hug me ( ͡~ ͜ʖ ͡°)", inline = False)
            await ctx.send(embed = embed)
        elif command == "meme":
            embed.description = "freshest and newest dankmemes!"
            embed.add_field(name = "!meme", value = "Well you sure know what a meme is, save them before it's too late.", inline = False)
            await ctx.send(embed = embed)
        elif command == "someone":
            embed.description = "Who is this someone ? Find it out!"
            embed.add_field(name = "!someone", value = "I'm pretty sure someone is getting annoyed...", inline = False)
            await ctx.send(embed = embed)
        elif command == "kick":
            embemd.description = "This might be it, try it!"
            embed.add_field(name = "!kick [@user] [reason]", value = "I mean you should know what that does", inline = False)
            await ctx.send(embed = embed)
        elif command == "purge":
            embemd.description = "Maybe this one ? TL;DR deletes given amount of messages."
            embed.add_field(name = "!purge [amount]", value = "i guess it deletes the messages in the channel you type it in", inline = False)
            await ctx.send(embed = embed)
        elif command == "coinflip":
            embed.description = "I think this is the command I use for my decisions."
            embed.add_field(name = "!coinflip", value = "50/50, heads or tails", inline = False)
        else:
            embed.add_field(name = "¯\_(ツ)_/¯", value = "Well I really couldn't find anything",  inline = False)
            await ctx.send(embed = embed)
        
def setup(annoyo):
    annoyo.add_cog(botHelp(annoyo))