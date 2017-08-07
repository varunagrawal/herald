from . import Notifier


class GmailNotifier(Notifier):
    def notify(self):
        print(self.message)

