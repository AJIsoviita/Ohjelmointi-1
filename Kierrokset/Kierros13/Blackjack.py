# TIE-02101 Johdatus ohjelmointiin
# Antti-Jussi Isoviita, 283435
# Maunu Halivaara, 291822
# antti-jussi.isoviita@tuni.fi
# maunu.halivaara@tuni.fi

# Blackjack - cardgame
# The program is player versus dealer basic blackjack game, cards get visually
# played to the table and the program counts total score each round.
# Instructions to the game can be found on the front page.
# Player can play multiple games in a row without quitting the game.

from tkinter import *
import random

# To create list which has all of the cards.
i = 1
CARDPICS = []
while i < 53:
    x = "{:d}.gif".format(i)
    CARDPICS.append(x)
    i += 1

PLAYER_NUMBER = 2


class Blackjack:
    # Class Blackjack is where methods which the game uses are created.

    def __init__(self):
        # The builder method of class Blackjack,
        # which has the most important widgets.
        self.__mainwindow = Tk()
        self.__mainwindow.title('Main menu')
        self.__mainwindow.minsize(300, 150)

        # To save pictures in list.
        self.__cardpics = []
        for picfile in CARDPICS:
            pic = PhotoImage(file=picfile)
            self.__cardpics.append(pic)

        # To get total points for player and dealer.
        self.__pointlabels = []
        for player_number in range(PLAYER_NUMBER):
            new_label = Label(self.__mainwindow)
            new_label.grid()
            self.__pointlabels.append(new_label)

        # Values that need to be used in different methods.
        self.__width = 6
        self.__multiplier = 1
        self.__current_card_score = 0
        self.__card_score_sum = 0
        self.__dealer_card_score_sum = 0
        self.__player_beginning_score_sum = 0
        self.__dealer_beginning_score_sum = 0
        self.__card_number = 0
        self.__card_labels = []
        self.__dealer_card_labels = []
        self.__player_wins = 0
        self.__player_loses = 0

        # Preset labels.
        self.__explanation_label = Label(
            text='What would you like to do?', width=50)

        self.__instructions_label = Label(
            text='', bg='gray80', bd=3, relief=SUNKEN)

        self.__player_points_total = Label(
            text='0', bg='black', bd=3, fg='white', relief=RAISED)

        self.__dealer_points_total = Label(
            text='0', bg='black', bd=3, fg='white', relief=RAISED)

        self.__player_name_label = Label(
            text='', bg='snow2', fg='black', relief=RAISED, bd=4)

        self.__dealer_label = Label(
            text='DEALER', bg='dim gray', fg='black', relief=RAISED, bd=4)

        self.__empty_label1 = Label(text='')
        self.__empty_label2 = Label(text='')
        self.__card_label = Label(text='')
        self.__player_card1_label = Label(text='')
        self.__player_card2_label = Label(text='')
        self.__dealer_card1_label = Label(text='')
        self.__dealer_card2_label = Label(text='')

        self.__busted_label = Label(
            text='BUSTED', bg='red', bd=4, fg='black', relief=RAISED)

        self.__blackjack_label = Label(
            text='BLACKJACK', bg='yellow', bd=4, fg='black', relief=RAISED)

        self.__winning_label_dealer = Label(
            text='DEALER WINS', bg='gold', bd=4, fg='black', relief=RAISED)

        self.__losing_label_dealer = Label(
            text='DEALER LOSES', bg='red', bd=4, fg='black', relief=RAISED)

        self.__winning_label_player = Label(
            text='PLAYER WINS', bg='gold', bd=4, fg='black', relief=RAISED)

        self.__losing_label_player = Label(
            text='PLAYER LOSES', bg='red', bd=4, fg='black', relief=RAISED)

        self.__player_wins_label = Label(text='Wins: {:d}'
                                         .format(self.__player_wins))
        self.__player_loses_label = Label(text='Losses: {:d}'
                                          .format(self.__player_loses))

        # Preset buttons.
        self.__continue_button = Button(self.__mainwindow, text='START',
                                        bg='green', bd=3, fg='black',
                                        command=self.proceed_to_name_selection)

        self.__instructions_button = Button(self.__mainwindow,
                                            text='INSTRUCTIONS', bd=3,
                                            bg='NavajoWhite3',
                                            fg='black',
                                            command=self.instructions)

        self.__stop_button = Button(self.__mainwindow, text='QUIT',
                                    background='firebrick1', bd=3,
                                    foreground='black',
                                    command=self.stop)

        self.__deal_button = Button(self.__mainwindow, text='DEAL', bg='green',
                                    bd=3, fg='black', command=self.deal)

        self.__quit_to_menu = Button(self.__mainwindow, text='RETURN TO MENU',
                                     bg='NavajoWhite3', fg='black',
                                     command=self.return_to_menu)

        self.__deal_again_button = Button(text='DEAL AGAIN?', bg='green',
                                          fg='black', bd=3,
                                          command=self.clear_table)

        self.__hit_button = Button(self.__mainwindow, text='HIT', bg='green',
                                   fg='black', bd=3, command=self.hit)

        self.__stand_button = Button(self.__mainwindow, text='STAND',
                                     bg='MistyRose3', fg='black', bd=3,
                                     command=self.stand)

        self.__stats_button = Button(self.__mainwindow, text='STATISTICS',
                                     bg='MistyRose2', fg='black', bd=3,
                                     command=self.stats)

        # Specialities.
        self.__player_name = Entry()

        # Placement for widgets in main menu.
        self.__explanation_label.grid(row=0, column=0, sticky='nsew')

        self.__continue_button.grid(
            row=2, column=0, columnspan=3, sticky='nsew')

        self.__instructions_button.grid(
            row=3, column=0, columnspan=3, sticky='nsew')

        self.__stats_button.grid(row=4, column=0, columnspan=3, sticky='nsew')

        self.__stop_button.grid(row=5, column=0, columnspan=3, sticky='nsew')

    def start(self):
        # To get Tk() started.
        self.__mainwindow.mainloop()

    def stop(self):
        # To stop Tk().
        self.__mainwindow.destroy()

    def proceed_to_name_selection(self):
        # Next phase of the game, where player selects player name.
        self.__instructions_button.grid_forget()
        self.__instructions_label.grid_forget()
        self.__player_wins_label.grid_forget()
        self.__player_loses_label.grid_forget()
        self.__stats_button.grid_forget()
        # Updating text labels.
        self.__player_name = Entry()
        self.__explanation_label.configure(text='Enter your name:')
        self.__continue_button.configure(
            text='CONTINUE', command=self.proceed_to_game)

        # Widget placement.
        self.__player_name.grid(row=1, sticky='nsew')
        self.__continue_button.grid(row=2, sticky='nsew')
        self.__stop_button.grid(row=3, sticky='nsew')

    def proceed_to_game(self):
        # Next phase of the game, where the real game begins.
        self.__mainwindow.title('Blackjack')

        playername = self.__player_name.get().upper()
        self.__player_name_label.configure(text=playername)

        self.__explanation_label.grid_forget()
        self.__continue_button.grid_forget()

        # Destroys the Entry(), so it won't cause errors.
        self.__player_name.destroy()

        # Widget placement in Game Interface.
        self.__player_name_label.grid(
            row=0, rowspan=2, columnspan=3, sticky='nsew')
        self.__empty_label1.grid(row=3, sticky='nsew')
        self.__deal_button.grid(row=8, rowspan=2, columnspan=2, sticky='nsew')
        self.__quit_to_menu.grid(row=10, rowspan=2, columnspan=2,
                                 sticky='nsew')
        self.__stop_button.grid(row=12, rowspan=2, columnspan=2, sticky='nsew')
        self.__empty_label2.grid(row=14, rowspan=2, columnspan=2,
                                 sticky='nsew')
        self.__dealer_label.grid(row=20, rowspan=2, columnspan=3,
                                 sticky='nsew')

    def return_to_menu(self):
        self.__mainwindow.title('Main menu')
        self.__mainwindow.minsize(300, 150)

        # Clearing useless widgets.
        self.clear_table()
        self.__player_name_label.grid_forget()
        self.__empty_label1.grid_forget()
        self.__deal_button.grid_forget()
        self.__quit_to_menu.grid_forget()
        self.__empty_label2.grid_forget()
        self.__dealer_label.grid_forget()

        # Updating hidden labels.
        self.__explanation_label.configure(text='What would you like to do?')
        self.__continue_button.configure(
            command=self.proceed_to_name_selection)

        # Widget placement.
        self.__explanation_label.grid(row=0, column=0, sticky='nsew')
        self.__continue_button.grid(row=1, sticky='nsew')
        self.__instructions_button.grid(row=2, sticky='nsew')
        self.__stop_button.grid(row=4, column=0, columnspan=3, sticky='nsew')
        self.__stats_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

    def deal(self):
        # Start of Blackjack, both players are given 2 random cards.

        # Clearing useless widgets.
        self.__deal_button.grid_forget()
        self.__quit_to_menu.grid_forget()
        self.__stop_button.grid_forget()

        # Widget placement.
        self.__empty_label1.grid()
        self.__hit_button.grid(row=8, rowspan=2, sticky='nsew')
        self.__stand_button.grid(row=10, rowspan=2, sticky='nsew')
        self.__stop_button.grid(row=12, rowspan=2, sticky='nsew')

        # Randomly selecting 2 cards and suits for player and dealer.
        player_number1 = random.randint(1, 13)
        player_number2 = random.randint(1, 13)
        dealer_number1 = random.randint(1, 13)
        dealer_number2 = random.randint(1, 13)
        suit = random.randint(0, 3)
        suit2 = random.randint(0, 3)
        suit3 = random.randint(0, 3)
        suit4 = random.randint(0, 3)

        self.__player_card1_label.configure(
            image=self.__cardpics[player_number1 + 13 * suit - 1])

        self.__player_card2_label.configure(
            image=self.__cardpics[player_number2 + 13 * suit2 - 1])

        self.__dealer_card1_label.configure(
            image=self.__cardpics[dealer_number1 + 13 * suit3 - 1])

        self.__dealer_card2_label.configure(
            image=self.__cardpics[dealer_number2 + 13 * suit4 - 1])

        # Counting the total points for player and dealer.
        self.__player_beginning_score_sum = \
            self.over_ten(player_number1) + self.over_ten(player_number2)

        self.__dealer_beginning_score_sum = \
            self.over_ten(dealer_number1) + self.over_ten(dealer_number2)

        self.__player_points_total.configure(
            text=self.__player_beginning_score_sum)

        self.__dealer_points_total.configure(
            text=self.__dealer_beginning_score_sum)

        # Widget placement.
        self.__player_points_total.grid(
            row=0, column=3, columnspan=2, rowspan=2, sticky='nsew')

        self.__dealer_points_total.grid(
            row=20, column=3, columnspan=2, rowspan=2, sticky='nsew')

        self.__player_card1_label.grid(
            row=4, column=0, columnspan=2, rowspan=2, sticky='nsew')

        self.__player_card2_label.grid(
            row=4, column=3, columnspan=2, rowspan=2, sticky='nsew')

        self.__dealer_card1_label.grid(
            row=15, column=0, columnspan=2, rowspan=2, sticky='nsew')

        self.__dealer_card2_label.grid(
            row=15, column=3, columnspan=2, rowspan=2, sticky='nsew')

        # If player gets score over 21 in start.
        if self.__player_beginning_score_sum > 21:
            self.__hit_button.grid_forget()
            self.__stand_button.grid_forget()
            self.__stop_button.grid_forget()
            self.__busted_label.grid(row=0, column=6, sticky='nsew')
            self.__winning_label_dealer.grid(row=20, column=6, sticky='nsew')
            self.__stop_button.grid(row=12, column=6, sticky='nsew')
            self.__deal_again_button.grid(row=12, sticky='nsew')
            self.__quit_to_menu.grid(row=12, column=4, sticky='nsew')
            self.__player_loses += 1

        # If player gets score 21 in start.
        elif self.__player_beginning_score_sum == 21:
            self.__hit_button.grid_forget()
            self.__stand_button.grid_forget()
            self.__stop_button.grid_forget()
            self.__blackjack_label.grid(row=0, column=6, sticky='nsew')
            self.__losing_label_dealer.grid(row=20, column=6, sticky='nsew')
            self.__stop_button.grid(row=12, column=6, sticky='nsew')
            self.__deal_again_button.grid(row=12, sticky='nsew')
            self.__quit_to_menu.grid(row=12, column=4, sticky='nsew')
            self.__player_wins += 1

        # If dealer gets score over 21 in start.
        elif self.__dealer_beginning_score_sum > 21:
            self.__hit_button.grid_forget()
            self.__stand_button.grid_forget()
            self.__stop_button.grid_forget()
            self.__busted_label.grid(row=20, column=6, sticky='nsew')
            self.__winning_label_player.grid(row=0, column=6, sticky='nsew')
            self.__stop_button.grid(row=12, column=6, sticky='nsew')
            self.__deal_again_button.grid(row=12, sticky='nsew')
            self.__quit_to_menu.grid(row=12, column=4, sticky='nsew')
            self.__player_wins += 1

        # If dealer gets score of 21 in start.
        elif self.__dealer_beginning_score_sum == 21:
            self.__hit_button.grid_forget()
            self.__stand_button.grid_forget()
            self.__stop_button.grid_forget()
            self.__blackjack_label.grid(row=20, column=6, sticky='nsew')
            self.__losing_label_player.grid(row=0, column=6, sticky='nsew')
            self.__stop_button.grid(row=12, column=6, sticky='nsew')
            self.__deal_again_button.grid(row=12, sticky='nsew')
            self.__quit_to_menu.grid(row=12, column=4, sticky='nsew')
            self.__player_loses += 1

    def hit(self):
        """
        Hitting or not hitting is only possible to the player, dealer is forced
        to hit until 17. If dealer gets score over 17 he won't get more cards.
        """

        # Choosing the card value and suit and showing it on the table.
        number = random.randint(1, 13)
        suit = random.randint(0, 3)
        self.__current_card_score += self.over_ten(number)

        self.__card_labels.append(Label(
            image=self.__cardpics[number + suit * 13 - 1]))

        self.__card_score_sum = \
            self.__current_card_score + self.__player_beginning_score_sum
        self.__player_points_total.configure(text=self.__card_score_sum)

        self.__card_labels[self.__card_number].grid(
            row=4, column=self.__width, sticky='nsew')
        self.__player_points_total.grid(
            row=0, column=3, columnspan=2, rowspan=2, sticky='nsew')
        self.__card_number += 1
        self.__width += 3 * self.__multiplier
        self.__multiplier += 1

        # If player gets total score of 21.
        if self.__card_score_sum == 21:
            self.__hit_button.grid_forget()
            self.__stand_button.grid_forget()
            self.__stop_button.grid_forget()
            self.__blackjack_label.grid(row=0, column=6, sticky='nsew')
            self.__losing_label_dealer.grid(row=20, column=6, sticky='nsew')
            self.__stop_button.grid(row=12, column=6, sticky='nsew')
            self.__deal_again_button.grid(row=12, sticky='nsew')
            self.__quit_to_menu.grid(row=12, column=4, sticky='nsew')
            self.__player_wins += 1

        # If player gets total score over 21.
        elif self.__card_score_sum > 21:
            self.__hit_button.grid_forget()
            self.__stand_button.grid_forget()
            self.__stop_button.grid_forget()
            self.__busted_label.grid(row=0, column=6, sticky='nsew')
            self.__winning_label_dealer.grid(row=20, column=6, sticky='nsew')
            self.__stop_button.grid(row=12, column=6, sticky='nsew')
            self.__deal_again_button.grid(row=12, sticky='nsew')
            self.__quit_to_menu.grid(row=12, column=4, sticky='nsew')
            self.__player_loses += 1

    def stand(self):
        """
        Phase of the game, where player has
        ended his turn and its dealer's turn to play.
        """

        dealer_card_score_sum = self.__dealer_beginning_score_sum
        self.__multiplier = 0
        self.__width = 6
        self.__dealer_card_labels = []
        self.__card_number = 0

        # Loop to play whole dealers turn at once.
        while dealer_card_score_sum < 18:
            number = random.randint(1, 13)
            suit = random.randint(0, 3)

            # To check for picture cards.
            dealer_card_score_sum += self.over_ten(number)

            # Getting the cards next to each other
            # and not on top of each other.
            self.__dealer_card_labels.append(Label(
                image=self.__cardpics[number + suit * 13 - 1]))
            self.__width = self.__width + 2 * self.__multiplier
            self.__dealer_card_labels[self.__card_number].configure(
                image=self.__cardpics[number + suit * 13 - 1])

            # Updating point label.
            self.__dealer_points_total.configure(text=dealer_card_score_sum)
            self.__dealer_card_labels[self.__card_number].grid(
                row=15, column=self.__width, sticky='nsew')
            self.__dealer_points_total.grid(
                row=20, column=3, columnspan=2, rowspan=2, sticky='nsew')

            self.__multiplier += 1
            self.__card_number += 1

            # If dealer gets total score of 21.
            if dealer_card_score_sum == 21:
                self.__hit_button.grid_forget()
                self.__stand_button.grid_forget()
                self.__stop_button.grid_forget()
                self.__blackjack_label.grid(row=20, column=6, sticky='nsew')
                self.__losing_label_player.grid(row=0, column=6, sticky='nsew')
                self.__stop_button.grid(row=12, column=6, sticky='nsew')
                self.__deal_again_button.grid(row=12, sticky='nsew')
                self.__quit_to_menu.grid(row=12, column=4, sticky='nsew')
                self.__player_loses += 1

            # If dealer gets total score over 21.
            elif dealer_card_score_sum > 21:
                self.__hit_button.grid_forget()
                self.__stand_button.grid_forget()
                self.__stop_button.grid_forget()
                self.__busted_label.grid(row=20, column=6, sticky='nsew')
                self.__winning_label_player.grid(row=0, column=6,
                                                 sticky='nsew')
                self.__stop_button.grid(row=12, column=6, sticky='nsew')
                self.__deal_again_button.grid(row=12, sticky='nsew')
                self.__quit_to_menu.grid(row=12, column=4, sticky='nsew')
                self.__player_wins += 1

        # Getting dealer total score out of method to reset it in other method
        self.__dealer_card_score_sum = dealer_card_score_sum

        # If player and dealer won't get total score of 21 or over 21.
        # And player has lower score than dealer.
        if 21 > dealer_card_score_sum >= self.__card_score_sum:
            self.__stop_button.grid_forget()
            self.__hit_button.grid_forget()
            self.__stand_button.grid_forget()
            self.__winning_label_dealer.grid(row=20, column=6, sticky='nsew')
            self.__losing_label_player.grid(row=0, column=6, sticky='nsew')
            self.__stop_button.grid(row=12, column=6, sticky='nsew')
            self.__deal_again_button.grid(row=12, sticky='nsew')
            self.__quit_to_menu.grid(row=12, column=4, sticky='nsew')
            self.__player_loses += 1

        # If player and dealer won't get total score of 21 or over 21,
        # and player has higher score than dealer.
        elif 21 > self.__card_score_sum > dealer_card_score_sum:
            self.__stop_button.grid_forget()
            self.__hit_button.grid_forget()
            self.__stand_button.grid_forget()
            self.__winning_label_player.grid(row=0, column=6, sticky='nsew')
            self.__losing_label_dealer.grid(row=20, column=6, sticky='nsew')
            self.__stop_button.grid(row=12, column=6, sticky='nsew')
            self.__deal_again_button.grid(row=12, sticky='nsew')
            self.__quit_to_menu.grid(row=12, column=4, sticky='nsew')
            self.__player_wins += 1

    def clear_table(self):
        # For resetting the table and its contents.
        self.__deal_again_button.grid_forget()
        self.__stop_button.grid_forget()
        self.__losing_label_dealer.grid_forget()
        self.__losing_label_player.grid_forget()
        self.__winning_label_dealer.grid_forget()
        self.__winning_label_player.grid_forget()
        self.__busted_label.grid_forget()
        self.__blackjack_label.grid_forget()
        self.__dealer_points_total.grid_forget()
        self.__player_points_total.grid_forget()
        self.__empty_label1.grid_forget()
        self.__empty_label2.grid_forget()
        self.__quit_to_menu.grid_forget()

        for labelsP in self.__card_labels:
            labelsP.configure(image='')

        for labelsD in self.__dealer_card_labels:
            labelsD.configure(image='')

        self.__card_labels = []
        self.__dealer_card_labels = []
        self.__dealer_card_score_sum = 0
        self.__card_score_sum = 0
        self.__current_card_score = 0
        self.__card_number = 0
        self.__width = 6
        self.__multiplier = 1

        self.__player_card1_label.config(image='')
        self.__player_card2_label.config(image='')
        self.__dealer_card1_label.config(image='')
        self.__dealer_card2_label.config(image='')

        self.__deal_button.grid(row=12, sticky='nsew')
        self.__stop_button.grid(row=12, column=4, sticky='nsew')

    def instructions(self):
        # Instructions to the game for new players.
        self.__explanation_label.configure(text='Game instructions: ')
        self.__continue_button.configure(text='CONTINUE')

        self.__stats_button.grid_forget()
        self.__continue_button.grid_forget()
        self.__instructions_button.grid_forget()
        self.__stop_button.grid_forget()

        self.__instructions_label.configure(text="¤ The goal of Blackjack is "
                                                 "to beat the dealer's hand \n"
                                                 '  without going over 21. \n'
                                                 '¤ Player and dealer both '
                                                 'start with 2 cards. \n'
                                                 '¤ To "Hit" is to ask '
                                                 'for another card. \n'
                                                 '¤ To "Stand" is to '
                                                 'end your turn. \n'
                                                 '¤ If you go over 21 you '
                                                 'bust, and the dealer wins\n'
                                                 "  regardless of the "
                                                 "dealer's hand.\n"
                                                 "¤ Every picture card "
                                                 "has value of 10.\n"
                                                 '¤ If you are dealt 21 from'
                                                 ' the start, you got '
                                                 'Blackjack.\n'
                                                 '¤ Dealer will hit until its'
                                                 ' card total is 17 or'
                                                 ' higher.\n', width=50)
        self.__instructions_label.grid(row=2, sticky='nsew')
        self.__continue_button.grid(row=5, sticky='nsew')
        self.__stop_button.grid(row=6, sticky='nsew')

    def over_ten(self, number_check):
        """
        In  Blackjack picture cards have value of 10 instead of their real
        values (11, 12 , 13). Param number_check is the value of the number
        being checked.
        """
        if number_check > 10:
            return 10
        else:
            return number_check

    def stats(self):
        # Counting total victories and defeats.
        self.__explanation_label.configure(text='Statistics: ')
        self.__continue_button.configure(text='CONTINUE')
        self.__player_wins_label.configure(text='WINS: {:d}'
                                           .format(self.__player_wins),
                                           bg='lawn green', bd=3,
                                           relief=RAISED)
        self.__player_loses_label.configure(text='LOSES: {:d}'
                                            .format(self.__player_loses),
                                            bg='red3', bd=3,
                                            relief=RAISED)

        self.__stats_button.grid_forget()
        self.__continue_button.grid_forget()
        self.__instructions_button.grid_forget()
        self.__stop_button.grid_forget()

        self.__player_wins_label.grid(row=3)
        self.__player_loses_label.grid(row=4)

        self.__continue_button.grid(row=5, sticky='nsew')
        self.__stop_button.grid(row=6, sticky='nsew')


def main():
    menu = Blackjack()
    menu.start()


main()
