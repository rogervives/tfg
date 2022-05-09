def normalitzar_lacuerda(song, artist): #aquesta funcio normalitza els noms adaptant-los al format web laCuerda i
    # retorna la url la cual sha de buscar.
    song = song.lower()
    artist = artist.lower()

    def normalize(z): #posar que elemini també els caracters especials??????????
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
    return url,a,s
