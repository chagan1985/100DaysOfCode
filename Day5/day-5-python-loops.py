###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 5 exercises - Christopher Hagan
#
###################################

# Exercise 5-1 Calculate average height
student_heights = input("Input a list of student heights ").split()

# Instructions - not allowed to use sum or len functions on list
total = 0
numberOfValues = 0

for height in student_heights:
    total += int(height)
    numberOfValues += 1

print('The average height of all the students is {}.\n\n'.format(round(total/numberOfValues, 0)))


# Exercise 5-2 highest score value
student_scores = input("Input a list of student scores ").split()

# Instructions - not allowed to use max function on list
currentMax = 0

for score in student_scores:
    if int(score) > currentMax:
        currentMax = int(score)

print('The highest score was {}.\n\n'.format(currentMax))


# Exercise 5-3 Adding Even numbers
total = 0
for i in range(2,101, 2):
    total += i

print('The total of the even numbers between 1 and 100 is {}.\n\n'.format(total))


# Exercise 5-4 Fizzbuzz
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
