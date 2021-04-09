###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 18 exercises - Christopher Hagan
#
###################################

from random import random
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

# Exercise 18-3 drawing shapes
colors = ['green', 'orange', 'purple', 'red', 'yellow']
for i in range(3, 11):
    turtle.color(random.choice(colors))
    for j in range(0, i):
        turtle.forward(100)
        turtle.right(360/i)

screen.exitonclick()
