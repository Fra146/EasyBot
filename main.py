#©Fra146 2020
#This software is under GPL-3.0 License
#You can't distribute a closed version of this software


"If you are here to contribute, thank you!"

import discord, json

def die(reason):
    print(reason)
    exit()

def error(reason):
    if reason == "json":
        die("Error in json file")

f = open("commands.json", "r")
not_serial = f.read()
f.close()
com_list = json.loads(not_serial)

client = discord.Client()


@client.event
async def on_ready():
    print('Executed login with {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content in com_list['Commands']:
        await message.channel.send(com_list['Commands'][message.content])
    else:
        await message.channel.send(com_list['Config']['NotFoundError'])
f = open("token.txt", "r")
token = f.read()
f.close()

client.run(token)
