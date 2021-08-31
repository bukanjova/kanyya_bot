import discord
import os
from keep_alive import keep_alive
from member_name import add_name, change_name, remove_name, get_name

intents = discord.Intents(messages=True, guilds=True, members=True)

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):
  channel = client.get_channel(882008576611201064)
  await add_name(str(member.id), member.name, member.display_name)
  await channel.send(f"Anjay welkam {member.name}. Harap interupsi dan perkenalkan diri") 
  await channel.send("<:Pepega:880828641766932500>")


@client.event
async def on_member_remove(member):
  channel = client.get_channel(882008576611201064)
  await remove_name(str(member.id))
  await channel.send(f"{member.name} kok left :(")
  await channel.send("<:PepeHands:881946934154231839>")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg == '!fact':
    embed = discord.Embed(title='Siapa Kamu?!')
    await get_name(message, embed)
  
  if msg.startswith("!changename"):
    if str(message.author.id) == os.getenv('ADMIN'):
      slug = msg.split(". ")
      if len(slug) != 3:
        await message.channel.send("input tidak valid")
      else:
        await change_name((slug[1])[3:-1], slug[2])
    else:
      await message.channel.send("I've told you thousands of times, only my boyfriend can use this command")
      await message.channel.send("<:Pepega:880828641766932500>")
  
  if msg == 'kanyya help':
    desc = "!fact = reveal every member's real name\n\n!changename. <tag>. <new name> = change member's real name. Btw, only my boyfriend can do this."
    embed = discord.Embed(title='Current Available Command', description=desc)
    await message.channel.send(embed = embed)
  
  if msg == "kanyya":
    await message.channel.send("wut?")
  
  if msg.startswith("kanyya i was hurt by "):
    victim = msg.split(" ")[-1]
    if victim[3:-1] != os.getenv('ADMIN') and victim[3:-1] != os.getenv('ADMIN2'):
      await message.channel.send(f"Fuck you {victim}! I will hate you for life.")
    else:
      await message.channel.send("I don't believe you. He is my boy.")
    
keep_alive()
client.run(os.getenv('TOKEN'))
