from notifiers.gmail import GmailNotifier


class Herald:
    def __init__(self, notifier=GmailNotifier, message="Hear ye, hear ye!"):
        self.notifier = notifier
        self.message = message

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.notifier.notify(self.message)
        return False


notifier = GmailNotifier()

with Herald(notifier, message="Yay the process is now complete!") as herald:
    print("Loooong running process")
