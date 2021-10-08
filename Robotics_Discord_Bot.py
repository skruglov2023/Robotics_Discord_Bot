import discord
from discord.ext import commands
TokenPath = '/home/pi/Desktop/scripts/Robotics_token'
GuildPath='/home/pi/Desktop/scripts/Robotics_guild'
#load files using above paths
with open(GuildPath, 'r') as guil:
    global GUILD
    almostGuild = guil.read()
    GUILD =  almostGuild
with open(TokenPath, 'r') as toke:
    global TOKEN
    almostToken = toke.read()
    TOKEN =  almostToken

bot = commands.Bot(command_prefix='!') #give bot some usage parameters
@bot.event
async def on_ready():
    print("Logged in as Robotics Bot")


bot.run(TOKEN) #run bot
