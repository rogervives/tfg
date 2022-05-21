from bs4 import BeautifulSoup
import requests

#   EXEMPLE 1:
sublink = "https://tabs.ultimate-guitar.com/tab/melendi/caminando-por-la-vida-chords-1821361"

def extreure_acords_ultimateguitar(sublink):
    sublink_page = requests.get(sublink)
    soup = BeautifulSoup(sublink_page.text, 'html.parser')
    #print(soup)

    linia_lletra = soup.find('div', {'class': "js-store"})
    linia_lletra = linia_lletra.find("content&quot")
    print(linia_lletra)

    #lletra = linia_lletra.findAll("data-content")
    #return lletra

extreure_acords_ultimateguitar(sublink)
#lletra = extreure_acords_ultimateguitar(sublink)
#print(lletra.getText())
#print(lletra)
