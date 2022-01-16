# TIE-02100 Johdatus ohjelmointiin
# Koodipohja laulu c, Yogi Bear


def repeat_name(nimi, maara):
    if maara == 1:
        print(nimi, ', ', nimi, sep='')
    if maara == 3:
        print(nimi, ', ', nimi, ' Bear', sep='')
        print(nimi, ', ', nimi, ' Bear', sep='')
        print(nimi, ', ', nimi, ' Bear', sep='')
    if maara == 2:
        print(nimi, ', ', nimi, ' Bear', sep='')


def verse(sae, nimi):
    print(sae)
    repeat_name(nimi, 1)

    print(sae)
    repeat_name(nimi, 3)

    print(sae)
    repeat_name(nimi, 2)


def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


main()
