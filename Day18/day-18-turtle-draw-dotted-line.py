###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 18 exercises - Christopher Hagan
#
###################################
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape('turtle')
turtle.color('orange')

screen = Screen()

# Exercise 18-2 draw a dotted line with turtle
for i in range (0, 30):
    if (i % 2 == 0):
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(10)

screen.exitonclick()
