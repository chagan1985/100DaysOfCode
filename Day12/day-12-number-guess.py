###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 12 project - Christopher Hagan
#
###################################

import random

lives_per_difficulty = {'easy': 10, 'hard': 5}


user_lives = 0
while user_lives == 0:
    difficulty_level = input("""Welcome to the number guessing game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': """).lower()
    if difficulty_level in lives_per_difficulty:
        user_lives = lives_per_difficulty[difficulty_level]
    else:
        print('\n***\nInvalid entry...\n***\n')

random_number = random.randint(1, 100)

for i in range(user_lives, 0, -1):
    print('You have {} attempts remaining to guess the number.'.format(i))
    guess = int(input('Make a guess: '))
    if guess == random_number:
        break
    elif guess < random_number:
        print('Too low')
    elif guess > random_number:
        print('Too high')
    print('Guess again...')

if guess == random_number:
    print('Congratulations, you guessed the number')
else:
    print('You did not guess the number, it was {}, better luck next time'.format(random_number))
