from gravadora_audio_auto import fes_gravacio_auto
from reconeixement_audio import reconeix_audio
from lacuerda import extreure_acords_lacuerda, escollir_acords_lacuerda, normalitzar_lacuerda

# Gravar àudio
# Reconeixement cançó
# Normalitzar
# Escollir versió d'acords
# Extreure acords

def main():
    # Gravar àudio
    # recorded_audio = fes_gravacio_auto() #Retorna la ruta del audio gravat
    # Reconeixement cançó
    #recorded_audio = "c.mp3" #r"C:\Users\roger\OneDrive\UNi\Unidara\TFG\PlanA\Repositori\shazamio\MAIN\Audios_prova\c.mp3"
    artist, song = reconeix_audio("c.mp3")
    # Normalitzar lacuerda
    url, a, s = normalitzar_lacuerda(artist, song)
    # Escollir versió d'acords
    urlversio = escollir_acords_lacuerda(url, a, s)
    # Extreure acords
    lletra_acords = extreure_acords_lacuerda(urlversio)

    print(lletra_acords)


main()
