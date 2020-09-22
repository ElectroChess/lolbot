import discord
from discord.ext import commands

class helpcmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title='lolbot Commands')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(helpcmd(bot))
