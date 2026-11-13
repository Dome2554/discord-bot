import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'บอท {bot.user} ออนไลน์แล้วบน Cloud!')

@bot.command(name='สูตรคูณ')
async def multiplication(ctx, number: int):
    table = "\n".join([f"{number} x {i} = {number * i}" for i in range(1, 13)])
    await ctx.send(f"```\nแม่สูตรคูณแม่ {number}:\n{table}\n```")

bot.run(os.getenv('TOKEN'))
