import requests
import bs4
from random import randrange
import json


rootUrl = "https://pokemondb.net/move/"
abilityUrl = "https://pokemondb.net/ability/"
itemUrl = "https://pokemondb.net/item/"
movesUrl = "https://play.pokemonshowdown.com/data/moves.json"

ShowdownUrl = "https://play.pokemonshowdown.com/data/pokedex.json"

def getPokemonData(text):
        #Alternate forms are written like this: ninetalesalola, typenull, mimejr
        htmlData = requests.get(ShowdownUrl)
        monjson = json.loads(htmlData.content.decode('utf-8'))
        mon = text.lower()
        mon_info = ''
        
        if mon in monjson:
               info = monjson[mon]
               ability_list = []
               mon_info += "Displaying data for: " + info['name'] + "\n"
               mon_info += "Type: " + str(info['types']) + "\n"
               # The data source has it as 0: Ability name ,just removing the number since its not relevant
               for ability in info['abilities']:
                       ability_list.append(info['abilities'][ability])
                
               mon_info += "Abilities: " + str(ability_list) + "\n"
               
               mon_info += "Base Stats: " + str(info['baseStats'])
               return mon_info
        else:
             return "Pokemon not found, please check your spelling and try again"  
       
                       
               

def textCleanUp(text):
        #This is just split up line by line so I can see easier if I'm missing something to replace
        text = text.replace(' ','-')
        text = text.replace("'",'')
        text = text.replace(":",'')
        text = text.replace(".",'')
        
        #Mr. Mime -> mr-mime
        #Mime Jr. -> mime-jr
        #Type: Null -> type-null
        text = text.lower()
        return text
        

def getMoveData(attack):
        htmldata = requests.get(movesUrl)
        moveJson = json.loads(htmldata.content.decode('utf-8'))
        fattack = "".join(attack.split())
        fattack = fattack.lower()
        
        
        if fattack in moveJson:
                info = moveJson[fattack]
                result = ""
                result += "Displaying data for: " + attack + "\n"
                result += "Type: " + str(info['type']) + "\n"
                result += "Accuracy: " + str(info['accuracy']) + "\n"
                result += "Category: " + str(info['category']) + "\n"
                result += "Base Power: " + str(info['basePower']) + "\n"
                result += "priority: " + str(info['priority']) + "\n"
                result += "Description: " + info['shortDesc']
                return result
        return "No attack found, please try a different attack"
        
        
                
       
def getAbilityData(ability):
        
       try:
                data = "" 
                ability = textCleanUp(ability)
                htmlData = requests.get(abilityUrl+ability)
                soup = bs4.BeautifulSoup(htmlData.text, "lxml")
                
                title = soup.find('h2').text
                effect = soup.find('p').text
                
                data +=  title + ": " + effect
                return data
       except:
               return "No data found"
               
      
        
        
def getItemData(item):
        try:
                item = textCleanUp(item)
                htmldata = requests.get(itemUrl + item);
                soup = bs4.BeautifulSoup(htmldata.text,"lxml");
                
                #Removing this for now since its a little repetitive
                #item_proper = soup.find('h1').text.strip();
                effect = soup.find('p').text.strip();
                return effect
        
        except:
                return "No data found"


def genCode():
        result = randrange(99999999)
        length = len(str(result))
        if (length > 4):
                test =  str(result)
                testslice = slice(4)
                
                rest = test[4:]
                """Put a space after 4 digits
                ex 12345678 becomes 1234 5678"""
                list = [test[testslice], rest]
                return " ".join(list)
                
                
        
        return result
        
        
def main():
        print(getMoveData('Jet Punch'))


if __name__ == "__main__":
    main()
    
    
    
                
        
        
