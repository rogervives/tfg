from lacuerda_nova.lacuerda_nou import lacuerda_nou

llista_webs = ["lacuerda", "tusacordes", "ultimate-guitar", "acordesweb", "cifraclub"]

def webs_per_ordre(l_resultats, artist, song):
    l_lletres = []
    for web, link in l_resultats:
        if web == "lacuerda":
            # executar extraccio per lacuerda. #ara nomes pq esta posat que es doni la primera opcio sino hi hauria mes cosa
            lletra_lacuerda = lacuerda_nou(link, artist, song)
            l_lletres.append(lletra_lacuerda)

    return l_lletres

