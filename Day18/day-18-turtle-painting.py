###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 18 project - Christopher Hagan
#
###################################

from random import choice
import colorgram
import turtle as t
from math import sqrt

turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)


def get_colours_from_painting(image):
    """Retrieves some colours from an image file, assumes there are a large variety
    of colours and removes any colours which account for more than 5% of the image
    and returns the other colours as a tuple"""
    colours_list = []
    for colour in colorgram.extract(image, 20):
        red = colour.rgb.r
        green = colour.rgb.g
        blue = colour.rgb.b
        if colour.proportion < 0.05:
            colours_list.append((red, green, blue))

    return colours_list


colours_in_image = get_colours_from_painting(image='spots.jpg')
number_of_dots = 100
turtle.penup()
turtle.hideturtle()
for dot in range(0, number_of_dots):
    turtle.setpos(dot % sqrt(number_of_dots) * 50, dot // sqrt(number_of_dots) * 50)
    turtle.dot(20, choice(colours_in_image))

screen.exitonclick()
