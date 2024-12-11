from .utils.Helper import Cog
from .main import NightmareFever
import asyncio


class StartCore(Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot : NightmareFever = bot
        
    
    async def load_core_programs(self):
        await self.bot.extend_modules(name="jishaku", path=None)
        await self.bot.extend_modules(name="Status", path="core")
        await self.bot.extend_modules(name="TogetherActivities", path="cogs")
        await self.bot.extend_modules(name="Admin", path="cogs")
        await self.bot.extend_modules(name="Fun", path="cogs")
        await self.bot.extend_modules(name="Event", path="cogs")
        await self.bot.extend_modules(name="Music", path="cogs")
        await self.bot.extend_modules(name="Economy", path="cogs")
        await self.bot.extend_modules(name="ErrorHandle", path="cogs")

def setup(bot):
    c = StartCore(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(c.load_core_programs())
    bot.add_cog(c)

