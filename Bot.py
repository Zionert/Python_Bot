import discord
import random
from discord.ext import commands
from discord import Member, guild

bot = commands.Bot(command_prefix='.')
client = discord.Client()
@@ -9,7 +10,7 @@ def random_color():
    return random.randint(32, 200)

@bot.command()
async def ave(ctx, *,  avamember : discord.Member=None):
async def profile(ctx, *,  avamember : discord.Member=None):
    embed_obj = discord.Embed(colour=discord.Color.from_rgb(random_color(), random_color(), random_color()))
    embed_obj.set_author(name=avamember.name)
    embed_obj.set_thumbnail(url=avamember.avatar_url)
@@ -34,6 +35,33 @@ async def billy(ctx):

    await ctx.send('https://media.tenor.com/images/d9158014d27f0f59a87c3233ad478f0e/tenor.gif')

@bot.command()
async def clean(ctx, quantity):
    author = ctx.author
    role_indent = discord.utils.find(lambda r: r.name == 'TEST', author.guild.roles)
    if ctx.message.author.guild_permissions.administrator or role_indent in author.roles:
        quantity = int(quantity)
        await  ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit=quantity)
    else:
        embed = discord.Embed(title="Відказано в доступі.", description="Ти не маєш дозволу на це.",
                              color=discord.Color.from_rgb(random_color(), random_color(), random_color()))
        await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def add_role(ctx, *, avamember : discord.Member=None):
    await ctx.channel.purge(limit=1)
    author = ctx.author
    role = discord.utils.get(author.guild.roles, name="TEST")

    embed=discord.Embed(title="Роль успішно додано",
                        description="***{0}*** додав роль ***{1}*** учаснику ***{2}***".format(author, role, avamember),
                        color=discord.Color.from_rgb(random_color(), random_color(), random_color()))

    await ctx.send(embed=embed)
    await discord.Member.add_roles(avamember, role)

@bot.command()
async def thank(ctx, *, avamember : discord.Member=None):
    await ctx.channel.purge(limit=1)
@@ -47,5 +75,17 @@ async def call(ctx, *, avamember : discord.Member=None):
    await ctx.send(avamember.mention)
    await ctx.send('https://thumbs.gfycat.com/HarmoniousQueasyAlaskanhusky.webp')

bot.run('Nzc5NDg4Mzc3MTMyNjc5MTY5.X7hRHw.YNzbT8AFVJ7FgCesFRsfv3Ekyvo')
@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member=None):
    author = ctx.author
    role_indent = discord.utils.find(lambda r: r.name == 'Емодзі', author.guild.roles)
    if ctx.message.author.guild_permissions.administrator or role_indent in author.roles:
        role = discord.utils.get(author.guild.roles, name="Буйний")
        await discord.Member.add_roles(member, role)
        embed=discord.Embed(title="Людина в муті", description="**{0}** був замучений **{1}**!".format(member, author), color=discord.Color.from_rgb(random_color(), random_color(), random_color()))
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Відказано в доступі.", description="Ти не маєш дозволу на це.", color=discord.Color.from_rgb(random_color(), random_color(), random_color()))
        await ctx.send(embed=embed)

bot.run(token)