from twilio.rest import Client
from env_var import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER_RECEIVE, PHONE_NUMBER_SEND

class NotificationManager:
    '''This class is responsible for sending notifications with the deal flight details.'''
    def __init__(self):
        '''Initialise the twilio client.'''
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        '''This sends a message to the user.'''
        message = self.client.messages \
            .create(
                body=message,
                from_=PHONE_NUMBER_SEND,
                to=PHONE_NUMBER_RECEIVE
            )

        print(message.status)
    

