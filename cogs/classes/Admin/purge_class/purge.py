import discord
from typing import Optional
from asyncinit import asyncinit



@asyncinit
class Purge:
    async def __init__(
            self, 
            bot, 
            ctx,
            opt:Optional[str],
            amount:Optional[int]):
        self.bot    = bot
        self.ctx    = ctx
        self.amount = amount
        self.opt = opt
        await self.chose()
        
    @asyncinit
    class normal:
        async def __init__(self, bot, ctx, amount:Optional[int]):
            self.bot    = bot
            self.ctx    = ctx
            self.amount = amount
            await self.start_purger()
            
        async def start_purger(self):
            await self.ctx.channel.purge(limit=self.amount)
    
    @asyncinit
    class channel:
        async def __init__(self, bot, ctx, amount:Optional[int]):
            self.bot    = bot
            self.ctx    = ctx
            self.amount = amount
            await self.start_purger()

        async def start_purger(self):
            await self.ctx.channel.purge(limit=self.amount)
    
    async def numberLogic(self, amount, option):
        if amount == None:
                amount = 10
        if option == "c":
            if amount <= 100:
                amount = 100
        if option == "n":
            if amount >= 100:
                amount = 100
            if amount <= 0:
                amount = 10
        self.amount = amount
        
    async def messageDisplay(self, ctx, opt, amount):
        if opt == "c":
            await self.ctx.send(f"I purged the channel by {amount}",delete_after=15)
        elif opt == "n":
            await self.ctx.send(f"I deleted {amount} messages",delete_after=15)
        else:
            await self.ctx.send("I purged the channel by 20, but please try `help purge`",delete_after=15)
            
    async def chose(self):
        await self.numberLogic(self.amount, self.opt)
        if self.opt == "c":
            await self.channel(self.bot, self.ctx, self.amount)
        elif self.opt == "n":
            await self.normal(self.bot, self.ctx, self.amount)
        else:
            await self.normal(self.bot, self.ctx, 20)
        await self.messageDisplay(self.ctx, self.opt, self.amount)