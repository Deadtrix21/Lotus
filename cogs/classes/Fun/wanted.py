from asyncinit import asyncinit
from PIL import Image, ImageDraw
from io import BytesIO
import discord, os

@asyncinit
class Wanted:
    async def __init__(self, bot, ctx, User:discord.Member = None):
        self.bot = bot
        self.context = ctx
        self.User = ctx.author if not User else User
        await self.__send()
    
    async def __get_user_avatar(self):
        pfp = self.User.display_avatar.with_format("jpg")
        pfp = Image.open( \
            BytesIO(await pfp.read())           
        )
        pfp = pfp.resize((252, 252))
        return pfp
    
    async def __get_wanted(self):
        wanted = Image.open("assets/img//wanted.jpg")
        wanted.paste(await self.__get_user_avatar(), (106, 247))
        wanted.save("profile.jpg")
        return wanted
    
    async def __send(self):
        try:
            await self.__get_wanted()
            await self.context.send(file=discord.File("profile.jpg"))
            os.remove("profile.jpg")
        except Exception as e:
            await self.context.send("Sorry Something Went Wrong")
            print(e)