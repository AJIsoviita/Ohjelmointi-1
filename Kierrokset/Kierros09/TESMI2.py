file = input("Enter the name of the file: ")
filename = open(file, 'r')


kategoriat = {}
for row in filename:
    name, genres = row.rstrip().split(";")
    genres = genres.split(",")

    # TODO add the info to the data structure
    for genre in genres:
        if name not in kategoriat[genre]:
            kategoriat[genre] = name
        else:
            kategoriat[genre] += name


print(kategoriat)