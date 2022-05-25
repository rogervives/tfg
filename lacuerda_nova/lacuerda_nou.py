import webbrowser
from bs4 import BeautifulSoup
import requests
from lacuerda_nova.escollir_acords_lacuerda import escollir_acords_lacuerda
from lacuerda_nova.extreure_acords_lacuerda import extreure_acords_lacuerda
from lacuerda_nova.normalitzar_lacuerda import normalitzar_lacuerda_i_url

#   EXEMPLE 1
#artist = "melendi"
#song = "caminando por la vida"
#link = "https://acordes.lacuerda.net/melendi/caminando_por_la_vida"

#   EXEMPLE 2
#s = "niña voladora"
#url = "https://chords.lacuerda.net/juanito_makande/ninia_voladora"


#   En aquest arxiu.py es juntaran totes les funcions per obtenir ja els acords.
def lacuerda_nou(url):
    # Normalitzem noms (ja que lacuerda es un cas especial)
    #a, s = normalitzar_lacuerda_i_url(artist, song)
    # Escollim versió d'acords de la canco, en forma de link (cas concret d'aquesta web).
    if "shtml" in url: # el link ja és el d'una versió
        # Obtenir acords en format text.
        lletra = extreure_acords_lacuerda(url)
    else:
        versio = escollir_acords_lacuerda(url) # de moment em dona la primera opcio nomes
        # Obtenim acords en format text.
        lletra = extreure_acords_lacuerda(versio)

    return lletra.getText()

#lletra = lacuerda_nou(url)
#print(lletra)