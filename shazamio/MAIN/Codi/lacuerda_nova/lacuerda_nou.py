import webbrowser
from bs4 import BeautifulSoup
import requests
from escollir_acords_lacuerda import escollir_acords_lacuerda
from extreure_acords_lacuerda import extreure_acords_lacuerda
from normalitzar_lacuerda import normalitzar_lacuerda_i_url

#   EXEMPLE
#artist = "melendi"
#song = "caminando por la vida"
#link = "https://acordes.lacuerda.net/melendi/caminando_por_la_vida"

#   En aquest arxiu.py es juntaran totes les funcions per obtenir ja els acords.
def lacuerda_nou(link, artist, song):
    # Normalitzem noms (ja que lacuerda es un cas especial)
    a, s = normalitzar_lacuerda_i_url(artist, song)
    # Escollim versió d'acords de la canco, en forma de link (cas concret d'aquesta web).
    versio = escollir_acords_lacuerda(link, s) # de moment em dona la primera opcio nomes
    # Obtenim acords en format text.
    lletra = extreure_acords_lacuerda(versio)

    return lletra.getText()

#lacuerda_nou(link, artist, song)