from bs4 import BeautifulSoup
import csv
import webbrowser
import requests

#sublink = "https://www.tusacordes.com/tab/melendi-caminando_por_la_vida-acordes-46960"

def extreure_acords_tusacordes(sublink):
    sublink_page = requests.get(sublink)
    soup = BeautifulSoup(sublink_page.text, 'html.parser')
    #print(soup)

    lletra = soup.find('pre', {'id': "cantxt"})
    #lletra = soup.find("pre")
    return lletra

#lletra = extreure_acords_tusacordes(sublink)
#print(lletra.getText())