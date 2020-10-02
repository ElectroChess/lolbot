import discord
import random
import datetime
from discord.ext import commands
from discord import File
from PIL import Image, ImageDraw, ImageFont
import io
import urllib.request


class image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pfp', 'av', 'prfp'])
    async def avatar(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        show_avatar = discord.Embed(
            description="[Avatar URL](%s)" % member.avatar_url,
            timestamp=datetime.datetime.utcnow(),
            color=random.randint(0, 0xFFFFFF))
        show_avatar.set_image(url=f"{member.avatar_url}")
        show_avatar.set_footer(text=f'{member}')
        await ctx.send(embed=show_avatar)

    @commands.command()
    async def yotub(self, ctx):
        file = discord.File('images/YoTub.png', filename='YoTub.png')
        embed = discord.Embed(color=0xff0000, title='YoTub')
        embed.set_image(url='attachment://YoTub.png')
        await ctx.send(file=file, embed=embed)

    @commands.command(name='canvas')
    async def canvas(self, ctx, text=None):
        # read background image only once
        url = 'images/GRAdient.png'
        urlFile = File(url, filename='CanvasCard.png')
        urlFileFinal = 'attachment://CanvasCard.png'

        response = urllib.request.urlopen(urlFileFinal)
        # it doesn't need `io.Bytes` because it `response` has method `read()`
        background_image = Image.open(response)
        # add channel ALPHA to draw transparent rectangle
        background_image = background_image.convert('RGBA')
        AVATAR_SIZE = 128

        # --- duplicate image ----

        image = background_image.copy()

        image_width, image_height = image.size

        # --- draw on image ---

        # create object for drawing

        #draw = ImageDraw.Draw(image)

        # draw red rectangle with alpha channel on new image (with the same size as original image)

        rect_x0 = 20  # left marign
        rect_y0 = 20  # top marign

        rect_x1 = image_width - 20  # right margin
        rect_y1 = 20 + AVATAR_SIZE - 1  # top margin + size of avatar

        rect_width = rect_x1 - rect_x0
        rect_height = rect_y1 - rect_y0

        rectangle_image = Image.new('RGBA', (image_width, image_height))
        rectangle_draw = ImageDraw.Draw(rectangle_image)

        rectangle_draw.rectangle(
            (rect_x0, rect_y0, rect_x1, rect_y1), fill=(0, 255, 0, 0))

        # put rectangle on original image

        image = Image.alpha_composite(image, rectangle_image)

        # create object for drawing

        # create new object for drawing after changing original `image`
        draw = ImageDraw.Draw(image)

        # draw text in center

        text = f'Hello {ctx.author.name}'

        font = ImageFont.truetype('Arial.ttf', 30)

        text_width, text_height = draw.textsize(text, font=font)
        # skip avatar when center text
        x = (rect_width - text_width - AVATAR_SIZE)//2
        y = (rect_height - text_height)//2

        x += rect_x0 + AVATAR_SIZE     # skip avatar when center text
        y += rect_y0

        draw.text((x, y), text, fill=(0, 0, 255, 255), font=font)

        # --- avatar ---

        # get URL to avatar
        # sometimes `size=` doesn't gives me image in expected size so later I use `resize()`
        avatar_asset = ctx.author.avatar_url_as(format='jpg', size=AVATAR_SIZE)

        # read JPG from server to buffer (file-like object)
        buffer_avatar = io.BytesIO(await avatar_asset.read())

    #    buffer_avatar = io.BytesIO()
    #    await avatar_asset.save(buffer_avatar)
    #    buffer_avatar.seek(0)

        # read JPG from buffer to Image
        avatar_image = Image.open(buffer_avatar)

        # resize it
        avatar_image = avatar_image.resize((AVATAR_SIZE, AVATAR_SIZE))

        circle_image = Image.new('L', (AVATAR_SIZE, AVATAR_SIZE))
        circle_draw = ImageDraw.Draw(circle_image)
        circle_draw.ellipse((0, 0, AVATAR_SIZE, AVATAR_SIZE), fill=255)
        # avatar_image.putalpha(circle_image)
        # avatar_image.show()

        image.paste(avatar_image, (rect_x0, rect_y0), circle_image)

        # --- sending image ---

        # create buffer
        buffer_output = io.BytesIO()

        # save PNG in buffer
        image.save(buffer_output, format='PNG')

        # move to beginning of buffer so `send()` it will read from beginning
        buffer_output.seek(0)

        # send image
        await ctx.send(file=File(buffer_output, 'myimage.png'))


def setup(bot):
    bot.add_cog(image(bot))
