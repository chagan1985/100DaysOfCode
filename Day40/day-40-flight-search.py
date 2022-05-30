###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 40 exercise - Christopher Hagan
#
###################################

import requests


GOOGLE_SHEET = 'https://api.sheety.co/5710e198fa764d93a9b36437674c6aa2/flightDeals/users/'
HEADER = {'Authorization': 'Bearer SECRETTOKEN'}

def main():
    print('What is your first name?')
    first_name = input()
    print('What is your last name?')
    last_name = input()

    email_first = 'not_set'
    email_second = 'also_not_set'
    while email_first != email_second:
        print('What is your email?')
        email_first = input()
        print('Type your email again.')
        email_second = input()

        if email_first != email_second:
            print('Email did not match, please try again...')

    user_data = {
        'user':{
            'first name': first_name,
            'last name': last_name,
            'email': email_first
        }
    }
    print(user_data)
    post_response = requests.post(url=GOOGLE_SHEET, json=user_data, headers=HEADER)
    print(post_response.status_code)
    print(post_response.text)
    if post_response.status_code == 200:
        print('You\'re in the club!')
    else:
        print('Unexpected error adding customer')



if __name__ == "__main__":
    main()
