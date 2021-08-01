###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 33 exercise - Christopher Hagan
#
###################################

from os import EX_TEMPFAIL
import requests
import smtplib
import argparse
import getpass
from datetime import datetime

MY_LAT = 54.585630
MY_LONG = -5.988890
EMAIL = 'c.hagan1985@icloud.com'

def getArguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-u", "--user", required=False,
                    help="Email address")
    ap.add_argument("-p", "--password", required=False,
                    help="Password for user")
    ap.add_argument("-t", "--latitude", required=False,
                    help="Your Latitude")
    ap.add_argument("-g", "--longititude", required=False,
                    help="Your Longititude")
    args = vars(ap.parse_args())
    return args


def iss_nearby(my_latitude, my_longititude):
    """If ISS station is within +5 and -5 degrees of current location"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    """Returns True if current position tuple within +5 or -5 degress of target tuple"""
    if (my_latitude - 5 < iss_latitude < my_latitude + 5) and \
        (my_longititude -5 < iss_longitude < my_longititude + 5):
        return True
    else:
        print('ISS location: {}, {}'.format(iss_latitude, iss_longitude))
        return False


def is_night(my_latitude, my_longititude):
    parameters = {
        "lat": my_latitude,
        "lng": my_longititude,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now < sunrise or time_now > sunset:
        return True
    else:
        print('Sunrise: {}\nSunset: {}'.format(sunset, sunrise))
        return False


arguments = getArguments()

if arguments['user'] is None:
    arguments['user'] = input('Enter your Email: ')

if arguments['password'] is None:
    arguments['password'] = getpass.getpass('Enter your Password: ')

if arguments['latitude'] is None:
    arguments['latitude'] = MY_LAT

if arguments['longititude'] is None:
    arguments['longititude'] = MY_LONG


if iss_nearby(arguments['latitude'], arguments['longititude']) and \
    (is_night(arguments['latitude'], arguments['longititude'])):
    
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=arguments['user'], password=arguments['password'])
        connection.sendmail(
            from_addr=arguments['user'], 
            to_addrs=EMAIL, 
            msg='Subject:Look up!\n\n{}'.format(email_body)
        )
