import discord
from discord.ext import commands
from discord.ext.commands import Context
from dotenv import load_dotenv
import os
import random

load_dotenv()

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot iniciado como: {bot.user}')

@bot.command()
async def consejo(ctx:Context):
    frases:list[str] = [
        """
        Apaga la luz cuando no la estas utilizando
        """,
        """
        No dejar el agua corriendo mientras no la utilizas
        """,
        """
        Mientras dejas que el agua de la ducha se caliente pon una cubeta
        """,
        """
        Desconecta cargadores y electrónicos cuando no los necesitas
        """,
        """
        Camina o usa bicicleta recorridos cortos
        """
    ]

    await ctx.send(frases[random.randint(0, len(frases)-1)])

bot.run(os.environ["TOKEN"])