###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 7 project - Christopher Hagan
#
###################################

import random
from hangman_words import word_list
import hangman_art

chosen_word = random.choice(word_list)
lives = 6
won = False

print('{}\nI have throught of a word...'.format(hangman_art.logo))

already_guessed = []
display = []
for i in range(len(chosen_word)):
    display.append('_')

while '_' in display and lives > 0:
    user_guess = input('Your guess is : ').lower()

    if user_guess in already_guessed:
        print('You have already guessed this letter, please try again...')
        continue
    else:
        already_guessed.append(user_guess)
    
    if user_guess in chosen_word:
        for i in range(len(chosen_word)):
            if user_guess == chosen_word[i]:
                display[i] = user_guess

        if '_' not in display:
            won = True
    else:
        lives -= 1
        print('\nThe letter \'{}\' is not in this word'.format(user_guess))

    for i in display:
        print(i, end=" ")
    print('{}'.format(hangman_art.stages[lives]))


if won:
    print('\n\nCongratulations you won!\n\n')
else:
    print('\n\nSorry you lost!\n\nThe word was {}\n'.format(chosen_word))
