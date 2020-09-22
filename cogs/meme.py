import discord
import aiohttp
import random
import datetime
from discord.ext import commands

class meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/hot.json?sort=new') as r:
                res = await r.json()
                ran = random.randint(0, 25)
                imgurl = res['data']['children'][ran]['data']['url']
                upvotes = res['data']['children'][ran]['data']['ups']
                title = res['data']['children'][ran]['data']['title']
                commments = res['data']['children'][ran]['data'][
                    'num_comments']
                memeurl = res['data']['children'][ran]['data']['permalink']
                awards = res['data']['children'][ran]['data'][
                    'total_awards_received']
                author = res['data']['children'][ran]['data']['author']
                embed = discord.Embed(
                    title=f"{title}",
                    url=f'https://reddit.com{memeurl}',
                    timestamp=datetime.datetime.utcnow(),
                    color=random.randint(0, 0xFFFFFF))
                embed.set_image(url=imgurl)
                embed.set_author(
                    name=author, url=f'https://reddit.com/u/{author}')
                embed.set_footer(
                    text=f"👍 {upvotes} | 💬 {commments} | 🏆 {awards}")
                await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def cleanmeme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/cleanmemes/hot.json?sort=new'
            ) as r:
                res = await r.json()
                ran = random.randint(0, 25)
                imageurl = res['data']['children'][ran]['data']['url']
                upvotes = res['data']['children'][ran]['data']['ups']
                title = res['data']['children'][ran]['data']['title']
                commments = res['data']['children'][ran]['data'][
                    'num_comments']
                memeurl = res['data']['children'][ran]['data']['permalink']
                awards = res['data']['children'][ran]['data'][
                    'total_awards_received']
                author = res['data']['children'][ran]['data']['author']
                embed = discord.Embed(
                    title=f"{title}",
                    url=f'https://reddit.com{memeurl}',
                    timestamp=datetime.datetime.utcnow(),
                    color=random.randint(0, 0xFFFFFF))
                embed.set_author(
                    name=author, url=f'https://reddit.com/u/{author}')
                embed.set_image(url=imageurl)
                embed.set_footer(
                    text=f"👍 {upvotes} | 💬 {commments} | 🏆 {awards}")
                await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def dankmeme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/dankmemes/hot.json?sort=new'
            ) as r:
                res = await r.json()
                ran = random.randint(0, 25)
                imgurl = res['data']['children'][ran]['data']['url']
                upvotes = res['data']['children'][ran]['data']['ups']
                title = res['data']['children'][ran]['data']['title']
                commments = res['data']['children'][ran]['data'][
                    'num_comments']
                memeurl = res['data']['children'][ran]['data']['permalink']
                author = res['data']['children'][ran]['data']['author']
                awards = res['data']['children'][ran]['data'][
                    'total_awards_received']
                embed = discord.Embed(
                    title=f"{title}",
                    url=f'https://reddit.com{memeurl}',
                    timestamp=datetime.datetime.utcnow(),
                    color=random.randint(0, 0xFFFFFF))
                embed.set_image(url=imgurl)
                embed.set_author(
                    name=author, url=f'https://reddit.com/u/{author}')
                embed.set_footer(
                    text=f"👍 {upvotes} | 💬 {commments} | 🏆 {awards}")
                await ctx.send(embed=embed)  

    @commands.command(pass_context=True)
    async def discordmeme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/Discordmemes/hot.json?sort=new'
            ) as r:
                res = await r.json()
                ran = random.randint(0, 25)
                imgurl = res['data']['children'][ran]['data']['url']
                upvotes = res['data']['children'][ran]['data']['ups']
                title = res['data']['children'][ran]['data']['title']
                commments = res['data']['children'][ran]['data'][
                    'num_comments']
                memeurl = res['data']['children'][ran]['data']['permalink']
                author = res['data']['children'][ran]['data']['author']
                awards = res['data']['children'][ran]['data'][
                    'total_awards_received']
                embed = discord.Embed(
                    title=f"{title}",
                    url=f'https://reddit.com{memeurl}',
                    timestamp=datetime.datetime.utcnow(),
                    color=random.randint(0, 0xFFFFFF))
                embed.set_image(url=imgurl)
                embed.set_author(
                    name=author, url=f'https://reddit.com/u/{author}')
                embed.set_footer(
                    text=f"👍 {upvotes} | 💬 {commments} | 🏆 {awards}")
                await ctx.send(embed=embed)  


def setup(bot):
    bot.add_cog(meme(bot))
