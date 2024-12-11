import asyncio
from datetime import timedelta
import arrow
import discord
import random
from discord.ext import commands


class Status(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.time = None
        self.get_startup_time()
    
    def get_startup_time(self) -> timedelta:
        if self.time == None:
            self.time = arrow.utcnow()
    
    def UPTIME(self):
        now                     = arrow.get(arrow.utcnow())
        utc                     = arrow.get(self.time)
        core                    = now-utc
        seconds                 = core.total_seconds()
        minutes,    seconds     = divmod(seconds, 60)
        hour,       minutes     = divmod(minutes , 60)
        hour                    = round(hour)
        minute                  = round(minutes)
        second                  = round(seconds)
        return f"for {hour} hours {minute} minutes {second}  seconds"
    
    def random(self):
        statusswitch = {
            1:Status.UPTIME(self),
            2:f'{len(self.bot.guilds)} Servers',
            }
        return statusswitch[random.randint(1,2)]
    
    async def task(self):
        while True:
            object_type = discord.ActivityType.streaming
            object_activity = (
                discord.Activity(
                    type=object_type,
                    name=Status.random(self), 
                    url="https://www.twitch.tv/DeadTrix0")
                )
            await self.bot.change_presence(status=object_activity, activity=object_activity)
            await asyncio.sleep(5)
    
def setup(bot):
    n = Status(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(n.task())
    bot.add_cog(n)
