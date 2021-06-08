###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 31 project - Christopher Hagan
#
###################################

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv('data/german_words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/200_common_german.csv')
finally:
    german_words_dictionary = data.to_dict(orient='records')

current_card = {}

def new_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(german_words_dictionary)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(title_text, text = 'German', fill='black')
    canvas.itemconfig(word_text, text = '{}'.format(current_card['German']), fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(title_text, text = 'English', fill='white')
    canvas.itemconfig(word_text, text = '{}'.format(current_card['English']), fill='white')

def correct_guess():
    german_words_dictionary.remove(current_card)
    remaining_words = pandas.DataFrame(german_words_dictionary)
    remaining_words.to_csv('data/german_words_to_learn.csv', index=False)
    new_random_word()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=4)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

title_text = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'))

tick_image = PhotoImage(file='images/right.png')
tick_button = Button(image=tick_image, highlightthickness=0, command=correct_guess)
tick_button.grid(column=1, row=1)

cross_image = PhotoImage(file='images/wrong.png')
cross_button = Button(image=cross_image, highlightthickness=0, command=new_random_word)
cross_button.grid(column=0, row=1)

new_random_word()

window.mainloop()
