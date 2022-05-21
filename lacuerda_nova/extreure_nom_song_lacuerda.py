'''
Aquest arxiu és per extreure el nom amb el que esta la canço a lacuerda.net i així no hi hagi errors.
Ja que de vegades no hi ha el mateix nom al shazam que a lacuerda.net.
'''

# EXEMPLE:
#url = "https://chords.lacuerda.net/juanito_makande/ninia_voladora"

def extreure_song_link_lacuerda(url):
    l = url.split("/") #separo el link a partir de les / que tenen iguals tots els links, i creo una llista,
                    # l'últim valor de la llista  sera el nom de la song que vull (de la manera en la que la vull).
                    # me la dona amb guions i tot en cada espai.
    return l[-1]

#song = extreure_song_link_lacuerda(url)
#print(song)