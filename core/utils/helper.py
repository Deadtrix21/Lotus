from .common import *

prefix = ["X", "...", "="]
def intents():
    return discord.Intents.default().all()

async def set_prefix(bot, ctx):
    return commands.when_mentioned_or(*prefix)(bot, ctx)