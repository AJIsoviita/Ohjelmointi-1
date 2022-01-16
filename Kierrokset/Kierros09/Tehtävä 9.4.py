def read_file(tiedosto):
    tiedosto = open(tiedosto, 'r')
    info = {}
    for rivi in tiedosto:
        jako = rivi.strip('').split(';')
        info[jako[0]] = {}
        info[jako[0]]['name'] = jako[1].strip('[').strip(']')
        info[jako[0]]['phone'] = jako[2].strip('[').strip(']')
        info[jako[0]]['email'] = jako[3].strip('[').strip(']')
        info[jako[0]]['skype'] = jako[4].strip('[').strip(']')
        print(jako)
    return info

read_file("contacts.csv")