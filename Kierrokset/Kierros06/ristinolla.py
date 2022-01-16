# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ristinolla, program code template
from collections import Counter


def main():
    list = [['.','.' ,'.' ], ['.', '.', '.'], ['.', '.', '.']]

    print(list[0][0], list[0][1], list[0][2], sep='')
    print(list[1][0], list[1][1], list[1][2], sep='')
    print(list[2][0], list[2][1], list[2][2], sep='')
    peli(list)

    # The game continues until the board is full.
    # 9 marks have been placed on the board when the player has been
    # switched 8 times.
def peli(list):
    turns = 0
    while turns < 9:

        # Change the mark for the player
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        coordinates = input("Player " + mark + ", give coordinates: ")
        lista = (vuoro(coordinates, mark, list))
        if list == lista:
            print(list[0][0], list[1][0], list[2][0], sep='')
            print(list[0][1], list[1][1], list[2][1], sep='')
            print(list[0][2], list[1][2], list[2][2], sep='')

        v0 = [list[0][0], list[1][0], list[2][0]]
        v1 = [list[0][1], list[1][1], list[2][1]]
        v2 = [list[0][2], list[1][2], list[2][2]]
        r = [list[0][0], list[1][1], list[2][2]]
        r1 = [list[2][0], list[1][1], list[0][2]]
        määräp0 = Counter(list[0])
        määräp1 = Counter(list[1])
        määräp2 = Counter(list[2])
        määräv0 = Counter(v0)
        määräv1 = Counter(v1)
        määräv2 = Counter(v2)
        määrär = Counter(r)
        määrär1 = Counter(r1)

        if määräp0['X'] == 3 or määräp1['X'] == 3 or määräp2['X'] == 3:
            print('The game ended, the winner is X')
            break
        if määräv0['X'] == 3 or määräv1['X'] == 3 or määräv2['X'] == 3:
            print('The game ended, the winner is X')
            break
        if määrär['X'] == 3 or määrär1['X'] == 3:
            print('The game ended, the winner is X')
            break
        if määräp0['O'] == 3 or määräp1['O'] == 3 or määräp2['O'] == 3:
            print('The game ended, the winner is O')
            break
        if määräv0['O'] == 3 or määräv1['O'] == 3 or määräv2['O'] == 3:
            print('The game ended, the winner is O')
            break
        if määrär['O'] == 3 or määrär1['O'] == 3:
            print('The game ended, the winner is O')
            break
        turns += 1
    if turns == 9:
        print('Draw!')


def vuoro(coordinates, mark, list):
        try:
            x, y = coordinates.split(" ")
            x = int(x)
            y = int(y)

            # TODO: implement the turn of one player here
            if list[x][y] == 'X' or list [x][y] == 'O':
                print("Error: a mark has already been placed on this square.")
                return
            else:
                if mark == 'X':
                    list[x][y] = 'X'

                else:
                    list[x][y] = 'O'
        except ValueError:
            print("Error: enter two integers, separated with spaces.")
            return
        except IndexError:
            print("Error: coordinates must be between 0 and 2.")
            return
        return list




main()
