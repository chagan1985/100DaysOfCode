###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 30 exercises - Christopher Hagan
#
###################################

# Exercise 30-1 Try and except block with an else
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('Fruit pie')
    else:
        print(fruit + " pie")


make_pie(4)

# Exercise 30-2 Try and except block with a finally
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        likes_for_post = post['Likes']
    except KeyError:
        likes_for_post = 0
    finally:
        total_likes = total_likes + likes_for_post

# Instructor solution looks better - 
# for post in facebook_posts:
#     try:
#         likes_for_post = post['Likes']
#     except KeyError:
#         pass

print(total_likes)

# Exercise 30-3 Phonetic alphabet rewrite with try and except
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word_valid = False
while not word_valid:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as key_error:
        print('Sorry, only letters in the alphabet please...')
    else:
        word_valid = True
        
print(output_list)
