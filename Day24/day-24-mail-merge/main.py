###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 24 mail merge project - Christopher Hagan
#
###################################

BASE_LETTER = './Input/Letters/starting_letter.txt'
RECIPIENTS_FILE = './Input/Names/invited_names.txt'

def get_letter_format(letter_file):
    with open(letter_file) as base_letter_file:
        letter = base_letter_file.read()

    return letter

def get_recipients(recipients_file):
    list_of_recipients = []
    with open(recipients_file) as base_recipient_file:
        for line in base_recipient_file:
            list_of_recipients.append(line.strip('\n'))
    
    return list_of_recipients

def format_letter(initial_letter, recipient, text_replacement='[name]'):
    return initial_letter.replace(text_replacement, recipient)


letter = get_letter_format(letter_file=BASE_LETTER)

recipients = get_recipients(recipients_file=RECIPIENTS_FILE)
print(recipients)

for name in recipients:
    with open ('./Output/ReadyToSend/Invite to {}.txt'.format(name), mode='w') as final_letter_file: 
        final_letter_file.write(format_letter(letter, name))
