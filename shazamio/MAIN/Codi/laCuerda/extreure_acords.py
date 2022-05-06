from bs4 import BeautifulSoup
import csv
import requests
from normalitzar_lacuerda import normalitzar_lacuerda

song = 'Hasta la raíz'
artist = 'Natalia Lafourcade'
url = normalitzar_lacuerda(song, artist)

urlpage = requests.get(url)
soup = BeautifulSoup(urlpage.text, 'html.parser')

#print(urlpage.text)
#print(url)

#haig d'agafar tots els href, és on estan els links per les opcions d'acords.
opcions = soup.find_all('a')
llista_opcions = []
for o in opcions:
    if 'Letra y acordes' in o:
        llista_opcions.append(o)
    print(llista_opcions)
#print(llista_opcions)
#print(len(llista_opcions))