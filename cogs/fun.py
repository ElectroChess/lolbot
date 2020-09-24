import discord
import random
import asyncio
from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kill(self, ctx, *, member: discord.Member):
        phrases = [f'{member.name} died because their fartnite account with $1 of winnings was compromised',
                   f'{member.name} died because they crapped too hard after eating too many taco bell tacos', 
                   f'{member.name} tripped and fell on {ctx.author.name}\'s foot',
                   f'{member.name} forgot their discord password.',
                   f'{member.name} was sat on by obese {ctx.author.name}',
                   f'{ctx.author.name} dropped a VGA TV on {member.name}']
        randomPhrase = random.choice(phrases)
        await ctx.send(randomPhrase)
    
    @commands.command()
    async def hack(self, ctx, member:discord.Member):
        creditcardnumber = member.id
        discrim = member.discriminator
        randomMessages = random.choice(['lol', 'bruh', 'i like cheese', 'sup', 'yooooooo', 'hi', 'https://tinyurl.com/vxrpbot'])
        randomEmojis = random.choice(['👨‍🎤', '🙎‍♂️','🧚‍♀️','🏃‍♂️','🤳','✋','🙌','👎','👌','🤩','🙄','☺','😑','😣','😩'])
        msg = await ctx.send(f'Starting hack on {member.name}')
        await asyncio.sleep(3)
        await msg.edit(content='Getting credit card number...\n- ')
        await asyncio.sleep(1)
        await msg.edit(content=f'Getting credit card number...\n- `{creditcardnumber}`')
        await asyncio.sleep(3)
        await msg.edit(content=f'Getting the number on the back...\n- ')
        await asyncio.sleep(1)
        await msg.edit(content=f'Getting the number on the back...\n- `{discrim}`')
        await asyncio.sleep(3)
        await msg.edit(content=f'Getting {member.name}\'s last sent message...\n- ')
        await asyncio.sleep(1)
        await msg.edit(content=f'Getting {member.name}\'s last sent message...\n- {randomMessages}')
        await asyncio.sleep(3)
        await msg.edit(content=f'Getting {member.name}\'s last sent emoji...\n- ')
        await asyncio.sleep(1)
        await msg.edit(content=f'Getting {member.name}\'s last sent emoji...\n- {randomEmojis}')
        await asyncio.sleep(3)
        await msg.edit(content=f'Reporting {member.name} to Discord for violating the ToS...')
        await asyncio.sleep(2)
        await msg.edit(content=f'Selling the info to the government...')
        await asyncio.sleep(2)
        await msg.delete()
        await ctx.send(f'The real hack on {member.name} is complete!')



def setup(bot):
    bot.add_cog(fun(bot))
