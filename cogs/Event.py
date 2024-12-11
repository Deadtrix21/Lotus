
from discord.ext import commands
import discord
from .classes.Events import TTS

class Snipe():
    class SnipeSchema():
        def __init__(self, ctx) -> None:
            self.author = ctx.author
            self.content = ctx.content

        def __repr__(self) -> str:
            return f"<{self.author}>   <{self.content}>"

    def __init__(self) -> None:
        self.message = [0,1,2] 
    
    def remove_one(self):
        if len(self.message) > 3:
            self.message.pop(0)

    def add_one(self, msg):
        self.remove_one()
        self.message.append(self.SnipeSchema(msg))

    def latest_get_snipe(self):
        value = len(self.message)-1
        return self.message[value]


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.snipe_guilds = self.snipe_guilds = {}



    async def add_snipe(self, ctx):
        try:
            if self.snipe_guilds[ctx.guild.id]:
                pass
        except KeyError:
            self.snipe_guilds[ctx.guild.id] = Snipe()
        return self.snipe_guilds[ctx.guild.id]




    async def tts(self, ctx):
        string = ctx.content.replace(";;", "")
        if len(string) <= 60:
            data = TTS.__data__(self.bot, ctx, string)
            await TTS.TTS(data)
        else:
            await ctx.send.channel("I can only read 60 charaters at a time ")
        return
    
    async def on_join_leave(self, guild, title:str):
        embed = None
        if title == "join":
            embed = discord.Embed(title=':white_check_mark: {Name}', type='rich', color=0x2ecc71)
        else:
            embed = discord.Embed(title=f':x: {guild.name}', type='rich', color=0xff0000)
        try:
            embed.set_thumbnail(url=guild.icon)
        except Exception:
            pass
        embed.add_field(name='Name', value=guild.name, inline=True)
        embed.add_field(name='ID', value=guild.id, inline=True)
        embed.add_field(name='Owner', value=f'{guild.owner}', inline=True)
        embed.add_field(name='Region', value=guild.region, inline=True)
        embed.add_field(name='Members', value=guild.member_count, inline=True)
        embed.add_field(name='Created at', value=guild.created_at, inline=True)
        channel = self.bot.get_channel(948139119723298846)
        await channel.send(embed=embed)
        return
    
    async def check_user(self, ctx):
        pass
    
    @commands.Cog.listener()
    async def on_message_delete(self, ctx):
        if ctx.author == self.bot.user:
            return
        snipe : Snipe = await self.add_snipe(ctx)
        snipe.add_one(ctx)

    @commands.Cog.listener()
    async def on_message(self, ctx):
        await self.check_user(ctx)
        if ctx.author == self.bot.user:
            return
        
        if ctx.content.startswith(";;"):
            await self.tts(ctx)
        return
        
    @commands.Cog.listener()		
    async def on_member_join(self, member):
        pass
    
    @commands.Cog.listener()		
    async def on_guild_join(self, guild):
        await self.on_join_leave(guild, "join")
        return
    
    @commands.Cog.listener()		
    async def on_guild_leave(self, guild):
        await self.on_join_leave(guild, "leave")
        return
    

def setup(bot):
    c = Event(bot)
    bot.add_cog(c)