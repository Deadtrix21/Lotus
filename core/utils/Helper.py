from discord.ext import commands
from discord.ext.bridge import AutoShardedBot
from discord.ext.commands import Cog
from .CustomErrors import *
import discord, os
from pymongo import MongoClient

prefix = ["X","...", "="]

def intents ():
    return discord.Intents.default().all()

async def set_prefix(bot, ctx):
    return commands.when_mentioned_or(*prefix)(bot, ctx)
