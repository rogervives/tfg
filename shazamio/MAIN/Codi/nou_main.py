from buscador_google.metode_google import buscar_webs_google
from obtenir_webs_ordre import webs_per_ordre

# EXEMPLE
artist = "melendi"
song = "caminando por la vida"

def main_nou():
    # Gravacio
    #recorded_audio = gravadora_audio_auto()  # Retorna la ruta del audio gravat

    # Reconeixement
    #artist, song = reconeixement_audio(recorded_audio)

    # Busqueda google, obtenir links webs
    l_resultats_webs = buscar_webs_google(artist, song) #   l_resultats_webs = [[nomWEB, linkWEB]]

    #       Per ordre, treballar webs:
    # lacuerda
    l_lletres = webs_per_ordre(l_resultats_webs, artist, song)
    return print(l_lletres)

main_nou()