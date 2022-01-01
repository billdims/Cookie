import discord
from discord.ext import commands
import discord.utils


# Token

TOKEN = ''


# Prefix

cookie = commands.Bot(command_prefix='/')


# Startup

@cookie.event
async def on_ready():
    print('Cookie is online.')


# Ping

@cookie.command()
async def ping(ctx):
    await ctx.send(f'The ping is currently {round(cookie.latency * 1000)}ms.')


# Suggestion / Announcement / Poll

@cookie.command()
async def suggestion(ctx, *, description):
    embed = discord.Embed(title='Suggestion', description=f'Suggested by {ctx.author.mention}', color=discord.Color.purple())
    embed.add_field(name='Description:', value=description)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')


@cookie.command()
@commands.has_permissions(administrator=True)
async def announcement(ctx, *, message):
    embed = discord.Embed(title='Announcement', color=discord.Color.purple())
    embed.set_footer(text=f'Announced by - {ctx.author}', icon_url=ctx.author.avatar_url)
    embed.add_field(name='Description', value=f'{message}', inline=False)
    await ctx.send(embed=embed)


@cookie.command()
async def poll(ctx, *, message):
    embed = discord.Embed(title='Poll', color=discord.Color.purple())
    embed.set_footer(text=f'Created by - {ctx.author}', icon_url=ctx.author.avatar_url)
    embed.add_field(name='Description', value=f'{message}', inline=False)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')


# Punishments

@cookie.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title='Ban', description=f'{member.mention} has been banned by {ctx.author.mention}', color=discord.Color.purple())
    embed.add_field(name='Reason', value=reason, inline=False)
    await ctx.send(embed=embed)


@cookie.command()
@commands.has_permissions(mute_members=False)
async def mute(ctx, member: discord.Member, reason=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role)
    embed = discord.Embed(title='Mute',description=f'{member.mention} has been muted by {ctx.author.mention}', color=discord.Color.orange())
    embed.add_field(name='Reason', value=reason, inline=False)
    await ctx.send(embed=embed)


# Run

cookie.run(TOKEN)