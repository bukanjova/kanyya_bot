from replit import db

async def add_hate(words):
  print(db["hate"])
  if "{}" in words:
    if "hate" in db.keys():
      hate = db["hate"]
      hate.append(words)   
      db["hate"] = hate 
    else:
      db["hate"] = [words]

async def get_hate():
  return list(db["hate"])

async def get_love(message):
  msg = message.content
  if msg.endswith('?'):
    slug = msg.split(' ')
    acc = slug[3] == 'love' and len(slug) == 5
    if acc:
      person1 = slug[2]
      person2 = slug[4][:-1]
      if person1 == person2:
        await message.channel.send("i don't know")
      elif not (len(person1) + len(person2)) % 3:
        await message.channel.send('yes')
      else:
        await message.channel.send('no')
    else:
      await message.channel.send('invalid input')
  else:
    await message.channel.send("missing '?'")
