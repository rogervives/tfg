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