from env_var import SHEETPOINT, SHEET_CODE, SHEETY_BEARER_AUTH, USER
import requests

class DataManager:
    '''This class is responsible for talking to the Google Sheet.'''
    
    def __init__(self):
        '''This function will initialise the class and store the API endpoint and headers'''
        # Store the API endpoint
        self.sheetpoint = SHEETPOINT
        # Store the headers
        self.headers = {
            "Authorization": f"Bearer {SHEETY_BEARER_AUTH}"
        }
        # Store the sheet code
        self.sheet_code = SHEET_CODE
        # Store the user
        self.user = USER
        # Store the API endpoint
        self.endpoint = f"https://api.sheety.co/{self.sheet_code}/{self.user}/{self.sheetpoint}"

    def get_city_data(self) -> list:
        '''This function will make a get request to the sheety API and return the data for the city names'''
        # Make the get request
        response = requests.get(self.endpoint, headers=self.headers)
        # Raise any errors
        response.raise_for_status()
        # Initialise a list to store the city names
        city_names = []
        # Loop through the data and store the city names
        for entry in response.json()["prices"]:
            city_names.append(entry["city"])
        # Return the list of city names
        return city_names
    
    def update_iata_codes(self, data: list):
        '''This function will make a put request to the sheety API to update the IATA codes'''
        # Loop through the data
        for index, entry in enumerate(data):
            # Store the params
            params = {
                "price": {
                    "iataCode": entry
                }
            }
            # Make the put request
            response = requests.put(f"{self.endpoint}/{index+2}", json=params, headers=self.headers)
            # Raise any errors
            response.raise_for_status()
            # Print the response
            print(response.text)

    def get_destination_data(self) -> list:
        '''This function will make a get request to the sheety API and return the data for each row as
        a dictionary'''
        # Make the get request
        response = requests.get(self.endpoint, headers=self.headers)
        # Raise any errors
        response.raise_for_status()
        # Initialise a list to store the city names
        destination_data = []
        # Loop through the data and store the city names
        for entry in response.json()["prices"]:
            destination_data.append(entry)
        # Return the list of city names
        print(destination_data)
        return destination_data
        
    def add_destination_data(self, data: dict):
        '''This function will make a post request to the sheety API to add a new destination'''
        # Lets make sure it has everything it needs
        if data["city"] and data["lowestPrice"]:
            # Make the post request
            response = requests.post(self.endpoint, json=data, headers=self.headers)
            # Raise any errors
            response.raise_for_status()
            # Print the response
            print(response.text)

