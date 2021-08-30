import discord
import os
from keep_alive import keep_alive
from member_name import get_name

intents = discord.Intents(messages=True, guilds=True, members=True)

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):
  channel = client.get_channel(877611571843592286)
  await channel.send(f"Anjay welkam {member.name}. Harap interupsi dan perkenalkan diri") 
  await channel.send("<:Pepega:880828641766932500>")


@client.event
async def on_member_remove(member):
  channel = client.get_channel(877611571843592286)
  await channel.send(f"{member.name} kok left :(\n :pepehands:")
  await channel.send("<:PepeHands:881946934154231839>")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg == '!siapakamu':
    embed = discord.Embed(title='Siapa Kamu?!')
    await get_name(message, embed)
    
keep_alive()
client.run(os.getenv('TOKEN'))