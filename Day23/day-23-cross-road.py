###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 23 project - Christopher Hagan
#
###################################

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_turtle = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player_turtle.up, 'Up')

game_is_on = True
while game_is_on:
    car.move_cars()

    if player_turtle.passed_finish():
        player_turtle.reset_position()
        car.increase_speed()
        score.increase_level()

    for single_car in car.cars_list:
        if player_turtle.distance(single_car) < 20:
            score.game_over()
            game_is_on = False

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
