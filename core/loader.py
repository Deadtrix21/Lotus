from . import Nightmarefever
from .common import *


class StartCore(Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot : Nightmarefever = bot
        self.load_core_programs()
          
    
    def load_core_programs(self):
        self.bot.__extend__bridge__slash__(name="jishaku", path=None)
        self.bot.__extend__bridge__slash__(name="Status", path="cogs")
        self.bot.__extend__bridge__slash__(name="Test", path="cogs")
        self.bot.__extend__bridge__slash__(name="Admin", path="cogs")
        self.bot.__extend__bridge__slash__(name="Economy", path="cogs")
        self.bot.__extend__bridge__slash__(name="Event", path="cogs")
        self.bot.__extend__bridge__slash__(name="Fun", path="cogs")
        self.bot.__extend__bridge__slash__(name="Music", path="cogs")
        self.bot.__extend__bridge__slash__(name="OnReady", path="cogs")


def setup(bot):
    c = StartCore(bot)
    bot.add_cog(c)

