member_list = {
  "713265740764938252": "Mas Jerry",
  "231415863629185026": "Arga Ganteng Katanya",
  "710509883245461515": "Jova Unch",
  "744764076651053106": "Jjooyy Pro Peler Valo",
  "739344507811921961": "Ayub Pacarnya Ragil",
  "748910496316522697": "Nikonikoniii",
  "703153744765779980": "Mozzz | Tian",
  "752168080641359883": "Mian Tukang Halu",
  "747626901413298277": "Greg - Lost People",
  "749111086195933286": "Stephanie I Lob U 3000",
  "747468422874660915": "Yohana VVibu"
}

async def get_name(message, embed):
  d_name = []
  r_name = []
  for member in message.guild.members:
    if member.bot or (str(member.id) not in member_list):
      continue
    d_name.append(member.display_name)
    r_name.append(member_list[str(member.id)])
    
  embed.add_field(name = "Nicknamenya\t\t.\t\t", value='\n'.join(d_name))
  embed.add_field(name = "Aslinya", value='\n'.join(r_name))
  await message.channel.send(embed = embed)