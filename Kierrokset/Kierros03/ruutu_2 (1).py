# Johdatus ohjelmointiin
# Print a box with input checking


def read_input(k):
    answer = -1
    while answer < 1:
        answer = int(input(k))
    return answer


def print_box(leveys,korkeus,merkki):
    w = int(leveys)
    h = int(korkeus)
    s = str(merkki)

    for i in range(h):
        print(merkki * w)


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    
    print_box(width, height, mark)

main()
