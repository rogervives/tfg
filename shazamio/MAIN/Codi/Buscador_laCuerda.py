import requests

song = 'Hasta la raíz'
artist = 'Natalia Lafourcade'

def normalitzar_nom_laCuerda(song, artist): #aquesta funcio normalitza els noms adaptant-los al format web laCuerda i
    # retorna la url la cual sha de buscar.
    song = song.lower()
    artist = artist.lower()

    def normalize(z):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
            ("ò", "o"),
            ("è", "e"),
            ("à", "a"),
            ("ï", "i"),
            ("ü", "u"),
        )
        for a, b in replacements:
            z = z.replace(a, b).replace(a.upper(), b.upper())
        return z

    song = normalize(song)
    artist = normalize(artist)

    song = song.split()
    artist = artist.split()

    s = ''
    a = ''

    for e in song:
        s = s+'_'+e
    for e in artist:
        a = a+'_'+e

    if s[0] == '_':
        s = s[1:]
    if a[0] == '_':
        a = a[1:]
    
    url = 'https://acordes.lacuerda.net/'+a+'/'+s



r = requests.get(url)
rt = r.text
# Utilitzar la funcion find per trobar la part on posa Letra y acordes, les
# vegades que faci falta. Pero i si a la lletra hi ha aquestes paraules exactes?
# el programa o codi es podria conforndre.
# I si la pàgina es tradueix a un altre idioma?

#LyA = rt.find('Letra y Acordes')
#print(rt[0])
#print(url)

import webbrowser
webbrowser.open(url)

