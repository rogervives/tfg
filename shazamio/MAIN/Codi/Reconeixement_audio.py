import asyncio
from shazamio import Shazam
import json
from pprint import pprint as pp


'''
RECONEIXEMENT DE L'ÀUDIO
'''
def reconeixement_audio(recording_path: str): # -> str, str:
    async def reconeixement_main(recording_path=None):
        shazam = Shazam()
        out = await shazam.recognize_song(recording_path)
        song = out['track']['title']
        artist = out['track']['subtitle']
        #print(song+'\n'+artist)
        return artist, song
        #pp(out) #sha de posar nomes el pp(out), sense json, pq quedi amb bona vista

    loop = asyncio.get_event_loop()
    loop.run_until_complete(reconeixement_main())

'''
ENVIAR NOM DE ARTISTA I CANÇÓ
'''


