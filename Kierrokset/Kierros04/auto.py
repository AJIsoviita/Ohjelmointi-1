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
    new_x = 0
    new_y = 0
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
def fill(tank_size, amount, current):
    return min(tank_size, current + amount)


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
def drive(cur_x, cur_y, dest_x, dest_y, gas, consumption):
    # It might be usefull to make one or two helper functions to help
    # the implementation of this function (drive)
    dist, dx, dy = distance(cur_x, cur_y, dest_x, dest_y)

    dist_left = calc_dist_left(gas, consumption)

    reach_x, reach_y = calc_reach(dx, dy, dist, dist_left)

    gas_left = calc_gas_left(gas, dist, consumption)

    return gas_left, cur_x + reach_x, cur_y + reach_y


# Implement your own functions here. It is required to implement at least
# two functions that take at least one parameter and return at least one
# value.
# The functions have to be used somewhere in the program.

# Distance between two points
def distance(cur_x, cur_y, dest_x, dest_y):
    delta_x = dest_x - cur_x
    delta_y = dest_y - cur_y
    dist = sqrt(delta_x * delta_x + delta_y * delta_y)
    return dist, delta_x, delta_y


# How much gas will be left after going specified distance
def calc_gas_left(gas, dist, consumption):
    return max(0.0, gas - dist * consumption / 100)


# How far can we go with our current gas amount
def calc_dist_left(gas, consumption):
    return 100 * gas / consumption


# How far along x and y-axes can we travel
def calc_reach(dx, dy, dist, dist_left):
    # reach is the fraction of the target distance we can still reach with our gas
    reach = min(1.0, dist_left / dist) if dist != 0 else 1
    reach_x = reach * dx
    reach_y = reach * dy

    return reach_x, reach_y


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
