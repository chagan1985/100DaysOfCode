###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 33 exercise - Christopher Hagan
#
###################################

import requests
from datetime import datetime as dt

URL = 'https://api.sunrise-sunset.org/json'
LAT = 54.585630
LONG = -5.988890

parameters = {
    'lat': LAT,
    'lng': LONG,
    'formatted': 0,
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

sunrise = response.json()['results']['sunrise'].split('T')[1].split(':')[0]
sunset = response.json()['results']['sunset'].split('T')[1].split(':')[0]

print('Sunrise today: {}\nSunset today: {}'.format(sunrise, sunset))

now = dt.now()
print('Now: {}'.format(now.hour))
