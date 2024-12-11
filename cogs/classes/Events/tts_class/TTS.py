import os, asyncio
import discord
from gtts import gTTS
from discord.utils import get
from asyncinit import asyncinit
from discord import FFmpegPCMAudio
from typing import Optional, List, Dict, Any
from dataclasses import field, fields, dataclass

@dataclass
class __data__:
    bot     : Optional[discord.ext.commands.AutoShardedBot]
    ctx     : Optional[Any]
    string  : Optional[str]



 
@asyncinit
class TTS:
    async def __init__(self, data:__data__):
        self.data = data
        self.next = asyncio.Event()
        self.name = "tts.wave"
        await self.process()
        
        
    async def get_audio(self):
        tts = gTTS(text=self.data.string, slow=False)
        tts.save(self.name)
        
    async def get_voice(self, channel:Optional[Any]=None):
        vc = get(self.data.bot.voice_clients, guild=self.data.ctx.guild)
        if not vc:
            try:
                channel = self.data.ctx.author.voice.channel
            except AttributeError:
                await ctx.send('No channel to join. Please join one.')
            try:
                vc = await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Connecting to channel: <{channel}> timed out.')
        return vc
    
    
        
        
        
    async def play_audio(self):
        vc = await self.get_voice()
        try:
            vc.play(FFmpegPCMAudio(self.name), after=None)
            await asyncio.sleep(10)
            await vc.disconnect()
        except Exception as E:
            print(E)
        
        
        
    async def process(self):
        await self.get_audio()
        await self.get_voice()
        await self.play_audio()