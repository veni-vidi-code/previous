import os
from os import environ as env
from re import compile

import aiohttp
from nextcord.ext import commands

bot = commands.Bot("=")
bot.load_extension("jishaku")

issue_regex = compile(r"##(\d+)")
discord_regex = compile(r"#!(\d+)")

@bot.listen()
async def on_message(message):
    if (result := issue_regex.search(message.content)):
        issue_id = result.groups()[0]
        await message.channel.send(f"https://github.com/nextcord/nextcord/issues/{issue_id}")
    if (result := discord_regex.search(message.content)):
        issue_id = result.groups()[0]
        await message.channel.send(f"https://github.com/rapptz/discord.py/issues/{issue_id}")

@bot.command()
async def todo(ctx):
    await ctx.send("https://github.com/nextcord/nextcord/projects/1 and going through all the issues")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}") 
    else:
        if os.path.isfile(filename):
            print(f"Unable to load {filename[:-3]}") 

async def startup():
	bot.session = aiohttp.ClientSession()

bot.loop.create_task(startup())
bot.run(env["TOKEN"])