from datetime import datetime as dt

class FlightData:
    '''This class is responsible for structuring the flight data.'''
    
    def __init__(self, boundary_price: int):
        '''This function will initialise the class and store the boundary price'''
        # Store the boundary price
        self.boundary_price = boundary_price

    def find_cheapest_flight(self, data: dict) -> dict:
        '''This function will find the cheapest flight from the given data'''
        # First set up curr placeholder for cheapest flight
        curr_flight = None
        curr_cheapest_price = 10000
        # Loop through all the flights data and find the cheapest flight
        for flight in data["data"]:
            # Store the price
            price = flight["price"]
            # If the price is less than the current cheapest price, and the price is less than the boundary price then store it as current
            if price < curr_cheapest_price and price < self.boundary_price:
                curr_cheapest_price = price
                curr_flight = flight
        # Return the cheapest flight
        return curr_flight

    def format_flight_data(self, flight: dict) -> str:
        '''This function will format the flight data into a string ready to be sent to the user'''
        # First lets get the flight data into a manageable dictionary with the parts we want
        flight_data = {
            "departure_city": flight["cityFrom"],
            "departure_city_code": flight["cityCodeFrom"],
            "arrival_city": flight["cityTo"],
            "arrival_city_code": flight["cityCodeTo"],
            "departure_airport": flight["flyFrom"],
            "arrival_airport": flight["flyTo"],
            "price": flight["price"],
            "bags_price": flight["bags_price"],
            "availability": flight["availability"]["seats"],
            "outbound_date": flight["local_departure"][0:10], # I need to change this because it should be working out
            "arrival_date": flight["local_arrival"][0:10], # the departure and arrival time of each flight
            "outbound_time": flight["local_departure"][11:16], # and also then working out the duration of both flights
            "arrival_time": flight["local_arrival"][11:16], # All the data I'm currently getting is for a single flight
            "outbound_utc-date": flight["utc_departure"][0:10], # and not the whole journey so I need to work out how to
            "arrival_utc-date": flight["utc_arrival"][0:10], # get the data for the whole journey
            "outbound_utc_time": flight["utc_departure"][11:16],
            "arrival_utc_time": flight["utc_arrival"][11:16],
            "link": flight["deep_link"]
        }
        # Next let's work out the duration using the outbound utc date and time and the return utc time
        # First let's convert the outbound and return utc date and times to datetime objects
        outbound_utc_datetime = dt.strptime(flight_data["outbound_utc-date"] + " " + flight_data["outbound_utc_time"], "%Y-%m-%d %H:%M")
        arrival_utc_datetime = dt.strptime(flight_data["return_utc-date"] + " " + flight_data["return_utc_time"], "%Y-%m-%d %H:%M")
        # Now let's work out the duration
        duration = arrival_utc_datetime - outbound_utc_datetime
        # Now let's convert the duration to hours and minutes
        hours = duration.seconds // 3600
        minutes = (duration.seconds // 60) % 60
        # Now let's add the duration to the flight data
        flight_data["duration"] = f"{hours}h {minutes}m"
        return flight_data
        
    def check_total_price(self, outbound_flight: dict, return_flight: dict, max_price: int) -> bool:
        '''This function will check the total price of the flights and return True if the total price is less than the max price'''
        # First let's get the total price
        total_price = outbound_flight["price"] + return_flight["price"]
        # Now let's check if the total price is less than the max price
        if total_price < max_price:
            return True
        else:
            return False
        
    def format_to_message(self, outbound_flight: dict, return_flight: dict) -> str:  
        # Now let's format the flight data into a string
        flight_data_string = f'''
        Low price alert! only £{outbound_flight["price"] + return_flight["price"]} to fly from:
        {outbound_flight["departure_city"]}, ({outbound_flight["departure_city_code"]} {outbound_flight["departure_airport"]}) to
        {outbound_flight["arrival_city"]}, ({outbound_flight["arrival_city_code"]} {outbound_flight["arrival_airport"]})

        Depart: {outbound_flight["outbound_date"]} {outbound_flight["outbound_time"]}
        Return: {return_flight["outbound_date"]} {return_flight["outbound_date"]}

        Return Airport: {return_flight["departure_city"]} ({return_flight["departure_city_code"]} {return_flight["departure_airport"]})

        The price for extra bags on your outbound flight is £{outbound_flight["bags_price"]}
        The price for extra bags on your return flight is £{return_flight["bags_price"]}

        There are {outbound_flight["availability"]} seats available on the outbound flight
        There are {return_flight["availability"]} seats available on the return flight

        Link to outbound flight: {outbound_flight["link"]}

        Link to return flight: {return_flight["link"]}
        '''

        return flight_data_string
        
