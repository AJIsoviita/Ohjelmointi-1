def main():
    rivi = int(input('Enter the number of the measurements: '))
    if rivi < 1:
        print('Error: the number must be expressed as a positive integer.')
    else:
        rivi1 = 0
        rivi2 = 1
        summa = 0
        ph1 = 7
        while rivi1 < rivi:
            ph = float(input('Enter the measurement result {:1d}: '.format(rivi2)))
            rivi1 = rivi1 + 1
            rivi2 = rivi2 + 1
            ph2 = ph1 - ph
            ph3 = ph - ph1
            if 8 < ph or 6 > ph:
                print('The conditions are not suitable for zebra fishes.')
                break
            if -1 > ph2 or ph2 > 1 or -1 > ph3 or ph3 > 1:
                print('The conditions are not suitable for zebra fishes.')
                break
            ph1 = ph
            summa = summa + ph
            if rivi1 == rivi:
                average = summa / rivi1
                print('Conditions are suitable for zebra fishes. The average pH is {:.2f}.'.format(average))


main()