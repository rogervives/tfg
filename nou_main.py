from gravadora.gravadora_audio_auto import gravadora_audio_auto
from reconeixement.reconeixement_a import reconeixement_audio
from buscador_google.metode_google import buscar_webs_google
from obtenir_webs_ordre import webs_per_ordre

# EXEMPLE
#artist = "melendi"
#song = "caminando por la vida"
#recorded_audio = "reconeixement/Audios_prova/d.mp3"

def main_nou():
    # Gravacio
    #recorded_audio = gravadora_audio_auto()  # Retorna la ruta del audio gravat
    #print(f"vull veure quin em dona {recorded_audio}")

    # Reconeixement
    artist, song = reconeixement_audio(recorded_audio)
    print(f"a veure que em dona de noms{artist, song}")

    # Busqueda google, obtenir links webs
    l_resultats_webs = buscar_webs_google(artist, song) #   l_resultats_webs = [[nomWEB, linkWEB]]
    print(f"webs que em dona{l_resultats_webs}")

    #       Per ordre, treballar webs:
    # lacuerda
    l_lletres = webs_per_ordre(l_resultats_webs)
    for web, lletra_web in l_lletres:
        print("AIXÒ ÉS DE: " + web + "\n\n" + lletra_web + "\n\n\n\n\n\n\n\n")
    #return print(l_lletres)

main_nou()