# Fill in all TODOs in this file

from math import sqrt

# This is a text-based menu. You should ONLY touch TODOs inside the menu.
# TODOs in the menu call functions that you have implemented and take care
# of the return values of the function calls.


def menu():
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)
            x = x
            y = y
        elif choice == "3":
            break

    print("Thank you and bye!")


# This function has three parameters which are all FLOATs:
#       (1) the size of the tank
#       (2) the amount of gas that is requested to be filled in
#       (3) the amount of gas in the tank currently
#
# The parameters have to be in this order.
# The function returns one FLOAT that is the amount of gas in the
# tank AFTER the filling up.
#
# The function does not print anything and does not ask for any
# input.
def fill(mtilavuus, täyttö, ntilavuus):
    float(mtilavuus)
    float(täyttö)
    float(ntilavuus)
    tilavuus1 = täyttö + ntilavuus
    if tilavuus1 > mtilavuus:
        return mtilavuus
    else:
        return tilavuus1


# This function has six parameters. They are all floats.
#   (1) The current x coordinate
#   (2) The current y coordinate
#   (3) The destination x coordinate
#   (4) The destination y coordinate
#   (5) The amount of gas in the tank currently
#   (6) The consumption of gas per 100 km of the car
#
# The parameters have to be in this order.
# The function returns three floats:
#   (1) The amount of gas in the tank AFTER the driving
#   (2) The reached (new) x coordinate
#   (3) The reached (new) y coordinate
#
# The return values have to be in this order.
# The function does not print anything and does not ask for any
# input.
def drive(x, y, ux, uy, gas, gas_consumption):
   etaisyys, dx, dy = matka(x, y, ux, uy)

   max_etaisyys = max_matka(gas, gas_consumption)

   siirtx, siirty = siirtyma(dx, dy, etaisyys, max_etaisyys)

   gas2 = max(0, gas - etaisyys * gas_consumption / 100)

   return gas2, x + siirtx, y + siirty

    # It might be useful to make one or two helper functions to help
    # the implementation of this function (drive)


def matka(x, y ,ux, uy):
    muutosx = ux - x
    muutosy = uy - y
    matka = sqrt(muutosx * muutosx + muutosy * muutosy)
    return matka, muutosx, muutosy
# Implement your own functions here. It is required to implement at least
# two functions that take at least one parameter and return at least one
# value.
# The functions have to be used somewhere in the program.


def max_matka(gas, gas_consumption):
    max_matka = 100 * gas / gas_consumption
    return max_matka


def siirtyma(dx, dy, etaisyys, max_etaisyys):
    siirtymä = min(1, max_etaisyys / etaisyys) if etaisyys != 0 else 1
    siirtymäx = dx * siirtymä
    siirtymäy = dy * siirtymä
    return siirtymäx, siirtymäy

def read_number(prompt, error_message="Incorrect input!"):

    # This function reads input from the user.
    # Do not touch this function.
    try:
        return float(input(prompt))
    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


main()
