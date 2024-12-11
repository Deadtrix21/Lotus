from .common import *
from .utils import *


class Nightmarefever(AutoShardedBot):
    def __init__(self, command_prefix=set_prefix, intents=intents()):
        super().__init__(command_prefix, intents=intents)
        self.__setup__classes__()
        self.bot = self
    

    # Activates the base system of the bot
    def __setup__classes__(self):
        self.DBmanager = DBmanager()
        self.connected = self.DBmanager.connected


    # Loads in the loader cogs that loads all the other modules
    def __load__all__cogs__(self):
        self.__extend__bridge__slash__("loader", "core")


    # Event override: Load all cogs before bot launches reason:
    # (Slash commands)/(Bridge commands)
    async def on_connect(self):
        self.__load__all__cogs__();time.sleep(10)
        return await super().on_connect()


    # Get the datbase and connect to it
    def __get__config__(self):
        connected = self.connected
        if self.connected:
            entry = os.getenv("flavour")
            return connected["NightmareFever"]["Config"].find_one({"name":entry})["token"]
        else:
            return None


    # Load the cogs
    def __extend__bridge__slash__(self, name=None, path=None):
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

    # Boot up the bot
    def boot(self):
        self.bot.run(self.__get__config__())