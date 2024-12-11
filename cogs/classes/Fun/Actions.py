import discord, os, random
from asyncinit import asyncinit
from waifu import WaifuClient, ImageCategories


@asyncinit
class Actions:
    async def __init__(self, action, ctx, string):
        self.waifu = WaifuClient()
        self.action = action
        self.context = ctx
        self.string = string
        self.User = ctx.author
        await self.send()
        
        
    async def get_thumbnail(self):
        return self.waifu.sfw(self.action)
        
    async def add_thumbnail(self, Embed:discord.Embed):
        Embed.set_image(url=await self.get_thumbnail())
    
    async def create_embed(self, Embed:discord.Embed=None):
        Embed = discord.Embed(
            title= f"{self.string}",
            description="",
            color= 0x000c30,
        )
        await self.add_thumbnail(Embed)
        return Embed
    
    async def send(self):
        Embed = await self.create_embed()
        await self.context.message.delete()
        await self.context.send(embed=Embed)
    