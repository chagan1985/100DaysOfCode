###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 23 project - Christopher Hagan
#
###################################

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-220, 260)
        self.write(('Level: {}'.format(self.level)), align='center', font=FONT)

    def increase_level(self):
        self.level += 1
        self.display_score()

    def game_over(self):
        self.goto(-25,0)
        self.write('Game over!', align='center', font=FONT)
