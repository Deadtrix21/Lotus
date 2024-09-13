from bot.services.extensions import ExtensionService
from helpers.cluster.bot import *


logger = specific_log("bot")


class DependencyBot(AutoShardedBot):
    extension_service: ExtensionService

    def __init__(self, **options):
        pass

    def configure_services(self, config: ApplicationConfig):
        self.extension_service = ExtensionService(self, config)

    def configure_env(self, config: DiscordConfig):
        command_prefix = when_mentioned_or(*config.container.prefix)
        case_insensitive = True
        super().__init__(case_insensitive=case_insensitive, command_prefix=command_prefix,
                         intents=discord.Intents.all())

    @logger.catch()
    @inject
    def run_bot(self, config: ApplicationConfig = Provide[ApplicationContainer.config]):
        self.configure_services(config)
        if config.environment.name == "development":
            select_env = config.environment.development
        else:
            select_env = config.environment.production
        self.configure_env(select_env)
        self.run(select_env.token)

    @logger.catch()
    async def run_services(self) -> None:
        await self.wait_until_ready()
        await self.extension_service.async_start_extension_loading()
        # await self.music_service.connect_nodes()

    @logger.catch()
    async def on_ready(self) -> None:
        await self.run_services()
        app = await self.application_info()
        logger.success(f"App Name - {app.name} | Made by - {app.owner.name} | {len(self.shards)}")
        logger.success(f"Bot Invite: https://discord.com/oauth2/authorize?client_id={app.id}&scope=bot&permissions=8")
