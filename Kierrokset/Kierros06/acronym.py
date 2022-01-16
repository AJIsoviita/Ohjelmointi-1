def create_an_acronym(syote):
    lkm = []
    lkm += syote.split(" ")
    lyhenne = ""
    for sana in lkm:
        iso = ""
        iso = sana.upper()
        kirjain = iso[0]
        lyhenne += kirjain
    return lyhenne