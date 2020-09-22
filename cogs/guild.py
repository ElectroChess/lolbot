import discord
import random
import datetime
from discord.ext import commands

class guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        global memberChannel
        homeChannel = self.bot.get_channel(754883409398071413)
        memberChannel = self.bot.get_channel(757784687648178316)
        await memberChannel.edit(name=f'{len(self.bot.guilds)} Servers')
        embed = discord.Embed(
            title=f'I was added :)',
            color=random.randint(0, 0xFFFFFF),
            timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(
            name=f'Added to `{guild.name}`',
            value=f'Member Count: `{guild.member_count}`')
        embed.add_field(name='Server Owner:', value=f'`{guild.owner}`')
        embed.set_footer(text=f'lolbot Now Serves {len(self.bot.users)} Users')
        await homeChannel.send(embed=embed)
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send('sup nerds\nso i have **3** prefixes.\nthe prefixes are `<@!757743672379834448>`, `lol` and `lol `. any of them will work.\njust do `lol help` for commands.')
            break

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        homeChannel = self.bot.get_channel(754883409398071414)
        await memberChannel.edit(name=f'{len(self.bot.guilds)} Servers')
        embed = discord.Embed(
            title=f'I was added :)',
            color=random.randint(0, 0xFFFFFF),
            timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(
            name=f'Added to `{guild.name}`',
            value=f'Member Count: `{guild.member_count}`')
        embed.add_field(name='Server Owner:', value=f'`{guild.owner}`')
        embed.set_footer(text=f'lolbot Now Serves {len(self.bot.users)} Users')
        await homeChannel.send(embed=embed)
    
def setup(bot):
    bot.add_cog(guild(bot))
