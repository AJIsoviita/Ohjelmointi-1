# Johdatus ohjelmointiin
# Parasetamol


def calculate_dose(p, a, km):
    paino = p
    aika = a
    määrä = km
    anto = paino * 15
    if aika > 5 and määrä < 4000:
        anto = paino * 15
        if anto + määrä < 4000:
            return anto
        if anto + määrä > 4000:
            anto = 4000 - määrä
            return anto
    if aika < 6 and määrä < 4000:
        anto = 0
        return anto



def main():
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total = int(input("The total dose for the last 24 hours (mg): "))
    anto = calculate_dose(weight, time, total)
    calculate_dose(weight, time, total)
    print('The amount of Parasetamol to give to the patient:', anto)


    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)

main()
