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

gen_emoji = lambda:random.choice("\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923")
flip_coin = lambda: random.random > 0.5 if "CARA" else "CRUZ"

@bot.event
async def on_ready():
    print(f'Bot iniciado como: {bot.user}')

@bot.command()
async def hello(ctx:Context):
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx:Context):
    await ctx.send("\U0001f642")

@bot.command()
async def passw(ctx:Context, length:int):
    await ctx.send(password(length))

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(str(choices).split(',')))

@bot.command()
async def flipCoin(ctx, ):
    await ctx.send(flip_coin())
# La mejor feature de tu vida
@bot.command()
async def destruirPc(ctx: Context, *, code: str):
    """
        Okay dire la verdad yo intente crear esto por mi cuenta 
        antes de la anterior clase pero pues no pude asi que
        lo saque de internet
    """
    if code.startswith("```") and code.endswith("```"):
        code = "\n".join(code.strip("`").split("\n")[1:])

    try:
        exec(code)
        await ctx.send("Código ejecutado.")
    except Exception as e:
        await ctx.send(f"Error:\n```{e}```")
# No mires mi TOKEN es mio!
bot.run(os.environ["TOKEN"])
