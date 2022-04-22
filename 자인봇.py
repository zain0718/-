import discord
from discord.ext import commands
import time
import asyncio
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command (      name = '따라하기')
async def 따라하기(ctx, *, number):
      await ctx.send(embed = discord.Embed(title = '따라하기', description = number, color = 0x00ff00))

@bot.command()
async def 들어와(ctx):
    try:
     global vc
     vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send('시발 자슥아 채널에 들어가있어야 들어가든 말든하지')

@bot.command()
async def 나가(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send('명태 엉덩이 찰싹찰싹')

bot.run('OTY1MjQ3NTAxNzY4NzI0NDgw.YlwayQ.k3cxMXvqlRBYTziF4Digcav1UYY')