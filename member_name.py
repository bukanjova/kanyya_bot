from replit import db

async def add_name(member_id, real_name, display_name):
  if "member_list" in db.keys():
    member_list = db["member_list"]
    member_list.append(member_id + " : " + real_name + " : " + display_name)
    db["member_list"] = member_list
  else:
    db["member_list"] = [member_id + " : " + real_name + " : " + display_name]


async def change_name(member_id, new_name):
  member_list = db["member_list"]
  for i in range(len(member_list)):
    if member_list[i].startswith(member_id):
      raw_name = (member_list[i]).split(" : ")
      member_list[i] = member_id + " : " + new_name + " : " + raw_name[2]
      break
  db["member_list"] = member_list


async def remove_name(member_id):
  member_list = db["member_list"]
  for i in range(len(member_list)):
    if member_list[i].startswith(member_id):
      member_list.pop(i)
      break
  db["member_list"] = member_list


async def get_name(message, embed):
  lists_name = []
  real_name = []
  list_server_id = []
  list_server_name = []

  if "member_list" in db.keys():
    lists_name = db["member_list"]

  for member in message.guild.members:
    if member.bot:
      continue
    list_server_id.append(str(member.id))
    list_server_name.append(f"{len(list_server_name) + 1}. {member.display_name}")

  for _id in list_server_id:
    for data_id in lists_name:
      if data_id.split(" : ")[0] == _id:
        real_name.append(f"{len(real_name) + 1}. {data_id.split(' : ')[1]}")
  
  embed.add_field(name = "Nickname\t\t.\t\t", value='\n'.join(list_server_name))
  embed.add_field(name = "Real Name", value='\n'.join(real_name))
  await message.channel.send(embed = embed)