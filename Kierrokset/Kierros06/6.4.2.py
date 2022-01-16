def create_an_acronym(nimi):
    nimi2 = nimi.split()
    list = []
    for x in range((len(nimi2))):
        list.append(nimi2[x][0])
    lst = ''.join(list)
    return lst.upper()

create_an_acronym("central intelligence agancy")