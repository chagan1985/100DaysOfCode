###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 4 exercises - Christopher Hagan
#
###################################

import random

# Exercise 4-1 coin flip
coin_flip = random.randint(0,1)

if coin_flip == 1:
    print('Heads')
else:
    print('Tails')


# Exercise 4-2 banker roulette
names_string = input('\n\nGive me everybody\'s name separated by a comma. ')
names = names_string.split(',') 

print('{} will pay for today\'s meal.\n\n'.format(names[random.randint(0, len(names)-1)]))


# Exercise 4-3 treasure map

# Code given at start
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# My code
x = int(position[0])
y = int(position[1])

map[x-1][y-1] = 'X'

# Code given for end
print(f"{row1}\n{row2}\n{row3}")
