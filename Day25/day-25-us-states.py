###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 25 project - Christopher Hagan
#
###################################

from os import stat
import pandas
import turtle
import random

image = 'blank_states_img.gif'

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.addshape(image)

turtle.shape(image)

states_data = '50_states.csv'
data = pandas.read_csv(states_data)
states_list = data['state'].to_list()

for i in range(len(data)):
    user_guess = ''
    while user_guess not in states_list and user_guess != 'quit':
        user_guess = screen.textinput(title='{}/50 the state'.format(i), prompt='What\'s another state\'s name?')
        
    if user_guess.title() in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        current_state_data = data[data.state == user_guess]
        t.goto(int(current_state_data.x), int(current_state_data.y))
        t.write(current_state_data.state.item())
        states_list.remove(user_guess)
    elif user_guess == 'quit':
        break

if states_list:
    remaining_states = pandas.DataFrame(states_list)
    remaining_states.to_csv('states_to_learn.csv')

screen.exitonclick()
