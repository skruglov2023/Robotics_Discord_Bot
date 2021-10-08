TokenPath = '/home/pi/Desktop/scripts/Robotics_token'
#GuildPath='/home/pi/Desktop/scripts/guild'

#with open(GuildPath, 'r') as guil:
#    global GUILD
#    almostGuild = guil.read()
#    GUILD =  almostGuild
with open(TokenPath, 'r') as toke:
    global TOKEN
    almostToken = toke.read()
    TOKEN =  almostToken
bot = commands.Bot(command_prefix='!')

bot.run(TOKEN)
