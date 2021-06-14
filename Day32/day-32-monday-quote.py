###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 32 exercises - Christopher Hagan
#
###################################


# Sends a motivational quote on a Monday
import smtplib
import argparse
import getpass
import random
import datetime as dt

def getArguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-u", "--user", required=False,
                    help="Email address")
    ap.add_argument("-p", "--password", required=False,
                    help="Password for user")
    ap.add_argument("-r", "--recipient", required=False,
                    help="Recipient email address")
    args = vars(ap.parse_args())
    return args


arguments = getArguments()

if arguments['user'] is None:
    arguments['user'] = input('Enter your Email: ')

if arguments['password'] is None:
    arguments['password'] = getpass.getpass('Enter your Password: ')

if arguments['recipient'] is None:
    arguments['recipient'] = input('Enter the recipient\'s email: ')

with open('quotes.txt') as quote_file:
    quote_today = random.choice(quote_file.readlines())

day_today = dt.datetime.now()

# Weekday is a 0 based integer value
if day_today.weekday() == 0:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=arguments['user'], password=arguments['password'])
        connection.sendmail(
            from_addr=arguments['user'], 
            to_addrs=arguments['recipient'], 
            msg='Subject:Monday quote\n\n{}'.format(quote_today)
        )
