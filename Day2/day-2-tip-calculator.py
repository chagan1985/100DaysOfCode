###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 2 project - Christopher Hagan
#
###################################

print('Welcome to the tip calculator!')
total = float(input('What was the total bill? £'))
percentage_tip = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people will split the bill? '))

total_per_person = ((total + total / 100 * percentage_tip) / people)

print('Each person should pay: £{:.2f}'.format(round(total_per_person, 2)))
