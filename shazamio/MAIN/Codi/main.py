from gravador_audio import gravadora
from reconeixement_audio import reconeixement
from lacuerda import normalitzar_lacuerda


# Gravar àudio
# Reconeixement cançó
# Normalitzar
# Escollir versió d'acords
# Extreure acords

def main():
    # Gravar àudio
    #recorded_audio = fes_gravacio() #Retorna la ruta del audio gravat
    # Reconeixement cançó
    recorded_audio = r"C:\Users\roger\OneDrive\UNi\Unidara\TFG\PlanA\Repositori\shazamio\MAIN\Audios_prova\a.mp3"
    artist, song = reconeix_la_canco(recorded_audio)
    # Normalitzar lacuerda
    url,a,s = normalitzar_lacuerda(song, artist)
    # Escollir versió d'acords
    urlversio = escollir_acords(url,a,s)
    # Extreure acords
    lletra_acords = extreure_acords(urlversio)
