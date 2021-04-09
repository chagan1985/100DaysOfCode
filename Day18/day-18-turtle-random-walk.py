###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 18 exercises - Christopher Hagan
#
###################################

from random import choice
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
colors = ['green', 'orange', 'purple', 'red', 'yellow']

# Exercise 18-4 random walk
turtle.pensize(10)
for x in range(0, 150):
    turtle.color(choice(colors))
    turtle.setheading(choice([0, 90, 180, 270]))
    turtle.forward(20)

screen.exitonclick()
