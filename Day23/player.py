###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 23 project - Christopher Hagan
#
###################################

from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.reset_position()

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def passed_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
