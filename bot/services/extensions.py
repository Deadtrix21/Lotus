from helpers.services.extension import *

Logger = specific_log(__name__)


def normalize_path(path: str) -> str:
    return os.path.normpath(path)


class BaseExtensionService:
    Initial = False

    def __init__(self, bot, config: ApplicationConfig):
        self.bot = bot
        self.extension = config.autoLoad.extensions
        self.listener = config.autoLoad.listeners
        self.tasks = config.autoLoad.tasks

    def load_extensions(self, folder_name: str):
        extensions_in_path = []
        folder_path = normalize_path(os.path.join(os.getcwd(), folder_name))
        for file in os.listdir(folder_path):
            extensions_in_path.append(f"{folder_name.replace('/', '.')}{file}")
        for extension in extensions_in_path:
            module_name = extension.split('.')[-1]
            self.load_one_extension(extension, folder_name, module_name)
        return

    def reload_extensions(self, folder_name: str):
        extensions_in_path = []
        folder_path = normalize_path(os.path.join(os.getcwd(), folder_name))
        for file in os.listdir(folder_path):
            extensions_in_path.append(f"{folder_name.replace(os.sep, '.')}.{file}")
        for extension in extensions_in_path:
            module_name = extension.split('.')[-1]
            self.reload_one_extension(extension, folder_name, module_name)
        return

    async def async_load_extensions(self, folder_name: str):
        return self.load_extensions(folder_name)

    async def async_reload_extensions(self, folder_name: str):
        return self.reload_extensions(folder_name)

    def reload_one_extension(self, extension: str = "", folder_name: str = "", name: str = ""):
        if name == "__pycache__":
            return
        try:
            self.bot.reload_extension(extension)
            Logger.info(f"{folder_name}: Reloaded {name}")
        except Exception as e:
            Logger.critical(e)

    def load_one_extension(self, extension: str = "", folder_name: str = "", name: str = ""):
        if name == "__pycache__":
            return
        try:
            self.bot.load_extension(extension)
            Logger.info(f"{folder_name}: Loaded {name}")
        except Exception as e:
            Logger.critical(e)


class ExtensionService(BaseExtensionService):

    def start_extension_loading(self):
        if self.Initial:
            self.reload_extensions(self.tasks)
        if not self.Initial:
            self.load_extensions(self.extension)
            self.load_extensions(self.listener)
            self.load_extensions(self.tasks)
        self.Initial = True

    async def async_start_extension_loading(self):
        if self.Initial:
            await self.async_reload_extensions(self.tasks)
        if not self.Initial:
            await self.async_load_extensions(self.extension)
            await self.async_load_extensions(self.listener)
            await self.async_load_extensions(self.tasks)
        self.Initial = True
