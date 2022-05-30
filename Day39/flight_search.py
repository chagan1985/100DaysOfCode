from urllib import response
import requests
import datetime
import pprint
from dateutil.relativedelta import relativedelta
from flight_data import FlightData

HEADER = {'apikey': 'J0liwnPpAGA5C5sHPJflgEe1Ll97O4Bi'}
GET_LOCATION_URL = 'https://tequila-api.kiwi.com/locations/query'
SEARCH_LOCATION_URL = 'https://tequila-api.kiwi.com/v2/search'
FLY_FROM = 'DUB'
SEARCH_DURATION_MONTHS = 6

# Figure it's easier to create a datetime object in case I need to edit in the future
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__():
        pass

    def get_iata_code(city):
        get_params = {
            'term': city,
            'location_types': 'airport',
            'limit': 1
        }

        get_response =  requests.get(url=GET_LOCATION_URL, headers=HEADER, params=get_params)
        iata_code = get_response.json()['locations'][0]['city']['code']

        return iata_code

    def get_cheapest_flight(iata_code, stop_overs=0):
        # Return is cheapest ASC therefore first entry is the cheapest
        today = datetime.datetime.today().date()
        get_params = {
            'fly_from': FLY_FROM,
            'fly_to': iata_code,
            'date_from': today + datetime.timedelta(days=1),
            'date_to': today + relativedelta(months=SEARCH_DURATION_MONTHS),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'stop_overs': stop_overs,
            'curr': 'GBP',
            'asc': 1
        }

        get_response = requests.get(url=SEARCH_LOCATION_URL, headers=HEADER, params=get_params)
        print(get_response.status_code)
        first_item = get_response.json().get('data')[0]
        print(first_item)
        #print(get_response.json())
        if get_response.status_code == 200 and stop_overs == 0:
            print(get_response.json())
            flight_data = FlightData(
                price = first_item['price'],
                depart_airport=first_item['cityCodeFrom'],
                depart_city= first_item['cityFrom'],
                dest_airport= first_item['cityCodeTo'],
                dest_city= first_item['cityTo'],
                depart_date = datetime.strptime(first_item['local_arrival'], DATETIME_FORMAT).date(),
                return_date = datetime.strptime(first_item['route'][-1]['local_departure'], DATETIME_FORMAT).date(),
            )
        elif get_response.status_code == 200 and stop_overs != 0:
            flight_data = FlightData(
                price = first_item['price'],
                depart_airport=first_item['cityCodeFrom'],
                depart_city= first_item['cityFrom'],
                dest_airport= first_item['cityCodeTo'],
                dest_city= first_item['cityTo'],
                depart_date = datetime.strptime(first_item['local_arrival'], DATETIME_FORMAT).date(),
                stop_overs=stop_overs,
                via_city=first_item["route"][0]["cityTo"]
            )
        else:
            flight_data = {}
          

        return flight_data

