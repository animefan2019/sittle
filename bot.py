import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='j!')

@bot.command()
async def finger(ctx):
    await ctx.send(":middle_finger:")

@bot.command()
async def dances(ctx):
    await ctx.send("https://media.discordapp.net/attachments/468970691501359107/476878885133221898/orange_justice.gif")



