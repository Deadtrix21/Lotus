from dependency_injector.wiring import inject, Provide
from mafic import NodePool

from containers import ApplicationContainer
from containers import LogSpecificFile
from containers.configs.DiscordConfigs import LavaLinkYaml
from src.helpers.imports import *

Logger = LogSpecificFile(__name__)


class MusicService:
    def __init__(self, bot: AutoShardedBot):
        self.bot = bot
        self.voice_node = NodePool(bot)

    @inject
    async def connect_nodes(self, config=Provide[ApplicationContainer.config]):
        cConfig = config["application"]["lavalink"]
        try:
            await self.voice_node.create_node(
                host=cConfig["host"],
                port=cConfig["port"],
                label=(await self.bot.application_info()).name,
                password=cConfig["password"],
                heartbeat=cConfig["heartbeat"],
            )
            Logger.trace(f"Loaded - [ Mafic Voice Connection ]")
        except Exception as e:
            Logger.critical(f"Unavailable - [ Mafic Voice Connection ] : {e}")
