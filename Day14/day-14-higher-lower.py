###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
#
# Day 14 project - Christopher Hagan
#
###################################

from game_data import data
import art
import random


def format_person(person):
    """Format and return the persons data as a string for comparison"""
    text_to_display = '{}, a {}, from {}'.format(
                                                person['name'],
                                                person['description'],
                                                person['country'])
    return text_to_display


def result(person_a_followers, person_b_followers, guess):
    """Evaluate the followers of person 'a' and person 'b' against the guess"""
    if person_a_followers > person_b_followers and guess == 'a':
        return True
    elif person_b_followers > person_a_followers and guess == 'b':
        return True
    else:
        return False


print(art.logo)

person_a_random_value = random.randint(0, len(data)-1)
# Set person B equal to person A initially so they equate to equal
person_b_random_value = person_a_random_value

score = 0
keep_guessing = True
while keep_guessing:
    while person_b_random_value == person_a_random_value:
        person_b_random_value = random.randint(0, len(data)-1)

    person_a = data[person_a_random_value]
    person_b = data[person_b_random_value]

    print('Compare A: {}'.format(format_person(person_a)))
    print(art.vs)
    print('Against B: {}'.format(format_person(person_b)))
    user_guess = ''
    while not user_guess:
        user_guess = input('Who has more followers? Type \'A\' or \'B\': ').lower()
        if user_guess not in ['a', 'b']:
            user_guess = ''
            print('Invalid entry')

    result_of_guess = result(person_a_followers=person_a['follower_count'],
                            person_b_followers=person_b['follower_count'],
                            guess=user_guess)

    if result_of_guess:
        score += 1
        person_a_random_value = person_b_random_value
        print('\n**\nYou\'re right! Current score: {}.\n**\n'.format(score))
    else:
        keep_guessing = False

print('Sorry that\'s wrong. Final score {}'.format(score))
