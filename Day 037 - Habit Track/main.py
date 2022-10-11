'''Day 037 - This project interacts via a number of functions that I built with the pixela API. It is simple
to use and helps you to track habits in the form of pixels. The project itself taught me a lot about using
post, put, and delete requests with the requests library. I also refreshed my knowledge of working with a
number of other libraries such as datetime, json and regex.'''
from env_var import PIXELA_API_KEY, USER
import requests
import re
import json
from datetime import datetime

# First store the pixela endpoint as a string
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
# Store todays date using date time in format YYYYMMDD for ease later
TODAY = datetime.now().strftime("%Y%m%d")

def create_user(api_key: str, username: str):
    '''This function creates a new user by taking in the necessary parameters and using them to call the API creation endpoint'''
    # First store the parameters
    user_creation_params = {
        "token": api_key,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    # Finally need to make a post request to the endpoint
    response = requests.post(url=PIXELA_ENDPOINT, json=user_creation_params)
    # On good response, update the user data file
    if response.status_code == 200:
        update_user_data("user", user=username)
    # Print the response for the request
    print(response.text)


def create_graph(user: str, api_key: str, id: str, name: str, unit: str, type: str, color: str):
    '''This function creates a new graph for the user by taking in the necessary parameters and using them to call the API graph creation endpoint'''
    # Store a new endpoint for creating a graph
    GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{user}/graphs"
    # Store the params for the graph
    graph_params = {
        "id": id,
        "name": name,
        "unit": unit,
        "type": type,
        "color": color,
    }
    # Create a headers dict for the request
    headers = {
        "X-USER-TOKEN": api_key
    }   
    # Make a post request to the graph endpoint using the headers
    response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
    # On good response, update the user data file
    if response.status_code == 200:
        update_user_data("graph", user=user, graph_id=id, graph_name=name)
    # Print the response for the request
    print(response.text)

def create_pixel(user: str, api_key: str, graph_id: str, date: str, quantity: str, **kwargs):
    '''This function creates a new pixel for the user by taking in the necessary parameters and using them to call the API pixel creation endpoint.
    Pass the kwarg "optional_data: str to add any optional data for the pixel. Amount of data in this string must be less than 10kb.'''
    # First lets check that the date is in the right format (yyyyMMdd) with some regex
    if re.fullmatch(r"\d{8}", date):
        # Store a new endpoint for creating a pixel
        PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{user}/graphs/{graph_id}"
        # Store the params for the pixel
        pixel_params = {
            "date": date,
            "quantity": quantity,
        }
        # Add any optional parameters if they exist to the pixel params
        if kwargs["optional_data"] and type(kwargs["optional_data"]) == str:
            pixel_params["optional_data"] = kwargs["optional_data"]
        # Create a headers dict for the request
        headers = {
            "X-USER-TOKEN": api_key
        }
        # Make a post request to the pixel endpoint using the headers
        response = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
        # Print the response for the request
        print(response.text)
    else:
        raise ValueError("The date must be in the format yyyyMMdd")

def update_pixel(id: str, user: str, api_key: str, date: str, quantity: str, **kwargs):
    '''This function updates a pixel for the user by taking in the necessary parameters and using them to call the API pixel update endpoint.
    Pass the kwarg "optional_data: str to add any optional data for the pixel. Amount of data in this string must be less than 10kb.'''
    # First lets check that the date is in the right format (yyyyMMdd) with some regex
    if re.fullmatch(r"\d{8}", date):
        # Store a new endpoint for updating a pixel
        PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{user}/graphs/{id}/{date}"
        # Store the params for the pixel
        pixel_params = {
            "quantity": quantity,
        }
        # Add any optional parameters if they exist to the pixel params
        if kwargs["optional_data"] and type(kwargs["optional_data"]) == str:
            pixel_params["optional_data"] = kwargs["optional_data"]
        # Create a headers dict for the request
        headers = {
            "X-USER-TOKEN": api_key
        }
        # Make a put request to the pixel endpoint using the headers
        response = requests.put(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
        # Print the response for the request
        print(response.text)
    else:
        raise ValueError("The date must be in the format yyyyMMdd")

def delete_pixel(id: str, user: str, api_key: str, date: str):
    '''This function deletes a pixel for the user by taking in the necessary parameters and using them to call the API pixel deletion endpoint.'''
    # First lets check that the date is in the right format (yyyyMMdd) with some regex
    if re.fullmatch(r"\d{8}", date):
        # Store a new endpoint for deleting a pixel
        PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{user}/graphs/{id}/{date}"
        # Create a headers dict for the request
        headers = {
            "X-USER-TOKEN": api_key
        }
        # Make a delete request to the pixel endpoint using the headers
        response = requests.delete(url=PIXEL_ENDPOINT, headers=headers)
        # Print the response for the request
        print(response.text)
    else:
        raise ValueError("The date must be in the format yyyyMMdd")

def update_graph(user: str, api_key: str, id: str, **kwargs):
    '''This function updates a graph for the user by taking in the necessary parameters and using them to call the API graph update endpoint.
    The optional arguments are name, unit, color, timezone, selfSufficient, isSecret and publishOptionalData. More detail
    about each option can be found at https://docs.pixe.la/entry/put-graph'''
    # Store a new endpoint for updating a graph
    GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{user}/graphs/{id}"
    # Store the params for the graph
    graph_params = {
    }
    # Add all the optional params
    if kwargs["name"] and type(kwargs["name"]) == str:
        graph_params["name"] = kwargs["name"]
    if kwargs["unit"] and type(kwargs["unit"]) == str:
        graph_params["unit"] = kwargs["unit"]
    if kwargs["color"] and type(kwargs["color"]) == str:
        graph_params["color"] = kwargs["color"]
    if kwargs["timezone"] and type(kwargs["timezone"]) == str:
        graph_params["timezone"] = kwargs["timezone"]
    if kwargs["selfSufficient"] and type(kwargs["selfSufficient"]) == str:
        graph_params["selfSufficient"] = kwargs["selfSufficient"]
    if kwargs["isSecret"] and type(kwargs["isSecret"]) == bool:
        graph_params["isSecret"] = kwargs["isSecret"]
    if kwargs["publishOptionalData"] and type(kwargs["publishOptionalData"]) == bool:
        graph_params["publishOptionalData"] = kwargs["publishOptionalData"]

    # Create a headers dict for the request
    headers = {
        "X-USER-TOKEN": api_key
    }   
    # Make a put request to the graph endpoint using the headers
    response = requests.put(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
    # Print the response for the request
    print(response.text)

def delete_graph(user: str, api_key: str, id: str):
    '''This function deletes a graph for the user by taking in the necessary parameters and using them to call the API graph deletion endpoint.'''
    # Store a new endpoint for deleting a graph
    GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{user}/graphs/{id}"
    # Create a headers dict for the request
    headers = {
        "X-USER-TOKEN": api_key
    }
    # Make a delete request to the graph endpoint using the headers
    response = requests.delete(url=GRAPH_ENDPOINT, headers=headers)
    # Print the response for the request
    print(response.text)

def update_user_data(request: str, **kwargs):
    '''This function helps to keep track of existing users and their graphs by updating and maintaining a json file when code is called'''    
    # First open the file context in read mode to get the data
    with open("user_data.json", "r") as file:
        # Read in the existing JSON data
        user_data = json.load(file)
    # Now check the request type
    if request == "user":
        # Call the helper function to handle the user request
        handle_user_request(user_data, kwargs["user"])
    elif request == "graph":
        # Call the helper function to handle the graph request
        handle_graph_request(user_data, kwargs["user"], kwargs["graph_id"], kwargs["graph_name"])
    else:
        raise ValueError("The request type must be either 'user' or 'graph'")

    
def handle_user_request(data: dict, user: str):
    '''This is a small helper function which simply handles updating the json user data file for a user request'''
    # First check if the user already exists
    if user in data:
        # Do nothing and return
        return
    else:
        # Let's update the dict with the user
        data["users"][user] = []
        # Now let's write the data back to the file
        # Open the file context in write mode
        with open("user_data.json", "w") as file:
            # Write the data back to the file
            json.dump(data, file) 

def handle_graph_request(data: dict, user: str, graph_id: str, graph_name: str):
    '''This is a small helper function which simply handles updating the json user data file for a graph request'''
    # First check if the graph already exists
    if graph_id in data["users"][user]:
        # Do nothing and return
        return
    else:
        # Let's update the dict with the graph
        data["users"][user].append((graph_id, graph_name))
        # Now let's write the data back to the file
        # Open the file context in write mode
        with open("user_data.json", "w") as file:
            # Write the data back to the file
            json.dump(data, file)

# ---------------------------- Main Code ---------------------------- #

# This is just an example of calling a function to add a new pixel
create_pixel(user=USER, api_key=PIXELA_API_KEY, graph_id="graph1", date=TODAY, quantity="2", optional_data="I read 2 pages today")