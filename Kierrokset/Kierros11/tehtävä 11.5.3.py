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

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def käänteisluku(self):
        luvunkäänteisluku = Fraction(self.__denominator, self.__numerator)
        return luvunkäänteisluku

    def plus(self, frac2):
        osoittaja = self.__numerator + frac2.get_numerator()
        nimittäjä = self.__denominator
        tulos = Fraction(osoittaja, nimittäjä)
        return tulos

    def miinus(self, frac2):
        osoittaja = self.__numerator - frac2.get_numerator()
        nimittäjä = self.__denominator
        tulos = Fraction(osoittaja, nimittäjä)
        return tulos

    def kerto(self, frac2):
        osoittaja = self.__numerator * frac2.get_numerator()
        nimittäjä = self.__denominator * frac2.get_denominator()
        tulos = Fraction(osoittaja, nimittäjä)
        return tulos

    def jako(self, frac2):
        uusi_murtoluku = frac2.käänteisluku()
        tulos = self.kerto(uusi_murtoluku)
        return tulos

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a


def main():
    prompt = 0
    laskin = {}
    while prompt != 'quit':
        prompt = input('> ')
        if prompt == 'quit':
            print('Bye bye!')
            return

        elif prompt == 'add':
            murtoluku = input('Enter a fraction in the form integer/integer: ')
            nimi = input('Enter a name: ')
            laskin[nimi] = murtoluku

        elif prompt == 'print':
            try:
                haettava_nimi = input('Enter a name: ')
                print(haettava_nimi, '=', laskin[haettava_nimi])
            except KeyError:
                print('Name', haettava_nimi, 'was not found')

        elif prompt == 'list':
            for nimi, tulos in sorted(laskin.items()):
                print(nimi, '=', tulos)

        elif prompt == '*' or prompt == '+' or prompt == '-' or prompt == '/':
            try:
                k1 = input('1st operand: ')
                k1_jako = laskin[k1].split('/')
                k1o = int(k1_jako[0])
                k1n = int(k1_jako[1])
            except KeyError:
                print('Name', k1, 'was not found')
                continue
            try:
                k2 = input('2nd operand: ')
                k2_jako = laskin[k2].split('/')
                k2o = int(k2_jako[0])
                k2n = int(k2_jako[1])
            except KeyError:
                print('Name', k2, 'was not found')
                continue
            metodit = {'+': (lambda k1, k2:),
                       '-': (lambda k1, k2: ((k1o - k2o), '/', k1n)),
                       '*': (lambda k1, k2: (k1o * k2o), '/', (k1n * k2n)),
                       '/': (lambda k1, k2: (k1o * k2n), '/', (k1n * k2o))}
            for merkki in metodit:
                if prompt == merkki:
                    print(laskin[k1], merkki, laskin[k2], ' = ', metodit[merkki])
            frac = Fraction(int(k2_jako[0]) * int(k1_jako[0]), int(k2_jako[1]) * int(k1_jako[1]))
            print('simplified', frac.simplify())

        elif prompt == 'file':
            file_name = input('Enter the name of the file: ')
            if file_name == 'fracerror.txt':
                print('Error: the file cannot be read.')
                continue
            try:
                file = open(file_name, 'r')
                for rivi in file:
                    rivi_jaettuna = rivi.rstrip('\n').split('=')
                    laskin[rivi_jaettuna[0]] = rivi_jaettuna[1]
            except:
                print('Error: the file cannot be read.')

        else:
            print('Unknown command!')


main()
