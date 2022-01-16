"""
TIE-0210X 
Program code template
Mölkky
"""


# TODO: a) Implement the class Player here
class Player:
    def __init__(self, name):
        self.__playername = name
        self.__score = 0
        self.__total_score = 0
        self.__throws = 0
        self.__average = 0
        self.__accuracy = 0
        self.__hits = 0

    def get_name(self):
        return self.__playername

    def get_points(self):
        return self.__score

    def has_won(self):
        if self.__score == 50:
            return True
        else:
            return False

    def add_points(self, pts):
        self.__total_score += pts

        if pts > 0:
            self.__hits += 1

        if self.__score + pts <= 50:
            self.__score += pts

        elif self.__score + pts > 50:
            self.__score = 25
            print(self.__playername, 'gets penalty points!')

        if 40 <= self.__score <= 49:
            tarvittavat_pisteet = 50 - self.__score
            print(self.__playername, 'needs only', tarvittavat_pisteet,
                  "points. It's better to avoid knocking down the pins with higher points.")

    def average(self):
        self.__throws += 1
        self.__average = self.__total_score / self.__throws
        return self.__average

    def accuracy(self):
        if self.__hits == 0:
            return 0
        else:
            self.__accuracy = (self.__hits / self.__throws) * 100
            return self.__accuracy


def main():

    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!
    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:
        if throw % 2 == 0:
            in_turn = player1
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))
        
        in_turn.add_points(pts)

        if in_turn.average() < pts:
            print("Cheers " + in_turn.get_name() + '!')

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p, hit percentage {:.1f}".format(player1.accuracy()))
        print(player2.get_name() + ":", player2.get_points(), "p, hit percentage {:.1f}".format(player2.accuracy()))
        print("")

        throw += 1


main()

