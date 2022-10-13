'''Day 038 - This project is a workout tracking app which essentially can take a workout type and duration,
and then add it to a Google Sheet. There was no real guidance with this project so I had to essentially
build it from scratch by just reading through the API documentation. It taught me a lot about reading
through API documentation'''
import requests
from datetime import datetime as dt
from env_var import NUTRITION_APP_ID, NUTRITION_API_KEY, SHEETY_BEARER_AUTH, USER, SHEETPOINT, SHEET_CODE

# Let's store the request into a function
def exercise_stats(**kwargs):
    '''This function will take a number of params related to an exercise and then print
    out some stats related to that exercise. Suitable kwargs are gender, weight_kg, height_cm
    and age - see API documentation for more detail https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise'''
    # First lets store the params
    exercise_params = {
        "query": input("Tell me how you exercised and for how long : ")
    }
    # Then lets store the API endpoint
    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    # Next lets store any additional kwargs, checking for their type and that they make logical sense i.e. 
    # no negative weight or gender alien etc
    if kwargs["gender"] and kwargs["gender"] == ("male" or "female"):
        exercise_params["gender"] = kwargs["gender"]
    if kwargs["weight_kg"] and type(kwargs["weight_kg"]) == ("float" or "int") and kwargs["weight_kg"] > 0:
        exercise_params["weight_kg"] = kwargs["weight_kg"]
    if kwargs["height_cm"] and type(kwargs["height_cm"]) == ("float" or "int") and kwargs["height_cm"] > 0:
        exercise_params["height_cm"] = kwargs["height_cm"]
    if kwargs["age"] and type(kwargs["age"]) == "int" and kwargs["age"] > 0:
        exercise_params["age"] = kwargs["age"]
    # Now let's store the headers
    exercise_headers = {
        "x-app-id": NUTRITION_APP_ID,
        "x-app-key": NUTRITION_API_KEY,
    }
    # Then lets try calling the API
    exercise_response = requests.post(exercise_endpoint, json=exercise_params, headers=exercise_headers)
    # Raise any errors
    exercise_response.raise_for_status()
    # Convert the response to JSON format
    exercise_data = exercise_response.json()
    # return data in a format that can be sent to sheety
    return format_data(exercise_data)

def format_data(data: dict) -> list:
    '''This function will take the data returned from the exercise_stats function and format it so that it
    can be sent to the sheety API'''
    # First lets initialise a list to store dictionaries with data on each exercise
    formatted_data = []
    # Then lets loop through the data and store it in a dictionary
    for exercise_datum in data["exercises"]:
        # Append a dictionary with the relevant data to the list
        formatted_data.append({
            "workout": {
                "date": dt.now().strftime("%d/%m/%Y"),
                "time": dt.now().strftime("%X"),
                "exercise": exercise_datum["name"].title(),
                "duration": exercise_datum["duration_min"],
                "calories": exercise_datum["nf_calories"]
            }
        })
    # Return the list of dictionaries
    return formatted_data

def send_to_sheety(exercise_data: list):
    '''This function will make a post request to the sheety API with the data returned from the exercise_stats function'''
    # First lets store the API endpoint
    sheety_endpoint = f"https://api.sheety.co/{SHEET_CODE}/{USER}/{SHEETPOINT}"
    # Then lets store the headers
    sheety_headers = {
        "Authorization": SHEETY_BEARER_AUTH,
    }
    # Then lets post each item in the list of data
    for exercise_datum in exercise_data:
        sheety_params = {
            "workout": exercise_datum["workout"]
        }
        # Then we call the api with a post request for the datum
        sheety_response = requests.post(sheety_endpoint, json=sheety_params, headers=sheety_headers)
        # Raise any errors
        sheety_response.raise_for_status()
        # Print the response
        print(sheety_response.text)

send_to_sheety(exercise_stats(gender="male", age="25", height_cm="170", weight_kg="79.2"))


