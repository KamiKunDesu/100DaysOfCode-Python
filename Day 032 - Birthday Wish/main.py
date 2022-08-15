import smtplib
from env_var import MY_PASSWORD, MY_EMAIL

# Write my email and password
my_email = MY_EMAIL
password = MY_PASSWORD

# Create an smtp connection with the gmail provider
connection = smtplib.SMTP("smtp.gmail.com")
# Secures the connection with transfer level security
connection.starttls()
# Log on to the system
connection.login(user=my_email, password=password)
# Finally                                 