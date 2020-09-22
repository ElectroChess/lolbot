import discord
from discord.ext import commands

class other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'<a:pong:757782930931187712> Pong! Bot Latency Is {round(self.bot.latency * 1000)} ms`')

def setup(bot):
    bot.add_cog(other(bot))
