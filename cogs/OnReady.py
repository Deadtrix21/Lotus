from .common import *

class OnReady(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("starting")

def setup(bot):
    cog = OnReady(bot)
    bot.add_cog(cog)
