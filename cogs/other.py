import discord
import random
import datetime
from discord.ext import commands

class other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'<a:pong:757782930931187712> Pong! Bot Latency Is {round(self.bot.latency * 1000)} ms`')
    
    @commands.command()
    async def avatar(self, ctx, member:discord.Member=None):
        if not member:
            member = ctx.message.author
        embed=discord.Embed(title=f'{member.name}\'s Avatar', url=member.avatar_url, color=random.randint(0, 0xffffff), timestamp=datetime.datetime.utcnow())
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(other(bot))
