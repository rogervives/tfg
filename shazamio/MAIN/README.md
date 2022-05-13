### Etapes:

1) Capturar àudio:
   - Gravadora manual.
    ##### `gravadora_audio.py`  

2) Reconeixement. Enviar Shazam i processar informació Shazam:
    - Mètode shazamio. Utilitzar API shazamio.
    - Obtenir nom artista i cançó.
   ##### `reconeixement_audio.py`

3) Normalitzar format nom artista i cançó depenent de la web:
   - laCuerda
      ##### `normalitzar_lacuerda.py`
     1) Escollir versió d'acords (si n'hi ha).
        ##### `escollir_acords_lacuerda.py`
     2) Extreure acords:
     - Obtenir els acords en un cert format.
     - Obtenir les imatges de la posició dels dits dels acords.
        ##### `extreure_acords_lacuerda.py`