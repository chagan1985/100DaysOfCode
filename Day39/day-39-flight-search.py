###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 39 exercise - Christopher Hagan
#
###################################

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

def main():
    flights_below_min = []
    # Get location data from google sheet
    places_to_search = DataManager.get_city_information().get('prices')

    # Query IATA code for each destination where it is not currently populated
    for place in places_to_search:
        if place.get('iataCode') == '':
            iata_code = FlightSearch.get_iata_code(city=place['city'])
            place['iataCode'] = iata_code

            DataManager.set_iata_code(data_row=place['id'], iata_code=place['iataCode'])

    # Get price information for flights
    for place in places_to_search:
        cheapest_flight = FlightSearch.get_cheapest_flight(place['iataCode'])
        print(cheapest_flight)
        # If no flights found matching criteria search again with the inclusion of stop overs
        if cheapest_flight != {}:
            cheapest_flight = FlightSearch.get_cheapest_flight(place['iataCode'], stop_overs=1)
        else:
            flight_data = cheapest_flight

        print('printing... \n{}'.format(flight_data))

        if flight_data.get('price') < place['lowestPrice']:
            flights_below_min.append(flight_data)

    for flight in flights_below_min:
        message = 'Low price alert! Only £{cost} to fly from {city_from} to {city_to}, on {depart_date} to {return_date}'.format(
            cost = flight.get('price'),
            city_from = '{}-{}'.format(flight.get('depart_city'), flight.get('depart_airport')),
            city_to = '{}-{}'.format(flight.get('dest_city'), flight.get('dest_airport')),
            depart_date = flight.get('depart_date'),
            return_date = flight.get('return_date'),
        )
        if flight.get('stop_overs') > 0:
            message += '\n\nFlight had 1 stop over, via {via_city}'.format(
                via_city= flight.get('route')[0]['cityTo']
            )

        NotificationManager.send_text_message(mobile_number='feck off', text_message=message)
        NotificationManager.send_email(message_text=message)


if __name__ == "__main__":
    main()
