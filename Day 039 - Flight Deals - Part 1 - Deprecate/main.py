'''Day 039 - The purpose of this project is to learn more about APIs and fuse it with my understanding of
sending messages using python. It's a capstone project so I was only given a brief and I had to come up
with the full code solution on my own. The program is a flight deals app that will send a text message to
a phone number if there is a flight deal from my city to another city for under a certain price.'''

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

# Set up all the instances of classes
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Lets make a function for getting and posting IATA codes so we don't have to keep doing it
def post_iata_codes():
    '''This function posts the IATA codes if needed'''    
    # Get the IATA codes for the cities in the sheet
    city_names = data_manager.get_city_data()
    # Now get the IATA codes for the cities
    iata_codes = []
    for city in city_names:
        iata_codes.append(flight_search.get_destination_code(city))
    print(iata_codes)
    # Now add the IATA codes to the sheet
    data_manager.update_iata_codes(iata_codes)

def return_flights_for_cheap_flight(departure_iata_code: str, destination_iata_code: str, price: int):
    '''This function checks if there is a flight for under the price'''
    # Get the flight data
    flight_data = flight_search.search_data(departure_iata_code, destination_iata_code)
    # Then choose the cheapest flight
    cheapest_flight = flight_data.find_cheapest_flight(flight_data)
    # Format the data
    formatted_cheapest_flight = flight_data.format_flight_data(cheapest_flight)
    # Check if the price is under the price
    if cheapest_flight["price"] < price:
        # Return the flight
        return formatted_cheapest_flight
    else:
        # Return None
        return None


def main():
    '''This is the main function that runs the program'''
    # First lets get all the data for the destinations
    destination_data = data_manager.get_destination_data()
    # Then lets store the IATA codes for the cities and the prices as a list of touples
    destination_data = [(entry["iataCode"], entry["lowestPrice"]) for entry in destination_data]
    # Next let's loop through the destinations and check if there is a flight for under the price
    # and if there is then send a text message
    
        

    