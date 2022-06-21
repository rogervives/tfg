from bs4 import BeautifulSoup
import csv
import webbrowser
import requests

#shtml = 'https://acordes.lacuerda.net/natalia_lafourcade/hasta_la_raiz.shtml'
#shtml2 = 'https://acordes.lacuerda.net/natalia_lafourcade/hasta_la_raiz-2.shtml'
#shtml3 = 'https://acordes.lacuerda.net/natalia_lafourcade/hasta_la_raiz-3.shtml'

#La idea daquest codi és, obtenir la lletra amb els acords i posarho en el meu format.
def extreure_acords_lacuerda(shtml):
    shtmlpage = requests.get(shtml)
    soup = BeautifulSoup(shtmlpage.text, 'html.parser')
    #print(soup)

    #< div class ="chordTit" > Cm < / div >
    #acorde = soup.find("div", {"class": "chordTit"})
    #print(acorde)

    #<div title="Cm" onclick="toolDiag.chordStart(this)" class="fretVer" id="fretAco0"><div class="cejillaV" style="margin-top:1.571em"></div><span class="spanV">3</span><div class="cruzV">×</div><div class="alaireV">&nbsp;</div><div class="dedoV" style="margin-top:8.35em">3</div><div class="dedoV" style="margin-top:8.35em">4</div><div class="dedoV" style="margin-top:5.6em">2</div><div class="alaireV">&nbsp;</div></div>
    # Cm = soup.find("div", {"title": "Cm"})
    # print(Cm)

    lletra = soup.find('div', {'id': "t_body"})
    return lletra

#extreure_acords_lacuerda(shtml)
#lletra = extreure_acords_lacuerda(shtml)
