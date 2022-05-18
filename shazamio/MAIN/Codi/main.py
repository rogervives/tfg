from gravadora_audio_auto import gravadora_audio_auto
from reconeixement.reconeixement_a import reconeixement_audio
from lacuerda.normalitzar_lacuerda import normalitzar_lacuerda
from lacuerda.escollir_acords_lacuerda import escollir_acords_lacuerda
from lacuerda.extreure_acords_lacuerda import extreure_acords_lacuerda

def main():
    # Gravar àudio
    recorded_audio = gravadora_audio_auto() #Retorna la ruta del audio gravat
    # Reconeixement cançó
    #recorded_audio = "c.mp3" #r"C:\Users\roger\OneDrive\UNi\Unidara\TFG\PlanA\Repositori\shazamio\MAIN\Audios_prova\c.mp3"
    artist, song = reconeixement_audio(recorded_audio)
    # Normalitzar lacuerda
    url, a, s = normalitzar_lacuerda(artist, song)
    # Escollir versió d'acords
    urlversio = escollir_acords_lacuerda(url, a, s)
    # Extreure acords
    lletra_acords = extreure_acords_lacuerda(urlversio)
    return print(lletra_acords.getText())

main()

#Cwd = os.getcwd()
#print(Cwd)