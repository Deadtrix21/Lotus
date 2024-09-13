from helpers.extentions.base import *
from helpers.extentions.custom_wrappers import guild_only


class Admin(Cog):
    def __init__(self, bot):
        self.bot = bot

    @guild_only("kick", ["k"])
    async def kick_command(self, ctx):
        """
        Kicks a member from the server. Reason is required.
        """
        await ctx.send(f"Kicked for reason")

    @guild_only("ban", ["b"])
    async def ban_command(self, ctx):
        """
        Bans a member from the server. Reason is required.
        """
        await ctx.send(f"Banned for reason")

    @guild_only("mass-kick", ["masskick", "mkick"], 1, 10)
    async def mass_kick_command(self, ctx):
        """
        Mass kicks members from the server. Reason is required.
        """
        await ctx.send(f"Mass kicked for reason")

    @guild_only("mass-ban", ["massban", "mban"], 1, 10)
    async def mass_ban_command(self, ctx):
        """
        Mass bans members from the server. Reason is required.
        """
        await ctx.send(f"Mass banned for reason")

    @guild_only("delete-messages-bot", ["delmsgbot", "dmbot"])
    async def delete_messages_bot_command(self, ctx):
        """
        Deletes messages from bot in the server.
        """
        await ctx.send(f"Deleted messages from bot")

    @guild_only("delete-messages", ["delmsg", "dm"])
    async def delete_messages_command(self, ctx):
        """
        Deletes messages from members in the server.
        """
        await ctx.send(f"Deleted messages from members")


def setup(bot):
    cog = Admin(bot)
    bot.add_cog(cog)
