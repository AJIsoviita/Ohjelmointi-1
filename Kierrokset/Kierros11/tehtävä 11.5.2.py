class Fraction:
    """ This class represents one single fraction that consists of
        numerator and denominator """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: fraction's numerator
        :param denominator: fraction's denominator
        """

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """ Returns a string-presentation of the fraction in the format
        numerator/denominator """

        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                      abs(self.__denominator))

    def simplify(self):
        a = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // a
        self.__denominator = self.__denominator // a
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                      abs(self.__denominator))


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a

def main():
    line = 0
    nimittäjät = []
    osoittajat = []

    print('Enter fractions in the format integer/integer.')
    print('One fraction per line. Stop by entering an empty line.')
    while line != '':
        line = input()
        if line != '':
            jako = line.split('/')
            osoittajat.append(int(jako[0]))
            nimittäjät.append(int(jako[1]))

    print('The given fractions in their simplified form:')
    for i in range(len(nimittäjät)):
        frac = Fraction(osoittajat[i], nimittäjät[i])
        print(frac.return_string(), '=', frac.simplify())


main()