from bs4 import BeautifulSoup
import requests

# import itertools

# The website from where we fetch/scrape the name of anime
url = "https://www.gogoanime.io"
response = requests.get(url)
# using bs we are kinda pretty printing the fetched page
soup = BeautifulSoup(response.text, "html.parser")
# we define an array that stores names of anime that have recently came and another array to store episode number
epnamearray = []
epnoarray = []
# we begin a loop which helps in finding all the names of anime that came recently using CSS selectors
# all websites have different way of using CSS selectors , gogoanime uses the <p> tag with name attribute
for epnames in soup.findAll('p', {"class": 'name'}):
    # we convert epnames to a string since it is a bs4 element tag
    epname = str(epnames.text)
    # appending the string of anime names into the array
    epnamearray.append(epname)

# same as above properties are applied for the episode number too
for epnos in soup.findAll('p', {"class": 'episode'}):
    epno = str(epnos.text)
    epnoarray.append(epno)

# we map the anime name and episode number together
# using the strip method because epnamearray is a list and the values in it are string
# so that we can use them as proper text we use strip method
for i in range(len(epnoarray)):
    print(epnamearray[i].strip() + "----->" + epnoarray[i])

# we make a list that contains the shows that we watch
watch_list = ["Kami no Tou", "Fruits Basket 2nd Season", "Gleipnir",
              "Kaguya-sama wa Kokurasetai?: Tensai-tachi no Renai Zunousen 2",
              "Kingdom 3rd Season", "Yesterday wo Utatte", "Toaru Kagaku no Railgun T", "Kakushigoto (TV)"]

# we compare the lists and find out what favorite anime has a new episode
for i in range(len(epnoarray)):
    if epnamearray[i] in watch_list:
        print("\033[1;34;40m" + epnamearray[i] + " has a new episode ")
