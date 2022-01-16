# Ohjelmointi 1
# Antti-Jussi Isoviita 283435
# Tekstin tasaus


def main():
    viesti = read_input()
    pituus = rivin_pituus()

    rivit = []
    teksti = []

    lista = " ".join(viesti).split(" ")
    tekstin_pituus = " ".join(teksti)

    for sana in lista:

        if sana == "":
            continue

        if len(" ".join(teksti)) + len(sana) + 1 > pituus:
            rivi = ""

            if len(teksti) > 1:
                lisää_väli = pituus - len(" ".join(teksti))
                paikka = lisää_väli // (len(teksti) - 1)
                ylim = lisää_väli % (len(teksti) - 1)

                for i in range(len(teksti)):
                    kokonaismäärä = 1 + paikka

                    if i < ylim:
                        kokonaismäärä += 1

                    rivi += teksti[i] + (" " * kokonaismäärä)
            else:
                rivi = teksti[0]

            rivit.append(rivi.strip())
            teksti = []

        teksti.append(sana)

    rivit.append(" ".join(teksti))

    for rivi in rivit:
        print(rivi)


def read_input():
    print('Enter text rows. Quit by entering an empty row.')
    lista = []
    viesti = 0
    while viesti != '':
        viesti = input('')
        lista.append(viesti)
    del lista[-1]

    return lista


def rivin_pituus():
    n = int(input('Enter the number of characters per line: '))
    return n


main()