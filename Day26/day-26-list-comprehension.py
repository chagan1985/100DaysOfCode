###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 26 exercises - Christopher Hagan
#
###################################

# Exercise 26-1 Squared numbers in list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [(num * num) for num in numbers]
print(squared_numbers)


# Exercise 26-2 Filtering list for even numbers
numbers_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

even_list = [num for num in numbers_list if (num % 2 == 0)]
print(even_list)


# Exercise 26-3 Overlapping lists
with open ('file1.txt') as file_1:
    file_1_numbers = file_1.readlines()

with open('file2.txt') as file_2:
    file_2_numbers = file_2.readlines()

numbers_in_both = [int(num) for num in file_1_numbers if num in file_2_numbers]

print(numbers_in_both)


# Exercise 26-4 Sentence to a dictionary
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_as_dict = {word:len(word) for word in sentence.split(' ')}

print(sentence_as_dict)


# Exercise 26-5 Convert weather temperature
weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24
}
weather_f = {day:((temp*9/5) + 32) for (day,temp) in weather_c.items()}

print(weather_f)


# Exercise 26-6 Iterate over pandas dataframe
import pandas

student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}

for(key, value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row)

