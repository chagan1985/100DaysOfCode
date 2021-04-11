###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 19 project - Christopher Hagan
#
###################################

from turtle import Turtle, Screen
import random

colour_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
y_spacing = 30
screen = Screen()
screen.setup(width=500, height=400)

def random_move(turtle, max_distance):
    """Moves turtle object forward between 0 and max_distance value each turn
    will return True should the turtle have reached the finish line"""
    turtle.forward(random.randint(0, max_distance))
    if turtle.position()[0] > 240:
        return True

valid_colour = False
racing = False
while not valid_colour:
    user_bet = screen.textinput(title='Make a bet', prompt='Which colour turtle will win the race?').lower()
    if user_bet in colour_list:
        valid_colour = True

y_field = 30 * len(colour_list)
for index in range(len(colour_list)):
    turtle = Turtle(shape='turtle')
    turtle.color(colour_list[index])
    turtle.penup()
    turtle.setpos(x=-240, y= (0 - (y_field // 2)) + (y_spacing * index))
    turtles.append(turtle)

racing = True
while racing:
    max_distance = 10
    for single_turtle in turtles:
        has_finished = random_move(single_turtle, max_distance)
        if has_finished:
            racing = False
            winning_turtle = single_turtle.pencolor()

if winning_turtle == user_bet:
    print('Congratulations, the {} turtle won!'.format(winning_turtle))
else:
    print('Sorry you lost, the {} turtle won!'.format(winning_turtle))

screen.exitonclick()
