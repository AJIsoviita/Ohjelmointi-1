# Johdatus ohjelmointiin
# Parasetamol


def calculate_dose(p, a, km):
    paino = int(p)
    aika = int(a)
    määrä = int(km)
    anto = paino * 15
    if aika > 6 and määrä < 4000:
        anto = paino * 15
        if anto + määrä < 4000:
            print('The amount of Parasetamol to give to the patient: ', anto)
        if anto + määrä > 4000:
            anto = 4000 - määrä
            print('The amount of Parasetamol to give to the patient: ', anto)
    if aika < 7 and määrä < 4000:
        anto = paino * 15
        if anto + määrä < 4000:
            print('The amount of Parasetamol to give to the patient: ', anto)
        if anto + määrä > 4000:
            anto = 4000 - määrä
            print('The amount of Parasetamol to give to the patient: ', anto)



def main():
    weight = input("Patient's weight (kg): ")
    time = input("How much time has passed from the previous dose (full hours): ")
    total = input("The total dose for the last 24 hours (mg): ")

    calculate_dose(weight, time, total)


    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)

main()
