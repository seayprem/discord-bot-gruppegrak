import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message():
    if message.author == client.user:
      return

    if message.content.startWith('$hello'):
      await message.channel.send('สำหรับท่านที่เดินผ่านไปผ่านมาแวะมาชิมกันก่อนได้นะครับ')

  client.run(os.getenv('TOKEN'))