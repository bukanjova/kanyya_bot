import discord
import os
from keep_alive import keep_alive
from member_name import add_name, change_name, remove_name, get_name
from temp_data import add_hate, get_hate, get_love
import random
from tugas import getTugas

intents = discord.Intents(messages=True, guilds=True, members=True)

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your heart"))
  print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):
  channel = client.get_channel(882008576611201064)
  await add_name(str(member.id), member.name, member.display_name)
  await channel.send(f"Welkam {member.name}. Harap interupsi dan perkenalkan diri") 
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
  
  if msg == 'kanyya revealname':
    embed = discord.Embed(title='How r u?!')
    await get_name(message, embed)
  
  if msg.startswith("!changename"):
    if str(message.author.id) == os.getenv('ADMIN'):
      slug = msg.split(". ")
      if len(slug) != 3:
        await message.channel.send("input tidak valid")
      else:
        print(slug[1])
        if slug[1].startswith("<@!"):
          await change_name((slug[1])[3:-1], slug[2])
          await message.channel.send("name updated")
        elif slug[1].startswith("<@"):
          await change_name((slug[1])[2:-1], slug[2])
          await message.channel.send("name updated")
        else:
          await message.channel.send('invalid input')
    else:
      await message.channel.send("I've told you thousands of times, only my boyfriend can use this command")
      await message.channel.send("<:Pepega:880828641766932500>")
  
  if msg == 'kanyya help':
    desc = "kanyya revealname = reveal every member's real name\n\nkanyya i was hurt by <tag or name> = I will by your side.\n\nkanyya do you love me? = just try it!\n\nkanyya does <he/she> love <he/she>? = I will use my vision\n\n<message>!rc = random capitalize message\n\n!changename. <tag>. <new name> = change member's real name. Btw, only my boyfriend can do this.\n\n"
    embed = discord.Embed(title='Current Available Command', description=desc)
    await message.channel.send(embed = embed)
  
  if msg == "kanyya":
    await message.channel.send("wut?")
  
  if msg.startswith("kanyya i was hurt by "):
    victim = msg.split(" ")[-1]
    if os.getenv('ADMIN2') in victim:
      await message.channel.send("I am so sorry :(")
    elif os.getenv('ADMIN') in victim:
      await message.channel.send("I don't believe you. He is my boy.")
    else:
      words = await get_hate()
      words = random.choice(words)
      await message.channel.send(words.format(victim))
  
  if msg.startswith("!addhate"):
    slug = msg.split(" ")[1:]
    await add_hate(' '.join(slug))
  
  if msg == "kanyya do you love me?":
    rnd_list_hahaha = ["of course", "maybe", "no", "definitely..no", "emmm.. ya", "YASS", "BIG NO", "i don't know", "trsrh", "iuhhhhh no", "-_-, i have boyfriend", "sorry..but, it's disgusting"]
    if str(message.author.id) == os.getenv('ADMIN'):
      await message.channel.send("YAA, OF COURSE. WHY DON'T U BELIEVE ME")
    else:
      await message.channel.send(random.choice(rnd_list_hahaha))
  
  if msg.startswith('kanyya does'):
    await get_love(message)
  
  if msg.startswith("task"):
    jurusan = msg.split("::")[-1]
    await getTugas(message, jurusan.upper())
  
  if msg.endswith('!rc'):
    new_msg = ''.join(random.choice((str.upper, str.lower))(c) for c in msg[:-3])
    await message.channel.send(new_msg)

keep_alive()
client.run(os.getenv('TOKEN'))
