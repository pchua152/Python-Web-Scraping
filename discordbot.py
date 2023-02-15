import os
import discord
from discord import app_commands

from scraper import *
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents = discord.Intents.all())
tree = app_commands.CommandTree(client)
discord_id = os.getenv('discord_id')

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=discord_id))
    print(f'{client.user} is now online!')


@tree.command(name = "move", description="Learn basic information about a certain move",guild=discord.Object(id=discord_id))
@app_commands.describe(move = "attack to learn information about")
async def moveData(phrase: discord.Interaction, move: str):    
    await phrase.response.send_message(getMoveData(move))
    
@tree.command(name = "ability", description="Learn what an ability does",guild=discord.Object(id=discord_id))
@app_commands.describe(ability = "ability to learn information about")
async def abilityData(phrase: discord.Interaction, ability: str):    
    await phrase.response.send_message(getAbilityData(ability))
    
@tree.command(name = "pokemon", description="Learn the competitive relevant information about a Pokemon",guild=discord.Object(id=discord_id))
@app_commands.describe(pokemon = "Pokemon to learn information about")
async def PokemonData(phrase: discord.Interaction, pokemon:str):    
    await phrase.response.send_message(getPokemonData(pokemon))

@tree.command(name = "item", description="Learn what an item does",guild=discord.Object(id=discord_id))
@app_commands.describe(item = "item to learn information about")
async def PokemonData(phrase: discord.Interaction, item:str):    
    await phrase.response.send_message(getItemData(item))
    

 
""" 
Leaving the ! starts in for now in case other people use it
@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    if message.content.startswith(f'!move '):
        search_term = message.content[6:]
        await message.channel.send(getMoveData(search_term))
    
    if message.content.startswith(f'!ability '):
    
        search_term = message.content[9:]
        await message.channel.send(getAbilityData(search_term))
       
    
    if message.content.startswith(f'!dt '):
        search_term = message.content[4:]
        await message.channel.send(getPokemonData(search_term))
        
    
    if message.content.startswith(f'!item '):
    
        search_term = message.content[6:]
        await message.channel.send(getItemData(search_term)) """
       
client.run(os.getenv('TOKEN'))
