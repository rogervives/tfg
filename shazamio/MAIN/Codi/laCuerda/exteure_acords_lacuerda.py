from bs4 import BeautifulSoup
import csv
import webbrowser
import requests
from normalitzar_lacuerda import normalitzar_lacuerda

shtml = 'https://acordes.lacuerda.net/natalia_lafourcade/hasta_la_raiz.shtml'
shtml2 = 'https://acordes.lacuerda.net/natalia_lafourcade/hasta_la_raiz-2.shtml'
shtml3 = 'https://acordes.lacuerda.net/natalia_lafourcade/hasta_la_raiz-3.shtml'

#La idea daquest codi és, obtenir la lletra amb els acords i posarho en el meu format.
def extreure_acords_lacuerda(shtml):
    shtmlpage = requests.get(shtml)
    soup = BeautifulSoup(shtmlpage.text, 'html.parser')
    #print(soup)

    lletra = soup.find('div', {'id': "t_body"})
    print(lletra.getText())

extreure_acords_lacuerda(shtml2)