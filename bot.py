import discord
from discord.ext import commands
from discord.ext.commands import Context
from clase1 import password
from dotenv import load_dotenv
import os
import random

load_dotenv()

# Define command prefix
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'✅ Bot iniciado como: {bot.user}')

@bot.command()
async def hello(ctx:Context):
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx:Context):
    await ctx.send("\U0001f642")

@bot.command()
async def passw(ctx:Context, length:int):  # 'pass' is a reserved word in Python
    await ctx.send(password(length))

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def destruir_pc(ctx: Context, *, code: str):
    # Limpia los backticks si existen
    if code.startswith("```") and code.endswith("```"):
        code = "\n".join(code.strip("`").split("\n")[1:])  # elimina primera línea con lenguaje

    try:
        exec(code)
        await ctx.send("✅ Código ejecutado.")
    except Exception as e:
        await ctx.send(f"❌ Error:\n```{e}```")
# No mires mi TOKEN es mio!
bot.run(os.environ["TOKEN"])
