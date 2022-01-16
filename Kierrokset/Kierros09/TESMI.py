def main():
    file = input("Enter the name of the file: ")
    filename = open(file, 'r')
    genrelista = []
    for rivi in filename:
        jako = rivi.strip().split(';')
        genret = jako[1].strip().split(',')
        for i in genret:
            x = 0
            while x < len(genret):
                if i == genret[x] and genrelista.count(i) == 0:
                    genrelista.append(i)
                    break
                else:
                    x += 1
    genrelista = sorted(genrelista)
    print('Available genres are: ', ', '.join(genrelista))
main()