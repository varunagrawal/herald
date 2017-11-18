from herald.herald import Herald
from herald import notifiers
import json


notifier = notifiers.TerminalNotifier(message="Test message")

def test_context_manager_custom_message():
    with Herald(notifier, message="Yay the process is now complete!"):
        print("Loooong running process")

def test_context_manager():
    with Herald(notifier):
        print("Another long running process")


def test_gmail_notifier():
    notifier = notifiers.GmailNotifier(message="This is a test message",
                                       client_secret_file='credentials/gmail_client_secret.json')
    notifier.notify()

def test_twilio_notifier():
    with open("credentials/twilio.json") as f:
        creds = json.load(f)
    notifier = notifiers.TwilioNotifier(message="Sample text message", account_sid=creds["account_sid"],
                                        account_token=creds["account_token"],
                                        to_number=creds["to"], from_number=creds["from"])
    notifier.notify()


if __name__ == "__main__":
    test_context_manager()
    test_context_manager_custom_message()
    test_gmail_notifier()
    test_twilio_notifier()
