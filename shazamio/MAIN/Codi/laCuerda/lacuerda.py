import requests
import webbrowser
from normalitzar_lacuerda import normalitzar_lacuerda

song = 'Hasta la raíz'
artist = 'Natalia Lafourcade'

url = normalitzar_lacuerda(song, artist)

r = requests.get(url)
rt = r.text

LyA = rt.find('Letra y Acordes')
print(rt)
#print(url)

#webbrowser.open(url)