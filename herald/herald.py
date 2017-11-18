from notifiers.gmail import GmailNotifier


class Herald:
    def __init__(self, notifier=GmailNotifier, message="Hear ye, hear ye!"):
        self.notifier = notifier
        self.message = message

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.notify()
        return False

    def notify(self, message=None):
        if message:
            self.message = message
        self.notifier.notify(self.message)


if __name__ == "__main__":
    notifier = GmailNotifier(message="This is a test message")
    # notifier = notifiers.TerminalNotifier(message="This should print to the terminal")

    with Herald(notifier, message="Yay the process is now complete!") as herald:
        print("Loooong running process")
