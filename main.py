import discord

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    pass

@client.event
async def on_ready():
    print('Ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you draft"))


reading = open('key.txt', 'r')
TOKEN = reading.readline().strip()
reading.close()

client.run(TOKEN)