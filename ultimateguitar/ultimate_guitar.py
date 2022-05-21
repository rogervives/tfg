

#   EXEMPLE 1:
#url = "https://tabs.ultimate-guitar.com/tab/melendi/caminando-por-la-vida-chords-1821361"

def tusacordes(url):
    # Extreure el .getText() dels acords directament, hi ha mes versions pero en aquesta web apareix directe la millor.
    lletra = extreure_acords_tusacordes(url)
    return lletra.getText()

#lletra = tusacordes(url)
#print(lletra)