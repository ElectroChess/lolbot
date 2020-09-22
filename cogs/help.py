import discord
import random
import datetime
from discord.ext import commands

class helpcmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title='lolbot Commands', color=random.randint(0, 0xffffff), timestamp=datetime.datetime.utcnow())
        embed.add_field(name='Meme Commands', value='`lol meme`, `lol cleanmeme`, `lol dankmeme`, `lol discordmeme`', inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(helpcmd(bot))
