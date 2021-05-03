###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 20 & 21 project - Christopher Hagan
#
###################################

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highscore.txt') as high_score_file:
            self.high_score = int(high_score_file.read())
        self.hideturtle()
        self.color('white')
        self.goto(-25, 280)
        self.print_score()


    def print_score(self):
        self.clear()
        self.write('Score : {}   High Score : {}'.format(self.score, self.high_score), align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', mode='w') as high_score_file:
                high_score_file.write(str(self.high_score))
        self.score = 0
        self.print_score()


    def game_over(self):
        self.goto(-25, 0)
        self.write('GAME OVER...', align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.print_score()
