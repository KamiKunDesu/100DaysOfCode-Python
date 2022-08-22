'''This is an initial practice piece of code that sends randomised quotes everyday to someone's email
address - it was built to learn about sending email with python using SMTP'''

import smtplib
import datetime as dt
import random
from env_var import MY_PASSWORD, MY_EMAIL, TARGET_MAIL

# Write my email and password
my_email = MY_EMAIL
password = MY_PASSWORD
target = TARGET_MAIL

# Then we need to get a list of our quotes from the quotes file
with open("quotes.txt", "r") as quotes:
    quotes_list = quotes.readlines()


# Open the SMTP context (so that we don't have to manually close with connection.close() at the end)
with smtplib.SMTP("smtp.gmail.com") as connection: 
    # Secures the connection with transfer level security
    connection.starttls()
    # Log on to the system
    connection.login(user=my_email, password=password)
    # Now we're going to check if the current dates weekday is a Weekday, and if so we'll send a motivational quote
    if dt.datetime.now().weekday() in range (0,4):
        # First get random quote
        quote = random.choice(quotes_list)
        # Finally send a mail
        connection.sendmail(
        from_addr=my_email,
        to_addrs=target,
        msg = f"Subject: Today's Inspirational Quote\n\n{quote}"
    )
