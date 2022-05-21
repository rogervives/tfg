import webbrowser
from bs4 import BeautifulSoup
import requests
from googlesearch import search

# EXEMPLE:
# artist = "melendi"
# song = "caminando por la vida"

def buscar_webs_google(artist, song): #amb aquesta funció, buscar al buscador de google tal qual el nom i cançó
    #llista de webs posibles:
    #   lacuerda
    #   tusacordes
    #   ultimate-guitar
    #   acordesweb
    #   cifraclub

    llista_webs = ["lacuerda", "tusacordes", "ultimate-guitar", "acordesweb", "cifraclub"]

    #   Amb aixo obtinc l'ordre amb la que surten els resultats a google, aixi el millor pot ser el primer sempre.
    info = artist+" "+song+" acordes"
    resultats = search(info)
    l_resultats = [] #llista ordenada de millor a pitjor segons les cookies
    for r in resultats:
        for web in llista_webs:
            if web in r:
                l_resultats.append([web, r])

    return l_resultats

# l = buscar_webs_google(artist, song)
# print(l)

#Podria ser que apareguessin dues opcions de tusacordes, una a l'inici, i l'altre al final de les r. Tenia
#pensat fer un contador pero tampoc ho tinc molt clar.