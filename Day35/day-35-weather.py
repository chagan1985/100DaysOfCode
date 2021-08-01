###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 35 exercise - Christopher Hagan
#
###################################

import requests
import smtplib
import argparse
import getpass

API_KEY = '0ed055569b890f044e29a7fe57232405'
URL = 'https://api.openweathermap.org/data/2.5/onecall'

def getArguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-e", "--email", required=False,
                    help="Email address")
    ap.add_argument("-p", "--password", required=False,
                    help="Password for user")
    args = vars(ap.parse_args())
    return args


weather_params = {
    "lat": 54.585630,
    "lon": -5.988890,
    "appid": API_KEY,
    "exclude": 'current,minutely,daily'
}

arguments = getArguments()

if arguments['email'] is None:
    arguments['email'] = input('Enter your Email: ')

if arguments['password'] is None:
    arguments['password'] = getpass.getpass('Enter your Password: ')

response = requests.get(URL, params=weather_params)
response.raise_for_status
weather_data = response.json()
weather_12hrs = weather_data['hourly'][:12]

going_to_rain = False
for hour in weather_12hrs:
    condition_code = hour['weather'][0]['id']
    if condition_code < 700:
        going_to_rain = True

if going_to_rain:
    subject = 'Bring an umbrella!'
else:
    subject = 'It\'s your lucky day...'


with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=arguments['email'], password=arguments['password'])
    connection.sendmail(
            from_addr=arguments['email'], 
            to_addrs=arguments['email'], 
            msg='Subject:{}'.format(subject)
    )
