###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 10 project - Christopher Hagan
#
###################################

from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

def calculator():
    another_calculation = True
    num1 = float(input('What\'s the first number?: '))

    while another_calculation:
        for key in operations:
            print(key, end = '')
        operation_symbol = input('\nPick an operation from the line above: ')
        num2 = float(input('What\'s the next number?: '))
        result_of_calculation =  operations[operation_symbol](num1, num2)
        print('{} {} {} = {}'.format(num1, operation_symbol, num2, result_of_calculation))

        and_again = input('Type \'y\' to contine calculating with {}, or type \'n\' to exit: '.format(result_of_calculation))

        if and_again.lower().startswith('y'):
            num1 = result_of_calculation
        else:
            another_calculation = False
            calculator()


print(logo)
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

calculator()
