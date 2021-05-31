###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 27 project - Christopher Hagan
#
###################################

from tkinter import *

def conversion():
    km_conversion = float(miles.get()) * 1.609
    km_value_label.config(text=km_conversion)

window = Tk()
window.title('Mile to KM conversion')
window.minsize(width=150, height=200)
window.config(padx=20, pady=20)

miles = Entry(width=10)
miles.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)

km_value_label = Label(text='0')
km_value_label.grid(column=1, row=1)

km_label = Label(text='KM')
km_label.grid(column=2, row=1)

calculate_button = Button(text='Calculate', command=conversion)
calculate_button.grid(column=1, row=2)

window.mainloop()
