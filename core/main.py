from .utils.Helper import (AutoShardedBot, ExtentionError, intents, set_prefix)
from .utils.EventDefault import DefaultEventManager
from .utils.Database import database_handler as DBManager
import os


class NightmareFever(AutoShardedBot):
    def __init__(self, command_prefix=set_prefix, intents=intents()):
        super().__init__(command_prefix, intents=intents)
        self.__setup__classes()
        self.bot = self
        return None
    
    def __setup__classes(self):
        self.EventManager = DefaultEventManager(bot=self)
        self.DBManager = DBManager()
        self.connected = self.DBManager.connected

    async def __setup__(self):
        await self.EventManager.on_ready()
        await self.EventManager.__discord__together__()


    async def on_ready(self):
        await self.__setup__()



    def get__config__(self):
        connected = self.connected
        if self.connected:
            entry = os.getenv("flavour")
            return connected["NightmareFever"]["Config"].find_one({"name":entry})["token"]
        else:
            return None



    async def extend_modules(self, name=None, path=None) -> object:
        if name is None:
            raise ExtentionError("No Extention name given")
        else:
            try:
                if path == None:
                    self.bot.load_extension(f"{name}")
                else:
                    self.bot.load_extension(f"{path}.{name}")
                return print(f"Green {name}")
            except Exception as E:
                print(f"Error in {name}:\n{E}")
        return
    

    def boot(self):
        self.bot.run(self.get__config__())
