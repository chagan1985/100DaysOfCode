###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 28 project - Christopher Hagan
#
###################################


from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='0:00')
    header.config(text='Timer', fg=GREEN)
    iterations.config(text='')
    global repetitions
    repetitions = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repetitions
    repetitions += 1

    if repetitions % 8 == 0:
        header.config(text='Break', fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    if repetitions % 2 == 0:
        header.config(text='Break', fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        header.config(text='Work', fg=GREEN)
        count_down(WORK_MIN * 60)

    count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = '0{}'.format(count_sec)

    canvas.itemconfig(timer_text, text = '{}:{}'.format(count_min, count_sec))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        ticks = ''
        for i in range(math.floor(repetitions/2)):
            ticks += '✔'    
        iterations.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

header = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42))
header.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start = Button(text='Start', command=start_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', command=reset_timer)
reset.grid(column=2,row=2)

iterations = Label(fg=GREEN, bg=YELLOW)
iterations.grid(column=1, row=3)

window.mainloop()
