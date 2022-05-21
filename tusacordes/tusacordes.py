from tusacordes.extreure_acords_tusacordes import extreure_acords_tusacordes

#   EXEMPLE 1:
#url = "https://www.tusacordes.com/tab/melendi-caminando_por_la_vida-acordes-46960"

def tusacordes(url):
    # Extreure el .getText() dels acords directament, hi ha mes versions pero en aquesta web apareix directe la millor.
    lletra = extreure_acords_tusacordes(url)
    return lletra.getText()

#lletra = tusacordes(url)
#print(lletra)