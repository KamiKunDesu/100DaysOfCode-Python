'''Day 032- The purpose of this project is to bring together my knowledge about file reading and pandas, as well
as building new knowledge about handling SMTPs in python, in order to make a program which looks through a CSV
of birthdays and sends a happy birthday email to anyone whose Birthday is on the list'''

import smtplib
import datetime as dt
import random
import pandas as pd
from env_var import MY_PASSWORD, MY_EMAIL, TARGET_MAIL

# First let's get the CSV into a dataframe in pandas and establish current date
birthdays_df = pd.read_csv("birthdays.csv", index_col=False)
# Set up the current date
current_date = dt.datetime.now()
# instantiate a list to store daily messages
birthday_messages = []

# Loop through the data frame and check if it's anyone's birthday
for index, row in birthdays_df.iterrows():
    # If it's their birthday get a random letter template and fill it with their name
    if row["month"] == current_date.month and row["day"] == current_date.day:
        with open (random.choice(["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]), 'r') as birthday_message:
            # Pick the message
            plain_text = birthday_message.read()
            # Replace the name
            true_text = plain_text.replace("[NAME]", row["names"])
            # Add it onto the birthday message queue
            birthday_messages.append(true_text)


# Get environment variables set up
my_email = MY_EMAIL
password = MY_PASSWORD
target = TARGET_MAIL

# Open the SMTP context (so that we don't have to manually close with connection.close() at the end)
with smtplib.SMTP("smtp.gmail.com") as connection: 
    # Secures the connection with transfer level security
    connection.starttls()
    # Log on to the system
    connection.login(user=my_email, password=password)
    # Send formatted mail for list of birthday emails
    for birthday_message in birthday_messages:
        connection.sendmail(
            from_addr=my_email,
            to_addrs=target,
            msg = f"Subject: Happy Birthday\n\n{birthday_message}"
        )




