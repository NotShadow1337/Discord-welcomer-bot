#libraries
import discord
from utils import *
from discord.ext import commands

#intents (used to detect member joins)
intents = discord.Intents.default()
intents.members = True

#client object
client = commands.Bot(command_prefix = 'z', case_insensitive = True, intents = intents)

#when the bot is ready to be used
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

#a simple command which sends the bots latency
@client.slash_command(name = 'ping', description = 'returns the client latency', usage = 'ping')
async def ping(ctx):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    await ctx.respond(f'Pong! **{round(client.latency * 1000)}**ms 🏓')

#the welcome channel command
@client.slash_command(name = 'welcome-channel', description = 'sets the welcome channel', usage = 'welcomes-channel <channel>')
async def welcome_channel(ctx, channel: discord.TextChannel):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    if str(get_channel()) == str(channel.id):
        await ctx.respond(f'{error_emoji} This channel is already the welcome channel.')
    else:
        set_channel(channel.id)
        await ctx.respond(f'{success_emoji} Welcome channel set to `{channel}`.')

#the welcome message command
@client.slash_command(name = 'welcome-message', description = 'sets the welcome message', usage = 'welcome-message <message>')
async def welcome_message(ctx, message: str):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    if str(get_message()) == str(message):
        await ctx.respond(f'{error_emoji} This message is already the welcome message.')
    else:
        set_message(message)
        await ctx.respond(f'{success_emoji} Welcome message set.')

#the welcome test command
@client.slash_command(name = 'welcome-test', description = 'sends a welcome message to the welcome channel', usage = 'welcome-test')
async def welcome_test(ctx):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    channel = client.get_channel(int(get_channel()))
    message = get_message()
    keywords = {
    'user.name' : f'{ctx.author.name}',
    'user.mention' : f'{ctx.author.mention}',
    'user.id' : f'{ctx.author.id}',
    'user.discriminator' : f'{ctx.author.discriminator}',
    'server.name' : f'{ctx.guild.name}',
    'server.id' : f'{ctx.guild.id}',
    'server.members' : f'{ctx.guild.member_count}',
}
    for key, value in keywords.items():
        message = message.replace(key, value)
    await channel.send(message)
    await ctx.respond(f'{success_emoji} Welcome message sent.')

#when a member joins the server
@client.event
async def on_member_join(member):
    if not int(guild_id) == member.guild.id:  return
    channel = client.get_channel(int(get_channel()))
    message = get_message()
    keywords = {
    'user.name' : f'{member.name}',
    'user.mention' : f'{member.mention}',
    'user.id' : f'{member.id}',
    'user.discriminator' : f'{member.discriminator}',
    'server.name' : f'{member.guild.name}',
    'server.id' : f'{member.guild.id}',
    'server.members' : f'{member.guild.member_count}',
}
    for key, value in keywords.items():
        message = message.replace(key, value)
    await channel.send(message)


#logging in to the bot
client.run(token)