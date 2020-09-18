from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class Quiz:
    def __init__(self):
        # Formatting variables...
        background_color = "white"

        self.starting_question = IntVar()
        self.starting_question.set(0)

        self.lower_amount = IntVar()
        self.lower_amount.set(0)

        self.higher_amount = IntVar()
        self.higher_amount.set(0)

        # Quiz frame
        self.quiz_frame = Frame(bg=background_color, height=300, width=300,
                                pady=10, padx=10)
        self.quiz_frame.grid(row=4)

        # Entry Frame
        self.entry_frame = Frame(bg=background_color, height=300, width=300,
                                 pady=10, padx=10)
        self.entry_frame.grid(row=2)

        self.error_frame = Frame(bg=background_color, height=300, width=300,
                                 pady=10, padx=10)
        self.error_frame.grid(row=3)

        # Heading (row 0)
        self.maths_label = Label(text="Math Quiz",
                                 font="Arial 32 bold",
                                 fg="#8589FF", bg="white",
                                 padx=10, pady=10)
        self.maths_label.grid(row=0)

        # Entry (for numbers they wanna play between)(row 1)
        self.amount_error_label = Label(self.error_frame, font="arial 10 italic",
                                        text="Choose a level below!", bg=background_color)
        self.amount_error_label.grid(row=5, columnspan=6)

        self.entry_label_1 = Label(self.entry_frame, text="Available numbers of questions are only to 1 to 10!", font="Arial 10",
                                   bg="white", pady=1)
        self.entry_label_1.grid(row=1, column=2, columnspan=3)
        self.amount_entry = Entry(self.entry_frame, width=5,
                                  font="Arial 10 bold", bg="white")
        self.amount_entry.grid(row=1)

        self.entry_label_1 = Label(self.entry_frame, text="What's the lowest number you want in your question?",
                                   font="Arial 10",
                                   bg="white", pady=1)
        self.entry_label_1.grid(row=2, column=2, columnspan=3)
        self.lower_number_entry = Entry(self.entry_frame, width=5,
                                      font="Arial 10 bold", bg="white")
        self.lower_number_entry.grid(row=2)

        self.entry_label_1 = Label(self.entry_frame, text="What's the highest number you want in your question?",
                                   font="Arial 10",
                                   bg="white", pady=1)
        self.entry_label_1.grid(row=3, column=2, columnspan=3)
        self.higher_number_entry = Entry(self.entry_frame, width=5,
                                       font="Arial 10 bold", bg="white")
        self.higher_number_entry.grid(row=3)

        # Game Buttons (row 2)
        self.game_buttons_frame = Frame(self.quiz_frame, bg="white")

        self.game_buttons_frame.grid(row=3, pady=10)

        self.question_amount_button = Button(self.error_frame, text="Submit", font="Arial 14", width=7,
                                             bg="#8589FF", padx=10, pady=10, command=self.check_question)
        self.question_amount_button.grid(row=1, column=0)

        self.easy_button = Button(self.game_buttons_frame,
                                  text="Easy", font="Arial 12", width=10,
                                  bg="light blue", padx=10, pady=10,
                                  command=lambda: self.to_game(1))
        self.easy_button.grid(row=1, column=0)

        self.hard_button = Button(self.game_buttons_frame,
                                  text="Hard", font="Arial 12", width=10,
                                  bg="blue", padx=10, pady=10,
                                  command=lambda: self.to_game(3))
        self.hard_button.grid(row=1, column=1)

        self.help_frame = Frame(self.quiz_frame)
        self.help_frame.grid(row=3)

        self.easy_button.config(state=DISABLED)
        self.hard_button.config(state=DISABLED)


        # stats / help button frame (row 5)
        self.stats_help_frame = Frame(self.quiz_frame)
        self.stats_help_frame.grid(row=4, pady=10)

        self.help_button = Button(self.stats_help_frame, font="Arial 14", bg="#8589FF",
                                  text="Help/Rules", width=12, command=self.help)
        self.help_button.grid(row=0, column=1)

    def help(self):
        print("Help needed?")
        get_help = Help(self)
        get_help.help_text.configure()

    def check_question(self):
        starting_question = self.amount_entry.get()
        lower_amount = self.lower_number_entry.get()
        higher_amount = self.higher_number_entry.get()

        # Set error background colour (and assum that there are no
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        # background to #8589FF
        self.amount_entry.config(bg="#8589FF")
        self.amount_error_label.config(text="")
        self.lower_number_entry.config(bg="#8589FF")
        self.lower_number_entry.config(text="")
        self.higher_number_entry.config(bg="#8589FF")
        self.higher_number_entry.config(text="")

        self.easy_button.config(state=DISABLED)
        self.hard_button.config(state=DISABLED)

        try:
            starting_question = int(starting_question)

            if starting_question < 1:
                has_error = "yes"
                error_feedback = "Number is needed/You can't go lower than 1!"
            elif starting_question > 10:
                has_error = "yes"
                error_feedback = "Sorry but 10 is the highest question in this Quiz"

        except ValueError:
            has_error = "yes"
            error_feedback = "Numbers on all the boxes are needed!"

        try:
            lower_amount = int(lower_amount, )

            if lower_amount < -50:
                has_error = "yes"
                error_feedback = "Sorry but your low number cant go lower than -50"
            elif lower_amount > 50:
                has_error = "yes"
                error_feedback = "Sorry but the low number cant go higher than 50!"

        except ValueError:
            has_error = "yes"
            error_feedback = "You need to fill all of it!"

        try:
            higher_amount = int(higher_amount)

            if higher_amount <= lower_amount:
                has_error = "yes"
                error_feedback = "The high number needs to be higher than the low number!"
            elif higher_amount > 60:
                has_error = "yes"
                error_feedback = "Sorry the high number cannot go higher than 60"

        except ValueError:
            has_error = "yes"
            error_feedback = "You've got to put numbers on all the boxes to start the Quiz!"

        if has_error == "yes":
            self.amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)
            self.higher_number_entry.config(bg=error_back)
            self.lower_number_entry.config(bg=error_back)

        else:
            self.starting_question.set(starting_question)
            self.lower_amount.set(lower_amount)
            self.higher_amount.set(higher_amount)
            self.easy_button.config(state=NORMAL)
            self.hard_button.config(state=NORMAL)
            self.lower_number_entry.config(state=DISABLED)
            self.higher_number_entry.config(state=DISABLED)
            self.amount_entry.config(state=DISABLED)

    def to_game(self, op):
        starting_question = self.amount_entry.get()
        lower_amount = self.lower_number_entry.get()
        higher_amount = self.higher_number_entry.get()
        print(starting_question, lower_amount, higher_amount)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    root.configure(background='white')
    something = Quiz()
    root.mainloop()