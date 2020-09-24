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

        # Games button (row 2)
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

        # Stats / help button frame (row 5)
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

        Game(self, op, starting_question, lower_amount, higher_amount)

class Game:
    def __init__(self, partner, op, starting_question, lower_amount, higher_amount):
        self.correct = IntVar()
        self.correct.set(0)

        lower_amount = int(lower_amount)
        higher_amount = int(higher_amount)
        self.history_questions = []
        background_color = "white"

        starting_question = int(starting_question)
        questions_played = int(1)
        how_many_correct = int(0)

        op = int(op)

        # Generates addition
        if op == 1:
            higher_low_number = random.randrange(lower_amount, higher_amount)
            higher_low_number2 = random.randrange(lower_amount, higher_amount)
            questions = "{} + {}".format(higher_low_number, higher_low_number2)
            var_correct = higher_low_number + higher_low_number2
            self.correct.set(var_correct)
            op_text = "Quiz / Easy Mode"
        # Generates Multiplication
        elif op == 3:
            higher_low_number = random.randrange(lower_amount, higher_amount)
            higher_low_number2 = random.randrange(lower_amount, higher_amount)
            questions = "{} x {}".format(higher_low_number, higher_low_number2)
            var_correct = higher_low_number * higher_low_number2
            self.correct.set(var_correct)
            op_text = "Quiz / Hard Mode"

        self.history_questions.append(questions)

        # disable button
        partner.easy_button.config(state=DISABLED)
        partner.hard_button.config(state=DISABLED)
        partner.help_button.config(state=DISABLED)

        # Set up Geo game one
        self.easy_box = Toplevel()

        # Set up GUI Frame
        self.game_frame = Frame(self.easy_box, width=300, bg=background_color)
        self.game_frame.grid()
        # Set up Geo Instruction heading (row 0)
        self.heading = Label(self.game_frame, text=op_text,
                             font="arial 20 bold", bg=background_color, fg="#8589FF")
        self.heading.grid(row=0)
        # Geo text (label, row 1)
        self.game = Label(self.game_frame,
                          text="Fill the boxes",
                          justify=LEFT, width=50, bg=background_color, wrap=200)
        self.game.grid(row=1)

        self.ask_questions_frame = Frame(self.game_frame, bg=background_color)
        self.ask_questions_frame.grid(row=1)

        self.get1_label = Label(self.ask_questions_frame,
                                text=questions,
                                font="arial 10 bold", fg="black", bg=background_color)
        self.get1_label.grid(row=1)

        self.game_entry = Entry(self.ask_questions_frame, font="arial 10 bold")

        self.game_entry.grid(row=2)

        self.dismiss_export_frame = Frame(self.game_frame, bg=background_color)
        self.dismiss_export_frame.grid(row=2)

        # Dismiss button (row 4)
        self.dismiss_button = Button(self.dismiss_export_frame, text="Dismiss", width=10, bg="#8589FF", fg="black",
                                     font="arial 10 bold", pady=7,
                                     command=partial(self.close_game, partner))
        self.dismiss_button.grid(row=2, column=2)
        self.check_answer_button = Button(self.dismiss_export_frame, text="Check Ans", font="arial 10 bold", fg="black",
                                    bg="#8589FF", pady=7, width=13,
                                    command=lambda: self.check_answer(lower_amount, higher_amount, op, starting_question,
                                                                   questions_played, how_many_correct,
                                                                   self.history_questions))
        self.check_answer_button.grid(row=1, column=1)

    def check_answer(self, lower_amount, higher_amount, op, starting_question, questions_played, how_many_correct,
                  history_questions):
        answer = self.game_entry.get()
        self.game_entry.config(state=DISABLED)

        # Set error background colour
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        var_correct = self.correct.get()

        # change background to white (for testing purposes) ...
        self.check_answer_button.config(bg="#EA6B66")
        self.check_answer_button.config(text="")

        try:
            answer = int(answer)
            correct = int(var_correct)
            self.history_questions.append(answer)

            if answer != correct:
                has_error = "yes"
                self.feedback_label = Label(self.ask_questions_frame, text="Incorrect",
                                            font="arial 10 bold", fg="black", bg="white", pady=8, width=25)
                self.feedback_label.grid(row=3)

            elif answer == correct:
                has_error = "no"
                self.feedback_label = Label(self.ask_questions_frame, text="Good Job!",
                                            font="arial 10 bold", fg="black", bg="white", pady=7, width=25)
                self.feedback_label.grid(row=3)
                how_many_correct += 1

        except ValueError:
            has_error = "yes"
            self.feedback_label = Label(self.ask_questions_frame, text="Needs Answer!",
                                        font="arial 10 bold", fg="black", bg="white", pady=7, width=25)
            self.feedback_label.grid(row=3)

        if questions_played >= starting_question:
            self.finished_button = Label(self.dismiss_export_frame, text="Your Done!", font="arial 10 bold", fg="black",
                                      bg="#8589FF", pady=9, width=14)
            self.finished_button.grid(row=1, column=1)
            self.export_button = Button(self.dismiss_export_frame, text="Export", font="arial 13 bold", fg="black",
                                        bg="#8589FF", pady=7, width=10,
                                        command=lambda: self.export(lower_amount, higher_amount, questions_played,
                                                                    how_many_correct, history_questions))
            self.export_button.grid(row=1, column=2)
        else:
            self.check_answer_button.config(text="")
            self.next_btn = Button(self.dismiss_export_frame, text="Go Next", font="arial 10 bold", fg="black",
                                   bg="#8589FF", pady=7, width=13,
                                   command=lambda: self.next(lower_amount, higher_amount, op, starting_question,
                                                             questions_played, how_many_correct, history_questions))
            self.next_btn.grid(row=1, column=1)

            self.played_label = Label(self.ask_questions_frame, font="arial 12 bold", fg="black",
                                      bg="#8589FF", pady=7,
                                      text="Number Of Question:{}/{}".format(questions_played, starting_question))
            self.played_label.grid(row=0)

    def next(self, lower_amount, higher_amount, op, starting_question, questions_played, how_many_correct, history_questions):
        starting_question = int(starting_question)
        self.game_entry.config(state=NORMAL)
        self.game_entry.delete(0, 'end')

        # Generates Addition//Multiplication
        if op == 1:
            higher_low_number = random.randrange(lower_amount, higher_amount)
            higher_low_number2 = random.randrange(lower_amount, higher_amount)
            questions = "{} + {}".format(higher_low_number, higher_low_number2)
            self.get1_label.config(text=questions)
            var_correct = higher_low_number + higher_low_number2
            self.correct.set(var_correct)
            questions_played += 1
            print(questions_played)
        elif op == 2:
            higher_low_number = random.randrange(lower_amount, higher_amount)
            higher_low_number2 = random.randrange(lower_amount, higher_amount)
            questions = "{} - {}".format(higher_low_number, higher_low_number2)
            self.get1_label.config(text=questions)
            var_correct = higher_low_number - higher_low_number2
            self.correct.set(var_correct)
            questions_played += 1
        elif op == 3:
            higher_low_number = random.randrange(lower_amount, higher_amount)
            higher_low_number2 = random.randrange(lower_amount, higher_amount)
            questions = "{} x {}".format(higher_low_number, higher_low_number2)
            self.get1_label.config(text=questions)
            var_correct = higher_low_number * higher_low_number2
            self.correct.set(var_correct)
            questions_played += 1

        self.history_questions.append(questions)

        # Checks answers whether its right or wrong
        self.check_answer_button = Button(self.dismiss_export_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#8589FF", pady=7, width=13,
                                    command=lambda: self.check_answer(lower_amount, higher_amount, op,
                                                                   starting_question, questions_played, how_many_correct,
                                                                   history_questions))
        self.check_answer_button.grid(row=1, column=1)

    def close_game(self, partner):
        # Put help button back to normal
        partner.easy_button.config(state=DISABLED)
        partner.question_amount_button.config(state=NORMAL)
        partner.hard_button.config(state=DISABLED)
        partner.help_button.config(state=NORMAL)
        partner.lower_number_entry.config(state=NORMAL)
        partner.higher_number_entry.config(state=NORMAL)
        partner.amount_entry.config(state=NORMAL)

        self.easy_box.destroy()

    def export(self, lower_amount, higher_amount, questions_played, how_many_correct, history_questions):
        Export(self, lower_amount, higher_amount, questions_played, how_many_correct, history_questions)

class Export:
    def __init__(self, partner, lower_amount, higher_amount, questions_played, how_many_correct, history_questions):
        print(lower_amount, higher_amount, questions_played, how_many_correct)
        print(history_questions)

        background_color = "#8589FF"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Set up child window (ie: export box)
        self.export_box = Toplevel()

        # If user press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background_color)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame,
                                 text="Export", fg="black",
                                 font="arial 20 bold", bg=background_color)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                                         "in the box below "
                                                         "to save your "
                                                         "game history ",

                                 font="arial 13 italic",
                                 justify=LEFT, width=50, bg=background_color, wrap=200)
        self.export_text.grid(row=1)

        # Help text (label, row 1)
        self.history_label = Label(self.export_frame, text="The low number had: {}""\n"
                                                           "The high number had: {}""\n"
                                                           "you have played {} around""\n"
                                                           "you got {} correct out of {}  ""\n"
                                   .format(lower_amount, higher_amount, questions_played, how_many_correct, questions_played),
                                   font="arial 13 italic",
                                   justify=LEFT, width=50, bg=background_color, wrap=200)
        self.history_label.grid(row=2)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                                         "you enter below "
                                                         "already exists, "
                                                         "its contents will "
                                                         "be replaced with "
                                                         "your game "
                                                         "history",
                                 justify=LEFT, bg="#8589FF", fg="black",
                                 font="arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=3, pady=10)

        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="arial 14 bold")
        self.filename_entry.grid(row=4, pady=10)

        # error massage labels (initially blank, row 4 )
        self.save_error_label = Label(self.export_frame, text=" ", fg="black",
                                      bg="#8589FF")
        self.save_error_label.grid(row=5)

        # Save and Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=6, pady=10)

        # Save and Cancel buttons 9row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="arial 10 bold", fg="black",
                                  bg="maroon", padx=10, pady=10,
                                  command=partial(lambda: self.save_history(partner, lower_amount, higher_amount,
                                                                            questions_played, how_many_correct,
                                                                            history_questions)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="arial 10 bold", fg="black",
                                    bg="white", padx=10, pady=10,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, lower_amount, higher_amount, questions_played, how_many_correct, history_questions):
        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            f.write("the low number was: {}""\n".format(lower_amount))
            f.write("the high number was: {}""\n".format(higher_amount))
            f.write("played {} throughout""\n".format(questions_played))
            f.write("you got {} correct out of {}  ""\n".format(how_many_correct, questions_played))
            f.write("{} ""\n".format(history_questions))

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

class Help:
    def __init__(self, partner):
        background_color = "#8589FF"

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
                                    " This includes addition and multiplication \n"
                                    "\n"
                                    "In order to play this Math Quiz Game\n"
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
    root.title("Quiz")
    root.configure(background='white')
    something = Quiz()
    root.mainloop()