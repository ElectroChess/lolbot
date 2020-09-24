import discord
import os
from discord.ext import commands

prefixes = ['<@!757743672379834448> ', 'lol ', 'lol']
bot = commands.Bot(command_prefix=prefixes)
bot.remove_command('help')

def is_it_me(ctx):
    return ctx.author.id == 475315771086602241

@bot.event
async def on_ready():
    print('Bot is online')

@bot.command()
@commands.check(is_it_me)
async def cog(ctx, typeOf, extension):
    if typeOf == 'load':
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded **{extension}**!')
    if typeOf == 'unload':
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unloaded **{extension}**!')      
    if typeOf == 'reload':        
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded **{extension}**!') 

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ('BOT_TOKEN'))