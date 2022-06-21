import asyncio
from shazamio import Shazam
from reconeixement.creacio_bloc_notes import creacio_bloc_notes
from reconeixement.obtenir_noms_notes import obtenir_noms_notes
import os
import json
from pprint import pprint as pp


def reconeixement_audio(recording_path):
    #song = ""
    #artist = ""
    async def reconeixement_main(recording_path):#, artist, song):  # recording_path=None
        shazam = Shazam()
        out = await shazam.recognize_song(recording_path)
        song = out['track']['title']
        artist = out['track']['subtitle']
        creacio_bloc_notes(artist, song)
        #print(song+'\n'+artist)
        # pp(out) #sha de posar nomes el pp(out), sense json, pq quedi amb bona vista
    loop = asyncio.get_event_loop()
    loop.run_until_complete(reconeixement_main(recording_path))
    artist, song = obtenir_noms_notes("artistsong.txt")
    return artist, song

#artist, song = reconeixement_audio("Audios_prova/h.mp3")
#print(artist, song)

