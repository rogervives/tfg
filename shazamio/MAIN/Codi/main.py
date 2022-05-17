from gravadora_audio_auto import fes_gravacio_auto
import reconeixement_audio
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
    recorded_audio = r"C:\Users\roger\OneDrive\UNi\Unidara\TFG\PlanA\Repositori\shazamio\MAIN\Audios_prova\c.mp3"
    artist, song = reconeixement_audio(recorded_audio)
    # Normalitzar lacuerda
    url, a, s = normalitzar_lacuerda(artist, song)
    # Escollir versió d'acords
    urlversio = escollir_acords_lacuerda(url, a, s)
    # Extreure acords
    lletra_acords = extreure_acords_lacuerda(urlversio)

    print(lletra_acords)


main()
