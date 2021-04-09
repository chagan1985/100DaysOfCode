###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 18 exercises - Christopher Hagan
#
###################################

from random import randint
import turtle as t

turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)
turtle.speed('fastest')

# Exercise 18-7 spirograph
def random_colour_choice():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    return (red, green, blue)


numberOfSpirals = 60
for i in range(1, numberOfSpirals + 1):
    turtle.setheading(i * 360 / numberOfSpirals)
    turtle.color(random_colour_choice())
    turtle.circle(100)

screen.exitonclick()