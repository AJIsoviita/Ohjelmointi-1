# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Template for the task: Car, the revenge

MENU_TEXT = "1) Fill 2) Drive 3) Quit\n-> "
CAR_TEXT = "The tank contains {:.1f} liters of gas and " + \
           "the odometer shows {:.1f} kilometers."

class Car:

    def __init__(self, tank_size, gas_consumption):
        self.__tank_size = tank_size
        self.__gas_consumption = gas_consumption
        self.__gas = 0
        self.__odometer = 0

    def printInformation(self):
        print(CAR_TEXT.format(self.__gas, self.__odometer))

    def fill(self, to_fill):
        if to_fill < 0:
            print('You cannot remove gas from the tank')
        elif to_fill + self.__gas >= self.__tank_size:
            self.__gas = self.__tank_size
        else:
            self.__gas = to_fill + self.__gas

    def drive(self, distance):

        if distance < 0:
            print('You cannot travel a negative distance')

        kulutus_km = self.__gas_consumption / 100
        if distance * kulutus_km < self.__gas:
            self.__odometer += distance
            self.__gas = self.__gas - distance * kulutus_km

        else:
            self.__odometer += self.__gas * self.__gas_consumption
            self.__gas = 0


def main():

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers? ")

    car = Car(tank_size, gas_consumption)

    # (In this program we only need one car-object but it is possible
    # to create multiple objects from one class. For example we could
    # create two objects:
    # lightning_mcqueen = Car(20, 30)
    # mater = Car(10, 10) )

    while True:
        car.printInformation()
        choice = input(MENU_TEXT)

        if choice == "1":
            to_fill = int(read_number("How many liters of gas to fill up? "))
            car.fill(to_fill)

        elif choice == "2":
            distance = read_number("How many kilometers to drive? ")
            car.drive(distance)
        elif choice == "3":
            break
    print("Thank you and bye!")


def read_number(prompt, error_message="Incorrect input!"):

    try:
        return float(input(prompt))
    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)

main()
