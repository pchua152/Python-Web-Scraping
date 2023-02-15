import requests
import bs4

rootUrl = "https://pokemondb.net/move/"
monUrl = "https://pokemondb.net/pokedex/"
abilityUrl = "https://pokemondb.net/ability/"
itemUrl = "https://pokemondb.net/item/"

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
        #Retrieve data
        data = "" 
        try:
                attack = textCleanUp(attack)
                htmlData = requests.get(rootUrl + attack)
                soup = bs4.BeautifulSoup(htmlData.text, "lxml")
                #The website has them so you can search based off attack
                #Find just the tbale that has the info
                table = soup.find('table', class_ = "vitals-table");
                
                #Print all the data about it
                for row in table.tbody.find_all('tr'):
                        column = row.find_all('th')
                        info = row.find_all('td')
                        if column[0].text.strip() not in ["Introduced"]:
                                data += column[0].text.strip() + ": " + info[0].text.strip() + " \n";
                
                #Commenting this out for now cause its a little buggy
                effect = soup.find('h2',{"id": "move-effects"}).text.strip();
                move = soup.find('p').text.strip()
                
                
                data += effect + ": " +  move
                return data
        except:
                return "No data found"
        
        
        
       
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
               
      


def getPokemonData(pokemon):
        ##What data should be received?
        data = ""
        try:
        ##Type/Height/Weight/Abilites
        ##Stats
                pokemon = textCleanUp(pokemon)
                htmldata = requests.get(monUrl + pokemon);
                soup = bs4.BeautifulSoup(htmldata.text, "lxml");
                ##Type/Height/Weight/Abilites
                table = soup.find('table', class_ = "vitals-table");
                for row in table.tbody.find_all('tr'):
                        column = row.find('th')
                        info = row.find('td')
                        column_name = column.text.strip();
                        ##Irrelevant information will not be output
                        if column_name not in ['National №', 'Species', 'Local №']:
                                ##Make the abilities better formated when printed
                                if column_name == "Abilities":
                                        abilities = []
                                        for ability in row.find_all('a'):
                                                abilities.append(ability.text.strip()); 
                                        
                                        data += "Abilities: " + str(abilities) + "\n";
                                else:
                                        data += column.text.strip() + ": " +  info.text.strip() + "\n"
                
                data += "\n \nBase Stats: "
                table2 = soup.find('div',class_ = "resp-scroll" );
                for row in table2.tbody.find_all('tr'):
                        column = row.find('th').text.strip()
                        bs = row.find('td', class_ = "cell-num").text.strip();
                        data += column + ": "+ bs + "\n";
                return data
        except:
                return "No data found, if Pokemon intended to search for is Nidoran, type Nidoran-m or Nidoran-f"
        
        
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

def main():
        print(getItemData("Booster Energy"))
        print(getMoveData("Headlong Rush"))
        print(getAbilityData("Own Tempo"))
        print(getPokemonData("Quagsire"))


if __name__ == "__main__":
    main()
                
        
        
