###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 3 exercises - Christopher Hagan
#
###################################


# Exercise 3-1 Odd or Even
number = int(input('Which number do you want to check? '))

if (number % 2 == 0):
    number_type = 'Even'
else:
    number_type = 'Odd'
    
print('You have entered an {} number...\n\n'.format(number_type))


# Exercise 3-2 BMI Calculator 2.0
height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

bmi = round(weight / height ** 2, 2)
print(bmi)
if bmi < 18.5:
    body_type = 'underweight'
elif bmi < 25:
    body_type = 'normal weight'
elif bmi < 30:
    body_type = 'overweight'
elif bmi < 35:
    body_type = 'obese'
elif bmi > 35:
    body_type = 'clinically obese'
else:
    print('You should not see me!')

print('Based upon your BMI value you are {}\n\n'.format(body_type))


# Exercise 3-3 Leap year
year = int(input('Which year do you want to check? '))

if (year % 4 == 0):
    if (year % 100 == 0 and year % 400 != 0):
        leap_year = False
    else:
        leap_year = True    
else:
    leap_year = False

print('The year you entered is a leap year' if leap_year else 'The year you entered is not a leap year')


# Exercise 3-4 Pizza order
print('\n\nWelcome to Python Pizza Deliveries!')
size = input('What size pizza do you want? S, M or L: ')
add_pepperoni = input('Do you want pepperoni? Y or N: ')
extra_cheese = input('Do you want extra cheese? Y or N: ')

if size.lower().startswith('s'):
    cost = 15
    if add_pepperoni.lower().startswith('y'):
        cost += 2
else:
    if size.lower().startswith('m'):
        cost = 20
    elif size.lower().startswith('l'):
        cost = 25
    else:
        print('Catch error')
        cost = 0
    
    if add_pepperoni.lower().startswith('y'):
        cost += 3

if extra_cheese.lower().startswith('y'):
    cost += 1

print('The total cost of your pizza is £{}.'.format(cost))


# Exercise 3-5 Love claculator
print('\n\nWelcome to the love calculator!')
your_name = input('Please enter your name: ')
partner_name = input('Please enter your partner\'s name: ')
concantenated_names = your_name + partner_name

total = 0
for letter in 'true':
    total += concantenated_names.lower().count(letter)

total = total * 10

for letter in 'love':
    total += concantenated_names.lower().count(letter)

if (total < 10) or (total > 90):
    print('Your score is {}, you go together like coke and mentos!'.format(total))
elif (total >= 40) and (total <= 50):
    print('Your score is {}, you are alright together.'.format(total))
else:
    print('Your score is {}'.format(total)) 
