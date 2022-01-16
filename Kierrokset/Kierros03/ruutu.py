# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Template for task: ruutu


def print_box(l, k, m):
    w = int(l)
    h = int(k)
    s = str(m)

    for i in range(h):
        print(s * w)

def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print_box(width, height, mark)


main()
