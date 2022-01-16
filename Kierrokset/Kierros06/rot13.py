# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ROT13, program code template


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


def row_encryption(sentence):
    muunnos=[]
    for kirjain in range(len(sentence)):
        muunnos += encrypt(sentence[kirjain])
    lst = ''.join(muunnos)
    return lst

row_encryption("Happy, happy, joy, joy!")