
from typing import Optional

import discord
import loguru
from dependency_injector.wiring import inject, Provide
from discord.ext.bridge import AutoShardedBot
from discord.ext.commands import when_mentioned_or

from containers.container import ApplicationContainer
from containers.factories.logger import specific_log

from containers.models.config import ApplicationConfig, DiscordConfig