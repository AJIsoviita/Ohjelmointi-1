# TIE-02100 Johdatus ohjelmointiin
# Read genres and tv-series from a file into a dict.
# Print a list of the genres in alphabetical order
# and list tv-series by given genre on user's command.


def read_file(filename):
    # reads and saves the series and their genres from the file

    # TODO initialize a new data structure
    kategoriat = {}

    try:
        file = open(filename, "r")

        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")

            # TODO add the info to the data structure
            for genre in genres:
                kategoriat[genre] = name
        file.close()
        return kategoriat

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():

    filename = input("Enter the name of the file: ")
    guide = read_file(filename)

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

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        # TODO print the series ...
    for ohjelma in genre:
        print(ohjelma)


main()
