class Notifier:
    def __init__(self, message):
        self.message = message

    def notify(self):
        print(self.message)


class GmailNotifier(Notifier):
    def notify(self):
        print(self.message)
