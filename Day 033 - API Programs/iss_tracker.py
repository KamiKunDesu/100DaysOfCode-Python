'''Day 033- The purpose of this project is to learn about using APIs and how to make API requests and work
with them in Python. This project is an ISS tracker which will track the ISS and if it's above head and also
nighttime it will send an email to a designated email address'''

import requests
from datetime import datetime
import smtplib
from env_var import MY_PASSWORD, MY_EMAIL, TARGET_MAIL

# Response tutorial
# 1XX = Hold On
# 2XX = Here You Go
# 3XX = Go Away
# 4XX = You Screwed Up
# 5XX = I Screwed Up

# Make a get request to the endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# This will raise an error for non 2XX requests
response.raise_for_status()

# Get the JSON into a python dictionary
data = response.json()

# Can work with JSON in exactly the same way as we work with python dictionaries
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# Put that data into a tuple
iss_position = (float(latitude), float(longitude))

# Get the sunset and sunrise 
# First create the params to give to the API, latitude, longitude and also make it formatted to 24 hour clock
parameters = {
    "lat": 51.454514,
    "lng": -2.587910,
    "formatted": 0,
}

# Get the API sunset and sunrise times
suntime_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# Raise any bad response
suntime_response.raise_for_status()
# Store data for sunrise and sunset into variables
sun_data = suntime_response.json()
# This chain stores a list of integers [Hours, Minutes] for both sunrise time and sunset time
sunrise_time = [int(x) for x in sun_data["results"]["sunrise"].split("T")[1].split(":") if len(x) == 2][0:2]
sunset_time = [int(x) for x in sun_data["results"]["sunset"].split("T")[1].split(":") if len(x) == 2 ][0:2]

# Get the current time
time_now = datetime.now()

# Get all email credentials stored
my_email = MY_EMAIL
password = MY_PASSWORD
target = TARGET_MAIL

# Let's make a helper function for lat, long closeness
def is_in_range(lat, lng, parameters):
    '''This helper function returns True if own lat and lng is within +- 5 of given lat and lng'''
    
    # Set up ranges and return bool
    lat_upper = parameters["lat"]+5
    lat_lower = parameters["lat"]-5
    lng_upper = parameters["lng"]+5
    lng_lower = parameters["lng"]-5

    return ((lat in range(lat_lower, lat_upper)) and (lng in range(lng_lower, lng_upper)))

# Quick helper function to make sure that it's night sky not sunny
def is_night_sky(time_now, sunrise_time, sunset_time):
    '''This function checks if the current time is before sunrise or after sunset'''
    if time_now.hour > sunset_time[0] and time_now.minute > sunset_time[1]:
        return True
    elif time_now.hour < sunrise_time[0] and time_now.minute < sunrise_time[1]:
        return True
    else:
        return False

# Check if it's night sky and ISS is in range
if is_night_sky(time_now, sunrise_time, sunset_time) and is_in_range(iss_position[0], iss_position[1], parameters=parameters):
    # Open the SMTP context (so that we don't have to manually close with connection.close() at the end)
    with smtplib.SMTP("smtp.gmail.com") as connection: 
        # Secures the connection with transfer level security
        connection.starttls()
        # Log on to the system
        connection.login(user=my_email, password=password)
        # Finally send mail to make sure we look up
        connection.sendmail(
            from_addr=my_email,
            to_addrs=target,
            msg = f"Subject: ISS Notification\n\nLook up! The ISS is overhead!"
        )
