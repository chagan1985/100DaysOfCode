###################################
#
# 100 Days of code bootcamp 2022
# (Udemy course by Angela Yu)
# 
# Day 47 exercise - Christopher Hagan
#
###################################

import argparse
import getpass
import smtplib
from requests import get
from bs4 import BeautifulSoup

PRODUCT_URL = 'https://www.amazon.com/TUBBZ-Kratos-Collectible-Rubber-Figurine/dp/B08CKYSR8R'
AMAZON_REQUIRED_HEADER = {
    'Accept-Language': 'en-GB,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}
GMAIL_SMTP = 'smtp.gmail.com'
GMAIL_PORT = 587

BELOW_PRICE_LIMIT = 25.00

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
    arguments['password'] = getpass.getpass('Enter your (app-specific) Password: ')

if arguments['recipient'] is None:
    arguments['recipient'] = input('Enter the recipient\'s email: ')

# Scrape the product from Amazon, it does require some HEADER information
get_product_details = get(headers=AMAZON_REQUIRED_HEADER, url=PRODUCT_URL)
soup = BeautifulSoup(get_product_details.text, 'html.parser')

# Get the price and convert it to a float
price = soup.find(id='price_inside_buybox', class_='a-size-medium a-color-price')
price_as_float = float(price.text.replace('$', ''))

if price_as_float < BELOW_PRICE_LIMIT:
    with smtplib.SMTP(GMAIL_SMTP, GMAIL_PORT) as connection:
        connection.starttls()
        connection.login(user=arguments['user'], password=arguments['password'])
        connection.sendmail(
            from_addr=arguments['user'], 
            to_addrs=arguments['recipient'], 
            msg=f'Subject: Price below desired limit for {PRODUCT_URL}'
        )
