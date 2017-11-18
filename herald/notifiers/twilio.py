from . import Notifier

class TwilioNotifier(Notifier):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def notify(self, message=None, **kwargs):
        pass