from . import Notifier
from twilio.rest import Client


class TwilioNotifier(Notifier):
    """Notifier to send SMS notification to phone number via Twilio"""
    def __init__(self, message, account_sid, account_token, to_number, from_number):
        """
        Constructor
        :param message: The default message to use in the notification.
        :param account_sid: The Twilio account SID.
        :param account_token: The Twilio account token.
        :param to_number: The default number to send the notification to.
        :param from_number: The Twilio verified number from which the notification will be received.
        """
        super().__init__(message)
        self.message = message
        self.to_number = to_number
        self.from_number = from_number
        self.client = Client(account_sid, account_token)

    def notify(self, message=None, to_number=None):
        """
        Send the notification.
        :param message: The optional message to use for the notification. Default is the message from the constructor.
        :param to_number: The optional number to send to. Default is the number from the constructor.
        :return: None
        """
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
