
'''
This bot for discord posts random quotes of chairman Mao based on the year
of publishing
'''


#Import all the libraries
import discord
from discord.ext import commands
import random
import pandas as pd


#Declare our client and bot
client = discord.Client()
bot = commands.Bot(command_prefix = 'Mao_')


#Load all the quotes from exel fail
quotes = pd.read_excel('/MaoZedong/quotes.xls')


#Make a directory for all the quotes through a dictionary
Mao_content = {key: [] for key in range(1, 8)}
for i in Mao_content.keys():
    Mao_content[i] = quotes.columns[i-1]
    
    
#A command sending the contnet of the quotations
@bot.command(aliases = ['contents', 'CONTENTS', 'CONTENT', 'Contents'])
async def content(ctx):
        await ctx.send('Contents:')
    for i in Mao_content.keys():
        await ctx.send(f"{i} - {Mao_content[i]}")


#Activate the bot
@bot.event
async def on_ready():
    print('Mao is active')


#A command sending the contnet of the quotation book
@bot.command(aliases = ['contents', 'Content', 'Contents'])
async def content(ctx):
    await ctx.send(Mao_content)


#A command with the direct referal accroding to the content
@bot.command(aliases = ['quote', 'personal'])
async def direct(ctx, *, n):
    await ctx.send(random.choice(quotes[quotes[Mao_content[int(n)]].isnull() == False]
        .loc[:, Mao_content[int(n)]]))


#A command sending an absolute random quote form .xls
@bot.command(aliases = ['random', '0'])
async def random_quote(ctx):
    i = random.choice(list(Mao_content.keys()))
    await ctx.send(random.choice(quotes[quotes[Mao_content[i]].isnull() == False]
        .loc[:, Mao_content[i]]))







bot.run(TOKEN)
