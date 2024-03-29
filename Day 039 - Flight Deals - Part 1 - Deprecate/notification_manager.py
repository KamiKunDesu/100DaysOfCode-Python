
from twilio.rest import Client

from env_var import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER_RECEIVE, PHONE_NUMBER_SEND

class NotificationManager:
    def __init__(self) -> None:
        self.client: Client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message: str) -> None:
        try:
            message = self.client.messages \
                .create(
                    body=message,
                    from_=PHONE_NUMBER_SEND,
                    to=PHONE_NUMBER_RECEIVE
                )

        except Exception as e:
            print(e)

    

