###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 38 exercise - Christopher Hagan
#
###################################

import requests
import datetime

GENDER = 'male'
WEIGHT = '98'
HEIGHT = '178'
AGE = '37'

# Nutritionix information
APP_ID = 'b7b72f3c'
API_KEY = 'c5e7dd8b63b1f47d4e8f91cf052797d6'
exercises_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# Sheety information
SHEETY_API = 'https://api.sheety.co/5710e198fa764d93a9b36437674c6aa2/myWorkouts/workouts'
SHEETY_HEADER = {'Authorization': 'Bearer SECRETTOKEN'}


headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}

exercise_params = {
    'query': 'I walked 2km',
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}

sheety_params = {
    'workout': {
        'date': None,
        'time': None,
        'exercise': None,
        'duration': None,
        'calories': None
    }
}

nutritionix_response = requests.post(url=exercises_url, headers=headers, json=exercise_params)
print(nutritionix_response.json())
exercises_json = nutritionix_response.json()

sheety_params['workout']['exercise'] = exercises_json['exercises'][0]['user_input'].title()
sheety_params['workout']['duration'] = exercises_json['exercises'][0]['duration_min']
sheety_params['workout']['calories'] = exercises_json['exercises'][0]['nf_calories']
datetime_now = datetime.datetime.now()
sheety_params['workout']['date'] = datetime_now.strftime('%d/%m/%Y')
sheety_params['workout']['time'] = datetime_now.strftime('%X')

print(sheety_params)
sheety_response = requests.post(url=SHEETY_API, headers=SHEETY_HEADER,params=sheety_params)
print(sheety_response.json())
