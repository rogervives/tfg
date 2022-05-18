import asyncio
from shazamio import Shazam
#from creacio_bloc_notes import creacio_bloc_notes
#from obtenir_noms_notes import obtenir_noms_notes
import os
import json
from pprint import pprint as pp

def reconeixement_audio(recording_path):
    async def reconeixement_main(recording_path):  # recording_path=None
        shazam = Shazam()
        out = await shazam.recognize_song(recording_path)
        song = out['track']['title']
        artist = out['track']['subtitle']
        creacio_bloc_notes(artist, song)
        # print(song+'\n'+artist)
        # pp(out) #sha de posar nomes el pp(out), sense json, pq quedi amb bona vista
    loop = asyncio.get_event_loop()
    loop.run_until_complete(reconeixement_main(recording_path))
    artist, song = obtenir_noms_notes("artistsong.txt")
    return artist, song

def creacio_bloc_notes(artist, song): #comprovar que es guarda correctament el nom si després es canvia la caacçó
    file = open("artistsong.txt", "w")
    file.write(artist + os.linesep)
    file.write(song)
    file.close()

def obtenir_noms_notes(file):
    l_linies = []
    with open(file, "r") as arxiu:
        for linia in arxiu:
            l_linies.append(linia)
    artist = l_linies[0]
    song = l_linies[2]
    artist = artist.rstrip()
    song = song.rstrip()
    return artist, song

#artist, song = reconeixement_audio("f.mp3")
#print(artist, song)

