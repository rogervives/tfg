from cifraclub.extreure_acords_cifraclub import extreure_acords_cifraclub

#   EXEMPLE 1:
#url = "https://www.cifraclub.com.br/melendi/caminando-por-la-vida/"

def cifraclub(url):
    #   Extreure acords de la web
    lletra_str = extreure_acords_cifraclub(url)
    return lletra_str

#lletra = cifraclub(url)
#print(lletra)
