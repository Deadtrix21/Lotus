from discord.ext import commands
from discord.ext import bridge
import asyncio
import discord
from .classes.Fun import Wanted, EightBall, Actions
from .Event import Snipe

Action_List = [ 
            'bully', 'cuddle', 'cry', 'hug',
            'kiss', 'lick', 'pat', 'smug', 'bonk', 
            'yeet', 'blush', 'smile', 'wave', 'highfive', 
            'handhold', 'nom', 'bite', 'slap', 
            'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe'
        ]


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def snipe_ui(self, context_class):
        Embed = discord.Embed(
            title= f"Sniped",
            description="",
            color= 0x000c30
        )
        Embed.add_field(name=f"{context_class.author.name} said:", value=f"```\n{context_class.content}\n```")
        return Embed

    @commands.command()
    @commands.guild_only()
    async def snipe(self, ctx, value:int=None):
        try:
            self.bot.snipe_guilds[ctx.guild.id]
            sniped : Snipe = self.bot.snipe_guilds[ctx.guild.id].latest_get_snipe()
            await ctx.send(embed=await self.snipe_ui(sniped))

        except KeyError:
            await ctx.send("Nothing to snipe", delete_after=10)
            


    @commands.command()
    @commands.guild_only()
    async def wanted(self, ctx, user: discord.Member = None):
        await Wanted(self.bot, ctx, user)
    
    
    @commands.command()
    @commands.guild_only()
    async def AnimeWaifu(self, ctx, *, argument):
        """
            
        """
        await ctx.send(self.waifu.sfw(argument))
    
    @commands.group(aliases=["action", "act"])
    @commands.guild_only()
    async def actions(self, ctx):
        list = [ 
            'bully', 'cuddle', 'cry', 'hug',
            'kiss', 'lick', 'pat', 'smug', 'bonk', 
            'yeet', 'blush', 'smile', 'wave', 'highfive', 
            'handhold', 'nom', 'bite', 'slap', 
            'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe'
        ]
        msg = "```\nCommand Options:"
        if ctx.invoked_subcommand is None:
            for i in list:
                msg+= f"\n     {i}"
            msg += "```"
            await ctx.send(msg)


    @commands.command(name="8ball")
    @commands.guild_only()
    async def eight_ball(self, ctx, *, asked):
        """Magic 8 ball

        Args:
            asked ([string]): the question
        """
        await EightBall(self.bot, ctx, asked)
    
    @actions.command()
    async def bully(self, ctx, User:discord.Member = None):
        await Actions("bully", ctx, f"{ctx.author.name} bullies {User.name}")
                    
    @actions.command()
    async def cuddle(self, ctx, User:discord.Member = None):
        await Actions("cuddle", ctx, f"{ctx.author.name} cuddles with {User.name}")
                    
    @actions.command()
    async def cry(self, ctx, User:discord.Member = None):
        await Actions("cry", ctx, f"{ctx.author.name} is crying....")
                    
    @actions.command()
    async def hug(self, ctx, User:discord.Member = None):
        await Actions("hug", ctx, f"{ctx.author.name} hugs {User.name}")
                    
    @actions.command()
    async def kiss(self, ctx, User:discord.Member = None):
        await Actions("kiss", ctx, f"{ctx.author.name} kisses {User.name}")
                    
    @actions.command()
    async def lick(self, ctx, User:discord.Member = None):
        await Actions("lick", ctx, f"{ctx.author.name} is licking {User.name}")
                    
    @actions.command()
    async def pat(self, ctx, User:discord.Member = None):
        await Actions("pat", ctx, f"{ctx.author.name} pats {User.name}")
                    
    @actions.command()
    async def smug(self, ctx, User:discord.Member = None):
        await Actions("smug", ctx, f"{ctx.author.name} is acting smug.....")
                    
    @actions.command()
    async def bonk(self, ctx, User:discord.Member = None):
        await Actions("bonk", ctx, f"{ctx.author.name} bonks {User.name}")
                    
    @actions.command()
    async def yeet(self, ctx, User:discord.Member = None):
        await Actions("yeet", ctx, f"{ctx.author.name} yeets {User.name}")
                    
    @actions.command()
    async def blush(self, ctx, User:discord.Member = None):
        await Actions("blush", ctx, f"{ctx.author.name} is blushing.....")
                    
    @actions.command()
    async def smile(self, ctx, User:discord.Member = None):
        await Actions("smile", ctx, f"{ctx.author.name} is smiling")
                    
    @actions.command()
    async def wave(self, ctx, User:discord.Member = None):
        await Actions("wave", ctx, f"{ctx.author.name} waves at {User.name}")
                    
    @actions.command()
    async def highfive(self, ctx, User:discord.Member = None):
        await Actions("highfive", ctx, f"{ctx.author.name} gives a highfive to {User.name}")
                    
    @actions.command()
    async def handhold(self, ctx, User:discord.Member = None):
        await Actions("handhold", ctx, f"{ctx.author.name} holds {User.name}'s hands ")
                    
    @actions.command()
    async def nom(self, ctx, User:discord.Member = None):
        await Actions("nom", ctx, f"{ctx.author.name} noms on {User.name}")
                    
    @actions.command()
    async def bite(self, ctx, User:discord.Member = None):
        await Actions("bite", ctx, f"{ctx.author.name} bites {User.name}")
                                       
    @actions.command()
    async def slap(self, ctx, User:discord.Member = None):
        await Actions("slap", ctx, f"{ctx.author.name} slaps {User.name}")           

    @actions.command()
    async def kill(self, ctx, User:discord.Member = None):
        await Actions("kill", ctx, f"{ctx.author.name} kills {User.name}")
                    
    @actions.command()
    async def kick(self, ctx, User:discord.Member = None):
        await Actions("kick", ctx, f"{ctx.author.name} kicks {User.name}")
                    

    @actions.command()
    async def happy(self, ctx, User:discord.Member = None):
        await Actions("happy", ctx, f"{ctx.author.name} seems happy.....")
                    

    @actions.command()
    async def wink(self, ctx, User:discord.Member = None):
        await Actions("wink", ctx, f"{ctx.author.name} winks at {User.name}")
                    

    @actions.command()
    async def poke(self, ctx, User:discord.Member = None):
        await Actions("poke", ctx, f"{ctx.author.name} pokes {User.name}")
                    

    @actions.command()
    async def dance(self, ctx, User:discord.Member = None):
        await Actions("dance", ctx, f"{ctx.author.name} is dancing")
                    

    @actions.command()
    async def cringe(self, ctx, User:discord.Member = None):
        await Actions("cringe", ctx, f"{ctx.author.name} cringes {User.name}")
              
    def get_actions():
        return [c for c in Action_List]

    @bridge.bridge_command()
    @discord.option(name="seconds", choices=range(1, 11))
    async def wait(self, ctx, seconds: int = 5):
        await ctx.defer()
        await asyncio.sleep(seconds)
        await ctx.respond(f"Waited for {seconds} seconds!")
        
    @bridge.bridge_command()
    @discord.option(name="action", choices= get_actions())
    async def do(self, ctx, action:str="None"):
        await ctx.respond(action)
    
def setup(bot):
    
    c = Fun(bot)
    bot.add_cog(c)