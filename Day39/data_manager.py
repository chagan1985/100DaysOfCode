from ctypes import py_object
from urllib import response
import requests

GOOGLE_SHEET = 'https://api.sheety.co/5710e198fa764d93a9b36437674c6aa2/flightDeals/prices/'
HEADER = {'Authorization': 'Bearer SECRETTOKEN'}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__():
        pass

    def get_city_information():
        get_response = requests.get(url=GOOGLE_SHEET, headers=HEADER)
        assert get_response.status_code == 200

        return get_response.json()

    def set_iata_code(data_row, iata_code):
        put_url = GOOGLE_SHEET + '/{object_id}'.format(object_id=data_row)
        data = {'price': {'iataCode': iata_code}}

        put_response = requests.put(url=put_url, headers=HEADER, json=data)
        assert put_response.status_code == 200



