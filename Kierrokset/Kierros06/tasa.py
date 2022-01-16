# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming

def read_message():
    rows = []
    while True:
        row = input()
        if row == "":
            break

        rows.append(row)

    return rows


def main():
    print("Enter text rows. Quit by entering an empty row.")
    msg = read_message()

    length = int(input("Enter the number of characters per line: "))
    
    words = " ".join(msg).split(" ")

    rows = []
    aggregate = []

    for word in words:
        if word == "":
            continue
        # row aggregate is "full"
        # print(len(" ".join(aggregate)), word)
        if len(" ".join(aggregate)) + len(word) + 1 > length:
            row = ""

            if len(aggregate) > 1:
                add_space = length - len(" ".join(aggregate))
                every = add_space // (len(aggregate) - 1)
                additional = add_space % (len(aggregate) - 1)

                for i in range(len(aggregate)):
                    total_space = 1 + every

                    if i < additional:
                        total_space += 1

                    row += aggregate[i] + (" " * total_space)
            else:
                row = aggregate[0]
            
            rows.append(row.strip())
            aggregate = []

        aggregate.append(word)

    rows.append(" ".join(aggregate))

    for row in rows:
        print(row)



main()
