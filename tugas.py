import requests
import json
import discord
import random

colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

async def getTugas(message, category=''):
  embed = discord.Embed(title='Semua Tugas {}\n_______'.format(category), color=random.choice(colors))
  response = requests.get('https://tugas-api.herokuapp.com/tugas/{}'.format(category))
  json_data = json.loads(response.text)
  tugas_txt = ""

  for item_tugas in json_data:
    tugas_txt = f"""
      **Deadline : {item_tugas['deadline']}**\n
      **Title : {item_tugas['title']}**
      Description : {item_tugas['description']}
      ___________
    """
    embed.add_field(name=item_tugas['category'], value=tugas_txt, inline=False)
    tugas_txt = ""

  await message.channel.send(embed=embed)