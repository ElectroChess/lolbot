import discord
import aiohttp
import random
import datetime
from discord.ext import commands

class joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cleanjoke(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/cleanjokes/hot.json?sort=new'
            ) as r:
                res = await r.json()
                ran = random.randint(0, 25)
                upvotes = res['data']['children'][ran]['data']['ups']
                author = res['data']['children'][ran]['data']['author']
                title = res['data']['children'][ran]['data']['title']
                commments = res['data']['children'][ran]['data'][
                    'num_comments']
                memeurl = res['data']['children'][ran]['data']['permalink']
                awards = res['data']['children'][ran]['data'][
                    'total_awards_received']
                text = res['data']['children'][ran]['data']['selftext']
                embed = discord.Embed(
                    title=f"{title}",
                    url=f'https://reddit.com{memeurl}',
                    timestamp=datetime.datetime.utcnow(),
                    color=random.randint(0, 0xFFFFFF),
                    description=f'{text}')
                embed.set_author(
                    name=author, url=f'https://reddit.com/u/{author}')
                embed.set_footer(
                    text=f"👍 {upvotes} | 💬 {commments} | 🏆 {awards}")
                await ctx.send(embed=embed)

    @commands.command()
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/jokes/hot.json?sort=new') as r:
                res = await r.json()
                ran = random.randint(0, 25)
                upvotes = res['data']['children'][ran]['data']['ups']
                author = res['data']['children'][ran]['data']['author']
                title = res['data']['children'][ran]['data']['title']
                commments = res['data']['children'][ran]['data'][
                    'num_comments']
                memeurl = res['data']['children'][ran]['data']['permalink']
                awards = res['data']['children'][ran]['data'][
                    'total_awards_received']
                text = res['data']['children'][ran]['data']['selftext']
                embed = discord.Embed(
                    title=f"{title}",
                    url=f'https://reddit.com{memeurl}',
                    timestamp=datetime.datetime.utcnow(),
                    color=random.randint(0, 0xFFFFFF),
                    description=f'{text}')
                embed.set_footer(
                    text=f"👍 {upvotes} | 💬 {commments} | 🏆 {awards}")
                embed.set_author(
                    name=author, url=f'https://reddit.com/u/{author}')
                await ctx.send(embed=embed)

    

def setup(bot):
    bot.add_cog(joke(bot))
