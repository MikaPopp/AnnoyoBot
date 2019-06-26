import discord
from discord.ext import commands, tasks
import json
from random import randint
import asyncio
import requests

emojiNormie = "🔥"
urlDoge = "https://vignette.wikia.nocookie.net/epicness/images/0/05/Doge.png/revision/latest?cb=20180616043904"
urlCate = "https://i.kym-cdn.com/photos/images/original/000/581/251/5af.jpg"
urlPando = "https://cms.qz.com/wp-content/uploads/2018/05/china-pandas-eyes-turned-white-in-sichuan-2018-e1525405988661.jpg?quality=75&strip=all&w=410&h=230.67037692891472"
urlLennyFace = "https://i.kym-cdn.com/entries/icons/original/000/011/764/LennyFace.jpg"
urlBlahBlah = "https://blogs.constantcontact.com/wp-content/uploads/2012/02/post-to-your-facebook-page-693x378.jpg"
randomEntry = json.loads(open("json/names.json").read())
randomThought = json.loads(open("json/shower.json").read())
settings = json.loads(open("json/settings.json").read())
guildId = settings["settings"]["guildId"]
channelIdSelfrole = settings["settings"]["channelIdSelfrole"]
rolenameNormie = settings["settings"]["rolenameNormie"] 
rolenamePending = settings["settings"]["rolenamePending"]

class botEvents(commands.Cog):

    def __init__(self, annoyo):
        self.annoyo = annoyo

    @commands.Cog.listener()
    async def on_ready(self):
        await self.annoyo.change_presence(status = discord.Status.do_not_disturb, activity=discord.Game(name = "annoys since 2019"))
        self.eventLoop.start()
        print("Ready to annoy")
        embed = discord.Embed (
            titel = "Selfrole",
            description = "Take a role, it's free!",
            colour = discord.Colour.red()
        )
        embed.set_thumbnail(url = urlLennyFace)
        channelSelfrole = self.annoyo.get_channel(channelIdSelfrole)
        reactMessage = await channelSelfrole.send(embed = embed)
        await reactMessage.add_reaction(emojiNormie)

    @commands.Cog.listener()
    async def on_member_join(self, user : discord.User):
        guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
        rolePending = discord.utils.get(guild.roles, name = rolenamePending)
        embed = discord.Embed (
            titel = "Ready to be annoyed ?",
            description = "Hello, stranger! Be sure to check out all the things in this server and get to know what could happen here!",
            colour = discord.Colour.red()
        )
        embed.set_footer(text = "AnnoyoBot - Version: 0.0.1")
        embed.set_image(url = urlBlahBlah)
        embed.set_thumbnail(url = urlLennyFace)
        embed.add_field(name = "Selfrole", value = "Click on any emoji to get the corresponding role.", inline = False)
        embed.add_field(name = "Have fun", value = "You might have already seen I'm a bot, but still!! I hope you have fun on the server, if not it seems to be a 'you' problem.", inline = False)
        await user.send(embed = embed)
        await user.add_roles(rolePending)

#///////////////////// Random event loop /////////////////////
    @tasks.loop(seconds = 180) 
    async def eventLoop(self):
        guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
        newName = randomEntry["groupNames"][randint(0, 48)]
        thought = randomThought["thoughts"][randint(0, 43)]
        currentEvent = randint(1, 5)
        if currentEvent == 1:
            embed = discord.Embed (
                titel = "Doge fact!",
                colour = discord.Colour.red()
            )
            embed.set_thumbnail(url = urlDoge)
            embed.set_footer(text = "Sponsored by Doge")
            textChannels = guild.text_channels
            randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            while randChannel.id == channelIdSelfrole:
                randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            url = "https://some-random-api.ml/facts/dog"
            r = requests.get(url = url)
            json = r.json()
            fact = json["fact"]
            embed.description = fact
            await randChannel.send(embed = embed)
        elif currentEvent == 2:
            embed = discord.Embed (
                titel = "Cate fact!",
                colour = discord.Colour.red()
            )
            embed.set_thumbnail(url = urlCate)
            embed.set_footer(text = "Sponsored by Cate")
            textChannels = guild.text_channels
            randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            while randChannel.id == channelIdSelfrole:
                randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            url = "https://some-random-api.ml/facts/cat"
            r = requests.get(url = url)
            json = r.json()
            fact = json["fact"]
            embed.description = fact
            await randChannel.send(embed = embed)
        elif currentEvent == 3:
            embed = discord.Embed (
                titel = "Pando fact!",
                colour = discord.Colour.red()
            )
            embed.set_thumbnail(url = urlPando)
            embed.set_footer(text = "Sponsored by Pando")
            textChannels = guild.text_channels
            randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            while randChannel.id == channelIdSelfrole:
                randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            url = "https://some-random-api.ml/facts/panda"
            r = requests.get(url = url)
            json = r.json()
            fact = json["fact"]
            embed.description = fact
            await randChannel.send(embed = embed) 
        elif currentEvent == 4:
            textChannels = guild.text_channels
            randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            while randChannel.id == channelIdSelfrole:
                randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            await randChannel.edit(name = newName)
        elif currentEvent == 5:
            textChannels = guild.text_channels
            randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            while randChannel.id == channelIdSelfrole:
                randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            await randChannel.send(thought, tts = True)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embed = discord.Embed (
            titel = "Support's on the way!",
            description = "I couldn't remember any command like this, I swear... I don't have alzheimer!!",
            colour = discord.Colour.purple()
        )
        embed.set_thumbnail(url = urlLennyFace)
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed = embed)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
        roleNormie = discord.utils.get(guild.roles, name = rolenameNormie)
        if reaction.message.channel.id != channelIdSelfrole:
            return
        elif str(reaction.emoji) == emojiNormie:
            await user.add_roles(roleNormie)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
        roleNormie = discord.utils.get(guild.roles, name = rolenameNormie)
        if reaction.message.channel.id != channelIdSelfrole:
            return
        elif str(reaction.emoji) == emojiNormie:
            await user.remove_roles(roleNormie)

def setup(annoyo):
    annoyo.add_cog(botEvents(annoyo))