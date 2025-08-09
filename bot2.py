import discord
import requests
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

def OpenPicture(filepath:str) -> discord.File:
    file:discord.File
    with open(filepath, 'rb') as f:
        file = discord.File(f)
    return file

@bot.event
async def on_ready():
    print(f"Hello {bot.user}")

@bot.command()
async def meme(ctx:commands.Context):
    await ctx.send(file=OpenPicture(f'{os.getcwd()}\\memes\\{random.choice(os.listdir('memes'))}'))

def get_xkcd_comic():
    print("I'm called")
    res = requests.get('https://c.xkcd.com/random/comic', allow_redirects=True)
    id = res.url
    id = id.replace('https://xkcd.com/', '')
    id = id.replace('/', '')
    print(f'https://xkcd.com/{id}/info.0.json')
    json = requests.get(f'https://xkcd.com/{id}/info.0.json').json()
    return json['img']

def get_anime_image(text:str):
    res = requests.get(f'https://kitsu.io/api/edge/anime?filter[text]={text}')
    json = res.json()
    count = json['meta']['count']
    print(count)
    first_anime = json["data"][random.choice(list(range(int(count))))]
    return first_anime["attributes"]["posterImage"]["original"]

@bot.command()
async def xkcd(ctx):
    image_url = get_xkcd_comic()
    await ctx.send(image_url)
@bot.command()
async def anime(ctx, text:str):
    await ctx.send(get_anime_image(text))

bot.run(os.environ["TOKEN"])