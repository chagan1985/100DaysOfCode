###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 27 exercises - Christopher Hagan
#
###################################

import tkinter

window = tkinter.Tk()
window.title('GUI title')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)

def button_clicked():
    print('I got clicked')
    my_label.config(text=input.get())

button = tkinter.Button(text='Click me', command=button_clicked)
button.grid(column=1,row=1)

input = tkinter.Entry(width=10)
input.grid(column=3, row=3)

new_label = tkinter.Label(text='new')
new_label.grid(column=2, row=0)

window.mainloop()
