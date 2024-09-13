import json

import requests

from helpers.extentions.base import *
from helpers.extentions.custom_wrappers import guild_only
from .features.displayEmbeds import build_embed


class ApexLegends(Cog):
    LEGENDS = [
        "Octane",
        "Wraith",
        "Bloodhound",
        "Pathfinder",
        "Lifeline",
        "Valkyrie",
        "Bangalore",
        "Caustic",
        "Horizon",
        "Loba",
        "Fuse",
        "Gibraltar",
        "Seer",
        "Mirage",
        "Revenant",
        "Rampart",
        "Wattson",
        "Crypto"
    ]
    PLATFORM = [
        "PC",
        "Playstation",
        "Xbox"
    ]

    def __init__(self, bot) -> None:
        self.bot = bot
        self.rotations: dict = {}
        self.embeds: tuple[Embed] = None
        self.get_apex_maps.start()

    def cog_unload(self):
        self.get_apex_maps.cancel()

    @tasks.loop(seconds=10)
    async def get_apex_maps(self) -> None:
        print(requests.get("get", "https://lil2-gateway.apexlegendsstatus.com/gateway.php?qt=map").json())
        data: dict = \
            json.loads(requests.get("get", "https://lil2-gateway.apexlegendsstatus.com/gateway.php?qt=map").json())[
                'rotation']
        if ("battle_royale" in data):
            self.rotations["br"] = data["battle_royale"]
        if ("ranked" in data):
            self.rotations["r"] = data["ranked"]
        if ("ltm" in data):
            self.rotations["ltm"] = data["ltm"]
        self.embeds = build_embed(self.rotations)

    @guild_only(name="apex-maps")
    async def apex_maps(self, ctx: BridgeContext):
        """ Get the current map rotations
        """
        print(requests.get("https://lil2-gateway.apexlegendsstatus.com/gateway.php?qt=map").json())
        if isinstance(ctx, BridgeExtContext):
            for i in self.embeds:
                await ctx.message.reply(embed=i)
            return
        if isinstance(ctx, BridgeApplicationContext):
            for i in self.embeds:
                await ctx.respond(embed=i)
            return

    # @bridge_command(name='apex-legend-stats')
    # @discord.option(name="platform", choices=PLATFORM, description="Search platform")
    # @discord.option(name="legend", choices=LEGENDS, description="Searched player legend")
    # @discord.option(name="player", description="Search player name")
    # async def apex_legend_stats(self, ctx: BridgeContext, platform: str = None, legend: str = None, player: str = None):
    #     """
    #     Get a players stats on a legend
    #     Please make sure to use Upper Case
    #
    #     platform: Example: Xbox
    #     legend: Example: Octane
    #     player: Example: DeadTrix4053
    #     """
    #     if platform == None or legend == None or player == None:
    #         return await ctx.reply("You missed some details.")
    #     platform = "PC" if platform == "PC" else platform
    #     platform = "PS4" if platform == "Playstation" else platform
    #     platform = "X1" if platform == "Xbox" else platform
    #     await ctx.reply("Starting Search")
    #     data = json.loads(urllib3.request("get",
    #                                       "https://lil2-gateway.apexlegendsstatus.com/gateway.php?qt=stats-single-legend&userName="
    #                                       + player + "&userPlatform=" + platform + "&userLegend=" + legend).data)
    #     with open("file.json", "w") as file:json.dump(data, file)
    #     if isinstance(ctx, BridgeExtContext):
    #         pass
    #     elif isinstance(ctx, BridgeApplicationContext):
    #         pass


def setup(bot):
    cog = ApexLegends(bot)
    bot.add_cog(cog)
