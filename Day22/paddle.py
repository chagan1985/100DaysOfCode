from turtle import Turtle, shapesize

MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x_pos, y=y_pos)

    def up(self):
        self.goto(x = self.xcor(), y= self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.goto(x = self.xcor(), y= self.ycor() - MOVE_DISTANCE)
