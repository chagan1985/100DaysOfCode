###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 26 project - Christopher Hagan
#
###################################

import pandas

nato_alphabet_file = 'nato_phonetic_alphabet.csv'
alphabet_data = pandas.read_csv(nato_alphabet_file)

phonetic_alphabet = {rows.letter:rows.code for (item, rows) in alphabet_data.iterrows()}

code_word = input('Enter a word to translate: ')

code_list = [phonetic_alphabet[code_letter.upper()] for code_letter in code_word]

print(code_list)
