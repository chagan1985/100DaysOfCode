###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 39 exercise - Christopher Hagan
#
###################################

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

def main():
    flights_below_min = []
    # Get location data from google sheet
    places_to_search = DataManager.get_city_information().get('prices')

    # Query IATA code for each destination where it is not currently populated
    for place in places_to_search:
        print(place)
        if place.get('iataCode') == '':
            iata_code = FlightSearch.get_iata_code(city=place['city'])
            place['iataCode'] = iata_code

            DataManager.set_iata_code(data_row=place['id'], iata_code=place['iataCode'])

    # Get price information for flights
    for place in places_to_search:
        cheapest_flight = FlightSearch.get_cheapest_flight(place['iataCode'])
        print(cheapest_flight.get('price'))
        if cheapest_flight.get('price') < place['lowestPrice']:
            flights_below_min.append(cheapest_flight)

    for flight in flights_below_min:
        depart_datetime = datetime.strptime(flight['local_arrival'], DATETIME_FORMAT)
        return_datetime = datetime.strptime(flight['route'][-1]['local_departure'], DATETIME_FORMAT)
        message = 'Low price alert! Only £{cost} to fly from {city_from} to {city_to}, on {depart_date} to {return_date}'.format(
            cost = flight['price'],
            city_from = '{}-{}'.format(flight['cityFrom'], flight['cityCodeFrom']),
            city_to = '{}-{}'.format(flight['cityTo'], flight['cityCodeTo']),
            depart_date = depart_datetime.date(),
            return_date = return_datetime.date(),
        )
        NotificationManager.send_text_message(mobile_number='feck off', text_message=message)


if __name__ == "__main__":
    main()
