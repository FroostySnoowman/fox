import discord
import random
import json
import asyncio
import os
import datetime
from datetime import datetime
from time import strftime
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='~', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
	activity = discord.Game(name="With Foxes", type=3)
	await client.change_presence(status=discord.Status.online, activity=activity)
	print('Bot is up and running :)'.format(client))

@client.event
async def on_message(ctx):
  if "welcome" in ctx.content.lower():
    await ctx.add_reaction('<:Hearts:773269286084542505>')
  if ctx.content.startswith("rules"):
    embed=discord.Embed(title="FoxHut Rules", url="", 
    description="1. Follow Discord ToS and Community Guidelines. \n \n2. Be respectful to EVERYONE in this server. \n \n3. No discrimination \n- Don't discriminate anyone based on their religion/creed, sexuality, gender, culture, etc. \n \n4. Don't be toxic. \n \n5. This is a SFW server, don't post any NSFW or gore related content. (NSFW topics are allowed to some extent, but NSFW media is not tolerated.) \n \n6. Avoid spamming. \n \n7. Listen to staff. \n \n8. Please reserach your topics before trying to educate others. It's okay to make a guess but don't spread false fact statements in the server. If you're not sure about the facts you're talking about, inform the people you are talking to that you're not sure. \n \n9. Sending/Linking any harmful material such as viruses, IP grabbers or harmware results in an immediate and permanent ban. \n \nDM staff if you have questions relating to the rules. \n \nDiscord TOS: https://discord.com/terms \nCommunity Guidelines: https://discord.com/guidelines", 
    color=discord.Color.blue())
    await ctx.author.send(embed=embed)
    await ctx.channel.send(f'{ctx.author.mention}, You have gotten mail!', delete_after=5)
  if ctx.content.startswith("Rules"):
    embed=discord.Embed(title="FoxHut Rules", url="", 
    description="1. Follow Discord ToS and Community Guidelines. \n \n2. Be respectful to EVERYONE in this server. \n \n3. No discrimination \n- Don't discriminate anyone based on their religion/creed, sexuality, gender, culture, etc. \n \n4. Don't be toxic. \n \n5. This is a SFW server, don't post any NSFW or gore related content. (NSFW topics are allowed to some extent, but NSFW media is not tolerated.) \n \n6. Avoid spamming. \n \n7. Listen to staff. \n \n8. Please reserach your topics before trying to educate others. It's okay to make a guess but don't spread false fact statements in the server. If you're not sure about the facts you're talking about, inform the people you are talking to that you're not sure. \n \n9. Sending/Linking any harmful material such as viruses, IP grabbers or harmware results in an immediate and permanent ban. \n \nDM staff if you have questions relating to the rules. \n \nDiscord TOS: https://discord.com/terms \nCommunity Guidelines: https://discord.com/guidelines", 
    color=discord.Color.blue())
    await ctx.author.send(embed=embed)
    await ctx.channel.send(f'{ctx.author.mention}, You have gotten mail!', delete_after=5)
  await client.process_commands(ctx)

@client.event
async def on_member_join(member):
  x = client.get_channel(752988771053600812)
  await x.send(f"{member.name} just joined the server! Say hi!")

client.run('')
