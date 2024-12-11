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
        self.action_help = self.set_actions_cmd_help()


    async def snipe_ui(self, context_class):
        Embed = discord.Embed(
            title= f"Sniped",
            description="",
            color= 0x000c30
        )
        Embed.add_field(name=f"{context_class.author.name} said:", value=f"```\n{context_class.content}\n```")
        return Embed

    def set_actions_cmd_help(self):
        msg = "```\nCommand Options:"
        for i in Action_List:
            msg+= f"\n     {i}"
        msg += "```"
        return msg

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

    
    @bridge.bridge_command(name="8ball")
    @commands.guild_only()
    async def EightBall(self, ctx, *, asked):
        """Magic 8 ball

        Args:
            asked ([string]): the question
        """
        embeds = await EightBall(self.bot, ctx, asked)
        if isinstance(ctx, bridge.BridgeExtContext):
            await ctx.reply(embed=embeds.Embedded)
        elif isinstance(ctx, bridge.BridgeApplicationContext):
            await ctx.respond(embed=embeds.Embedded)
              

    @bridge.bridge_command()
    @discord.option(name="action", choices=Action_List)
    async def do(self, ctx:bridge.BridgeContext, action:str="None", member:discord.Member=None):
        """Anime Emotions: Actions required, Member sometimes
        """
        if isinstance(ctx, bridge.BridgeExtContext):
            if action == "None":
                await ctx.reply(self.action_help)
            elif action not in Action_List:
                await ctx.reply(self.action_help)
            else:
                Embed = await Actions(ctx, action, member)
                await ctx.send(embed=Embed.Embeded)
                try:
                   pass
                except Exception as E:
                    print(E)
                    await ctx.reply("that command needs a member mentioned", delete_after=10)
        elif isinstance(ctx, bridge.BridgeApplicationContext):
            try:
                Embed = await Actions(ctx, action, member)
                await ctx.respond(embed=Embed.Embeded)
            except Exception as E:
                print(E)
                await ctx.reply("that command needs a member mentioned", delete_after=10)
        if member != None: 
            await ctx.send(member.mention)
    
def setup(bot):
    c = Fun(bot)
    bot.add_cog(c)
