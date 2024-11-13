# Python-Web-Scraping

# About the Project
This project is a web scraper that browses through https://pokemondb.net/ and [the Pokemon Showdown Web API](https://github.com/smogon/pokemon-showdown-client/blob/master/WEB-API.md) to retrieve data on Pokemon attacks, items, abilities, or Pokemon. The web scraper was integrated with a Discord bot which allows users to search for the information on their own in a server using commands.

# Purpose
This bot is a personal use bot focused mainly on Pokemon. It currently is used to assist when preparing for Pokemon tournaments through looking up information on attacks and Pokemon. Other uses not compeititve related, but still Pokemon related, include helping create Link Codes to help make it easier to connect with other players in online tours.

# Examples of bot usage

![image](https://user-images.githubusercontent.com/115382866/219090751-a8b44346-b90d-45e7-876f-0657fd32ee45.png)

![image](https://user-images.githubusercontent.com/115382866/219090771-dd2f2099-b1b9-4e03-ab58-5299efabcdd4.png)

![image](https://user-images.githubusercontent.com/115382866/219090797-d64ff860-a6cb-4200-a400-6a43cd689a97.png)

![image](https://user-images.githubusercontent.com/115382866/219090817-34214dba-f164-407f-acdc-3e5d0e632f33.png)

# Requirements
To run this program, you first need to install discord.py as well as requests, lxml and bs4

To install, run pip install requests beautifulsoup4 discord.py lxml

To run the program, python discordbot.py will run the bot, however you need to provide your own token for it to work

To run the discord bot in your own server, replace the parameters TOKEN and discord_id with your own. Instructions can be found [here for the token](https://www.writebots.com/discord-bot-token/#:~:text=at%20ALL%20COSTS!-,What%20is%20a%20Discord%20Bot%20Token%3F,in%20turn%20controls%20bot%20actions.) and [here for the discord_id](https://poshbot.readthedocs.io/en/latest/guides/backends/setup-discord-backend/#find-your-guild-id-server-id)

The scraper itself is a standalone program which can also be run through python scraper.py to run a demo which looks for one attack, one Pokemon, one item, and one ability as an example



# Known Issues
1. Pokemon with multiple forms (Wooper, Tauros, Slowpoke, etc.) only return the first form introduced with no way to access the other forms
2. Moves that change power based off health (Wring Out, Water Spout, etc) do not display the caluclation formula due to the code tag
