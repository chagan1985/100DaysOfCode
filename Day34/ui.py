###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 34 exercise - Christopher Hagan
#
###################################

from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOUR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOUR)

        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOUR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280,
            text='Question text goes here...', 
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        tick_image = PhotoImage(file='images/true.png')
        self.true = Button(image=tick_image, highlightthickness=0, command=self.true_guess)
        self.true.grid(column=0, row=2)

        cross_image = PhotoImage(file='images/false.png')
        self.false = Button(image=cross_image, highlightthickness=0, command=self.false_guess)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text='Score: {}'.format(self.quiz.score))
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text='You\'re reached the end of the question deck')
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def true_guess(self):
        self.feedback(self.quiz.check_answer('True'))

    def false_guess(self):
        self.feedback(self.quiz.check_answer('False'))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
