from asyncinit import asyncinit
from waifu import WaifuClient
from discord import Embed
from discord.ext import bridge


@asyncinit
class action_anime():
   
    
    
    async def __init__(self, ctx, member, action:str, nsfw=False) -> None:
        self.waifu = WaifuClient()
        self.action = action.lower()
        self.context = ctx
        self.member = member
        self.nsfw = nsfw
        await self.send_embed()

    
    async def set_gif(self):
        if self.nsfw:
            if self.action in self.ImagesNsfw:
                return self.waifu.nsfw(self.action)
            else:
                return self.waifu.sfw(self.action)
        else:
            return self.waifu.sfw(self.action)


    async def set_thumbnail(self, UserEmbed:Embed):
        UserEmbed.set_thumbnail(url=await self.set_gif())


    async def generate_embed(self):
        UserEmbed = None
        if self.nsfw:
            UserEmbed = Embed(
                title = f"{self.action}",
                description = "",
                color = 0x00c30
            )
        else:
            word = None
            UserEmbed = Embed(
                title = f"{word}",
                description = "",
                color = 0x00c30
            )
        await self.set_thumbnail()
        return UserEmbed


    async def sentence_generate(self):
        word = None
        self.cringe(word)
        self.dance(word)
        self.poke(word)
        self.wink(word)
        self.happy(word)
        self.kick(word)
        self.kill(word)
        self.slap(word)
        self.bite(word)
        self.nom(word)
        self.handhold(word)
        self.highfive(word)
        self.wave(word)
        self.smile(word)
        self.blush(word)
        self.yeet(word)
        self.bonk(word)
        self.smug(word)
        self.pat(word)
        self.lick(word)
        self.kiss(word)
        self.hug(word)
        self.cry(word)
        self.cuddle(word)
        self.bully(word)
        return word


    async def send_embed(self):
        if isinstance(self.context, bridge.BridgeExtContext):
            return self.context.send(embed= await self.generate_embed())
        elif isinstance(self.context, bridge.BridgeApplicationContext):
            return self.context.respond(embed= await self.generate_embed())

    def cringe(self, _):pass;
    def dance(self, _):pass;
    def poke(self, _):pass;
    def wink(self, _):pass;
    def happy(self, _):pass;
    def kick(self, _):pass;
    def kill(self, _):pass;
    def slap(self, _):pass;
    def bite(self, _):pass;
    def nom(self, _):pass;
    def handhold(self, _):pass;
    def highfive(self, _):pass;
    def wave(self, _):pass;
    def smile(self, _):pass;
    def blush(self, _):pass;
    def yeet(self, _):pass;
    def bonk(self, _):pass;
    def smug(self, _):pass;
    def pat(self, _):pass;
    def lick(self, _):pass;
    def kiss(self, _):pass;
    def hug(self, _):
        if self.action == "hug":
            if self.member != None:
                _ = f""
            else:
                _ = f""
    def cry(self, _):
        if self.action == "cry":
            if self.member != None:
                _ = f""
            else:
                _ = f""
    def cuddle(self, _):
        if self.action == "cuddle":
            if self.member != None:
                _ = f""
            else:
                _ = f""
    def bully(self, _):
        if self.action == "bully":
            if self.member != None:
                _ = f""
            else:
                _ = f""
                
    


    ImagesNsfw = [
        'waifu',
        'neko',
        'blowjob'
        ]
    ImagesSfw = [ 
        'bully',    'cuddle',   'cry',      'hug',
        'kiss',     'lick',     'pat',      'smug',
        'bonk',     'yeet',     'blush',    'smile',
        'wave',     'highfive', 'handhold', 'nom', 
        'bite',     'slap',     'kill',     'kick', 
        'happy',    'wink',     'poke',     'dance', 
        'cringe'
        ]