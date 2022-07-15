from cProfile import label
import discord, os, time, asyncio
from discord.ext import commands
from discord.ui import Button
import random

game = discord.Game("당신의 오류를 보는중")
bot = discord.Bot(status=discord.Status.online)
game = discord.Game("noProb!!")
token = "(TOKEN)"

# if bot ready
@bot.event
async def on_ready():
    print(f'Logged on: {bot.user}')

#commands
@bot.slash_command(description="봇의 반응속도를 보여줍니다.")
async def ping(ctx):
    embed = discord.Embed(title="🏓 퐁!", description=f"봇의 반응속도: {bot.latency}ms", color=0xffffff)
    await ctx.respond(embed=embed)

@bot.slash_command(description="주사위를 굴려보아요")
async def roll(ctx):
    embed = discord.Embed(title="🎲 주사위를 굴립니다...")
    await ctx.respond(embed=embed)
    a = random.randrange(1,10)
    b = random.randrange(1,10)
    if a > b:
        embed = discord.Embed(title="✅ 성공!", description="봇의 숫자: " + str(a) + " 당신의 숫자: " +  str(b), color=0x42f55d)
        await ctx.respond(embed=embed)
    elif a == b:
        embed = discord.Embed(title="무승부!", description="봇의 숫자: " + str(a) + " 당신의 숫자: " +  str(b), color=0xffffff)
        await ctx.respond(embed=embed)
    elif a < b:
        embed = discord.Embed(title="❌ 실패!", description="봇의 숫자: " + str(a) + " 당신의 숫자: " +  str(b), color=0xff2200)
        await ctx.respond(embed=embed)

help = bot.command.group(
    "도움말", "도움말을 볼수 있어요."
)
# currently devloping
@help.command(description="명령어를 볼수 있어요.")
async def help(ctx):
    embed = discord.Embed(title="🛠️ 명령어")
    embed.add_field(name="주사위", value="/roll")
    embed.add_field(name="현재 반응속도를 볼수 있어요.", value="/ping")
    embed.add_field(name="도움말을 볼수 있어요, 지금 쓰고있는 명령어에요!", value="/help")
    embed.set_footer(text="Page 1/2, /명령어 2 를 입력해서 다음 페이지를 보세요!")
    await ctx.respond(embed=embed)

@help.command(description="명령어의 다음장이에요.")
async def help2(ctx):
    embed = discord.Embed(title="🛠️ 명령어", description="description", color=0xff0000)
    embed.add_field(name="asdf", value="asdf", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def hellothisisverification(ctx):
    await ctx.respond("다람루#9913(660131925801041950)")

bot.run(token)
