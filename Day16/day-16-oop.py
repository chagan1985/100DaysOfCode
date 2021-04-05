###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 16 exercise - Christopher Hagan
#
# (prettytable external class required)
#
###################################

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color('brown')
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon name',['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type',['Electric', 'Water', 'Fire'])

table.align = 'l'

print(table)
