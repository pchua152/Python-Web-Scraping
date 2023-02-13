# Python-Web-Scraping

# About the Project
This project is a simple web scraper that browses through https://pokemondb.net/ to retrieve data on Pokemon attacks, items, abilities, or Pokemon. The web scraper was integrated with a Discord bot which allows users to search for the information on their own in a server using commands.

# Purpose
The purpose of the project was to allow me to have an easier way to look up data regarding certain Pokemon strategies while I practice for competitive Pokemon events.

# Data is returned in the following formats


![FopM4hwWcAAtQn5](https://user-images.githubusercontent.com/115382866/218520550-90e8a3df-8457-417b-9f0d-3c5ad4eb5dea.png)
![FopM51qWcAECYxM](https://user-images.githubusercontent.com/115382866/218520592-83e63a7d-3378-4132-a709-9d15dbbb2cef.png)
![FopM7JlX0AEBqnO](https://user-images.githubusercontent.com/115382866/218520604-5b62e7aa-89c8-445b-b6da-bc000bf04548.png)
![FopM8YzWIAISEdH](https://user-images.githubusercontent.com/115382866/218520610-f3d7de7c-62ef-4105-b77a-406204042ae8.png)

# Requirements
To run this program, you first need to install discord.py as well as requests and bs4

to install, run pip install requests beautifulsoup4 discord.py

to run the program, python discordbot.py will run the bot, however you need to provide your own token for it to work

the scraper itself is a standalone program which can also be run through python scraper.py to run a demo which looks for one attack, one Pokemon, one item, and one ability as an example

# Known Issues
1. Pokemon with multiple forms (Wooper, Tauros, Slowpoke, etc.) only return the first form introduced with no way to access the other forms
2. Using ! to start a command probably isnt the greatest way to use this, currently working on a way to get / commands to work for ease of use along with detailed descriptions
