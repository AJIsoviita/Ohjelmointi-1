# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: viesti, program code template


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    lst = row_encryption(msg)
    print("The same, shouting:")
    for x in range(len(msg)):
        print(lst[x].upper())

def read_message():
    lista = []
    viesti = 0
    while viesti != '':
            viesti = input('')
            lista.append(viesti)
    del lista[-1]
    return lista

def encrypt(alphabet):
    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    # Implement encryption here
    for kirjain in range(len(regular_chars)):
        if alphabet == regular_chars[kirjain]:
            alphabet = encrypted_chars[kirjain]
            return alphabet
        if alphabet.upper() == regular_chars[kirjain].upper():
            alphabet = encrypted_chars[kirjain].upper()
            return alphabet
    else:
        return alphabet


def row_encryption(lista):
    muunnos=[]
    sentence = read_message()
    for kirjain in range(len(sentence)):
        muunnos += encrypt(sentence[kirjain])
    lst = ''.join(muunnos)
    print(lst)
    return lst

main()
