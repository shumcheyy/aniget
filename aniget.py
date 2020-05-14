from bs4 import BeautifulSoup
import requests

url = "https://www.gogoanime.io"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
epnamearray = []
epnoarray = []
for epnames in soup.findAll('p',{"class":'name'}):
    epname = str(epnames.text)
    epnamearray.append(epname)

    #print(epname)

for epnos in soup.findAll('p',{"class":'episode'}):
    epno = str(epnos.text)
    epnoarray.append(epno)
    #print(epno)


for i in range(len(epnoarray)):
    print(epnamearray[i].strip() + "----->" + epnoarray[i])

