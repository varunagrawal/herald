class Notifier:
    """
    Base notifier class.
    """
    def __init__(self, message):
        self.message = message

    def notify(self, *args, **kwargs):
        """
        Send the notification
        :param args:
        :param kwargs:
        :return: None
        """
        pass


class TerminalNotifier(Notifier):
    """
    Send the notifier to the terminal.
    """
    def __init__(self, message):
        """
        Constructor
        :param message: The default message to use in the notifier.
        """
        super().__init__(message)
        self.default_message = message

    def notify(self, message=None):
        """
        Send the notification.
        :param message: The message to send in the notification.
        :return: None
        """
        if message:
            self.message = message
        else:
            self.message = self.default_message

        print(self.message)
