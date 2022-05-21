from bs4 import BeautifulSoup
import csv
import webbrowser
import requests
from lacuerda_nova.extreure_nom_song_lacuerda import extreure_song_link_lacuerda

# EXEMPLE 1:
#s = "caminando_por_la_vida"
#url = "https://acordes.lacuerda.net/melendi/caminando_por_la_vida"

#EXEMPLE 2:
#s = "niña_voladora"
#url = "https://chords.lacuerda.net/juanito_makande/ninia_voladora"

def escollir_acords_lacuerda(url):
    #   Obtenir nom de la cançó tal i com està al link de lacuerda.
    s = extreure_song_link_lacuerda(url)

    #   Preparar informació per poder treballar amb ella.
    urlpage = requests.get(url)
    soup = BeautifulSoup(urlpage.text, 'html.parser')
    #print(urlpage.text)
    #print(url)

    #   Obtenir els links de les opcions disponibles d'acords.
    opcions = soup.find_all('a')
    l_shtml = []
    for o in opcions:
        #print(o)
        link = o.get('href')
        if type(link) == str:
            if 'shtml' in link:
                link = link[len(s):]
                l_shtml.append(link)
    #print(l_shtml)

    l_opcions = []
    for i in l_shtml:
        l_opcions.append(url+i)
    #print(l_opcions)
    #print(llista_opcions)
    #print(len(llista_opcions))

    #   Extreure tots els acords que s'utilitzen per poder escollir, és només una previsualització.
    #acords = soup.find_all('pre')
    #for a in acords:
        #print(a)
    #print(acords[0])
    #print(type(opcions))

    #   Escull directament la canco 1
    return l_opcions[0]

    #   Input per escollir la opció.
    #   Es podria posar que et dones directament els acords si només hi ha una opció????????????
    #print('Opcions disponibles')
    #contador = 0
    #for i in l_opcions:
    #    contador += 1
    #    print(contador)
    #opcio = input('Escriu quina opció vols: ')
    #webbrowser.open(l_opcions[int(opcio)-1])

#link_versio = escollir_acords_lacuerda(url)
#print(link_versio)