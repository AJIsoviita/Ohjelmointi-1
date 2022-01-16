# TIE-02101 Ohjelmointi 1: Johdanto
# Tehtävä 6.2, Kahvigallup

from collections import Counter


def main():
    print('Enter one response per line. End by entering an empty row.')
    vastaukset = lista()
    poistetut_nollat, jlista, suurin_numero, eniten = tarkistus(vastaukset)
    if poistetut_nollat > 0:
        print('Removed {} non-coffee-drinkers responses'.format(poistetut_nollat))
    if jlista.count(jlista[0]) == len(jlista):
        print('x')
        return
    else:
        print('Information related to coffee drinkers: ')
        graafi(jlista)
        print_box(jlista, suurin_numero, eniten)

# Tämä funktio kysyy käyttäjältä gallupin tuloksia ja
# tekee syötteestä listan.


def lista():
    rivi = 1
    lista = []
    while True:
        try:
            rivi = int(input(''))
            lista.append(rivi)
        except ValueError:
            break
    return lista

# Tämä funktio laskee poistettavien nollien määrän, sekä
# suurimman, että yleisimmän vastauksen.
def tarkistus(vastaukset):
    jlista = sorted(vastaukset)
    määrä0 = jlista.count(0)
    del jlista[0:määrä0]
    suurin = max(jlista)
    eniten = max(jlista, key=jlista.count)
    return määrä0, jlista, suurin, eniten


# Funktio tulostaa jakauman, sekä lisäinformaation.

def print_box(jlista, viimeinen, eniten):
    print('The greatest response: {} cups of coffee per day'.format(viimeinen))
    print('The most common response: {} cups of coffee per day'.format(eniten))
    arvo = []
    x = 0
    a = len(jlista)
    while x < a:
        if jlista[x] > 3:
            arvo.append(jlista[x])
            x += 1
        else:
            x += 1
    jakauma = float(sum(arvo) / len(jlista))
    print('{:.1f}% of the respondents drink more than 4 cups of coffee per day'. format(jakauma))


def graafi(jlista):
    merkki = '#'
    a = len(jlista)
    x = 0
    index = 1
    index0 = 0
    o = 1
    numero = 1
    for x in range(len(jlista)):
        while jlista[index0] == jlista[index]:
            o += 1
            index += 1
            index0 += 1
            if index == a:
                break
        if jlista[x] == numero:
            print(numero, o * merkki)
        else:
            print(numero)
            numero += 1
        o = 1
        index = 1 + x
        index0 = 0 + x

        if index == a:
            break


main()
