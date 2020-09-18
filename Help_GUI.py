from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class Start:
    def __init__(self, partner):

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Quiz Game Heading (row 0)
        self.math_quiz_label = Label(self.start_frame, text="Math Quiz Game",
                                     font="Arial 16 bold")
        self.math_quiz_label.grid(row=1)

        # Help Button (row 2)
        self.help_button = Button(self.start_frame, text="Help/Rules",
                                  command=self.to_quiz)
        self.help_button.grid(row=2, pady=10)

    def to_quiz(self):
        get_help = Help(self)

class Help:
    def __init__(self, partner):
        background_color = "#EA6B66"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # If user press cross at top, closes export and 'releases' export button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background_color)
        self.help_frame.grid()
        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame,
                                 text="Help / Rules",
                                 font="arial 20 bold", bg=background_color)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="As you can see this is a Math Quiz Game"
                                    " This includes addition and multiplication.\n"
                                    "\n"
                                    "In order to play this Math Quiz Game.\n"
                                    "\n"
                                    "The first box on the top is the Amount of questions you want.\n"
                                    "\n"
                                    "The second box is for the lowest number you want, e.g if you put 5, the questions will be asked won't go less than 5.\n"
                                    "\n"
                                    "Lastly the third box is for the highest number you want, e.g if you put 20, the questions will be asked won't go more than 20.\n "
                                    "\n",
                               justify=LEFT, width=50, bg=background_color, wrap=400, font="arial 15 ")
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_button = Button(self.help_frame, text="Dismiss", width=10, bg="maroon",
                                     font="arial 12 bold",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10)


    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()

