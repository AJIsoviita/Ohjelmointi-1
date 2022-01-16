# TIE-02100 Johdatus ohjelmointiin
# TIE-02100 Introduction to programming
# Template song b, Old MacDonald
def print_verse(eläin, ääni):
    print('Old MACDONALD had a farm')
    print('E-I-E-I-O')
    print('And on his farm he had a', eläin)
    print('E-I-E-I-O')
    print('With a', ääni, ääni, 'here')
    print('And a', ääni, ääni, 'there')
    print('Here a ', ääni,',' ' there a ', ääni, sep='')
    print('Everywhere a', ääni, ääni)
    print('Old MacDonald had a farm')
    print('E-I-E-I-O')
def main():

    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")

main()
