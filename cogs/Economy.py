import discord, random
from discord.ext import commands, bridge
from numpy.random import choice
from .models import Manager

class Economy(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.database = self.bot.connected
        self.Manager = Manager(self.database)

    def staff_perms(user_level:str):
        async def predicate(ctx:bridge.BridgeExtContext):
            manager = Manager(ctx.bot.connected)
            user = await manager.get_staff_level(ctx=ctx)
            if user.enable:
                if user.category >= await manager.determine_staff_level(user_level):
                    del manager
                    return True
                else:
                    del manager
                    return False
            else:
                del manager
                return False
        return commands.check(predicate)
        

    async def dig_values(self):
         items = random.randrange(0,300),random.randrange(300,500),random.randrange(500,700),random.randrange(700, 1200) 
         probabilities = [0.5,0.35,0.1,0.05] 
         return choice(items,p=probabilities)

    @commands.command()
    async def register(self, ctx):
        """Register for Economy
        """
        await self.Manager.error_if_registed(ctx)
        await self.Manager.create_account(ctx)
        return await ctx.author.send("Welcome to the game")


    @commands.command(aliases=["balance", "bal"])
    async def money(self, ctx, Member:discord.Member=None):
        """ Look at your balance
        """
        Member = ctx.author if Member == None else Member
        await self.Manager.error_non_registed(ctx, Member)
        await self.Manager.view_money(ctx, Member)


    @commands.command()
    @commands.cooldown(1, 35, commands.BucketType.user)
    async def dig(self, ctx):
        """ Dig for loot
        """
        Member = ctx.author
        await self.Manager.error_non_registed(ctx, Member)
        await self.Manager.add_money_auto(ctx, await self.dig_values(), random.randrange(1,10))


    @commands.command(aliases=["give"])
    @commands.cooldown(1, 25, commands.BucketType.user)
    async def pay(self, ctx, value:int, Member:discord.Member):
        """ Pay or Give people money
        """
        await self.Manager.error_non_registed(ctx, Member)
        await self.Manager.transfer_money(ctx, Member, value)

    @commands.command(hidden=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def lick(self, ctx , member:discord.Member):
        """(Hidden) Steal from a person
        """
        await ctx.message.delete();
        res = await self.Manager.steal(ctx, member)
        
        

    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def work(self, ctx):
        pass

    @commands.command(aliases=["dep"])
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def deposit(self, ctx, amount):
        """Deposit money into the bank
        """
        await self.Manager.bank_money(ctx, amount)

    @commands.command(aliases=["with"])
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def withdraw(self, ctx, amount):
        """Withdraw money from the bank
        """
        await self.Manager.withdraw_money(ctx, amount)

#Admin Commands
    @commands.command()
    @commands.is_owner()
    async def admingive(self, ctx, value:int, Member:discord.Member=None):
        Member = ctx.author if Member == None else Member
        await self.Manager.add_money_admin(ctx, Member, value)




    @commands.group(aliases=["Console"])
    @staff_perms("Mod")
    async def EconomyConsole(self, ctx):
        """The economy console(Staff Only)
        """
        await ctx.respond("Hello there, if u can see this you are a staff member")

    @EconomyConsole.command(name="stafflvl")
    @staff_perms("Owner")
    async def staff_level(self, ctx, member:discord.Member, lvl=None):
        """Change the staff's job lvl
        """
        if lvl == None:
            await ctx.respond("You for got to assign the job level")
        else:
            await self.Manager.set_staff_level(member=member, lvl=lvl)
            await ctx.respond(f"Done setting {member.mentio} to {lvl}")

    @EconomyConsole.command(name="give")
    @staff_perms("Admin")
    async def admingive(self, ctx, value:int, Member:discord.Member=None):
        """You can give someone money from the infinite pool
        """
        Member = ctx.author if Member == None else Member
        await self.Manager.add_money_admin(ctx, Member, value)

    @EconomyConsole.command()
    @staff_perms("Admin")
    async def addstaff(self, ctx, Member:discord.Member):
        """Gives a user staff
        """
        await self.Manager.add_to_staff(Member)
        await ctx.send(f"{Member.mention} was added to staff")


def setup(bot):
    cog1 = Economy(bot)
    bot.add_cog(cog1)
