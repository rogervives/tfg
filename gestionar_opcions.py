# EXEMPLE:


def opcions_per_escollir(l_lletres):
    inf = 2
    while inf > 1:
        for n, web, lletra_web in l_lletres:
            print("\n\n\n"+n + ") " + web)

        n_opcio = input("Escollir opció: ")

        for n, web, lletra_web in l_lletres:
            if n_opcio == n:
                print("\n\n\n\nNom de la WEB: "+web+"\n\n"+lletra_web)
                break #pq ja pari de fer el for en el que està. Em pararà el while també? No crec.

        nova_opcio = input("\n\n\n\nPrémer intro per escollir una nova opció: ")
        if nova_opcio == "":
            pass
        elif nova_opcio == "stop":
            break