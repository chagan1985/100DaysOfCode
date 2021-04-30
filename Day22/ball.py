from turtle import Turtle

START_X = 0
START_Y = 0

class Ball(Turtle):

    def __init__(self, x_pos=START_X, y_pos=START_Y):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('circle')
        self.goto(START_X, START_Y)
        self.x_speed = 10
        self.y_speed = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(
            self.xcor() + self.x_speed,
            self.ycor() + self.y_speed
        )

    def bounce_and_reverse(self, x_dir=-1, y_dir=-1, move_speedup=1):
        self.x_speed *= x_dir
        self.y_speed *= y_dir
        self.move_speed *= move_speedup

    def reset_ball(self, x_pos=START_X, y_pos=START_Y):
        self.goto(x_pos, y_pos)
        self.bounce_and_reverse(x_dir=-1, y_dir=1)
        self.move_speed = 0.1
