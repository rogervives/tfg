from lacuerda_nova.lacuerda_nou import lacuerda_nou
from tusacordes.tusacordes import tusacordes
from cifraclub.cifraclub import cifraclub

llista_webs = ["lacuerda", "tusacordes", "ultimate-guitar", "acordesweb", "cifraclub"]
#l_resultats = [['lacuerda', 'https://chords.lacuerda.net/melendi/caminando_por_la_vida'], ['cifraclub', 'https://www.cifraclub.com.br/melendi/caminando-por-la-vida/'], ['tusacordes', 'https://www.tusacordes.com/tab/melendi-caminando_por_la_vida-acordes-46960'], ['acordesweb', 'https://acordesweb.com/cancion/melendi/caminando-por-la-vida'], ['ultimate-guitar', 'https://tabs.ultimate-guitar.com/tab/melendi/caminando-por-la-vida-chords-1821361']]

def webs_per_ordre(l_resultats):
    l_lletres = []
    for web, link in l_resultats:
        if web == "lacuerda":
            # executar extraccio per lacuerda. #ara nomes pq esta posat que es doni la primera opcio sino hi hauria mes cosa
            lletra_lacuerda = lacuerda_nou(link)
            l_lletres.append([web, lletra_lacuerda])
        elif web == "tusacordes":
            lletra_tusacordes = tusacordes(link)
            l_lletres.append([web, lletra_tusacordes])
        elif web == "cifraclub":
            lletra_cifraclub = cifraclub(link)
            l_lletres.append([web, lletra_cifraclub])

    return l_lletres

#l_lletres = webs_per_ordre(l_resultats)
#for web, lletra in l_lletres:
#    print("AIXÒ ÉS DE: "+web+"\n\n"+lletra+"\n\n\n\n\n\n\n\n")

