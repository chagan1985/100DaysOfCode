###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 8 exercises - Christopher Hagan
#
###################################

import math

# Exercise 8-1 Paint Calculator
def paint_calc(height, width, cover):
    paint_needed = (height * width) / coverage
    print('You will need {} cans of paint.\n\n'.format(math.ceil(paint_needed)))

# Supplied code
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Exercise 8-2 Prime Number
def prime_checker(number):
    prime = True
    for i in range(2, number):
        if (number % i == 0):
            prime = False

    if prime:
        print('This is a prime number.')
    else:
        print('This is not a prime number.')


# Supplied code
n = int(input("Check this number: "))
prime_checker(number=n)
