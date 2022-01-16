# Johdatus ohjelmointiin
# Introduction to programming
# Area


def area(sivu1, sivu2, sivu3):
    x = sivu1
    y = sivu2
    z = sivu3
    s = (x + y + z) / 2
    Area = (s * (s - x) * (s - y) * (s - z)) ** 0.5
    return Area


def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))
    Area = area(a, b, c)
    print("The triangle's area is {:.1f}".format(Area))


main()
