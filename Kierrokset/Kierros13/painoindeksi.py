from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__mainwindow.title('BMI calculator')

        # TODO: Create an Entry-component for the weight.
        self.__weight_label = Label(text='Enter your weight: ')
        self.__weight_label.grid(row=0, column=0)
        self.__weight_value = Entry()
        self.__weight_value.grid(row=1, column=0)
        # TODO: Create an Entry-component for the height.
        self.__height_label = Label(text='Enter your height: ')
        self.__height_label.grid(row=0, column=1)
        self.__height_value = Entry()
        self.__height_value.grid(row=1, column=1)

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        # the default colour.
        self.__calculate_button = Button(self.__mainwindow, text='Calculate BMI',
                                         background='blue', foreground='white',
                                         command=self.calculate_BMI)
        self.__calculate_button.grid(row=1, column=3)
        # TODO: Create a Label that will show the decimal value of the BMI
        # after it has been calculated.
        self.__result_label = Label(text='Results: ')
        self.__result_label.grid(row=0, column=4)
        self.__result_text = Label(text='')
        self.__result_text.grid(row=1, column=4)
        # TODO: Create a Label that will show a verbal description of the BMI
        # after the BMI has been calculated.
        self.__explanation_label = Label(text='Explanation')
        self.__explanation_label.grid(row=0, column=5)
        self.__explanation_text = Label()
        self.__explanation_text.grid(row=1, column=5)
        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text='Stop',
                                    background='red', foreground='white',
                                    command=self.stop)
        self.__stop_button.grid(row=3, column=3)

    # TODO: Implement this method.
    def calculate_BMI(self):
        """ Section b) This method calculates the BMI of the user and
            displays it. First the method will get the values of
            height and weight from the GUI components
            self.__height_value and self.__weight_value.  Then the
            method will calculate the value of the BMI and show it in
            the element self.__result_text.

            Section e) Last, the method will display a verbal
            description of the BMI in the element
            self.__explanation_text.
        """
      
        try:
            weight = float(self.__weight_value.get())
            height = float(self.__height_value.get()) / 100
            bmi = weight / (height * height)
            if weight < 0 or height < 0:
                self.__explanation_text.configure(text='Error: height and weight must be positive.')
                self.reset_fields()
                pass
            else:
                self.__result_text.configure(text='{:.2f}'.format(bmi))
                if bmi < 18.5:
                    self.__explanation_text.configure(text='You are underweight.')
                if 18.5 < bmi < 25:
                    self.__explanation_text.configure(text="Your weight is normal.")
                if bmi > 25:
                    self.__explanation_text.configure(text="You are overweight.")

        except ValueError:
            self.__explanation_text.configure(text='Error: height and weight must be numbers.')

    # TODO: Implement this method.
    def reset_fields(self):
        """ In error situations this method will zeroize the elements
            self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def stop(self):
        """ Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """ Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    ui = Userinterface()
    ui.start()


main()