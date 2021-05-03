###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 20 & 21 project - Christopher Hagan
#
###################################

from turtle import Turtle

STARTING_POSITIONS = [(-20, 0), (0, 0), (20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.whole_snake = []
        self.create_snake()
        self.snake_head = self.whole_snake[0]


    def add_segment(self, position):
        newSnakeTile = Turtle('square')
        newSnakeTile.color('white')
        newSnakeTile.penup()
        newSnakeTile.goto(position)
        self.whole_snake.append(newSnakeTile)


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            

    def extend(self):
        self.add_segment(self.whole_snake[-1].position())


    def move(self):
        for segment_index in range((len(self.whole_snake) - 1), 0, -1):
            new_x = self.whole_snake[segment_index - 1].xcor()
            new_y = self.whole_snake[segment_index - 1].ycor()
            self.whole_snake[segment_index].setpos(new_x, new_y)
        self.whole_snake[0].forward(MOVE_DISTANCE)


    def reset(self):
        for segment in self.whole_snake:
            segment.goto(1000,1000)
        self.whole_snake.clear()
        self.create_snake()
        self.snake_head = self.whole_snake[0]


    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)


    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)


    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)


    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
