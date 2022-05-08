from bs4 import BeautifulSoup
import csv
import webbrowser
import requests
from normalitzar_lacuerda import normalitzar_lacuerda

song = 'Hasta la raíz'
artist = 'Natalia Lafourcade'
url,a,s = normalitzar_lacuerda(song, artist)

urlpage = requests.get(url)
soup = BeautifulSoup(urlpage.text, 'html.parser')

#print(urlpage.text)
#print(url)

#haig d'agafar tots els href, és on estan els links per les opcions d'acords.
opcions = soup.find_all('a')
llista_links = []
for o in opcions:
    #print(o)
    link = o.get('href')
    if type(link) == str:
        if 'shtml' in link:
            link = link[len(s):]
            llista_links.append(link)
print(llista_links)

for i in llista_links:
    webbrowser.open(url+i)
#print(llista_opcions)
#print(len(llista_opcions))