# TIE-02101 Johdatus ohjelmointiin
# Antti-Jussi Isoviita, 283435
# antti-jussi.isoviita@tuni.fi

from tkinter import *
import random
import time

i = 1
CARDPICS = []
while i < 53:
    x = "{:d}.gif".format(i)
    CARDPICS.append(x)
    i += 1

PLAYER_NUMBER = 2


class Blackjack:
    def __init__(self):
        self.__mainwindow = Tk()
        self.__mainwindow.title('Main menu')
        self.__mainwindow.geometry('300x150')
        self.__turn = 0

        self.__cardpics = []
        for picfile in CARDPICS:
            pic = PhotoImage(file=picfile)
            self.__cardpics.append(pic)

        self.__explanation_label = Label(text='What would you like to do?')
        self.__continue_button = Button(self.__mainwindow, text='Start', bg='green', fg='white',
                                        command=self.proceed_to_name_selection)
        self.__stop_button = Button(self.__mainwindow, text='Quit',
                                    background='red', foreground='white',
                                    command=self.stop)

        self.__explanation_label.pack(fill=X)
        self.__continue_button.pack(fill=X)
        self.__stop_button.pack(fill=X)

    def start(self):
        self.__mainwindow.mainloop()

    def stop(self):
        self.__mainwindow.destroy()

    def proceed_to_name_selection(self):
        self.__continue_button.destroy()
        self.__stop_button.destroy()

        self.__player_name = Entry()
        self.__explanation_label.configure(text='Enter your name: ')
        self.__continue_button = Button(self.__mainwindow, text='Continue', bg='green', fg='white',
                                        command=self.proceed_to_game)
        self.__stop_button = Button(self.__mainwindow, text='Quit',
                                    background='red', foreground='white',
                                    command=self.stop)

        self.__player_name.pack(fill=X)
        self.__continue_button.pack(fill=X)
        self.__stop_button.pack(fill=X)

    def proceed_to_game(self):
        self.__mainwindow.geometry('750x500')
        self.__mainwindow.title('Blackjack')

        playername = self.__player_name.get().upper()
        self.__player_name_label = Label(text=playername, bg='yellow', fg='black')
        self.__dealer_label = Label(text='DEALER', bg='black', fg='white')
        self.__empty_label1 = Label(text='')
        self.__empty_label2 = Label(text='')
        self.__deal_button = Button(self.__mainwindow, text='DEAL', bg='green', fg='white', command=self.deal)
        self.__quit_to_menu = Button(self.__mainwindow, text='RETURN TO MENU', bg='grey', fg='white',
                                     command=self.return_to_menu)
        self.__explanation_label.destroy()
        self.__player_name.destroy()
        self.__continue_button.destroy()
        self.__stop_button.destroy()

        self.__stop_button = Button(self.__mainwindow, text='QUIT',
                                    background='red', foreground='white',
                                    command=self.stop)

        self.__player_name_label.pack(fill=X, padx=10, pady=10, side=TOP)
        self.__empty_label1.pack(fill=X)

        self.__deal_button.pack(fill=BOTH, padx=10, pady=5)
        self.__quit_to_menu.pack(fill=BOTH, padx=10, pady=5)
        self.__stop_button.pack(fill=BOTH, padx=10, pady=5)

        self.__empty_label2.pack(fill=X)
        self.__dealer_label.pack(fill=X, padx=10, pady=10, side=BOTTOM)

    def return_to_menu(self):
        self.__mainwindow.title('Main menu')
        self.__mainwindow.geometry('300x100')

        self.__player_name_label.destroy()
        self.__empty_label1.destroy()
        self.__deal_button.destroy()
        self.__quit_to_menu.destroy()
        self.__stop_button.destroy()
        self.__empty_label2.destroy()
        self.__dealer_label.destroy()

        self.__explanation_label = Label(text='What would you like to do?')
        self.__continue_button = Button(self.__mainwindow, text='Start', bg='green', fg='white',
                                        command=self.proceed_to_name_selection)
        self.__stop_button = Button(self.__mainwindow, text='Quit',
                                    background='red', foreground='white',
                                    command=self.stop)

        self.__explanation_label.pack(fill=X)
        self.__continue_button.pack(fill=X)
        self.__stop_button.pack(fill=X)

    def deal(self):
        self.__empty_label1.destroy()
        self.__deal_button.destroy()
        self.__quit_to_menu.destroy()
        self.__stop_button.destroy()
        self.__empty_label2.destroy()

        self.__hit_button = Button(self.__mainwindow, text='HIT', bg='green', fg='black', command=self.hit)
        self.__stand_button = Button(self.__mainwindow, text='STAND', bg='grey', fg='white', command=self.hit)
        self.__stop_button = Button(self.__mainwindow, text='QUIT', background='red', foreground='white',
                                    command=self.stop)

        self.__hit_button.pack(fill=BOTH, padx=10, pady=5)
        self.__stand_button.pack(fill=BOTH, padx=10, pady=5)
        self.__stop_button.pack(fill=BOTH, padx=10, pady=5)

        self.__cardpiclabels = []
        for i in range(2):
            continue
            new_card = Label(self.__mainwindow)
            new_card.pack()
            self.__cardpiclabels.append(new_card)

        number1 = random.randint(1, 13)
        country = random.randint(0,3)
        self.__card1 = self.__cardpics[number1+13*country-1]
        card1_label = Label(image=self.__card1).pack()
        for image in self.__cardpiclabels:
            continue
            card_value1 = self.__card1
            image.configure(image=self.__card1)

        number2 = random.randint(1, 13)
        self.__card2 = self.__cardpics[number2*country-1]
        card2_label = Label(image=self.__card2).pack()
        for image in self.__cardpiclabels:
            continue
            card_value2 = self.__card2
            image.configure(image=self.__card2)


    def hit(self):
        number = random.randint(1, 13)
        country = random.randint(0, 3)
        self.card = self.__cardpics[number + country*13]

    def stand(self):
        card_sum = sum(self.__current_card_score)
        self.__player_points_total[self.__turn] = self.__player_points_total[self.__turn] + card_sum

        if self.__turn == 0:
            self.__turn += 1
        else:
            self.__turn -= 1



    def calculate_score(self):
        pass

def main():
    menu = Blackjack()
    menu.start()


main()
