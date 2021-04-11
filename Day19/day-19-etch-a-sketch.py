###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 19 exercises - Christopher Hagan
#
###################################

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
movement_distance = 10
rotation_amount = 30

def move_forwards():
    turtle.forward(movement_distance)

def move_backwards():
    turtle.backward(movement_distance)

def rotate_clockwise():
    turtle.left(rotation_amount)

def rotate_anticlockwise():
    turtle.right(rotation_amount)

def clear_screen():
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.clear()

screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(rotate_clockwise, 'd')
screen.onkey(rotate_anticlockwise, 'a')
screen.onkey(clear_screen, 'c')

screen.exitonclick()
