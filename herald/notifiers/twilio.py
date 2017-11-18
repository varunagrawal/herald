from . import Notifier
from twilio.rest import Client

class TwilioNotifier(Notifier):
    def __init__(self, message, account_sid, account_token, to_number, from_number):
        super().__init__(message)
        self.message = message
        self.to_number = to_number
        self.from_number = from_number
        self.client = Client(account_sid, account_token)

    def notify(self, message=None, to_number=None):
        if not message:
            message = self.message

        if not to_number:
            to_number = self.to_number

        twilio_message = self.client.messages.create(
            to=to_number,
            from_=self.from_number,
            body=message
        )
        print("Sent message with SID: {0}".format(twilio_message.sid))
