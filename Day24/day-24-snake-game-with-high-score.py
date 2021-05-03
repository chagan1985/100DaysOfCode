###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 24 update to Snake project - Christopher Hagan
#
###################################

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_active = True
while game_active:        
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.snake_head.xcor() < -300 or snake.snake_head.xcor() > 280 or snake.snake_head.ycor() < -280 or snake.snake_head.ycor() > 280:
        snake.reset()
        scoreboard.reset()

    # Detect collision with tail
    for segment in snake.whole_snake[1:]:
        print('head = {}'.format(snake.snake_head))
        print(segment.position())
        if snake.snake_head.distance(segment) < 1:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()
