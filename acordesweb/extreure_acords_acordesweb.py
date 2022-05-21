from bs4 import BeautifulSoup
import requests

#   EXEMPLE 1:
#sublink = "https://acordesweb.com/cancion/melendi/caminando-por-la-vida"

#   EXEMPLE 2:
#sublink = "https://acordesweb.com/cancion/wos/arrancarmelo"

def extreure_acords_acordesweb(sublink):
    sublink_page = requests.get(sublink)
    soup = BeautifulSoup(sublink_page.text, 'html.parser')
    print(soup)

    # linia_horitzontal = soup.find('pre', {'id': "acorde"})
    # print(f"A veure que em dona la linia horitzintal: {linia_horitzontal}")

    # lletra_sencera_h = ""
    # for i in linia_horitzontal:
    #     lletra_sencera_h = i
    #
    # lletra = lletra_sencera_h.get_text("br")
    # l = lletra.split("br")
    # for i in l:
    #     #i = i.replace(u'\xa0', u' ')
    #     print(i)
    #print(lletra)
    #print(type(lletra))
    #   Intento obtenir la lletra en el format que vull

    #
    # lletra_sencera_h_str = lletra_sencera_h.getText()
    # l_lletra = lletra_sencera_h_str.split(" ")
    #
    # for i in l_lletra:
    #     print(i+"\n")
    #print(linia_horitzontal)

    #print(lletra)
    #return lletra

#extreure_acords_acordesweb(sublink)
#lletra = extreure_acords_acordesweb(sublink)
#print(lletra.getText())