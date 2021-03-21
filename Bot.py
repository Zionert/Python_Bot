import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='.')
client = discord.Client()

def random_color():
    return random.randint(32, 200)

@bot.command()
async def ave(ctx, *,  avamember : discord.Member=None):
    embed_obj = discord.Embed(colour=discord.Color.from_rgb(random_color(), random_color(), random_color()))
    embed_obj.set_author(name=avamember.name)
    embed_obj.set_thumbnail(url=avamember.avatar_url)
    embed_obj.add_field(name='Ролі', value=avamember.roles)
    if avamember.name == 'Zionert':
        embed_obj.description = 'Маэстро своего дела и укратитель дешёвок'
    elif avamember.name == 'Reyt1':
        embed_obj.description = '15 рочків, полюбляє грати в бравл старс і майнкрафт'
    else:
        embed_obj.description = 'Дешёвка'
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed_obj)

@bot.command()
async def role(ctx, *, avamember : discord.Member=None):
    await ctx.channel.purge(limit=1)
    await ctx.send([i for i in avamember.roles])

@bot.command()
async def billy(ctx):
    await ctx.channel.purge(limit=1)

    await ctx.send('https://media.tenor.com/images/d9158014d27f0f59a87c3233ad478f0e/tenor.gif')

@bot.command()
async def thank(ctx, *, avamember : discord.Member=None):
    await ctx.channel.purge(limit=1)

    await ctx.send(avamember.mention)
    await ctx.send('https://media1.tenor.com/images/eec4d682f2fc7d20abf2afdb7ba0ae51/tenor.gif?itemid=19120897')

@bot.command()
async def call(ctx, *, avamember : discord.Member=None):
    await ctx.channel.purge(limit=1)
    await ctx.send(avamember.mention)
    await ctx.send('https://thumbs.gfycat.com/HarmoniousQueasyAlaskanhusky.webp')

bot.run('Nzc5NDg4Mzc3MTMyNjc5MTY5.X7hRHw.YNzbT8AFVJ7FgCesFRsfv3Ekyvo')

