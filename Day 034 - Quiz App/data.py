'''This module calls to the API and gets a list of 10 random true or false questions from the Trivia
open database.'''
import requests

# State the parameters needed for the API call
parameters = {
    "amount": 10,
    "type": "boolean",
}

# Make API request
questions = requests.get(url="https://opentdb.com/api.php", params=parameters)
# Raise any bad response
questions.raise_for_status()
# Put data into list of questions and answers
question_data = questions.json()["results"]

