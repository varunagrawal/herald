from .notifiers.gmail import GmailNotifier


class Herald:
    def __init__(self, notifier=GmailNotifier, message="Hear ye, hear ye!"):
        self.notifier = notifier
        self.message = message

    def __enter__(self):
        # Don't do anything
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):\
        # TODO deal with exceptions
        self.notify()
        return False

    def notify(self, message=None):
        if message:
            self.message = message
        self.notifier.notify(self.message)
