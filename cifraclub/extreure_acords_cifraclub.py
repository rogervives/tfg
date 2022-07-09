from bs4 import BeautifulSoup
import csv
import webbrowser
import requests

#   EXEMPLE 1:
#sublink = "https://www.cifraclub.com.br/melendi/caminando-por-la-vida/"

def extreure_acords_cifraclub(sublink):
    sublink_page = requests.get(sublink)
    soup = BeautifulSoup(sublink_page.text, 'html.parser')
    #print(soup)

    #   EXTREURE paràmetres a tenir en compte per llegir correctament la cançó:
    #tono = soup.find("span", {"id": "cifra_tom"})
    #tono = tono.getText()

    #tuning = soup.find("span", {"data-cy": "song-tuning"})
    #tuning = tuning.getText()

    #capo = soup.find("span", {"data-cy": "song-capo"})
    #capo = capo.getText()

    lletra = soup.find("pre")
    lletra = lletra.getText()

    # print(tono.getText(), end =" ")#+" "+tuning.getText())
    # print(tuning.getText())
    # print(capo.getText())
    # print(lletra.getText())

    #   S'ha de tenir en compte si tindrà capo o no:
    # if "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15" in capo:
    #     lletra_amb_tot = tono + "\n" + tuning + "\n" + "Capo: " + capo + "\n" + lletra
    # else:
    #     lletra_amb_tot = tono + "\n" + tuning + "\n" + lletra

    #lletra_amb_tot = "\n" + tuning + "\n" + "Capo: " + capo + "\n" + lletra

    return lletra

#extreure_acords_cifraclub(sublink)
#lletra = extreure_acords_cifraclub(sublink)
#print(lletra)