###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 27 exercises - Christopher Hagan
#
###################################

# args example
def add(*args):
    result = 0
    for value in args:
        result += value

    return result

result_of_addition = add(15, 6, 12)
print(result_of_addition)

# kwargs example
def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n

result_of_calculation = calculate(2, add=3, multiply=5)
print(result_of_calculation)
