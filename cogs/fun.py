import discord
import random
from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kill(self, ctx, *, member: discord.Member):
        phrases = [f'{member.name} died because his fartnite account with $1 of winnings was compromised',
                   f'{member.name} died because he crapped too hard after eating too many taco bell tacos', 
                   f'{member.name} tripped and fell on {ctx.author.name}\'s foot',
                   f'{member.name} forgot his discord password.',
                   f'{member.name} was sat on by obese {ctx.author.name}']
        randomPhrase = random.choice(phrases)
        await ctx.send(randomPhrase)


def setup(bot):
    bot.add_cog(fun(bot))
