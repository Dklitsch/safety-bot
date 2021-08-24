import os
import discord
from discord.ext.commands import bot
from dotenv import load_dotenv
from discord_slash import SlashCommand
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='/')
slash = SlashCommand(bot, sync_commands=True)

intro = """Hello, I'm SafetyBot! I'm designed to help keep you safe during TTRPGS.

To help make the game fun for everyone, if anything in the game makes anyone uncomfortable, simply type '/x' into chat, you don't have to explain why. When the x-card is played, we simply edit out anything X-Carded. And if there is ever an issue, anyone can call for a break and we can talk privately.

If you think something uncomfortable is about to come up and you'd like to skip it, please press '/fade' to fade to black.

If you'd like to check that everyone is ok with what's happening, press '/o?' to do an o check."""

guild_ids = [int(os.getenv('GUILD_ID'))]


@slash.slash(name="safety_intro",
             description="Display the safety introduction.",
             guild_ids=guild_ids)
async def safety_intro(ctx):
    await ctx.send(intro)


@slash.slash(name="x",
             description="Display an X card.",
             guild_ids=guild_ids)
async def x(ctx):
    await ctx.send("https://skaldforge.files.wordpress.com/2018/12/X-Card.jpg?w=640")


@slash.slash(name="fade",
             description="End the scene.",
             guild_ids=guild_ids)
async def fade(ctx):
    await ctx.send("http://b.vimeocdn.com/ts/390/854/390854128_640.jpg")


@slash.slash(name="o",
             description="Check to see if everyone is ok.",
             guild_ids=guild_ids)
async def o_check(ctx):
    await ctx.send("O-check! Is everyone ok with what's happening?")

bot.run(TOKEN)
