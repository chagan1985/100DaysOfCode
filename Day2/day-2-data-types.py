###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 2 exercises - Christopher Hagan
#
###################################

# String - substrings
print("Hello\n\n"[4])

# Floats can be made more human readable, Python ignores the underscores
value = 1_987_123.89
print('A float value might be {}\n\n'.format(value))

# The type keyword can tell you the data type of a variable
shouldBeInteger = 12
print(type(shouldBeInteger))

# Exercise 2-1 Add to digits (No validation)
number = input('\n\nType a two digit number: ')
result = int(number[0]) + int(number[1])
print('{}\n\n'.format(result))

# Exercise 2-2 BMI calculator
height = input('Please enter your height in m: ')
weight = input('Please enter your weight in kg: ')
bmi = float(weight) / float(height) ** 2
print('Your BMI is: {}\n\n'.format(round(bmi, 0)))

# Exercise 2-3 Life in weeks, how long you have left assuming you live to 90
age = input('What is your current age? ')
timeLeft = 90 - int(age)
print('You have {} days, {} weeks or {} months left to live...'.format(
    timeLeft * 365,
    timeLeft * 52,
    timeLeft * 12
))
