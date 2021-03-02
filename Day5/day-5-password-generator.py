###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 5 project - Christopher Hagan
#
###################################

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')

requiredLetters = int(input('How many letters would you like in your password? : '))
requiredSymbols = int(input('How many numbers would you like in your password? : '))
requiredNumbers = int(input('How many symbolss would you like in your password? : '))

password = ''
lettersCurrentlyInPassword = 0
numbersCurrentlyInPassword = 0
symbolsCurrentlyInPassword = 0
for i in range(0, requiredLetters + requiredNumbers + requiredSymbols):
    possibleItemInPassword = []
    if lettersCurrentlyInPassword < requiredLetters:
        possibleItemInPassword.append(1)
    if numbersCurrentlyInPassword < requiredNumbers:
        possibleItemInPassword.append(2)
    if symbolsCurrentlyInPassword < requiredSymbols:
        possibleItemInPassword.append(3)

    randomChoice = random.choice(possibleItemInPassword)
    if randomChoice == 1:
        password += random.choice(letters)
    if randomChoice == 2:
        password += random.choice(numbers)
    if randomChoice == 3:
        password +=random.choice(symbols)

print('Your password is "{}".'.format(password))
