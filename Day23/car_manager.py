###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 23 project - Christopher Hagan
#
###################################

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_CARS = 50


class CarManager:
    
    def __init__(self):
        self.cars_list = []
        self.add_car()
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        new_car = Turtle('square')
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(300, random.randint(-250, 250))
        self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            if car.xcor() < -320:
                self.cars_list.remove(car)
            else:
                car.goto(car.xcor() - self.speed, car.ycor()                        )

        if (random.randint(0, 3) == 3) and len(self.cars_list) < MAX_CARS:
            self.add_car()

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
