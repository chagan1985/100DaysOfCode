###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 22 project - Christopher Hagan
#
###################################

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

left_paddle = Paddle(x_pos=-350, y_pos=0)
right_paddle = Paddle(x_pos=350, y_pos=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

game_active = True
while game_active:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_and_reverse(x_dir=1, y_dir=-1)

    if ((ball.xcor() >= 330 and right_paddle.distance(ball) < 50) or
            (ball.xcor() <= -330 and left_paddle.distance(ball) < 50)):
        ball.bounce_and_reverse(x_dir=-1, y_dir=1, move_speedup=0.9)
    
    if ball.xcor() > 400:
        scoreboard.left_point()
        ball.reset_ball()

    if ball.xcor() < -400:
        scoreboard.right_point()
        ball.reset_ball()

    screen.update()

screen.exitonclick()
