###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 35 exercise - Christopher Hagan
#
###################################

import requests
import argparse
import getpass
import smtplib
from datetime import *

from requests.models import encode_multipart_formdata

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_ADVANGATE_API_KEY = 'VK85N8STSHWU0HLW'
ALPHA_ADVANTAGE_URL = 'https://www.alphavantage.co/query'

NEWS_API_KEY = 'a42ed3edd1b34faf85da3d5650239fb6'
NEWS_URL = 'https://newsapi.org/v2/everything'


def getArguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-e", "--email", required=False,
                    help="Email address")
    ap.add_argument("-p", "--password", required=False,
                    help="Password for user")
    args = vars(ap.parse_args())
    return args


arguments = getArguments()
yesterday = date.today() - timedelta(days = 1)
last_three_articles = ''


if arguments['email'] is None:
    arguments['email'] = input('Enter your Email: ')

if arguments['password'] is None:
    arguments['password'] = getpass.getpass('Enter your Password: ')

query_stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': ALPHA_ADVANGATE_API_KEY
}

stocks_response = requests.get(url=ALPHA_ADVANTAGE_URL, params=query_stock_params)
stocks_response.raise_for_status()
compact_report = stocks_response.json()['Time Series (Daily)']

last_two_days_in_report_list = list(compact_report)[:2]

### REMOVE ###
yesterday = '2021-07-30'
###

try:
    # Don't fire if there was no trading yesterday, ie prevent it from repeating over a weekend break
    yesterday_closing_value = float(compact_report[yesterday]['4. close'])

except:
    print('There was no trading yesterday')

else:
    before_yesterday_closing_value = float(compact_report[last_two_days_in_report_list[1]]['4. close'])
    one_percent_previous_closing_value = (before_yesterday_closing_value / 100) * 1

    if (yesterday_closing_value < before_yesterday_closing_value - (one_percent_previous_closing_value * 5) ) or \
        (yesterday_closing_value > before_yesterday_closing_value + (one_percent_previous_closing_value * 5)):

        difference_in_stock = (yesterday_closing_value - before_yesterday_closing_value) % one_percent_previous_closing_value
        news_params = {
            'q': COMPANY_NAME,
            'language': 'en',
            'sortBy': 'publishedAt',
            'from': last_two_days_in_report_list[1],
            'apiKey': NEWS_API_KEY
        }
        news_response = requests.get(url=NEWS_URL, params=news_params)
        news_response.raise_for_status()
        last_three_articles = news_response.json()['articles'][:3]

    else:
        print("All fine in stock town...")


if last_three_articles:

    if difference_in_stock < 0:
        email_subject = 'Down {}%'.format(int(difference_in_stock))
    else:
        email_subject = 'Up {}%'.format(int(difference_in_stock))

    email_body = ''
    
    for article in last_three_articles:
        email_body += 'HEADLINE: {}Brief: {}---'.format(article['title'], article['description'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=arguments['email'], password=arguments['password'])
        connection.sendmail(
                from_addr=arguments['email'], 
                to_addrs=arguments['email'], 
                msg='Subject:{}\n\n{}'.format(email_subject, email_body.encode('utf-8'))
        )
