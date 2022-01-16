def main():
    tiedoston_nimi = input('Enter the name of the file: ')
    try:
        tiedosto = open(tiedoston_nimi,'r')
        kuitti = {}
        koko_summa = 0
        henkilö_määrä = 0
        henkilön_ostokset = {}

        for rivi in tiedosto:
            kulu = 0
            jako = rivi.split(':')
            kulu = jako[1].strip('')
            if jako[0] in kuitti:
                kuitti[jako[0]].append(kulu)
            else:
                kuitti[jako[0]] = [kulu]
                henkilön_ostokset[jako[0]] = [kulu]
                henkilö_määrä += 1
            koko_summa += float(kulu)

        for nimi in sorted(kuitti):
            summa = 0
            for i in range(len(kuitti[nimi])):
                x = float(kuitti[nimi][i])
                y = str(kuitti[nimi][i])
                henkilön_ostokset[nimi].append("{:.2f}".format(x))
                summa += x
            kuitti[nimi] = summa
            del henkilön_ostokset[nimi][0]

        print("Total costs: {:.2f}e".format(koko_summa))
        print('')

        tasattu_osuus = koko_summa/henkilö_määrä

        for maksaja, määrä in sorted(kuitti.items()):
            print(maksaja, "has paid {:.2f} in the following amounts:".format(määrä),", ".join(henkilön_ostokset[maksaja]))

            raha = float(tasattu_osuus - määrä)
            if abs(raha) > 0.05:
                if raha < 0.05:
                    print(maksaja, 'needs to receive {:.2f}e.'.format(abs(raha)))
                    print('')
                else:
                    print(maksaja, 'needs to pay {:.2f}e.'.format(abs(raha)))
                    print('')
            else:
                print('No transfers needed.')

    except OSError:
        print("Error: file", tiedoston_nimi, " cannot be read.")
    except ValueError:
        print("Error: there was an erroneous line in the file.")
    except IndexError:
        print("Error: there was an erroneous line in the file.")
main()