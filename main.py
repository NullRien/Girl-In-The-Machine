import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from PIL import Image
load_dotenv()
TOKEN = os.getenv("TOKEN")
intent = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intent, help_command=None)
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
#save the image that the user sends to chat
@bot.command()
async def kill(ctx):
    await ctx.send('Putting it in the machine...')
    await ctx.message.attachments[0].save('downloaded.png')
    await ctx.message.delete()
    #convert the image size
    basewidth = 100
    img = Image.open('downloaded.png')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('converted.png')
    # open the image
    Image1 = Image.open('empty.png')
    Image1copy = Image1.copy()
    Image2 = Image.open('converted.png')
    Image2copy = Image2.copy()
    Image1copy.paste(Image2copy, (250, 250))
    Image1copy.save('finished.png')
    #send the finished image
    await ctx.send(file=discord.File('finished.png'))
bot.run(TOKEN)