class Notifier:
    def __init__(self, message):
        self.message = message

    def notify(self, *args, **kwargs):
        pass


class TerminalNotifier(Notifier):
    def __init__(self, message):
        super().__init__(message)
        self.orig_message = message

    def notify(self, message=None):
        if message:
            self.message = message
        else:
            self.message = self.orig_message

        print(self.message)
