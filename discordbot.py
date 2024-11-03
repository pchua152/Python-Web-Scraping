import os
import discord
from random import randrange
from discord import app_commands

from scraper import *
from dotenv import load_dotenv

# get environment variables from .env file
load_dotenv()

client = discord.Client(intents = discord.Intents.all())
tree = app_commands.CommandTree(client)
discord_id = os.getenv('discord_id')

@client.event
async def on_ready():
    channelid = os.getenv('channelid')
    await tree.sync()
    await client.get_channel(int(channelid)).send("Hello, bot online is now")
    
    print(f'{client.user} is now online!')


@tree.command(name = "move", description="Learn basic information about a certain move")
@app_commands.describe(move = "attack to learn information about")
async def moveData(phrase: discord.Interaction, move: str):    
    await phrase.response.send_message(getMoveData(move))
    
@tree.command(name = "ability", description="Learn what an ability does")
@app_commands.describe(ability = "ability to learn information about")
async def abilityData(phrase: discord.Interaction, ability: str):    
    await phrase.response.send_message(getAbilityData(ability))
    
@tree.command(name = "pokemon", description="Learn the competitive relevant information about a Pokemon")
@app_commands.describe(pokemon = "Pokemon to learn information about")
async def PokemonData(phrase: discord.Interaction, pokemon:str):    
    await phrase.response.send_message(getPokemonData(pokemon))

@tree.command(name = "item", description="Learn what an item does")
@app_commands.describe(item = "item to learn information about")
async def PokemonData(phrase: discord.Interaction, item:str):    
    await phrase.response.send_message(getItemData(item))

@tree.command(name = "code", description= "Generate link code to use when playing vs others")
async def randomgenerate(interaction: discord.Interaction):
    await interaction.response.send_message(genCode())
    

client.run(os.getenv('TOKEN'))
