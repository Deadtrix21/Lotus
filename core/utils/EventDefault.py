from discord.ext import commands
from discord_together import DiscordTogether
import discord


class DefaultEventManager:
    def __init__(self, bot) -> None:
        self.bot = bot
        self.core_loaded = False

    async def on_ready(self):
        if self.core_loaded == False:
            print(f"{'-'*50}")
            print(f"{'-'*18} Core Online {'-'*19}")
            print(f"{'-'*50}")
            await self.bot.extend_modules(name="Loader", path="core")
            self.core_loaded = True
        else:
            print(f"{'-'*50}")
            print(f"{'-'*18} Reboot {'-'*19}")
            print(f"{'-'*50}")
    
    async def __discord__together__(self):
        self.bot.togetherControl = await DiscordTogether(self.bot.get__config__(), debug=True)