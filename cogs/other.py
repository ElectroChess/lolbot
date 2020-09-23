import discord
import random
import datetime
from discord.ext import commands

class other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'i responded in `{round(self.bot.latency * 1000)}`` milliseconds')

def setup(bot):
    bot.add_cog(other(bot))
