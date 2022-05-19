import os

def creacio_bloc_notes(artist, song): #comprovar que es guarda correctament el nom si després es canvia la caacçó
    file = open("artistsong.txt", "w")
    file.write(artist + os.linesep)
    file.write(song)
    file.close()