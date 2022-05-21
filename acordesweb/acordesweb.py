

#   EXEMPLE 1:
#url = "https://acordesweb.com/cancion/melendi/caminando-por-la-vida"

def acordesweb(url):
    # Extreure el .getText() dels acords directament, hi ha mes versions pero en aquesta web apareix directe la millor.
    lletra = extreure_acords_acordesweb(url)
    return lletra.getText()

#lletra = acordesweb(url)
#print(lletra)