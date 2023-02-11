import os
import discord
from discord import app_commands

from scraper import *
from dotenv import load_dotenv

load_dotenv()

no_result = "No result found! Please check your spelling or that what you are looking for actually exists."
client = discord.Client(intents = discord.Intents.all())
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'{client.user} is now online!')


@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    if message.content.startswith(f'!move '):
        search_term = message.content[6:]
        try:
            await message.channel.send(getMoveData(search_term));
        except: 
            await message.channel.send(no_result)
    
    if message.content.startswith(f'!ability '):
        try:
            search_term = message.content[9:]
            await message.channel.send(getAbilityData(search_term))
        except:
            await message.channel.send(no_result) 
    
    if message.content.startswith(f'!dt '):
        try:
            search_term = message.content[4:]
            await message.channel.send(getPokemonData(search_term))
        except:
            await message.channel.send(no_result)
    
    if message.content.startswith(f'!item '):
        try:
            search_term = message.content[6:]
            await message.channel.send(getItemData(search_term))
        except:
            await message.channel.send(no_result)
client.run(os.getenv('TOKEN'))
