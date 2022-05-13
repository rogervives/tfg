import asyncio
from shazamio import Shazam
import json
from pprint import pprint as pp


'''
RECONEIXEMENT DE L'ÀUDIO
'''
def reconeixement():
    async def reconeixement_main():
        shazam = Shazam()
        out = await shazam.recognize_song('b.mp3')
        song = out['track']['title']
        artist = out['track']['subtitle']
        print(song+'\n'+artist)
        #pp(out) #sha de posar nomes el pp(out), sense json, pq quedi amb bona vista

    loop = asyncio.get_event_loop()
    loop.run_until_complete(reconeixement_main())

'''
ENVIAR NOM DE ARTISTA I CANÇÓ
'''


