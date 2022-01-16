"""
TIE-02101 Ohjelmointi 1
10/03/2020
Kauppakori projekti
antti-jussi.isoviita@tuni.fi, 283435
elias.kukkanen@tuni.fi, 291625
"""

DEFAULT_FILENAME = "products.txt"

def print_known_products(kaupat):
    tuotevalikoima = {}

    # Käydään kaupat läpi
    for kauppa in kaupat:

        # Käydään kaikkien kauppojen tuotteet ja hinnat
        for tuote, hinta in kaupat[kauppa].items():

            # Jos samaa tuotetta, niin ei tallenneta sitä tuotevalikoimaan.
            if tuote not in tuotevalikoima:
                tuotevalikoima[tuote] = hinta

            elif tuote in tuotevalikoima:
                if tuotevalikoima[tuote] > hinta:
                    tuotevalikoima[tuote] = hinta

    print("Available products:")
    # tulostetaan akkosjärjestyksessä tuotevalikoima
    for tuote in sorted(tuotevalikoima):
        print_price_info(tuote, tuotevalikoima[tuote])

def pick_the_products(kaupat, mitka_tuotteet):
    #poimii tuotteet kaupoista, tekee ns. kauppakorin.
    kauppakori = {}

    # kaupat läpi
    for kauppa in kaupat:
        kauppakori[kauppa] = []

        for tuote, hinta in kaupat[kauppa].items():

            # jos etsittävä tuote, niin lisätään se kauppakoriin
            if tuote in mitka_tuotteet:
                kauppakori[kauppa].append(hinta)

    return kauppakori


def find_cheapest_stores(kaupat):

    mitka_tuotteet = read_shopping_basket()
    kauppakori = pick_the_products(kaupat, mitka_tuotteet)
    halvin_kauppa, paras_hinta = calculate_basket_price(mitka_tuotteet, kauppakori)


    if len(halvin_kauppa) == 1:
        print("The cheapest price for this shopping basket: {:s} for {:.2f} e".format(halvin_kauppa[0],paras_hinta))

    elif len(halvin_kauppa) > 1:
        print("Multiple stores sell this basket for {:.2f} e:".format(paras_hinta),", ".join(halvin_kauppa))

    else:
        print("There is no store selling all those products.")

def print_selections(kaupat):
    """
        Apufunktio, joka tulostaa kauppojen hinnaston lopullisessa muodossa.
        :param kaupat: Apufunktio ottaa parametrinaan kauppakohtaisen hinnaston
        :return: Apufunktio ei palauta mitään
        """
    for kauppa in kaupat:
        print(kauppa)
        for tuote, hinta in sorted(kaupat[kauppa].items()):
            print_price_info(tuote, hinta)


def read_inputfile(filename=DEFAULT_FILENAME):
    """Fukntio lukee tiedoston, laittaa sen dictiin, joka sisältään dictin. Ulommassa dictissä kauppa tuote,
     sisimmässä tuote ja hinta.
     :param filename=DEFAULT_FILENAME: sovittu default tiedostonimi.
     :return: palauttaa dictin, jonka tekee. Sisältää kaupat, tuotteet ja hinnat
    """
    try:
        file = open(filename, 'r')
        kaupat = {}

        for rivi in sorted(file):
            kauppa, tuote, hinta = rivi.strip().split(':')

            # Sijoitetaan kaupat dictiin kaupan nimi ja hinta.
            if kauppa not in kaupat:
                kaupat[kauppa] = {}
                kaupat[kauppa][tuote] = float(hinta)
            else:
                kaupat[kauppa][tuote] = float(hinta)

        return kaupat

    except KeyError:
        print('There was an error in reading the input file!')

    except OSError:
        print('There was an error in reading the input file!')

    except ValueError:
        print('There was an error in reading the input file!')

    pass

def print_price_info(product, price):
    # Tulostaa tuotteen ja hinnan
    print("    {:<15s} {:>10.2f} e".format(product, price))


def read_shopping_basket():
    # Tallentaa listaan tuotteet, joiden hinta halutaan saada ja palauttaa tämän listan.

    print("Input product names separated by a white space:")
    tuotteet = input().split(" ")
    # Laitetaan tuotteet listaan ja palautetaan lista

    return tuotteet

def calculate_basket_price(mitka_tuotteet, kauppakori):
    """Laskee halvimman kauppakorin hinnan
    :Param: mitka_tuotteet: tuotteet, joiden hinta halutaan saada. kauppakori: Dicti, jossa avaimena kauppa,
    arvona tuotteen hinta tässä kaupassa, vain halutut tuotteet tässä dictissä.
    :Return: halvin_kauppa: lista mistä saa halvimmalla. Paras_hinta: mikä on halvin hinta.
    """

    paras_hinta = 1000000
    # Valitaan parhaaksi hinnaksi, niin suuri luku, että varmasti kauppakorin hinta on alle sen.
    halvin_kauppa = []

    for kauppa in kauppakori:

        if len(kauppakori[kauppa]) == len(mitka_tuotteet):
            # tutkitaan onko oikea määrä tuotteita

            if sum(kauppakori[kauppa]) < paras_hinta:
                # lasketaan halvimman korin hinta

                paras_hinta= sum(kauppakori[kauppa])
                halvin_kauppa.clear()
                halvin_kauppa.append(kauppa)

            elif sum(kauppakori[kauppa]) == paras_hinta:
                # Jos sama korin hinta toisessakin kaupassa
                halvin_kauppa.append(kauppa)

    return halvin_kauppa, paras_hinta

def main():

    data = read_inputfile()

    print("Welcome to the shopping basket optimization app!")
    print("Available commands:")
    print(" S Print all the [S]tores with their available products")
    print(" P Print all the [P]roducts available in all the stores")
    print(" C Show the [C]heapest seller for a specified shopping basket")
    print(" Q [Q]uit")

    while True:
        print()

        command = input("Input command (S, P, C, Q): ")

        if command == "S":
            print_selections(data)

        elif command == "P":
            print_known_products(data)

        elif command == "C":
            find_cheapest_stores(data)

        elif command == "Q":
            print("Bye!")
            return

        else:
            print("Unknown command!?!")

main()