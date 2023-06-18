from env_var import FLIGHT_TRACKER_KEY
import requests
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

class FlightSearch:
    '''This class is responsible for talking to the Flight Search API.'''

    def __init__(self):
        '''This function will initialise the class and store the API endpoint and headers'''
        # Store the API endpoint
        self.endpoint = "https://tequila-api.kiwi.com"
        # Store the headers
        self.headers = {
            "apikey": FLIGHT_TRACKER_KEY
        }
        self.other_search_kwargs = [
            "return_from",
            "return_to",
            "nights_in_dst_from",
            "nights_in_dst_to",
            "max_fly_duration",
            "one_for_city",
            "one_per_date",
            "one_per_date",
            "adults",
            "children",
            "infants",
            "selected_cabins",
            "mix_with_cabins",
            "adult_hold_bag",
            "adult_hand_bag",
            "child_hold_bag",
            "child_hand_bag",
            "fly_days",
            "fly_days_type",
            "ret_fly_days",
            "ret_fly_days_type",
            "only_working_days",
            "only_weekends",
            "partner_market",
            "curr",
            "locale",
            "price_from",
            "price_to",
            "dtime_from",
            "dtime_to",
            "atime_from",
            "atime_to",
            "ret_dtime_from",
            "ret_dtime_to",
            "ret_atime_from",
            "ret_atime_to",
            "stopover_to",
            "max_stopovers",
            "max_sector_stopovers",
            "conn_on_diff_airport",
            "ret_from_diff_airport",
            "ret_to_diff_airport",
            "selected_airlines",
            "selected_airlines_exclude",
            "select_stop_airport",
            "select_stop_airport_exclude",
            "vehicle_type",
            "sort",
            "asc",
            "limit",
        ]
        self.curr_date = dt.now().strftime("%d/%m/%Y")
        self.six_months_from_now = (dt.now() + relativedelta(months=+6)).strftime("%d/%m/%Y")
    
    def get_data_query(self, city_name: str):
        '''This function will query the search API based on the city name and return full data for
        it'''
        # Store the params
        params = {
            "term": city_name,
            "location_types": "city"
        }
        # Make the get request
        response = requests.get(f"{self.endpoint}/locations/query", params=params, headers=self.headers)
        # Raise any errors
        response.raise_for_status()
        # Store the IATA code
        flight_data = response.json()
        # Return the flight data
        return flight_data
    
    def get_destination_code(self, city_name: str) -> str:
        '''This function will make a get request to the flight search API and return the IATA code for the city name'''
        data = self.get_data_query(city_name)
        # Store the IATA code
        iata_code = data["locations"][0]["code"]
        # Return the IATA code
        return iata_code

    def return_destination_code_list(self, data: list) -> list:
        '''This function will make a get request to the flight search API and return the IATA code for a group of
        city names'''
        # Initialise a list to store the IATA codes
        iata_codes = []
        # Loop through the data
        for entry in data:
            # Store the IATA code
            iata_code = self.get_destination_code(entry)
            # Store the IATA code in the list
            iata_codes.append(iata_code)
        # Return the IATA codes
        return iata_codes

    def search_data(self, fly_from: str, fly_to: str, **kwargs) -> dict:
        '''This function will make a get request to the flight search API and return the flight data for the
        given parameters'''
        # First refresh the dates
        self.refresh_date()
        # Store the params
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": self.curr_date,
            "date_to": self.six_months_from_now,
            "curr": "GBP"
        }
        # Loop through the kwargs and add them to the params if they're an acceptable param
        for key, value in kwargs.items():
            if key in self.other_search_kwargs:
                params[key] = value
        # Make the get request
        response = requests.get(f"{self.endpoint}/v2/search", params=params, headers=self.headers)
        # Raise any errors
        response.raise_for_status()
        # Store the flight data
        flight_data = response.text
        # Return the flight data
        return flight_data

    def refresh_date(self):
        '''This function will refresh the current date and six months from now'''
        self.curr_date = dt.now().strftime("%d/%m/%Y")
        self.six_months_from_now = (dt.now() + relativedelta(months=+6)).strftime("%d/%m/%Y")
    

#flight_search = FlightSearch()
#flight_search.get_data_query("London")