import discord
from discord.ext import commands, tasks
import json
from random import randint
import asyncio
import requests

guildId = 378219558248644608
urlDoge = "https://vignette.wikia.nocookie.net/epicness/images/0/05/Doge.png/revision/latest?cb=20180616043904"
urlCate = "https://i.kym-cdn.com/photos/images/original/000/581/251/5af.jpg"
urlPando = "https://cms.qz.com/wp-content/uploads/2018/05/china-pandas-eyes-turned-white-in-sichuan-2018-e1525405988661.jpg?quality=75&strip=all&w=410&h=230.67037692891472"
randomEntry = json.loads(open("json/names.json").read())
randomThought = json.loads(open("json/shower.json").read())

class botEvents(commands.Cog):

    def __init__(self, annoyo):
        self.annoyo = annoyo

    @commands.Cog.listener()
    async def on_ready(self):
        await self.annoyo.change_presence(status = discord.Status.do_not_disturb, activity=discord.Game(name = "annoys since 2019"))
        self.eventLoop.start()
        print("ready to annoy")

    @commands.Cog.listener()
    async def on_member_join(self, user : discord.User):
        guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
        rolePending = discord.utils.get(guild.roles, name = "pending")
        embed = discord.Embed (
            titel = "Ready to be annoyed ?",
            description = "Hello, stranger! Be sure to check out all the things in this server and get to know what could happen here!",
            colour = discord.Colour.red()
        )
        embed.set_footer(text = "AnnoyoBot - Version: 0.0.1")
        embed.set_image(url = "https://blogs.constantcontact.com/wp-content/uploads/2012/02/post-to-your-facebook-page-693x378.jpg")
        embed.set_thumbnail(url = "https://i.kym-cdn.com/entries/icons/original/000/011/764/LennyFace.jpg")
        embed.add_field(name = "Rules", value = "The rules are written down in the text channel 'rules', by getting any role on the server you accept them.", inline = False)
        embed.add_field(name = "Selfrole", value = "Click on any emoji to get the corresponding role.", inline = False)
        embed.add_field(name = "Have fun", value = "You might have already seen I'm a bot, but still!! I hope you have fun on the server, if not it seems to be a 'you' problem.", inline = False)
        await user.send(embed = embed)
        await user.add_roles()

#///////////////////// Random event loop /////////////////////
    @tasks.loop(seconds = 180)
    async def eventLoop(self):
        newName = randomEntry["groupNames"][randint(0, 48)]
        thought = randomThought["thoughts"][randint(0, 43)]
        currentEvent = 5
        if currentEvent == 1:
            embed = discord.Embed (
                titel = "Doge fact!",
                colour = discord.Colour.red()
            )
            embed.set_thumbnail(url = urlDoge)
            embed.set_footer(text = "Sponsored by Doge")
            guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
            textChannels = guild.text_channels
            randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            url = "https://some-random-api.ml/facts/dog"
            r = requests.get(url=url)
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
            guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
            textChannels = guild.text_channels
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
            guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
            textChannels = guild.text_channels
            randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            url = "https://some-random-api.ml/facts/panda"
            r = requests.get(url=url)
            json = r.json()
            fact = json["fact"]
            embed.description = fact
            await randChannel.send(embed = embed) 
        elif currentEvent == 4:
            guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
            textChannels = guild.text_channels
            randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            await randChannel.edit(name = newName)
        elif currentEvent == 5:
            guild = discord.utils.find(lambda g : g.id == guildId, self.annoyo.guilds)
            textChannels = guild.text_channels
            randChannel = self.annoyo.get_channel(textChannels[randint(0, len(textChannels) - 1)].id)
            await randChannel.send(thought, tts = True)

def setup(annoyo):
    annoyo.add_cog(botEvents(annoyo))