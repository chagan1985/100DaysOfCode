###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 4 project - Christopher Hagan
#
###################################

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('Welcome to Rock, Papers, Scissors!')
moves = [rock, paper, scissors]

user_move = int(input('Which do you choose? Type 0 for rock, 1 for Paper and 2 for Scissors : '))
if user_move in [0, 1, 2]:
    print(moves[user_move])

    cpu_move = random.randint(0,2)
    print('\n\nComputer choice:\n{}\n\n'.format(moves[cpu_move]))

    if moves[user_move-1] == moves[cpu_move]:
        print('You win!')
    elif moves[cpu_move-1] == moves[user_move]:
        print('You lose!')
    else:
        print('Tie')
else:
    print('Invalid move')
