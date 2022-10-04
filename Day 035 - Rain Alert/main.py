'''Day 035 - The purpose of this project is to learn more about APIs and fuse it with my understanding of
sending messages using python. Specifically, it is helping me learn the usage of API keys. The program is
a weather app that will send a text message to a phone number if it is going to rain in the next 12 hours
and also report on what the weather will be for the next 12 hours.'''
import requests
from env_var import API_KEY, ACCOUNT_SID, AUTH_TOKEN, PHONE_NUMBER_SEND, PHONE_NUMBER_RECEIVE
import os
from twilio.rest import Client
import datetime as dt

# Set up the API end point to call later
OWN_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
# Store the environment variables
api_key = API_KEY
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
phone_number_send = PHONE_NUMBER_SEND
phone_number_receive = PHONE_NUMBER_RECEIVE
# Set up the parameters for the API call
weather_params = {
    "lat": 51.4552,
    "lon": -2.5967,
    "appid": api_key,
    "exclude": "current,minutely,daily"
    }

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get(OWN_endpoint, params=weather_params)
response.raise_for_status()

# Get weather data into JSON format.
weather_data = response.json()

# Get the first 12 hours of weather data
weather_slice = weather_data["hourly"][:12]

# Make a will rain flag
will_rain = False
# Make a list to store weather condition codes for the next 12 hours
hourly_weather_codes = []
# Make a list to store touples of the weather descriptions for the next 12 hours
weather_descriptions = []
# Make a for loop to get the weather condition codes and descriptions for the next 12 hours
for hour_data in weather_slice:
    hourly_weather_codes.append(hour_data["weather"][0]["id"])
    weather_descriptions.append((hour_data["weather"][0]["main"], hour_data["weather"][0]["description"]))
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True

# Set up a twilio client
client = Client(account_sid, auth_token)

# Store time now
time_now = dt.datetime.now()
# Get current hour
current_hour = time_now.hour

# Set up string to send
message_string = f"""
{"You need to bring an umbrella today."*will_rain} 
Your weather forecast for the next twelve hours is:
{current_hour}-{current_hour+1}: {weather_descriptions[0][0]} - {weather_descriptions[0][1]}
{current_hour+1}-{current_hour+2}: {weather_descriptions[1][0]} - {weather_descriptions[1][1]}
{current_hour+2}-{current_hour+3}: {weather_descriptions[2][0]} - {weather_descriptions[2][1]}
{current_hour+3}-{current_hour+4}: {weather_descriptions[3][0]} - {weather_descriptions[3][1]}
{current_hour+4}-{current_hour+5}: {weather_descriptions[4][0]} - {weather_descriptions[4][1]}
{current_hour+5}-{current_hour+6}: {weather_descriptions[5][0]} - {weather_descriptions[5][1]}
{current_hour+6}-{current_hour+7}: {weather_descriptions[6][0]} - {weather_descriptions[6][1]}
{current_hour+7}-{current_hour+8}: {weather_descriptions[7][0]} - {weather_descriptions[7][1]}
{current_hour+8}-{current_hour+9}: {weather_descriptions[8][0]} - {weather_descriptions[8][1]}
{current_hour+9}-{current_hour+10}: {weather_descriptions[9][0]} - {weather_descriptions[9][1]}
{current_hour+10}-{current_hour+11}: {weather_descriptions[10][0]} - {weather_descriptions[10][1]}
{current_hour+11}-{current_hour+12}: {weather_descriptions[11][0]} - {weather_descriptions[11][1]}
"""

# Set up a message to send
message = client.messages \
                .create(
                        body=message_string,
                        from_=phone_number_send,
                        to=phone_number_receive
                    )

# Print the message SID
print(message.sid)