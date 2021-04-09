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
turtle.color('blue')

screen = Screen()

# Exercise 18-1 draw a square with turtle
for _ in range(0, 4):
    turtle.forward(100)
    turtle.right(90)

screen.exitonclick()
