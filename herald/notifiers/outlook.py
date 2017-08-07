from . import Notifier


class OutlookNotifier(Notifier):
    def notify(self):
        raise NotImplementedError

