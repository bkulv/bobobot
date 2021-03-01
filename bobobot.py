import os

import discord
from dotenv import load_dotenv

import random

# import mého webscaperu
from zakony import ustanoveniZakona

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.author)
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if message.content.find("§") == 0 or message.content.find("Čl.") == 0:
        ustanoveni = message.content.split()
        cislozakona = ustanoveni[3].split("/")
        response = ustanoveniZakona(f"{ustanoveni[0]} {ustanoveni[1]}", f"{cislozakona[1]}-{cislozakona[0]}")
        response = f"```{response}```"
        # response = "PARAGRAF"
        await message.channel.send(response)


client.run(TOKEN)