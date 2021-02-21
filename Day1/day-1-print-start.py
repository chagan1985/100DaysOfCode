###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 1 exercises - Christopher Hagan
#
###################################

# Print over a few lines
print("""Day 1 - Python Print Function
The function is declared like this:
print('what to print')\n\n""")

# Fixed code
print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.\n\n")

# Input function
print("The number of characters in your name is {}\n\n".format(len(input('What is your name?: '))))

# Variable swapping
a = input("Enter a value for a: ")
b = input("Enter a value for b: ")

# Switch a for b as per exercise instructions using a placeholder
tmp = b
b = a
a = tmp

print('The new value for a is: {}'.format(a))
print('The new value for b is: {}'.format(b))
