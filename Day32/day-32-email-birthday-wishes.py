###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 32 project - Christopher Hagan
#
###################################

import smtplib
import argparse
import getpass
import pandas
import random
import datetime as dt

def getArguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-u", "--user", required=False,
                    help="Email address")
    ap.add_argument("-p", "--password", required=False,
                    help="Password for user")
    args = vars(ap.parse_args())
    return args


arguments = getArguments()

if arguments['user'] is None:
    arguments['user'] = input('Enter your Email: ')

if arguments['password'] is None:
    arguments['password'] = getpass.getpass('Enter your Password: ')

birthday_data = pandas.read_csv('birthdays.csv')

today = dt.datetime.now()

email_list_df = birthday_data[(birthday_data['month'] == today.month) & (birthday_data['day'] == today.day)]

if not email_list_df.empty:
    for index in email_list_df.index:
        letter = random.choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])
        with open('letter_templates/{}'.format(letter)) as letter_contents:
            email_body = letter_contents.read()

        email_body = email_body.replace('[NAME]', email_list_df['name'][index])

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=arguments['user'], password=arguments['password'])
            connection.sendmail(
                from_addr=arguments['user'], 
                to_addrs=email_list_df['email'][index], 
                msg='Subject:Happy Birthday!\n\n{}'.format(email_body)
            )
