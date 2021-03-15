###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 8 project - Christopher Hagan
#
###################################

from art import logo

letters_in_alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
alphabet = letters_in_alphabet.split(' ')

def caesar(message, shift_index, direction):
    newString = ''
    for message_char in message:
        if message_char in alphabet:
            alphabet_index = alphabet.index(message_char)
            if direction.lower() == 'encode':
                shift_amount = (alphabet_index + shift_index) % 26
            elif direction.lower() == 'decode':
                shift_amount = (alphabet_index - shift_index) % 26
            newString += alphabet[shift_amount]
        else:
            newString += message_char
    
    print('The adjusted text is {}'.format(newString))


print(logo)
keep_encrypting = True
while keep_encrypting:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction.lower() not in ['encode', 'decode']:
        print('I don\'t get it...')
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    go_again = input('Type \'yes\' to go again, otherwise type \'no\' : ')
    if go_again.lower().startswith('n'):
        keep_encrypting = False

print('\nGoodbye!')
