import discord
import random
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def kill(self, ctx, *, member: discord.Member):
        phrases = ['died because his fartnite account with $1 of winnings was compromised']
        memberSpace = f'{member.name} '
        randomPhrase = random.choice(phrases)
        await ctx.send(f'{memberSpace}{randomPhrase}')



def setup(bot):
    bot.add_cog(fun(bot))
