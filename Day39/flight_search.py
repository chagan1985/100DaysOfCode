from urllib import response
import requests
import datetime
from dateutil.relativedelta import relativedelta

HEADER = {'apikey': 'J0liwnPpAGA5C5sHPJflgEe1Ll97O4Bi'}
GET_LOCATION_URL = 'https://tequila-api.kiwi.com/locations/query'
SEARCH_LOCATION_URL = 'https://tequila-api.kiwi.com/v2/search'
FLY_FROM = 'DUB'
SEARCH_DURATION_MONTHS = 6


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

    def get_cheapest_flight(iata_code):
        # Return is cheapest ASC therefore first entry is the cheapest
        today = datetime.date.today()
        get_params = {
            'fly_from': FLY_FROM,
            'fly_to': iata_code,
            'date_from': today + datetime.timedelta(days=1),
            'date_to': today + relativedelta(months=SEARCH_DURATION_MONTHS),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'curr': 'GBP',
            'asc': 1
        }

        get_response = requests.get(url=SEARCH_LOCATION_URL, headers=HEADER, params=get_params)
        assert get_response.status_code == 200

        print(get_response.json().get('data')[0])

        return get_response.json().get('data')[0]

