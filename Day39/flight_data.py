class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self, price, depart_city, depart_airport, dest_city, dest_airport, depart_date, return_date, stop_overs=0, via_city=''):
        self.price = price
        self.depart_city = depart_city
        self.depart_airport = depart_airport
        self.dest_city = dest_city
        self.dest_airport = dest_airport
        self.depart_date = depart_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city


