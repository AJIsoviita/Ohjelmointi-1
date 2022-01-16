import traceback, sys

def main():
    tiedoston_nimi = input('Enter the name of the score file: ')
    try:
        tiedosto = open(tiedoston_nimi, "r")
        pistetilanne = {}
        lista = []
        for i in tiedosto:
            i = i.rstrip()
            jako = i.split()
            pisteet = int(jako[1])
            if jako[0] in pistetilanne:
                pistetilanne[jako[0]].append(jako[1])
            else:
                pistetilanne[jako[0]] = [jako[1]]

        for nimi in pistetilanne:
            summa = 0
            for x in range(len(pistetilanne[nimi])):
                y = int(pistetilanne[nimi][x])
                summa += y
            pistetilanne[nimi] = summa

        print('Contestant score: ')
        for a, b in sorted(pistetilanne.items()):
            print(a, b)

    except OSError:
        print('There was an error in reading the file.')
    except IndexError:
        print('There was an erroneous line in the file:')
        print(''.join(jako))
    except ValueError:
        print('There was an erroneous score in the file:')
        print(''.join(jako[1]))
main()