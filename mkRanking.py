import discord
#from discord.ext.commands import Bot
from discord.ext import commands
import extractRanking

Client = discord.Client()
bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)
footer_img = "https://cdn.discordapp.com/attachments/839743332891885588/929645365479759882/pylogo.png"

TOKEN = ''

@client.event
async def on_ready():
    global TOKEN
    print("Check your MetaKongz Rank")

@client.event
async def on_message(message):
    if message.content.startswith('!rank'):
      messageSplit = message.content.split(' ')
      kongz_number = str(messageSplit[1])
      channel = message.channel
      
      score, rank, img = extractRanking.extract(kongz_number)
      
      embed = discord.Embed(title="META KONGZ #" + str(kongz_number), description="", color=0x000000)
      embed.add_field(name="**Ranking**", value=rank, inline=True)
      embed.add_field(name="**Score**", value=score, inline=True)
      embed.set_image(url=img)
      embed.set_footer(text="Powered By pYsson#3604", icon_url=footer_img)
      await channel.send(embed=embed)


if __name__ == '__main__':
  while True:
    if len(TOKEN) == 0:
      TOKEN = input("Type your discord bot token: ")
    else:
      break
    
  client.run(TOKEN)