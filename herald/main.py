import herald.notifiers as notifiers


class Herald:
    def __init__(self, notifier):
        self.notifier = notifier

    def __enter__(self):
        print("Oooh entered a context manager")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.notifier.notify()
        return False


notifier = notifiers.GmailNotifier("I will now send a mail via GMAIL")

with Herald(notifier) as herald:
    print("Loooong running process")
