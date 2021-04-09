###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 18 exercises - Christopher Hagan
#
###################################

from random import randint, choice
import turtle as t

turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)

# Exercise 18-6 random walk with RGB colouring
def random_colour_choice():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    return (red, green, blue)


turtle.pensize(10)
for x in range(0, 150):
    turtle.color(random_colour_choice())
    turtle.setheading(choice([0, 90, 180, 270]))
    turtle.forward(20)

screen.exitonclick()
