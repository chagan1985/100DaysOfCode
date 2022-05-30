from ctypes import py_object
from urllib import response
import requests

GOOGLE_PRICES_SHEET = 'https://api.sheety.co/5710e198fa764d93a9b36437674c6aa2/flightDeals/prices/'
GOOGLE_USERS_SHEET = 'https://api.sheety.co/5710e198fa764d93a9b36437674c6aa2/flightDeals/users/'
HEADER = {'Authorization': 'Bearer SECRETTOKEN'}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__():
        pass

    def get_city_information():
        get_response = requests.get(url=GOOGLE_PRICES_SHEET, headers=HEADER)
        assert get_response.status_code == 200

        return get_response.json()

    def set_iata_code(data_row, iata_code):
        put_url = GOOGLE_PRICES_SHEET + '/{object_id}'.format(object_id=data_row)
        data = {'price': {'iataCode': iata_code}}

        put_response = requests.put(url=put_url, headers=HEADER, json=data)
        assert put_response.status_code == 200

    def get_user_emails():
        emails_list = []

        get_users = requests.get(url=GOOGLE_USERS_SHEET, headers=HEADER)
        assert get_users.status_code == 200

        for user in get_users.json()['users']:
            emails_list.append(user.get('email'))

        return emails_list


