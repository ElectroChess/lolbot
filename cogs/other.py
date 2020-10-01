import discord
import random
import datetime
from discord.ext import commands


class other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'i responded in `{round(self.bot.latency * 1000)}` milliseconds')

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            description='[**invite me pls**](https://tinyurl.com/lolbot-discordbot)', color=random.randint(0, 0xffffff))
        await ctx.send(embed=embed)

    @commands.command()
    async def discord(self, ctx):
        embed = discord.Embed(
            description='[**join my dev server pls**](https://tinyurl.com/lolbot-server)', color=random.randint(0, 0xffffff))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(other(bot))
