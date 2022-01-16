def main():
    tiedoston_nimi = input('Enter the name of the file: ')
    tiedosto = open(tiedoston_nimi, "r")
    x = 1
    for i in tiedosto:
        i = i.rstrip()
        print(x, i)
        x += 1
    tiedosto.close()

main()