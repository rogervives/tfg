# EXEMPLE:


def opcions_per_escollir(l_lletres):
    inf = 0
    while inf == 0:
        for n, web, lletra_web in l_lletres:
            print("\n"+n + ") " + web)

        n_opcio = input("Escollir opció: ")

        for n, web, lletra_web in l_lletres:
            if n_opcio == n:
                print("\nNom de la WEB: "+web+"\n"+lletra_web)
                break #pq ja pari de fer el for en el que està. Em pararà el while també? No crec.

        nova_opcio = input("\nPrémer intro per escollir una nova opció: ")
        if nova_opcio == "":
            pass
        elif nova_opcio == "stop":
            inf += 1